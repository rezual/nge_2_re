#!/usr/bin/env python2.7

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

class EvsWrapper(object):
    def __init__(self):
        self.entries = []

    def open(self, file_path):
        with open(file_path, 'rb') as f:
            file_size = common.get_file_size(f)

            # Read magic header
            magic_number = f.read(4)
            if magic_number != '.EVS':
                raise Exception('Not an EVS file!')

            # Read the number of entries
            number_of_entries = common.read_uint32(f)
            
            # Read entry offsets
            entry_offsets = [0] * number_of_entries
            for i in xrange(0, number_of_entries):
                entry_offsets[i] = common.read_uint32(f)

            # Loop through entries
            for i in xrange(0, number_of_entries):
                f.seek(entry_offsets[i])

                # Read entry type
                entry_type = common.read_uint16(f)

                # Read entry size
                entry_size = common.read_uint16(f)

                # Read entry
                include_in_output = True #False
                number_of_parameters = 0 
                if entry_type == 0x01:
                    # Japanese text
                    number_of_parameters = 3
                    
                    include_in_output = True

                elif entry_type == 0x02:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x04:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x05:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x07:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x0A:
                    # Unknown
                    number_of_parameters = 3
                elif entry_type == 0x0D:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x0E:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x11:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x12:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x13:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x14:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x15:
                    # Unknown
                    number_of_parameters = 3
                elif entry_type == 0x16:
                    # Unknown
                    number_of_parameters = 3
                elif entry_type == 0x18:
                    # Unknown
                    number_of_parameters = 3
                elif entry_type == 0x1A:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x1F:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x28:
                    # Unknown
                    number_of_parameters = 3
                elif entry_type == 0x29:
                    # Unknown
                    number_of_parameters = 4
                elif entry_type == 0x2A:
                    # Unknown
                    number_of_parameters = 4
                elif entry_type == 0x2B:
                    # Unknown
                    number_of_parameters = 3
                elif entry_type == 0x2C:
                    # Unknown
                    number_of_parameters = 4
                elif entry_type == 0x2E:
                    # Unknown
                    number_of_parameters = 3
                elif entry_type == 0x2F:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x30:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x31:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x32:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x33:
                    # Unknown
                    number_of_parameters = 3
                elif entry_type == 0x34:
                    # Unknown
                    number_of_parameters = 3
                elif entry_type == 0x51:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x52:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x53:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x54:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x56:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x57:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x60:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x65:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x71:
                    # Unknown / Terminator?
                    number_of_parameters = 0
                elif entry_type == 0x72:
                    # Unknown / Terminator?
                    number_of_parameters = 0
                elif entry_type == 0x78:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x79:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x7A:
                    # Unknown / Terminator?
                    number_of_parameters = 0
                elif entry_type == 0x7B:
                    # Unknown / Terminator?
                    number_of_parameters = 0
                elif entry_type == 0x7D:
                    # Unknown / Terminator?
                    number_of_parameters = 1
                elif entry_type == 0x85:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x86:
                    # Unknown
                    number_of_parameters = 0
                elif entry_type == 0x87:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x8C:
                    # A .zpt file? (compressed HGPT)
                    number_of_parameters = 1
                elif entry_type == 0x8D:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x8E:
                    # A .zpt file? (titlet19.zpt)
                    number_of_parameters = 1
                elif entry_type == 0x8F:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x90:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x91:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x92:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x93:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x94:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x95:
                    # Parameter-less text?
                    number_of_parameters = 0
                    
                    include_in_output = True

                elif entry_type == 0x98:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0x9A:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x9B:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x99:
                    # Unknown
                    number_of_parameters = 2
                elif entry_type == 0x9E:
                    # Unknown
                    number_of_parameters = 1
                elif entry_type == 0xA3:
                    # A .bin file?
                    number_of_parameters = 1
                elif entry_type == 0xA7:
                    # Unknown
                    number_of_parameters = 3
                elif entry_type == 0xB7:
                    # Unknown
                    number_of_parameters = 3
                else:
                    # Commands that I've yet to document the parameter count for
                    include_in_output = False #True     
                
                # Read the parameters
                entry_parameters = []
                for j in xrange(0, number_of_parameters):
                    entry_parameters.append(common.read_uint32(f))

                # Whatever remains after the parameters is the content
                size_adjust = 4 * number_of_parameters

                try:
                    entry_content = f.read(entry_size - size_adjust).decode('shift_jis').encode('utf-8')
                except (UnicodeDecodeError, UnicodeEncodeError): 
                    raise Exception('There seems to be an character that cannot be converted to UTF-8. Check the text:' + entry_content)

                #json.dumps(content, ensure_ascii=False).replace('\\u0000', '\\0')

                """if include_in_output:
                    parameters = ', '.join([format(u, '08X') for u in entry_parameters])
                    if parameters != '':
                        parameters += ', '
                    parameters += json.dumps(entry_content.decode('shift_jis', 'replace').encode('utf-8'), ensure_ascii=False).replace('\\u0000', '\\0')
                    print '    0x' + format(i, '08X') + ': %s' % entry_size, 'func_' + format(entry_type, '04X') + '(' + parameters + ')'
                """

                # Add entry
                self.entries.append((entry_type, entry_parameters, entry_content))

    def save(self, file_path):
        with open(file_path, 'wb') as f:
            file_size = common.get_file_size(f)

            # Write magic header
            f.write('.EVS')

            # Write the number of entries
            common.write_uint32(f, len(self.entries))
            
            # Write entry offsets
            # Size of header + size of entry table
            previous_entry_end = 8 + 4 * len(self.entries)
            converted_entries = []
            for (entry_type, entry_parameters, entry_content) in self.entries:
                # Write offset
                common.write_uint32(f, previous_entry_end)

                # Calculate the size of this entry,
                # so that we know when the next entry starts
                # Convert UTF8 to Shift-JIS
                try:
                    entry_content = entry_content.decode('utf-8').encode('shift_jis')
                except (UnicodeDecodeError, UnicodeEncodeError): 
                    raise Exception('There seems to be an character that cannot be converted to Shift_JIS. Check the text:' + entry_content)

                # Calculate the entry_size
                # parameters + content
                entry_size = 4 * len(entry_parameters) + len(entry_content)

                # Update previous_entry_end for the next iteration
                # Add 4 for the entry_type and entry_size fields, along with padding
                previous_entry_end += common.align_size(4 + entry_size, 4)

                # Add the entry to the converted entries
                converted_entries.append((entry_type, entry_size, entry_parameters, entry_content))

            # Loop through entries
            for (entry_type, entry_size, entry_parameters, entry_content) in converted_entries:

                # Write entry type
                common.write_uint16(f, entry_type)

                # Write entry size
                common.write_uint16(f, entry_size)

                # Write the parameters
                for entry_parameter in entry_parameters:
                    common.write_uint32(f, entry_parameter)
                
                # Write the content
                f.write(entry_content)

                # Add padding
                entry_padding = (common.align_size(entry_size, 4) - entry_size)
                f.write('\0' * entry_padding)

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
            f.write(json.dumps(data, indent=4, ensure_ascii=False))

    def import_evs(self, file_path):
        
        # Check if the input file exists
        if not os.path.exists(file_path):
            raise Exception('File does not exist: %s' % file_path)

        # Load the JSON
        data = ''
        with open(file_path, 'rb') as f:
            data = f.read()

        try:
            data = json.loads(data)
        except:
            raise Exception('File has invalid JSON data: %s' % file_path)

        # Populate the instance
        self.entries = []

        # Reprocess entries
        for entry in data['entries']:
            
            entry_type = entry['function']
            entry_parameters = entry['parameters']
            entry_content = entry['content']

            # Convert unicode to UTF-8
            entry_content = entry_content.encode('utf-8')

            # Convert trailing \0's to a single \0
            entry_content = re.sub('\0+$', r'\0', entry_content)

            # Add this string to the array
            self.entries.append((entry_type, entry_parameters, entry_content))

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print 'evs.py <action> <file.evs>'
        print ''
        print 'evs.py --export <file.evs>           # Output is file.evs.EVS.json'
        print 'evs.py --import <file.evs.EVS.json>  # Output is file.evs'
        sys.exit(0)

    action = sys.argv[1]
    input_path = sys.argv[2]
    output_path = ''

    if len(input_path) == 0:
        print 'Error: Empty input path provided'
        sys.exit(-1)

    if action in ('-i', '--info'):
        #try:
            print '%s:' % input_path
            evs_wrapper = EvsWrapper()
            evs_wrapper.open(input_path)
            evs_wrapper.save(input_path + '.TEST')
            #evs.info()
        
        #except Exception, e:
        #   print 'Error: %s' % e
        #   sys.exit(-1)

    if action in ('-e', '--export'):
        try:
            print '# Exporting %s:' % input_path

            evs_wrapper = EvsWrapper()
            evs_wrapper.open(input_path)

            evs_wrapper.export_evs(input_path)

        except Exception, e:
            print 'Error: %s' % e
            sys.exit(-1)

    elif action in ('-i', '--import'):
        try:
            print '# Importing %s:' % input_path
            evs_wrapper = EvsWrapper()
            evs_wrapper.import_evs(input_path)

            # Figure out the output path
            output_path = input_path

            suffix = '.EVS.json'
            if not output_path.endswith(suffix):
                raise Exception('Input path must have a suffix of %s' % suffix)
            output_path = output_path[:-len(suffix)]

            # Save
            evs_wrapper.save(output_path)

        except Exception, e:
            print 'Error: %s' % e
            sys.exit(-1)


    else:
        print 'Error: Unknown action: %s' % action
        sys.exit(-1)

    sys.exit(0)
