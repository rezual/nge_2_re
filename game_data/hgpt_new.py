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
import common

def read_uint8(file_handle):
	return ord(file_handle.read(1))

def read_uint16(file_handle):
	return struct.unpack('H', file_handle.read(2))[0]

def read_uint32(file_handle):
	return struct.unpack('I', file_handle.read(4))[0]

def decode_alpha(encoded_alpha):
	return min(encoded_alpha << 1, 0xFF)

def encode_alpha(alpha):
	return alpha >> 1

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

write_pixel_buffer = None
def write_pixel(file_handle, color, palette_total):
	global write_pixel_buffer

	if palette_total == 256:
		common.write_uint8(file_handle, color)

	elif palette_total == 16:
		"""if write_pixel_buffer is None:
			write_pixel_buffer = read_uint8(file_handle)
			value = write_pixel_buffer & 0xF
			return value

		else:
			value = (write_pixel_buffer & 0xF0) >> 4
			write_pixel_buffer = None
			return value"""
		pass

	elif palette_total is None:
		# Read full RGBA
		#return (read_uint8(file_handle), read_uint8(file_handle), read_uint8(file_handle), decode_alpha(read_uint8(file_handle)))
		pass

class PictureWrapper(object):
	def __init__(self):
		self.pp_header = 0x000005050
		self.ppd_header = 0x000445050
		self.ppc_header = None

		self.unknown_one = 0x0001
		self.unknown_two = None     # 00 00 00 00 in zero-division pictures; ff ff ff ff in pics with multiple divisions

		self.unknown_three = 0x0013  # Only for things with multiple divisions

		self.unknown_four = 0x00000000
		self.unknown_five = 0x00000000

		self.unknown_six = 0x00000000

		self.unknown_seven = 0x00000000
		self.unknown_eight = 0x00000000
		self.unknown_nine = 0x00000000

		self.unknown_ten = 0x0000 	# Only on paletted PSP pictures

		self.unknown_eleven = 0x00000000  # Only on paletted PSP pictures
		self.unknown_twelve = 0x00000000  # Only on paletted PSP pictures

		self.width = 0
		self.height = 0
		self.palette = []
		self.division_name = '\0' * 8
		self.divisions = []
		self.content = []

	def info(self):
		pass

	def save(self, file_path):
		print '# Writing %s:' % file_path
		with open(file_path, 'wb') as f:

			pass

			# Calculate various sizes
			pp_offset = 16

			divisions_padded_size = 0
			divisions_padding = 0
			if len(self.divisions) > 0:
				divisions_size = 12 + len(self.divisions) * 8
				divisions_padded_size = align_size(divisions_size, 8)
				divisions_padding = divisions_padded_size - divisions_size
			pp_offset += divisions_padded_size

			# Write magic header
			f.write('HGPT')

			# Write pp offset
			common.write_uint16(f, pp_offset)

			# Write if has multiple divisions
			common.write_uint16(f, len(self.divisions) > 0)

			# Write number of divisions
			common.write_uint16(f, len(self.divisions))

			# Write unknowns
			common.write_uint16(f, self.unknown_one) # 01 00
			common.write_uint32(f, self.unknown_two) # 00 00 00 00 in zero-division pictures; ff ff ff ff in pics with multiple divisions

			if len(self.divisions) > 0:
				# Write the number of divisions again
				common.write_uint16(f, len(self.divisions))

				# Write unknowns
				common.write_uint16(f, self.unknown_three) # 13 00

				# Write division name
				f.write((self.division_name + '\0' * 8)[0:8])

				# Write divisions
				for division in self.divisions:
					common.write_uint16(f, division[0]) 
					common.write_uint16(f, division[1])
					common.write_uint16(f, division[2])
					common.write_uint16(f, division[3])

				# Add null padding
				# Null padding seems to be based on offset after 0xFFFFFFFF, being divisible by either 8 or 16
				f.write('\0' * divisions_padding)

			# Write PP header
			common.write_uint32(f, self.pp_header)

			# Calculate picture format
			picture_format = (self.pp_header >> 24) & 0xFF

			# Write display dimensions
			common.write_uint16(f, self.width)  # display_width
			common.write_uint16(f, self.height) # display_height

			# Write unknowns
			common.write_uint32(f, self.unknown_four) # 00 00 00 00
			common.write_uint32(f, self.unknown_five) # 00 00 00 00
			
			# Calculate storage resolution
			storage_width = align_size(self.width, 16)
			storage_height = align_size(self.height, 8)

			# Write ppd header
			common.write_uint32(f, self.ppd_header)

			# Write display dimensions again
			common.write_uint16(f, self.width)  # ppd_display_width
			common.write_uint16(f, self.height) # ppd_display_height

			# Write unknowns
			common.write_uint32(f, self.unknown_six) # 00 00 00 00

			# Write ppd storage dimensions
			common.write_uint16(f, storage_width)  # ppd_storage_width
			common.write_uint16(f, storage_height) # ppd_storage_height

			# Calculate bytes per pixel
			bytes_per_pixel = 1
			if picture_format == 0x88:
				bytes_per_pixel = 4

			# Calculate ppd size
			# TODO: Below comment is confusing since what about files with divisions that change header size?
			# In the disassembly, they increment BASE (pointing to the start of the file) by 0x20
			# They then read BASE[0x10], then add the read value to BASE,
			# explaining why it's off by 0x20 (since they already added 0x20 to BASE)
			ppd_size = (storage_width * storage_height * bytes_per_pixel)

			# Write ppd size
			# TODO: Does the divisions count affect ppd size?
			common.write_uint32(f, ppd_size + 0x20)

			# Write unknowns
			common.write_uint32(f, self.unknown_seven)
			common.write_uint32(f, self.unknown_eight)
			common.write_uint32(f, self.unknown_nine)

			# Figure out palette_total
			palette_total = len(self.palette)

			# Figure out tile-width
			if palette_total == 16:
				tile_width = 32
			elif palette_total == 256:
				tile_width = 16
			elif palette_total is None:
				tile_width = 4
			else:
				raise Exception('Unknown palette total, %s' % palette_total)

			# Re-tile
			tiled_data = [0] * (storage_width * storage_height)
			TILE_WIDTH = tile_width
			TILE_HEIGHT = 8
			TILE_SIZE = TILE_WIDTH * TILE_HEIGHT
			TILE_ROW = TILE_SIZE * int(storage_width / TILE_WIDTH)
			for y in xrange(0, self.height):
				for x in xrange(0, self.width):
					tile_y = int(y / TILE_HEIGHT)
					tile_x = int(x / TILE_WIDTH)
					tile_sub_y = y % TILE_HEIGHT
					tile_sub_x = x % TILE_WIDTH
					tiled_data[tile_y * TILE_ROW + tile_x * TILE_SIZE + tile_sub_y * TILE_WIDTH + tile_sub_x] = self.content[y * self.width + x]

			# Write image data
			for y in xrange(0, storage_height):
				for x in xrange(0, storage_width):
					write_pixel(f, tiled_data[y * storage_width + x], palette_total)

			# Wrie palette
			if picture_format == 0x88:
				# There is no palette
				pass

			else:
				# Write ppc header
				common.write_uint32(f, self.ppc_header)

				# Write unknowns
				common.write_uint16(f, self.unknown_ten)

				# Write number of palette entries (but needing to be divided by 8)
				common.write_uint16(f, palette_total / 8)

				# Write unknowns
				common.write_uint32(f, self.unknown_eleven)
				common.write_uint32(f, self.unknown_twelve)

				# Write palette
				for c in self.palette:
					common.write_uint8(f, c[0])
					common.write_uint8(f, c[1])
					common.write_uint8(f, c[2])

					if len(c) >= 4:
						common.write_uint8(f, encode_alpha(c[3]))
					else:
						common.write_uint8(f, encode_alpha(0xFF))

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

					self.divisions.append((division_start_x, division_start_y, division_width, division_height))

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

			self.width = display_width = read_uint16(f)
			self.height = display_height = read_uint16(f)

			self.unknown_four = read_uint32(f) # 00 00 00 00
			self.unknown_five = read_uint32(f) # 00 00 00 00

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

			self.unknown_six = read_uint32(f) # 00 00 00 00

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

			self.unknown_seven = read_uint32(f) # 00 00 00 00
			self.unknown_eight = read_uint32(f) # 00 00 00 00
			self.unknown_nine = read_uint32(f) # 00 00 00 00

			# Image data begins
			if picture_format == 0x88:
				palette_total = None
				self.palette = []

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
				self.unknown_ten = None
				if ps2_version:
					# PS2 version uses a PPD section (used for storing image data) to store palette information
					palette_width = read_uint16(f)
					palette_height = read_uint16(f)
					palette_total = (palette_width * palette_height) / 4
				else:
					# PSP version has an unknown hword
					self.unknown_ten = read_uint16(f) # 00 00

					# Then the number of palette entries (but needing to be multiplied by 8)
					palette_total = read_uint16(f) * 8

				print 'Palette total: %s' % palette_total

				# These two are not present on the PS2 version
				self.unknown_eleven = None
				self.unknown_twelve = None
				if not ps2_version:
					self.unknown_eleven = read_uint32(f) # 00 00 00 00
					self.unknown_twelve = read_uint32(f) # 00 00 00 00

				self.palette = [(read_uint8(f), read_uint8(f), read_uint8(f), decode_alpha(read_uint8(f))) for i in xrange(0, palette_total)]

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

			self.content = [0] * (display_width * display_height)
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
					self.content[y * display_width + x] = tiled_data[tile_y * TILE_ROW + tile_x * TILE_SIZE + tile_sub_y * TILE_WIDTH + tile_sub_x]

	def exportpic(self, file_path):
		# HACK: Extract a division
		# Should really be a JSON instead
		"""
		i=0
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
				flattened_tiled_data = [color_channel for pixel in self.content for color_channel in pixel]
				pw.write_array(w, flattened_tiled_data)
				
			else:
				pw = png.Writer(display_width, display_height, palette=self.palette)
				pw.write_array(w, self.content)

	def importpic(self, file_path):
		# Open picture (Quick implementation that only does 8bpp paletted for now)
		f=png.Reader(filename=file_path)
		pic = f.read()
		self.width = pic[0]
		self.height = pic[1]

		self.content = [c for row in pic[2] for c in row]

		self.palette = pic[3]['palette']

		#with open('test.png', 'wb') as f:
			#if picture_format == 0x88:
			#	pw = png.Writer(display_width, display_height, alpha=True)
			#	flattened_tiled_data = [color_channel for pixel in self.content for color_channel in pixel]
			#	pw.write_array(w, flattened_tiled_data)
			#else:
			#	pw = png.Read(display_width, display_height, palette=self.palette)
			#	pw.write_array(w, self.content)


if __name__ == '__main__':
	import sys
	
	if len(sys.argv) < 3:
		print 'hgpt.py <action> <picture.hpt>'
		print ''
		print 'hgpt.py --info <picture.hpt>'
		print 'hgpt.py --export <picture.hpt> # Output are files picture.hpt.png and picture.hpt.METADATA.json'
		print 'hgpt.py --import <picture.hpt> # Input are files picture.hpt.png and picture.hpt.METADATA.json'
		sys.exit(0)

	action = sys.argv[1]
	input_path = sys.argv[2]
	output_path = ''

	if len(input_path) == 0:
		print 'Error: Empty input path provided'
		sys.exit(-1)


	if action in ('-i', '--info'):
		#try:
			print '# Infoing %s:' % input_path
			picture_wrapper = PictureWrapper()
			picture_wrapper.open(input_path)
			picture_wrapper.info()
			picture_wrapper.importpic('test.png')
			picture_wrapper.save(input_path + '.REMIT')

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
