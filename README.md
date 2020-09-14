# Neon Genesis Evangelion 2: Another Cases (PSP)
# Reverse Engineering & Translation

## Foreword
The translation is still a work in progress, and the tools are aimed at developers/translators,
and are not the tools the final patch user will ever need to use or install.
In its final form, the patch will be one or two files and a one-step apply process.

![](https://i.imgur.com/jtsF9UV.gif)

## Contribution
WIP: Currently ironing out processes before opening up the contribution flood-gates.

## Quick Summary
I've deprecated all the patches in the ./patches/ folder and instead replaced them with the 
./translation/ folder that is a mix of human translation and machine translation. 
More on this later.

`./apply.sh` is a script that applies the WIP in translations to unpacked iso contents in the ./unpacked/ folder.

## Image Translation Status
- Images with text:
	- [x] Pick all the images with text that need to be translated
	- [ ] Write up the text translations of the contents in the images
	- [ ] Modify images, removing text, replacing it with the background
	- [ ] Modify images, injecting text with proper font

## Debug Mode:
![](https://i.imgur.com/YgnCVvG.png)

[Go to DEBUG_MODE.md for debug mode related discoveries](DEBUG_MODE.md)

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
