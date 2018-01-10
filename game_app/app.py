#!/usr/bin/env python2.7

import os

from support import *

if os.environ.get('LINK_TRANSLATE', 'false').lower() == 'true':
	from section_rodata_translate import *
	from section_data_translate import *	

else:
	from section_rodata import *
	from section_data import *

class App(object):
	base_address = 0x08804000

	section_init = AppSection('.init', 0x00000000, 0x00000024, AppSectionFlag.Allocated | AppSectionFlag.Executable)
	section_text = AppSection('.text', 0x00000040, 0x001AE74C, AppSectionFlag.Allocated | AppSectionFlag.Executable)
	section_fini = AppSection('.fini', 0x001AE78C, 0x0000001C, AppSectionFlag.Allocated | AppSectionFlag.Executable)
	section_sceStub_text = AppSection('.sceStub.text', 0x001AE7A8, 0x00000528, AppSectionFlag.Allocated |AppSectionFlag.Executable)
	section_lib_ent_top = AppSection('.lib.ent.top', 0x001AECD0, 0x00000004, AppSectionFlag.Allocated)
	section_lib_ent = AppSection('.lib.ent', 0x001AECD4, 0x00000010, AppSectionFlag.Allocated)
	section_lib_ent_btm = AppSection('.lib.ent.btm', 0x001AECE4, 0x00000004, AppSectionFlag.Allocated)
	section_lib_stub_top = AppSection('.lib.stub.top', 0x001AECE8, 0x00000004, AppSectionFlag.Allocated)
	section_lib_stub = AppSection('.lib.stub', 0x001AECEC, 0x0000017C, AppSectionFlag.Allocated)
	section_lib_stub_btm = AppSection('.lib.stub.btm', 0x001AEE68, 0x00000004, AppSectionFlag.Allocated)
	section_rodata_sceModuleInfo = AppSection('.rodata.sceModuleInfo', 0x001AEE6C, 0x00000034, AppSectionFlag.Allocated)
	section_rodata_sceResident = AppSection('.rodata.sceResident', 0x001AEEA0, 0x00000190, AppSectionFlag.Allocated)
	section_rodata_sceNid = AppSection('.rodata.sceNid', 0x001AF030, 0x00000294, AppSectionFlag.Allocated)
	section_ctors = AppSection('.ctors', 0x001AF2C4, 0x00000008, AppSectionFlag.Allocated | AppSectionFlag.Writable)
	section_dtors = AppSection('.dtors', 0x001AF2CC, 0x00000008, AppSectionFlag.Allocated | AppSectionFlag.Writable)
	section_jcr = AppSection('.jcr', 0x001AF2D4, 0x00000004, AppSectionFlag.Allocated | AppSectionFlag.Writable)
	section_eh_frame = AppSection('.eh_frame', 0x001AF2D8, 0x0000130C, AppSectionFlag.Allocated)
	section_gcc_except_table = AppSection('.gcc_except_table', 0x001B05E4, 0x00000054, AppSectionFlag.Allocated)
	section_rodata = section_rodata
	section_data = section_data

	sections = {
		section_init.name: section_init,
		section_text.name: section_text,
		section_fini.name: section_fini,
		section_sceStub_text.name: section_sceStub_text,
		section_lib_ent_top.name: section_lib_ent_top,
		section_lib_ent.name: section_lib_ent,
		section_lib_ent_btm.name: section_lib_ent_btm,
		section_lib_stub_top.name: section_lib_stub_top,
		section_lib_stub.name: section_lib_stub,
		section_lib_stub_btm.name: section_lib_stub_btm,
		section_rodata_sceModuleInfo.name: section_rodata_sceModuleInfo,
		section_rodata_sceResident.name: section_rodata_sceResident,
		section_rodata_sceNid.name: section_rodata_sceNid,
		section_ctors.name: section_ctors,
		section_dtors.name: section_dtors,
		section_jcr.name: section_jcr,
		section_eh_frame.name: section_eh_frame,
		section_gcc_except_table.name: section_gcc_except_table,
		section_rodata.name: section_rodata,
		section_data.name: section_data
	}

	title = 'Shinseiki Evangelion 2: Tsukurareshi Sekai - Another Cases'
	serial_number = 'ULJS-00064' 

	@staticmethod
	def decrypted_md5():
		return '8d26e5b1e432adf950eb7976316a9bc3'

	@staticmethod
	def decrypted_sha1():
		return 'b2857497b268066ae42c1c708ba66181f354acf2' 

	@staticmethod
	def encrypted_md5():
		return '5ef01bba69113a1bd22f8348b62a803e'

	@staticmethod
	def encrypted_sha1():
		return 'cc28a44e4e8b07b11c3e7d1afa209f7f933095be'

	@staticmethod
	def section_via_address(address):
		address -= App.base_address

		for section in App.sections.itervalues():
			if address >= section.start_address and address < section.end_address:
				return section

		return None

