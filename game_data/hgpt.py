#!/usr/bin/env python2.7

# WIP as new findings come in
# Best to clean up duplicates / optimize once unknowns are solved for

# HGPT converter

# Oddities: 
# im/im124003c.zpt_DECOMPRESSED_CONVERTED has weird alpha
# im/im059800.zpt_DECOMPRESSED: Missing HGPT header id.
# event/bs088.har_EXTRACT/fs_21_01.zpt_DECOMPRESSED: Error: Unknown pp version: 8800!
# event/bs094.har_EXTRACT/fs_21_01.zpt_DECOMPRESSED: Error: Unknown pp version: 8800! (Seems to be 1/4th the color + 8-bit alpha?)

import os
import struct

def read_uint8(file_handle):
	return ord(file_handle.read(1))

def read_uint16(file_handle):
	return struct.unpack('H', file_handle.read(2))[0]

def read_uint32(file_handle):
	return struct.unpack('I', file_handle.read(4))[0]

def varying_skip_read(buffer, offset, nibble_read=False):
	if not nibble_read:
		return buffer[offset]

	byte_offset = int(offset / 2)
	nibble_offset = offset % 2

	byte = ord(buffer[byte_offset])
	return chr((byte >> (4 * nibble_offset)) & 0xF)

def info(input_path):
	with open(input_path, 'rb') as f:
		file_size = os.fstat(f.fileno()).st_size
		print input_path
		print 'File_size:', format(file_size, '08x')

		magic_number = f.read(4)
		if magic_number != 'HGPT':
			raise Exception('Not an HGPT file! Missing HGPT header id.')

		pp_offset = read_uint16(f)
		unknown = read_uint16(f) # Some kind of extension flag? Is 0 in solo pic, 1 in multi-sprite pic

		unknown = read_uint32(f) # 00 00 01 00 in solo pics; 07 00 001 00 in pics with multiple sprites within
		unknown = read_uint32(f) # 00 00 00 00 in solo pics; ff ff ff ff in pics with multiple sprites within

		# Multi-sprite data example:
		# u16?    07 00 # Possibly the # of sprites
		# u16?    13 00 
		# str[8]? 66 30 31 5f 30 31 5f 32 # some kind of name
		# uint16 (start_x, start_y, width, height) coords for the sprites:
		#         01 00 01 00 1c 00 14 00
		#         01 00 3d 00 1c 00 14 00
		#         01 00 79 00 1c 00 14 00
		#         51 00 01 00 48 00 14 00
		#         51 00 3d 00 48 00 14 00
		#         51 00 79 00 48 00 14 00
		#         7f 00 72 00 69 00 4f 00
		#         00 00 00 00
		#         00 00 00 00
		#         00 00 00 00
		##################
		
		# PP header
		f.seek(pp_offset)

		pp_header = f.read(2)
		if pp_header != 'pp':
			raise Exception('Missing pp header!')
		
		pp_version = read_uint16(f)

		if pp_version not in (0x13, 0x14, 0x8800):
			raise Exception('Unknown pp version: %s!' % format(pp_version, '02X'))

		width = read_uint16(f)
		height = read_uint16(f)

		unknown = read_uint32(f) # 00 00 00 00
		unknown = read_uint32(f) # 00 00 00 00

		print 'Resolution: %s x %s' % (width, height)	
		
		# PPD header
		ppd_header = f.read(3)
		if ppd_header != 'ppd':
			raise Exception('Missing ppd header!')

		ppd_version = read_uint8(f)
		if ppd_version not in (0x13, 0x14, 0x00):
			raise Exception('Unknown ppd version: %s!' % format(ppd_version, '02X'))

		if (pp_version & 0xFF) != ppd_version:
			raise Exception('pp version (%s) doesn\'t match ppd version (%s)!' % (format((pp_version & 0xFF) , '02X'), format(ppd_version, '02X')))

		# Figure out number of colors
		if pp_version == 0x13:
			color_total = 256
			tile_width = 16
		elif pp_version == 0x14:
			color_total = 16
			tile_width = 32
		elif pp_version == 0x8800:
			color_total = 0
			tile_width = 16

		another_width = read_uint16(f)
		another_height = read_uint16(f)

		unknown = read_uint32(f) # 00 00 00 00

		tile_aligned_width = read_uint16(f)
		tile_aligned_height = read_uint16(f)
		print 'Actual Tiled Resolution: %s x %s' % (tile_aligned_width, tile_aligned_height)

		ppd_size = read_uint32(f) # Might be an offset. It's off by > 0x20

		print 'Data size: %s' % (ppd_size - 0x20)

		unknown = read_uint32(f) # 00 00 00 00
		unknown = read_uint32(f) # 00 00 00 00
		unknown = read_uint32(f) # 00 00 00 00

		# Image data begins
		tiled_data = f.read(ppd_size - 0x20) # or width * height
		
		# Un-tile
		untiled_data = [0] * (width * height)
		TILE_WIDTH = tile_width
		TILE_HEIGHT = 8
		TILE_SIZE = TILE_WIDTH * TILE_HEIGHT
		TILE_ROW = TILE_SIZE * int(tile_aligned_width / TILE_WIDTH)
		for y in xrange(0, height):
			for x in xrange(0, width):
				tile_y = int(y / TILE_HEIGHT)
				tile_x = int(x / TILE_WIDTH)
				tile_sub_y = y % TILE_HEIGHT
				tile_sub_x = x % TILE_WIDTH
				untiled_data[y * width + x] = varying_skip_read(tiled_data, tile_y * TILE_ROW + tile_x * TILE_SIZE + tile_sub_y * TILE_WIDTH + tile_sub_x, color_total == 16)

		if pp_version != 0x8800:
			# PPC header?
			ppc_header = f.read(4)
			if ppc_header != 'ppc\0':
				raise Exception('Not an HGPT file; missing ppc header!')

			unknown = read_uint32(f) # 00 00 20 00 when 8bit pal index + 32bit color?; 00 00 02 00 when 4bit pal index + 32bit color?
			unknown = read_uint32(f) # 00 00 00 00
			unknown = read_uint32(f) # 00 00 00 00

			palette_data = [0] * color_total
			for i in xrange(0, color_total):
				palette_data[i] = read_uint32(f)

	return True

def convert(input_path, output_path):
	with open(input_path, 'rb') as f:
		file_size = os.fstat(f.fileno()).st_size
		print input_path
		print 'File_size:', format(file_size, '08x')

		magic_number = f.read(4)
		if magic_number != 'HGPT':
			raise Exception('Not an HGPT file! Missing HGPT header id.')

		pp_offset = read_uint16(f)
		unknown = read_uint16(f) # Some kind of extension flag? Is 0 in solo pic, 1 in multi-sprite pic

		unknown = read_uint32(f) # 00 00 01 00 in solo pics; 07 00 001 00 in pics with multiple sprites within
		unknown = read_uint32(f) # 00 00 00 00 in solo pics; ff ff ff ff in pics with multiple sprites within

		# Multi-sprite data example:
		# u16?    07 00 # Possibly the # of sprites
		# u16?    13 00 
		# str[8]? 66 30 31 5f 30 31 5f 32 # some kind of name
		# uint16 (start_x, start_y, width, height) coords for the sprites:
		#         01 00 01 00 1c 00 14 00
		#         01 00 3d 00 1c 00 14 00
		#         01 00 79 00 1c 00 14 00
		#         51 00 01 00 48 00 14 00
		#         51 00 3d 00 48 00 14 00
		#         51 00 79 00 48 00 14 00
		#         7f 00 72 00 69 00 4f 00
		#         00 00 00 00
		#         00 00 00 00
		#         00 00 00 00
		##################
		
		# PP header
		f.seek(pp_offset)

		pp_header = f.read(2)
		if pp_header != 'pp':
			raise Exception('Missing pp header!')
		
		pp_version = read_uint16(f)

		if pp_version not in (0x13, 0x14): #, 0x8800):
			raise Exception('Unknown pp version: %s!' % format(pp_version, '02X'))

		width = read_uint16(f)
		height = read_uint16(f)

		unknown = read_uint32(f) # 00 00 00 00
		unknown = read_uint32(f) # 00 00 00 00

		print 'Resolution: %s x %s' % (width, height)	
		
		# PPD header
		ppd_header = f.read(3)
		if ppd_header != 'ppd':
			raise Exception('Missing ppd header!')

		ppd_version = read_uint8(f)
		if ppd_version not in (0x13, 0x14, 0x00):
			raise Exception('Unknown ppd version: %s!' % format(ppd_version, '02X'))

		if (pp_version & 0xFF)  != ppd_version:
			raise Exception('pp version (%s) doesn\'t match ppd version (%s)!' % (format((pp_version & 0xFF) , '02X'), format(ppd_version, '02X')))

		# Figure out number of colors
		if pp_version == 0x13:
			color_total = 256
			tile_width = 16
		elif pp_version == 0x14:
			color_total = 16
			tile_width = 32
		elif pp_version == 0x8800:
			color_total = 16
			tile_width = 16

		another_width = read_uint16(f)
		another_height = read_uint16(f)

		unknown = read_uint32(f) # 00 00 00 00

		tile_aligned_width = read_uint16(f)
		tile_aligned_height = read_uint16(f)
		print 'Actual Tiled Resolution: %s x %s' % (tile_aligned_width, tile_aligned_height)

		ppd_size = read_uint32(f) # Might be an offset. It's off by > 0x20

		print 'Data size: %s' % (ppd_size - 0x20)

		unknown = read_uint32(f) # 00 00 00 00
		unknown = read_uint32(f) # 00 00 00 00
		unknown = read_uint32(f) # 00 00 00 00

		# Image data begins
		tiled_data = f.read(ppd_size - 0x20) # or width * height
		
		# Un-tile
		untiled_data = [0] * (width * height)
		TILE_WIDTH = tile_width
		TILE_HEIGHT = 8
		TILE_SIZE = TILE_WIDTH * TILE_HEIGHT
		TILE_ROW = TILE_SIZE * int(tile_aligned_width / TILE_WIDTH)
		for y in xrange(0, height):
			for x in xrange(0, width):
				tile_y = int(y / TILE_HEIGHT)
				tile_x = int(x / TILE_WIDTH)
				tile_sub_y = y % TILE_HEIGHT
				tile_sub_x = x % TILE_WIDTH
				untiled_data[y * width + x] = varying_skip_read(tiled_data, tile_y * TILE_ROW + tile_x * TILE_SIZE + tile_sub_y * TILE_WIDTH + tile_sub_x, color_total == 16)

		if pp_version != 0x8800:
			# PPC header?
			ppc_header = f.read(4)
			if ppc_header != 'ppc\0':
				raise Exception('Not an HGPT file; missing ppc header!')

			unknown = read_uint32(f) # 00 00 20 00 when 8bit pal index + 32bit color?; 00 00 02 00 when 4bit pal index + 32bit color?
			unknown = read_uint32(f) # 00 00 00 00
			unknown = read_uint32(f) # 00 00 00 00

			palette_data = [0] * color_total
			for i in xrange(0, color_total):
				palette_data[i] = read_uint32(f)

			# Output
			with open(output_path, 'wb') as w:
				w.write("P7\nWIDTH %s\nHEIGHT %s\nDEPTH 4\nMAXVAL 255\nTUPLTYPE RGB_ALPHA\nENDHDR\n" % (width, height))
				for i in untiled_data:
					rgba = palette_data[ord(i)]
					w.write(chr((rgba >> 0) & 0xFF))
					w.write(chr((rgba >> 8) & 0xFF))
					w.write(chr((rgba >> 16) & 0xFF))
					
					a = (rgba >> 24) & 0xFF
					a_disabled = ((a & 0x80) == 0x80)
					if a_disabled:
						a = 0xFF

					else:
						a = (a << 1) | ((a >> 6) & 1)

					w.write(chr(a))

		else:
			# Output (0x0088 is not working; broken)
			with open(output_path, 'wb') as w:
				w.write("P7\nWIDTH %s\nHEIGHT %s\nDEPTH 4\nMAXVAL 255\nTUPLTYPE RGB_ALPHA\nENDHDR\n" % (width, height))
				for i in untiled_data:
					rgba = ord(i) * 16
					w.write(chr(rgba))
					w.write(chr(rgba))
					w.write(chr(rgba))
					w.write(chr(0xFF))

if __name__ == '__main__':
	import sys
	
	if len(sys.argv) < 3:
		print 'hgpt.py <action> <file>'
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

	elif action in ('-c', '--convert'):
		try:
			output_path = input_path + '_CONVERTED.ppm'
			convert(input_path, output_path)

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	else:
		print 'Error: Unknown action: %s' % action
		sys.exit(-1)

	sys.exit(0)
