#!/usr/bin/env python2.7

import struct
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'game_app'))
from psp import CPU

class Zipped(object):
	def __init__(self):
		self.cpu = CPU(0x00003068, None)

		# Decompression routine entry point
		self.cpu.memory.content[0x00003068] = 0x27BDFFE0
		self.cpu.memory.content[0x0000306C] = 0x00803021
		self.cpu.memory.content[0x00003070] = 0x03A03821
		self.cpu.memory.content[0x00003074] = 0x00A02021
		self.cpu.memory.content[0x00003078] = 0x3C050100
		self.cpu.memory.content[0x0000307C] = 0xAFBF0010
		self.cpu.memory.content[0x00003080] = 0x0C00298C
		self.cpu.memory.content[0x00003084] = 0xAFA00000
		self.cpu.memory.content[0x00003088] = 0x28440000
		self.cpu.memory.content[0x0000308C] = 0x8FA20000
		self.cpu.memory.content[0x00003090] = 0x8FBF0010
		self.cpu.memory.content[0x00003094] = 0x0004100B
		self.cpu.memory.content[0x00003098] = 0x03E00008
		self.cpu.memory.content[0x0000309C] = 0x27BD0020

		# Decompression routine main body
		self.cpu.memory.content[0x0000A630] = 0x27BDFC80
		self.cpu.memory.content[0x0000A634] = 0xAFB40308
		self.cpu.memory.content[0x0000A638] = 0x00852821
		self.cpu.memory.content[0x0000A63C] = 0x00807021
		self.cpu.memory.content[0x0000A640] = 0x3C0F001B
		self.cpu.memory.content[0x0000A644] = 0x25EF1380
		self.cpu.memory.content[0x0000A648] = 0xAFBF0310
		self.cpu.memory.content[0x0000A64C] = 0x30D90003
		self.cpu.memory.content[0x0000A650] = 0x00D93023
		self.cpu.memory.content[0x0000A654] = 0x8CD80000
		self.cpu.memory.content[0x0000A658] = 0x0019C8C0
		self.cpu.memory.content[0x0000A65C] = 0x2739FFE0
		self.cpu.memory.content[0x0000A660] = 0x27390003
		self.cpu.memory.content[0x0000A664] = 0x1F20002A
		self.cpu.memory.content[0x0000A668] = 0x03381046
		self.cpu.memory.content[0x0000A66C] = 0x7C430F80
		self.cpu.memory.content[0x0000A670] = 0x10600159
		self.cpu.memory.content[0x0000A674] = 0x7C4A0740
		self.cpu.memory.content[0x0000A678] = 0x2468FFFE
		self.cpu.memory.content[0x0000A67C] = 0x11000039
		self.cpu.memory.content[0x0000A680] = 0xA7AA0314
		self.cpu.memory.content[0x0000A684] = 0x1D000150
		self.cpu.memory.content[0x0000A688] = 0x27AA0000
		self.cpu.memory.content[0x0000A68C] = 0x25F4006C
		self.cpu.memory.content[0x0000A690] = 0x8DEB0000
		self.cpu.memory.content[0x0000A694] = 0x254A0004
		self.cpu.memory.content[0x0000A698] = 0x25EF0004
		self.cpu.memory.content[0x0000A69C] = 0x168FFFFC
		self.cpu.memory.content[0x0000A6A0] = 0xAD4BFFFC
		self.cpu.memory.content[0x0000A6A4] = 0x24090000
		self.cpu.memory.content[0x0000A6A8] = 0x24140090
		self.cpu.memory.content[0x0000A6AC] = 0xA5490000
		self.cpu.memory.content[0x0000A6B0] = 0x25290001
		self.cpu.memory.content[0x0000A6B4] = 0x1534FFFD
		self.cpu.memory.content[0x0000A6B8] = 0x254A0002
		self.cpu.memory.content[0x0000A6BC] = 0x25F40010
		self.cpu.memory.content[0x0000A6C0] = 0x8DEB0000
		self.cpu.memory.content[0x0000A6C4] = 0x254A0004
		self.cpu.memory.content[0x0000A6C8] = 0x25EF0004
		self.cpu.memory.content[0x0000A6CC] = 0x168FFFFC
		self.cpu.memory.content[0x0000A6D0] = 0xAD4BFFFC
		self.cpu.memory.content[0x0000A6D4] = 0x2414011E
		self.cpu.memory.content[0x0000A6D8] = 0xA5490000
		self.cpu.memory.content[0x0000A6DC] = 0x25290001
		self.cpu.memory.content[0x0000A6E0] = 0x1534FFFD
		self.cpu.memory.content[0x0000A6E4] = 0x254A0002
		self.cpu.memory.content[0x0000A6E8] = 0x25F40040
		self.cpu.memory.content[0x0000A6EC] = 0x8DEB0000
		self.cpu.memory.content[0x0000A6F0] = 0x254A0004
		self.cpu.memory.content[0x0000A6F4] = 0x25EF0004
		self.cpu.memory.content[0x0000A6F8] = 0x168FFFFC
		self.cpu.memory.content[0x0000A6FC] = 0xAD4BFFFC
		self.cpu.memory.content[0x0000A700] = 0x25EFFF44
		self.cpu.memory.content[0x0000A704] = 0xA7AB029A
		self.cpu.memory.content[0x0000A708] = 0x08002A0E
		self.cpu.memory.content[0x0000A70C] = 0xA7AB027C
		self.cpu.memory.content[0x0000A710] = 0x8CD80004
		self.cpu.memory.content[0x0000A714] = 0x03221004
		self.cpu.memory.content[0x0000A718] = 0x24C60004
		self.cpu.memory.content[0x0000A71C] = 0x2739FFE0
		self.cpu.memory.content[0x0000A720] = 0x7F027804
		self.cpu.memory.content[0x0000A724] = 0x0800299B
		self.cpu.memory.content[0x0000A728] = 0x03221046
		self.cpu.memory.content[0x0000A72C] = 0x8CD80004
		self.cpu.memory.content[0x0000A730] = 0x03221004
		self.cpu.memory.content[0x0000A734] = 0x24C60004
		self.cpu.memory.content[0x0000A738] = 0x2739FFE0
		self.cpu.memory.content[0x0000A73C] = 0x7F027804
		self.cpu.memory.content[0x0000A740] = 0x080029DC
		self.cpu.memory.content[0x0000A744] = 0x03221046
		self.cpu.memory.content[0x0000A748] = 0x8CD80004
		self.cpu.memory.content[0x0000A74C] = 0x03221004
		self.cpu.memory.content[0x0000A750] = 0x24C60004
		self.cpu.memory.content[0x0000A754] = 0x2739FFE0
		self.cpu.memory.content[0x0000A758] = 0x7F027804
		self.cpu.memory.content[0x0000A75C] = 0x080029E7
		self.cpu.memory.content[0x0000A760] = 0x03221046
		self.cpu.memory.content[0x0000A764] = 0x2739000E
		self.cpu.memory.content[0x0000A768] = 0x1F20FFF0
		self.cpu.memory.content[0x0000A76C] = 0x03381046
		self.cpu.memory.content[0x0000A770] = 0xAFA2035C
		self.cpu.memory.content[0x0000A774] = 0x7C541F00
		self.cpu.memory.content[0x0000A778] = 0x26940004
		self.cpu.memory.content[0x0000A77C] = 0x27AB02F8
		self.cpu.memory.content[0x0000A780] = 0x01E04021
		self.cpu.memory.content[0x0000A784] = 0x028FA021
		self.cpu.memory.content[0x0000A788] = 0x1114000B
		self.cpu.memory.content[0x0000A78C] = 0x25080001
		self.cpu.memory.content[0x0000A790] = 0x27390003
		self.cpu.memory.content[0x0000A794] = 0x1F20FFEC
		self.cpu.memory.content[0x0000A798] = 0x03381046
		self.cpu.memory.content[0x0000A79C] = 0x00021742
		self.cpu.memory.content[0x0000A7A0] = 0x1040FFF9
		self.cpu.memory.content[0x0000A7A4] = 0x810A0005
		self.cpu.memory.content[0x0000A7A8] = 0x256B0002
		self.cpu.memory.content[0x0000A7AC] = 0x7C4A7244
		self.cpu.memory.content[0x0000A7B0] = 0x080029E2
		self.cpu.memory.content[0x0000A7B4] = 0xA56A003A
		self.cpu.memory.content[0x0000A7B8] = 0x0C002AC8
		self.cpu.memory.content[0x0000A7BC] = 0x27B402F8
		self.cpu.memory.content[0x0000A7C0] = 0x8FAD035C
		self.cpu.memory.content[0x0000A7C4] = 0x110000F8
		self.cpu.memory.content[0x0000A7C8] = 0x27B40000
		self.cpu.memory.content[0x0000A7CC] = 0x7DAD2480
		self.cpu.memory.content[0x0000A7D0] = 0x0C002A82
		self.cpu.memory.content[0x0000A7D4] = 0x25AD0101
		self.cpu.memory.content[0x0000A7D8] = 0x110000F3
		self.cpu.memory.content[0x0000A7DC] = 0x27A80000
		self.cpu.memory.content[0x0000A7E0] = 0x8509003C
		self.cpu.memory.content[0x0000A7E4] = 0x25080002
		self.cpu.memory.content[0x0000A7E8] = 0x312A00FF
		self.cpu.memory.content[0x0000A7EC] = 0x11490003
		self.cpu.memory.content[0x0000A7F0] = 0x014A5021
		self.cpu.memory.content[0x0000A7F4] = 0x014F5021
		self.cpu.memory.content[0x0000A7F8] = 0x8549003C
		self.cpu.memory.content[0x0000A7FC] = 0x150BFFF8
		self.cpu.memory.content[0x0000A800] = 0xA509003A
		self.cpu.memory.content[0x0000A804] = 0x8FAD035C
		self.cpu.memory.content[0x0000A808] = 0x27B4027C
		self.cpu.memory.content[0x0000A80C] = 0x0C002A81
		self.cpu.memory.content[0x0000A810] = 0x7DAD25C0
		self.cpu.memory.content[0x0000A814] = 0x27A8FFC0
		self.cpu.memory.content[0x0000A818] = 0x850902F8
		self.cpu.memory.content[0x0000A81C] = 0x3129001F
		self.cpu.memory.content[0x0000A820] = 0x01294821
		self.cpu.memory.content[0x0000A824] = 0x012F4821
		self.cpu.memory.content[0x0000A828] = 0x8529007C
		self.cpu.memory.content[0x0000A82C] = 0x25080002
		self.cpu.memory.content[0x0000A830] = 0x151DFFF9
		self.cpu.memory.content[0x0000A834] = 0xA50902F6
		self.cpu.memory.content[0x0000A838] = 0x83AA0000
		self.cpu.memory.content[0x0000A83C] = 0x97A3001E
		self.cpu.memory.content[0x0000A840] = 0x0C002A5E
		self.cpu.memory.content[0x0000A844] = 0x27A80002
		self.cpu.memory.content[0x0000A848] = 0x27A8027E
		self.cpu.memory.content[0x0000A84C] = 0x7C025520
		self.cpu.memory.content[0x0000A850] = 0x0441001F
		self.cpu.memory.content[0x0000A854] = 0x0002A103
		self.cpu.memory.content[0x0000A858] = 0x05500028
		self.cpu.memory.content[0x0000A85C] = 0x97A3029A
		self.cpu.memory.content[0x0000A860] = 0x83AA027C
		self.cpu.memory.content[0x0000A864] = 0x0C002A5E
		self.cpu.memory.content[0x0000A868] = 0x00940823
		self.cpu.memory.content[0x0000A86C] = 0x00A1A02B
		self.cpu.memory.content[0x0000A870] = 0x168000D1
		self.cpu.memory.content[0x0000A874] = 0x00405016
		self.cpu.memory.content[0x0000A878] = 0x254AFFE2
		self.cpu.memory.content[0x0000A87C] = 0x05500018
		self.cpu.memory.content[0x0000A880] = 0x0082A023
		self.cpu.memory.content[0x0000A884] = 0x01D4502B
		self.cpu.memory.content[0x0000A888] = 0x114000C9
		self.cpu.memory.content[0x0000A88C] = 0x24840001
		self.cpu.memory.content[0x0000A890] = 0x9288FFFF
		self.cpu.memory.content[0x0000A894] = 0x26940001
		self.cpu.memory.content[0x0000A898] = 0x1024FFE7
		self.cpu.memory.content[0x0000A89C] = 0xA088FFFF
		self.cpu.memory.content[0x0000A8A0] = 0x24840001
		self.cpu.memory.content[0x0000A8A4] = 0x08002A25
		self.cpu.memory.content[0x0000A8A8] = 0x9288FFFF
		self.cpu.memory.content[0x0000A8AC] = 0x8CD80004
		self.cpu.memory.content[0x0000A8B0] = 0x03221004
		self.cpu.memory.content[0x0000A8B4] = 0x24C60004
		self.cpu.memory.content[0x0000A8B8] = 0x2739FFE0
		self.cpu.memory.content[0x0000A8BC] = 0x7F027804
		self.cpu.memory.content[0x0000A8C0] = 0x03221046
		self.cpu.memory.content[0x0000A8C4] = 0x01421006
		self.cpu.memory.content[0x0000A8C8] = 0x03E00008
		self.cpu.memory.content[0x0000A8CC] = 0x0282A023
		self.cpu.memory.content[0x0000A8D0] = 0x108500B9
		self.cpu.memory.content[0x0000A8D4] = 0x24840001
		self.cpu.memory.content[0x0000A8D8] = 0x08002A0E
		self.cpu.memory.content[0x0000A8DC] = 0xA082FFFF
		self.cpu.memory.content[0x0000A8E0] = 0x044000B3
		self.cpu.memory.content[0x0000A8E4] = 0x032AC823
		self.cpu.memory.content[0x0000A8E8] = 0x1F20FFF0
		self.cpu.memory.content[0x0000A8EC] = 0x03381046
		self.cpu.memory.content[0x0000A8F0] = 0x01421006
		self.cpu.memory.content[0x0000A8F4] = 0x03E00008
		self.cpu.memory.content[0x0000A8F8] = 0x0282A023
		self.cpu.memory.content[0x0000A8FC] = 0x000A5703
		self.cpu.memory.content[0x0000A900] = 0x128A0006
		self.cpu.memory.content[0x0000A904] = 0x032AC823
		self.cpu.memory.content[0x0000A908] = 0x1F20FFE8
		self.cpu.memory.content[0x0000A90C] = 0x03381046
		self.cpu.memory.content[0x0000A910] = 0x01421006
		self.cpu.memory.content[0x0000A914] = 0x03E00008
		self.cpu.memory.content[0x0000A918] = 0x0282A023
		self.cpu.memory.content[0x0000A91C] = 0x24420001
		self.cpu.memory.content[0x0000A920] = 0x104000A3
		self.cpu.memory.content[0x0000A924] = 0x87A80314
		self.cpu.memory.content[0x0000A928] = 0x1100FF4D
		self.cpu.memory.content[0x0000A92C] = 0x032AC821
		self.cpu.memory.content[0x0000A930] = 0x10E00005
		self.cpu.memory.content[0x0000A934] = 0x008E1023
		self.cpu.memory.content[0x0000A938] = 0x27390027
		self.cpu.memory.content[0x0000A93C] = 0x001948C2
		self.cpu.memory.content[0x0000A940] = 0x00C93021
		self.cpu.memory.content[0x0000A944] = 0xACE20000
		self.cpu.memory.content[0x0000A948] = 0x8FBF0310
		self.cpu.memory.content[0x0000A94C] = 0x8FB40308
		self.cpu.memory.content[0x0000A950] = 0x03E00008
		self.cpu.memory.content[0x0000A954] = 0x27BD0380
		self.cpu.memory.content[0x0000A958] = 0x24C60004
		self.cpu.memory.content[0x0000A95C] = 0x8CD80000
		self.cpu.memory.content[0x0000A960] = 0x03221004
		self.cpu.memory.content[0x0000A964] = 0x2739FFE0
		self.cpu.memory.content[0x0000A968] = 0x7F027804
		self.cpu.memory.content[0x0000A96C] = 0x03221046
		self.cpu.memory.content[0x0000A970] = 0x08002A62
		self.cpu.memory.content[0x0000A974] = 0x7C027804
		self.cpu.memory.content[0x0000A978] = 0x03381006
		self.cpu.memory.content[0x0000A97C] = 0x032AC823
		self.cpu.memory.content[0x0000A980] = 0x1F20FFF5
		self.cpu.memory.content[0x0000A984] = 0x01421004
		self.cpu.memory.content[0x0000A988] = 0x7C021520
		self.cpu.memory.content[0x0000A98C] = 0x0043502B
		self.cpu.memory.content[0x0000A990] = 0x1140000D
		self.cpu.memory.content[0x0000A994] = 0x00421021
		self.cpu.memory.content[0x0000A998] = 0x00481021
		self.cpu.memory.content[0x0000A99C] = 0x03E00008
		self.cpu.memory.content[0x0000A9A0] = 0x8442003A
		self.cpu.memory.content[0x0000A9A4] = 0x850A0000
		self.cpu.memory.content[0x0000A9A8] = 0x00481021
		self.cpu.memory.content[0x0000A9AC] = 0x1D400003
		self.cpu.memory.content[0x0000A9B0] = 0x004A1021
		self.cpu.memory.content[0x0000A9B4] = 0x03E00008
		self.cpu.memory.content[0x0000A9B8] = 0x8442003C
		self.cpu.memory.content[0x0000A9BC] = 0x24428000
		self.cpu.memory.content[0x0000A9C0] = 0x03E00008
		self.cpu.memory.content[0x0000A9C4] = 0x8442803C
		self.cpu.memory.content[0x0000A9C8] = 0x13200009
		self.cpu.memory.content[0x0000A9CC] = 0x9503001E
		self.cpu.memory.content[0x0000A9D0] = 0x03385006
		self.cpu.memory.content[0x0000A9D4] = 0x7D420004
		self.cpu.memory.content[0x0000A9D8] = 0x0043182A
		self.cpu.memory.content[0x0000A9DC] = 0x00421021
		self.cpu.memory.content[0x0000A9E0] = 0x1460FFF0
		self.cpu.memory.content[0x0000A9E4] = 0x27390001
		self.cpu.memory.content[0x0000A9E8] = 0x08002A72
		self.cpu.memory.content[0x0000A9EC] = 0x25080002
		self.cpu.memory.content[0x0000A9F0] = 0x24C60004
		self.cpu.memory.content[0x0000A9F4] = 0x8CD80000
		self.cpu.memory.content[0x0000A9F8] = 0x2419FFE0
		self.cpu.memory.content[0x0000A9FC] = 0x08002A76
		self.cpu.memory.content[0x0000AA00] = 0x7F020004
		self.cpu.memory.content[0x0000AA04] = 0x25AD0001
		self.cpu.memory.content[0x0000AA08] = 0xAE800038
		self.cpu.memory.content[0x0000AA0C] = 0x00006021
		self.cpu.memory.content[0x0000AA10] = 0x2401FFFF
		self.cpu.memory.content[0x0000AA14] = 0xAE80002C
		self.cpu.memory.content[0x0000AA18] = 0x02805821
		self.cpu.memory.content[0x0000AA1C] = 0x03E00011
		self.cpu.memory.content[0x0000AA20] = 0xAE800034
		self.cpu.memory.content[0x0000AA24] = 0x24090007
		self.cpu.memory.content[0x0000AA28] = 0x018D402B
		self.cpu.memory.content[0x0000AA2C] = 0x11000039
		self.cpu.memory.content[0x0000AA30] = 0x83AA02F8
		self.cpu.memory.content[0x0000AA34] = 0x97A30316
		self.cpu.memory.content[0x0000AA38] = 0x0C002A5E
		self.cpu.memory.content[0x0000AA3C] = 0x27A802FA
		self.cpu.memory.content[0x0000AA40] = 0x2448FFF0
		self.cpu.memory.content[0x0000AA44] = 0x1900000A
		self.cpu.memory.content[0x0000AA48] = 0x0109502D
		self.cpu.memory.content[0x0000AA4C] = 0x032AC821
		self.cpu.memory.content[0x0000AA50] = 0x1F20000F
		self.cpu.memory.content[0x0000AA54] = 0x03381046
		self.cpu.memory.content[0x0000AA58] = 0x000A5022
		self.cpu.memory.content[0x0000AA5C] = 0x01421006
		self.cpu.memory.content[0x0000AA60] = 0x01024021
		self.cpu.memory.content[0x0000AA64] = 0x01886021
		self.cpu.memory.content[0x0000AA68] = 0x08002A8A
		self.cpu.memory.content[0x0000AA6C] = 0x2581FFFF
		self.cpu.memory.content[0x0000AA70] = 0x1100000E
		self.cpu.memory.content[0x0000AA74] = 0x258C0001
		self.cpu.memory.content[0x0000AA78] = 0x1040FFEB
		self.cpu.memory.content[0x0000AA7C] = 0x2581FFFF
		self.cpu.memory.content[0x0000AA80] = 0x7C417244
		self.cpu.memory.content[0x0000AA84] = 0xA561003C
		self.cpu.memory.content[0x0000AA88] = 0x08002A8A
		self.cpu.memory.content[0x0000AA8C] = 0x256B0002
		self.cpu.memory.content[0x0000AA90] = 0x8CD80004
		self.cpu.memory.content[0x0000AA94] = 0x03221004
		self.cpu.memory.content[0x0000AA98] = 0x24C60004
		self.cpu.memory.content[0x0000AA9C] = 0x2739FFE0
		self.cpu.memory.content[0x0000AAA0] = 0x7F027804
		self.cpu.memory.content[0x0000AAA4] = 0x08002A96
		self.cpu.memory.content[0x0000AAA8] = 0x03221046
		self.cpu.memory.content[0x0000AAAC] = 0x04200044
		self.cpu.memory.content[0x0000AAB0] = 0x27390002
		self.cpu.memory.content[0x0000AAB4] = 0x1F20000D
		self.cpu.memory.content[0x0000AAB8] = 0x03381046
		self.cpu.memory.content[0x0000AABC] = 0x00021782
		self.cpu.memory.content[0x0000AAC0] = 0x30287E00
		self.cpu.memory.content[0x0000AAC4] = 0x1100FFE7
		self.cpu.memory.content[0x0000AAC8] = 0x24480003
		self.cpu.memory.content[0x0000AACC] = 0x01014021
		self.cpu.memory.content[0x0000AAD0] = 0x24210001
		self.cpu.memory.content[0x0000AAD4] = 0xA561003C
		self.cpu.memory.content[0x0000AAD8] = 0x1428FFFD
		self.cpu.memory.content[0x0000AADC] = 0x256B0002
		self.cpu.memory.content[0x0000AAE0] = 0x302C01FF
		self.cpu.memory.content[0x0000AAE4] = 0x08002A8A
		self.cpu.memory.content[0x0000AAE8] = 0x258C0001
		self.cpu.memory.content[0x0000AAEC] = 0x8CD80004
		self.cpu.memory.content[0x0000AAF0] = 0x03221004
		self.cpu.memory.content[0x0000AAF4] = 0x24C60004
		self.cpu.memory.content[0x0000AAF8] = 0x2739FFE0
		self.cpu.memory.content[0x0000AAFC] = 0x7F027804
		self.cpu.memory.content[0x0000AB00] = 0x08002AAF
		self.cpu.memory.content[0x0000AB04] = 0x03221046
		self.cpu.memory.content[0x0000AB08] = 0x2401FFFF
		self.cpu.memory.content[0x0000AB0C] = 0x03E00008
		self.cpu.memory.content[0x0000AB10] = 0xA521001C
		self.cpu.memory.content[0x0000AB14] = 0xAE800030
		self.cpu.memory.content[0x0000AB18] = 0x158D0029
		self.cpu.memory.content[0x0000AB1C] = 0x0000F810
		self.cpu.memory.content[0x0000AB20] = 0xAE800020
		self.cpu.memory.content[0x0000AB24] = 0x00004021
		self.cpu.memory.content[0x0000AB28] = 0xAE800024
		self.cpu.memory.content[0x0000AB2C] = 0x26890002
		self.cpu.memory.content[0x0000AB30] = 0x2401FFFF
		self.cpu.memory.content[0x0000AB34] = 0xAE800028
		self.cpu.memory.content[0x0000AB38] = 0x1174FFF3
		self.cpu.memory.content[0x0000AB3C] = 0x24210001
		self.cpu.memory.content[0x0000AB40] = 0x268C0002
		self.cpu.memory.content[0x0000AB44] = 0x8682003C
		self.cpu.memory.content[0x0000AB48] = 0x8583003C
		self.cpu.memory.content[0x0000AB4C] = 0x116C0005
		self.cpu.memory.content[0x0000AB50] = 0x258C0002
		self.cpu.memory.content[0x0000AB54] = 0x0062502C
		self.cpu.memory.content[0x0000AB58] = 0xA58A003A
		self.cpu.memory.content[0x0000AB5C] = 0x08002AD2
		self.cpu.memory.content[0x0000AB60] = 0x0062102D
		self.cpu.memory.content[0x0000AB64] = 0x00026242
		self.cpu.memory.content[0x0000AB68] = 0x304201FF
		self.cpu.memory.content[0x0000AB6C] = 0xA682003C
		self.cpu.memory.content[0x0000AB70] = 0x110CFFF1
		self.cpu.memory.content[0x0000AB74] = 0x26940002
		self.cpu.memory.content[0x0000AB78] = 0x010C5023
		self.cpu.memory.content[0x0000AB7C] = 0x11000008
		self.cpu.memory.content[0x0000AB80] = 0x01804021
		self.cpu.memory.content[0x0000AB84] = 0xA521001C
		self.cpu.memory.content[0x0000AB88] = 0x01410846
		self.cpu.memory.content[0x0000AB8C] = 0x014A5021
		self.cpu.memory.content[0x0000AB90] = 0x012A4823
		self.cpu.memory.content[0x0000AB94] = 0x02815023
		self.cpu.memory.content[0x0000AB98] = 0x01415023
		self.cpu.memory.content[0x0000AB9C] = 0x01495023
		self.cpu.memory.content[0x0000ABA0] = 0x1940FFE5
		self.cpu.memory.content[0x0000ABA4] = 0xA52AFFFE
		self.cpu.memory.content[0x0000ABA8] = 0x08002AF3
		self.cpu.memory.content[0x0000ABAC] = 0x24020108
		self.cpu.memory.content[0x0000ABB0] = 0x08002AF3
		self.cpu.memory.content[0x0000ABB4] = 0x24020108
		self.cpu.memory.content[0x0000ABB8] = 0x08002AF3
		self.cpu.memory.content[0x0000ABBC] = 0x24020104
		self.cpu.memory.content[0x0000ABC0] = 0x08002AF3
		self.cpu.memory.content[0x0000ABC4] = 0x24020108
		self.cpu.memory.content[0x0000ABC8] = 0x24020108
		self.cpu.memory.content[0x0000ABCC] = 0x3C038000
		self.cpu.memory.content[0x0000ABD0] = 0x08002A52
		self.cpu.memory.content[0x0000ABD4] = 0x00431025
		self.cpu.memory.content[0x0000ABD8] = 0x00194022
		self.cpu.memory.content[0x0000ABDC] = 0x000840C2
		self.cpu.memory.content[0x0000ABE0] = 0x00C83023
		self.cpu.memory.content[0x0000ABE4] = 0x88C80007
		self.cpu.memory.content[0x0000ABE8] = 0x98C80004
		self.cpu.memory.content[0x0000ABEC] = 0x3103FFFF
		self.cpu.memory.content[0x0000ABF0] = 0x00641821
		self.cpu.memory.content[0x0000ABF4] = 0x00A3482B
		self.cpu.memory.content[0x0000ABF8] = 0x1520FFEF
		self.cpu.memory.content[0x0000ABFC] = 0x01004827
		self.cpu.memory.content[0x0000AC00] = 0x00294C02
		self.cpu.memory.content[0x0000AC04] = 0x1528FFF1
		self.cpu.memory.content[0x0000AC08] = 0x24020108
		self.cpu.memory.content[0x0000AC0C] = 0x90C90008
		self.cpu.memory.content[0x0000AC10] = 0x24C60001
		self.cpu.memory.content[0x0000AC14] = 0x24840001
		self.cpu.memory.content[0x0000AC18] = 0x1464FFFC
		self.cpu.memory.content[0x0000AC1C] = 0xA089FFFF
		self.cpu.memory.content[0x0000AC20] = 0x1540FF43
		self.cpu.memory.content[0x0000AC24] = 0x24190020
		self.cpu.memory.content[0x0000AC28] = 0x08002993
		self.cpu.memory.content[0x0000AC2C] = 0x24C60008

		# Decompression routine look-up-tables
		self.cpu.memory.content[0x001B1380] = 0xFFCEFFF9
		self.cpu.memory.content[0x001B1384] = 0x1310FE3C
		self.cpu.memory.content[0x001B1388] = 0x0708001B
		self.cpu.memory.content[0x001B138C] = 0x050A0609
		self.cpu.memory.content[0x001B1390] = 0x030C040B
		self.cpu.memory.content[0x001B1394] = 0x010E020D
		self.cpu.memory.content[0x001B1398] = 0x0000000F
		self.cpu.memory.content[0x001B139C] = 0x00180000
		self.cpu.memory.content[0x001B13A0] = 0x020000C8
		self.cpu.memory.content[0x001B13A4] = 0x00000000
		self.cpu.memory.content[0x001B13A8] = 0x00000000
		self.cpu.memory.content[0x001B13AC] = 0x00000000
		self.cpu.memory.content[0x001B13B0] = 0x00000000
		self.cpu.memory.content[0x001B13B4] = 0x00000000
		self.cpu.memory.content[0x001B13B8] = 0x00000000
		self.cpu.memory.content[0x001B13BC] = 0xFFD0FFE7
		self.cpu.memory.content[0x001B13C0] = 0xFFB0FFC0
		self.cpu.memory.content[0x001B13C4] = 0xFF90FFA0
		self.cpu.memory.content[0x001B13C8] = 0xFF70FF80
		self.cpu.memory.content[0x001B13CC] = 0xFF5FFF60
		self.cpu.memory.content[0x001B13D0] = 0xFF1FFF3F
		self.cpu.memory.content[0x001B13D4] = 0xFED7FEFF
		self.cpu.memory.content[0x001B13D8] = 0xFE57FE97
		self.cpu.memory.content[0x001B13DC] = 0xFDDBFE17
		self.cpu.memory.content[0x001B13E0] = 0xFCDBFD5B
		self.cpu.memory.content[0x001B13E4] = 0xFBD3FC5B
		self.cpu.memory.content[0x001B13E8] = 0xF9D3FAD3
		self.cpu.memory.content[0x001B13EC] = 0xF7DDF8D3
		self.cpu.memory.content[0x001B13F0] = 0xF3DDF5DD
		self.cpu.memory.content[0x001B13F4] = 0xEFE0F1DD
		self.cpu.memory.content[0x001B13F8] = 0xFFFFFFFF
		self.cpu.memory.content[0x001B13FC] = 0x00010000
		self.cpu.memory.content[0x001B1400] = 0x00030002
		self.cpu.memory.content[0x001B1404] = 0x00060004
		self.cpu.memory.content[0x001B1408] = 0x000C0008
		self.cpu.memory.content[0x001B140C] = 0x00180010
		self.cpu.memory.content[0x001B1410] = 0x00300020
		self.cpu.memory.content[0x001B1414] = 0x00600040
		self.cpu.memory.content[0x001B1418] = 0x00C00080
		self.cpu.memory.content[0x001B141C] = 0x01800100
		self.cpu.memory.content[0x001B1420] = 0x03000200
		self.cpu.memory.content[0x001B1424] = 0x06000400
		self.cpu.memory.content[0x001B1428] = 0x0C000800
		self.cpu.memory.content[0x001B142C] = 0x18001000
		self.cpu.memory.content[0x001B1430] = 0x30002000
		self.cpu.memory.content[0x001B1434] = 0x60004000
		self.cpu.memory.content[0x001B1438] = 0xFFFBFFFB
		self.cpu.memory.content[0x001B143C] = 0x00000000

	def decompress(self, file_path):
		INPUT_BUFFER = 0x09E6A2E8
		OUTPUT_BUFFER = 0x08F475C0

		# Initial register setup
		self.cpu.regs.gp.ra.set(0x00062F68)
		self.cpu.regs.gp.sp.set(0x09FF7390)
		self.cpu.regs.gp.fp.set(0x00000001)

		# Reset PC
		# TODO: Make this a simple function of the cpu class
		# so that others don't need to know about jump clearing etc.
		self.cpu.regs.pc.set(0x00003068)
		self.cpu._jump_clear()

		# Load the file
		file_size = self.cpu.memory.load_file(file_path, INPUT_BUFFER)
		file_size = 4 * int((file_size + 3) / 4)
		OUTPUT_SIZE = self.cpu.memory.content[INPUT_BUFFER]

		self.cpu.regs.gp.a0.set(INPUT_BUFFER + 4) # Input buffer + 4 bytes to skip output size
		self.cpu.regs.gp.a1.set(OUTPUT_BUFFER) # Output buffer
		self.cpu.regs.gp.a2.set(OUTPUT_SIZE) # Decompressed size

		self.cpu.regs.gp.v0.set(0)

		while self.cpu.regs.pc.get() != 0x00062F68:
		    self.cpu.execute()

		print 'Writing: %s' % (file_path + '_DECOMPRESSED')
		with open(file_path + '_DECOMPRESSED', 'wb') as of:

		    filled_addresses = sorted(self.cpu.memory.content.keys())
		    for address in filled_addresses:
		        value = self.cpu.memory.content[address]
		        if address < OUTPUT_BUFFER:
		            continue
		        elif address >= OUTPUT_BUFFER + OUTPUT_SIZE:
		            break
		        
		        of.write(struct.pack('I', value))

if __name__ == '__main__':

	if len(sys.argv) < 2:
	    print './zipped.py <path to compressed file>'
	    sys.exit(0)

	INPUT_PATH = sys.argv[1]
	print 'Opening', INPUT_PATH
	zipped = Zipped()
	zipped.decompress(INPUT_PATH)


