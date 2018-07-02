# Neon Genesis Evangelion 2: Another Cases (PSP)
# Reverse Engineering & Translation
## Foreword
The translation is still a work in progress, and the tools are aimed at developers/translators,
and are not the tools the final patch user will ever need to use or install.
In its final form, the patch will be one or two files and a one-step apply process.

## Contribution
WIP: Currently ironing out processes before opening up the contribution flood-gates.

## Text Translation Status:
- Text in Game Executable located at `umd0:/PSP_GAME/SYSDIR/EBOOT.BIN`:
	- [ ] 100.00% translated Writable sections - See patches/eboot_data.py
	- [ ] 61.31% translated Read-Only sections - See patches/eboot_rodata.py
- Conversation text: `umd0:/PSP_GAME/USRDIR/game/imtext.bin`:
	- [ ] 0.00% translated (in total)
		- [ ] 0.00% translated - See patches/imtext_1.py
		- [ ] 0.00% translated - See patches/imtext_2.py
		- [ ] 0.00% translated - See patches/imtext_3.py
		- [ ] 0.00% translated - See patches/imtext_4.py
		- [ ] 0.00% translated - See patches/imtext_5.py
- Scripted event text (`.evs` files) located in various `.har` files: `umd0:/PSP_GAME/USRDIR/`:
	- [ ] 12.09% translated (in total)
		- [ ] 16.07% translated - See patches/evs_1.py
		- [ ] 8.66% translated - See patches/evs_2.py
		- [ ] 11.55% translated - See patches/evs_3.py
- Battle mode text: `umd0:/PSP_GAME/USRDIR/btl/btimtext.bin`:
	- [ ] 37.28% translated - See patches/btimtext.py
- Secret Information menu text: `umd0:/PSP_GAME/USRDIR/free/f2info.bin`:
	- [ ] 25.00% translated - See patches/f2info.py
- Tutorial menu text: `umd0:/PSP_GAME/USRDIR/free/f2tuto.bin`:
	- [ ] 0.00% translated - See patches/f2tuto.py

## Image Translation Status
- Images with text:
	- [ ] Pick all the images with text that need to be translated
	- [ ] Write up the text translations of the contents in the images
	- [ ] Modify images, removing text, replacing it with the background
	- [ ] Modify images, injecting text with proper font

## Reverse Engineering Status:
- [x] Unpack `.har` files
- [x] Decompress `.zpt` files/`.har` entries
- [x] Unpack WAVE `.bin` files
- [x] Unpack BIND `.bin` files
- [x] Modify/Repack `.har` files
- [x] Modify/Repack WAVE `.bin` files
- [x] Modify/Repack BIND `.bin` files
- [x] Export TEXT `.bin` files
- [x] Import/Patch TEXT `.bin` files
- [ ] 99.0% Export HGPT pictures 
- [ ] 90.0% Import HGPT pictures 
- [ ] Compress `.zpt` files/`.har` entries
- [ ] Write custom PSP CFW plugin to apply translation
	- Replace directly in memory translated text shorter than the original Japanese text (Easy)
	- Redirect assembly read/writes to other areas of memory for translated text longer than the original Japanese text (Hard)
	- Instead of allocating a new buffer, possibly
- [ ] Wait for translators
- [ ] Release

## Project Folder Breakdown
- **game_app:** Contains the game disassembly as Python code.
	- app.py: Python summary of the decrypted EBOOT.bin information
	- section_data.py: Contains a listing of the read-writeable addresses within the game and descriptions
	- section_rodata.py: Contains a listing of the read-only addresses within the game and descriptions
	- section_text.py: The game disassembly
	- support.py: Support functions and classes for the above files
- **patches:** 
	-   `eboot_data.py`
	    -   Translation patches for the writable parts of the game code, in the  `umd0:/PSP_GAME/SYSDIR/EBOOT.BIN`  file
	    -   No method to apply yet
	-   `eboot_rodata.py`
	    -   Translation patches for the read-only parts of the game code, in the  `umd0:/PSP_GAME/SYSDIR/EBOOT.BIN`  file
	    -   No method to apply yet
	-   `f2info.py`
	    -   Translation patches for the text entries in the game’s Secret Information menu
	    -   Can be applied with:  `text.py --patch path_to_extracted_game/PSP_GAME/USRDIR/free/f2info.bin path_to_toolchain/patches/f2info.py`
	-   `f2tuto.py`
	    -   Translation patches for the text entries in the game's Tutorial menu
	    -   Can be applied with:  `text.py --patch path_to_extracted_game/PSP_GAME/USRDIR/free/f2tuto.bin path_to_toolchain/patches/f2tuto.py`
	-   `imtext_#.py`
	    -   Translation patches for the TEXT  `.bin`'s in the BIND  `umd0:/PSP_GAME/USRDIR/game/imtext.bin`
	    -   The BIND  `.bin`  will need to be unpacked with  `tools/bind.py --unpack`  and then you can use  `text.py --patch`  to patch the resulting TEXT  `.bin`'s, followed by re-packing the files with  `tools/bind.py --repack`  again
	-   `btimtext.py`
	    -   Translation patches for the TEXT  `.bin`'s in the BIND  `umd0:/PSP_GAME/USRDIR/btl/btimtext.bin`
	    -   The BIND  `.bin`  will need to be unpacked with  `tools/bind.py --unpack`  and then you can use  `text.py --patch`  to patch the resulting TEXT  `.bin`'s, followed by re-packing the files with  `tools/bind.py --repack`  again
	-   `evs_#.py`
	    -   Translation patches for the  `.evs`  scripts found in unpacked event  `.har`  files. They'll need to be patched with  `tools/evs.py`  (WIP) followed by re-injecting the patched  `.evs`  into the  `.har`  file using  `tools/hgar.py --replace-raw`
- **tools:**
	- `wave.py`: Pack/Unpack WAVE `.bin` files in: `umd0:/PSP_GAME/USRDIR/voice/` 
	- `bind.py`: Pack/Unpack BIND `.bin` files, `umd0:/PSP_GAME/USRDIR/game/imtext.bin` and `umd0:/PSP_GAME/USRDIR/btl/btimtext.bin`
	- `text.py`: Export/Import/Patch TEXT `.bin` files, found in BIND `.bin` files after unpacking, and `umd0:/PSP_GAME/USRDIR/free/f2tuto.bin` along with `umd0:/PSP_GAME/USRDIR/free/f2info.bin`
	- `hgar.py`: Unpack/Modify `.har` files. Uses `zipped.py` to decompress, but cannot recompress. Use `--replace-raw` to replace files & turn-off the compression bit, where-as `--replace` keeps the compression bit on.
	- `zipped.py`: Decompress `.zpt` files, and in the future, be able to recompress (WIP)
	- `hgpt.py`: Export/Import Pictures (WIP)
	- `evs.py`: Export Event Scripts (WIP)
- **unused:** These files are no longer used but may be helpful to others

## Debug Mode:
These are pieces of debug mode found in the course of this project.

1. Player Position & Memory/CPU usage:

  ![](https://i.imgur.com/mWBdZW9.png)

2. Some kind of map trigger viewer:

  ![](https://i.imgur.com/YgnCVvG.png)

3. General Debug Menu with various features:

  ![](https://i.imgur.com/mopj0Kh.png)

  Currently looking into a cleaner way to enter this menu, but to activate:
  1. Make sure no menus/messageboxes are visible in the game when you enable this, since it hooks unto the menu handler to open up a new menu.
  2. Set 0x088CB750 to 0x0A226130 ( j 0x088984c0 )
  3. Go back to the game and press O, the debug menu should pop up.

  To return to the game, since you won't be able to cancel out of the debug menu by pressing X:
  1. First set 0x088CB750 back to 0x03E00008 to disable the cheat ( jr ra )
  2. Careful: Press X once, it'll put you into the regular O-menu
  3. Press O on something (like Items) to load a new menu so it fixes the menu stack, cause pressing X will most likely crash
  4. Once the new menu loads, now you may use X to exit out of the menu.

## Cheats:
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
