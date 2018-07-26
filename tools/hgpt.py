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

def decode_alpha(encoded_alpha):
    return min(encoded_alpha << 1, 0xFF)

def encode_alpha(alpha):
    return alpha >> 1

write_pixel_buffer = None
def write_pixel(file_handle, color, palette_total):
    global write_pixel_buffer

    if palette_total == 256:
        common.write_uint8(file_handle, color)

    elif palette_total == 16:
        """if write_pixel_buffer is None:
            write_pixel_buffer = common.read_uint8(file_handle)
            value = write_pixel_buffer & 0xF
            return value

        else:
            value = (write_pixel_buffer & 0xF0) >> 4
            write_pixel_buffer = None
            return value"""
        pass

    elif palette_total is None:
        # Read full RGBA
        #return (common.read_uint8(file_handle), 
        #common.read_uint8(file_handle), 
        #common.read_uint8(file_handle), 
        #decode_alpha(common.read_uint8(file_handle)))
        pass

class PictureWrapper(object):
    def __init__(self):
        self.has_extended_header = True

        self.unknown_two = None     # 00 00 00 00 in zero-division pictures; ff ff ff ff in pics with multiple divisions
        self.unknown_three = 0x0013  # Only for things with multiple divisions

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

            # Calculate various sizes
            pp_offset = 16

            # Divisions sizes
            divisions_padded_size = 0
            divisions_padding = 0
            if self.has_extended_header:
                divisions_size = 12 + len(self.divisions) * 8
                divisions_padded_size = common.align_size(divisions_size, 16)
                divisions_padding = divisions_padded_size - divisions_size
            pp_offset += divisions_padded_size

            # Figure out palette_total
            palette_total = len(self.palette)

            # Set values that depend on the palette total
            pp_format = 0x13
            bytes_per_pixel = 1
            tile_width = 16

            if palette_total == 0:
                pp_format = 0x8800
                bytes_per_pixel = 4
                tile_width = 4

            elif palette_total == 16:
                pp_format = 0x14
                bytes_per_pixel = 0.5
                tile_width = 32
            
            elif palette_total == 256:
                pp_format = 0x13
                bytes_per_pixel = 1
                tile_width = 16

            else:
                raise Exception('Unknown palette total, %s' % palette_total)
            
            # Set values that depend on the display resolution
            ppd_sixteenths_width = common.align_size(self.width, 16)
            ppd_sixteenths_height = common.align_size(self.height, 8)

            storage_width = common.align_size(self.width, tile_width)
            storage_height = common.align_size(self.height, 8)

            number_of_pixels = calculated_storage_width * calculated_storage_height

            # The size also includes the PPD header in the count, which is 0x20 bytes in size, add it
            ppd_size = (storage_width * storage_height * bytes_per_pixel) + 0x20

            # Calculate headers
            pp_header  = 0x00007070 | (pp_format << 16) & 0xFFFF
            ppd_header = 0x00647070 | (pp_format << 24) & 0xFF
            ppc_header = 0x00637070

            # Write magic header
            f.write('HGPT')

            # Write pp offset
            common.write_uint16(f, pp_offset)

            # Write if has extended header
            common.write_uint16(f, 1 if self.has_extended_header else 0)

            # Write number of divisions
            common.write_uint16(f, len(self.divisions))

            # Write unknowns
            common.write_uint16(f, 0x0001)

            # ff ff ff ff in pics with extended header; 00 00 00 00 in pictures w/o extended header; 
            common.write_uint32(f, 0xFFFFFFFF if self.has_extended_header else 0x00000000)
            
            if self.has_extended_header:
                # Write the number of divisions again
                common.write_uint16(f, len(self.divisions))

                # Write unknowns
                common.write_uint16(f, self.unknown_three) # 13 00 or 14 00

                # Write division name
                f.write((self.division_name + '\0' * 8)[0:8])

                # Write divisions
                for division in self.divisions:
                    common.write_uint16(f, division[0]) 
                    common.write_uint16(f, division[1])
                    common.write_uint16(f, division[2])
                    common.write_uint16(f, division[3])

                # Add zero padding
                f.write('\0' * divisions_padding)

            # Write PP header
            common.write_uint32(f, pp_header)

            # Write display dimensions
            common.write_uint16(f, self.width)  # display_width
            common.write_uint16(f, self.height) # display_height

            # Write zero padding
            f.write('\0' * 8)
            
            # Write ppd header
            common.write_uint32(f, ppd_header)

            # Write display dimensions again
            common.write_uint16(f, self.width)  # ppd_display_width
            common.write_uint16(f, self.height) # ppd_display_height

            # Write zero padding
            f.write('\0' * 4)

            # Write ppd sixteenths dimensions
            common.write_uint16(f, ppd_sixteenths_width)
            common.write_uint16(f, ppd_sixteenths_height)

            # Write ppd_size
            common.write_uint32(f, ppd_size)

            # Write zero padding
            f.write('\0' * 12)

            # Figure out palette_total
            palette_total = len(self.palette)

            # Re-tile
            tiled_data = [0] * number_of_pixels
            tile_width = tile_width
            tile_height = 8
            tile_size = tile_width * tile_height
            tile_row = tile_size * int(storage_width / tile_width)
            for y in xrange(0, self.height):
                for x in xrange(0, self.width):
                    tile_y = int(y / tile_height)
                    tile_x = int(x / tile_width)
                    tile_sub_y = y % tile_height
                    tile_sub_x = x % tile_width
                    tiled_data[tile_y * tile_row + tile_x * tile_size + tile_sub_y * tile_width + tile_sub_x] = self.content[y * self.width + x]

            # Write image data
            for y in xrange(0, storage_height):
                for x in xrange(0, storage_width):
                    write_pixel(f, tiled_data[y * storage_width + x], palette_total)

            # Write palette
            if pp_format == 0x8800:
                # There is no palette
                pass

            else:
                # Write ppc header
                common.write_uint32(f, ppc_header)

                # Write zero padding
                f.write('\0' * 2)

                # Write number of palette entries (but needing to be divided by 8)
                common.write_uint16(f, palette_total / 8)

                # Write zero padding
                f.write('\0' * 8)

                # Write palette
                for c in self.palette:
                    common.write_uint8(f, c[0])
                    common.write_uint8(f, c[1])
                    common.write_uint8(f, c[2])
                    common.write_uint8(f, encode_alpha(c[3]))

    def open(self, file_path):
        with open(file_path, 'rb') as f:
            file_size = common.get_file_size(f)

            # Read magic header
            magic_number = f.read(4)
            if magic_number != 'HGPT':
                raise Exception('Not an HGPT file! Missing HGPT header id.')

            # Read pp offset
            pp_offset = common.read_uint16(f)
            if pp_offset < 0x10:
                raise Exception('PP offset less than 0x10, PS2 variant not supported!')

            # Read if it has extended header
            has_extended_header = common.read_uint16(f)
            if has_extended_header not in (0, 1):
                raise Exception('Unknown has_extended_header value: %s' % has_extended_header)
            self.has_extended_header = has_extended_header = (has_extended_header == 1)

            # Read number of divisions
            number_of_divisions = common.read_uint16(f)
            
            # Read unknowns
            unknown_one = common.read_uint16(f)
            if unknown_one != 0x0001:
                raise Exception('First unknown is not 0x0001: %08X' % unknown_one)

            unknown_two = common.read_uint32(f)
            # 00 00 00 00 in pics without extended header
            # ff ff ff ff in pics with extended header
            # 00 f0 00 00 in /USRDIR/game/system.har/dbgfont.zmt
            
            # Load divisions
            if has_extended_header == 1:
                # Read number of divisions (again)
                number_of_divisions_repeat = common.read_uint16(f)
                if number_of_divisions != number_of_divisions_repeat:
                    raise Exception('Number of divisions and its repeat don\'t match: %s != %s' % (number_of_divisions, number_of_divisions_repeat))

                # Read unknown
                unknown_three = common.read_uint16(f) # 13 00
                if unknown_three != 0x0013:
                    print '# Warning: UnknownThree (0x%X) != 0x0013' % unknown_three

                # Read division name
                self.division_name = (f.read(8) + '\0' * 8)[0:8]

                # Read divisions
                for i in xrange(0, number_of_divisions):
                    division_start_x = common.read_uint16(f) 
                    division_start_y = common.read_uint16(f)
                    division_width = common.read_uint16(f)
                    division_height = common.read_uint16(f)

                    self.divisions.append((division_start_x, division_start_y, division_width, division_height))

                # Calculate and skip zero padding
                divisions_size = 12 + 8 * number_of_divisions
                divisions_padded_size = common.align_size(divisions_size, 16)
                divisions_padding = divisions_padded_size - divisions_size

                f.seek(divisions_padding, os.SEEK_CUR)

            # Skip to PP header
            if f.tell() != pp_offset:
                raise Exception('Incorrect pp offset')

            # Read pp header
            pp_header = common.read_uint32(f)
            if pp_header & 0x0000FFFF != 0x00007070:
                raise Exception('Missing pp header! %08X' % pp_header)

            # Decipher pp format
            pp_format = (pp_header >> 16) & 0xFFFF
            if pp_format not in (0x13, 0x14, 0x8800):
                raise Exception('PP format (0x%X) is unknown' % pp_format)

            # Set values that depend on the pp format
            bytes_per_pixel = 1
            tile_width = 16

            if pp_format == 0x8800:
                bytes_per_pixel = 4
                tile_width = 4

            elif pp_format == 0x13:
                bytes_per_pixel = 1
                tile_width = 16

            elif pp_format == 0x14:
                bytes_per_pixel = 0.5
                tile_width = 32

            # Read picture display dimensions
            self.width = pp_display_width = common.read_uint16(f)
            self.height = pp_display_height = common.read_uint16(f)

            # Skip zero padding
            f.seek(2 * 4, os.SEEK_CUR)

            # Read ppd header
            ppd_header = common.read_uint32(f)
            if ppd_header & 0x00FFFFFF != 0x00647070:
                raise Exception('Missing ppd header!')

            # Decipher ppd format
            ppd_format = (ppd_header >> 24) & 0xFF
            if ppd_format != (pp_format & 0xFF):
                raise Exception('PPD format (0x%X) does not match PP format (0x%X)' % (ppd_format, pp_format & 0xFF))

            # Read ppd display resolution
            ppd_display_width = common.read_uint16(f)
            ppd_display_height = common.read_uint16(f)

            if pp_display_width != ppd_display_width:
                raise Exception('PP display width (%s) != PPD display width (%s)' % (pp_display_width, ppd_display_width))
                
            if pp_display_height != ppd_display_height:
                raise Exception('PP display height (%s) != PPD display height (%s)' % (pp_display_height, ppd_display_height))

            # Skip zero padding
            f.seek(4, os.SEEK_CUR)

            # Read ppd sixteenths resolution
            ppd_sixteenths_width = common.read_uint16(f)
            ppd_sixteenths_height = common.read_uint16(f)

            # Calculate ppd sixteenths resolution (using the pp_display resolution)
            calculated_sixteenths_width = common.align_size(pp_display_width, 16)
            calculated_sixteenths_height = common.align_size(pp_display_height, 8)

            if (calculated_sixteenths_width != ppd_sixteenths_width) or (calculated_sixteenths_height != ppd_sixteenths_height):
                raise Exception('PPD sixteenths resolution (%s x %s) doesn\'t match the calculated eights resolution (%s x %s)' % (ppd_sixteenths_width, ppd_sixteenths_height, calculated_sixteenths_width, calculated_sixteenths_height))

            # Calculate storage resolution (using the pp_display resolution)
            # This is the resolution that ties in with the ppd_size
            calculated_storage_width = common.align_size(pp_display_width, tile_width)
            calculated_storage_height = common.align_size(pp_display_height, 8)

            number_of_pixels = calculated_storage_width * calculated_storage_height

            # Read ppd_size which is the size of the ppd section
            # The size also includes the PPD header in the count, which is 0x20 bytes in size, subtract it
            ppd_size = common.read_uint32(f) - 0x20

            # Skip padding
            f.seek(3 * 4, os.SEEK_CUR)

            # Read the tiled image data
            # The image data is stored in a scrambled tiled format, so we'll have to reprocess it   
            tiled_image_data = [0] * number_of_pixels

            cache_last_pixel = None
            number_of_bytes = ppd_size
            for i in xrange(0, number_of_pixels):
                if number_of_bytes <= 0:
                    break

                if pp_format == 0x13:
                    tiled_image_data[i] = common.read_uint8(f)
                    number_of_bytes -= 1

                elif pp_format == 0x14:
                    if (i & 1) == 0:
                        # Even read
                        cache_last_pixel = common.read_uint8(f) 
                    else:
                        # Odd read
                        number_of_bytes -= 1

                    tiled_image_data[i] = cache_last_pixel & 0xF
                    cache_last_pixel = cache_last_pixel >> 4

                elif pp_format == 0x8800:
                    # Read full RGBA
                    tiled_image_data[i] = (
                            common.read_uint8(f), 
                            common.read_uint8(f), 
                            common.read_uint8(f), 
                            decode_alpha(common.read_uint8(f))
                        )
                    number_of_bytes -= 4

            # Skip unread bytes
            f.seek(number_of_bytes, os.SEEK_CUR)

            # Un-tile and store the information as the content
            self.content = [0] * (pp_display_width * pp_display_height)
            tile_height = 8
            tile_size = tile_width * tile_height
            tile_row = tile_size * int(calculated_storage_width / tile_width)
            for y in xrange(0, pp_display_height):
                for x in xrange(0, pp_display_width):
                    tile_y = int(y / tile_height)
                    tile_x = int(x / tile_width)
                    tile_sub_y = y % tile_height
                    tile_sub_x = x % tile_width
                    self.content[y * pp_display_width + x] = tiled_image_data[tile_y * tile_row + tile_x * tile_size + tile_sub_y * tile_width + tile_sub_x]

            # Check if optional ppc header exists
            if pp_format == 0x8800:
                self.palette = []

            else:
                # Read ppc header
                ppc_header = common.read_uint32(f)
                if ppc_header & 0xFFFFFFFF != 0x00637070:
                    raise Exception('Missing ppc header!')

                # Skip zero padding
                f.seek(2, os.SEEK_CUR)
                
                # Read the number of palette entries
                # It needs to be multiplied by 8 to get the correct total
                palette_total = common.read_uint16(f) * 8

                # Skip zero padding
                f.seek(2 * 4, os.SEEK_CUR)

                # Read palette
                self.palette = [(common.read_uint8(f), 
                                    common.read_uint8(f),
                                    common.read_uint8(f),
                                    decode_alpha(common.read_uint8(f))) 
                                for i in xrange(0, palette_total)]

    def export_pic(self, file_path):

        output_path_metadata = file_path + '.EXPORT.json'
        output_path_helper = file_path + '.EXPORT.HELPER.png' 
        output_path_picture = file_path + '.EXPORT.png'

        # Write metadata
        metadata = {
            "extended_header": self.has_extended_header,

            "unknown_two": self.unknown_two,
            "unknown_three": self.unknown_three,

            "width": self.width,
            "height": self.height,

            "palette_total": len(self.palette),
            "division_name": self.division_name,
            "divisions": self.divisions
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
            if len(self.palette) == 0:
                pw = png.Writer(self.width, self.height, alpha=True)
                flattened_image_data = [color_channel for pixel in self.content for color_channel in pixel]
                pw.write_array(f, flattened_image_data)
                
            else:
                pw = png.Writer(self.width, self.height, palette=self.palette)
                pw.write_array(f, self.content)

    def import_pic(self, file_path):
        # Open picture (Quick implementation that only does 8bpp paletted for now)
        f=png.Reader(filename=file_path)
        pic = f.read()
        self.width = pic[0]
        self.height = pic[1]

        self.content = [c for row in pic[2] for c in row]

        self.palette = pic[3]['palette']

        #with open('test.png', 'wb') as f:
            #if picture_format == 0x88:
            #   pw = png.Writer(display_width, display_height, alpha=True)
            #   flattened_tiled_data = [color_channel for pixel in self.content for color_channel in pixel]
            #   pw.write_array(w, flattened_tiled_data)
            #else:
            #   pw = png.Read(display_width, display_height, palette=self.palette)
            #   pw.write_array(w, self.content)


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
            #picture_wrapper.import_pic('test.png')
            #picture_wrapper.save(input_path + '.REMIT')

        #except Exception, e:
        #   print 'Error: %s' % e
        #   sys.exit(-1)

    elif action in ('-e', '--export'):
        try:
            print '# Exporting %s:' % input_path
            picture_wrapper = PictureWrapper()
            picture_wrapper.open(input_path)

            output_path = input_path

            picture_wrapper.export_pic(output_path)

        except Exception, e:
            print 'Error: %s' % e
            sys.exit(-1)

    else:
        print 'Error: Unknown action: %s' % action
        sys.exit(-1)

    sys.exit(0)
