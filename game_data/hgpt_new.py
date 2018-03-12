#!/usr/bin/env python2.7

# WIP as new findings come in
# Best to clean up duplicates / optimize once unknowns are solved for

# HGPT converter

# Oddities: 
# im/im124003c.zpt_DECOMPRESSED_CONVERTED has weird alpha
# im/im059800.zpt_DECOMPRESSED: Is an HGMT file - which seems to be an untiled, HPT file but without the magic numbers
# event/bs088.har_EXTRACT/fs_21_01.zpt_DECOMPRESSED: Error: Unknown pp version: 8800!
# event/bs094.har_EXTRACT/fs_21_01.zpt_DECOMPRESSED: Error: Unknown pp version: 8800! (Seems to be 1/4th the color + 8-bit alpha?)

import os
import struct
import png

def read_uint8(file_handle):
	return ord(file_handle.read(1))

def read_uint16(file_handle):
	return struct.unpack('H', file_handle.read(2))[0]

def read_uint32(file_handle):
	return struct.unpack('I', file_handle.read(4))[0]

def decode_alpha(encoded_alpha):
	return min(encoded_alpha << 1, 0xFF)

def align_size(unaligned_size, alignment):
	return alignment * int((unaligned_size + alignment - 1) / alignment)

read_pixel_buffer = None
def read_pixel(file_handle, palette_total):
	global read_pixel_buffer

	if palette_total == 256:
		return read_uint8(file_handle)

	elif palette_total == 16:
		if read_pixel_buffer is None:
			read_pixel_buffer = read_uint8(file_handle)
			value = read_pixel_buffer & 0xF
			return value

		else:
			value = (read_pixel_buffer & 0xF0) >> 4
			read_pixel_buffer = None
			return value

	elif palette_total is None:
		# Read full RGBA
		return (read_uint8(file_handle), read_uint8(file_handle), read_uint8(file_handle), decode_alpha(read_uint8(file_handle)))

class HGPicture(object):
	def __init__(self):
		self.pp_header = 0x000005050
		self.ppd_header = None
		self.ppc_header = None

		self.unknown_one = 1
		self.unknown_two = None

		self.unknown_three = None
		self.unknown_four = None

		self.unknown_five = None

		self.unknown_six = None
		self.unknown_seven = None
		self.unknown_eight = None

		self.unknown_nine = None

		self.unknown_ten = None
		self.unknown_eleven = None

		self.palette = []
	
	def open(self, file_path):
		with open(file_path, 'rb') as f:
			file_size = os.fstat(f.fileno()).st_size

			# Not exposed to users, but for development purposes
			ps2_version = False

			magic_number = f.read(4)
			if magic_number != 'HGPT':
				raise Exception('Not an HGPT file! Missing HGPT header id.')

			pp_offset = read_uint16(f)
			has_multiple_divisions = read_uint16(f)

			if has_multiple_divisions not in (0, 1):
				raise Exception('Unknown has_multiple_divisions value: %s' % has_multiple_divisions)
			print 'Has multiple divisions: %s' % (has_multiple_divisions == 1)

			if pp_offset < 0x10:
				raise Exception('PP offset less than 0x10, PS2 variant not supported!')

			number_of_divisions = read_uint16(f)
			self.unknown_one = read_uint16(f) #  01 00

			self.unknown_two = read_uint32(f) # 00 00 00 00 in zero-division pictures; ff ff ff ff in pics with multiple divisions

			divisions = []
			if has_multiple_divisions == 1:
				number_of_divisions_repeat = read_uint16(f)
				self.unknown_three = read_uint16(f) # 13 00

				if self.unknown_three != 0x0013:
					print 'Warning: Unknown #3 != 0x0013'

				if number_of_divisions != number_of_divisions_repeat:
					print 'Warning: Number of divisions and it\'s repeat don\'t match: 0x%04X != 0x%04X' % (number_of_divisions, number_of_divisions_repeat)

				name = f.read(8)

				for i in xrange(0, number_of_divisions):
					division_start_x = read_uint16(f) 
					division_start_y = read_uint16(f)
					division_width = read_uint16(f)
					division_height = read_uint16(f)

					divisions.append((division_start_x, division_start_y, division_width, division_height))

				# Null padding seems to be based on offset after 0xFFFFFFFF, being divisible by either 8 or 16

				for i in divisions:
					print i
			
			# PP header
			f.seek(pp_offset)

			self.pp_header = read_uint32(f)
			if self.pp_header & 0x000005050 != 0x000005050:
				raise Exception('Missing pp header!')

			print 'PP header: 0x%08X' % self.pp_header
			
			picture_format = (self.pp_header >> 24) & 0xFF
			print 'Picture format: %02X' % picture_format

			display_width = read_uint16(f)
			display_height = read_uint16(f)

			self.unknown_three = read_uint32(f) # 00 00 00 00
			self.unknown_four = read_uint32(f) # 00 00 00 00

			print 'Display Resolution: %s x %s' % (display_width, display_height)
			
			# Calculate storage resolution
			storage_width = align_size(display_width, 16)
			storage_height = align_size(display_height, 8)

			print 'On-Disk Resolution: %s x %s' % (storage_width, storage_height)

			# PPD header
			self.ppd_header = read_uint32(f)
			if self.ppd_header & 0x000445050 != 0x000445050:
				raise Exception('Missing ppd header!')

			print 'PPD header: 0x%08X' % self.ppd_header

			"""ppd_version = read_uint8(f)
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
				tile_width = 16"""

			ppd_display_width = read_uint16(f)
			ppd_display_height = read_uint16(f)
			print 'PPD Display Resolution: %s x %s' % (ppd_display_width, ppd_display_height)

			self.unknown_five = read_uint32(f) # 00 00 00 00

			ppd_storage_width = read_uint16(f)
			ppd_storage_height = read_uint16(f)
			print 'PPD Storage Resolution: %s x %s' % (ppd_storage_width, ppd_storage_height)

			# In the disassembly, they increment BASE (pointing to the start of the file) by 0x20
			# They then read BASE[0x10], then add the read value to BASE,
			# explaining why it's off by 0x20 (since they already added 0x20 to BASE)
			ppd_size = read_uint32(f) - 0x20 # Technically an offset...

			# Adjust ppd_size based on bpp
			bytes_per_pixel = 1
			if picture_format == 0x88:
				bytes_per_pixel = 4
				ppd_size *= 4

			print 'Calculated PPD size: %s' % (storage_width * storage_height * bytes_per_pixel)
			print 'Stored PPD size:     %s' % ppd_size

			unknown_six = read_uint32(f) # 00 00 00 00
			unknown_seven = read_uint32(f) # 00 00 00 00
			unknown_eight = read_uint32(f) # 00 00 00 00

			# Image data begins
			if picture_format == 0x88:
				palette_total = None

			else:
				tiled_data_offset = f.tell()
				f.seek(ppd_size, os.SEEK_CUR)

				# PPD or PPC header
				# Read palette total
				self.ppc_header = read_uint32(f)
				if self.ppc_header & 0x000475050 not in (0x000445050, 0x000435050):
					print f.tell()
					raise Exception('Missing ppd/ppc header!')

				print 'PPC header: 0x%08X' % self.ppc_header

				palette_total = 0
				self.unknown_nine = None
				if ps2_version:
					# PS2 version uses a PPD section (used for storing image data) to store palette information
					palette_width = read_uint16(f)
					palette_height = read_uint16(f)
					palette_total = (palette_width * palette_height) / 4
				else:
					# PSP version has an unknown hword
					self.unknown_nine = read_uint16(f) # 00 00

					# Then the number of palette entries (but needing to be multiplied by 8)
					palette_total = read_uint16(f) * 8

				print 'Palette total: %s' % palette_total

				# These two are not present on the PS2 version
				self.unknown_ten = None
				self.unknown_eleven = None
				if not ps2_version:
					self.unknown_ten = read_uint32(f) # 00 00 00 00
					self.unknown_eleven = read_uint32(f) # 00 00 00 00

				palette_data = [(read_uint8(f), read_uint8(f), read_uint8(f), decode_alpha(read_uint8(f))) for i in xrange(0, palette_total)]

				# Go back and read the image data now that we know the palette
				f.seek(tiled_data_offset)
			
			# Read the image data				
			tiled_data = [read_pixel(f, palette_total) for y in xrange(0, storage_height) for x in xrange(0, storage_width)]

			# Un-tile
			if palette_total == 16:
				tile_width = 32
			elif palette_total == 256:
				tile_width = 16
			elif palette_total is None:
				tile_width = 4
			else:
				raise Exception('Unknown palette total, %s' % palette_total)

			untiled_data = [0] * (display_width * display_height)
			TILE_WIDTH = tile_width
			TILE_HEIGHT = 8
			TILE_SIZE = TILE_WIDTH * TILE_HEIGHT
			TILE_ROW = TILE_SIZE * int(storage_width / TILE_WIDTH)
			for y in xrange(0, display_height):
				for x in xrange(0, display_width):
					tile_y = int(y / TILE_HEIGHT)
					tile_x = int(x / TILE_WIDTH)
					tile_sub_y = y % TILE_HEIGHT
					tile_sub_x = x % TILE_WIDTH
					untiled_data[y * display_width + x] = tiled_data[tile_y * TILE_ROW + tile_x * TILE_SIZE + tile_sub_y * TILE_WIDTH + tile_sub_x]

			tiled_data = untiled_data

			# HACK: Extract a division
			"""i=0
			sx = divisions[i][0]
			sy = divisions[i][1]
			xw = divisions[i][2]
			yh = divisions[i][3]

			untiled_data = [0] * (xw * yh)
			for y in xrange(0, yh):
				for x in xrange(0, xw):
					untiled_data[y * xw + x] = tiled_data[(sy + y) * display_width + (sx + x)]

			display_width = xw
			display_height = yh

			tiled_data = untiled_data"""

			# Output
			with open('test.png', 'wb') as w:
				if picture_format == 0x88:
					pw = png.Writer(display_width, display_height, alpha=True)
					flattened_tiled_data = [color_channel for pixel in tiled_data for color_channel in pixel]
					pw.write_array(w, flattened_tiled_data)
					
				else:
					pw = png.Writer(display_width, display_height, palette=palette_data)
					pw.write_array(w, tiled_data)


if __name__ == '__main__':
	import sys
	
	if len(sys.argv) < 3:
		print 'hgpt.py <action> <picture.hpt>'
		print ''
		print 'hgpt.py --info <picture.hpt>'
		print 'hgpt.py --convert <picture.hpt>'
		print 'hgpt.py --replace <picture.hpt> <index_to_replace> <file_to_inject>'
		sys.exit(0)

	action = sys.argv[1]
	input_path = sys.argv[2]
	output_path = ''

	if len(input_path) == 0:
		print 'Error: Empty input path provided'
		sys.exit(-1)

	if action in ('-i', '--info'):
		#try:
			print 'Opening %s:' % input_path
			hgpt = HGPicture()
			hgpt.open(input_path)
			#hgpt.info()

		#except Exception, e:
		#	print 'Error: %s' % e
		#	sys.exit(-1)

	elif action in ('-c', '--convert'):
		"""try:
			output_path = input_path + '_CONVERTED.ppm'
			convert(input_path, output_path)

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)"""
		pass

	else:
		print 'Error: Unknown action: %s' % action
		sys.exit(-1)

	sys.exit(0)
