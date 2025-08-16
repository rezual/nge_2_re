#!/usr/bin/env python3

import os
import struct
import json
import common
import re

class TextArchive(object):
    def __init__(self):
        self.entries = []
        self.strings = []

        self.warnings = []

        self.header_padding = 0
        self.entry_padding = 0

    def warn(self, message):
        # Temporary debug helper to track warning messages in metadata
        self.warnings.append(message)
        print(message)

    def open(self, file_path):
        with open(file_path, 'rb') as f:
            file_size = common.get_file_size(f)

            # Read magic header
            magic_number = f.read(4).decode('ascii', 'ignore')
            if magic_number != 'TEXT':
                raise Exception('Not a TEXT file!')

            # Read number of entries
            number_of_entries = common.read_uint32(f)

            # Read size of header
            header_size = common.read_uint32(f)
            if (header_size != 16):
                msg='# Warning: Non-standard TEXT header size: %s' % header_size
                self.warn(msg)
            
            # Read content start offset
            content_start_offset = common.read_uint32(f)

            # There should be no post-header padding,
            # but check for it anyways
            pre_header_skip_position = f.tell()

            # Skip the header
            f.seek(header_size)

            # Complete the header padding calculation
            self.header_padding = f.tell() - pre_header_skip_position

            # Read entries
            # Don't create them yet,
            # since we want to store the string index instead of the offset
            # and we can't figure out the string index until we've seen all the strings
            entry_unknowns = [0] * number_of_entries
            entry_string_offsets = [0] * number_of_entries
            for i in range(0, number_of_entries):
                entry_unknowns[i] = common.read_uint32(f)
                entry_string_offsets[i] = common.read_uint32(f)

            # There should be no post-header padding,
            # but check for it anyways
            pre_entry_skip_position = f.tell()

            # Skip to the content start
            f.seek(content_start_offset)

            # Complete the header padding calculation
            self.entry_padding = f.tell() - pre_entry_skip_position

            # Read the actual strings (which are used multiple times per entry)
            # Figure out the string index by sorting string offsets from low to high
            string_offset_index_map = {}
            for index, offset in enumerate(sorted(set(entry_string_offsets))):

                # Update the string offset map
                string_offset_index_map[offset] = index

                # Go to the string offset
                f.seek(offset)

                # If offset is at the end, skip
                if (offset >= file_size):
                    self.warn('Out of bounds string in TEXT file, using nulls instead')
                    self.strings.append((None, None, None))
                    continue

                # Read the unknowns
                unknown_first = common.read_uint32(f)
                unknown_second = common.read_uint32(f)

                # Read content until null-terminator (but aligned to 32-bit boundaries)
                raw_string_content = b''
                while True:
                    raw_string_content += f.read(4)
                    if raw_string_content[-1] == 0:
                        break

                # Convert Shift-JIS to unicode
                string_content = common.from_eva_sjis(raw_string_content)
 
                # Strip trailing \0's
                string_content = string_content.rstrip('\0')
                
                # Add this string to the array
                self.strings.append((unknown_first, unknown_second, string_content))

            # Finally create the entries now that we know the string offset to index mapping
            for i in range(0, number_of_entries):
                self.entries.append((entry_unknowns[i], string_offset_index_map[entry_string_offsets[i]]))

    def save(self, file_path):
        with open(file_path, 'wb') as f:

            # Write magic header
            f.write(b'TEXT')

            # Write number of entries
            common.write_uint32(f, len(self.entries))
            
            # Write size of header
            common.write_uint32(f, 16)
            
            # Write content start offset
            # Size of each entry * number of entries + header size
            content_start_offset = 8 * len(self.entries) + 16
            common.write_uint32(f, content_start_offset)

            # Generate the string offsets
            previous_string_end = content_start_offset
            converted_strings = []
            for (unknown_first, unknown_second, string_content) in self.strings:
                # If string is None, because its contents were outside the end of the file,
                # then recreate the same conditions by injecting a dummy
                if string_content is None:
                    converted_strings.append((unknown_first, unknown_second, None, previous_string_end))
                    continue

                # Calculate the offset of this string based on the end of the previous string
                string_offset = previous_string_end

                # Add the implicit null terminator
                string_content += '\0'

                # Convert unicode to Shift-JIS
                raw_string_content = common.to_eva_sjis(string_content)

                # Calculate how much memory this string takes
                raw_string_content = common.zero_pad_and_align_string(raw_string_content)
                string_padded_size = len(raw_string_content)

                # Update previous_string_end for the next iteration (+ 8 for the two unknowns)
                previous_string_end += string_padded_size + 8

                # Add the string to converted strings
                converted_strings.append((unknown_first, unknown_second, raw_string_content, string_offset))

            # Write entries
            for (entry_unknown, entry_string_index) in self.entries:
                # Write unknown
                common.write_uint32(f, entry_unknown)

                # Write string offset
                # 3rd index is the string offset
                common.write_uint32(f, converted_strings[entry_string_index][3])

            # Write the actual strings (which are used multiple times per entry)
            # They should already be in order of appearance
            for (unknown_first, unknown_second, string_content, string_offset) in converted_strings:

                # This feature is used by the game to put a
                # dynamic string at the end possibly
                if string_content is None:
                    continue

                # Write the unknowns
                common.write_uint32(f, unknown_first)
                common.write_uint32(f, unknown_second)

                # Write the string
                f.write(string_content)

    def patch(self, patch_file):
        translate_map = {}
        with open (patch_file, "r", encoding='utf-8') as f:
            translate_map = json.loads(f.read())

        # Loop through strings, applying the translate_map
        for string_index, (unknown_first, unknown_second, string_content) in enumerate(self.strings):
            line = translate_map.get(string_content)
            if line:
                translation = line.get("translation") or line.get("machine_deepl") or line.get("machine_google")
                self.strings[string_index] = (unknown_first, unknown_second, translation)

    def export_text(self, file_path):

        output_path = file_path + '.TEXT.json'

        data = {
            "entries": self.entries,
            "strings": self.strings,
            "warnings": self.warnings,

            "header_padding": self.header_padding,
            "entry_padding": self.entry_padding
        }

        with open(output_path, 'wb') as f:
            f.write(json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8'))

    def import_text(self, file_path):
        
        # Check if the input file exists
        if not os.path.exists(file_path):
            raise Exception('File does not exist: %s' % file_path)

        # Load the JSON
        data = ''
        with open(file_path, 'rb') as f:
            data = f.read()

        try:
            data = json.loads(data.decode('utf-8'))
        except:
            raise Exception('File has invalid JSON data: %s' % file_path)

        # Populate the instance
        self.entries = data['entries']
        self.strings = []
        self.warnings = data['warnings']
        self.header_padding = data['header_padding']
        self.entry_padding = data['entry_padding']

        # Reprocess strings
        for (unknown_first, unknown_second, string_content) in data['strings']:
            # Add this string to the array
            self.strings.append((unknown_first, unknown_second, string_content))

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print('text.py <action> <archive.bin>')
        print('')
        print('text.py -e,--export <archive.bin>            # Output is file archive.bin.TEXT.json')
        print('text.py -i,--import <archive.bin.TEXT.json>  # Output is file archive.bin')
        print('text.py -p,--patch <archive.bin> <patch.py>  # Output is file archive.bin.PATCHED')
        sys.exit(0)

    action = sys.argv[1]
    input_path = os.path.normpath(sys.argv[2])
    output_path = ''

    try:
        if len(input_path) == 0:
            raise Exception('Empty input path provided')

        if action in ('-e', '--export'):
            print('# Exporting %s:' % input_path)
            text_archive = TextArchive()
            text_archive.open(input_path)

            output_path = input_path
            text_archive.export_text(output_path)

        elif action in ('-i', '--import'):
            print('# Importing %s:' % input_path)
            text_archive = TextArchive()
            
            suffix = '.TEXT.json'
            if not input_path.lower().endswith(suffix.lower()):
                raise Exception('Input path must have a suffix of %s' % suffix)
            output_path = input_path[:-len(suffix)]

            text_archive.import_text(input_path)
            text_archive.save(output_path)

        elif action in ('-p', '--patch'):

            if len(sys.argv) < 4:
                print('text.py -p,--patch <archive.bin> <patch.py>  # Output is file archive.bin.PATCHED')
                sys.exit(0)

            patch_path = os.path.normpath(sys.argv[3])

            print('# Patching %s:' % input_path)
            text_archive = TextArchive()
            text_archive.open(input_path)

            output_path = input_path + '.PATCHED'

            text_archive.patch(patch_path)
            text_archive.save(output_path)

        else:
            raise Exception('Unknown action: %s' % action)
            
    except Exception as e:
        import traceback

        print('Error: %s' % e)
        traceback.print_exc()
        sys.exit(-1)

    sys.exit(0)
