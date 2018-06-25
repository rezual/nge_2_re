#!/usr/bin/env python2.7

import os
import common

class WaveEntry(object):
	def __init__(self, content):
		self.content = content

	def get_size(self):
		return len(self.content)

	def get_block_aligned_size(self):
		wave_size = self.get_size()
		return WaveWrapper.BLOCK_SIZE * int((WaveWrapper.BLOCK_SIZE - 1 + wave_size) / WaveWrapper.BLOCK_SIZE)

class WaveWrapper(object):
	# Wave .bin archives align content to 0x800 byte blocks
	BLOCK_SIZE = 0x800

	def __init__(self):
		self.entries = []

	def add_entry(self, content):
		new_entry = WaveEntry(content)
		self.entries.append(new_entry)
		return new_entry

	def get_total_entries(self):
		return len(self.entries)

	def open(self, file_path):
		with open(file_path, 'rb') as f:
			archive_size = common.get_file_size(f)
			while f.tell() < archive_size:
				magic_number = f.read(4)
				if magic_number != 'RIFF':
					raise Exception('Not a WAVE entry!')

				wave_size = common.read_uint32(f) + 8
				f.seek(-8, os.SEEK_CUR)
				
				content = f.read(wave_size)
				new_entry = self.add_entry(content)

				# Find how many blocks are needed to contain wave_size
				# and skip that amount of remaining bytes
				f.seek(new_entry.get_block_aligned_size() - wave_size, os.SEEK_CUR)

	def save(self, file_path):
		print '# Writing %s:' % file_path
		with open(file_path, 'wb') as f:
			counter = 0
			offset = 0
			for entry in self.entries:
				wave_size = entry.get_size()
				block_aligned_size = entry.get_block_aligned_size()
			
				print '#\tWriting entry %s at offset 0x%X, size %s' % (counter, offset, wave_size)
				f.write(entry.content)

				padding_size = block_aligned_size - wave_size
				f.write('\0' * padding_size)
			
				counter += 1
				offset += block_aligned_size
		
	def info(self):
		print '# Wave Archive'
		print '{'

		print '\t"entries": {'
		counter = 0
		offset = 0
		for entry in self.entries:
			wave_size = entry.get_size()
			block_aligned_size = entry.get_block_aligned_size()
			print '\t\t%s: {' % counter
			print '\t\t\t"offset": 0x%X,' % offset
			print '\t\t\t"size": %s' % wave_size
			print '\t\t}'
			counter += 1
			offset += block_aligned_size
		print '\t}'
		print '}'

if __name__ == '__main__':
	import sys

	if len(sys.argv) < 3:
		print 'wave.py <action> <archive.bin>'
		print ''
		print 'wave.py --info <archive.bin>'
		print 'wave.py --unpack <archive.bin>      # Output is dir archive.bin.UNPACK'
		print 'wave.py --pack <archive.bin.UNPACK> # Output is file archive.bin'
		sys.exit(0)

	action = sys.argv[1]
	input_path = sys.argv[2]
	output_path = ''

	if len(input_path) == 0:
		print 'Error: Empty input path provided'
		sys.exit(-1)

	if action in ('-i', '--info'):
		try:
			print '# Infoing %s:' % input_path
			wave_archive = WaveWrapper()
			wave_archive.open(input_path)
			wave_archive.info()

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	elif action in ('-u', '--unpack'):
		try:
			print '# Unpacking %s:' % input_path
			wave_archive = WaveWrapper()
			wave_archive.open(input_path)

			output_path = input_path + '.UNPACK' + os.sep
			if not os.path.exists(output_path):
				os.makedirs(output_path)

			counter = 0
			for entry in wave_archive.entries:
				output_file = output_path + ('%s.wav' % counter)
				print '#\tWriting %s:' % output_file
				with open(output_file, 'wb') as w:
					w.write(entry.content)
				counter += 1

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	elif action in ('-p', '--pack'):
		try:
			print '# Packing %s:' % input_path
			wave_archive = WaveWrapper()

			if input_path[-1] == os.sep:
				output_path = input_path[0:-1]
			else:
				output_path = input_path

			if not output_path.endswith('.UNPACK'):
				print 'Error: input path must have a suffix of .UNPACK'
				sys.exit(-1)
			output_path = output_path[:-7]

			counter = 0
			while True:
				input_file = input_path + ('%s.wav' % counter)
				print '#\tReading %s:' % input_file
				if not os.path.exists(input_file):
					print '#\t\tDoesn\'t exist, no more files to pack'
					break
				with open(input_file, 'rb') as f:
					content = f.read()
				
				wave_archive.add_entry(content)
				counter += 1

			wave_archive.save(output_path)

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	else:
		print 'Error: Unknown action: %s' % action
		sys.exit(-1)

	sys.exit(0)
