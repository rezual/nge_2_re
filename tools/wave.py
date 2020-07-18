#!/usr/bin/env python3

import os
import common

class WaveEntry(object):
    def __init__(self, content):
        self.content = content

    def get_size(self):
        return len(self.content)

class WaveArchive(object):
    # Wave .bin archives align content to 0x800 byte blocks
    BLOCK_SIZE = 0x800

    def __init__(self):
        self.entries = []

    def add_entry(self, content):
        new_entry = WaveEntry(content)
        self.entries.append(new_entry)
        return new_entry

    def get_total_entries(self):
        return len(self.entries)

    def open(self, file_path):
        with open(file_path, 'rb') as f:
            archive_size = common.get_file_size(f)
            while f.tell() < archive_size:
                magic_number = f.read(4).decode('ascii', 'ignore')
                if magic_number != 'RIFF':
                    raise Exception('Not a WAVE entry!')

                wave_size = common.read_uint32(f) + 8
                f.seek(-8, os.SEEK_CUR)
                
                content = f.read(wave_size)
                new_entry = self.add_entry(content)

                # Find how many blocks are needed to contain wave_size
                # and skip that amount of remaining bytes
                block_aligned_wave_size = common.align_size(wave_size, WaveArchive.BLOCK_SIZE)
                f.seek(block_aligned_wave_size - wave_size, os.SEEK_CUR)

    def save(self, file_path):
        with open(file_path, 'wb') as f:
            counter = 0
            offset = 0
            for entry in self.entries:
                wave_size = entry.get_size()
                block_aligned_wave_size = common.align_size(wave_size, WaveArchive.BLOCK_SIZE)
            
                print('#\tWriting entry %s at offset 0x%X, size %s' % (counter, offset, wave_size))
                f.write(entry.content)

                padding_size = block_aligned_wave_size - wave_size
                f.write(b'\0' * padding_size)
            
                counter += 1
                offset += block_aligned_wave_size

    def unpack(self, file_path):
        counter = 0
        for entry in self.entries:
            output_file = os.path.join(file_path, ('%s.wav' % counter))
            
            print('#\tWriting %s:' % output_file)

            with open(output_file, 'wb') as w:
                w.write(entry.content)

            counter += 1

    def pack(self, file_path):
        counter = 0
        while True:
            input_file = os.path.join(file_path, ('%s.wav' % counter))
            
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
        print('wave.py <action> <archive.bin>')
        print('')
        print('wave.py -u,--unpack <archive.bin>        # Output is dir archive.bin.WAVEPACK')
        print('wave.py -p,--pack <archive.bin.WAVEPACK> # Output is file archive.bin')
        sys.exit(0)

    action = sys.argv[1]
    input_path = os.path.normpath(sys.argv[2])
    output_path = ''

    try:
        if len(input_path) == 0:
            raise Exception('Empty input path provided')

        if action in ('-u', '--unpack'):
            print('# Unpacking %s:' % input_path)
            wave_archive = WaveArchive()
            wave_archive.open(input_path)

            output_path = input_path + '.WAVEPACK'
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            wave_archive.unpack(output_path)

        elif action in ('-p', '--pack'):
            print('# Packing %s:' % input_path)
            wave_archive = WaveArchive()

            suffix = '.WAVEPACK'
            if not input_path.lower().endswith(suffix.lower()):
                raise Exception('Input path must have a suffix of %s' % suffix)
            output_path = input_path[:-len(suffix)]

            wave_archive.pack(input_path)
            wave_archive.save(output_path)

        else:
            raise Exception('Unknown action: %s' % action)
            
    except Exception as e:
        import traceback

        print('Error: %s' % e)
        traceback.print_exc()
        sys.exit(-1)

    sys.exit(0)
