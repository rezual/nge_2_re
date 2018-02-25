#!/usr/bin/env python2.7

import os
import struct
import json

def read_uint8(file_handle):
	return ord(file_handle.read(1))

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

class TextEntry(object):
	def __init__(self, unknown, string):
		self.unknown = unknown
		self.string = string

class TextString(object):
	def __init__(self, unknown_first, unknown_second, offset, content):
		self.unknown_first = unknown_first
		self.unknown_second = unknown_second
		self.content = content
		self.offset = offset

class Text(object):
	def __init__(self, size):
		self.size = size
		self.entries = []
		self.string_map = {}

	def add_entry(self, unknown, string):
		new_entry = TextEntry(unknown, string)
		self.entries.append(new_entry)
		return new_entry

	def add_string(self, unknown_first, unknown_second, offset, content):
		if offset in self.string_map:
			return self.string_map[offset]
		
		new_string = TextString(unknown_first, unknown_second, offset, content)
		self.string_map[offset] = new_string
		return new_string

	def open(self, f):
		base_offset = f.tell()

		magic_number = f.read(4)
		if magic_number != 'TEXT':
			raise Exception('Not a TEXT file!')

		number_of_entries = read_uint32(f)
		
		header_size = read_uint32(f)
		if (header_size != 16):
			print 'Warning: Non-standard TEXT header size: %s' % header_size
		
		content_start_offset = read_uint32(f)

		f.seek(base_offset + header_size)

		# Entry look up table
		unknown = [0] * number_of_entries
		string_offsets = [0] * number_of_entries
		for i in xrange(0, number_of_entries):
			unknown[i] = read_uint32(f)
			string_offsets[i] = read_uint32(f)

		f.seek(base_offset + content_start_offset)

		# The actual strings (which are used multiple times per entry)
		for i in xrange(0, number_of_entries):
			f.seek(base_offset + string_offsets[i])

			unknown_first = read_uint32(f)
			unknown_second = read_uint32(f)

			# Read content until null-terminator (but aligned to 32-bit boundaries)
			content = ''
			while True:
				content += f.read(4)
				if content[-1] == '\0':
					break

			# Convert Shift JIS to UTF8
			try:
				content = content.decode('shift_jis').encode('utf-8')
			except UnicodeDecodeError: 
				pass

			new_string = self.add_string(unknown_first, unknown_second, string_offsets[i], content)
			new_entry = self.add_entry(unknown[i], new_string)

class Bind(object):
	def __init__(self):
		self.index_size = 4
		self.block_size = 2048
		self.header_size = 16
		self.entries = []

	def add_entry(self, size):
		new_text = Text(size)
		self.entries.append(new_text)
		return new_text

	def open(self, file_path):
		with open(file_path, 'rb') as f:
			file_size = os.fstat(f.fileno()).st_size

			magic_number = f.read(4)
			if magic_number == 'TEXT':
				f.seek(-4, os.SEEK_CUR)
				new_text = self.add_entry(file_size)
				new_text.open(f)
				return

			elif magic_number != 'BIND':
				raise Exception('Not a BIND file!')

			self.index_size = read_uint16(f)
			if self.index_size not in (1, 2, 4):
				raise Exception('Illegal BIND index size: %s' % self.index_size)
			
			number_of_entries = read_uint16(f)
			self.block_size = read_uint32(f)
			self.header_size = read_uint32(f)

			index_sizes = [0] * number_of_entries
			for i in xrange(0, number_of_entries):
				if self.index_size == 1:
					index_sizes[i] = read_uint8(f)

				elif self.index_size == 2:
					index_sizes[i] = read_uint16(f)

				elif self.index_size == 4:
					index_sizes[i] = read_uint32(f)

			index_offsets = [0] * number_of_entries
			index_offsets[0] = self.header_size

			for i in xrange(1, number_of_entries):
				previous_index_offset = index_offsets[i - 1]
				previous_index_size = index_sizes[i - 1]

				previous_index_block_size = self.block_size * int(((self.block_size - 1) + previous_index_size) / self.block_size)

				current_index_offset = previous_index_offset + previous_index_block_size
				index_offsets[i] = current_index_offset

			for i in xrange(0, number_of_entries):
				f.seek(index_offsets[i])

				peek_magic_number = f.read(4)
				f.seek(-4, os.SEEK_CUR)

				if peek_magic_number == 'TEXT':
					new_text = self.add_entry(index_sizes[i])
					new_text.open(f)
				else:
					print 'Warning: Unknown type of entry at offset 0x%s, peek yielded: %s' % (format(f.tell(), '08X'), peek_magic_number)


	def info(self):
		print 'Header Size: %s' % self.header_size
		print 'Number of Entries: %s' % len(self.entries)
		print 'Index Size: %s' % self.index_size
		print 'Block Size: %s' % self.block_size

		print 'Entries:'
		entry_number = 0
		for entry in self.entries:
			print '\tNumber: %s' % entry_number
			entry_number += 1

			print '\tNumber of Sub-Entries: %s' % len(entry.entries)
			print '\tSize: %s' % entry.size

			subentry_number = 0
			for subentry in entry.entries:
				print '\t\tSub-Entry Number: %s' % subentry_number
				subentry_number += 1

				print '\t\tUnknown: 0x%s' % format(subentry.unknown, '08X')
				print '\t\tString offset: 0x%s' % format(subentry.string.offset, '08X')

				print '\t\tUnknown first: 0x%s' % format(subentry.string.unknown_first, '08X')
				print '\t\tUnknown second: 0x%s' % format(subentry.string.unknown_second, '08X')
				print '\t\tContent: %s' % json.dumps(subentry.string.content, ensure_ascii=False).replace('\\u0000', '\\0')

				print ''
	
			print ''

	def export(self, file_path):
		print '#!/usr/bin/env python2.7'
		print '# -*- coding: UTF-8 -*-'
		print ''
		print '# Note:'
		print '# This file contains section-specific untranslated strings'
		print '# Put the translations in the ???'
		print '# \\n is a linebreak'
		print '# \\0 is the end of the string'
		print '# \\\' is a single quote'
		print ''

		print 'strings = ['
		entry_number = 0
		for entry in self.entries:

			# This following code is specific to a TEXT-entry

			# Re-calculate string refs (don't use offsets when exporting)
			ascending_string_offsets = sorted(entry.string_map.keys())
			string_offset_remap = {offset: numeric for numeric, offset in enumerate(ascending_string_offsets)}

			if not entry.entries:
				print '    [],'

			else:
				print '    ['

				for string_offset in ascending_string_offsets:
					string = entry.string_map[string_offset]
					print '        (0x%08X, 0x%08X, \'???\', %s),' % (string.unknown_first, string.unknown_second, json.dumps(string.content, ensure_ascii=False).replace('\\u0000', '\\0')) 

				print '    ],'

			entry_number += 1

		print ']'

		print ''

		print 'mappings = ['
		entry_number = 0
		for entry in self.entries:

			# This following code is specific to a TEXT-entry

			# Re-calculate string refs (don't use offsets when exporting)
			ascending_string_offsets = sorted(entry.string_map.keys())
			string_offset_remap = {offset: numeric for numeric, offset in enumerate(ascending_string_offsets)}

			if not entry.entries:
				print '    [],'

			else:
				print '    ['

				for subentry in entry.entries:
					print '        (0x%08X, strings[%s][%s]),' % (subentry.unknown, entry_number, string_offset_remap[subentry.string.offset])

				print '    ],'

			entry_number += 1

		print ']'

if __name__ == '__main__':
	import sys
	
	if len(sys.argv) < 3:
		print 'bind.py <action> <archive.bin>'
		print ''
		print 'bind.py --info <archive.bin>'
		print 'bind.py --export <archive.bin>'
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
			bind = Bind()
			bind.open(input_path)
			bind.info()
		
		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	elif action in ('-e', '--export'):
		try:
			print 'Opening %s:' % input_path

			bind = Bind()
			bind.open(input_path)
			
			output_path = input_path + '_EXPORT'

			bind.export(output_path)

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	else:
		print 'Error: Unknown action: %s' % action
		sys.exit(-1)

	sys.exit(0)
