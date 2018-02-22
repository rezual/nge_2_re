# Neon Genesis Evangelion 2: Another Cases (PSP)
## Reverse Engineering & Translation

## Translation Status:
- Text in Writable Section of Game Executable: 
	- [ ] 40.29% translated 
		- See game_app/section_data_translate.py
- Text in Read-Only Section of Game Executable: 
	- [ ] 1.54% translated
		- See game_app/section_rodata_translate.py
- Images with text:
	- [ ] Pick all the images with text that need to be translated
	- [ ] Write up the text translations of the contents in the images
	- [ ] Modify images, removing text, replacing it with the background
	- [ ] Modify images, injecting text with proper font
- /USRDIR/game/imtext.bin: 
	- [ ] 0% translated
		- Format not yet understood

## Reverse Engineering Status:
- Figure out .har file format, which is a package format containing several game files
	- Extracting
		- [x] Done
			- See game_data/hgar.py's --decompress
	- Modifying
		- [x] Done
			- See game_data/hgar.py's --replace
- Figoure out how to decompress .zpt and other compressed files in the .har packages
	- Decompressing
		- [x] Done
			- See game_data/zipped.py
	- Compressing
		- [ ] Skipping
			- Unnecessary, since we can import into the game the decompressed but modified files
- Figure out the game's picture format.
	- Exporting
		- [ ] 90% done, some bugs remain
			- See game_data/hgpt.py
	- Importing
		- [ ] TODO
- Write a script to re-calculate text pointers so any translated text that can't fit in memory is moved elsewhere
	- [ ] TODO
- Figure out format of /USRDIR/game/imtext.bin - where most of the game dialog is stored
	- [ ] TODO
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

