# Debug mode
So I've found a bunch of debug menus which can trigger various scenarios,
like making everyone want to use the bathroom at the same time.
(Remember, this game is The Sims meets RPG, so it has some sort of AI per character)

The debug menus will be helpful with the translation project,
allowing translations to be verified without having to play through the game.

## The approach
The way the debug menus were found was by having a script that'd relaunch the PPSSPP emulator ~20K times with a save-state, and each time forcing a jump to a different piece of code as if it was a menu function. I think people refer to these as variants of corruptors?

Since it's almost impossible to tell where a function starts in disassembly code, the patterns looked for to reduce search space was stuff like, is it decrementing sp, or is it right after the delay-slot of a jr ra?

After the emulator is launched, be a 1.5-second delay to trigger an in-emulator screenshot. Most attempts would crash the emulator (and not save a screenshot), some would yield interesting results. The search took about two days.

## Search for master continues
Sadly I couldn't find a "master" debug menu that links to all these little menus.
Also I've toggled one-off features like slow-motion or player position information before,
and I've not seen those exposed anywhere in the debug menus uncovered so far.

And based on the pieces of text like this, I'm sure the master debug menu must exist in there still:

    0x001D1438: Data(DataType.String, 20, '● Battle Play Start\0', "●戦闘プレイ開始\0"),
    0x001D144C: Data(DataType.String, 20, '● Battle Demo Test\0', "●戦闘デモテスト\0"),
    0x001D1460: Data(DataType.String, 16, '● Adjusted Play\0', "●調整プレイ\0"),
    0x001D1470: Data(DataType.String, 16, '● Demo Check\0', "●デモチェック\0"),
    0x001D1480: Data(DataType.String, 20, '● Debug Switch\0', "●デバッグスイッチ\0"),
    0x001D1494: Data(DataType.String, 20, '● Game Flag Settings\0', "●ゲームフラグ設定\0"),
    0x001D14A8: Data(DataType.String, 24, '● Hideaki Anno Mode Settings\0', "●庵野監督モード設定\0"),
    0x001D14C0: Data(DataType.String, 24, '● Display Test Menu\0', "●表示テストメニュー\0"),
    0x001D14D8: Data(DataType.String, 28, '● Event Test Menu\0', "●イベントテストメニュー\0"),
    0x001D14F4: Data(DataType.String, 24, '● Screen Test Menu\0', "●画面テストメニュー\0"),
    0x001D150C: Data(DataType.String, 24, '● Misc. Test Menu\0', "●その他テストメニュー\0"),
    0x001D1524: Data(DataType.String, 20, '● Misato 1 Day Vacation\0', "●ミサト１日やすみ\0"),
    0x001D1538: Data(DataType.String, 16, '● Option\0', "●オプション\0"),
    0x001D1548: Data(DataType.String, 12, '● Test\0', "●テスト\0"),

I _think_ I've tried to trace a while back what pieces of code reference the above lines,
and I don't recall finding any matching liu/adds/oris. I'll give it another try.

The game tends to use lots of dynamic jumps, so it's difficult to know what the parent function of the debug menu functions might be, since it's not a clear-cut `jal` instruction.

## The debug menus

After enabling cheats in PPSSPP,
and adding the code to PPSSPP's cheats folder `PPSSPP_folder\PSP\Cheats\ULJS00064.ini`,
and enabling the cheat in PPSSPP's cheat menu (press `Esc`, right side-bar if cheats are enabled),
then press triangle to activate it in-game.

The first couple of debug menus have lots of other sub-menus,
so definitely worth exploring.

I suggest using these on a PSP emulator,
since the menu selections tend to crash,
or some menus can't be exited without a reset.

Also, the debug menus don't pause the game,
so if a character interrupts with a new message box,
it'll "freeze/burn-in" the menu.

Finally, lots of the battle-mode menus can't be brought up in battle-mode
since I haven't looked into a button hook for it, yet.

All these debug cheats override the triangle menu,
so press the triangle button to use them!

```
_C0 Debug menu: Dummy/Outside/bath (crashes)
_L 0x201C97CC 0x088B6320
```

![](https://i.imgur.com/5xmpN5N.jpg)

```
_C0 Debug menu: Priorities of something (no idea)
_L 0x201C97CC 0x088C295C
```

![](https://i.imgur.com/wNrPYtX.jpg)

```
_C0 Debug menu: IM/Door trigger-locations viewer (can't exit)
_L 0x201C97CC 0x088CB99C
```

![](https://i.imgur.com/VVrAgyq.jpg)

```
_C0 Debug menu: Shows IM by ranges; probably a select few for quickly executing
_L 0x201C97CC 0x088E6D28
```

![](https://i.imgur.com/s61zPyn.jpg)

```
_C0 Debug menu: IM Executor; select an IM and execute it
_L 0x201C97CC 0x088E71F0
```

![](https://i.imgur.com/WRZzciH.jpg)

If you set IM-0001 and Execute it, it will open up the following debug menu:
![](https://i.imgur.com/zPKT47d.jpg)

Or you can directly access the above menu via:
```
_C0 Debug menu: Impulse Debug Functions
_L 0x201C97CC 0x088ECD08
```

```
_C0 Debug menu: Daily Special Debug
_L 0x201C97CC 0x088984C0
```

![](https://i.imgur.com/By6iSje.jpg)

```
_C0 Debug menu: Some kind of Eva attack menu (Punch/Kick)
_L 0x201C97CC 0x0893A400
```

![](https://i.imgur.com/hkIiJfl.jpg)

```
_C0 Debug menu: Another kind of Eva attack menu (act/cmd)
_L 0x201C97CC 0x0894B81C
```

![](https://i.imgur.com/Ym6g89z.jpg)

```
_C0 Debug menu: Battle mode settings 1
_L 0x201C97CC 0x0895AFA0
```

![](https://i.imgur.com/TXOkAFE.jpg)

```
_C0 Debug menu: Battle mode settings 2
_L 0x201C97CC 0x089387B8
```

![](https://i.imgur.com/HFOHHkV.jpg)

```
_C0 Debug menu: Battle mode settings 3
_L 0x201C97CC 0x0895737C
```

![](https://i.imgur.com/V3ZSAfd.jpg)

```
_C0 Debug menu: Battle mode settings 4
_L 0x201C97CC 0x08910850
```

![](https://i.imgur.com/Yjbqrb1.jpg)

```
_C0 Debug menu: Some kind of btdemo/btldemo menu (they do nothing?)
_L 0x201C97CC 0x0893C958
```

![](https://i.imgur.com/wFyGhTS.jpg)

```
_C0 Debug menu: Window frame/Display Tests (Lots of Unimplemented errors)
_L 0x201C97CC 0x089107A8
```

![](https://i.imgur.com/twr5MXS.jpg)

```
_C0 Debug menu: Event Tests (Lots of Unimplemented errors)
_L 0x201C97CC 0x089107FC
```

![](https://i.imgur.com/AFzhI8y.jpg)

```
_C0 Debug menu: Impulse/Memory/Unit-Data (Lots of Unimplemented errors)
_L 0x201C97CC 0x089108A4
```

![](https://i.imgur.com/vOaGali.jpg)

```
_C0 Debug menu: Modify AT field values
_L 0x201C97CC 0x08910CE0
```

![](https://i.imgur.com/5sgDCAN.jpg)

```
_C0 Debug menu: Possibly camera controls (things just go pitch black/have no effect)
_L 0x201C97CC 0x08965C98
```

![](https://i.imgur.com/4lfXZzF.jpg)

```
_C0 Debug menu: Character expressions
_L 0x201C97CC 0x088E6A44
```

![](https://i.imgur.com/oU78OAB.jpg)
![](https://i.imgur.com/REpf8p7.jpg)

![](https://i.imgur.com/qkkjqFR.jpg)
![](https://i.imgur.com/mj2oCmF.jpg)

![](https://i.imgur.com/epIShIe.jpg)

## Misc. oddities discovered
```
_C0 Oddity: Directly trigger siren (crashes afterwards):
_L 0x201C97CC 0x0888EEA0
```

![](https://i.imgur.com/vKQAbCl.jpg)

```
_C0 Oddity: Sometimes crashes, sometimes makes a person leave the map
_L 0x201C97CC 0x0895DC64
```

In the top-right you'll notice Shinji has left
![](https://i.imgur.com/OfsuNDb.jpg)

```
_C0 Oddity: Invert the draw ordering
_L 0x201C97CC 0x0898E96C
```

This is a fun/trippy one:

![](https://i.imgur.com/DLwB2Ny.jpg)

```
_C0 Oddity: Set time to midnight
_L 0x201C97CC 0x08842CE0
```

![](https://i.imgur.com/MEFVYXl.jpg)

```
_C0 Oddity: Some kind of data transmission menu
_L 0x201C97CC 0x088851B0
```

![](https://i.imgur.com/Jb2Yoim.jpg)

```
_C0 Oddity: Some kind of Back/Redo/Next commands, unless this is used somewhere within the game?
_L 0x201C97CC 0x08840320
```

![](https://i.imgur.com/n8GqXMA.jpg)
