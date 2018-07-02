# Contributing to the Neon Genesis Evangelion 2: Another Cases (PSP) translation

**This is a WIP guide. Bunch of formatting issues too; will fix soon**

1. Setting up your Development Environment
2. Familiarizing yourself with the Game's file formats and directories
3. Extracting it all
4. Familiarizing yourself with the Patches
5. Technical Considerations
6. Translation Conventions
7. Types of game translation crashes

## Setting up your Development Environment

### What you'll need:
- Actual UMD of the game: Neon Genesis Evangelion 2 - Another Cases / ULJS-00064
- Actual PSP with CFW (Custom Firmware)
- Mini USB cable

### 1. Setting up a PSP emulator with the official Sony font
If you don't do this, then fonts within the emulator will be glitched/scrambled.

1. Install the PSP emulator "PPSSPP " from: https://www.ppsspp.org
2. Run PPSSPP, then go to File -> Open Memory Stick.
3. A file explorer window should open, with a single directory called "PSP," enter it.
4. Create a directory within the "PSP" folder called flash0
5. Turn on your actual PSP with CFW
6. Press Select, a CFW menu should come up: "PRO VSH MENU"
7. Scroll down to "USB Device" and press right until you get "flash0"
8. Press Select to Accept and close the menu
9. Connect the PSP to your computer via the Mini USB cable
10. You should see a drive appear with the folders "codepage", "dic", "font", and "vsh"
11. Copy the "font" folder from the PSP's flash0 and paste it in the emulator's flash0 folder
12. Stop the USB session on the PSP (but don't disconnect the cable just yet).

### 2. Getting the game from the actual UMD and extracting it
The PPSSPP emulator can run game ISOs that have been extracted.
This makes it easier to patch specific files on the fly.

1. Place the game UMD within the actual PSP
2. Press Select, a custom firmware menu should come up: "PRO VSH MENU"
3. Scroll down to "USB Device" and press right until you get "UMD Disc"
4. Press Select to Accept and close the menu
5. Connect the PSP to your computer via the Mini USB cable, or manually re-initiate USB session
6. You should see a drive appear with a single file: "UMD9660.ISO"
7. Copy the "UMD9660.ISO" file to your desktop.
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

### 4. Setting up the nge_2_re tooling
The nge_2_re tooling will enable us to import, export, pack, unpack, and patch files while we work on translating them. It's important to note the final user will not need to do all this jut to patch the game,
but instead this is needed for developing the patch.
1. Go to https://github.com/rezual/nge_2_re
2. Click the big green "Clone or download" button
	If you're familiar with Git, then do a Clone
	If not, for now, do a Zip download,
	but do know that to contribute back you'll need to know how to contribute via Git and Github.
	(If you want some training using Git and Github, see: https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners )
3. Extract or clone the contents to a local folder called nge_2_re

There are only two folders of concern to translators within nge_2_re:
- **patches:**
	- Patches are translations in a search & replace format or replace-at-location format
	- These are consumed by scripts in the tools folder
- **tools:**
	- Scripts that can decompress/unpack/pack/convert/patch game data

## Familiarizing yourself with the Game's file formats and directories

The following is the game's directory hierarchy:

- **umd0:/PSP_GAME/SYSDIR/**
	- `EBOOT.BIN`: Encrypted game code. Applying translation patches to it requires decrypting it first or applying translation patches during run-time via an seplugin. We've not yet tackled this problem besides applying game code translation patches temporarily as run-time cheat codes
	- `BOOT.BIN`: On new PSP games, like NGE2, a file filled with zeroes. This is the file developers send to Sony, which Sony encrypts (& zeroes) to make EBOOT.bin
- **umd0:/PSP_GAME/USRDIR/**
	- `btdemo`: Maps, models, animations, and textures of battle stages, angels, and evas
	- `btface`: Character battle expressions, for use in Eva intercom
	- `btl`: Battle menu textures, and certain event scripts
	- `chara`: Models, textures, and animations for characters, but looks like most are unused (see `map`)
	- `event`: Event pictures/title-images and event scripts
	- `face`: Character day-to-day conversation expressions
	- `free`:  Text for game's Secret Information and Tutorial sections.
	- `game`: Game menu textures
	- `im`: Pictures for possibly hardcoded events in the game that don't need event scripts but just pictures
	- `map`: Maps, models, animations, and textures, for world maps as well as characters
		- Instead of loading the Asuka model from `/chara/`, they seem to duplicate the model per map
	- `modules`: Extra code modules used by the PSP .prx (think of them like Windows DLL files)
	- `sound`: Unknown format for game sounds and possibly music
	- `voice`: Voice clips

It should be noted that most of the game's files are packed/compressed within` .har` files. The only thing you should know about `.har` files for now is that they're proprietary `.zip` files. We'll be unzipping them in the next section. Furthermore, the game reuses the `.bin` suffix for various file formats. For clarity we'll add BIND/WAVE/TEXT/CODE before them, keeping in mind that BIND & WAVE `.bin` are archives that can be unpacked just like `.har` as well.

For translation, we're mainly interested in modifying pictures (which might contain Japanese text) and the Japanese text scattered across various places.

The game stores pictures all over `umd0:/PSP_GAME/USRDIR/`
- Some are in `.har` files as `.hpt` files
- Some are in `.har` files as `.zpt` files
- Some are in `umd0:/PSP_GAME/USRDIR/im/` as .zpt files
- At least two are in the game executable, in `umd0:/PSP_GAME/SYSDIR/EBOOT.BIN` as .zpt files
	- The Bandai logo screen and the Eva tenth anniversary screen

The game stores voice dialogue as Sony atrac3plus encoded `.wav` files in WAVE `.bin` files:
-  `umd0:/PSP_GAME/USRDIR/voice/na0.bin`
-  `umd0:/PSP_GAME/USRDIR/voice/na1.bin`
-  `umd0:/PSP_GAME/USRDIR/voice/na2.bin`

The game stores Japanese text in various places and formats as well:
- In the encrypted game executable: `umd0:/PSP_GAME/SYSDIR/EBOOT.BIN`
	- There's Japanese text in the read-only sections
	- There's Japanese text in read-writable sections
	- These are mainly menu text and short actions like "open door."
	- No tool yet for formally re-injecting these translations back
- As `.evs` files contained located in:
	- Almost every `.har` file in `umd0:/PSP_GAME/USRDIR/event/` 
	- In  the following `.har` files:
		- `umd0:/PSP_GAME/USRDIR/btl/b2event.har` 
		- `umd0:/PSP_GAME/USRDIR/btl/bevent.har` 
		- `umd0:/PSP_GAME/USRDIR/btl/tabris.har` 
- As TEXT `.bin` files:
	-  `umd0:/PSP_GAME/USRDIR/free/f2tuto.bin`
	- `umd0:/PSP_GAME/USRDIR/free/f2info.bin`
	- As TEXT files packed in BIND `.bin` files:
		-  `umd0:/PSP_GAME/USRDIR/btl/btimtext.bin` 
		- `umd0:/PSP_GAME/USRDIR/game/imtext.bin`

## Extracting it all
So it's clear from above that a lot of the game's content is hidden in archive files:
- `.har`
- WAVE `.bin`
- BIND `.bin`

To extract it all:
- on Windows run: TODO, provide a glue script
- on MacOS X run: TODO, provide a glue script

This will take a while. Let it run overnight!

What the extract-all scripts do is:
1. Ask for the path to where you extracted the contents of the game ISO to
2. Decompresses the standalone `.zpt` pictures in `umd0:/PSP_GAME/USRDIR/im/` by running `tools/zipped.py` on them
3. Unpacks and decompresses all the `.har` files in `umd0:/PSP_GAME/USRDIR/` by running `tools/hgar.py --decompress` on them (and calls `tools/zipped.py` for us if necessary)
4. Converts all `.hpt` pictures to `.png` for us by running `tools/hgpt.py --export` on all `.hpt.DECOMPRESSED` files in `umd0:/PSP_GAME/USRDIR/`
5. Converts all `.zpt` pictures to `.png` for us by running `tools/hgpt.py --export` on all `.zpt.DECOMPRESSED` files in `umd0:/PSP_GAME/USRDIR/`
6. Unpacks all the WAVE `.bin` files in `umd0:/PSP_GAME/USRDIR/voice/` by running  `tools/wave.py --unpack` 
	- Though to listen to them one'll still need a player that supports Sony's atrac3plus codec
		- One can install ffmpeg and do `ffmpeg -i in.wav out.mp3`

You should now have a bunch of easily accessible decompressed and converted game content.
Despite this, you shouldn't delete the original files!

## Familiarizing yourself with the Patches
In the the tooling ( https://github.com/rezual/nge_2_re ) you should notice two folders: `patches` and `tools`.

The `patches` directory contains the following:
- `eboot_data.py`
	- Translation patches for the writable parts of the game code, in the `umd0:/PSP_GAME/SYSDIR/EBOOT.BIN` file
	- No method to apply yet
- `eboot_rodata.py`
	- Translation patches for the read-only parts of the game code, in the `umd0:/PSP_GAME/SYSDIR/EBOOT.BIN` file
	- No method to apply yet
- `f2info.py`
	- Translation patches for the text entries in the game’s Secret Information menu
	- Can be applied with:
		```text.py --patch path_to_extracted_game/PSP_GAME/USRDIR/free/f2info.bin path_to_toolchain/patches/f2info.py```
- `f2tuto.py`
	- Translation patches for the text entries in the game's Tutorial menu
	- Can be applied with:
		```text.py --patch path_to_extracted_game/PSP_GAME/USRDIR/free/f2tuto.bin path_to_toolchain/patches/f2tuto.py```
- `imtext_#.py`
	- Translation patches for the TEXT `.bin`'s in the BIND `umd0:/PSP_GAME/USRDIR/game/imtext.bin`
	- The BIND `.bin` will need to be unpacked with `tools/bind.py` and then you can use `text.py` to patch the resulting TEXT `.bin`'s, followed by re-packing the files with `tools/bind.py` again
- `btimtext.py`
	- Translation patches for the TEXT `.bin`'s in the BIND `umd0:/PSP_GAME/USRDIR/btl/btimtext.bin`
	- The BIND `.bin` will need to be unpacked with `tools/bind.py` and then you can use `text.py` to patch the resulting TEXT `.bin`'s, followed by re-packing the files with `tools/bind.py` again
- `evs_#.py`
	- Translation patches for the `.evs` scripts found in unpacked event `.har` files. They'll need to be patched with `tools/evs.py` (WIP) followed by re-injecting the patched `.evs` into the `.har` file using `tools/hgar.py --replace-raw`

## Technical Considerations
1. The game's text uses Shift-JIS encoding with a few tweaks by the game's developers,
    to account for characters such as `²`  not existing in Shift-JIS.
	The nge_2_re tooling exports text to UTF-8, but it doesn't account for these customization,
	and we do not intend to utilize most of these customizations (except possibly S² and N² at a later time).
	But for now, if you see:
	- A Greek `Θ` `(ShiftJIS: 0x83, 0xA6)` the game renders as `J.`
		- If you see it, just put a regular `J.` 
    - A Greek `Α` `(ShiftJIS: 0x83, 0x9F)` the game renders as `A.`
	    - If you see it, just put a regular  `A.` 
    - A Greek `Τ` `(ShiftJIS: 0x83, 0xB1)` the game renders as `T.`
	    - If you see it, just put a regular `T.` .
    - A Greek `Ν` `(ShiftJIS: 0x83, 0xAB)` the game renders as `N²`
	    - If you see it, just put `N2` instead for now.
    - A Greek `Σ` `(ShiftJIS: 0x83, 0xB0)` the game renders as `S²`
	    - If you see it, just put `S2` instead for now.
    - The Fullwidth Latin`Ｓ` `(ShiftJIS: 0x82, 0x72)` the game renders as `S`
	    - If you see it, just put a regular `S` instead.
2. Please do not use the following characters in your translation since they cannot be converted to Shift-JIS:
	- The en dash `–` nor the em dash `—`
	- Superscripts `⁰`, `¹`, `²`, etc. 
	- Subscripts `₀`, `₁`, `₂`, etc.
3. We use Python quotes for containing the original Japanese and the translated text, and as such you need to understand certain concepts such as escape codes.
	If a `"` signifies the start of a block of text and another `"` signifies the end,
	how do we create a block of text that has a `"` as part of the text?
	Let's say we have the following text that we want to put in quotes:
		```The man's watch "froze" during the monday\tuesday transition```
		```when the storm happened.```
	A naive approach might be:
		```"The man's watch "```froze```" during the monday\t``` ```uesday transition,```
		```when the storm happened."```
	This has a couple of issues:
	- There's a `"` inside the text that's terminating the text-block early.
	- The line-break is not encapsulated by the `"` and will instead give errors.
	- The `\t` in `\tuesday` will actually get treated as a tab.
	
	This is because there are a set of sequences common across most programming languages, Python included, that start with a `\` and represent other characters.
	- To have a `"` that's part of the text, it should actually be written as  `\"`
	- With `\` being used to start special sequences, how to have a `\` that's part of the text? By doubling it up as `\\`
	- The other escape codes are a line-break, `\n` and tab, `\t`
	- And finally `\0` denotes a string terminator
		- The C programming language automatically adds a `\0`, but for this translation project we initially expected that fine control over `\0` placement will be needed but turns out that's not the case. For now continue placing `\0` manually, but we'll probably revisit this and automatically add `\0`.
	
	Finally with all that said, the correctly quoted text should be written as:
	```"The man's watch \"froze\" during the monday\\tuesday transition\nwhen the storm happened.\0"```
	
	And regarding character counts, it's important to keep in mind that when counting the number of characters,
	escape sequences are to be counted as one character, e.g. `\n` is one character.
4. The game uses special sequences of text to denote insertion points. We're still not sure what all the sequences are.
	The following are standard sequences across most modern programming languages:
	- `%s` is used to insert other pieces of text from elsewhere
	- `%f` is used to insert decimal numbers, like 3.14, or 1.68
	- `%d` is used to insert integers, like 4, 8, or 2
    
    The game then has its own sequences:
    - `$a` seems to be the active participant/subject/player
    - `$b` seems to be the passive participant/owner-of-object
    - `$c` seems to be an intruder/overriding subject/non-player subject
    - `$d` seems to be a number (or maybe angel ordinal)
    - `$n` seems to denote a super-line-break that triggers the start of a new page while `\n` triggers the start of a new line.
    - `$o` seems to be an item/object in subject's possession
    - `$p` seems to be an item/object in passive participant's possession
    
    The game also seems to have its own special characters:
    - The character `▽` is used to start a new "page" of dialog box text.

	When placing sequences in the translation, try to remap their position in the translation the best you can.

5. The translations to the game code (in `patches/eboot_rodata.py` and `patches/eboot_data.py`), if longer than the original Japanese text, will need to be moved elsewhere within the game code, and this is an involved process. For now, don't worry about this or length restrictions when translating until further notice.

## Translation Conventions
1. **Character names:**
	1. **Name order**: `First Name` before `Last Name`
		Example: Shinji Ikari
	2. **Compound last name order:** `Japanese Last Name` before `Foreign Last Name`
		Example: Asuka Soryu Langley
	3. **Honorifics:** Keep them. If you run into `Ikari Shinji-kun`, where the name order rule would make it `Shinji Ikari`, make it `Shinji Ikari-kun`
		Example: Shinji-kun.
	4. **Exceptions:** In menus (which are a few of the entries in `patches/eboot_rodata.py` & `patches/eboot_data.py`), drop the Last name and instead use the First name only to save on menu-screen space.
	5. **Special Considerations:**
		- `キール` `ローレンツ` should be Kiel Lorenz
		- `ペンペン` should be `Pen Pen`, and not `PenPen` nor `Pen-Pen`
		- `JA2`  should be `J.A.2`
2. **Other Names**
	1. **Organization Names:** Capitalize first letter, then lowercase the letters that follow.
		Example: Nerv, Seele
	2. **Food names:** Stay as close to the Japanese dish as possible
		Example: `弁当`  should be Bento
	3. **Angel Names:**
		Use the more modern Angel name spellings from the Eva Chronicle (left column): https://wiki.evageeks.org/Evangelion_Chronicle
	4. **Eva Units:**
		Follow the source,
		- If it's, `初号機`, use `Eva-01`
		- If it's `エヴァ初号機`, use `Eva Unit-01`
	6. **Special Considerations:**
		- `マギ` should be MAGI
		- `秘密情報` should be Confidential Information
		- `機密` should be Classified Information
3. **Acronyms:**
	1. **Expansion:** Do not expand if the source isn't expanded.
		Do: `JA` to `J.A.`
		Do Not: `JA` to `Jet Alone`
	2. **Periods:** Common acronyms that are not organizations/countries should OMIT periods. Non-common/Eva acronyms should maintain periods.
		Common acronyms: `TV`, `DNA`, `WC`, `UN`, `US`/`USA`
		Uncommon acronyms: `A.T.`, `J.A.`
4. **Abbreviations:**
	If it's a common word, keep the abbreviation and the period.
	For non-common/Eva words, keep the abbreviation but leave out the period.
	Do: Prog Knife
	Do Not: Prog. Knife
	Do Not: Progressive Knife
	Rationale:
	Usually abbreviations are used for very common words,
	but Progressive is not common. So if one writes prog. it looks like a sentence end,
	and as such is jarring.
5. **Word Casing:**
	Actions should be normal sentences,
	examples: `Open the door` and `Press button`
	But items and attack names should be capitalized,
	examples: `Ultra Spin Kick`, `Lightning Storm`, `Cold Pizza`
6. **Recurring settled translations:**
	These are phrases that may appear often,
	and it was decided that a more natural translation should be used:
        1. 心の迷宮 (kokoro no meikyuu): literally "emotional maze", but instead go with "labyrinth of the heart"
        2. Keel Lorenz, or Kiel Lorenz? Go with Kiel to be in-line with the most recent official translation of Kiel in the `Evangelion Chronicle`, and it's the more realistic German name.
7. **Angel Ordinals:**
	In the `.evs` files, you'll see `第$d使徒` for "The `$d` Angel." The `$d` just fills in a plain integer, and in Japanese the Kanji `第` makes the integer that follows it an ordinal. When translating, this doesn't work since it'll become `The 4 Angel` instead of `The 4th Angel`. 
	For now, go with `$dth`. We can revisit it by trying to modify the game code to generate the suffix properly later.
8. **Pronouns:**
	If due to script replacement via the game's use of `$a`, `$b`, `%s` makes it difficult to know the pronoun, go with `they/them/themselves`.
9. **Emphasis:** 
	1. Translate`「example here」` to `"example here"`
	2. Translate `He worked at Nerv -- a secret agency` to `He worked at Nerv, a secret agency.`
	3. Vocal loudness using uppercase: `I did NOT give him the cake.`
	4. Meaning emphasis using hyphens: `You don't understand, he -lost- the money`

# Types of game translation crashes
If there is a crash after injecting a translation into the game,
most likely the crash is one of the following classes:
1. Game crashes/freezes/fails silently because it expected text to be a certain length.
	- Already seen with *patches/f2tuto.py* and *patches/f2info.py*:
		- If text has more than 5 line-breaks, crash unless a new page is triggered via a special $n token
		- If text is more than 64 bytes (including the line-breaks), crash
2. Game crashes/freezes/fails silently/doesn't show properly because it expected text to start at a certain position within a bigger piece of text.
3. Game crashes/freezes/fails silently because it's scanning text for a certain character that was removed.
4. Game crashes/freezes/fails silently because it expected text to be a certain value,
or text was translated that wasn't text but a number that happened to register as Japanese text.
(Most likely the case for things in *patches/rodata.py* /data that are 1 or 2 Kanji)
5. Game crashes/freezes/fails silently because it ran out of memory due to the translated text exerting different memory pressure
6. Untranslated text appears
7. Translated text overruns/is badly linebreaked or spaced in the menu/messagebox
