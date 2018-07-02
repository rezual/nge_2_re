#!/usr/bin/env python2.7

# A quick rush-job of a script to calculate percents to be pasted into the README

import binascii
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'game_app'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'patches'))

import support

from eboot_data import section_data
from eboot_rodata import section_rodata

from btimtext import translate_map as file_btimtext
from f2info import translate_map as file_f2info
from f2tuto import translate_map as file_f2tuto
from imtext_1 import translate_map as file_imtext_1
from imtext_2 import translate_map as file_imtext_2
from imtext_3 import translate_map as file_imtext_3
from imtext_4 import translate_map as file_imtext_4
from imtext_5 import translate_map as file_imtext_5
from evs_1 import translate_map as files_evs_1
from evs_2 import translate_map as files_evs_2
from evs_3 import translate_map as files_evs_3

sections = (section_data, section_rodata)
files = (file_btimtext, file_f2info, file_f2tuto, file_imtext_1, file_imtext_2, file_imtext_3, file_imtext_4, file_imtext_5, files_evs_1, files_evs_2, files_evs_3)
results = []

for section in sections:
	total = 0
	translated = 0
	for _, data in section.content.iteritems():
		if data.type != support.DataType.String:
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

print """- Text in Game Executable located at `umd0:/PSP_GAME/SYSDIR/EBOOT.BIN`:
	- [x] %0.2f%% translated Writable sections - See patches/eboot_data.py
	- [ ] %0.2f%% translated Read-Only sections - See patches/eboot_rodata.py
- Conversation text: `umd0:/PSP_GAME/USRDIR/game/imtext.bin`:
	- [ ] %0.2f%% translated (in total)
		- [ ] %0.2f%% translated - See patches/imtext_1.py
		- [ ] %0.2f%% translated - See patches/imtext_2.py
		- [ ] %0.2f%% translated - See patches/imtext_3.py
		- [ ] %0.2f%% translated - See patches/imtext_4.py
		- [ ] %0.2f%% translated - See patches/imtext_5.py
- Scripted event text (`.evs` files) located in various `.har` files: `umd0:/PSP_GAME/USRDIR/`:
	- [ ] %0.2f%% translated (in total)
		- [ ] %0.2f%% translated - See patches/evs_1.py
		- [ ] %0.2f%% translated - See patches/evs_2.py
		- [ ] %0.2f%% translated - See patches/evs_3.py
- Battle mode text: `umd0:/PSP_GAME/USRDIR/btl/btimtext.bin`:
	- [ ] %0.2f%% translated - See patches/btimtext.py
- Secret Information menu text: `umd0:/PSP_GAME/USRDIR/free/f2info.bin`:
	- [ ] %0.2f%% translated - See patches/f2info.py
- Tutorial menu text: `umd0:/PSP_GAME/USRDIR/free/f2tuto.bin`:
	- [ ] %0.2f%% translated - See patches/f2tuto.py""" % (
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
