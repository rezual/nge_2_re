#!/usr/bin/env python2.7

# The purpose of this file is to combine all btimtext, f2info, f2tuto, and imtext_#.py files as one,
# in order to be used as a patch

from btimtext import translate_map as btimtext_translate_map

from f2info import translate_map as f2info_translate_map
from f2tuto import translate_map as f2tuto_translate_map

from imtext_1 import translate_map as imtext_1_translate_map
from imtext_2 import translate_map as imtext_2_translate_map
from imtext_3 import translate_map as imtext_3_translate_map
from imtext_4 import translate_map as imtext_4_translate_map
from imtext_5 import translate_map as imtext_5_translate_map

translate_map = {}
translate_map.update(btimtext_translate_map)
translate_map.update(f2info_translate_map)
translate_map.update(f2tuto_translate_map)
translate_map.update(imtext_1_translate_map)
translate_map.update(imtext_2_translate_map)
translate_map.update(imtext_3_translate_map)
translate_map.update(imtext_4_translate_map)
translate_map.update(imtext_5_translate_map)
