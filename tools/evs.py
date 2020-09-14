#!/usr/bin/env python3

import os
import struct
import json
import re
import common

"""
function 1: say(avatar, facial_expression, audio) "sentence\n\0"
    avatar:
        0 = no one
        1 = shinji
        2 = asuka
        3 = rei
        4 = misato
        5 = Gendo
        6 = Fuyutsuki
        7 = Ritsuko
        8 = Maya
        9 = Hyuga
        10 = Aoba
        11 = Kaji
        12 = Hikari
        13 = Toji
        14 = Kensuke
        15 = Kaworu
        16 = Pen Pen
        17 = Male Staff
        18 = Female Staff
        19 = Clerk

    facial_expression:

        0 = do not show avatar
        1 = (school uniform) happy
        2 = (school uniform) angry
        3 = (school uniform) down
        4 = (school uniform) happy + loud
        5 = (school uniform) disappointed
        6 = (school uniform) blushing
        7 = (school uniform) concerned
        8 = (school uniform) wide-eyed/unsure
        9 = (school uniform) angry/defensive
        10 = (plug suit) happy
        11 = (plug suit) concerned
        12 = (summer outfit) happy
        13 = (summer outfit) happy + loud
        14 = (summer outfit) angry

        4096 = do not show avatar
        8192 = do not show message box (implies 4096)
        16384 = do not play audio

    parameter 3: audio

function 135: extension(extension_id)
    extension_id:
        1 = 
        623 = hides arrows
        624 = point arrow and highlight AT field
        625 = show arrow and highlight impulse field
        626 = show arrow highlighting ???
        627 = show arrow highlighting ???
        628 =
        629 =
        630 =
        631 = 
        632 = 
        633 =
        634 =
        635 = two arrows pointing in middle of screen to the upper-right
        636 = shows save dialog
        637 = show HUD
        638 = hide HUD
        639 = demo-counting DEFCON level
        640 = show arrow that points to DEFCON level
        641 = Wait for player to press square or circle
        642 = Bring up Triangle-Menu
        643 = Select / Simulate Circle
        644 = Simulate Press-Down
        645 = Hide Menu
        646 = Show arrow pointing at ???
        647 = Show arrow pointing at ???
        648 = ???
        649 = Show two arrows pointing at ???
        650 = 



function 140: load_bg(?) "background_file_name"

function 144: wait(# msecs)

function 154: ???(?, ?)    

"""

FUNCTION_PARAMETER_SIZE = [
     None,     3,     1,  None,     1,     1,     1,     1,     1,     1,     3,  None,     1,     1,     1,     1,  # 0x00 - 0x0F
        2,     1,     1,     1,     1,     3,     3,     3,     3,     2,     2,  None,     2,  None,     2,     2,  # 0x10 - 0x1F
        4,     4,     2,     2,     2,  None,     4,     4,     3,     4,     4,     3,     4,     3,     3,     2,  # 0x20 - 0x2F
        2,     2,     2,     3,     3,     3,     3,     3,     4,     3,     2,     2,  None,     2,     2,     2,  # 0x30 - 0x3F
        2,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2,  # 0x40 - 0x4F
        2,     2,     2,     2,     2,     3,     2,     1,     1,     1,     1,     1,     1,     1,     1,     1,  # 0x50 - 0x5F
        1,     1,     1,     2,     2,     1,  None,     1,     1,     0,     0,     0,     0,     0,     0,     0,  # 0x60 - 0x6F
        0,     0,     0,     0,     0,     0,     0,     0,     2,     1,     0,     0,     0,     1,     1,     1,  # 0x70 - 0x7F
        0,     0,  None,  None,  None,     1,     0,     1,  None,  None,  None,  None,     1,     1,     1,     1,  # 0x80 - 0x8F
        1,     1,     1,     1,     1,     0,  None,     0,     1,     2,     2,     2,     2,     1,     1,     2,  # 0x90 - 0x9F
        1,     1,     1,     1,     1,     1,     2,     3,     3,     1,     1,     1,     1,     1,     1,     2,  # 0xA0 - 0xAF
        1,  None,     3,     3,  None,     1,  None,     3,  None,  None,  None,  None,  None,  None,  None,  None,  # 0xB0 - 0xBF
     None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  # 0xC0 - 0xCF
     None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  # 0xD0 - 0xDF
     None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  # 0xE0 - 0xEF
     None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  # 0xF0 - 0xFF
]

HAS_CONTENT_SECTION = (0x01, 0x8C, 0x8D, 0xA3, 0x8E, 0x95)

def get_number_of_parameters(entry_type):
    if entry_type >= len(FUNCTION_PARAMETER_SIZE) or entry_type < 0:
        return None

    return FUNCTION_PARAMETER_SIZE[entry_type]

class EvsWrapper(object):
    def __init__(self):
        self.entries = []

    def open(self, file_path):
        with open(file_path, 'rb') as f:
            file_size = common.get_file_size(f)

            # Read magic header
            magic_number = f.read(4).decode('ascii', 'ignore')
            if magic_number != '.EVS':
                raise Exception('Not an EVS file!')

            # Read the number of entries
            number_of_entries = common.read_uint32(f)
            
            # Read entry offsets
            entry_offsets = [0] * number_of_entries
            for i in range(0, number_of_entries):
                entry_offsets[i] = common.read_uint32(f)

            # Loop through entries
            for i in range(0, number_of_entries):
                f.seek(entry_offsets[i])

                # Read entry type
                entry_type = common.read_uint16(f)

                # Read entry size
                entry_size = common.read_uint16(f)

                # Read entry
                number_of_parameters = get_number_of_parameters(entry_type)
                has_content_section = entry_type in HAS_CONTENT_SECTION

                if number_of_parameters is None:
                    # Commands that I've yet to document the parameter count for
                    raise Exception('Unknown number of parameters for entry type: 0x%X, size: %s' % (entry_type, entry_size))
                
                # Read the parameters
                entry_parameters = []
                for j in range(0, number_of_parameters):
                    entry_parameters.append(common.read_uint32(f))

                # Whatever remains after the parameters is the content
                parameter_size = 4 * number_of_parameters
                remaining_bytes = entry_size - parameter_size

                if remaining_bytes < 0:
                    raise Exception('Number of parameters overshoots total entry size; entry type: 0x%X, size: %s' % (entry_type, entry_size))

                if has_content_section:
                    raw_entry_content = f.read(remaining_bytes)

                    # Convert encoding
                    entry_content = common.from_eva_sjis(raw_entry_content)

                    # Strip trailing \0's
                    entry_content = entry_content.rstrip('\0')

                else:
                    entry_content = None

                if not has_content_section and (entry_size != parameter_size):
                    raise Exception('Extra unannounced content in entry type: 0x%X, size: %s' % (entry_type, entry_size))

                # Add entry
                self.entries.append((entry_type, entry_parameters, entry_content))

    def save(self, file_path):
        with open(file_path, 'wb') as f:
            file_size = common.get_file_size(f)

            # Write magic header
            f.write(b'.EVS')

            # Write the number of entries
            common.write_uint32(f, len(self.entries))
            
            # Write entry offsets
            # Size of header + size of entry table
            previous_entry_end = 8 + 4 * len(self.entries)
            converted_entries = []
            for (entry_type, entry_parameters, entry_content) in self.entries:

                has_content_section = entry_type in HAS_CONTENT_SECTION

                # Write offset
                common.write_uint32(f, previous_entry_end)

                # Calculate the size of this entry,
                # so that we know when the next entry starts
                
                # Calculate how much memory this string takes
                if has_content_section:
                    # Convert UTF8 to Shift-JIS
                    raw_entry_content = common.to_eva_sjis(entry_content)

                    # We add a single null terminator and only count the single null terminator,
                    # but later we include the extra alignment padding in the size calculation
                    string_terminated_size = len(raw_entry_content) + 1
                    raw_entry_content = common.zero_pad_and_align_string(raw_entry_content)
                else:
                    string_terminated_size = 0
                    raw_entry_content = b''

                # Calculate the entry_size
                # parameters + content
                entry_size = 4 * len(entry_parameters) + string_terminated_size

                # Update previous_entry_end for the next iteration
                # Add 4 for the entry_type (omitted in the entry_size calculation)
                previous_entry_end += common.align_size(4 + entry_size, 4)

                # Add the entry to the converted entries
                converted_entries.append((entry_type, entry_size, entry_parameters, raw_entry_content))

            # Loop through entries
            for (entry_type, entry_size, entry_parameters, raw_entry_content) in converted_entries:

                # Write entry type
                common.write_uint16(f, entry_type)

                # Write entry size
                common.write_uint16(f, entry_size)

                # Write the parameters
                for entry_parameter in entry_parameters:
                    common.write_uint32(f, entry_parameter)
                
                # Write the content
                f.write(raw_entry_content)

    def patch(self, patch_file):
        translate_map = {}
        with open (patch_file, "r", encoding='utf-8') as f:
            translate_map = json.loads(f.read())

        # Loop through strings, applying the translate_map
        for entry_index, (entry_type, entry_parameters, entry_content) in enumerate(self.entries):
            line = translate_map.get(entry_content)
            if line:
                translation = line.get("translation") or line.get("machine_deepl") or line.get("machine_google")
                self.entries[entry_index] = (entry_type, entry_parameters, translation)

    def export_evs(self, file_path):

        output_path = file_path + '.EVS.json'

        data = {
            "entries": [
                {
                    "function": entry_type,
                    "parameters": entry_parameters,
                    "content": entry_content
                }
                for (entry_type, entry_parameters, entry_content) in self.entries
            ]
        }

        with open(output_path, 'wb') as f:
            f.write(json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8'))

    def import_evs(self, file_path):
        
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
        self.entries = []

        # Reprocess entries
        for entry in data['entries']:
            
            entry_type = entry['function']
            entry_parameters = entry['parameters']
            entry_content = entry['content']

            # Add this string to the array
            self.entries.append((entry_type, entry_parameters, entry_content))

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print('evs.py <action> <file.evs>')
        print('')
        print('evs.py -e,--export <file.evs>             # Output is file.evs.EVS.json')
        print('evs.py -i,--import <file.evs.EVS.json>    # Output is file.evs')
        print('evs.py -p,--patch <file.evs> <patch.py>   # Output is file file.evs.PATCHED')
        sys.exit(0)

    action = sys.argv[1]
    input_path = os.path.normpath(sys.argv[2])
    output_path = ''

    try:
        if len(input_path) == 0:
            print('Error: Empty input path provided')
            sys.exit(-1)

        if action in ('-e', '--export'):
            print('# Exporting %s:' % input_path)
            evs_wrapper = EvsWrapper()
            evs_wrapper.open(input_path)

            output_path = input_path
            evs_wrapper.export_evs(output_path)

        elif action in ('-i', '--import'):
            print('# Importing %s:' % input_path)
            evs_wrapper = EvsWrapper()

            suffix = '.EVS.json'
            if not input_path.lower().endswith(suffix.lower()):
                raise Exception('Input path must have a suffix of %s' % suffix)
            output_path = input_path[:-len(suffix)]

            evs_wrapper.import_evs(input_path)
            evs_wrapper.save(output_path)

        elif action in ('-p', '--patch'):

            if len(sys.argv) < 4:
                print('evs.py -p,--patch <file.evs> <patch.py>   # Output is file file.evs.PATCHED')
                sys.exit(0)

            patch_path = os.path.normpath(sys.argv[3])

            print('# Patching %s:' % input_path)
            evs_wrapper = EvsWrapper()
            evs_wrapper.open(input_path)

            output_path = input_path + '.PATCHED'

            evs_wrapper.patch(patch_path)
            evs_wrapper.save(output_path)

        else:
            raise Exception('Unknown action: %s' % action)

    except Exception as e:
        import traceback

        print('Error: %s' % e)
        traceback.print_exc()
        sys.exit(-1)

    sys.exit(0)