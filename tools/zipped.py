#!/usr/bin/env python2.7

import sys
import os
import struct

class WordPlay(object):
        REVERSE_BYTE_BITS = (0x00, 0x80, 0x40, 0xC0, 0x20, 0xA0, 0x60, 0xE0, 0x10, 0x90, 0x50, 0xD0, 0x30, 0xB0, 0x70, 0xF0, 
                                                 0x08, 0x88, 0x48, 0xC8, 0x28, 0xA8, 0x68, 0xE8, 0x18, 0x98, 0x58, 0xD8, 0x38, 0xB8, 0x78, 0xF8, 
                                                 0x04, 0x84, 0x44, 0xC4, 0x24, 0xA4, 0x64, 0xE4, 0x14, 0x94, 0x54, 0xD4, 0x34, 0xB4, 0x74, 0xF4, 
                                                 0x0C, 0x8C, 0x4C, 0xCC, 0x2C, 0xAC, 0x6C, 0xEC, 0x1C, 0x9C, 0x5C, 0xDC, 0x3C, 0xBC, 0x7C, 0xFC, 
                                                 0x02, 0x82, 0x42, 0xC2, 0x22, 0xA2, 0x62, 0xE2, 0x12, 0x92, 0x52, 0xD2, 0x32, 0xB2, 0x72, 0xF2, 
                                                 0x0A, 0x8A, 0x4A, 0xCA, 0x2A, 0xAA, 0x6A, 0xEA, 0x1A, 0x9A, 0x5A, 0xDA, 0x3A, 0xBA, 0x7A, 0xFA, 
                                                 0x06, 0x86, 0x46, 0xC6, 0x26, 0xA6, 0x66, 0xE6, 0x16, 0x96, 0x56, 0xD6, 0x36, 0xB6, 0x76, 0xF6, 
                                                 0x0E, 0x8E, 0x4E, 0xCE, 0x2E, 0xAE, 0x6E, 0xEE, 0x1E, 0x9E, 0x5E, 0xDE, 0x3E, 0xBE, 0x7E, 0xFE, 
                                                 0x01, 0x81, 0x41, 0xC1, 0x21, 0xA1, 0x61, 0xE1, 0x11, 0x91, 0x51, 0xD1, 0x31, 0xB1, 0x71, 0xF1, 
                                                 0x09, 0x89, 0x49, 0xC9, 0x29, 0xA9, 0x69, 0xE9, 0x19, 0x99, 0x59, 0xD9, 0x39, 0xB9, 0x79, 0xF9, 
                                                 0x05, 0x85, 0x45, 0xC5, 0x25, 0xA5, 0x65, 0xE5, 0x15, 0x95, 0x55, 0xD5, 0x35, 0xB5, 0x75, 0xF5, 
                                                 0x0D, 0x8D, 0x4D, 0xCD, 0x2D, 0xAD, 0x6D, 0xED, 0x1D, 0x9D, 0x5D, 0xDD, 0x3D, 0xBD, 0x7D, 0xFD, 
                                                 0x03, 0x83, 0x43, 0xC3, 0x23, 0xA3, 0x63, 0xE3, 0x13, 0x93, 0x53, 0xD3, 0x33, 0xB3, 0x73, 0xF3, 
                                                 0x0B, 0x8B, 0x4B, 0xCB, 0x2B, 0xAB, 0x6B, 0xEB, 0x1B, 0x9B, 0x5B, 0xDB, 0x3B, 0xBB, 0x7B, 0xFB, 
                                                 0x07, 0x87, 0x47, 0xC7, 0x27, 0xA7, 0x67, 0xE7, 0x17, 0x97, 0x57, 0xD7, 0x37, 0xB7, 0x77, 0xF7, 
                                                 0x0F, 0x8F, 0x4F, 0xCF, 0x2F, 0xAF, 0x6F, 0xEF, 0x1F, 0x9F, 0x5F, 0xDF, 0x3F, 0xBF, 0x7F, 0xFF)

        REPLACE_BYTE_INDEX = (0xFFFFFF00, 0xFFFF00FF, 0xFF00FFFF, 0x00FFFFFF)
        REPLACE_HWORD_INDEX = (0xFFFF0000, 0x0000FFFF)

        @staticmethod
        def sanitize_byte(byte_value):
                return byte_value & 0xFF

        @staticmethod
        def sanitize_hword(hword_value):
                return hword_value & 0xFFFF

        @staticmethod
        def sanitize_word(word_value):
                return word_value & 0xFFFFFFFF

        @staticmethod
        def sign_extend_byte(byte_value):
                if byte_value & 0x80:
                        return (byte_value & 0x7F) | 0xFFFFFF80
                return byte_value

        @staticmethod
        def zero_extend_byte(byte_value):
                return byte_value

        @staticmethod
        def sign_extend_hword(hword_value):
                if hword_value & 0x8000:
                        return (hword_value & 0x7FFF) | 0xFFFF8000
                return hword_value

        @staticmethod
        def zero_extend_hword(hword_value):
                return hword_value

        @staticmethod
        def not_byte(byte_value):
                # Python's ~ takes into account sign
                return 0xFF - byte_value

        @staticmethod
        def not_hword(hword_value):
                # Python's ~ takes into account sign
                return 0xFFFF - hword_value

        @staticmethod
        def not_word(word_value):
                # Python's ~ takes into account sign
                return 0xFFFFFFFF - word_value

        @staticmethod
        def as_bytes(word_value):
                return ((word_value >> 24) & 0xFF, (word_value >> 16) & 0xFF, (word_value >> 8) & 0xFF, word_value & 0xFF)

        @staticmethod
        def from_bytes(a, b, c, d):
                return (a << 24) | (b << 16) | (c << 8) | d

        @staticmethod
        def as_hwords(word_value):
                return ((word_value >> 16) & 0xFFFF, word_value & 0xFFFF)

        @staticmethod
        def from_hwords(a, b):
                return (a << 16) | b

        @staticmethod
        def get_byte(word_value, byte_index):
                bit_shift = 8 * byte_index
                return (word_value >> bit_shift) & 0xFF

        @staticmethod
        def get_hword(word_value, hword_index):
                bit_shift = 16 * hword_index
                return (word_value >> bit_shift)  & 0xFFFF

        @staticmethod
        def replace_byte(word_value, byte_index, byte_value):
                bit_shift = 8 * byte_index
                return (word_value & WordPlay.REPLACE_BYTE_INDEX[byte_index]) | (byte_value << bit_shift)

        @staticmethod
        def replace_hword(word_value, hword_index, hword_value):
                bit_shift = 16 * hword_index
                return (word_value & WordPlay.REPLACE_HWORD_INDEX[hword_index]) | (hword_value << bit_shift)

        @staticmethod
        def reverse_word(word_value):
                a, b, c, d = WordPlay.as_bytes(word_value)
                return WordPlay.from_bytes(WordPlay.REVERSE_BYTE_BITS[d], WordPlay.REVERSE_BYTE_BITS[c], WordPlay.REVERSE_BYTE_BITS[b], WordPlay.REVERSE_BYTE_BITS[a])

        @staticmethod
        def arithmetic_shift_left(word_value, shift_amount):
                return WordPlay.sanitize_word(word_value << shift_amount)

        @staticmethod
        def logical_shift_left(word_value, shift_amount):
                return WordPlay.sanitize_word(word_value << shift_amount)

        @staticmethod
        def arithmetic_shift_right(word_value, shift_amount):
                return WordPlay.sanitize_word(WordPlay.as_signed(word_value) >> shift_amount)

        @staticmethod
        def logical_shift_right(word_value, shift_amount):
                return word_value >> shift_amount

        @staticmethod
        def rotate_left(word_value, rotate_amount):
                return WordPlay.sanitize_word((word_value << rotate_amount) | (word_value >> (32 - rotate_amount)))

        @staticmethod
        def rotate_right(word_value, rotate_amount):
                return WordPlay.sanitize_word((word_value << (32 - rotate_amount)) | (word_value >> rotate_amount))

        @staticmethod
        def count_leading_zeroes(word_value):
                mask = (1 << 31)
                counter = 0
                while mask:
                        if (word_value & mask):
                                return counter
                        mask >>= 1
                        counter += 1
                return 32

        @staticmethod
        def as_signed(word_value):
                if word_value & 0x80000000:
                        return -(WordPlay.not_word(word_value) + 1)
                return word_value

class Memory(object):
        def __init__(self, memory_miss_handler=None):
                self.content = {}
                self.default = 0x00000000
                self.memory_miss_handler = memory_miss_handler

        @staticmethod
        def _get_aligned_address(address):
                return address & 0xFFFFFFFC

        def load_file(self, file_path, base_address):

                file_size = 0

                with open(file_path, 'rb') as f:
                        file_size = os.fstat(f.fileno()).st_size
                        
                        address = base_address
                        counter = file_size
                        word_value = 0

                        while counter > 0:
                                if counter >= 4:
                                        word_value = f.read(4)
                                        counter -= 4

                                else:
                                        word_value = f.read(counter) + ('\0' * (4 - counter))
                                        counter = 0

                                word_value = struct.unpack('I', word_value)[0]

                                self.set_word(address, word_value)
                                address += 4

                return file_size

        def _shared_word_get(self, address):
                try:
                        return self.content[address]

                except KeyError:
                        if self.memory_miss_handler is None:
                                return self.default

                        return self.memory_miss_handler(self, address, self.default)

                raise Exception('Memory Read entered bad state')

        def get_word(self, address):
                aligned_address = Memory._get_aligned_address(address)
                return self._shared_word_get(aligned_address)

        def get_hword(self, address):
                aligned_address = Memory._get_aligned_address(address)
                word_value = self._shared_word_get(aligned_address)
                return WordPlay.get_hword(word_value, (address >> 1) & 1)

        def get_byte(self, address):
                aligned_address = Memory._get_aligned_address(address)
                word_value = self._shared_word_get(aligned_address)
                return WordPlay.get_byte(word_value, address & 3)

        def set_word(self, address, word_value):
                aligned_address = Memory._get_aligned_address(address)
                self.content[aligned_address] = word_value & 0xFFFFFFFF

        def set_hword(self, address, hword_value):
                aligned_address = Memory._get_aligned_address(address)
                word_value = self._shared_word_get(aligned_address)
                self.content[aligned_address] = WordPlay.replace_hword(word_value, (address >> 1) & 1, hword_value & 0xFFFF)

        def set_byte(self, address, byte_value):
                aligned_address = Memory._get_aligned_address(address)
                word_value = self._shared_word_get(aligned_address)
                self.content[aligned_address] = WordPlay.replace_byte(word_value, address & 3, byte_value & 0xFF)

class ZipWrapper(object):
        def __init__(self):
                self.memory = Memory()

                # Decompression routine look-up-tables
                self.memory.content[0x001B1380] = 0xFFCEFFF9
                self.memory.content[0x001B1384] = 0x1310FE3C
                self.memory.content[0x001B1388] = 0x0708001B
                self.memory.content[0x001B138C] = 0x050A0609
                self.memory.content[0x001B1390] = 0x030C040B
                self.memory.content[0x001B1394] = 0x010E020D
                self.memory.content[0x001B1398] = 0x0000000F
                self.memory.content[0x001B139C] = 0x00180000
                self.memory.content[0x001B13A0] = 0x020000C8
                self.memory.content[0x001B13A4] = 0x00000000
                self.memory.content[0x001B13A8] = 0x00000000
                self.memory.content[0x001B13AC] = 0x00000000
                self.memory.content[0x001B13B0] = 0x00000000
                self.memory.content[0x001B13B4] = 0x00000000
                self.memory.content[0x001B13B8] = 0x00000000
                self.memory.content[0x001B13BC] = 0xFFD0FFE7
                self.memory.content[0x001B13C0] = 0xFFB0FFC0
                self.memory.content[0x001B13C4] = 0xFF90FFA0
                self.memory.content[0x001B13C8] = 0xFF70FF80
                self.memory.content[0x001B13CC] = 0xFF5FFF60
                self.memory.content[0x001B13D0] = 0xFF1FFF3F
                self.memory.content[0x001B13D4] = 0xFED7FEFF
                self.memory.content[0x001B13D8] = 0xFE57FE97
                self.memory.content[0x001B13DC] = 0xFDDBFE17
                self.memory.content[0x001B13E0] = 0xFCDBFD5B
                self.memory.content[0x001B13E4] = 0xFBD3FC5B
                self.memory.content[0x001B13E8] = 0xF9D3FAD3
                self.memory.content[0x001B13EC] = 0xF7DDF8D3
                self.memory.content[0x001B13F0] = 0xF3DDF5DD
                self.memory.content[0x001B13F4] = 0xEFE0F1DD
                self.memory.content[0x001B13F8] = 0xFFFFFFFF
                self.memory.content[0x001B13FC] = 0x00010000
                self.memory.content[0x001B1400] = 0x00030002
                self.memory.content[0x001B1404] = 0x00060004
                self.memory.content[0x001B1408] = 0x000C0008
                self.memory.content[0x001B140C] = 0x00180010
                self.memory.content[0x001B1410] = 0x00300020
                self.memory.content[0x001B1414] = 0x00600040
                self.memory.content[0x001B1418] = 0x00C00080
                self.memory.content[0x001B141C] = 0x01800100
                self.memory.content[0x001B1420] = 0x03000200
                self.memory.content[0x001B1424] = 0x06000400
                self.memory.content[0x001B1428] = 0x0C000800
                self.memory.content[0x001B142C] = 0x18001000
                self.memory.content[0x001B1430] = 0x30002000
                self.memory.content[0x001B1434] = 0x60004000
                self.memory.content[0x001B1438] = 0xFFFBFFFB
                self.memory.content[0x001B143C] = 0x00000000

        def decompress(self, file_path):
                memory = self.memory

                input_buffer = 0x09E6A2E8
                output_buffer = 0x08F475C0

                # Initialize state
                reg_at = 0
                reg_v0 = 0
                reg_v1 = 0
                reg_a0 = 0
                reg_a1 = 0
                reg_a2 = 0
                reg_a3 = 0
                reg_t0 = 0
                reg_t1 = 0
                reg_t2 = 0
                reg_t3 = 0
                reg_t4 = 0
                reg_t5 = 0
                reg_t6 = 0
                reg_t7 = 0
                reg_s0 = 0
                reg_s1 = 0
                reg_s2 = 0
                reg_s3 = 0
                reg_s4 = 0
                reg_s5 = 0
                reg_s6 = 0
                reg_s7 = 0
                reg_t8 = 0
                reg_t9 = 0
                reg_k0 = 0
                reg_k1 = 0
                reg_gp = 0
                reg_sp = 0
                reg_fp = 0
                reg_ra = 0

                reg_lo = 0
                reg_hi = 0

                # Initial register setup
                reg_ra = 0x00062F68
                reg_sp = 0x09FF7390
                reg_fp = 0x00000001

                reg_pc = 0x3068

                # Load the file
                file_size = memory.load_file(file_path, input_buffer)
                file_size = 4 * int((file_size + 3) / 4)
                output_size = memory.content[input_buffer]

                reg_a0 = input_buffer + 4 # Input buffer + 4 bytes to skip output size
                reg_a1 = output_buffer # Output buffer
                reg_a2 = output_size # Decompressed size

                reg_v0 = 0

                while True:
                        if reg_pc == 0x3068: # decompression entry point, _start
                                reg_sp = (reg_sp - 0x20) & 0xFFFFFFFF           # 0x3068
                                reg_a2 = (reg_a0) & 0xFFFFFFFF                  # 0x306C
                                reg_a3 = (reg_sp) & 0xFFFFFFFF                  # 0x3070
                                reg_a0 = (reg_a1) & 0xFFFFFFFF                  # 0x3074
                                reg_a1 = 0x1000000                              # 0x3078
                                memory.set_word(reg_sp + 0x10, reg_ra)          # 0x307C
                                memory.set_word(reg_sp, 0)                      # 0x3084 (delayed: 0x3080)
                                reg_ra = 0x3088; reg_pc=0xA630; continue        # 0x3080

                        elif reg_pc == 0x3088: # decompression entry point, _end
                                reg_a0 = 1 if (WordPlay.as_signed(reg_v0) < 0) else 0     # 0x3088
                                reg_v0 = memory.get_word(reg_sp)                          # 0x308C
                                reg_ra = memory.get_word(reg_sp + 0x10)                   # 0x3090
                                if reg_a0 != 0: reg_v0 = 0                                # 0x3094
                                reg_sp = (reg_sp + 0x20) & 0xFFFFFFFF                     # 0x309C (delayed: 0x3098)
                                reg_pc=reg_ra; continue                                   # 0x3098

                        elif reg_pc == 0xA630: # decompression main, _start
                                reg_sp = (reg_sp - 0x380) & 0xFFFFFFFF          # 0xA630
                                memory.set_word(reg_sp + 0x308, reg_s4)         # 0xA634
                                reg_a1 = (reg_a0 + reg_a1) & 0xFFFFFFFF         # 0xA638
                                reg_t6 = (reg_a0) & 0xFFFFFFFF                  # 0xA63C
                                reg_t7 = 0x1B0000                               # 0xA640
                                reg_t7 = (reg_t7 + 0x1380) & 0xFFFFFFFF         # 0xA644
                                memory.set_word(reg_sp + 0x310, reg_ra)         # 0xA648
                                reg_pc=0xA64C; continue # to-next

                        elif reg_pc == 0xA64C:
                                reg_t9 = reg_a2 & 3                                     # 0xA64C
                                reg_a2 = (reg_a2 - reg_t9) & 0xFFFFFFFF                 # 0xA650
                                reg_t8 = memory.get_word(reg_a2)                        # 0xA654
                                reg_t9 = WordPlay.logical_shift_left(reg_t9, 3)         # 0xA658
                                reg_t9 = (reg_t9 - 0x20) & 0xFFFFFFFF                   # 0xA65C
                                reg_pc=0xA660; continue # to-next

                        elif reg_pc == 0xA660:
                                reg_t9 = (reg_t9 + 0x3) & 0xFFFFFFFF                    # 0xA660
                                reg_v0 = WordPlay.rotate_right(reg_t8, reg_t9 & 0x1F)   # 0xA668 (delayed: 0xA664)

                                if (WordPlay.as_signed(reg_t9) > 0):
                                        reg_pc=0xA710
                                        continue
                                # 0xA664

                                reg_pc=0xA66C; continue # to-next

                        elif reg_pc == 0xA66C:
                                reg_v1 = ((reg_v0 >> 30) & 0x3)         # 0xA66C
                                reg_t2 = ((reg_v0 >> 29) & 0x1)         # 0xA674 (delayed: 0xA670)

                                if (reg_v1 == 0):
                                        reg_pc=0xABD8
                                        continue
                                # 0xA670

                                reg_t0 = (reg_v1 - 0x2) & 0xFFFFFFFF            # 0xA678
                                memory.set_hword(reg_sp + 0x314, reg_t2)        # 0xA680 (delayed: 0xA67C)

                                if (reg_t0 == 0):
                                        reg_pc=0xA764
                                        continue
                                # 0xA67C

                                reg_t2 = (reg_sp) & 0xFFFFFFFF                  # 0xA688 (delayed: 0xA684)

                                if (WordPlay.as_signed(reg_t0) > 0):
                                        reg_pc=0xABC8
                                        continue
                                # 0xA684

                                reg_s4 = (reg_t7 + 0x6C) & 0xFFFFFFFF           # 0xA68C
                                
                                reg_pc=0xA690; continue # to-next

                        elif reg_pc == 0xA690:
                                reg_t3 = memory.get_word(reg_t7)                # 0xA690
                                reg_t2 = (reg_t2 + 0x4) & 0xFFFFFFFF            # 0xA694
                                reg_t7 = (reg_t7 + 0x4) & 0xFFFFFFFF            # 0xA698
                                memory.set_word(reg_t2 - 0x4, reg_t3)           # 0xA6A0 (delayed: 0xA69C)

                                if (reg_s4 != reg_t7):
                                        reg_pc=0xA690
                                        continue
                                # 0xA69C

                                reg_t1 = 0x0            # 0xA6A4
                                reg_s4 = 0x90           # 0xA6A8
                                
                                reg_pc=0xA6AC; continue # to-next

                        elif reg_pc == 0xA6AC:
                                memory.set_hword(reg_t2, reg_t1)                # 0xA6AC
                                reg_t1 = (reg_t1 + 0x1) & 0xFFFFFFFF            # 0xA6B0
                                reg_t2 = (reg_t2 + 0x2) & 0xFFFFFFFF            # 0xA6B8 (delayed: 0xA6B4)

                                if (reg_t1 != reg_s4):
                                        reg_pc=0xA6AC
                                        continue
                                # 0xA6B4
                                reg_s4 = (reg_t7 + 0x10) & 0xFFFFFFFF           # 0xA6BC
                                reg_pc=0xA6C0; continue # to-next

                        elif reg_pc == 0xA6C0:
                                reg_t3 = memory.get_word(reg_t7)                # 0xA6C0
                                reg_t2 = (reg_t2 + 0x4) & 0xFFFFFFFF            # 0xA6C4
                                reg_t7 = (reg_t7 + 0x4) & 0xFFFFFFFF            # 0xA6C8
                                memory.set_word(reg_t2 - 0x4, reg_t3)           # 0xA6D0 (delayed: 0xA6CC)

                                if (reg_s4 != reg_t7):
                                        reg_pc=0xA6C0
                                        continue
                                # 0xA6CC

                                reg_s4 = 0x11E          # 0xA6D4
                                reg_pc=0xA6D8; continue # to-next

                        elif reg_pc == 0xA6D8:
                                memory.set_hword(reg_t2, reg_t1)                # 0xA6D8
                                reg_t1 = (reg_t1 + 0x1) & 0xFFFFFFFF            # 0xA6DC
                                reg_t2 = (reg_t2 + 0x2) & 0xFFFFFFFF            # 0xA6E4 (delayed: 0xA6E0)

                                if (reg_t1 != reg_s4):
                                        reg_pc=0xA6D8
                                        continue
                                # 0xA6E0

                                reg_s4 = (reg_t7 + 0x40) & 0xFFFFFFFF           # 0xA6E8
                                reg_pc=0xA6EC; continue # to-next

                        elif reg_pc == 0xA6EC:
                                reg_t3 = memory.get_word(reg_t7)                # 0xA6EC
                                reg_t2 = (reg_t2 + 0x4) & 0xFFFFFFFF            # 0xA6F0
                                reg_t7 = (reg_t7 + 0x4) & 0xFFFFFFFF            # 0xA6F4
                                memory.set_word(reg_t2 - 0x4, reg_t3)           # 0xA6FC (delayed: 0xA6F8)

                                if (reg_s4 != reg_t7):
                                        reg_pc=0xA6EC
                                        continue
                                # 0xA6F8

                                reg_t7 = (reg_t7 - 0xBC) & 0xFFFFFFFF           # 0xA700
                                memory.set_hword(reg_sp + 0x29A, reg_t3)        # 0xA704
                                memory.set_hword(reg_sp + 0x27C, reg_t3)        # 0xA70C (delayed: 0xA708)
                                reg_pc=0xA838; continue                         # 0xA708

                        elif reg_pc == 0xA710:
                                reg_t8 = memory.get_word(reg_a2 + 0x4)                                          # 0xA710
                                reg_v0 = WordPlay.logical_shift_left(reg_v0, reg_t9 & 0x1F)                     # 0xA714
                                reg_a2 = (reg_a2 + 0x4) & 0xFFFFFFFF                                            # 0xA718
                                reg_t9 = (reg_t9 - 0x20) & 0xFFFFFFFF                                           # 0xA71C
                                reg_v0 = ((reg_v0 & 0xFFFF0000) | ((reg_t8 & 0xFFFF) << 0)) & 0xFFFFFFFF        # 0xA720
                                reg_v0 = WordPlay.rotate_right(reg_v0, reg_t9 & 0x1F)                           # 0xA728 (delayed: 0xA724)
                                reg_pc=0xA66C; continue                                                         # 0xA724

                        elif reg_pc == 0xA72C:
                                reg_t8 = memory.get_word(reg_a2 + 0x4)                                          # 0xA72C
                                reg_v0 = WordPlay.logical_shift_left(reg_v0, reg_t9 & 0x1F)                     # 0xA730
                                reg_a2 = (reg_a2 + 0x4) & 0xFFFFFFFF                                            # 0xA734
                                reg_t9 = (reg_t9 - 0x20) & 0xFFFFFFFF                                           # 0xA738
                                reg_v0 = ((reg_v0 & 0xFFFF0000) | ((reg_t8 & 0xFFFF) << 0)) & 0xFFFFFFFF        # 0xA73C
                                reg_v0 = WordPlay.rotate_right(reg_v0, reg_t9 & 0x1F)                           # 0xA744 (delayed: 0xA740)
                                reg_pc=0xA770; continue                                                         # 0xA740

                        elif reg_pc == 0xA748:
                                reg_t8 = memory.get_word(reg_a2 + 0x4)                                          # 0xA748
                                reg_v0 = WordPlay.logical_shift_left(reg_v0, reg_t9 & 0x1F)                     # 0xA74C
                                reg_a2 = (reg_a2 + 0x4) & 0xFFFFFFFF                                            # 0xA750
                                reg_t9 = (reg_t9 - 0x20) & 0xFFFFFFFF                                           # 0xA754
                                reg_v0 = ((reg_v0 & 0xFFFF0000) | ((reg_t8 & 0xFFFF) << 0)) & 0xFFFFFFFF        # 0xA758
                                reg_v0 = WordPlay.rotate_right(reg_v0, reg_t9 & 0x1F)                           # 0xA760 (delayed: 0xA75C)
                                reg_pc=0xA79C; continue                                                         # 0xA75C
                                
                        elif reg_pc == 0xA764: # in xyz, xy == 10
                                reg_t9 = (reg_t9 + 0xE) & 0xFFFFFFFF                            # 0xA764
                                reg_v0 = WordPlay.rotate_right(reg_t8, reg_t9 & 0x1F)           # 0xA76C (delayed: 0xA768)

                                if (WordPlay.as_signed(reg_t9) > 0):
                                        reg_pc=0xA72C
                                        continue
                                # 0xA768
                                
                                reg_pc=0xA770; continue # to-next

                        elif reg_pc == 0xA770:
                                memory.set_word(reg_sp + 0x35C, reg_v0)         # 0xA770
                                reg_s4 = ((reg_v0 >> 28) & 0xF)                 # 0xA774
                                reg_s4 = (reg_s4 + 0x4) & 0xFFFFFFFF            # 0xA778
                                reg_t3 = (reg_sp + 0x2F8) & 0xFFFFFFFF          # 0xA77C
                                reg_t0 = (reg_t7) & 0xFFFFFFFF                  # 0xA780
                                reg_s4 = (reg_s4 + reg_t7) & 0xFFFFFFFF         # 0xA784
                                reg_pc=0xA788; continue # to-next

                        elif reg_pc == 0xA788:
                                delay_t0 = reg_t0
                                reg_t0 = (reg_t0 + 0x1) & 0xFFFFFFFF                    # 0xA78C (hazard-jump-delay-slot: 0xA788)

                                if (delay_t0 == reg_s4):
                                        reg_pc=0xA7B8
                                        continue
                                # 0xA788

                                reg_t9 = (reg_t9 + 0x3) & 0xFFFFFFFF                    # 0xA790
                                reg_v0 = WordPlay.rotate_right(reg_t8, reg_t9 & 0x1F)   # 0xA798 (delayed: 0xA794)

                                if (WordPlay.as_signed(reg_t9) > 0):
                                        reg_pc=0xA748
                                        continue
                                # 0xA794
                                
                                reg_pc=0xA79C; continue # to-next

                        elif reg_pc == 0xA79C:
                                reg_v0 = WordPlay.logical_shift_right(reg_v0, 29)                       # 0xA79C
                                reg_t2 = WordPlay.sign_extend_byte(memory.get_byte(reg_t0 + 0x5))       # 0xA7A4 (delayed: 0xA7A0)

                                if (reg_v0 == 0):
                                        reg_pc=0xA788
                                        continue
                                # 0xA7A0

                                reg_t3 = (reg_t3 + 0x2) & 0xFFFFFFFF                                    # 0xA7A8
                                reg_t2 = ((reg_t2 & 0xFFFF81FF) | ((reg_v0 & 0x3F) << 9)) & 0xFFFFFFFF  # 0xA7AC
                                memory.set_hword(reg_t3 + 0x3A, reg_t2)                                 # 0xA7B4 (delayed: 0xA7B0)
                                reg_pc=0xA788; continue                                                 # 0xA7B0
                                
                        elif reg_pc == 0xA7B8:
                                reg_s4 = (reg_sp + 0x2F8) & 0xFFFFFFFF          # 0xA7BC (jump-delay-slot: 0xA7B8)
                                reg_ra = 0xA7C0; reg_pc=0xAB20; continue        # 0xA7B8

                        elif reg_pc == 0xA7C0:
                                reg_t5 = memory.get_word(reg_sp + 0x35C)        # 0xA7C0
                                reg_s4 = (reg_sp) & 0xFFFFFFFF                  # 0xA7C8 (delayed: 0xA7C4)

                                if (reg_t0 == 0):
                                        reg_pc=0xABA8
                                        continue
                                # 0xA7C4

                                reg_t5 = ((reg_t5 >> 18) & 0x1F)                # 0xA7CC
                                reg_t5 = (reg_t5 + 0x101) & 0xFFFFFFFF          # 0xA7D4 (delayed: 0xA7D0)
                                reg_ra = 0xA7D8; reg_pc=0xAA08; continue        # 0xA7D0

                        elif reg_pc == 0xA7D8:
                                delay_t0 = reg_t0
                                reg_t0 = (reg_sp) & 0xFFFFFFFF          # 0xA7DC (hazard-delayed: 0xA7D8)

                                if (delay_t0 == 0):
                                        reg_pc=0xABA8
                                        continue
                                # 0xA7D8
                                
                                reg_pc=0xA7E0; continue # to-next

                        elif reg_pc == 0xA7E0:
                                reg_t1 = WordPlay.sign_extend_hword(memory.get_hword(reg_t0 + 0x3C))    # 0xA7E0
                                reg_t0 = (reg_t0 + 0x2) & 0xFFFFFFFF                                    # 0xA7E4
                                reg_t2 = reg_t1 & 0xFF                                                  # 0xA7E8
                                
                                delay_t2 = reg_t2
                                reg_t2 = (reg_t2 + reg_t2) & 0xFFFFFFFF                                 # 0xA7F0 (hazard-delayed: 0xA7EC)

                                if (delay_t2 == reg_t1):
                                        reg_pc=0xA7FC
                                        continue
                                # 0xA7EC

                                reg_t2 = (reg_t2 + reg_t7) & 0xFFFFFFFF                                 # 0xA7F4
                                reg_t1 = WordPlay.sign_extend_hword(memory.get_hword(reg_t2 + 0x3C))    # 0xA7F8

                                reg_pc=0xA7FC; continue # to-next

                        elif reg_pc == 0xA7FC:
                                memory.set_hword(reg_t0 + 0x3A, reg_t1)         # 0xA800 (jump-delay-slot: 0xA7FC)

                                if (reg_t0 != reg_t3):
                                        reg_pc=0xA7E0
                                        continue
                                # 0xA7FC

                                reg_t5 = memory.get_word(reg_sp + 0x35C)        # 0xA804
                                reg_s4 = (reg_sp + 0x27C) & 0xFFFFFFFF          # 0xA808
                                reg_t5 = ((reg_t5 >> 23) & 0x1F)                # 0xA810 (delayed: 0xA80C)
                                reg_ra = 0xA814; reg_pc=0xAA04; continue        # 0xA80C

                        elif reg_pc == 0xA814:
                                reg_t0 = (reg_sp - 0x40) & 0xFFFFFFFF           # 0xA814
                                reg_pc=0xA818; continue # to-next

                        elif reg_pc == 0xA818:
                                reg_t1 = WordPlay.sign_extend_hword(memory.get_hword(reg_t0 + 0x2F8))   # 0xA818
                                reg_t1 &= 31                                                            # 0xA81C
                                reg_t1 = (reg_t1 + reg_t1) & 0xFFFFFFFF                                 # 0xA820
                                reg_t1 = (reg_t1 + reg_t7) & 0xFFFFFFFF                                 # 0xA824
                                reg_t1 = WordPlay.sign_extend_hword(memory.get_hword(reg_t1 + 0x7C))    # 0xA828
                                reg_t0 = (reg_t0 + 0x2) & 0xFFFFFFFF                                    # 0xA82C
                                memory.set_hword(reg_t0 + 0x2F6, reg_t1)                                # 0xA834 (delayed: 0xA830)

                                if (reg_t0 != reg_sp):
                                        reg_pc=0xA818
                                        continue
                                # 0xA830
                                
                                reg_pc=0xA838; continue # to-next

                        elif reg_pc == 0xA838:
                                reg_t2 = WordPlay.sign_extend_byte(memory.get_byte(reg_sp))     # 0xA838
                                reg_v1 = memory.get_hword(reg_sp + 0x1E)                        # 0xA83C
                                reg_t0 = (reg_sp + 0x2) & 0xFFFFFFFF                            # 0xA844 (delayed: 0xA840)
                                reg_ra = 0xA848; reg_pc=0xA978; continue                        # 0xA840
                                
                        elif reg_pc == 0xA848:
                                reg_t0 = (reg_sp + 0x27E) & 0xFFFFFFFF                          # 0xA848
                                reg_t2 = WordPlay.reverse_word(reg_v0)                          # 0xA84C
                                reg_s4 = WordPlay.arithmetic_shift_right(reg_v0, 4)             # 0xA854 (delayed: 0xA850)

                                if (WordPlay.as_signed(reg_v0) >= 0):
                                        reg_pc=0xA8D0
                                        continue
                                # 0xA850

                                reg_v1 = memory.get_hword(reg_sp + 0x29A)                       # 0xA85C (delayed: 0xA858)

                                if (WordPlay.as_signed(reg_t2) < 0):
                                        reg_ra = 0xA860
                                        reg_pc=0xA8FC
                                        continue
                                # 0xA858

                                reg_pc=0xA860; continue # to-next

                        elif reg_pc == 0xA860:
                                reg_t2 = WordPlay.sign_extend_byte(memory.get_byte(reg_sp + 0x27C))     # 0xA860
                                reg_at = (reg_a0 - reg_s4) & 0xFFFFFFFF                                 # 0xA868 (delayed: 0xA864)
                                reg_ra = 0xA86C; reg_pc=0xA978; continue                                # 0xA864

                        elif reg_pc == 0xA86C:
                                reg_s4 = 1 if (reg_a1 < reg_at) else 0                  # 0xA86C
                                reg_t2 = WordPlay.count_leading_zeroes(reg_v0)          # 0xA874 (delayed: 0xA870)

                                if (reg_s4 != 0):
                                        reg_pc=0xABB8
                                        continue
                                # 0xA870

                                reg_t2 = (reg_t2 - 0x1E) & 0xFFFFFFFF                   # 0xA878
                                reg_s4 = (reg_a0 - reg_v0) & 0xFFFFFFFF                 # 0xA880 (delayed: 0xA87C)

                                if (WordPlay.as_signed(reg_t2) < 0):
                                        reg_ra = 0xA884
                                        reg_pc=0xA8E0
                                        continue
                                # 0xA87C

                                reg_pc=0xA884; continue # to-next

                        elif reg_pc == 0xA884:
                                reg_t2 = 1 if (reg_t6 < reg_s4) else 0          # 0xA884
                                reg_a0 = (reg_a0 + 0x1) & 0xFFFFFFFF            # 0xA88C (delayed: 0xA888)

                                if (reg_t2 == 0):
                                        reg_pc=0xABB0
                                        continue
                                # 0xA888

                                reg_t0 = memory.get_byte(reg_s4 - 0x1)          # 0xA890
                                reg_pc=0xA894; continue # to-next

                        elif reg_pc == 0xA894:
                                reg_s4 = (reg_s4 + 0x1) & 0xFFFFFFFF            # 0xA894
                                memory.set_byte(reg_a0 - 0x1, reg_t0)           # 0xA89C (delayed: 0xA898)

                                if (reg_at == reg_a0):
                                        reg_pc=0xA838
                                        continue
                                # 0xA898

                                reg_a0 = (reg_a0 + 0x1) & 0xFFFFFFFF            # 0xA8A0
                                reg_t0 = memory.get_byte(reg_s4 - 0x1)          # 0xA8A8 (delayed: 0xA8A4)
                                reg_pc=0xA894; continue                         # 0xA8A4
                                
                        elif reg_pc == 0xA8AC:
                                reg_t8 = memory.get_word(reg_a2 + 0x4)                                          # 0xA8AC
                                reg_v0 = WordPlay.logical_shift_left(reg_v0, reg_t9 & 0x1F)                     # 0xA8B0
                                reg_a2 = (reg_a2 + 0x4) & 0xFFFFFFFF                                            # 0xA8B4
                                reg_t9 = (reg_t9 - 0x20) & 0xFFFFFFFF                                           # 0xA8B8
                                reg_v0 = ((reg_v0 & 0xFFFF0000) | ((reg_t8 & 0xFFFF) << 0)) & 0xFFFFFFFF        # 0xA8BC
                                reg_v0 = WordPlay.rotate_right(reg_v0, reg_t9 & 0x1F)                           # 0xA8C0
                                reg_v0 = WordPlay.logical_shift_right(reg_v0, reg_t2 & 0x1F)                    # 0xA8C4
                                reg_s4 = (reg_s4 - reg_v0) & 0xFFFFFFFF                                         # 0xA8CC (delayed: 0xA8C8)
                                reg_pc=reg_ra; continue                                                         # 0xA8C8
                                
                        elif reg_pc == 0xA8D0:
                                delay_a0 = reg_a0
                                reg_a0 = (reg_a0 + 0x1) & 0xFFFFFFFF            # 0xA8D4 (hazard-jump-delay-slot: 0xA8D0)

                                if (delay_a0 == reg_a1):
                                        reg_pc=0xABB8
                                        continue
                                # 0xA8D0

                                memory.set_byte(reg_a0 - 0x1, reg_v0)           # 0xA8DC (delayed: 0xA8D8)
                                reg_pc=0xA838; continue                         # 0xA8D8
                                
                        elif reg_pc == 0xA8E0:
                                reg_t9 = (reg_t9 - reg_t2) & 0xFFFFFFFF                         # 0xA8E4 (jump-delay-slot: 0xA8E0)

                                if (WordPlay.as_signed(reg_v0) < 0):
                                        reg_pc=0xABB0
                                        continue
                                # 0xA8E0

                                reg_v0 = WordPlay.rotate_right(reg_t8, reg_t9 & 0x1F)           # 0xA8EC (delayed: 0xA8E8)

                                if (WordPlay.as_signed(reg_t9) > 0):
                                        reg_pc=0xA8AC
                                        continue
                                # 0xA8E8

                                reg_v0 = WordPlay.logical_shift_right(reg_v0, reg_t2 & 0x1F)    # 0xA8F0
                                reg_s4 = (reg_s4 - reg_v0) & 0xFFFFFFFF                         # 0xA8F8 (delayed: 0xA8F4)
                                reg_pc=reg_ra; continue                                         # 0xA8F4

                        elif reg_pc == 0xA8FC:
                                reg_t2 = WordPlay.arithmetic_shift_right(reg_t2, 28)            # 0xA8FC
                                reg_t9 = (reg_t9 - reg_t2) & 0xFFFFFFFF                         # 0xA904 (delayed: 0xA900)

                                if (reg_s4 == reg_t2):
                                        reg_pc=0xA91C
                                        continue
                                # 0xA900

                                reg_v0 = WordPlay.rotate_right(reg_t8, reg_t9 & 0x1F)           # 0xA90C (delayed: 0xA908)

                                if (WordPlay.as_signed(reg_t9) > 0):
                                        reg_pc=0xA8AC
                                        continue
                                # 0xA908

                                reg_v0 = WordPlay.logical_shift_right(reg_v0, reg_t2 & 0x1F)    # 0xA910
                                reg_s4 = (reg_s4 - reg_v0) & 0xFFFFFFFF                         # 0xA918 (delayed: 0xA914)
                                reg_pc=reg_ra; continue                                         # 0xA914

                        elif reg_pc == 0xA91C:
                                reg_v0 = (reg_v0 + 0x1) & 0xFFFFFFFF                                    # 0xA91C
                                reg_t0 = WordPlay.sign_extend_hword(memory.get_hword(reg_sp + 0x314))   # 0xA924 (delayed: 0xA920)

                                if (reg_v0 == 0):
                                        reg_pc=0xABB0
                                        continue
                                # 0xA920

                                reg_t9 = (reg_t9 + reg_t2) & 0xFFFFFFFF                                 # 0xA92C (delayed: 0xA928)

                                if (reg_t0 == 0):
                                        reg_pc=0xA660
                                        continue
                                # 0xA928
                                
                                reg_pc=0xA930; continue # to-next

                        elif reg_pc == 0xA930:
                                reg_v0 = (reg_a0 - reg_t6) & 0xFFFFFFFF                 # 0xA934 (jump-delay-slot: 0xA930)

                                if (reg_a3 == 0):
                                        reg_pc=0xA948
                                        continue
                                # 0xA930

                                reg_t9 = (reg_t9 + 0x27) & 0xFFFFFFFF                   # 0xA938
                                reg_t1 = WordPlay.logical_shift_right(reg_t9, 3)        # 0xA93C
                                reg_a2 = (reg_a2 + reg_t1) & 0xFFFFFFFF                 # 0xA940
                                memory.set_word(reg_a3, reg_v0)                         # 0xA944
                                reg_pc=0xA948; continue # to-next

                        elif reg_pc == 0xA948: # decompression main, _exit
                                reg_ra = memory.get_word(reg_sp + 0x310)        # 0xA948
                                reg_s4 = memory.get_word(reg_sp + 0x308)        # 0xA94C
                                reg_sp = (reg_sp + 0x380) & 0xFFFFFFFF          # 0xA954 (delayed: 0xA950)
                                reg_pc=reg_ra; continue                         # 0xA950
                                
                        elif reg_pc == 0xA958:
                                reg_a2 = (reg_a2 + 0x4) & 0xFFFFFFFF                                            # 0xA958
                                reg_t8 = memory.get_word(reg_a2)                                                # 0xA95C
                                reg_v0 = WordPlay.logical_shift_left(reg_v0, reg_t9 & 0x1F)                     # 0xA960
                                reg_t9 = (reg_t9 - 0x20) & 0xFFFFFFFF                                           # 0xA964
                                reg_v0 = ((reg_v0 & 0xFFFF0000) | ((reg_t8 & 0xFFFF) << 0)) & 0xFFFFFFFF        # 0xA968
                                reg_v0 = WordPlay.rotate_right(reg_v0, reg_t9 & 0x1F)                           # 0xA96C
                                reg_v0 = ((reg_v0 & 0xFFFF0000) | ((0 & 0xFFFF) << 0)) & 0xFFFFFFFF             # 0xA974 (delayed: 0xA970)
                                reg_pc=0xA988; continue                                                         # 0xA970

                        elif reg_pc == 0xA978:
                                reg_v0 = WordPlay.logical_shift_right(reg_t8, reg_t9 & 0x1F)            # 0xA978
                                reg_t9 = (reg_t9 - reg_t2) & 0xFFFFFFFF                                 # 0xA97C
                                reg_v0 = WordPlay.logical_shift_left(reg_v0, reg_t2 & 0x1F)             # 0xA984 (delayed: 0xA980)

                                if (WordPlay.as_signed(reg_t9) > 0):
                                        reg_pc=0xA958
                                        continue
                                # 0xA980
                                
                                reg_pc=0xA988; continue # to-next

                        elif reg_pc == 0xA988:
                                reg_v0 = WordPlay.reverse_word(reg_v0)          # 0xA988
                                reg_t2 = 1 if (reg_v0 < reg_v1) else 0          # 0xA98C
                                reg_v0 = (reg_v0 + reg_v0) & 0xFFFFFFFF         # 0xA994 (delayed: 0xA990)

                                if (reg_t2 == 0):
                                        reg_pc=0xA9C8
                                        continue
                                # 0xA990

                                reg_v0 = (reg_v0 + reg_t0) & 0xFFFFFFFF                                 # 0xA998
                                reg_v0 = WordPlay.sign_extend_hword(memory.get_hword(reg_v0 + 0x3A))    # 0xA9A0 (delayed: 0xA99C)
                                reg_pc=reg_ra; continue                                                 # 0xA99C

                        elif reg_pc == 0xA9A4:
                                reg_t2 = WordPlay.sign_extend_hword(memory.get_hword(reg_t0))           # 0xA9A4
                                reg_v0 = (reg_v0 + reg_t0) & 0xFFFFFFFF                                 # 0xA9A8
                                reg_v0 = (reg_v0 + reg_t2) & 0xFFFFFFFF                                 # 0xA9B0 (delayed: 0xA9AC)

                                if (WordPlay.as_signed(reg_t2) > 0):
                                        reg_pc=0xA9BC
                                        continue
                                # 0xA9AC

                                reg_v0 = WordPlay.sign_extend_hword(memory.get_hword(reg_v0 + 0x3C))    # 0xA9B8 (delayed: 0xA9B4)
                                reg_pc=reg_ra; continue                                                 # 0xA9B4

                        elif reg_pc == 0xA9BC:
                                reg_v0 = (reg_v0 + 0xFFFF8000) & 0xFFFFFFFF                             # 0xA9BC
                                reg_v0 = WordPlay.sign_extend_hword(memory.get_hword(reg_v0 - 0x7FC4))  # 0xA9C4 (delayed: 0xA9C0)
                                reg_pc=reg_ra; continue                                                 # 0xA9C0

                        elif reg_pc == 0xA9C8:
                                reg_v1 = memory.get_hword(reg_t0 + 0x1E)                                # 0xA9CC (jump-delay-slot: 0xA9C8)

                                if (reg_t9 == 0):
                                        reg_pc=0xA9F0
                                        continue
                                # 0xA9C8

                                reg_t2 = WordPlay.logical_shift_right(reg_t8, reg_t9 & 0x1F)            # 0xA9D0
                                reg_v0 = ((reg_v0 & -0x2) | ((reg_t2 & 0x1) << 0)) & 0xFFFFFFFF         # 0xA9D4
                                reg_pc=0xA9D8; continue # to-next

                        elif reg_pc == 0xA9D8:
                                reg_v1 = 1 if (WordPlay.as_signed(reg_v0) < WordPlay.as_signed(reg_v1)) else 0  # 0xA9D8
                                reg_v0 = (reg_v0 + reg_v0) & 0xFFFFFFFF                                         # 0xA9DC
                                reg_t9 = (reg_t9 + 0x1) & 0xFFFFFFFF                                            # 0xA9E4 (delayed: 0xA9E0)

                                if (reg_v1 != 0):
                                        reg_pc=0xA9A4
                                        continue
                                # 0xA9E0

                                reg_t0 = (reg_t0 + 0x2) & 0xFFFFFFFF                                    # 0xA9EC (delayed: 0xA9E8)
                                reg_pc=0xA9C8; continue                                                 # 0xA9E8

                        elif reg_pc == 0xA9F0:
                                reg_a2 = (reg_a2 + 0x4) & 0xFFFFFFFF                                    # 0xA9F0
                                reg_t8 = memory.get_word(reg_a2)                                        # 0xA9F4
                                reg_t9 = -0x20                                                          # 0xA9F8
                                reg_v0 = ((reg_v0 & -0x2) | ((reg_t8 & 0x1) << 0)) & 0xFFFFFFFF         # 0xAA00 (delayed: 0xA9FC)
                                reg_pc=0xA9D8; continue                                                 # 0xA9FC
                                
                        elif reg_pc == 0xAA04:
                                reg_t5 = (reg_t5 + 0x1) & 0xFFFFFFFF            # 0xAA04
                                reg_pc=0xAA08; continue # to-next

                        elif reg_pc == 0xAA08:
                                memory.set_word(reg_s4 + 0x38, 0)               # 0xAA08
                                reg_t4 = 0                                      # 0xAA0C
                                reg_at = 0xFFFFFFFF                             # 0xAA10
                                memory.set_word(reg_s4 + 0x2C, 0)               # 0xAA14
                                reg_t3 = (reg_s4) & 0xFFFFFFFF                  # 0xAA18
                                reg_hi = reg_ra                                 # 0xAA1C
                                memory.set_word(reg_s4 + 0x34, 0)               # 0xAA20
                                reg_t1 = 0x7                                    # 0xAA24
                                reg_pc=0xAA28; continue # to-next

                        elif reg_pc == 0xAA28:
                                reg_t0 = 1 if (reg_t4 < reg_t5) else 0                                  # 0xAA28
                                reg_t2 = WordPlay.sign_extend_byte(memory.get_byte(reg_sp + 0x2F8))     # 0xAA30 (delayed: 0xAA2C)

                                if (reg_t0 == 0):
                                        reg_pc=0xAB14
                                        continue
                                # 0xAA2C

                                reg_v1 = memory.get_hword(reg_sp + 0x316)                               # 0xAA34
                                reg_t0 = (reg_sp + 0x2FA) & 0xFFFFFFFF                                  # 0xAA3C (delayed: 0xAA38)
                                reg_ra = 0xAA40; reg_pc=0xA978; continue                                # 0xAA38

                        elif reg_pc == 0xAA40:
                                reg_t0 = (reg_v0 - 0x10) & 0xFFFFFFFF                                                           # 0xAA40
                                reg_t2 = WordPlay.sanitize_word(min(WordPlay.as_signed(reg_t0), WordPlay.as_signed(reg_t1)))    # 0xAA48 (delayed: 0xAA44)

                                if (WordPlay.as_signed(reg_t0) <= 0):
                                        reg_pc=0xAA70
                                        continue
                                # 0xAA44

                                reg_t9 = (reg_t9 + reg_t2) & 0xFFFFFFFF                                                         # 0xAA4C
                                reg_v0 = WordPlay.rotate_right(reg_t8, reg_t9 & 0x1F)                                           # 0xAA54 (delayed: 0xAA50)

                                if (WordPlay.as_signed(reg_t9) > 0):
                                        reg_pc=0xAA90
                                        continue
                                # 0xAA50
                                
                                reg_pc=0xAA58; continue # to-next

                        elif reg_pc == 0xAA58:
                                reg_t2 = (-reg_t2) & 0xFFFFFFFF                                 # 0xAA58
                                reg_v0 = WordPlay.logical_shift_right(reg_v0, reg_t2 & 0x1F)    # 0xAA5C
                                reg_t0 = (reg_t0 + reg_v0) & 0xFFFFFFFF                         # 0xAA60
                                reg_pc=0xAA64; continue # to-next

                        elif reg_pc == 0xAA64:
                                reg_t4 = (reg_t4 + reg_t0) & 0xFFFFFFFF          # 0xAA64
                                reg_at = (reg_t4 + 0xFFFFFFFF) & 0xFFFFFFFF      # 0xAA6C (delayed: 0xAA68)
                                reg_pc=0xAA28; continue                          # 0xAA68
                                
                        elif reg_pc == 0xAA70:
                                reg_t4 = (reg_t4 + 0x1) & 0xFFFFFFFF             # 0xAA74 (jump-delay-slot: 0xAA70)

                                if (reg_t0 == 0):
                                        reg_pc=0xAAAC
                                        continue
                                # 0xAA70

                                reg_at = (reg_t4 + 0xFFFFFFFF) & 0xFFFFFFFF      # 0xAA7C (delayed: 0xAA78)

                                if (reg_v0 == 0):
                                        reg_pc=0xAA28
                                        continue
                                # 0xAA78

                                reg_at = ((reg_at & 0xFFFF81FF) | ((reg_v0 & 0x3F) << 9)) & 0xFFFFFFFF  # 0xAA80
                                memory.set_hword(reg_t3 + 0x3C, reg_at)                                 # 0xAA84
                                reg_t3 = (reg_t3 + 0x2) & 0xFFFFFFFF                                    # 0xAA8C (delayed: 0xAA88)
                                reg_pc=0xAA28; continue                                                 # 0xAA88
                                
                        elif reg_pc == 0xAA90:
                                reg_t8 = memory.get_word(reg_a2 + 0x4)                                          # 0xAA90
                                reg_v0 = WordPlay.logical_shift_left(reg_v0, reg_t9 & 0x1F)                     # 0xAA94
                                reg_a2 = (reg_a2 + 0x4) & 0xFFFFFFFF                                            # 0xAA98
                                reg_t9 = (reg_t9 - 0x20) & 0xFFFFFFFF                                           # 0xAA9C
                                reg_v0 = ((reg_v0 & 0xFFFF0000) | ((reg_t8 & 0xFFFF) << 0)) & 0xFFFFFFFF        # 0xAAA0
                                reg_v0 = WordPlay.rotate_right(reg_v0, reg_t9 & 0x1F)                           # 0xAAA8 (delayed: 0xAAA4)
                                reg_pc=0xAA58; continue                                                         # 0xAAA4

                        elif reg_pc == 0xAAAC:
                                reg_t9 = (reg_t9 + 0x2) & 0xFFFFFFFF                                            # 0xAAB0 (jump-delay-slot: 0xAAAC)

                                if (WordPlay.as_signed(reg_at) < 0):
                                        reg_pc=0xABC0
                                        continue
                                # 0xAAAC

                                reg_v0 = WordPlay.rotate_right(reg_t8, reg_t9 & 0x1F)                           # 0xAAB8 (delayed: 0xAAB4)

                                if (WordPlay.as_signed(reg_t9) > 0):
                                        reg_pc=0xAAEC
                                        continue
                                # 0xAAB4
                                
                                reg_pc=0xAABC; continue # to-next

                        elif reg_pc == 0xAABC:
                                reg_v0 = WordPlay.logical_shift_right(reg_v0, 30)       # 0xAABC
                                reg_t0 = reg_at & 0x7E00                                # 0xAAC0
                                
                                delay_t0 = reg_t0
                                reg_t0 = (reg_v0 + 0x3) & 0xFFFFFFFF                    # 0xAAC8 (hazard-delayed: 0xAAC4)

                                if (delay_t0 == 0):
                                        reg_pc=0xAA64
                                        continue
                                # 0xAAC4

                                reg_t0 = (reg_t0 + reg_at) & 0xFFFFFFFF                 # 0xAACC
                                
                                reg_pc=0xAAD0; continue # to-next

                        elif reg_pc == 0xAAD0:
                                reg_at = (reg_at + 0x1) & 0xFFFFFFFF            # 0xAAD0
                                memory.set_hword(reg_t3 + 0x3C, reg_at)         # 0xAAD4
                                reg_t3 = (reg_t3 + 0x2) & 0xFFFFFFFF            # 0xAADC (delayed: 0xAAD8)

                                if (reg_at != reg_t0):
                                        reg_pc=0xAAD0
                                        continue
                                # 0xAAD8

                                reg_t4 = reg_at & 511                           # 0xAAE0
                                reg_t4 = (reg_t4 + 0x1) & 0xFFFFFFFF            # 0xAAE8 (delayed: 0xAAE4)
                                reg_pc=0xAA28; continue                         # 0xAAE4

                        elif reg_pc == 0xAAEC:
                                reg_t8 = memory.get_word(reg_a2 + 0x4)                                          # 0xAAEC
                                reg_v0 = WordPlay.logical_shift_left(reg_v0, reg_t9 & 0x1F)                     # 0xAAF0
                                reg_a2 = (reg_a2 + 0x4) & 0xFFFFFFFF                                            # 0xAAF4
                                reg_t9 = (reg_t9 - 0x20) & 0xFFFFFFFF                                           # 0xAAF8
                                reg_v0 = ((reg_v0 & 0xFFFF0000) | ((reg_t8 & 0xFFFF) << 0)) & 0xFFFFFFFF        # 0xAAFC
                                reg_v0 = WordPlay.rotate_right(reg_v0, reg_t9 & 0x1F)                           # 0xAB04 (delayed: 0xAB00)
                                reg_pc=0xAABC; continue                                                         # 0xAB00

                        elif reg_pc == 0xAB08:
                                reg_at = 0xFFFFFFFF                             # 0xAB08
                                memory.set_hword(reg_t1 + 0x1C, reg_at)         # 0xAB10 (delayed: 0xAB0C)
                                reg_pc=reg_ra; continue                         # 0xAB0C

                        elif reg_pc == 0xAB14:
                                memory.set_word(reg_s4 + 0x30, 0)               # 0xAB14
                                reg_ra = reg_hi                                 # 0xAB1C (delayed: 0xAB18)

                                if (reg_t4 != reg_t5):
                                        reg_pc=0xABC0
                                        continue
                                # 0xAB18
                                
                                reg_pc=0xAB20; continue # to-next

                        elif reg_pc == 0xAB20: # Some kind of function?
                                memory.set_word(reg_s4 + 0x20, 0)               # 0xAB20
                                reg_t0 = 0                                      # 0xAB24
                                memory.set_word(reg_s4 + 0x24, 0)               # 0xAB28
                                reg_t1 = (reg_s4 + 0x2) & 0xFFFFFFFF            # 0xAB2C
                                reg_at = 0xFFFFFFFF                             # 0xAB30
                                memory.set_word(reg_s4 + 0x28, 0)               # 0xAB34
                                reg_pc=0xAB38; continue # to-next

                        elif reg_pc == 0xAB38:
                                reg_at = (reg_at + 0x1) & 0xFFFFFFFF            # 0xAB3C (jump-delay-slot: 0xAB38)

                                if (reg_t3 == reg_s4):
                                        reg_pc=0xAB08
                                        continue
                                # 0xAB38

                                reg_t4 = (reg_s4 + 0x2) & 0xFFFFFFFF                                            # 0xAB40
                                reg_v0 = WordPlay.sign_extend_hword(memory.get_hword(reg_s4 + 0x3C))            # 0xAB44
                                reg_pc=0xAB48; continue # to-next

                        elif reg_pc == 0xAB48:
                                reg_v1 = WordPlay.sign_extend_hword(memory.get_hword(reg_t4 + 0x3C))            # 0xAB48
                                
                                delay_t4 = reg_t4
                                reg_t4 = (reg_t4 + 0x2) & 0xFFFFFFFF                                            # 0xAB50 (hazard-delayed: 0xAB4C)

                                if (reg_t3 == delay_t4):
                                        reg_pc=0xAB64
                                        continue
                                # 0xAB4C

                                reg_t2 = WordPlay.sanitize_word(max(WordPlay.as_signed(reg_v1), WordPlay.as_signed(reg_v0)))    # 0xAB54
                                memory.set_hword(reg_t4 + 0x3A, reg_t2)                                                         # 0xAB58
                                reg_v0 = WordPlay.sanitize_word(min(WordPlay.as_signed(reg_v1), WordPlay.as_signed(reg_v0)))    # 0xAB60 (delayed: 0xAB5C)
                                reg_pc=0xAB48; continue                                                                         # 0xAB5C
                                
                        elif reg_pc == 0xAB64:
                                reg_t4 = WordPlay.logical_shift_right(reg_v0, 9)                # 0xAB64
                                reg_v0 &= 511                                                   # 0xAB68
                                memory.set_hword(reg_s4 + 0x3C, reg_v0)                         # 0xAB6C
                                reg_s4 = (reg_s4 + 0x2) & 0xFFFFFFFF                            # 0xAB74 (delayed: 0xAB70)

                                if (reg_t0 == reg_t4):
                                        reg_pc=0xAB38
                                        continue
                                # 0xAB70

                                reg_t2 = (reg_t0 - reg_t4) & 0xFFFFFFFF                         # 0xAB78
                                
                                delay_t0 = reg_t0
                                reg_t0 = (reg_t4) & 0xFFFFFFFF                                  # 0xAB80 (hazard-delayed: 0xAB7C)

                                if (delay_t0 == 0):
                                        reg_pc=0xABA0
                                        continue
                                # 0xAB7C

                                memory.set_hword(reg_t1 + 0x1C, reg_at)                         # 0xAB84
                                reg_at = WordPlay.rotate_right(reg_at, reg_t2 & 0x1F)           # 0xAB88
                                reg_t2 = (reg_t2 + reg_t2) & 0xFFFFFFFF                         # 0xAB8C
                                reg_t1 = (reg_t1 - reg_t2) & 0xFFFFFFFF                         # 0xAB90
                                reg_t2 = (reg_s4 - reg_at) & 0xFFFFFFFF                         # 0xAB94
                                reg_t2 = (reg_t2 - reg_at) & 0xFFFFFFFF                         # 0xAB98
                                reg_t2 = (reg_t2 - reg_t1) & 0xFFFFFFFF                         # 0xAB9C
                                reg_pc=0xABA0; continue # to-next

                        elif reg_pc == 0xABA0:
                                memory.set_hword(reg_t1 - 0x2, reg_t2)          # 0xABA4 (jump-delay-slot: 0xABA0)

                                if (WordPlay.as_signed(reg_t2) <= 0):
                                        reg_pc=0xAB38
                                        continue
                                # 0xABA0
                                
                                reg_pc=0xABA8; continue # to-next

                        elif reg_pc == 0xABA8:
                                reg_v0 = 0x108                  # 0xABAC (jump-delay-slot: 0xABA8)
                                reg_pc=0xABCC; continue         # 0xABA8
                                
                        elif reg_pc == 0xABB0:
                                reg_v0 = 0x108                  # 0xABB4 (jump-delay-slot: 0xABB0)
                                reg_pc=0xABCC; continue         # 0xABB0

                        elif reg_pc == 0xABB8:
                                reg_v0 = 0x104                  # 0xABBC (jump-delay-slot: 0xABB8)
                                reg_pc=0xABCC; continue         # 0xABB8
                                
                        elif reg_pc == 0xABC0:
                                reg_v0 = 0x108                  # 0xABC4 (jump-delay-slot: 0xABC0)
                                reg_pc=0xABCC; continue         # 0xABC0

                        elif reg_pc == 0xABC8:
                                reg_v0 = 0x108                  # 0xABC8
                                reg_pc=0xABCC; continue         # to-next

                        elif reg_pc == 0xABCC:
                                reg_v1 = 0x80000000             # 0xABCC
                                reg_v0 |= reg_v1                # 0xABD4 (delayed: 0xABD0)
                                reg_pc=0xA948; continue         # 0xABD0

                        elif reg_pc == 0xABD8:
                                reg_t0 = (-reg_t9) & 0xFFFFFFFF                                 # 0xABD8
                                reg_t0 = WordPlay.logical_shift_right(reg_t0, 3)                # 0xABDC
                                reg_a2 = (reg_a2 - reg_t0) & 0xFFFFFFFF                         # 0xABE0
                                raise Exception() #reg_t0 |lwl| memory[reg_a2 + 0x7].word       # 0xABE4
                                raise Exception() #reg_t0 |lwr| memory[reg_a2 + 0x4].word       # 0xABE8
                                reg_v1 = reg_t0 & 65535                                         # 0xABEC
                                reg_v1 = (reg_v1 + reg_a0) & 0xFFFFFFFF                         # 0xABF0
                                reg_t1 = 1 if (reg_a1 < reg_v1) else 0                          # 0xABF4
                                
                                delay_t1 = reg_t1
                                reg_t1 = WordPlay.not_word(reg_t0)                              # 0xABFC (hazard-delayed: 0xABF8)

                                if (delay_t1 != 0):
                                        reg_pc=0xABB8
                                        continue
                                # 0xABF8

                                reg_t1 = WordPlay.rotate_right(reg_t1, 16)                      # 0xAC00
                                reg_v0 = 0x108                                                  # 0xAC08 (delayed: 0xAC04)

                                if (reg_t1 != reg_t0):
                                        reg_pc=0xABCC
                                        continue
                                # 0xAC04
                                
                                reg_pc=0xAC0C; continue # to-next

                        elif reg_pc == 0xAC0C:
                                reg_t1 = memory.get_byte(reg_a2 + 0x8)          # 0xAC0C
                                reg_a2 = (reg_a2 + 0x1) & 0xFFFFFFFF            # 0xAC10
                                reg_a0 = (reg_a0 + 0x1) & 0xFFFFFFFF            # 0xAC14
                                memory.set_byte(reg_a0 - 0x1, reg_t1)           # 0xAC1C (delayed: 0xAC18)

                                if (reg_v1 != reg_a0):
                                        reg_pc=0xAC0C
                                        continue
                                # 0xAC18

                                reg_t9 = 0x20                                   # 0xAC24 (delayed: 0xAC20)

                                if (reg_t2 != 0):
                                        reg_pc=0xA930
                                        continue
                                # 0xAC20

                                reg_a2 = (reg_a2 + 0x8) & 0xFFFFFFFF            # 0xAC2C (delayed: 0xAC28)
                                reg_pc=0xA64C; continue                         # 0xAC28

                        elif reg_pc == 0x62F68:
                                break

                        else:
                                raise Exception('Unimplemented PC: 0x%X' % reg_pc)

                output_path = file_path + '.DECOMPRESSED'
                print '# Writing: %s' % output_path
                
                with open(output_path, 'wb') as w:

                    filled_addresses = sorted(memory.content.keys())
                    for address in filled_addresses:
                        value = memory.content[address]
                        if address < output_buffer:
                            continue
                        elif address >= output_buffer + output_size:
                            break
                        
                        w.write(struct.pack('I', value))

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print 'zipped.py <action> <file>'
        print ''
        print 'zipped.py --decompress <file>            # Output is file.DECOMPRESSED'
        print 'zipped.py --compress <file.DECOMPRESSED> # Input is file.DECOMPRESSED'
        sys.exit(0)

    action = sys.argv[1]
    input_path = sys.argv[2]
    output_path = ''

    if len(input_path) == 0:
        print 'Error: Empty input path provided'
        sys.exit(-1)


    if action in ('-d', '--decompress'):
        try:
            print '# Decompressing %s:' % input_path
            zip_wrapper = ZipWrapper()
            zip_wrapper.open(input_path)

            output_path = input_path

            zip_wrapper.decompress(output_path)

        except Exception, e:
            print 'Error: %s' % e
            sys.exit(-1)

    elif action in ('-c', '--compress'):
        try:
            print '# Compressing %s:' % input_path
            zip_wrapper = ZipWrapper()
            
            # Figure out the output path
            output_path = input_path

            suffix = '.DECOMPRESSED'
            if not output_path.endswith(suffix):
                raise Exception('Input path must have a suffix of %s' % suffix)
            output_path = output_path[:-len(suffix)]

            #zip_wrapper.compress(output_path)

            # Save
            #zip_wrapper.save(output_path)

        except Exception, e:
            print 'Error: %s' % e
            sys.exit(-1)

    else:
        print 'Error: Unknown action: %s' % action
        sys.exit(-1)

    sys.exit(0)

