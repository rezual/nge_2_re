#!/usr/bin/env python2.7

# A quick rush-job of a script to calculate percents to be pasted into the README

import binascii
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'game_app'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'game_data'))

import support

os.environ['LINK_TRANSLATE'] = 'true'
os.environ['LINK_DUMMY_TEXT'] = 'true'
from app import *

from file_btimtext_translate import translate_map as file_btimtext
from file_f2info_translate import translate_map as file_f2info
from file_f2tuto_translate import translate_map as file_f2tuto
from file_imtext_translate_part_1 import translate_map as file_imtext_1
from file_imtext_translate_part_2 import translate_map as file_imtext_2
from file_imtext_translate_part_3 import translate_map as file_imtext_3
from file_imtext_translate_part_4 import translate_map as file_imtext_4
from file_imtext_translate_part_5 import translate_map as file_imtext_5
from files_evs_part_1 import translate_map as files_evs_1
from files_evs_part_2 import translate_map as files_evs_2
from files_evs_part_3 import translate_map as files_evs_3

sections = (section_data, section_rodata)
files = (file_btimtext, file_f2info, file_f2tuto, file_imtext_1, file_imtext_2, file_imtext_3, file_imtext_4, file_imtext_5, files_evs_1, files_evs_2, files_evs_3)
results = []

for section in sections:
	total = 0
	translated = 0
	for _, data in section.content.iteritems():
		if data.type != DataType.String:
			continue

		total += 1

		# Skip yet to be translated
		if data.value == '???':
			continue

		translated += 1

	if total != 0:
		results.append((translated / float(total) * 100))
	else:
		results.append(0)		

for file in files:
	total = 0
	translated = 0
	for key, value in file.iteritems():
		total += 1

		# Skip yet to be translated
		if value == '???':
			continue

		translated += 1

	if total != 0:
		btimtext_percent = format((translated / float(total) * 100), '0.2f') + '%'
		results.append((translated / float(total) * 100))
	else:
		results.append(0)		

# Calculate avg percentages
avg_imtext = (results[5] + results[6] + results[7] + results[8] + results[9]) / 5
avg_evs = (results[10] + results[11] + results[12]) / 3

print """- Text in Writable Section of Game Executable:
        - [ ] %0.2f%% translated
                - See game_app/section_data_translate.py
- Text in Read-Only Section of Game Executable:
        - [ ] %0.2f%% translated
                - See game_app/section_rodata_translate.py
- umd0:/PSP_GAME/USRDIR/game/imtext.bin:
        - [ ] %0.2f%% translated
                - [ ] %0.2f%% translated
                        - See game_data/file_imtext_translate_part_1.py
                - [ ] %0.2f%% translated
                        - See game_data/file_imtext_translate_part_2.py
                - [ ] %0.2f%% translated
                        - See game_data/file_imtext_translate_part_3.py
                - [ ] %0.2f%% translated
                        - See game_data/file_imtext_translate_part_4.py
                - [ ] %0.2f%% translated
                        - See game_data/file_imtext_translate_part_5.py
- umd0:/PSP_GAME/USRDIR/*.evs:
	- [ ] %0.2f%% translated
		- [ ] %0.2f%% translated
			- See game_data/files_evs_part_1.py
		- [ ] %0.2f%% translated
			- See game_data/files_evs_part_2.py
		- [ ] %0.2f%% translated
			- See game_data/files_evs_part_3.py
- umd0:/PSP_GAME/USRDIR/btl/btimtext.bin:
        - [ ] %0.2f%% translated
                - See game_data/file_btimtext_translate.py
- umd0:/PSP_GAME/USRDIR/free/f2info.bin:
        - [ ] %0.2f%% translated
                - See game_data/file_f2info_translate.py
- umd0:/PSP_GAME/USRDIR/free/f2tuto.bin:
        - [ ] %0.2f%% translated
                - See game_data/file_f2tuto_translate.py""" % (
results[0],
results[1],

avg_imtext,
results[5],
results[6],
results[7],
results[8],
results[9],

avg_evs,
results[10],
results[11],
results[12],

results[2],
results[3],
results[4]
)
