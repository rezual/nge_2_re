#!/usr/bin/env python3

import os
import sys
import json

from hgpt import HgptWrapper
from evs import EvsWrapper
from zipped import ZipWrapper
from bind import BindArchive
from text import TextArchive
from wave import WaveArchive
from hgar import HGArchive

def unpack_dir(directory_path):
    num_changed = 0

    for filename in os.listdir(directory_path):
        combined_path = os.path.join(directory_path, filename)

        if os.path.isdir(combined_path):
            # Skip looping through the WAVEPACKs
            if filename in ('na0.bin.WAVEPACK', 'na1.bin.WAVEPACK', 'na2.bin.WAVEPACK'):
                continue

            num_changed += unpack_dir(combined_path)

        elif filename.endswith(".har"): 
            if not os.path.exists(combined_path + '.HGARPACK'):
                print(combined_path)
                num_changed += 1

                hgar = HGArchive()
                hgar.open(combined_path)
                
                output_path = combined_path + '.HGARPACK' + os.sep

                if not os.path.exists(output_path):
                    os.makedirs(output_path)

                for file in hgar.files:
                    print('# Extracting: ' + file.get_viable_name())

                    with open(output_path + file.get_viable_name(), 'wb') as w:
                        w.write(file.content)

                    # Decompress as well?
                    if file.is_compressed:
                        zip_wrapper = ZipWrapper()
                        zip_wrapper.open(output_path + file.get_viable_name())
                        zip_wrapper.decompress_as(output_path + file.get_viable_name() + '.DECOMPRESSED')

        elif filename.endswith(".zpt"):
            if not os.path.exists(combined_path + '.DECOMPRESSED'):
                print(combined_path)
                num_changed += 1

                zip_wrapper = ZipWrapper()
                zip_wrapper.open(combined_path)
                zip_wrapper.decompress_as(combined_path + '.DECOMPRESSED')

        elif filename.endswith(".hpt.DECOMPRESSED") or (filename.endswith(".zpt.DECOMPRESSED") and filename != 'im059800.zpt.DECOMPRESSED'):
            if not os.path.exists(combined_path + '.PICTURE.png'):
                print(combined_path)
                num_changed += 1

                hgpt_wrapper = HgptWrapper()
                hgpt_wrapper.open(combined_path)
                hgpt_wrapper.export_hgpt(combined_path)
                
        elif filename.endswith(".evs"):
            if not os.path.exists(combined_path + '.EVS.json'):
                print(combined_path)
                num_changed += 1

                evs_wrapper = EvsWrapper()
                evs_wrapper.open(combined_path)
                evs_wrapper.export_evs(combined_path)

        elif filename.endswith('bin'):
            header_code = ''
            
            with open(combined_path, 'rb') as f:
                header_code = f.read(4).decode('ascii', 'ignore')

            if header_code == 'RIFF':
                if not os.path.exists(combined_path + '.WAVEPACK'):
                    print(combined_path)
                    num_changed += 1

                    wave_archive = WaveArchive()
                    wave_archive.open(combined_path)

                    output_path = combined_path + '.WAVEPACK' + os.sep
                    if not os.path.exists(output_path):
                        os.makedirs(output_path)

                    wave_archive.unpack(output_path)

            elif header_code == 'BIND':
                 if not os.path.exists(combined_path + '.BINDPACK'):
                    print(combined_path)
                    num_changed += 1

                    bind_archive = BindArchive()
                    bind_archive.open(combined_path)

                    output_path = combined_path + '.BINDPACK' + os.sep
                    if not os.path.exists(output_path):
                        os.makedirs(output_path)

                    bind_archive.unpack(output_path)

            elif header_code == 'TEXT':
                if not os.path.exists(combined_path + '.TEXT.json') and filename != '1048.bin':
                    print(combined_path)
                    num_changed += 1

                    text_archive = TextArchive()
                    text_archive.open(combined_path)
                    text_archive.export_text(combined_path)

            elif header_code == 'CODE':
                pass

        continue

    return num_changed


if __name__ == '__main__':
    import sys

    print('NGE2 content unpacker')
    print('unpack-all.py <path to umd_data.bin>')

    umd_data_bin_path = None
    if len(sys.argv) >= 2:
        umd_data_bin_path = os.path.normpath(sys.argv[1])

    while True:
        if umd_data_bin_path:

            if not os.path.exists(umd_data_bin_path):
                print('Error: "%s" does not exist' % umd_data_bin_path)
                umd_data_bin_path = None
                continue

            with open(umd_data_bin_path, 'rb') as f:
                data = f.read().decode('ascii', 'ignore')
                umd_id = data.split('|')[0]

                if umd_id != 'ULJS-00064':
                    raise Exception('Error: This is not NGE2, expected to see ID ULJS-00064 in the umd_data.bin file, instead saw %s' % umd_id)

                break

        umd_data_bin_path = input("Please enter the path to the UMD_DATA.BIN file (drag and drop it here):\n")
        if umd_data_bin_path == '':
            print('Blank inputted, exiting')
            sys.exit(0)
    
    umd_path = os.path.join(os.path.dirname(umd_data_bin_path), 'PSP_GAME', 'USRDIR')

    if not os.path.exists(umd_path):
        raise Exception('Error: The file path "%s" does not exist!' % umd_path)

    print('Unpacking all from:', umd_path)
    while unpack_dir(umd_path) != 0:
        pass

    print('Success')

    sys.exit(0)