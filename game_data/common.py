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

