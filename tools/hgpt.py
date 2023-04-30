#!/usr/bin/env python3

# Oddities: 
# im/im059800.zpt.DECOMPRESSED: It's not a HGPT file, but instead is a HGMT file - which seems to be an untiled, HPT file
# game/system.har.HGARPACK/dbgfont.zmt.DECOMPRESSED: The second unknown is neither 0x00000000 nor 0xFFFFFFFF, but instead 0x0000F000 
# game/ja.har.HGARPACK/f013_15a.hpt.DECOMPRESSED: This seems to be a prototype HGPT encoding that uses full 0xFF for alpha and swaps byte order,
#   with the final one being in event/f013.har.HGARPACK/f013_15a.zpt.DECOMPRESSED

import os
import struct
import json
import png
import common

def decode_alpha(encoded_alpha):
    return min(encoded_alpha << 1, 0xFF)

def encode_alpha(alpha):
    alpha >>= 1
    if alpha == 0x7F:
        return 0x80
    return alpha

class HgptWrapper(object):
    def __init__(self):
        self.has_extended_header = True

        self.unknown_two = 0x00000000
        self.unknown_three = 0x0013 # Spotted as 0x0013 most of the time; few times 0x0014; only used if extended header is True

        self.width = 0
        self.height = 0
        self.palette = []
        self.division_name = (b'\0' * 8).decode('utf-8')
        self.divisions = []
        self.content = []

    def open(self, file_path):
        with open(file_path, 'rb') as f:
            file_size = common.get_file_size(f)

            # Read magic header
            magic_number = f.read(4).decode('ascii', 'ignore')
            if magic_number != 'HGPT':
                raise Exception('Not an HGPT file! Missing HGPT header id.')

            # Read pp offset
            pp_offset = common.read_uint16(f)
            if pp_offset < 0x10:
                raise Exception('PP offset less than 0x10, PS2 variant not supported!')

            # Read if it has an extended header
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

            # ff ff ff ff in pictures with extended header 
            # 00 00 00 00 in pictures w/o extended header 
            unknown_two = common.read_uint32(f)
            
            # Load divisions
            if has_extended_header:
                # Read number of divisions (again)
                number_of_divisions_repeat = common.read_uint16(f)
                if number_of_divisions != number_of_divisions_repeat:
                    raise Exception('Number of divisions and its repeat don\'t match: %s != %s' % (number_of_divisions, number_of_divisions_repeat))

                # Read unknown
                # 0x0013 is the most common 
                # 0x0014 is the other occurence 
                unknown_three = common.read_uint16(f)
                if unknown_three != 0x0013:
                    print('# Warning: UnknownThree (0x%X) != 0x0013' % unknown_three)

                # Read division name
                self.division_name = (f.read(8) + b'\0' * 8)[0:8].decode('utf-8')

                # Read divisions
                for i in range(0, number_of_divisions):
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

            # Check that it's the correct pp_offset
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

            # Calculate values that depend on the pp format
            bytes_per_pixel = 1
            bytes_per_pixel_ppd_size = bytes_per_pixel
            tile_width = 16

            if pp_format == 0x8800:
                bytes_per_pixel = 4
                bytes_per_pixel_ppd_size = 1
                tile_width = 4

            elif pp_format == 0x13:
                bytes_per_pixel = 1
                bytes_per_pixel_ppd_size = bytes_per_pixel
                tile_width = 16

            elif pp_format == 0x14:
                bytes_per_pixel = 0.5
                bytes_per_pixel_ppd_size = bytes_per_pixel
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

            # Read ppd_size which is the size of the ppd header + number of pixels
            # The ppd header which is 0x20 bytes in size
            ppd_size = common.read_uint32(f)

            calculated_ppd_size = int(number_of_pixels * bytes_per_pixel_ppd_size) + 0x20
            if (calculated_ppd_size != ppd_size):
                raise Exception ('PPD size %s does not match the calculated ppd size %s' % (ppd_size, calculated_ppd_size))

            # Calculate the number of bytes
            number_of_bytes = int(number_of_pixels * bytes_per_pixel)

            # Skip padding
            f.seek(3 * 4, os.SEEK_CUR)

            # Read the tiled image data
            # The image data is stored in a scrambled tiled format, so we'll have to reprocess it   
            tiled_image_data = [0] * number_of_pixels
            cache_last_pixel = None
            
            for i in range(0, number_of_pixels):
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
            for y in range(0, pp_display_height):
                for x in range(0, pp_display_width):
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
                                for i in range(0, palette_total)]

    def save(self, file_path):
        with open(file_path, 'wb') as f:

            # Calculate various sizes

            # Divisions sizes
            divisions_padded_size = 0
            divisions_padding = 0
            if self.has_extended_header:
                divisions_size = 12 + len(self.divisions) * 8
                divisions_padded_size = common.align_size(divisions_size, 16)
                divisions_padding = divisions_padded_size - divisions_size

            # PP offset
            pp_offset = 16 + divisions_padded_size

            # Palette total, PP format, bytes_per_pixel, and tile_width
            palette_total = len(self.palette)
            pp_format = 0x13
            bytes_per_pixel = 1
            bytes_per_pixel_ppd_size = bytes_per_pixel
            tile_width = 16

            if palette_total == 0:
                pp_format = 0x8800
                bytes_per_pixel = 4
                bytes_per_pixel_ppd_size = 1 
                tile_width = 4

            elif palette_total == 16:
                pp_format = 0x14
                bytes_per_pixel = 0.5
                bytes_per_pixel_ppd_size = bytes_per_pixel
                tile_width = 32
            
            elif palette_total == 256:
                pp_format = 0x13
                bytes_per_pixel = 1
                bytes_per_pixel_ppd_size = bytes_per_pixel
                tile_width = 16

            else:
                raise Exception('Unknown palette total, %s' % palette_total)
            
            # Sixteenths resolution and storage resolution
            ppd_sixteenths_width = common.align_size(self.width, 16)
            ppd_sixteenths_height = common.align_size(self.height, 8)

            storage_width = common.align_size(self.width, tile_width)
            storage_height = common.align_size(self.height, 8)

            number_of_pixels = storage_width * storage_height

            # PPD Size
            # The size also includes the PPD header in the count, which is 0x20 bytes
            ppd_size = int(number_of_pixels * bytes_per_pixel_ppd_size) + 0x20

            # Calculate the number of bytes
            number_of_bytes = int(number_of_pixels * bytes_per_pixel)

            # Calculate headers
            pp_header  = 0x00007070 | ((pp_format & 0xFFFF) << 16)
            ppd_header = 0x00647070 | ((pp_format & 0xFF) << 24) 
            ppc_header = 0x00637070

            # Begin writing
            # Write magic header
            f.write(b'HGPT')

            # Write pp offset
            common.write_uint16(f, pp_offset)

            # Write if it has an extended header
            common.write_uint16(f, 1 if self.has_extended_header else 0)

            # Write number of divisions
            common.write_uint16(f, len(self.divisions))

            # Write unknowns
            common.write_uint16(f, 0x0001)

            # ff ff ff ff in pics with extended header 
            # 00 00 00 00 in pictures w/o extended header 
            common.write_uint32(f, 0xFFFFFFFF if self.has_extended_header else 0x00000000)
            
            if self.has_extended_header:
                # Write the number of divisions again
                common.write_uint16(f, len(self.divisions))

                # Write unknown
                # 0x0013 is the most common 
                # 0x0014 is the other occurence 
                common.write_uint16(f, self.unknown_three) 

                # Write division name
                f.write((self.division_name.encode('utf-8') + b'\0' * 8)[0:8])

                # Write divisions
                for division in self.divisions:
                    common.write_uint16(f, division[0]) # division_start_x
                    common.write_uint16(f, division[1]) # division_start_y
                    common.write_uint16(f, division[2]) # division_width
                    common.write_uint16(f, division[3]) # division_height

                # Add zero padding
                f.write(b'\0' * divisions_padding)

            # Write PP header
            common.write_uint32(f, pp_header)

            # Write display dimensions
            common.write_uint16(f, self.width)  # display_width
            common.write_uint16(f, self.height) # display_height

            # Write zero padding
            f.write(b'\0' * 8)
            
            # Write ppd header
            common.write_uint32(f, ppd_header)

            # Write display dimensions again
            common.write_uint16(f, self.width)  # ppd_display_width
            common.write_uint16(f, self.height) # ppd_display_height

            # Write zero padding
            f.write(b'\0' * 4)

            # Write ppd sixteenths dimensions
            common.write_uint16(f, ppd_sixteenths_width)
            common.write_uint16(f, ppd_sixteenths_height)

            # Write ppd_size
            common.write_uint32(f, ppd_size)

            # Write zero padding
            f.write(b'\0' * 12)

            # Re-tile
            tiled_image_data = [0] * number_of_pixels

            tile_height = 8
            tile_size = tile_width * tile_height
            tile_row = tile_size * int(storage_width / tile_width)
            for y in range(0, self.height):
                for x in range(0, self.width):
                    tile_y = int(y / tile_height)
                    tile_x = int(x / tile_width)
                    tile_sub_y = y % tile_height
                    tile_sub_x = x % tile_width
                    tiled_image_data[tile_y * tile_row + tile_x * tile_size + tile_sub_y * tile_width + tile_sub_x] = self.content[y * self.width + x]

            # Write image data
            cache_last_pixel = None

            for i in range(0, number_of_pixels):
                if number_of_bytes <= 0:
                    break

                if pp_format == 0x13:
                    common.write_uint8(f, tiled_image_data[i])
                    number_of_bytes -= 1

                elif pp_format == 0x14:
                    if (i & 1) == 0:
                        # Even write
                        cache_last_pixel = (tiled_image_data[i] & 0xF)
                    else:
                        # Odd write
                        common.write_uint8(f, cache_last_pixel | ((tiled_image_data[i] & 0xF) << 4))
                        number_of_bytes -= 1

                elif pp_format == 0x8800:
                    # Write full RGBA
                    common.write_uint8(f, tiled_image_data[i][0])
                    common.write_uint8(f, tiled_image_data[i][1])
                    common.write_uint8(f, tiled_image_data[i][2])
                    common.write_uint8(f, encode_alpha(tiled_image_data[i][3]))
                    number_of_bytes -= 4

            # Write palette
            if pp_format == 0x8800:
                # There is no palette
                pass

            else:
                # Write ppc header
                common.write_uint32(f, ppc_header)

                # Write zero padding
                f.write(b'\0' * 2)

                # Write number of palette entries (but needing to be divided by 8)
                common.write_uint16(f, palette_total // 8)

                # Write zero padding
                f.write(b'\0' * 8)

                # Write palette
                for c in self.palette:
                    common.write_uint8(f, c[0])
                    common.write_uint8(f, c[1])
                    common.write_uint8(f, c[2])
                    common.write_uint8(f, encode_alpha(c[3]))

    def export_hgpt(self, file_path):

        output_path_metadata = file_path + '.PICTURE.json'
        output_path_helper = file_path + '.PICTURE.HELPER.png' 
        output_path_picture = file_path + '.PICTURE.png'

        # Write metadata
        metadata = {
            "has_extended_header": self.has_extended_header,

            "unknown_two": self.unknown_two,
            "unknown_three": self.unknown_three,

            "width": self.width,
            "height": self.height,

            "palette_total": len(self.palette),
            "division_name": self.division_name,
            "divisions": self.divisions
        }

        with open(output_path_metadata, 'wb') as f:
            f.write(json.dumps(metadata, indent=4, ensure_ascii=False).encode('utf-8'))

        # Create a divisions helper file
        if (self.divisions):
            # Get background color
            background_color = common.unique_color(-1, None)

            # Create the canvas
            canvas = [background_color] * (self.width * self.height)

            def is_in_bounds(x, y, width, height):
                return (x >= 0) and (x < width) and (y >= 0) and (y < height)

            # Loop through divisions, plotting them onto the canvas
            for i, (division_x_pos, division_y_pos, division_width, division_height) in enumerate(self.divisions):

                # Get a unique color
                draw_color = common.unique_color(i, len(self.divisions))

                # Draw an empty square
                for y in range(0, division_height):
                    if is_in_bounds(division_x_pos, division_y_pos + y, self.width, self.height):
                        canvas[(division_y_pos + y) * self.width + (division_x_pos + 0)] = draw_color

                    if is_in_bounds(division_x_pos + division_width - 1, division_y_pos + y, self.width, self.height):
                        canvas[(division_y_pos + y) * self.width + (division_x_pos + division_width - 1)] = draw_color

                for x in range(1, division_width - 1):
                    if is_in_bounds(division_x_pos + x, division_y_pos, self.width, self.height):
                        canvas[(division_y_pos + 0) * self.width + (division_x_pos + x)] = draw_color

                    if is_in_bounds(division_x_pos + x, division_y_pos + division_height - 1, self.width, self.height):
                        canvas[(division_y_pos + division_height - 1) * self.width + (division_x_pos + x)] = draw_color

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

    def import_hgpt(self, file_path):

        input_path_metadata = file_path + '.PICTURE.json'
        input_path_picture = file_path + '.PICTURE.png'

        # Check if the input file exists
        if not os.path.exists(input_path_picture):
            raise Exception('File does not exist: %s' % input_path_picture)

        # Load the JSON
        metadata = {}
        if os.path.exists(input_path_metadata):
            with open(input_path_metadata, 'rb') as f:
                metadata = f.read()

                try:
                    metadata = json.loads(metadata.decode('utf-8'))
                except:
                    raise Exception('File has invalid JSON data: %s' % input_path_metadata)

        # Set defaults
        self.has_extended_header = metadata.get('has_extended_header', False)
        self.unknown_two         = metadata.get('unknown_two', 0x00000000)
        self.unknown_three       = metadata.get('unknown_three', 0x0013)
        self.width               = metadata.get('width', 0)
        self.height              = metadata.get('height', 0)
        self.division_name       = metadata.get('division_name', (b'\0' * 8).decode('utf-8'))
        self.divisions           = metadata.get('divisions', [])

        palette_total = metadata.get('palette_total', 0)

        # Open picture
        pr = png.Reader(filename=input_path_picture)
        pic = pr.read()

        # Check dimensions for changes
        new_width = pic[0]
        new_height = pic[1]

        if new_width != self.width or new_height != self.height:
            print('# Warning: Picture dimensions have changed, old: (%s x %s), new: (%s x %s)' % (self.width, self.height, new_width, new_height))

        self.width = new_width
        self.height = new_height

        # Check palette for changes
        new_palette = pic[3].get('palette', [])

        if palette_total != len(new_palette):
            print('# Warning: Picture palette count has changed, old: %s, new %s' % (palette_total, len(new_palette)))

        self.palette = [(c[0], c[1], c[2], (0xFF if len(c) == 3 else c[3])) for c in new_palette]

        # Extend the palette if it doesn't fit into a 0, 16, 256 bucket
        if len(self.palette) != 0:
            if len(self.palette) < 16:
                self.palette.extend([(0,0,0, 0xFF)] * (16 - len(self.palette)))

            elif len(self.palette) > 16 and len(self.palette) < 256:
                self.palette.extend([(0,0,0, 0xFF)] * (256 - len(self.palette)))

        # Load content
        if len(new_palette) == 0:
            self.content = []
            color_channel_buffer = [0] * 4
            color_channel_buffer[3] = 0xFF
            i = 0
            for row in pic[2]:
                for color_channel in row:
                    color_channel_buffer[i] = color_channel
                    i += 1

                    if (pic[3]['alpha'] and i == 4) or (not pic[3]['alpha'] and i == 3):
                        self.content.append((
                            color_channel_buffer[0],
                            color_channel_buffer[1],
                            color_channel_buffer[2],
                            color_channel_buffer[3]))
                        i = 0

        else:
            self.content = [c for row in pic[2] for c in row]

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print('hgpt.py <action> <picture.hpt>')
        print('')
        print('hgpt.py -e,--export <picture.hpt>             # Output are files picture.hpt.PICTURE.png and picture.hpt.PICTURE.json')
        print('hgpt.py -i,--import <picture.hpt.PICTURE.png> # Input are files picture.hpt.PICTURE.png and picture.hpt.PICTURE.json')
        sys.exit(0)

    action = sys.argv[1]
    input_path = os.path.normpath(sys.argv[2])
    output_path = ''

    try:
        if len(input_path) == 0:
            raise Exception('Empty input path provided')

        if action in ('-e', '--export'):
            print('# Exporting %s:' % input_path)
            hgpt_wrapper = HgptWrapper()
            hgpt_wrapper.open(input_path)

            output_path = input_path
            hgpt_wrapper.export_hgpt(output_path)

        elif action in ('-i', '--import'):
            print('# Importing %s:' % input_path)
            hgpt_wrapper = HgptWrapper()
            
            # Figure out the base input path,
            # which will also serve as the output path
            suffix_a = '.PICTURE.json'
            suffix_b = '.PICTURE.png'
            if input_path.lower().endswith(suffix_a.lower()):
                output_path = input_path = input_path[:-len(suffix_a)]

            elif input_path.lower().endswith(suffix_b.lower()):
                output_path = input_path = input_path[:-len(suffix_b)]
                
            else:
                raise Exception('Input path must have a suffix of %s or %s' % (suffix_a, suffix_b))

            hgpt_wrapper.import_hgpt(input_path)
            hgpt_wrapper.save(output_path)

        else:
            raise Exception('Unknown action: %s' % action)
            
    except Exception as e:
        import traceback

        print('Error: %s' % e)
        traceback.print_exc()
        sys.exit(-1)

    sys.exit(0)
