#!/usr/bin/env python2.7

import os
import re
import struct

class DataType(object):
    Unknown = 0
    Integer = 1
    Unsigned = 2
    Float = 3
    String = 4
    Pointer = 5
    Code = 6
    RelocatableCode = 7

class DataEndianess(object):
    Unknown = 0
    BigEndian = 1
    LittleEndian = 2

class Data(object):
    def __init__(self, type, byte_size, value=None, comment=None, label=None, group=None, endianess=DataEndianess.LittleEndian):
        self.type = type
        self.size = byte_size

        if isinstance(value, basestring):
            value = value.replace('\\n', '\n').replace('\\0', '\0')

        self.value = value

        self.comment = comment
        self.label = label
        self.group = group

        # Filled in after section creation
        self.section = None
        self.address = None

    def get_word_aligned_trimmed_value(self):
        # Strings need to be null terminated.
        # A four letter string is 5 bytes due to the null terminator
        # On a MIPS machine, where accesses are done in groups of four bytes,
        # a 5 byte string actually takes 8 bytes

        if self.type == DataType.String and isinstance(self.value, basestring):
            # Convert UTF8 to Shift-JIS
            try:
                string_content = self.value.decode('utf-8').encode('shift_jis')
            except (UnicodeDecodeError, UnicodeEncodeError): 
                raise Exception('There seems to be an character that cannot be converted to Shift_JIS. Check the text:' + self.value)

            length_without_terminator = min(len(string_content), self.size - 1)

            # Find first occurence of '\0' in the last group of '\0's
            while length_without_terminator >= 1:
                if string_content[length_without_terminator - 1] != '\0':
                    break

                length_without_terminator -= 1

            # Trim value to fit in given size (or better)
            trimmed_value = string_content[0:length_without_terminator] + '\0\0\0\0'

            length_with_terminator = 4 * int((length_without_terminator + 4) / 4)
            
            return trimmed_value[0:length_with_terminator]

        else:
            # For all other types, the size shouldn't change
            return self.value

class AppSectionFlag(object):
    Writable=1
    Allocated=2
    Executable=4

class AppSection(object):
    def __init__(self, name, start_address, size, flags, content=None):
        self.name = name
        self.start_address = start_address
        self.size = size
        self.end_address = start_address + size
        self.flags = flags

        if content is None:
            content = {}

        self.content = content

        self.labels = {}
        self.pointers = {}

        # Fill in missing content attributes
        # Keep in mind this loop is out of order due to how dictionaries work
        for data_address, data_content in content.iteritems():
            data_content.section = self
            data_content.address = data_address

            # Collect all the labels under the section
            if data_content.label:
                self.labels[data_content.label] = data_content.address

            # Collect all the pointers under the section
            if data_content.type == DataType.Pointer:
                if data_content.value not in self.pointers:
                    self.pointers[data_content.value] = data_content.address
                elif isinstance(self.pointers[data_content.value], list):
                    self.pointers[data_content.value].append(data_content.address)
                else:
                    promote_to_list = self.pointers[data_content.value]
                    self.pointers[data_content.value] = [promote_to_list, data_content.address]

    def inject_values_from_elf(self, elf_file_path):
        f = open(elf_file_path, 'rb')
        
        # HACK: Hacky approximation that works in this case; In the future, actually parse the ELF in the App class
        f.seek(self.start_address + 0x80)

        address = self.start_address
        while (address < self.end_address):
            data_line = self.content[address]

            if data_line.size == 0:
                raise Exception('Data line at 0x%s is of size 0!' % format(address, '08X'))

            # The values that are None are those that were excluded
            # for copyright reasons, so inject those since the others
            # are already loaded. Furthermore, certain values
            # require relocation adjustments. 
            # The ones that do require said adjustments (pointers, address loads in code sections, etc.)
            # are already present in the .py file! So don't overwrite them with this inject!
            if data_line.value == None:
                value = f.read(data_line.size)

                if (data_line.type == DataType.String) or (data_line.size > 4) or (data_line.size == 3):
                    # Represent value as a tuple
                    value = tuple([ord(i) for i in value])

                elif data_line.size == 4:
                    # Represent value as uint32
                    value = struct.unpack('I', value)[0]

                elif data_line.size == 2:
                    # Represent value as uint16
                    value = struct.unpack('H', value)[0]

                elif data_line.size == 1:
                    # Represent value as uint8
                    value = struct.unpack('B', value)[0]

                else:
                    raise Exception('Unsure how to represent value at data line 0x%s!' % format(address, '08X'))

                data_line.value = value

            else:
                f.seek(data_line.size, os.SEEK_CUR)

            address += data_line.size

        f.close()

    def as_identifier(self):
        # Drop all initial periods or 0-9
        # Convert remaining periods to _
        # Remove all remaining non alphnumeric
        return re.sub(r'[^0-9A-Za-z_]', '', re.sub(r'\.', '_', re.sub(r'^[0-9.]*', '', self.name)))

    def __str__(self):
        return self.name

