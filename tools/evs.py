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

class EvsFile(object):
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
			if magic_number != '.EVS':
				raise Exception('Not an EVS file!')

			number_of_entries = read_uint32(f)
			entry_offsets = [0] * number_of_entries

			for i in xrange(0, number_of_entries):
				entry_offsets[i] = read_uint32(f)

			for i in xrange(0, number_of_entries):
				f.seek(entry_offsets[i])

				entry_type = read_uint16(f)
				entry_size = read_uint16(f)

				include_in_output = False
				number_of_parameters = 0 
				if entry_type == 0x01:
					# Japanese text
					number_of_parameters = 3
					
					include_in_output = True

				elif entry_type == 0x02:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x04:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x05:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x07:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x0A:
					# Unknown
					number_of_parameters = 3
				elif entry_type == 0x0D:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x0E:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x11:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x12:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x13:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x14:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x15:
					# Unknown
					number_of_parameters = 3
				elif entry_type == 0x16:
					# Unknown
					number_of_parameters = 3
				elif entry_type == 0x18:
					# Unknown
					number_of_parameters = 3
				elif entry_type == 0x1A:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x1F:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x28:
					# Unknown
					number_of_parameters = 3
				elif entry_type == 0x29:
					# Unknown
					number_of_parameters = 4
				elif entry_type == 0x2A:
					# Unknown
					number_of_parameters = 4
				elif entry_type == 0x2B:
					# Unknown
					number_of_parameters = 3
				elif entry_type == 0x2C:
					# Unknown
					number_of_parameters = 4
				elif entry_type == 0x2E:
					# Unknown
					number_of_parameters = 3
				elif entry_type == 0x2F:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x30:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x31:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x32:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x33:
					# Unknown
					number_of_parameters = 3
				elif entry_type == 0x34:
					# Unknown
					number_of_parameters = 3
				elif entry_type == 0x51:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x52:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x53:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x54:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x56:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x57:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x60:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x65:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x71:
					# Unknown / Terminator?
					number_of_parameters = 0
				elif entry_type == 0x72:
					# Unknown / Terminator?
					number_of_parameters = 0
				elif entry_type == 0x78:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x79:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x7A:
					# Unknown / Terminator?
					number_of_parameters = 0
				elif entry_type == 0x7B:
					# Unknown / Terminator?
					number_of_parameters = 0
				elif entry_type == 0x7D:
					# Unknown / Terminator?
					number_of_parameters = 1
				elif entry_type == 0x85:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x86:
					# Unknown
					number_of_parameters = 0
				elif entry_type == 0x87:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x8C:
					# A .zpt file? (compressed HGPT)
					number_of_parameters = 1
				elif entry_type == 0x8D:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x8E:
					# A .zpt file? (titlet19.zpt)
					number_of_parameters = 1
				elif entry_type == 0x8F:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x90:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x91:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x92:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x93:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x94:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x95:
					# Parameter-less text?
					number_of_parameters = 0
					
					include_in_output = True

				elif entry_type == 0x98:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0x9A:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x9B:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x99:
					# Unknown
					number_of_parameters = 2
				elif entry_type == 0x9E:
					# Unknown
					number_of_parameters = 1
				elif entry_type == 0xA3:
					# A .bin file?
					number_of_parameters = 1
				elif entry_type == 0xA7:
					# Unknown
					number_of_parameters = 3
				elif entry_type == 0xB7:
					# Unknown
					number_of_parameters = 3
				else:
					# Commands that I've yet to document the parameter count for
					include_in_output = False #True		
						
				unknowns = [0] * number_of_parameters
				for j in xrange(0, number_of_parameters):
					unknowns[j] = read_uint32(f)
				size_adjust = 4 * number_of_parameters

				content = f.read(entry_size - size_adjust)
			
				if include_in_output:
					parameters = ', '.join([format(u, '08X') for u in unknowns])
					if parameters != '':
						parameters += ', '
					parameters += json.dumps(content.decode('shift_jis', 'replace').encode('utf-8'), ensure_ascii=False).replace('\\u0000', '\\0')
					print '    0x' + format(i, '08X') + ':', 'func_' + format(entry_type, '04X') + '(' + parameters + ')'

if __name__ == '__main__':
	import sys
	
	if len(sys.argv) < 3:
		print 'evs.py <action> <file.evs>'
		print ''
		print 'evs.py --info <file.evs>'
		print 'evs.py --export <file.evs>'
		sys.exit(0)

	action = sys.argv[1]
	input_path = sys.argv[2]
	output_path = ''

	if len(input_path) == 0:
		print 'Error: Empty input path provided'
		sys.exit(-1)

	if action in ('-i', '--info'):
		#try:
			print '%s:' % input_path
			evs = EvsFile()
			evs.open(input_path)
			#evs.info()
		
		#except Exception, e:
		#	print 'Error: %s' % e
		#	sys.exit(-1)

	else:
		print 'Error: Unknown action: %s' % action
		sys.exit(-1)

	sys.exit(0)
