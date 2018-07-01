# Contributing to the Neon Genesis Evangelion 2: Another Cases (PSP) translation

1. Setting up your development environment
2. Familiarizing yourself with the game's directory hierarchy
3. Extracting it all
4. Familiarizing yourself with the patches
5. Translation Conventions

## Setting up your development environment

### What you'll need:
- Actual UMD of the game: Neon Genesis Evangelion 2 - Another Cases / ULJS-00064
- Actual PSP with CFW (Custom Firmware)
- Mini USB cable

### 1. Setting up the PPSSPP emulator with the official Sony font
If you don't do this, then fonts within the emulator will be glitched/scrambled.

1. Install the PSP emulator "PPSSPP " from: https://www.ppsspp.org
2. Run PPSSPP, then go to File -> Open Memory Stick.
3. A file explorer window should open, with a single directory called PSP, enter it.
4. Create a directory within the PSP folder called flash0
5. Turn on your actual PSP with CFW
6. Press Select, a CFW menu should come up, "PRO VSH MENU"
7. Scroll down to "USB Device" and press right until you get "flash0"
8. Press Select to Accept and close the menu
9. Connect the PSP to your computer via the Mini USB cable
10. You should see a drive appear with the folders "codepage", "dic", "font", and "vsh"
11. Copy the "font" folder from the PSP's flash0 and paste it in the emulator's flash0 folder
12. Stop the USB session on the PSP (but don't disconnect the cable just yet).

### 2. Setting up the game from the actual UMD
The PPSSPP emulator can run game ISOs that have been unpacked.
This makes it easier to patch specific files on the fly.

1. Place the game UMD within the actual PSP
2. Press Select, a custom firmware menu should come up ("PRO VSH MENU")
3. Scroll down to "USB Device" and press right until you get "UMD Disc"
4. Press Select to Accept and close the menu
5. Connect the PSP to your computer via the Mini USB cable, or manually re-initiate USB session
6. You should see a drive appear with a single file, UMD9660.ISO
7. Copy the UMD9660.ISO file to your desktop.
8. Extract the contents of the ISO into a folder called "EVA_GAME" or whatever you prefer.
    WinRAR can be used to accomplish this.
9. When you're all done, press "Select" on your PSP, change the "USB Device" back to "Memory Stick", and press Select to Accept and close the menu

### 3. Setting up Python
The tooling for this project is currently written in Python 2.7 and as such you'll need it installed. If you're on MacOS X, a suitable Python version should already be installed.

1. Download the proper Python package for your machine. 
	If you're on a 64-bit Windows machine, download Windows x86-64 MSI installer
    If you're on a 32-bit Windows machine, or you're not sure, download Windows x86 MSI installer
    At time of writing, Python 2.7.15 was the latest version of the Python 2.7 branch: https://www.python.org/downloads/release/python-2715/
2. Run the Python package installer

### 4. Setting up tooling
These scripts will enable us to import, export, pack, unpack, and patch files while we work on translating them. Ultimately the final user will not need to do all this jut to patch the game,
but instead this is needed for developing the patch.
1. Go to https://github.com/rezual/nge_2_re
2. Click the big green "Clone or download" button.
	If you're familiar with Git, then do a Clone.
	If not, for now, do a Zip download,
	but do know that to contribute back you'll need to know how to contribute via Git and Github.
	(If you want some training using Git and Github, see: https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners )
3. Extract or clone the contents to a local folder.

There are only two folders to focus on:
- patches
	- Patches contain translations in a search/replace format or replace-at-address format
	- These are consumed by the tools to patch specific files
- tools
	- Scripts that can decompress/unpack/pack/convert/patch files. More and more functionality is slowly being added.

## Familiarizing yourself with the game's directory hierarchy
This is the file hierarchy of the game, and there are some file formats mentioned like .har.
The only thing you should know about them for now is that they're proprietary .zip files.
We'll be unzipping them in the next section.
Furthermore the other thing to keep in mind is that the game tends to reuse the .bin suffix for various formats.
- umd0:/PSP_GAME/SYSDIR/
	- BOOT.BIN - On new PSP games, like NGE2, a file filled with zeroes. This is the file Sony encrypts to make EBOOT.bin
	- EBOOT.BIN - Encrypted game code. Applying translation patches to it requires decrypting it first or applying translation patches during run-time. We've not yet tackled this problem besides applying game code translation patches as run-time cheat codes.
- umd0:/PSP_GAME/USRDIR/
	- btdemo - .har files containing what looks to be battle stage/character models
	- btface - .har files containing battle faces/Eva intercom faces
	- btl - .har files containing scenario specific battle menus and battle event scripts
		- b2event.har contains .evs scripts
		- bevent.har contains .evs scripts
		- tabris.har contains .evs scripts
		- btimtext.bin contains a bunch of (battle?) TEXT files BINDed together
	- chara - .har files containing character models and animations, but looks like most are unused (see "map")
	- event - .har files containing event pictures and .evs scripts,
	- face - character day-to-day conversation expressions
	- free
		- f2tuto.bin contains notes on game features accessible via the game's tutorial menu
		- f2info.bin contains the text entries for the game's secret information menu
		- status.har contains stylized player names possibly used for the status screen
	- game - various .har file containing game menu graphics
		- .dat - It is unknown what the .dat files are for
		- imtext.bin contains a bunch of (regular game?) TEXT files BINDed together
	- im - contains a bunch of .zpt pictures and a .har file; they seem to be hardcoded events in the game
	- map - contains models for maps as well as looks like duplicates character models and textures. Instead of loading the Asuka model from /chara/, they seem to duplicate the model per map.
	- modules - PSP .prx (think of them like Windows DLL files)
	- sound - Unknown format for game sounds and possibly music
	- voice
		- na0.bin, na1.bin, and na2.bin contain .wav files that use Sony's atrac3plus codec 

In essence,
1. Pictures:
	Pictures are stored all over in umd0:/PSP_GAME/USRDIR/.
	Some are in .har files (HGAR tool) as .hpt files (HGPT tool)
	Some are in .har files (HGAR tool, w/ --decompress) as .zpt files
	Some are in umd0:/PSP_GAME/USRDIR/im/ as .zpt files (zipped tool)
2. Text:
	The game stores text in various places in various formats:
	1. In the encrypted game executable located at umd0:/PSP_GAME/SYSDIR/EBOOT.BIN, as read-only text and read-writable text. (No tool yet for reinjecting these back yet)
	2. As .evs files (EVS tool) in .har files located in umd0:/PSP_GAME/USRDIR/event/ and umd0:/PSP_GAME/USRDIR/btl/
	3. As .bin files (TEXT tool) in umd0:/PSP_GAME/USRDIR/free/
	4. As BINDed .bin (BIND tool) as umd0:/PSP_GAME/USRDIR/btl/btimtext.bin or umd0:/PSP_GAME/USRDIR/game/imtext.bin 

## Extracting it all
So it's clear from above that a lot of the game's content is hidden behind .har files.
To extract it all:
- on Windows run: TODO, provide a glue script
- on MacOS X run: TODO, provide a glue script

This will take a while. Let it run overnight!
What the above scripts do is:
	1. To decompress the standalone picture files, run the zipped.py tool on all the .zpt files in umd0:/PSP_GAME/USRDIR/im/
	2. To unpack the .har files, run the hgar.py --decompress operation on all .har files in umd0:/PSP_GAME/USRDIR/ and if there are compressed files, it'll called zipped.py on them for us
	3. To convert all .hpt pictures to .png for us, run the hgpt.py --export operation on all .hpt.DECOMPRESSED files in umd0:/PSP_GAME/USRDIR/
	4. To convert all .zpt pictures to .png for us, run the hgpt.py --export operation on all .zpt.DECOMPRESSED files in umd0:/PSP_GAME/USRDIR/
	5. To unpack the voice files, run the wave.py --unpack tool on all .bin files in umd0:/PSP_GAME/USRDIR/voice/ (though they'll still need something that supports Sony's atrac3plus code to view, see ffmpeg)

You should now have a bunch of easily accessible decompressed and converted game content.
Despite this, you shouldn't delete the original files!

## Familiarizing yourself with the patches
In the the tooling ( https://github.com/rezual/nge_2_re ) you should notice two folders, patches and tools.

The patches directory contains the following:
- eboot_data.py
	- Translation patches for the read-and-write parts of the game code, the EBOOT.BIN file
	- No method to apply yet (besides run-time cheat codes, which don't solve the text being trimmed problem that requires translation data to be moved around in memory)
- eboot_rodata.py
	- Translation patches for the read-only parts of the game code, the EBOOT.BIN file
	- No method to apply yet (besides run-time cheat codes, which don't solve the text being trimmed problem that requires translation data to be moved around in memory)
- f2info.py
	- Translation patches for the text entries in the game’s Secret Information menu 
	- Can be applied with:
		```text.py --patch path_to_extracted_game/PSP_GAME/USRDIR/free/f2info.bin path_to_toolchain/patches/f2info.py```
- f2tuto.py
	- Translation patches for the text entries in the game's Tutorial menu
	- Can be applied with:
		```text.py --patch path_to_extracted_game/PSP_GAME/USRDIR/free/f2tuto.bin path_to_toolchain/patches/f2tuto.py```
- imtext_#.py
	- Translation patches for the file at umd0:/PSP_GAME/USRDIR/game/imtext.bin
	- The file is actually a bunch of files text.py can handle, that are BINDed together.
	- It'll need to be unpacked with bind.py (WIP) and then you can use text.py to patch it, followed by re-BINDing the files.
- btimtext.py
	- Translation patches for the file at umd0:/PSP_GAME/USRDIR/btl/btimtext.bin
	- The file is actually a bunch of files text.py can handle, that are BINDed together.
	- It'll need to be unpacked with bind.py (WIP) and then you can use text.py to patch it, followed by re-BINDing the files.
- evs_#.py
	- Script files that'll need to be patched (WIP) followed by reinjecting into the .har file (hgar.py --replace-raw)

## Translation Conventions

1. Technical Constraints
    1. The game's text is exported by the tooling in an UTF-8 encoding, but the game is in a modified Shift-JIS. When text is placed back in the game, it's converted from UTF-8 back to Shift-JIS.
    Regarding the "modified Shift-JIS", certain characters in UTF-8 become something else in the game.
    - The Greek `Θ` (0x83, 0xA6) becomes a `J.` If you see it, just put a regular `J.` .
    - The Greek `Α` (0x83, 0x9F) becomes an `A.` If you see it, just put a regular  `A.` .
    - The Greek `Τ` ( 0x83, 0xB1) becomes `T.` If you see it, just put a regular `T.` .
    - The Fullwidth Latin`Ｓ` ( 0x82, 0x72) becomes just an `S` If you see it, just put a regular `S` instead.
    - The Greek `Ν` (0x83, 0xAB) becomes `N²` If you see it, just put `N2` instead.
    - The Greek `Σ` (0x83, 0xB0) becomes `S²` If you see it, just put `S2` instead.
    - The standalone `²` does not exist in Shift-JIS, so if you use it, it won't be able to convert it back to the game!
    - The character `▽` is used to pause flow of message box text. Keep it in your translation.
 
    2. We use escapes to denote certain characters:
        A single `\` is actually` \\`
        A single `'` is actually `\'`
        A single `"` is actually `\"`
        A linebreak is `\n`

	C - The game uses special tokens to act as insertion points.
        Tokens such as `%s`, `%f`, `%d` are used by the game to insert text or numbers.
        Furthermore, the game uses tokens such as `$n` and `$c` for inserting other game specific information into a sentence.
        If you see such a token in the original Japanese, try to do your best to gauge what might be getting inserted, and restructure the sentence around that.
        TODO: Cut down on guess-work and create a table of token meanings.

    D - Positioning linebreaks (\n)
        For now do your best to match the linebreak position in the translation as where it appears in Japanese. Later we can go back and better rebalance the positions as we see how things wrap on screen, etc.

    E - The translations to the game code, if they're longer than the original Japanese text, will need to be moved elsewhere within the game code, and this is an involved process. For now, don't worry about this, but keep it in mind.

2. Translation Conventions
	1. **Honorifics?**
        - Menus (rodata/data): Keep them out
        - Elsewhere: Keep them in
        - Rationale:
	        - Menus don't have a lot of display space, thus keep it short to avoid over-runing the menu's edge
	2. **Include Last Names?**
        - Menus (rodata/data): Keep them out
        - Elsewhere: Keep them in
        - Rationale:
	        - Menus don't have a lot of display space, thus keep it short to avoid over-runing the menu's edge

	3. **Compound last name order: Asuka Soryu Langley or Asuka Langley Soryu?**
		- Place the Japanese surname first, which would be (Soryu) in this case.
        - Rationale:
	        - To match precedent with khara's official translations

	4. **Rename Japanese food names to something more familiar?**
        - No, keep the Japanese food name.
        - Strive to find the closest English word for the dish.
     
	5. **How to format Organization Names, SEELE or Seele, NERV or Nerv?**
        - Capitalize first letter, then lowercase the letters that follow.
        - Rationale:
	        - To keep precedent with khara's in-house translator
	6. **Expand Acronyms, JA or Jet Alone?**
		- Go with the source text.
		- If the source is JA, use J.A.
		- If the source is Jet Alone, use Jet Alone

    7. **Acronym Periods, AT or A.T.?**
        - If the acronym is TV, DNA, WC, omit the periods.
        - If the acronym is laser, do not treat it as an acronymn (despite it being so).
        - For everything else, add the periods.
        - Rationale:
	        - It matches precedent with the game's use of A.T. in menus.
	        - Unfamiliar acronyms (A.T., J.A., U.N.) should have periods to make it obvious that they're acronyms, while known acronyms like TV should not. Furthermore, roman acronyms within Japanese text already stand out, compared to Roman acronyms in fully Roman sentences which are harder to spot or might come across as typos.

    8. **Abbreviations, Prog Knife, or Prog. Knife, or Progressive Knife?**
        - Keep the abbreviation but leave out the period: Prog Knife
         - Rationale:
            Usually abbreviations are used for very common words,
            but Progressive is not common. So if one writes prog. it looks like a sentence end,
            and as such is jarring.

    9. **Capitalizing every word, Snack Attack or Snack attack?**
        - Depends on context.
        - Actions could be normal sentences:
	        - Open the door
	        - Press button
        - But Items / Attack Names should be capitalized:
	        - Ultra Spin Kick
	        - Lightning Storm

	10. **Eva Units, Eva-01 or Eva Unit-01?**
		- Depends on the source.
		- If it's, `初号機`, use `Eva-01`
		- If it's `エヴァ初号機`, use `Eva Unit-01`

	11. **Official terminology or Fan terminology:**
		These are cases where the fan community has their own terminology.
		The rule of thumb is to go with the official version.
			1. JA2 or JA Prime: Go with J.A.2
			2. For `秘密情報`, Classified Information or Confidential Information? Use Confidential Information. `機密` would be Classified Information.

  12. Recurring settled translations:
        These are phrases that may appear often,
        and it was decided that a more natural English translation should be used

        1 - 心の迷宮 (kokoro no meikyuu): literally "emotional maze", but instead go with "labyrinth of the heart" 

