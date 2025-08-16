#!/usr/bin/env python3

import os
import common

class BindEntry(object):
    def __init__(self, content):
        self.content = content

    def get_size(self):
        return len(self.content)

class BindArchive(object):
    def __init__(self):
        self.size_byte_size = 4
        self.block_size = 2048
        self.entries = []

    def add_entry(self, content):
        new_entry = BindEntry(content)
        self.entries.append(new_entry)
        return new_entry

    def open(self, file_path):
        with open(file_path, 'rb') as f:
            file_size = common.get_file_size(f)

            # Read magic header
            magic_number = f.read(4).decode('ascii', 'ignore')
            if magic_number != 'BIND':
                raise Exception('Not a BIND file! Missing BIND header id.')

            # Read "size" byte size
            # This determines what's the "size" of the size variable itself
            self.size_byte_size = common.read_uint16(f)
            if self.size_byte_size not in (1, 2, 4):
                raise Exception('Illegal BIND size byte size: %s' % self.index_size)
            
            # Read number of entries
            number_of_entries = common.read_uint16(f)

            # Read block size
            self.block_size = common.read_uint32(f)

            # Read header size
            header_size = common.read_uint32(f)

            # The header size is:
            # (16 + number of entries * self.size_byte_size) aligned to self.block_size
            
            # Load the entry sizes 
            processed_entries = []
            previous_entry_end = header_size
            for i in range(0, number_of_entries):
                # Calculate the offset of this entry based on the end of the previous entry
                entry_offset = previous_entry_end

                # Read the entry size
                entry_size = 0
                if self.size_byte_size == 1:
                    entry_size = common.read_uint8(f)

                elif self.size_byte_size == 2:
                    entry_size = common.read_uint16(f)

                elif self.size_byte_size == 4:
                    entry_size = common.read_uint32(f)

                # Calculate how much memory this entry takes
                entry_padded_size = common.align_size(entry_size, self.block_size)

                # Update previous_entry_end for the next iteration
                previous_entry_end += entry_padded_size 
            
                # Add the entry to processed entries
                processed_entries.append((entry_offset, entry_size))

            # Read entries
            for (entry_offset, entry_size) in processed_entries:
                f.seek(entry_offset)

                content = f.read(entry_size)
                new_entry = self.add_entry(content)

    def save(self, file_path):
        with open(file_path, 'wb') as f:
 
            # Write magic header
            f.write(b'BIND')

            # Write "size" byte size
            # This determines what's the "size" of the size variable itself
            common.write_uint16(f, self.size_byte_size)
            
            # Write the number of entries
            common.write_uint16(f, len(self.entries))

            # Write block size
            common.write_uint32(f, self.block_size)

            # Calculate header size, and padding
            # The header size is:
            # (16 + number of entries * self.size_byte_size) aligned to self.block_size
            header_size = 16 + len(self.entries) * self.size_byte_size
            padded_header_size = common.align_size(header_size, self.block_size)

            # Write header size
            common.write_uint32(f, padded_header_size)
            
            # Write the entry sizes 
            for entry in self.entries:
                # Write the entry size
                if self.size_byte_size == 1:
                    common.write_uint8(f, entry.get_size())

                elif self.size_byte_size == 2:
                    common.write_uint16(f, entry.get_size())

                elif self.size_byte_size == 4:
                    common.write_uint32(f, entry.get_size())

            # Insert padding
            f.write(b'\0' * (padded_header_size - header_size))

            # Write entries
            for entry in self.entries:
                entry_size = entry.get_size()
                padded_entry_size = common.align_size(entry_size, self.block_size)

                f.write(entry.content)
                f.write(b'\0' * (padded_entry_size - entry_size))

    def unpack(self, file_path):
        counter = 0
        for entry in self.entries:
            output_file = os.path.join(file_path, ('%s.bin' % counter))

            print('#\tWriting %s:' % output_file)

            with open(output_file, 'wb') as w:
                w.write(entry.content)

            counter += 1

    def pack(self, file_path):
        counter = 0
        while True:
            input_file = os.path.join(file_path, ('%s.bin' % counter))

            print('#\tReading %s:' % input_file)

            if not os.path.exists(input_file):
                print('#\t\tDoesn\'t exist, no more files to pack')
                break

            with open(input_file, 'rb') as f:
                content = f.read()
            
            self.add_entry(content)
            counter += 1

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('bind.py <action> <archive.bin>')
        print('')
        print('bind.py -u,--unpack <archive.bin>        # Output is dir archive.bin.BINDPACK')
        print('bind.py -p,--pack <archive.bin.BINDPACK> # Output is file archive.bin')
        sys.exit(0)

    action = sys.argv[1]
    input_path = os.path.normpath(sys.argv[2])
    output_path = ''

    try:
        if len(input_path) == 0:
            raise Exception('Empty input path provided')

        if action in ('-u', '--unpack'):
            print('# Unpacking %s:' % input_path)
            bind_archive = BindArchive()
            bind_archive.open(input_path)

            output_path = input_path + '.BINDPACK'
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            bind_archive.unpack(output_path)

        elif action in ('-p', '--pack'):
            print('# Packing %s:' % input_path)
            bind_archive = BindArchive()

            suffix = '.BINDPACK'
            if not input_path.lower().endswith(suffix.lower()):
                raise Exception('Input path must have a suffix of %s' % suffix)
            output_path = input_path[:-len(suffix)]

            bind_archive.pack(input_path)
            bind_archive.save(output_path)

        else:
            raise Exception('Unknown action: %s' % action)

    except Exception as e:
        import traceback

        print('Error: %s' % e)
        traceback.print_exc()
        sys.exit(-1)

    sys.exit(0)
