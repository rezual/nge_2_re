#!/usr/bin/env python2.7

# HGAR packer/unpacker
# Mass-extract on Windows: forfiles /P C:\path_to\PSP_GAME\USRDIR\ /M *.har /S /C "C:\Python27\python.exe -c C:\path_to\hgar.py --extract @path"
# Mass-extract on Unix: find /path_to/PSP_GAME/USRDIR/ -name '*.har' -exec /path_to/hgar.py --extract {} \;

# TODO: 
# Make is_compressed call zipped.py to unzip (if requested)
# and possibly call hgpt.py as well for .hpt/.zpt files

import os
import struct

def read_uint16(file_handle):
	return struct.unpack('H', file_handle.read(2))[0]

def read_uint32(file_handle):
	return struct.unpack('I', file_handle.read(4))[0]

def write_uint16(file_handle, value):
	return file_handle.write(struct.pack('H', value))

def write_uint32(file_handle, value):
	return file_handle.write(struct.pack('I', value))

def word_aligned_length(length):
	return 4 * int((length + 3) / 4)

class HGArchiveFile(object):
	def __init__(self, name, size):
		self.set_name(name)
		
		self.size = size

		self.encoded_identifier = 0
		self.identifier = 0

		self.unknown_first = None
		self.unknown_last = None

		self.content = ''

	def set_name(self, name):
		self.name = name

		base_name = name
		extension = ''
		if '.' in name:
			(base_name, extension) = name.rsplit('.', 1)

		self.short_name = (base_name[0:min(8, len(base_name))] + ' ' * 8)[0:8] + '.' + (extension + ' ' * 3)[0:3]

		long_name_length = len(name) + 1 # Add 1 for the terminator
		word_aligned_length = 4 * int((long_name_length + 3) / 4)
		self.long_name = (name + '\0\0\0\0')[0:word_aligned_length]
		
	def encode_identifier(self, limit):
		compression_mask = 0
		if self.is_compressed:
			compression_mask = 0x80000000

		for guess_encode in xrange(0x7FFFFFFF, 0, -1):
			xor_mask = guess_encode & 0x7FFFFFFF
			mult_result = 0

			rounds = 6
			while rounds > 0:
				mult_result = ((mult_result ^ xor_mask) * 0x3D09) & 0xFFFFFFFF
				xor_mask >>= 5
				rounds -= 1

			mult_result &= (limit - 1)
			if mult_result == self.identifier:
				self.encoded_identifier = guess_encode | compression_mask
				return

	def decode_identifier(self, limit):
		self.is_compressed = ((self.encoded_identifier >> 31) == 1)

		xor_mask = self.encoded_identifier & 0x7FFFFFFF
		mult_result = 0

		rounds = 6
		while rounds > 0:
			mult_result = ((mult_result ^ xor_mask) * 0x3D09) & 0xFFFFFFFF
			xor_mask >>= 5
			rounds -= 1

		mult_result &= (limit - 1)
		self.identifier = mult_result
		
class HGArchive(object):
	def __init__(self):
		self.version = None
		self.files = []
		self.calculate_identifier_limit()

	def add_file(self, name, size):
		new_file = HGArchiveFile(name, size)
		self.files.append(new_file)
		self.calculate_identifier_limit()
		return new_file

	def get_total_files(self):
		return len(self.files)

	def calculate_identifier_limit(self):
		# This function duplicates what the actual game does
		# to calculate the size of the buffers needed
		# to do * something *.
		# That * something * ties into the encoded_identifier value per file entry.
		# The procedure doesn't make sense,
		# but as long as it's the same thing the game does,
		# then we're good.

		v1 = len(self.files)
		t0 = 0x10
		a1 = 0x8000
		s4 = t0 < v1

		while True:
			a0 = t0
			t0 = t0 << 1
			a3 = a1 < t0

			if (s4 is False):
				break

			s4 = t0 < v1
			if (a3 is False):
				continue
			
			else:
				a0 = 0x8000
				break

		a2 = a0 << 1
		t1 = a2 - 1
		a0 = a0 << 2
		
		# mask = t1
		# alloc = a0
		self.identifier_limit = a2

	def decode_identifiers(self):
		# This must be done once finalizing a HGAR for saving (or after open is complete)
		# since the IDs depend on the # of files in the HGAR
		for file in self.files:
			file.decode_identifier(self.identifier_limit)

	def info(self):
		print 'Version: %s' % self.version
		print 'Number of Files: %s' % len(self.files)
		print 'Number of Files (Hex): 0x%s' % format(len(self.files), '08X')
		print 'Identifier limit:      0x%s' % format(self.identifier_limit, '08X')

		print 'Files:'
		for file in self.files:
			print '\tName: %s' % file.name
			print '\tCompressed: %s' % file.is_compressed
			print '\tUnknown first: 0x%s' % format(file.unknown_first, '08X')
			print '\tUnknown last:  0x%s' % format(file.unknown_first, '08X')
			print '\tEncoded Identifier: 0x%s' % format(file.encoded_identifier, '08X')
			print '\tDecoded Identifier: 0x%s' % format(file.identifier, '08X')
			
			print ''
		
	def replace(self, file_to_replace, file_content):
		for file in self.files:
			if file.name == file_to_replace:
				file.content = file_content
				file.size = len(file_content)
				return

		raise Exception('Could not replace "%s", not found in archive!' % file_to_replace)

	def open(self, file_path):
		with open(file_path, 'rb') as f:
			magic_number = f.read(4)
			if magic_number != 'HGAR':
				raise Exception('Not an HGAR file!')

			self.version = read_uint16(f)
			if self.version not in (1, 3):
				raise Exception('Unknown HGAR version: %s' % self.version)
			
			number_of_files = read_uint16(f)

			file_header_offsets = [0] * number_of_files
			for i in xrange(0, number_of_files):	
				file_header_offsets[i] = read_uint32(f)

			file_unknowns = [(None, None)] * number_of_files
			file_long_names = [None] * number_of_files

			if self.version == 3:
				for i in xrange(0, number_of_files):
					file_unknowns[i] = (read_uint32(f), read_uint32(f))

				for i in xrange(0, number_of_files):
					# Read file number
					file_number = read_uint32(f)

					# Read name until null-terminator (but aligned to 32-bit boundaries)
					long_name = ''
					while True:
						long_name += f.read(4)
						if long_name[-1] == '\0':
							break

					file_long_names[i] = long_name

					if file_number != i:
						print '\tWarning: File "%s" is stored as file number %s, but should be %s' % (long_name, file_number, i)

			for i in xrange(0, number_of_files):
				f.seek(file_header_offsets[i])

				short_name = f.read(0xC)
				reformatted_name = short_name[0:-4].rstrip() + short_name[-4:].rstrip()

				encoded_identifier = read_uint32(f)
				file_size = read_uint32(f)

				new_file = self.add_file(reformatted_name, file_size)
				new_file.encoded_identifier = encoded_identifier

				new_file.unknown_first = file_unknowns[i][0]
				new_file.unknown_last = file_unknowns[i][1]
				
				new_file.content = f.read(file_size)

				# The new file object will generate the short name and long name
				# upon creation, BUT overwrite these since we're opening
				# and know the exact values (instead of creating from scratch)
				new_file.short_name = short_name
				new_file.long_name = file_long_names[i]

			# This must be done after the exact file count is known
			self.decode_identifiers()

	def save(self, file_path):
		with open(file_path, 'wb') as f:
			f.write('HGAR')

			write_uint16(f, self.version)

			number_of_files = self.get_total_files()

			write_uint16(f, number_of_files)

			# Calculate the header size to be able to calculate the file start offsets
			#                Magic + Version + nFiles + FileOffsets   
			size_of_header = 4 +     2 +       2 +      4 * number_of_files
			if self.version == 3:
				#                 Unknowns
				size_of_header += 8 * number_of_files

				# Add long names
				for file in self.files:
					size_of_header += 4 + len(file.long_name)

			# Write file start offsets
			file_offset = size_of_header
			for file in self.files:
				write_uint32(f, file_offset)

				#              ShortName + Identifier + Size
				file_offset += 0xC       + 4 +   4

				# Actual file content
				file_offset += word_aligned_length(file.size)

			if self.version == 3:
				# Write unknowns
				for file in self.files:
					write_uint32(f, file.unknown_first)
					write_uint32(f, file.unknown_last)

				# Write long names
				for number, file in enumerate(self.files):
					write_uint32(f, number)
					f.write(file.long_name)

			for file in self.files:
				# Write short name
				f.write(file.short_name)

				# Write encoded identifier
				#file.encode_identifier(self.identifier_limit)
				write_uint32(f, file.encoded_identifier)

				# Write file size
				write_uint32(f, file.size)

				# Write content
				f.write(file.content)

				# Write padding
				padding_length = 4 - (file.size & 3)
				if padding_length != 4:
					f.write('\0' * padding_length)

if __name__ == '__main__':
	import sys

	if len(sys.argv) < 3:
		print 'hgar.py <action> <archive.har>'
		print ''
		print 'hgar.py --info <archive.har>'
		print 'hgar.py --extract <archive.har>'
		print 'hgar.py --replace <archive.har> <file_to_replace> <file_to_inject>'
		sys.exit(0)

	action = sys.argv[1]
	input_path = sys.argv[2]
	output_path = ''

	if len(input_path) == 0:
		print 'Error: Empty input path provided'
		sys.exit(-1)

	if action in ('-i', '--info'):
		try:
			print 'Opening %s:' % input_path
			hgar = HGArchive()
			hgar.open(input_path)
			hgar.info()

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	elif action in ('-r', '--replace'):

		if len(sys.argv) < 5:
			print 'hgar.py --replace <archive.har> <file_to_replace> <file_to_inject>'
			sys.exit(0)

		file_to_replace = sys.argv[3]
		file_to_inject = sys.argv[4]

		try:
			print 'Opening %s:' % input_path

			hgar = HGArchive()
			hgar.open(input_path)

			print '\tLoading %s' % file_to_inject
			file_content = ''
			with open(file_to_inject, 'rb') as f:
				file_content = f.read()
			
			print '\tReplacing %s' % file_to_replace
			hgar.replace(file_to_replace, file_content)

			hgar.save(input_path + '_REPLACE')

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	elif action in ('-e', '--extract'):
		try:
			print 'Opening %s:' % input_path

			hgar = HGArchive()
			hgar.open(input_path)
			
			output_path = input_path + '_EXTRACT' + os.sep

			if not os.path.exists(output_path):
				os.makedirs(output_path)

			for file in hgar.files:
				print '\tExtracting: ' + file.name

				with open(output_path + file.name, 'wb') as w:
					w.write(file.content)

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	else:
		print 'Error: Unknown action: %s' % action
		sys.exit(-1)

	sys.exit(0)
