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
import json
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
		self.ppc_header = 0x000435050

		self.pp_offset = 0x0
		self.pp_format = 0x0

		self.ppd_format = 0x0

		self.ppd_size = 0
		self.calculated_ppd_size = 0

		self.division_size = 0
		self.calculated_division_size_with_8 = 0
		self.calculated_division_size_with_16 = 0

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

		self.warnings = []

		self.width = 0
		self.height = 0
		self.palette = []
		self.division_name = '\0' * 8
		self.divisions = []
		self.content = []

	def warn(self, message):
		# Temporary debug helper to track warning messages in metadata
		self.warning.append(message)
		print message

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

			# Write palette
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

			# Read magic header
			magic_number = f.read(4)
			if magic_number != 'HGPT':
				raise Exception('Not an HGPT file! Missing HGPT header id.')

			# Read pp offset
			self.pp_offset = read_uint16(f)
			if self.pp_offset < 0x10:
				raise Exception('PP offset less than 0x10, PS2 variant not supported!')

			# Read if it has multiple divisions
			has_multiple_divisions = read_uint16(f)
			if has_multiple_divisions not in (0, 1):
				raise Exception('Unknown has_multiple_divisions value: %s' % has_multiple_divisions)

			# Read number of divisions
			number_of_divisions = read_uint16(f)
			if (number_of_divisions == 0 and has_multiple_divisions == 1) or (number_of_divisions != 0 and has_multiple_divisions == 0):
				msg='# Warning: Conflicting values between number_of_divisions (%s) and has_multiple_divisions (%s)' % (number_of_divisions, has_multiple_divisions)
				self.warn(msg)

			# Read unknowns
			self.unknown_one = read_uint16(f) # 01 00
			if self.unknown_one != 0x0001:
				msg='# Warning: UnknownOne is not 0x0001'
				self.warn(msg)
			self.unknown_two = read_uint32(f) # 00 00 00 00 in zero-division pictures; ff ff ff ff in pics with multiple divisions
			if (has_multiple_divisions == 1 and self.unknown_two != 0xFFFFFFFF) or (has_multiple_divisions == 0 and self.unknown_two != 0x00000000):
				msg='# Warning: UnknownTwo (0x%08X) doesn\'t match expected value along with has_multiple_divisions (%s)' % (self.unknown_two, has_multiple_divisions)		
				self.warn(msg)

			# Store the current position (for calculating division padding)
			pre_division_position = f.tell()

			# Load divisions
			if has_multiple_divisions == 1:
				# Read number of divisions (again)
				number_of_divisions_repeat = read_uint16(f)
				if number_of_divisions != number_of_divisions_repeat:
					msg='# Warning: Number of divisions and its repeat don\'t match: 0x%04X != 0x%04X' % (number_of_divisions, number_of_divisions_repeat)
					self.warn(msg)

				# Read unknown
				self.unknown_three = read_uint16(f) # 13 00
				if self.unknown_three != 0x0013:
					msg='# Warning: UnknownThree (0x%X) != 0x0013' % self.unknown_three
					self.warn(msg)

				# Read division name
				self.division_name = (f.read(8) + '\0' * 8)[0:8]

				# Read divisions
				for i in xrange(0, number_of_divisions):
					division_start_x = read_uint16(f) 
					division_start_y = read_uint16(f)
					division_width = read_uint16(f)
					division_height = read_uint16(f)

					self.divisions.append((division_start_x, division_start_y, division_width, division_height))

				# What follows is null padding,
				# which seems to be a number of bytes after self.unknown_two till the end of the section,
				# to the effect that it's divisible by either 8 or 16 - not sure which yet; going with 8 atm

			# Skip to PP header
			f.seek(self.pp_offset)

			# Measure and calculate division size so we can figure out which is correct
			self.division_size = f.tell() - pre_division_position
			self.calculated_division_size_with_8 = 0
			self.calculated_division_size_with_16 = 0
			if has_multiple_divisions == 1:
				calculated_division_size = 12 + len(self.divisions) * 8
				self.calculated_division_size_with_8 = common.align_size(calculated_division_size, 8)
				self.calculated_division_size_with_16 = common.align_size(calculated_division_size, 16)

			# Read pp header
			self.pp_header = read_uint32(f)
			if self.pp_header & 0x000005050 != 0x000005050:
				raise Exception('Missing pp header!')

			# Decipher pp format
			self.pp_format = (self.pp_header >> 24) & 0xFF

			# Read picture display dimensions
			self.width = pp_display_width = read_uint16(f)
			self.height = pp_display_height = read_uint16(f)

			# Read unknowns
			self.unknown_four = read_uint32(f)
			self.unknown_five = read_uint32(f)
			if self.unknown_four != 0:
				msg='# Warning: UnknownFour (0x%08X) is not zero' % self.unknown_four
				self.warn(msg)
			if self.unknown_five != 0:
				msg='# Warning: UnknownFive (0x%08X) is not zero' % self.unknown_five
				self.warn(msg)

			# Read ppd header
			self.ppd_header = read_uint32(f)
			if self.ppd_header & 0x000445050 != 0x000445050:
				raise Exception('Missing ppd header!')

			# Decipher ppd format
			self.ppd_format = self.pp_format = (self.ppd_header >> 24) & 0xFF
			if self.ppd_format not in (0x13, 0x14, 0x00):
				# We don't actually uses the pp format or ppd format,
				# but instead we figure the picture format by skipping to the palette
				# Though, it's still good to know this stuff so we can do it properly
				# sometime later
				msg='# Warning: PPD format (0x%X) is unknown' % self.ppd_format
				self.warn(msg)

			# Read ppd display resolution
			ppd_display_width = read_uint16(f)
			ppd_display_height = read_uint16(f)
			if pp_display_width != ppd_display_width:
				msg='# Warning: PP display width (%s) != PPD display width (%s)' % (pp_display_width, ppd_display_width)
				self.warn(msg)
			if pp_display_height != ppd_display_height:
				msg='# Warning: PP display width (%s) != PPD display width (%s)' % (pp_display_height, ppd_display_height)
				self.warn(msg)

			# Read unknown
			self.unknown_six = read_uint32(f) # 00 00 00 00
			if self.unknown_six != 0:
				msg='# Warning: UnknownSix (0x%08X) is not zero' % self.unknown_six
				self.warn(msg)

			# Read ppd storage resolution
			ppd_storage_width = read_uint16(f)
			ppd_storage_height = read_uint16(f)

			# Calculate storage resolution (using the pp_display resolution)
			# If the ppd_display resolution doesn't match the pp_display resolution,
			# then this is not relevant
			storage_width = align_size(pp_display_width, 16)
			storage_height = align_size(pp_display_height, 8)

			if (storage_width != ppd_storage_width) or (storage_height != ppd_storage_height):
				msg='# Warning: PPD storage resolution (%s x %s) doesn\'t match the calculated storage resolution (%s x %s)' % (ppd_storage_width, ppd_storage_height, storage_width, storage_height)
				self.warn(msg)

			# TODO: Below comment is confusing since what about files with divisions that change header size?
			# In the disassembly, they increment BASE (pointing to the start of the file) by 0x20
			# They then read BASE[0x10], then add the read value to BASE,
			# explaining why it's off by 0x20 (since they already added 0x20 to BASE)
			self.ppd_size = read_uint32(f) - 0x20 # Technically an offset...

			# Adjust ppd_size based on bpp
			bytes_per_pixel = 1
			if self.pp_format == 0x88:
				bytes_per_pixel = 4
				self.ppd_size *= 4

			# Calculate ppd size
			self.calculated_ppd_size = (storage_width * storage_height * bytes_per_pixel)

			# Read unknowns
			self.unknown_seven = read_uint32(f) # 00 00 00 00
			self.unknown_eight = read_uint32(f) # 00 00 00 00
			self.unknown_nine = read_uint32(f) # 00 00 00 00
			if self.unknown_seven != 0:
				msg='# Warning: UnknownSeven (0x%08X) is not zero' % self.unknown_seven
				self.warn(msg)
			if self.unknown_eight != 0:
				msg='# Warning: UnknownEight (0x%08X) is not zero' % self.unknown_eight
				self.warn(msg)
			if self.unknown_nine != 0:
				msg='# Warning: UnknownNine (0x%08X) is not zero' % self.unknown_nine
				self.warn(msg)

			# Skip the image data first, and go right away to the palette data
			# We do this because we're still vague on the details regarding the pixel formats,
			# and the palette is so far the most accurate method
			palette_total = None
			if self.pp_format == 0x88:
				self.palette = []

			else:
				# Skip over the image data and go to the palette
				tiled_image_data_offset = f.tell()
				f.seek(self.ppd_size, os.SEEK_CUR)

				# Read ppc header
				self.ppc_header = read_uint32(f)
				if self.ppc_header & 0x000435050 != 0x000435050:
					raise Exception('Missing ppc header!')

				# Read unknown
				self.unknown_ten = read_uint16(f) # 00 00
				if self.unknown_ten != 0:
					msg='# Warning: UnknownTen (0x%08X) is not zero' % self.unknown_ten
					self.warn(msg)

				# Read the number of palette entries
				# It needs to be multiplied by 8 - forgot as to why
				# (We know there's 4 bytes per color entry but that doesn't explain the other 2x)
				palette_total = read_uint16(f) * 8

				# Read unknowns
				self.unknown_eleven = read_uint32(f) # 00 00 00 00
				if self.unknown_eleven != 0:
					msg='# Warning: UnknownEleven (0x%08X) is not zero' % self.unknown_eleven
					self.warn(msg)
				self.unknown_twelve = read_uint32(f) # 00 00 00 00
				if self.unknown_twelve != 0:
					msg='# Warning: UnknownTwelve (0x%08X) is not zero' % self.unknown_twelve
					self.warn(msg)

				# Read palette
				self.palette = [(read_uint8(f), read_uint8(f), read_uint8(f), decode_alpha(read_uint8(f))) for i in xrange(0, palette_total)]

				# Go back and read the image data now that we know the palette
				f.seek(tiled_image_data_offset)
			
			# Read the tiled image data
			# The image data is stored in a scrambled tiled format, so we'll have to reprocess it	
			tiled_image_data = [read_pixel(f, palette_total) for y in xrange(0, storage_height) for x in xrange(0, storage_width)]

			# The tile width changes depending on the pixel format,
			# but instead of finding the pixel format from the pp/ppd headers,
			# we do it backwards by guessing it from the palette total
			if palette_total == 16:
				tile_width = 32
			elif palette_total == 256:
				tile_width = 16
			elif palette_total is None:
				tile_width = 4
			else:
				raise Exception('Unknown palette total, %s' % palette_total)

			# Un-tile and store the information as the content
			self.content = [0] * (pp_display_width * pp_display_height)
			TILE_WIDTH = tile_width
			TILE_HEIGHT = 8
			TILE_SIZE = TILE_WIDTH * TILE_HEIGHT
			TILE_ROW = TILE_SIZE * int(storage_width / TILE_WIDTH)
			for y in xrange(0, pp_display_height):
				for x in xrange(0, pp_display_width):
					tile_y = int(y / TILE_HEIGHT)
					tile_x = int(x / TILE_WIDTH)
					tile_sub_y = y % TILE_HEIGHT
					tile_sub_x = x % TILE_WIDTH
					self.content[y * pp_display_width + x] = tiled_image_data[tile_y * TILE_ROW + tile_x * TILE_SIZE + tile_sub_y * TILE_WIDTH + tile_sub_x]

	def exportpic(self, file_path):

		output_path_metadata = file_path + '.EXPORT.json'
		output_path_helper = file_path + '.EXPORT.HELPER.png' 
		output_path_picture = file_path + '.EXPORT.png'

		# Write metadata
		metadata = {
			"pp": self.pp_header,
			"ppd": self.ppd_header,
			"ppc": self.ppc_header,

			"pp_offset": self.pp_offset,
			"pp_format": self.pp_format,

			"ppd_format": self.ppd_format,

			"ppd_size": self.ppd_size,
			"calculated_ppd_size": self.calculated_ppd_size,

			"division_size": self.division_size,
			"calculated_division_size_with_8": self.calculated_division_size_with_8,
			"calculated_division_size_with_16": self.calculated_division_size_with_16,

			"unknown_one": self.unknown_one,
			"unknown_two": self.unknown_two,
			"unknown_three": self.unknown_three,
			"unknown_four": self.unknown_four,
			"unknown_five": self.unknown_five,
			"unknown_six": self.unknown_six,
			"unknown_seven": self.unknown_seven,
			"unknown_eight": self.unknown_eight,
			"unknown_nine": self.unknown_nine,
			"unknown_ten": self.unknown_ten,
			"unknown_eleven": self.unknown_eleven,
			"unknown_twelve": self.unknown_twelve,

			"width": self.width,
			"height": self.height,

			"palette_total": len(self.palette),
			"division_name": self.division_name,
			"divisions": self.divisions,

			"warnings": self.warnings
		}

		with open(output_path_metadata, 'wb') as f:
			f.write(json.dumps(metadata, indent=4))

		# Create a divisions helper file
		if (self.divisions):
			# Get background color
			background_color = common.unique_color(-1, None)

			# Create the canvas
			canvas = [background_color] * (self.width * self.height)

			# Loop through divisions, plotting them onto the canvas
			for i, (division_x_pos, division_y_pos, division_width, division_height) in enumerate(self.divisions):
				# Get a unique color
				draw_color = common.unique_color(i, len(self.divisions))

				# Draw an empty square
				try:
					for y in xrange(0, division_height):	
						canvas[(division_y_pos + y) * self.width + (division_x_pos + 0)] = draw_color
						canvas[(division_y_pos + y) * self.width + (division_x_pos + division_width - 1)] = draw_color

					for x in xrange(1, division_width - 1):
						canvas[(division_y_pos + 0) * self.width + (division_x_pos + x)] = draw_color
						canvas[(division_y_pos + division_height - 1) * self.width + (division_x_pos + x)] = draw_color
				except:
					# Ignore all failures
					# Most likely bounds failures
					pass

			# Save resulting canvas
			with open(output_path_helper, 'wb') as f:
				pw = png.Writer(self.width, self.height)
				flattened_helper_data = [color_channel for pixel in canvas for color_channel in pixel]
				pw.write_array(f, flattened_helper_data)
		
		# Output
		with open(output_path_picture, 'wb') as f:
			if self.pp_format == 0x88:
				pw = png.Writer(self.width, self.height, alpha=True)
				flattened_image_data = [color_channel for pixel in self.content for color_channel in pixel]
				pw.write_array(f, flattened_image_data)
				
			else:
				pw = png.Writer(self.width, self.height, palette=self.palette)
				pw.write_array(f, self.content)

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
		print 'hgpt.py --export <picture.hpt> # Output are files picture.hpt.EXPORT.png and picture.hpt.EXPORT.json'
		print 'hgpt.py --import <picture.hpt> # Input are files picture.hpt.EXPORT.png and picture.hpt.EXPORT.json'
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
			#picture_wrapper.importpic('test.png')
			#picture_wrapper.save(input_path + '.REMIT')

		#except Exception, e:
		#	print 'Error: %s' % e
		#	sys.exit(-1)

	elif action in ('-e', '--export'):
		try:
			print '# Exporting %s:' % input_path
			picture_wrapper = PictureWrapper()
			picture_wrapper.open(input_path)

			output_path = input_path

			picture_wrapper.exportpic(output_path)

		except Exception, e:
			print 'Error: %s' % e
			sys.exit(-1)

	else:
		print 'Error: Unknown action: %s' % action
		sys.exit(-1)

	sys.exit(0)
