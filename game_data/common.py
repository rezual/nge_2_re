#!/usr/bin/env python2.7

import struct
import os

# Common helper functions
def read_uint8(file_handle):
    return ord(file_handle.read(1))

def read_uint16(file_handle):
    return struct.unpack('H', file_handle.read(2))[0]

def read_uint32(file_handle):
    return struct.unpack('I', file_handle.read(4))[0]

def write_uint8(file_handle, value):
    return file_handle.write(chr(value))

def write_uint16(file_handle, value):
    return file_handle.write(struct.pack('H', value))

def write_uint32(file_handle, value):
    return file_handle.write(struct.pack('I', value))

def calculate_word_aligned_length(unaligned_length):
    return 4 * int((unaligned_length + 3) / 4)

def get_file_size(file_handle):
    return os.fstat(file_handle.fileno()).st_size
    
def align_size(unaligned_size, alignment):
    return alignment * int((unaligned_size + alignment - 1) / alignment)

def unique_color(index, total):
    if index == -1:
        return (0, 0, 0)

    if total == 0:
        return (255, 255, 255)

    fractional = index/float(total)
    sectofractional = 6 * fractional
    sectointeger = int(sectofractional)
    sectoremainder = sectofractional - sectointeger
    subsectofractional = min(int(sectoremainder * 256), 255)
    subremaindersectofractional = min(int((1 - sectoremainder) * 256), 255)

    if sectointeger == 0:
        return (255, subsectofractional, 0)

    if sectointeger == 1:
        return (subremaindersectofractional, 255, 0)

    if sectointeger == 2:
        return (0, 255, subsectofractional)

    if sectointeger == 3:
        return (0, subremaindersectofractional, 255)

    if sectointeger == 4:
        return (subsectofractional, 0, 255)

    return (255, 0, subremaindersectofractional)

   