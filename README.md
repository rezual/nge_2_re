# Neon Genesis Evangelion 2: Another Cases (PSP)
## Reverse Engineering & Translation

## Translation Status:
- Text in Writable Section of Game Executable: 
	- [ ] 97.84% translated 
		- See game_app/section_data_translate.py
- Text in Read-Only Section of Game Executable: 
	- [ ] 28.65% translated
		- See game_app/section_rodata_translate.py
- umd0:/PSP_GAME/USRDIR/game/imtext.bin: 
	- [ ] 0% translated
		- [ ] 0% translated
			- See game_data/file_imtext_translate_part_1.py
		- [ ] 0% translated
			- See game_data/file_imtext_translate_part_2.py
		- [ ] 0% translated
			- See game_data/file_imtext_translate_part_3.py
		- [ ] 0% translated
			- See game_data/file_imtext_translate_part_4.py
		- [ ] 0% translated
			- See game_data/file_imtext_translate_part_5.py
- umd0:/PSP_GAME/USRDIR/btl/btimtext.bin: 
	- [ ] 0% translated
		- See game_data/file_btimtext_translate.py
- umd0:/PSP_GAME/USRDIR/free/f2info.bin: 
	- [ ] 0% translated
		- See game_data/file_f2info_translate.py
- umd0:/PSP_GAME/USRDIR/free/f2tuto.bin: 
	- [ ] 0% translated
		- See game_data/file_f2tuto_translate.py
- Images with text:
	- [ ] Pick all the images with text that need to be translated
	- [ ] Write up the text translations of the contents in the images
	- [ ] Modify images, removing text, replacing it with the background
	- [ ] Modify images, injecting text with proper font

## Reverse Engineering Status:
- Figure out .har file format, which is a package format containing several game files
	- [x] Extracting
		- See game_data/hgar.py's --decompress
	- [x] Modifying
		- See game_data/hgar.py's --replace
- Figure out how to decompress .zpt and other compressed files in the .har packages
	- [x] Decompressing
		- See game_data/zipped.py
	- [ ] Compressing
		- Skipping. It's unnecessary since we can load modified decompressed files into the game.
- Figure out the game's picture format.
	- Exporting
		- [ ] 90% done, some bugs remain
			- See game_data/hgpt.py
	- Importing
		- [ ] TODO
- Write a script to re-calculate text pointers so any translated text that can't fit in memory is moved elsewhere
	- [ ] TODO
- Figure out format of /USRDIR/game/imtext.bin - where most of the game dialog is stored
	- [ ] 90% done, bare minimum implemented
		- See game_data/bind.py
- Write custom PSP CFW plugin to patch the game and no longer rely on CWCheat
	- [ ] TODO

## File Breakdown:
###### Game App:
- game_app/app.py
	- Hardcoded wrapper for the game's executable, the decoded BOOT.BIN file
- game_app/section_data.py
	- Preliminary data-boundries in Writable memory and descriptions
- game_app/section_rodata.py
	- Preliminary data-boundries in Read-Only memory and descriptions
- game_app/section_text.py
	- Disassembly code and descriptions

###### Support Code:
- game_app/psp.py
	- Barebones PSP MIPS emulator, just enough implemented to run certain non-floating-point routines
- game_app/support.py
	- Shared definitions for various abstractions used by the Game App

###### Translation Files:
- game_app/section_data_translate.py
	- Japanese text in the Writable regions of the game executable
- game_app/section_rodata_translate.py
	- Japanese text in the Read-Only regions of the game executable

###### Scripts:
- game_app/generate_translate_cwcheat_codes.py
	- Generates CWCheat codes to patch the game.
- game_data/zipped.py
	- Decompress a .zpt file, as well as compressed files in .har packages (when used by hgar.py)
- game_data/hgar.py
	- Extract and decompress .har files
- game_data/hgpt.py
	- Convert to PPM .hpt picture files

