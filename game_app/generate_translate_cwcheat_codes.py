#!/usr/bin/env python2.7

import binascii
import os

import support

os.environ['LINK_TRANSLATE'] = 'true'
from app import *

# Generate address, value pairs
cwcheat_code_list = []

for section in (section_data, section_rodata):
	for _, data in section.content.iteritems():
		if data.type != DataType.String:
			continue

		# Skip yet to be translated
		if data.value == '???':
			continue

		if not isinstance(data.value, basestring):
			continue

		# Generate the Cwcheat code
		value = data.get_word_aligned_trimmed_value()
	
		fourths_counter = 0
		address = data.address
		while fourths_counter < len(value):
			word_value = value[fourths_counter:fourths_counter + 4]
		
			cwcheat_formatted_address = '0x2' + format(address + 0x4000, '07x').upper()
			cwcheat_formatted_value	= '0x' + binascii.hexlify(word_value[::-1]).upper()

			cwcheat_code_list.append((cwcheat_formatted_address, cwcheat_formatted_value))

			fourths_counter += 4
			address += 4

# Cwcheat has a limit of how many lines per cheat, so bucket them
print '_S ' + App.serial_number
print '_G ' + App.title

cheat_group = 1
cheat_number = 0
for (address, value) in cwcheat_code_list:

	if cheat_number == 0:
		print '_C1 Translate %s' % cheat_group

	print '_L ' + address + ' ' + value

	cheat_number += 1
	if cheat_number >= 30:
		cheat_number = 0
		cheat_group += 1
