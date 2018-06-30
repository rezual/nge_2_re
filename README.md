# Neon Genesis Evangelion 2: Another Cases (PSP)
## Reverse Engineering & Translation

## Translation Status:
- Text in Writable Section of Game Executable:
	- [ ] 100.00% translated - See game_app/section_data_translate.py
- Text in Read-Only Section of Game Executable:
	- [ ] 61.31% translated - See game_app/section_rodata_translate.py
- umd0:/PSP_GAME/USRDIR/game/imtext.bin:
	- [ ] 0.00% translated (in total)
		- [ ] 0.00% translated - See patches/imtext_1.py
		- [ ] 0.00% translated - See patches/imtext_2.py
		- [ ] 0.00% translated - See patches/imtext_3.py
		- [ ] 0.00% translated - See patches/imtext_4.py
		- [ ] 0.00% translated - See patches/imtext_5.py
- umd0:/PSP_GAME/USRDIR/*.evs:
	- [ ] 12.09% translated (in total)
		- [ ] 16.07% translated - See patches/evs_1.py
		- [ ] 8.66% translated - See patches/evs_2.py
		- [ ] 11.55% translated - See patches/evs_3.py
- umd0:/PSP_GAME/USRDIR/btl/btimtext.bin:
	- [ ] 37.28% translated - See patches/btimtext.py
- umd0:/PSP_GAME/USRDIR/free/f2info.bin:
	- [ ] 25.00% translated - See patches/f2info.py
- umd0:/PSP_GAME/USRDIR/free/f2tuto.bin:
	- [ ] 0.00% translated - See patches/f2tuto.py
- Images with text:
	- [ ] Pick all the images with text that need to be translated
	- [ ] Write up the text translations of the contents in the images
	- [ ] Modify images, removing text, replacing it with the background
	- [ ] Modify images, injecting text with proper font

## Reverse Engineering Status:
- Figure out .har file format, which is a package format containing several game files
	- [x] Extracting
		- See tools/hgar.py's --decompress
	- [x] Modifying
		- See tools/hgar.py's --replace
- Figure out how to decompress .zpt and other compressed files in the .har packages
	- [x] Decompressing
		- See tools/zipped.py
	- [ ] Compressing
		- TODO.
- Figure out the game's picture format.
	- Exporting
		- [ ] 90% done, some bugs remain
			- See tools/hgpt.py
	- Importing
		- [ ] 90% done, some bugs remain.
- Write a script to re-calculate text pointers so any translated text that can't fit in memory is moved elsewhere
	- [ ] TODO
- Figure out format of /USRDIR/game/imtext.bin - where most of the game dialog is stored
	- [ ] 90% done, bare minimum implemented
		- See tools/bind.py (Currently in game_data, needs to be fixed up)
		- See tools/text.py
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
- game_app/support.py
	- Shared definitions for various abstractions used by the Game App
- tools/png.py
	- Third-party PNG library

###### Translation Files:
- patches/section_data_translate.py
	- Japanese text in the Writable regions of the game executable
- patches/section_rodata_translate.py
	- Japanese text in the Read-Only regions of the game executable
- patches/imtext_#.py
- patches/btimtext.py
- patches/f2info.py
- patches/f2tuto.py
- patches/evs_#.py

###### Scripts:
- tools/zipped.py
	- Decompress a .zpt file, as well as compressed files in .har packages (when used by hgar.py)
- tools/hgar.py
	- Extract and decompress .har files
- tools/hgpt.py
	- Convert to PPM .hpt picture files
- game_data/bind.py
	- Parse .bin files with a magic header of TEXT or BIND
- tools/wave.py
	- Pack/Unpack .bin files in the umd0:/PSP_GAME/USRDIR/voice/ folder
	- You will need an atrac3plus codec to listen to the unpacked .wav files
		- ffmpeg -i ?.wav ?.mp3 works

###### Misc. Cheats:
These are the cheats made in the course of this project:

```
_C0 Pulse autowin
This disables player input in the Pulse mini-game
which is needed to prevent a crash from player input
interferring and then changes the Miss check to go 
to a Win check
_L 0x2005B478 0x00000000
_L 0x2005B5FC 0x00000000
_L 0x2005B5CC 0x0A216D82
_L 0x2005B5C4 0x00000000
```

```
_C0 Frame-skip mode
Press start to toggle frame-skip mode
Press digital up to progress normally
Tap digital right or L trigger to progress ahead one frame
Press R to fast forward time
_L 0x202FB8DC 0x00000001
```
