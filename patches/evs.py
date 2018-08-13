#!/usr/bin/env python2.7

# The purpose of this file is to combine all evs_#.py files as one,
# in order to be used as a patch

from evs_1 import translate_map as evs_1_translate_map
from evs_2 import translate_map as evs_2_translate_map
from evs_3 import translate_map as evs_3_translate_map

translate_map = {}
translate_map.update(evs_1_translate_map)
translate_map.update(evs_2_translate_map)
translate_map.update(evs_3_translate_map)
