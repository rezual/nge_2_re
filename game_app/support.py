#!/usr/bin/env python2.7

import re

class DataType(object):
	Unknown = 0
	Integer = 1
	Unsigned = 2
	Float = 3
	String = 4
	Pointer = 5
	Code = 6

class DataEndianess(object):
	Unknown = 0
	BigEndian = 1
	LittleEndian = 2

class Data(object):
	def __init__(self, type, byte_size, value=None, comment=None, group=None, endianess=DataEndianess.LittleEndian):
		self.type = type
		self.size = byte_size
		self.value = value
		self.comment = comment
		self.group = group

		# Filled in after section creation
		self.section = None
		self.address = None

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

		# Fill in missing content attributes
		for data_address, data_content in content.iteritems():
			data_content.section = self
			data_content.address = data_address

        def as_identifier(self):
                # Drop all initial periods or 0-9
                # Convert remaining periods to _
                # Remove all remaining non alphnumeric
                return re.sub(r'[^0-9A-Za-z_]', '', re.sub(r'\.', '_', re.sub(r'^[0-9.]*', '', self.name)))

        def __str__(self):
                return self.name

