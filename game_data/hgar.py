#!/usr/bin/env python2.7

# WIP as new findings come in
# Best to clean up duplicates / optimize once unknowns are solved for

# HGAR packer/unpacker
# Mass-extract on Windows: forfiles /P C:\path_to\PSP_GAME\USRDIR\ /M *.har /S /C "C:\Python27\python.exe -c C:\path_to\hgar.py --extract @path"
# Mass-extract on Unix: find /path_to/PSP_GAME/USRDIR/ -name '*.har' -exec /path_to/hgar.py --extract {} \;

import os
import struct

class SubFile(object):
	def __init__(self, start):
		self.start = start

		self.unknown_first = None
		self.unknown_second = None

		self.number = None
		self.name = None
		self.long_name = None
		self.unknown_maybe_crc = None
		self.size = None

def read_uint16(file_handle):
	return struct.unpack('H', file_handle.read(2))[0]

def read_uint32(file_handle):
	return struct.unpack('I', file_handle.read(4))[0]

def info(input_path):
	with open(input_path, 'rb') as f:
		file_size = os.fstat(f.fileno()).st_size
		print 'File_size:', format(file_size, '08x')

		magic_number = f.read(4)
		if magic_number != 'HGAR':
			raise Exception('Not an HGAR file!')

		version = read_uint16(f)
		if version not in (1, 3):
			raise Exception('Unknown HGAR version: %s' % version)
		
		subfiles = []
		number_of_files = read_uint16(f)

		for i in xrange(0, number_of_files):
			file_start = read_uint32(f)
			subfiles.append(SubFile(file_start))

		if version == 3:
			for i in xrange(0, number_of_files):
				subfiles[i].unknown_first = read_uint32(f)
				subfiles[i].unknown_second = read_uint32(f)

			for i in xrange(0, number_of_files):
				# Read file number
				subfiles[i].number = read_uint32(f)

				# Read name until null-terminator (but aligned to 32-bit boundaries)
				long_name = ''
				while True:
					long_name += f.read(4)
					if long_name[-1] == '\0':
						break
				subfiles[i].long_name = long_name

		if version in (1, 3):
			for i in xrange(0, number_of_files):
				f.seek(subfiles[i].start)

				name = f.read(0xC)
				
				# Remove spaces before extension and after the extension
				subfiles[i].name = name[0:-4].rstrip() + name[-4:].rstrip()
				subfiles[i].unknown_maybe_crc = read_uint32(f)
				subfiles[i].size = read_uint32(f)

		print input_path
		for i in xrange(0, number_of_files):
			print '\t' + subfiles[i].name,
			print 'start:', format(subfiles[i].start , '08x'), #+ 0x14
			print 'size:', format(subfiles[i].size, '08x')

	return True

def extract(input_path, output_path):
	with open(input_path, 'rb') as f:
		file_size = os.fstat(f.fileno()).st_size

		magic_number = f.read(4)
		if magic_number != 'HGAR':
			raise Exception('Not an HGAR file!')

		version = read_uint16(f)
		if version not in (1, 3):
			raise Exception('Unknown HGAR version: %s' % version)
		
		subfiles = []
		number_of_files = read_uint16(f)

		for i in xrange(0, number_of_files):
			file_start = read_uint32(f)
			subfiles.append(SubFile(file_start))

		if version == 3:
			for i in xrange(0, number_of_files):
				subfiles[i].unknown_first = read_uint32(f)
				subfiles[i].unknown_second = read_uint32(f)

			for i in xrange(0, number_of_files):
				# Read file number
				subfiles[i].number = read_uint32(f)

				# Read name until null-terminator (but aligned to 32-bit boundaries)
				long_name = ''
				while True:
					long_name += f.read(4)
					if long_name[-1] == '\0':
						break
				subfiles[i].long_name = long_name

		if version in (1, 3):
			for i in xrange(0, number_of_files):
				f.seek(subfiles[i].start)

				name = f.read(0xC)
				
				# Remove spaces before extension and after the extension
				subfiles[i].name = name[0:-4].rstrip() + name[-4:].rstrip()
				subfiles[i].unknown_maybe_crc = read_uint32(f)
				subfiles[i].size = read_uint32(f)

		print input_path

		if not os.path.exists(output_path):
			os.makedirs(output_path)

		for i in xrange(0, number_of_files):
			print '\tExtracting: ' + subfiles[i].name,
			print format(subfiles[i].start + 0x14, '08x'),
			print format(subfiles[i].size, '08x')

			with open(output_path + subfiles[i].name, 'wb') as w:
				f.seek(subfiles[i].start + 0x14)
				data = f.read(subfiles[i].size)
				w.write(data)

	return True

if __name__ == '__main__':
	import sys
	
	if len(sys.argv) < 3:
		print 'hgar.py <action> <file>'
		sys.exit(0)

	action = sys.argv[1]
	input_path = sys.argv[2]
	output_path = ''

	if len(input_path) == 0:
		print 'Error: Empty input path provided'
		sys.exit(-1)

	if action in ('-i', '--info'):
		try:
			info(input_path)

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	elif action in ('-e', '--extract'):
		try:
			if input_path[-1] == os.pathsep:
				output_path = input_path[:-1] + '_EXTRACT' + os.sep
			else:
				output_path = input_path + '_EXTRACT' + os.sep

			extract(input_path, output_path)

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	else:
		print 'Error: Unknown action: %s' % action
		sys.exit(-1)

	sys.exit(0)
