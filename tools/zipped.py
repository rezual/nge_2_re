#!/usr/bin/env python3

import sys
import os
import common
import zlib

class ZipWrapper(object):
    def __init__(self):
        self.size = 0
        self.content = b''

    def open(self, file_path):
        with open(file_path, 'rb') as f:
            self.size = common.read_uint32(f)
            self.content = f.read()

    def save(self, file_path):
         with open(file_path, 'wb') as f:
            common.write_uint32(f, self.size)
            result = zlib.compress(self.content)
            #Skip 2 byte header and four byte checksum at end
            f.write(result[2:-4])
            
    def compress_from(self, file_path):
        with open(file_path, 'rb') as f:
            self.content = f.read()
            self.size = len(self.content)

    def decompress_as(self, file_path):
        result = zlib.decompress(self.content, -15)
        with open(file_path, 'wb') as f:
            aligned_size = common.align_size(len(result), 4)
            f.write((result + b'\0\0\0\0')[:aligned_size])

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print('zipped.py <action> <file>')
        print('')
        print('zipped.py -d,--decompress <file>            # Output is file.DECOMPRESSED')
        print('zipped.py -c,--compress <file.DECOMPRESSED> # Input is file.DECOMPRESSED')
        sys.exit(0)

    action = sys.argv[1]
    input_path = os.path.normpath(sys.argv[2])
    output_path = ''

    try:
        if len(input_path) == 0:
            raise Exception('Empty input path provided')

        if action in ('-d', '--decompress'):
            print('# Decompressing %s:' % input_path)
            zip_wrapper = ZipWrapper()
            zip_wrapper.open(input_path)

            output_path = input_path + '.DECOMPRESSED'
            zip_wrapper.decompress_as(output_path)

        elif action in ('-c', '--compress'):
            print('# Compressing %s:' % input_path)
            zip_wrapper = ZipWrapper()
            
            suffix = '.DECOMPRESSED'
            if not input_path.lower().endswith(suffix.lower()):
                raise Exception('Input path must have a suffix of %s' % suffix)
            output_path = input_path[:-len(suffix)]

            zip_wrapper.compress_from(input_path)
            zip_wrapper.save(output_path)

        else:
            raise Exception('Unknown action: %s' % action)
            
    except Exception as e:
        import traceback

        print('Error: %s' % e)
        traceback.print_exc()
        sys.exit(-1)

    sys.exit(0)
