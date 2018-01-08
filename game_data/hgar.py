#!/usr/bin/env python2.7

# HGAR packer/unpacker

import os
import struct

class SubFile(object):
	def __init__(self, start):
		self.start = start
		self.end = None

		self.number = None
		self.name = None

def info(input_path):
	with open(input_path, 'rb') as f:
		file_size = os.fstat(f.fileno()).st_size

		magic_number = f.read(4)
		if magic_number != 'HGAR':
			raise Exception('Not an HGAR file!')

		version = struct.unpack('H', f.read(2))[0]
		if version not in (1, 3):
			raise Exception('Unknown HGAR version: %s' % version)
		
		subfiles = []
		number_of_files = struct.unpack('H', f.read(2))[0]

		for i in xrange(0, number_of_files):
			file_start = struct.unpack('I', f.read(4))[0]
			subfiles.append(SubFile(file_start))

		for i in xrange(0, number_of_files):
			if i + 1 >= number_of_files:
				subfiles[i].end = file_size
			else:
				subfiles[i].end = subfiles[i + 1].start
		if version == 3:
			for i in xrange(0, number_of_files):
				unknown = struct.unpack('I', f.read(4))[0]
				unknown = struct.unpack('I', f.read(4))[0]

		if version in (1, 3):
			for i in xrange(0, number_of_files):
				f.seek(subfiles[i].start)

				name = f.read(0xC)
				
				# Remove spaces before extension and after the name itself
				subfiles[i].name = name[0:-4].rstrip() + name[-4:]

		"""elif version == 3:
			for i in xrange(0, number_of_files):
				# Read file number
				subfiles[i].number = struct.unpack('I', f.read(4))[0]

				# Read name until null-terminator (but aligned to 32-bit boundaries)
				name = ''
				while True:
					name += f.read(4)
					if name[-1] == '\0':
						break
				subfiles[i].name = name"""

		print input_path
		for i in xrange(0, number_of_files):
			print '\t' + subfiles[i].name,
			print format(subfiles[i].start, '08x'),
			print format(subfiles[i].end, '08x')

			continue

			with open(subfiles[i].name, 'wb') as w:
				f.seek(subfiles[i].start + 0x14)
				data = f.read(subfiles[i].end - (subfiles[i].start + 0x14))
				w.write(data)

	return True

if __name__ == '__main__':
	import sys
	
	if len(sys.argv) < 3:
		print 'hgar.py <action> <file>'
		sys.exit(0)

	action = sys.argv[1]
	input_path = sys.argv[2]

	if action in ('-i', '--info'):
		try:
			info(input_path)
		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	else:
		print 'Error: Unknown action: %s' % action
		sys.exit(-1)

	sys.exit(0)
