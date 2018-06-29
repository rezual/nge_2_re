#!/usr/bin/env python2.7

import os
import struct

class UnknownOpcodeException(Exception):
	pass

class WordPlay(object):
	REVERSE_BYTE_BITS = (0x00, 0x80, 0x40, 0xC0, 0x20, 0xA0, 0x60, 0xE0, 0x10, 0x90, 0x50, 0xD0, 0x30, 0xB0, 0x70, 0xF0, 
						 0x08, 0x88, 0x48, 0xC8, 0x28, 0xA8, 0x68, 0xE8, 0x18, 0x98, 0x58, 0xD8, 0x38, 0xB8, 0x78, 0xF8, 
						 0x04, 0x84, 0x44, 0xC4, 0x24, 0xA4, 0x64, 0xE4, 0x14, 0x94, 0x54, 0xD4, 0x34, 0xB4, 0x74, 0xF4, 
						 0x0C, 0x8C, 0x4C, 0xCC, 0x2C, 0xAC, 0x6C, 0xEC, 0x1C, 0x9C, 0x5C, 0xDC, 0x3C, 0xBC, 0x7C, 0xFC, 
						 0x02, 0x82, 0x42, 0xC2, 0x22, 0xA2, 0x62, 0xE2, 0x12, 0x92, 0x52, 0xD2, 0x32, 0xB2, 0x72, 0xF2, 
						 0x0A, 0x8A, 0x4A, 0xCA, 0x2A, 0xAA, 0x6A, 0xEA, 0x1A, 0x9A, 0x5A, 0xDA, 0x3A, 0xBA, 0x7A, 0xFA, 
						 0x06, 0x86, 0x46, 0xC6, 0x26, 0xA6, 0x66, 0xE6, 0x16, 0x96, 0x56, 0xD6, 0x36, 0xB6, 0x76, 0xF6, 
						 0x0E, 0x8E, 0x4E, 0xCE, 0x2E, 0xAE, 0x6E, 0xEE, 0x1E, 0x9E, 0x5E, 0xDE, 0x3E, 0xBE, 0x7E, 0xFE, 
						 0x01, 0x81, 0x41, 0xC1, 0x21, 0xA1, 0x61, 0xE1, 0x11, 0x91, 0x51, 0xD1, 0x31, 0xB1, 0x71, 0xF1, 
						 0x09, 0x89, 0x49, 0xC9, 0x29, 0xA9, 0x69, 0xE9, 0x19, 0x99, 0x59, 0xD9, 0x39, 0xB9, 0x79, 0xF9, 
						 0x05, 0x85, 0x45, 0xC5, 0x25, 0xA5, 0x65, 0xE5, 0x15, 0x95, 0x55, 0xD5, 0x35, 0xB5, 0x75, 0xF5, 
						 0x0D, 0x8D, 0x4D, 0xCD, 0x2D, 0xAD, 0x6D, 0xED, 0x1D, 0x9D, 0x5D, 0xDD, 0x3D, 0xBD, 0x7D, 0xFD, 
						 0x03, 0x83, 0x43, 0xC3, 0x23, 0xA3, 0x63, 0xE3, 0x13, 0x93, 0x53, 0xD3, 0x33, 0xB3, 0x73, 0xF3, 
						 0x0B, 0x8B, 0x4B, 0xCB, 0x2B, 0xAB, 0x6B, 0xEB, 0x1B, 0x9B, 0x5B, 0xDB, 0x3B, 0xBB, 0x7B, 0xFB, 
						 0x07, 0x87, 0x47, 0xC7, 0x27, 0xA7, 0x67, 0xE7, 0x17, 0x97, 0x57, 0xD7, 0x37, 0xB7, 0x77, 0xF7, 
						 0x0F, 0x8F, 0x4F, 0xCF, 0x2F, 0xAF, 0x6F, 0xEF, 0x1F, 0x9F, 0x5F, 0xDF, 0x3F, 0xBF, 0x7F, 0xFF)

	REPLACE_BYTE_INDEX = (0xFFFFFF00, 0xFFFF00FF, 0xFF00FFFF, 0x00FFFFFF)
	REPLACE_HWORD_INDEX = (0xFFFF0000, 0x0000FFFF)

	@staticmethod
	def sanitize_byte(byte_value):
		return byte_value & 0xFF

	@staticmethod
	def sanitize_hword(hword_value):
		return hword_value & 0xFFFF

	@staticmethod
	def sanitize_word(word_value):
		return word_value & 0xFFFFFFFF

	@staticmethod
	def sign_extend_byte(byte_value):
		if byte_value & 0x80:
			return (byte_value & 0x7F) | 0xFFFFFF80
		return byte_value

	@staticmethod
	def zero_extend_byte(byte_value):
		return byte_value

	@staticmethod
	def sign_extend_hword(hword_value):
		if hword_value & 0x8000:
			return (hword_value & 0x7FFF) | 0xFFFF8000
		return hword_value

	@staticmethod
	def zero_extend_hword(hword_value):
		return hword_value

	@staticmethod
	def not_byte(byte_value):
		# Python's ~ takes into account sign
		return 0xFF - byte_value

	@staticmethod
	def not_hword(hword_value):
		# Python's ~ takes into account sign
		return 0xFFFF - hword_value

	@staticmethod
	def not_word(word_value):
		# Python's ~ takes into account sign
		return 0xFFFFFFFF - word_value

	@staticmethod
	def as_bytes(word_value):
		return ((word_value >> 24) & 0xFF, (word_value >> 16) & 0xFF, (word_value >> 8) & 0xFF, word_value & 0xFF)

	@staticmethod
	def from_bytes(a, b, c, d):
		return (a << 24) | (b << 16) | (c << 8) | d

	@staticmethod
	def as_hwords(word_value):
		return ((word_value >> 16) & 0xFFFF, word_value & 0xFFFF)

	@staticmethod
	def from_hwords(a, b):
		return (a << 16) | b

	@staticmethod
	def get_byte(word_value, byte_index):
		bit_shift = 8 * byte_index
		return (word_value >> bit_shift) & 0xFF

	@staticmethod
	def get_hword(word_value, hword_index):
		bit_shift = 16 * hword_index
		return (word_value >> bit_shift)  & 0xFFFF

	@staticmethod
	def replace_byte(word_value, byte_index, byte_value):
		bit_shift = 8 * byte_index
		return (word_value & WordPlay.REPLACE_BYTE_INDEX[byte_index]) | (byte_value << bit_shift)

	@staticmethod
	def replace_hword(word_value, hword_index, hword_value):
		bit_shift = 16 * hword_index
		return (word_value & WordPlay.REPLACE_HWORD_INDEX[hword_index]) | (hword_value << bit_shift)

	@staticmethod
	def reverse_word(word_value):
		a, b, c, d = WordPlay.as_bytes(word_value)
		return WordPlay.from_bytes(WordPlay.REVERSE_BYTE_BITS[d], WordPlay.REVERSE_BYTE_BITS[c], WordPlay.REVERSE_BYTE_BITS[b], WordPlay.REVERSE_BYTE_BITS[a])

	@staticmethod
	def arithmetic_shift_left(word_value, shift_amount):
		return WordPlay.sanitize_word(word_value << shift_amount)

	@staticmethod
	def logical_shift_left(word_value, shift_amount):
		return WordPlay.sanitize_word(word_value << shift_amount)

	@staticmethod
	def arithmetic_shift_right(word_value, shift_amount):
		return WordPlay.sanitize_word(WordPlay.as_signed(word_value) >> shift_amount)

	@staticmethod
	def logical_shift_right(word_value, shift_amount):
		return word_value >> shift_amount

	@staticmethod
	def rotate_left(word_value, rotate_amount):
		return WordPlay.sanitize_word((word_value << rotate_amount) | (word_value >> (32 - rotate_amount)))

	@staticmethod
	def rotate_right(word_value, rotate_amount):
		return WordPlay.sanitize_word((word_value << (32 - rotate_amount)) | (word_value >> rotate_amount))

	@staticmethod
	def as_signed(word_value):
		if word_value & 0x80000000:
			return -(WordPlay.not_word(word_value) + 1)
		return word_value

class Memory(object):
	def __init__(self, memory_miss_handler=None):
		self.content = {}
		self.default = 0x00000000
		self.memory_miss_handler = memory_miss_handler

	@staticmethod
	def _get_aligned_address(address):
		return address & 0xFFFFFFFC

	def load_file(self, file_path, base_address):

		file_size = 0

		with open(file_path, 'rb') as f:
			file_size = os.fstat(f.fileno()).st_size
			
			address = base_address
			counter = file_size
			word_value = 0

			while counter > 0:
				if counter >= 4:
					word_value = f.read(4)
					counter -= 4

				else:
					word_value = f.read(counter) + ('\0' * (4 - counter))
					counter = 0

				word_value = struct.unpack('I', word_value)[0]

				self.set_word(address, word_value)
				address += 4

		return file_size

	def _shared_word_get(self, address):
		try:
			return self.content[address]

		except KeyError:
			if self.memory_miss_handler is None:
				return self.default

			return self.memory_miss_handler(self, address, self.default)

		raise Exception('Memory Read entered bad state')

	def get_word(self, address):
		aligned_address = Memory._get_aligned_address(address)
		return self._shared_word_get(aligned_address)

	def get_hword(self, address):
		aligned_address = Memory._get_aligned_address(address)
		word_value = self._shared_word_get(aligned_address)
		return WordPlay.get_hword(word_value, (address >> 1) & 1)

	def get_byte(self, address):
		aligned_address = Memory._get_aligned_address(address)
		word_value = self._shared_word_get(aligned_address)
		return WordPlay.get_byte(word_value, address & 3)

	def set_word(self, address, word_value):
		aligned_address = Memory._get_aligned_address(address)
		self.content[aligned_address] = word_value

	def set_hword(self, address, hword_value):
		aligned_address = Memory._get_aligned_address(address)
		word_value = self._shared_word_get(aligned_address)
		self.content[aligned_address] = WordPlay.replace_hword(word_value, (address >> 1) & 1, hword_value)

	def set_byte(self, address, byte_value):
		aligned_address = Memory._get_aligned_address(address)
		word_value = self._shared_word_get(aligned_address)
		self.content[aligned_address] = WordPlay.replace_byte(word_value, address & 3, byte_value)

class CPUIntegerRegister(object):
	def __init__(self, name, value=0):
		self.name = name
		self.value = value

	def set(self, word_value):
		self.value = word_value

	def get(self):
		return self.value

	def get_signed(self):
		return WordPlay.as_signed(self.value)

	def add(self, word_value):
		return WordPlay.sanitize_word(self.value + word_value)

	def sub(self, word_value):
		return WordPlay.sanitize_word(self.value - word_value)

	def logical_shift_left(self, shift_amount):
		return WordPlay.logical_shift_left(self.value, shift_amount)

	def logical_shift_right(self, shift_amount):
		return WordPlay.logical_shift_right(self.value, shift_amount)

	def arithmethic_shift_left(self, shift_amount):
		return WordPlay.arithmethic_shift_left(self.value, shift_amount)

	def arithmetic_shift_right(self, shift_amount):
		return WordPlay.arithmetic_shift_right(self.value, shift_amount)

	def rotate_left(self, rotate_amount):
		return WordPlay.rotate_left(self.value, rotate_amount)

	def rotate_right(self, rotate_amount):
		return WordPlay.rotate_right(self.value, rotate_amount)

class CPUZeroRegister(CPUIntegerRegister):
	def __init__(self, name):
		CPUIntegerRegister.__init__(self, name, 0)

	def set(self, word_value):
		return

class CPUGeneralPurposeRegisters(object):
	def __init__(self):
		self.zero = CPUZeroRegister('zero')
		self.at = CPUIntegerRegister('at')
		self.v0 = CPUIntegerRegister('v0')
		self.v1 = CPUIntegerRegister('v1')
		self.a0 = CPUIntegerRegister('a0')
		self.a1 = CPUIntegerRegister('a1')
		self.a2 = CPUIntegerRegister('a2')
		self.a3 = CPUIntegerRegister('a3')
		self.t0 = CPUIntegerRegister('t0')
		self.t1 = CPUIntegerRegister('t1')
		self.t2 = CPUIntegerRegister('t2')
		self.t3 = CPUIntegerRegister('t3')
		self.t4 = CPUIntegerRegister('t4')
		self.t5 = CPUIntegerRegister('t5')
		self.t6 = CPUIntegerRegister('t6')
		self.t7 = CPUIntegerRegister('t7')
		self.s0 = CPUIntegerRegister('s0')
		self.s1 = CPUIntegerRegister('s1')
		self.s2 = CPUIntegerRegister('s2')
		self.s3 = CPUIntegerRegister('s3')
		self.s4 = CPUIntegerRegister('s4')
		self.s5 = CPUIntegerRegister('s5')
		self.s6 = CPUIntegerRegister('s6')
		self.s7 = CPUIntegerRegister('s7')
		self.t8 = CPUIntegerRegister('t8')
		self.t9 = CPUIntegerRegister('t9')
		self.k0 = CPUIntegerRegister('k0')
		self.k1 = CPUIntegerRegister('k1')
		self.gp = CPUIntegerRegister('gp')
		self.sp = CPUIntegerRegister('sp')
		self.fp = CPUIntegerRegister('fp')
		self.ra = CPUIntegerRegister('ra')

		# Optimization: Pre-declare these tuples
		self._register_look_up_table = (self.zero, self.at, self.v0, self.v1, self.a0, self.a1, self.a2, self.a3, 
				self.t0, self.t1, self.t2, self.t3, self.t4, self.t5, self.t6, self.t7, 
				self.s0, self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7, 
				self.t8, self.t9, self.k0, self.k1, self.gp, self.sp, self.fp, self.ra)

	def __getitem__(self, key):
		return self._register_look_up_table[key]

	def dump(self):
		for register in self._register_look_up_table:
			print register.name + ':', '0x' + format(register.value, '08X'), 
		print ''

class CPURegisters(object):
	def __init__(self):
		self.gp = CPUGeneralPurposeRegisters()
		self.pc = CPUIntegerRegister('pc')
		self.lo = CPUIntegerRegister('lo')
		self.hi = CPUIntegerRegister('hi')

class CPU(object):
	def __init__(self, start_address=0, memory_miss_handler=None):
		self.regs = CPURegisters()
		self.memory = Memory(memory_miss_handler)

		self.regs.pc.set(start_address)

		self._jump_clear()

		# Optimization: Pre-declare these tuples
		self._opcode_look_up_table = (
			self.opcode_00,
			self.opcode_01,
			self.opcode_02,
			self.opcode_03,
			self.opcode_04,
			self.opcode_05,
			self.opcode_06,
			self.opcode_07,
			None,
			self.opcode_09,
			self.opcode_0A,
			None,
			self.opcode_0C,
			None,
			None,
			self.opcode_0F,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			self.opcode_1F,
			self.opcode_20,
			self.opcode_21,
			self.opcode_22,
			self.opcode_23,
			self.opcode_24,
			self.opcode_25,
			self.opcode_26,
			None,
			self.opcode_28,
			self.opcode_29,
			None,
			self.opcode_2B
		)

		self._opcode_00_look_up_table = (
			self.opcode_00_funct_00,
			None,
			self.opcode_00_funct_02,
			self.opcode_00_funct_03,
			self.opcode_00_funct_04,
			None,
			self.opcode_00_funct_06,
			None,
			self.opcode_00_funct_08,
			None,
			None,
			self.opcode_00_funct_0B,
			None,
			None,
			None,
			None,
			self.opcode_00_funct_10,
			self.opcode_00_funct_11,
			None,
			None,
			None,
			None,
			self.opcode_00_funct_16,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			self.opcode_00_funct_21,
			self.opcode_00_funct_22,
			self.opcode_00_funct_23,
			None,
			self.opcode_00_funct_25,
			None,
			self.opcode_00_funct_27,
			None,
			None,
			self.opcode_00_funct_2A,
			self.opcode_00_funct_2B,
			self.opcode_00_funct_2C,
			self.opcode_00_funct_2D
		)

		self._opcode_1F_look_up_table = (
			self.opcode_1F_funct_00,
			None,
			None,
			None,
			self.opcode_1F_funct_04,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			self.opcode_1F_funct_20
		)
	def _jump_to(self, address):
		self.jump_delay = True
		self.jump_destination = address

	def _jump_clear(self):
		self.jump_delay = False
		self.jump_destination = None

	def execute(self):
		# Simulate pipeline delay
		current_fetch_address = self.regs.pc.get()
		if self.jump_delay is True:
			next_fetch_address = self.jump_destination
			self._jump_clear()
		else:
			next_fetch_address = self.regs.pc.add(4)
		
		# Check if valid memory
		#if current_fetch_address not in self.memory.content:
		#	raise Exception('Executing unhashed address: 0x%s' % format(current_fetch_address, '08X'))

		##Decode instruction
		instruction = self.memory.get_word(current_fetch_address)

		field_opcode = (instruction >> 26) & 0x3F
		field_rs     = (instruction >> 21) & 0x1F
		field_rt     = (instruction >> 16) & 0x1F
		field_rd     = (instruction >> 11) & 0x1F
		field_shamt  = (instruction >> 6) & 0x1F
		field_funct  = instruction & 0x3F

		field_imm    = instruction & 0xFFFF

		# Execute opcode
		try:
			self._opcode_look_up_table[field_opcode](field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm)

		except (UnknownOpcodeException, TypeError, IndexError):
			raise Exception('Unknwon opcode at 0x%s:\n\tOpcode: %s\n\tRs: %s\n\tRt: %s\n\tRd: %s\n\tShift Amount: %s\n\tFunct: %s' % (
					format(current_fetch_address, '08X'), 
					field_opcode,
					field_rs,
					field_rt,
					field_rd,
					field_shamt,
					field_funct
				))

		#self.regs.gp.dump()

		# Simulate pipeline delay
		self.regs.pc.set(next_fetch_address)

	def opcode_00_funct_00(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# sll: 000000 sssss ttttt ddddd aaaaa 000000
		self.regs.gp[field_rd].set(self.regs.gp[field_rt].logical_shift_left(field_shamt))

	def opcode_00_funct_02(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# srl: 000000 00000 ttttt ddddd aaaaa 000010
		if field_rs == 0x00:
			self.regs.gp[field_rd].set(self.regs.gp[field_rt].logical_shift_right(field_shamt))
		
		# rotr:  000000 00001 ttttt ddddd aaaaa 000010
		elif field_rs == 0x01:
			self.regs.gp[field_rd].set(self.regs.gp[field_rt].rotate_right(field_shamt))

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_03(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# sra: 000000 00000 ttttt ddddd aaaaa 000011
		if field_rs == 0x00:
			self.regs.gp[field_rd].set(self.regs.gp[field_rt].arithmetic_shift_right(field_shamt))
		else:
			raise UnknownOpcodeException()
		
	def opcode_00_funct_04(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# sllv: 000000 sssss ttttt ddddd 00000 000100
		if field_shamt == 0x00:
			self.regs.gp[field_rd].set(self.regs.gp[field_rt].logical_shift_left(self.regs.gp[field_rs].get() & 0x1F))
		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_06(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# srlv: 000000 sssss ttttt ddddd 00000 000110
		if field_shamt == 0x00:
			self.regs.gp[field_rd].set(self.regs.gp[field_rt].logical_shift_right(self.regs.gp[field_rs].get() & 0x1F))
		
		# rotrv: 000000 sssss ttttt ddddd 00001 000110
		elif field_shamt == 0x01:
			self.regs.gp[field_rd].set(self.regs.gp[field_rt].rotate_right(self.regs.gp[field_rs].get() & 0x1F))

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_08(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# jr: 000000 sssss 00000 00000 00000 001000
		if field_shamt == 0x00 and field_rd == 0x00 and field_rt == 0x00:
			self._jump_to(self.regs.gp[field_rs].get())

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_0B(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# movn: 000000 sssss ttttt ddddd 00000 001011
		if field_shamt == 0x00:
			if self.regs.gp[field_rt].get() != 0:
				self.regs.gp[field_rd].set(self.regs.gp[field_rs].get())

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_10(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# mfhi: 000000 00000 00000 ddddd 00000 010000
		if field_shamt == 0x00 and field_rs == 0x00 and field_rt == 0x00:
			self.regs.gp[field_rd].set(self.regs.hi.get())

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_11(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# mthi: 000000 sssss 00000 00000 00000 010001
		if field_shamt == 0x00 and field_rd == 0x00 and field_rt == 0x00:
			self.regs.hi.set(self.regs.gp[field_rs].get())

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_16(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# clz: 000000 sssss 00000 ddddd 00000 010110
		if field_shamt == 0x00 and field_rt == 0x00:
			temp = 32
			for i in xrange(31, -1, -1):
				if (self.regs.gp[field_rs].get() >> i) & 1 == 1:
					temp = 31 - i
					break
			self.regs.gp[field_rd].set(temp)

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_21(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# addu: 000000 sssss ttttt ddddd 00000 100001
		if field_shamt == 0x00:
			self.regs.gp[field_rd].set(self.regs.gp[field_rs].add(self.regs.gp[field_rt].get()))

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_22(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# sub: 000000 sssss ttttt ddddd 00000 100010
		if field_shamt == 0x00:
			self.regs.gp[field_rd].set(self.regs.gp[field_rs].sub(self.regs.gp[field_rt].get()))

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_23(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# subu: 000000 sssss ttttt ddddd 00000 100011
		if field_shamt == 0x00:
			self.regs.gp[field_rd].set(self.regs.gp[field_rs].sub(self.regs.gp[field_rt].get()))

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_25(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# or: 000000 sssss ttttt ddddd 00000 100101
		if field_shamt == 0x00:
			self.regs.gp[field_rd].set(self.regs.gp[field_rs].get() | self.regs.gp[field_rt].get())

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_27(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# not: 000000 sssss 00000 ddddd 00000 100111
		if field_shamt == 0x00:
			self.regs.gp[field_rd].set(self.regs.gp[field_rs].not_word())

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_2A(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# slt: 000000 sssss ttttt ddddd 00000 101010
		if field_shamt == 0x00:
			if self.regs.gp[field_rs].get_signed() < self.regs.gp[field_rt].get_signed():
				self.regs.gp[field_rd].set(1)
			else:
				self.regs.gp[field_rd].set(0)

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_2B(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# sltu: 000000 sssss ttttt ddddd 00000 101011
		if field_shamt == 0x00:
			if self.regs.gp[field_rs].get() < self.regs.gp[field_rt].get():
				self.regs.gp[field_rd].set(1)
			else:
				self.regs.gp[field_rd].set(0)

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_2C(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# max: 000000 sssss ttttt ddddd 00000 101100
		if field_shamt == 0x00:
			if self.regs.gp[field_rs].get_signed() > self.regs.gp[field_rt].get_signed():
				self.regs.gp[field_rd].set(self.regs.gp[field_rs].get())
			else:
				self.regs.gp[field_rd].set(self.regs.gp[field_rt].get())

		else:
			raise UnknownOpcodeException()

	def opcode_00_funct_2D(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# min: 000000 sssss ttttt ddddd 00000 101101
		if field_shamt == 0x00:
			if self.regs.gp[field_rs].get_signed() < self.regs.gp[field_rt].get_signed():
				self.regs.gp[field_rd].set(self.regs.gp[field_rs].get())
			else:
				self.regs.gp[field_rd].set(self.regs.gp[field_rt].get())

		else:
			raise UnknownOpcodeException()

	def opcode_00(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# Execute funct
		try:
			self._opcode_00_look_up_table[field_funct](field_rs, field_rt, field_rd, field_shamt, field_imm)

		except (TypeError, IndexError):
			raise UnknownOpcodeException()

	def opcode_01(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		
		# bltz: 000001 sssss 00000 iiii iiii iiii iiii
		if field_rt == 0x00:
			if self.regs.gp[field_rs].get_signed() < 0: 
				self._jump_to(self.regs.pc.add(4 + (WordPlay.sign_extend_hword(field_imm) << 2)))
		
		# bgez: 000001 sssss 00001 iiii iiii iiii iiii
		elif field_rt == 0x01:
			if self.regs.gp[field_rs].get_signed() >= 0: 
				self._jump_to(self.regs.pc.add(4 + (WordPlay.sign_extend_hword(field_imm) << 2)))

		# bltzal: 000001 sssss 10000 iiii iiii iiii iiii
		elif field_rt == 0x10:
			if self.regs.gp[field_rs].get_signed() < 0: 
				self.regs.gp.ra.set(self.regs.pc.add(8))
				self._jump_to(self.regs.pc.add(4 + (WordPlay.sign_extend_hword(field_imm) << 2)))

		else:
			raise UnknownOpcodeException()

	def opcode_02(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# j: 000010 ii iiii iiii iiii iiii iiii iiii
		imm = (field_rs << 21) | (field_rt << 16) |  field_imm
		self._jump_to((self.regs.pc.add(4) & 0xF0000000) | (imm << 2))

	def opcode_03(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# jal: 000011 ii iiii iiii iiii iiii iiii iiii
		imm = (field_rs << 21) | (field_rt << 16) |  field_imm
		self.regs.gp.ra.set(self.regs.pc.add(8))
		self._jump_to((self.regs.pc.add(4) & 0xF0000000) | (imm << 2))

	def opcode_04(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# beq: 000100 sssss ttttt iiii iiii iiii iiii
		if self.regs.gp[field_rs].get() == self.regs.gp[field_rt].get(): 
			self._jump_to(self.regs.pc.add(4 + (WordPlay.sign_extend_hword(field_imm) << 2)))

	def opcode_05(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# bne: 000101 sssss ttttt iiii iiii iiii iiii
		if self.regs.gp[field_rs].get() != self.regs.gp[field_rt].get(): 
			self._jump_to(self.regs.pc.add(4 + (WordPlay.sign_extend_hword(field_imm) << 2)))

	def opcode_06(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# blez: 000110 sssss 00000 iiii iiii iiii iiii
		if field_rt == 0x00:
			if self.regs.gp[field_rs].get_signed() <= 0: 
				self._jump_to(self.regs.pc.add(4 + (WordPlay.sign_extend_hword(field_imm) << 2)))

		else:
			raise UnknownOpcodeException()

	def opcode_07(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# bgtz: 000111 sssss 00000 iiii iiii iiii iiii
		if field_rt == 0x00:
			if self.regs.gp[field_rs].get_signed() > 0: 
				self._jump_to(self.regs.pc.add(4 + (WordPlay.sign_extend_hword(field_imm) << 2)))
		else:
			raise UnknownOpcodeException()

	def opcode_09(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# addiu: 001001 sssss ttttt iiii iiii iiii iiii
		self.regs.gp[field_rt].set(self.regs.gp[field_rs].add(WordPlay.sign_extend_hword(field_imm)))

	def opcode_0A(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# slti: 001010 sssss ttttt iiii iiii iiii iiii
		if self.regs.gp[field_rs].get_signed() < WordPlay.as_signed(WordPlay.sign_extend_hword(field_imm)):
			self.regs.gp[field_rt].set(1)
		else:
			self.regs.gp[field_rt].set(0)

	def opcode_0C(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# andi: 001100 sssss ttttt iiii iiii iiii iiii
		self.regs.gp[field_rt].set(self.regs.gp[field_rs].get() & WordPlay.zero_extend_hword(field_imm))

	def opcode_0F(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# lui: 001111 00000 ttttt iiii iiii iiii iiii
		if field_rs == 0x00:
			self.regs.gp[field_rt].set(field_imm << 16)
		else:
			raise UnknownOpcodeException()

	def opcode_1F_funct_00(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# ext: 011111 sssss ttttt eeeee aaaaa 000000
		size = field_rd + 1
		pos = field_shamt
		mask = ((1 << size) - 1)
		self.regs.gp[field_rt].set((self.regs.gp[field_rs].get() >> pos) & mask)

	def opcode_1F_funct_04(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# ins: 011111 sssss ttttt nnnnn NNNNN 000100 tsani
		size = (field_rd - field_shamt) + 1
		pos = field_shamt
		mask = ((1 << size) - 1)
		self.regs.gp[field_rt].set((self.regs.gp[field_rt].get() & WordPlay.not_word(mask << field_shamt)) | ((self.regs.gp[field_rs].get() & mask) << field_shamt))

	def opcode_1F_funct_20(self, field_rs, field_rt, field_rd, field_shamt, field_imm):
		# bitrev: 011111 00000 ttttt ddddd 10100 100000
		if field_shamt == 0x14 and field_rs == 0x00:
			self.regs.gp[field_rd].set(WordPlay.reverse_word(self.regs.gp[field_rt].get()))

		else:
			raise UnknownOpcodeException()

	def opcode_1F(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# Execute funct
		try:
			self._opcode_1F_look_up_table[field_funct](field_rs, field_rt, field_rd, field_shamt, field_imm)

		except (TypeError, IndexError):
			raise UnknownOpcodeException()

	def opcode_20(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# lb: 100000 sssss ttttt iiii iiii iiii iiii
		self.regs.gp[field_rt].set(WordPlay.sign_extend_byte(self.memory.get_byte(self.regs.gp[field_rs].add(WordPlay.sign_extend_hword(field_imm)))))

	def opcode_21(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# lh: 100001 sssss ttttt iiii iiii iiii iiii
		self.regs.gp[field_rt].set(WordPlay.sign_extend_hword(self.memory.get_hword(self.regs.gp[field_rs].add(WordPlay.sign_extend_hword(field_imm)))))

	def opcode_22(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# lwl: 100010 sssss ttttt iiii iiii iiii iiii
		unaligned_source_address = self.regs.gp[field_rs].add(WordPlay.sign_extend_hword(field_imm))
		word_aligned_end_address = 4 * int((unaligned_source_address + 3) / 4)

		byte_counter = 0
		while unaligned_source_address < word_aligned_end_address:
			byte_read = self.memory.get_byte(unaligned_source_address)
			self.regs.gp[field_rt].set((self.regs.gp[field_rt].get() & WordPlay.not_word(0xFF000000 >> (8 * byte_counter))) | (byte_read << (8 * (3 - byte_counter))))
			unaligned_source_address += 1
			byte_counter += 1

	def opcode_23(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# lw: 100011 sssss ttttt iiii iiii iiii iiii
		self.regs.gp[field_rt].set(self.memory.get_word(self.regs.gp[field_rs].add(WordPlay.sign_extend_hword(field_imm))))

	def opcode_24(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# lbu: 100100 sssss ttttt iiii iiii iiii iiii
		self.regs.gp[field_rt].set(self.memory.get_byte(self.regs.gp[field_rs].add(WordPlay.sign_extend_hword(field_imm))))

	def opcode_25(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# lhu: 100101 sssss ttttt iiii iiii iiii iiii
		self.regs.gp[field_rt].set(self.memory.get_hword(self.regs.gp[field_rs].add(WordPlay.sign_extend_hword(field_imm))))

	def opcode_26(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# lwr: 100110 sssss ttttt iiii iiii iiii iiii
		unaligned_source_address = self.regs.gp[field_rs].add(WordPlay.sign_extend_hword(field_imm))
		word_aligned_end_address = 4 * int(unaligned_source_address / 4)

		byte_counter = 0
		while unaligned_source_address >= word_aligned_end_address:
			byte_read = self.memory.get_byte(unaligned_source_address, 0x00)
			self.regs.gp[field_rt].set((self.regs.gp[field_rt].get() & not_word(0xFF << (8 * byte_counter))) | (byte_read << (8 * byte_counter)))
			unaligned_source_address -= 1
			byte_counter += 1

	def opcode_28(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# sb: 101000 sssss ttttt iiii iiii iiii iiii
		self.memory.set_byte(self.regs.gp[field_rs].add(WordPlay.sign_extend_hword(field_imm)), WordPlay.sanitize_byte(self.regs.gp[field_rt].get()))

	def opcode_29(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# sh: 101001 sssss ttttt iiii iiii iiii iiii
		self.memory.set_hword(self.regs.gp[field_rs].add(WordPlay.sign_extend_hword(field_imm)), WordPlay.sanitize_hword(self.regs.gp[field_rt].get()))

	def opcode_2B(self, field_rs, field_rt, field_rd, field_shamt, field_funct, field_imm):
		# sw: 101011 sssss ttttt iiii iiii iiii iiii
		self.memory.set_word(self.regs.gp[field_rs].add(WordPlay.sign_extend_hword(field_imm)), self.regs.gp[field_rt].get())

