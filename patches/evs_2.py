#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

# Note:
# This file is a bit different to the section_*_translate files,
# in that the Japanese to be translated is BEFORE the ???.
# Put the translations in the ???
# \n is a linebreak
# \0 is the end of the string
# \' is a single quote
# If you see: ▽, carry it over to your translation
# %s are placeholders for text
# %d are placeholders for integer numbers
# %f are placeholders for floating point numbers, think 1.2, 3.5
# $a-z look to be game specific placeholders

translate_map = {
#
# ./USRDIR/event/bs001.har_EXTRACT/bs001.evs
#
# [Text Only - No Designated Speaker]
"家出していた$lは\n黒服たちに連れもどされた。\n\0":
'???',

#
# ./USRDIR/event/bs002.har_EXTRACT/bs002.evs
#
# [Text Only - No Designated Speaker]
"$lが退院しました。\n\0":
'???',

#
# ./USRDIR/event/bs003.har_EXTRACT/bs003.evs
#
# [Battle: Unit-01 Berserk]
#
# Shinji Ikari
"………う。▽\nもう、駄目だ…、僕は、\n僕は死ぬかもしれない…、僕は。▽\n死ぬかもしれない、死ぬかもしれ\nない、死ぬかもしれない、死ぬかも\nしれない、死ぬかもしれない…。\n\0":
'???',

# Shinji Ikari
"あっ、うわあああああああああー！！\n\0":
'???',

# Shinji Ikari
"機体が…、機体の損傷が激しくて\nもう…。\n僕は…、死んじゃうの…？▽\n嫌だ…、死ぬのは嫌だよ。\n嫌だ、嫌だ、嫌だ、嫌だ、嫌だ、\n嫌だ、嫌だ、嫌だ、嫌だ、嫌だ！！\n\0":
'???',

# Shinji Ikari
"…動け、お願いだよ、動いてよ！！\n頼むから動いてくれよ！！\n\0":
'Move, please, move it!\n I\'m begging you, move for me!!\n\0',

# Misato Katsuragi, Ritsuko Akagi, Female Staff
"初号機、エントリープラグ\n強制射出！！\n\0":
'Force eject Unit-01\'s entry plug!!\n\0',

# Kozo Fuyutsuki
"初号機のエントリープラグを\n強制射出しろ！！\n\0":
'Force eject Unit-01\'s entry plug!!\n\0',

# Maya Ibuki, Female Staff
"駄目です！\n信号を受付けません。\n\0":
'No good!\nThe signal\'s being rejected!\n\0',

# Misato Katsuragi 
"シンジ君っ！！\n\0":
'Shinji-kun!!\n\0',

# Ritsuko Akagi, Misato Katsuragi, Kaworu Nagisa
"シンジ君！！\n\0":
'Shinji-kun!!\n\0',

# Kozo Fuyutsuki
"もう一度、\nプラグを強制排除しろ！\n\0":
'Force eject the plug again!\n\0',

# Female Staff
"もう一度、\nプラグを強制排除して下さい！\n\0":
'Please force eject the plug again!\n\0',

# Maya Ibuki 
"そんな…！？\nエヴァ初号機、再起動！！▽\n初号機のシンクロ率が、\n急激に上昇していきます！\n\0":
'But that\'s--!?\nUnit-01 has reactivated!!▽\n Unit-01\'s synch ratio is climbing rapidly!\n\0',

# Female Staff
"これは…！？\nエヴァ初号機、再起動！！▽\n初号機のシンクロ率が、\n急激に上昇していきます！\n\0":
'This is--?!\nUnit-01 has reactivated!!▽\n Unit-01\'s synch ratio is climbing rapidly!\n\0',

# Ritsuko Akagi 
"どうなってるの？\n原因は？\n\0":
'What\'s going on?\nWhat\'s causing it?\n\0',

# Male Staff
"いったい、\n何が起こっているんだ！？\n\0":
'What on earth\n is happening?!\n\0',

# Maya Ibuki 
"わかりません！\n制御不能です！\n\0":
'We don\'t know!\nControl is impossible!\n\0',

# Female Staff
"シンクロ率、測定出来ません！\n制御不能です！\n\0":
'The synch ratio can\'t be measured!\nControl is impossible!\n\0',

# Ritsuko Akagi 
"…暴走！？\n\0":
'...It\'s berserk?!\n\0',

# Male Staff
"まさか…、暴走！？\n\0":
'It can\'t be... berserk?!\n\0',

# Maya Ibuki, Female Staff
"初号機、暴走！！\nパイロットからのコントロールも\n不可能です！\n\0":
'Unit-01 is berserk!!\n It can\'t be controlled by the pilot either!\n\0',

#
# ./USRDIR/event/bs004.har_EXTRACT/bs004.evs
#
# Shinji Ikari
"…怖いよ、…もう嫌だ。\n死んじゃうよ…。▽\n誰か、誰か助けてよ…、\n誰かぁぁぁぁぁぁぁぁぁぁぁ！！\n\0":
'???',

# Shinji Ikari
"駄目だ…、機体のダメージが\n大きくて動かない…。▽\n動かないよ…、動かない、\nこのままだとやられちゃうよ！！\n\0":
'It\'s no use... The unit\'s taken\n too much damage, it won\'t move...▽\n Won\'t move... It won\'t move...\n このままだとやられちゃうよ！！\n\0',

# Shinji Ikari
"そんな、予備電源が切れた！？▽\nもう動かないの？\nそんな、お願いだよ、動いてよ！！▽\n…みんなを、…僕を助けてよ！！\n\0":
'Oh no! The internal power ran out?!▽\n It won\'t move any more?\n No! Move, I beg you!▽\n To save everyone... To save me!!\n\0',

# Maya Ibuki, Female Staff
"エヴァ初号機、活動停止！！\n\0":
'Eva Unit-01 has ceased activity!!\n\0',

# Shinji Ikari
"……………………………！？\n\0":
'???',

# Maya Ibuki, Female Staff
"初号機、再起動！！▽\nまさか…、そんな。\nシンクロ率が４００パーセントを\n超えています！\n\0":
'Unit-01 has reactivated!!▽\n This is impossible...\n The synch ratio is exceeding 400 percent!\n\0',

# Ritsuko Akagi 
"やはり、…目覚めたのね。\n…彼女が。\n\0":
'So... she\'s awakened after all.\n\0',

# Male Staff
"何だって！？\nそんな…バカな。\n\0":
'???',

# Misato Katsuragi, Female Staff
"使徒を…食ってる？\n\0":
'It\'s eating the Angel?\n\0',

# Kozo Fuyutsuki
"Σ機関を取りこむ気か！\n\0":
'So it means to take in the S2 engine!\n\0',

# Maya Ibuki 
"うっ…………。\n\0":
'Hrk....\n\0',

# Kozo Fuyutsuki
"はじまったな。\n\0":
'So it\'s begun.\n\0',

# Gendo Ikari
"ああ、全ては、これからだ。\n\0":
'Yes. Everything starts here.\n\0',

# Kozo Fuyutsuki
"はじまったな…。\n全てはこれからだ。\n\0":
'So it\'s begun...\n Everything starts here.\n\0',

# Gendo Ikari
"はじまったな…。\n全ては、これからだ。\n\0":
'So it\'s begun...\n Everything starts here.\n\0',

#
# ./USRDIR/event/bs005.har_EXTRACT/bs005.evs
#
# [Battle: GeoFront Breach]
#
# Shigeru Aoba, Male Staff
"目標、ゼロエリアを突破！\nジオフロントに向かっています！\n\0":
'Target has breached Area Zero!\nIt\’s heading for the GeoFront!\n\0',

# Misato Katsuragi 
"エヴァは、リニアレールから\nジオフロントまで撤退！\n迎撃態勢を取って！\n\0":
'Withdraw the Evas into the\nGeoFront by linear rail!\nPrepare to intercept!\n\0',

# Kozo Fuyutsuki
"エヴァは、リニアレールから\nジオフロントまで撤退！\n迎撃態勢を取れ！\n\0":
'Withdraw the Evas into the\nGeoFront by linear rail!\nPrepare to intercept!\n\0',

# Female Staff
"エヴァは、リニアレールから\nジオフロントまで撤退、\n急いで迎撃にまわってください！\n\0":
'Please withdraw the Evas into the\nGeoFront by linear rail,\nand quickly turn to intercept!\n\0',

#
# ./USRDIR/event/bs006.har_EXTRACT/bs006.evs
# ./USRDIR/event/bs999.har_EXTRACT/bs999.evs (Partial)
#
# [Battle: Headquarters Breach]
#
# Shigeru Aoba, Male Staff
"目標、ネルフ本部に侵入。\nすぐに、ここまで来ます！\n\0":
'The target has penetrated Nerv H.Q.\n It\'ll be here any second!\n\0',

# Misato Katsuragi, Kozo Fuyutsuki
"総員、本部から撤退！！\n\0":
'???',

# Female Staff
"総員、本部より撤退して下さい！！\n\0":
'???',
 
# Maya Ibuki 
"…っ！\n来ました…。\nあああぁぁ！！\n\0":
'...!\nIt\'s here...\nAahhh!\n\0',

# Maya Ibuki 
"っ！　来ました…。\nあああぁぁ！！\n\0":
'???',

# Makoto Hyuga
"き、来ました…。\nうわぁぁぁぁあー！！\n\0":
'???',

# Shigeru Aoba
"あぁっ、き、来たぁぁ！\nわああああああああー！！\n\0":
'???',

# Male Staff
"わぁっ！！\nき、来ました…。\nうわぁぁぁぁぁあ！！\n\0":
'???',

#
# ./USRDIR/event/bs009.har_EXTRACT/bs009.evs
#
# [Text Only - No Designated Speaker]
"%1iボタンでコマンドが使える\nようになりました。\n\0":
'???',

#
# ./USRDIR/event/bs010.har_EXTRACT/bs010.evs
# ./USRDIR/btl/bevent.har_EXTRACT/ba019.evs
#
# Shinji Ikari
"どうしたんだ、\n動かない、動かないよ…。\n\0":
'???',

# Asuka Soryu Langley
"動かない…。\n動かないの、動いてくれないの！\n\0":
'???',

# Rei Ayanami 
"駄目…、動かない…。\n私には…、動かせない。\n\0":
'???',

# Toji Suzuhara 
"動かへん…。ああ、何でや…。\n何で動かへんのや…。\n\0":
'???',

# Toji Suzuhara 
"動かへん…。\nああ、何でや…。\n何で動かへんのや…。\n\0":
'???',

# Kaworu Nagisa 
"そんな、動かない…。\n僕に動かせないなんて…。なぜだ…！！\n\0":
'???',

# Kaworu Nagisa 
"そんな、動かない…。\n僕に動かせないなんて…。\nなぜだ…！！\n\0":
'???',

# Maya Ibuki, Female Staff
"パイロットのシンクロ率が低すぎます！\n…これではエヴァは稼動しません！\n\0":
'???',

# Maya Ibuki, Female Staff
"パイロットのシンクロ率が\n低すぎます！\n…これではエヴァは稼動しません！\n\0":
'???',

# Maya Ibuki, Female Staff
"パイロットのシンクロ率が\n低すぎます！▽\n…これでは、同時荷重攻撃は\n不可能です！\n\0":
'???',

# Misato Katsuragi 
"ここまで来て…、何てことなの！？\n\0":
'???',

# Kozo Fuyutsuki
"万事休すか…。\n\0":
'???',

# Female Staff
"そんな、作戦は失敗なの…。\n\0":
'???',

# Makoto Hyuga, Male Staff
"目標、移動を開始しました！\n\0":
'???',

#
# ./USRDIR/event/bs011.har_EXTRACT/bs011.evs
#
# Maya Ibuki, Female Staff
"エヴァ初号機の予備電源終了。\n\0":
'Eva Unit-01\'s backup power has terminated.\n\0',

# Shinji Ikari
"そんな…、もう…？\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ弐号機の予備電源終了。\n\0":
'Eva Unit-02\'s backup power has terminated.\n\0',

# Maya Ibuki, Female Staff
"エヴァ零号機の予備電源終了。\n\0":
'Eva Unit-00\'s backup power has terminated.\n\0',

# Maya Ibuki, Female Staff
"エヴァ参号機の予備電源終了。\n\0":
'Eva Unit-03\'s backup power has terminated.\n\0',

# Maya Ibuki, Female Staff
"エヴァ四号機の予備電源終了。\n\0":
'Eva Unit-04\'s backup power has terminated.\n\0',

# Maya Ibuki, Female Staff
"エヴァ両機の予備電源終了。\n\0":
'Both Evas\' backup power has terminated.\n\0',

#
# ./USRDIR/event/bs012.har_EXTRACT/bs012.evs
#
# Rei Ayanami 
"…っくぅぅぅぅぅ！\n\0":
'???',

#
# ./USRDIR/event/bs014.har_EXTRACT/bs014.evs
#
# [Battle: Positron Sniper Rifle]
#

# Maya Ibuki 
"エヴァ初号機、\nポジトロンスナイパーライフル\n発射！\n\0":
'???',

# Male Staff
"エヴァ初号機、\nポジトロンスナイパーライフルの\n発射に成功しました！\n\0":
'???',

# Maya Ibuki 
"エヴァ弐号機、\nポジトロンスナイパーライフル\n発射！\n\0":
'???',

# Male Staff
"エヴァ弐号機、\nポジトロンスナイパーライフルの\n発射に成功しました！\n\0":
'???',

# Maya Ibuki 
"エヴァ零号機、\nポジトロンスナイパーライフル\n発射！\n\0":
'???',

# Male Staff
"エヴァ零号機、\nポジトロンスナイパーライフルの\n発射に成功しました！\n\0":
'???',

# Maya Ibuki 
"エヴァ参号機、\nポジトロンスナイパーライフル\n発射！\n\0":
'???',

# Male Staff
"エヴァ参号機、\nポジトロンスナイパーライフルの\n発射に成功しました！\n\0":
'???',

# Maya Ibuki 
"エヴァ四号機、\nポジトロンスナイパーライフル\n発射！\n\0":
'???',

# Male Staff
"エヴァ四号機、\nポジトロンスナイパーライフルの\n発射に成功しました！\n\0":
'???',

# Misato Katsuragi 
"次！！\n再装填、急いで！\n\0":
'???',

# Kozo Fuyutsuki
"次だ！\n再装填を急げ！\n\0":
'???',

# Female Staff
"技術班、再装填急いで下さい！\n\0":
'???',

#
# ./USRDIR/event/bs016.har_EXTRACT/bs016.evs
#
# [Battle: Bardiel and Aftermath]
#
# Shinji Ikari
"ダメだ！\nやっぱりダメだよ、戦えないよ！\n\0":
'???',

# Gendo Ikari
"シンジ、なぜ戦わない？\n\0":
'???',

# Shinji Ikari
"だって…、\n人、人が乗ってるんだよ！\n父さん！\n\0":
'Because...\nthere\'s a person in there,\nFather!\n\0',

# Shinji Ikari
"だって、トウジが、\nトウジが乗ってるんだよ！\n父さん！\n\0":
'Because Toji...\n Toji\'s in there,\nFather!\n\0',

# Gendo Ikari
"構わん。\nそいつは使徒だ。\n我々の敵だ。\n\0":
'Irrelevant.\nIt\'s an Angel.\nOur enemy.\n\0',

# Shinji Ikari
"でも、でも、出来ないよ。\n助けなきゃ！\n人殺しなんて出来ないよ！\n\0":
'But, but I can\'t do it!\nI have to help them!\nI can\'t kill somebody!\n\0',

# Shinji Ikari
"トウジは、友達なんだ。\n僕の友達なんだ。\n戦えるわけないじゃないか！！\n\0":
'???',

# Gendo Ikari
"お前が死ぬぞ。\n\0":
'You will die.\n\0',

# Shinji Ikari
"いいよ。\n人を殺すよりはいいっ！！\n\0":
'That\'s okay.\nIt\'s better than killing someone!\n\0',

# Shinji Ikari
"いいよ。\nトウジを殺すくらいなら、\n僕が死んだほうがいい…！！\n\0":
'???',

# Gendo Ikari
"初号機とパイロットのシンクロを\n全面カット。▽\n回路をダミーシステムに\n切り替えろ。\n\0":
'???',

# Kozo Fuyutsuki
"碇、完成していたのか？\n\0":
'???',

# Gendo Ikari
"まだ試作段階だが、\n初号機には搭載してある。\n\0":
'???',

# Kozo Fuyutsuki
"しかし、委員会への報告も無しに\n使用するのはマズいぞ。\n\0":
'???',

# Gendo Ikari
"今が使う時だ。\n上には私から報告する。\n\0":
'???',

# Male Staff
"ダミーシステム？\n既に完成していたのか…。\n\0":
'???',

# Maya Ibuki 
"しかし、ダミーシステムには\nまだ問題が多く…。\n\0":
'???',

# Female Staff
"しかし、ダミーシステムには\nまだ色々な問題が…。\n\0":
'???',

# Gendo Ikari
"構わん。\n今のパイロットよりは役に立つ。\nやれ。\n\0":
'???',

# Maya Ibuki, Female Staff
"…はい。\nダミーシステム切り替え、準備開始！\n\0":
'???',

# Shinji Ikari
"…何？\n何をしたんだ、父さん！\n\0":
'...What?\nWhat have you done, Father?!\n\0',

# Maya Ibuki, Female Staff
"管制システム、切り替え終了。\n全神経、ダミーシステムへ直結完了。▽\n感情素子の３２．８パーセントが\n不鮮明。\nモニター出来ません。\n\0":
'???',

# Gendo Ikari
"構わん、システム開放。\n攻撃開始。\n\0":
'???',

#
# ./USRDIR/event/bs017.har_EXTRACT/bs017.evs
#
# [Battle: Bardiel Aftermath]
#
# Shigeru Aoba, Male Staff
"エヴァ参号機…いえ、\n目標は完全に沈黙しました。\n\0":
'Eva Unit-03-- I mean,\nthe target is completely silent.\n\0',

# Makoto Hyuga
"エントリープラグの解体班より連絡。\n生存者を確認！\n\0":
'???',

# Male Staff
"参号機パイロットは…、\n生存確認！\n生きてます！\n\0":
'Unit-03\'s pilot...\n Life signs confirmed!\nHe\'s alive!\n\0',

# Shinji Ikari,Toji's Mother, Kensuke Aida
"トウジ…。\n\0":
'Toji...\n\0',

# Shinji Ikari
"うわぁぁぁぁぁぁぁぁぁぁぁ！\n\0":
'???',

# Misato Katsuragi 
"シンジ君！\n\0":
'Shinji-kun!\n\0',

# Kozo Fuyutsuki
"初号機パイロットが…！\n\0":
'???',

# Shinji Ikari
"父さん！\n父さんはトウジを殺そうとしたんだ！▽\nこの僕の手で！\n\0":
'Father!\n He tried to kill Toji!▽\n With my own hands!\n\0',

# Misato Katsuragi 
"でも、シンジ君。\nああしなければ、\nあなたがやられていたわ！\n\0":
'???',

# Kozo Fuyutsuki
"聞け！\nああしなければ、\nキミがやられていたんだぞ！\n\0":
'???',

# Female Staff
"しかし、ああしなければ、\nシンジ君がやられていたんですよ！\n\0":
'???',

# Shinji Ikari
"そんなの関係ないよっ！！\n\0":
'???',

# Misato Katsuragi, Hikari Horaki, Shinji Ikari
"でも…。\n\0":
'???',

# Kozo Fuyutsuki, Makoto Hyuga
"だが、それも事実だ。\n\0":
'???',

# Female Staff
"しかし…。\n\0":
'???',

# Shinji Ikari
"そんなこと言って\nこれ以上、僕を怒らせないでよ。▽\n初号機の力があれば、\n本部を破壊する事だって出来るよ！\n\0":
'???',

# Shinji Ikari
"父さん、そこにいるんだろ？\n何か言えよっ！！\n答えてよ！！\n\0":
'???',

# Gendo Ikari
"ＬＣＬ圧縮濃度を限界まで上げろ。\n子供のダダに\n付き合っている暇はない。\n\0":
'???',

# Shinji Ikari
"…かはっ！？\n何をしたんだ…、\nちくしょう、ちくしょう…！！\n\0":
'???',

# Shinji Ikari
"………父さん。▽\n………トウジ…。\n\0":
'???',

#
# ./USRDIR/event/bs018.har_EXTRACT/bs018.evs
#
# [Battle: Eva Series Reactivation]
#

# Shigeru Aoba
"エヴァシリーズ、\n全機沈黙しました！\n\0":
'???',

# Male Staff
"エヴァシリーズ、\n全機破壊しました！\n\0":
'???',

# Misato Katsuragi, Female Staff
"やった！\n\0":
'???',

# Kozo Fuyutsuki
"やったか！\n\0":
'???',

# Maya Ibuki 
"何これ………………！？\n倒したはずのエヴァシリーズが！\n\0":
'???',

# Female Staff
"これは………………！？\n倒したはずのエヴァシリーズが…！\n\0":
'???',

# Maya Ibuki 
"エヴァシリーズ、活動再開…。\n\0":
'???',

# Female Staff
"エヴァシリーズ、全機、\n活動再開しました………。\n\0":
'???',

# Misato Katsuragi 
"そんな………。\nヤツらを倒す方法はないの！？\n\0":
'???',

# Kozo Fuyutsuki
"やはりそうか、\nΣ機関による力だな。\n\0":
'???',

# Female Staff
"そんな…、どうすれば………？\n\0":
'???',

# ./USRDIR/event/bs019.har_EXTRACT/bs019.evs
#
# Shinji Ikari, Misato Katsuragi 
"カヲル君！！\n\0":
'Kaworu-kun!!\n\0',

# Shinji Ikari
"待って、カヲル君！\n\0":
'Wait, Kaworu-kun!\n\0',

#
# ./USRDIR/event/bs020.har_EXTRACT/bs020.evs
#
# [Battle: Rei Self-Destructs]
#

# Misato Katsuragi 
"このままでは本部が…。\nせめて子供達だけでも…。\n\0":
'At this rate H.Q. is...\n But at least the children will...\n\0',

# Kozo Fuyutsuki
"こいつを道連れに、\n本部を自爆させるしかないのか…。\n\0":
'???',

# Female Staff
"使徒が…、\n使徒が本部にたどり着きました！\n\0":
'???',

# Rei Ayanami 
"碇君、\n…あなたは私が守るわ。\n\0":
'Ikari-kun,\n I will protect you.\n\0',

# Shinji Ikari
"綾波、何を…？\n何をするんだ！？\n\0":
'Ayanami, what are...?\n What are you doing?!\n\0',

# Rei Ayanami 
"私には代わりがいる…。\nでも、あなたの代わりはいない。\n\0":
'I can be replaced...\n But you cannot.\n\0',

# Asuka Soryu Langley
"アンタ、何いってんの？\nまさか！？\n\0":
'???',

# Rei Ayanami 
"鈴原君…、\nあなたは、私が守るわ。\n生きて…。\n\0":
'Suzuhara-kun...\nI will protect you.\nLive...\n\0',

# Toji Suzuhara 
"おい、綾波。\n馬鹿な事すんな！！\n綾波ーーーーーーー！！\n\0":
'Hey, Ayanami.\n Don\'t do something stupid!!\n Ayanamiiii!!\n\0',

# Rei Ayanami 
"渚君…、\nあなたは私が守る…。\nあなたを死なせはしない。\n\0":
'???',

# Kaworu Nagisa 
"ファースト、やめるんだ！！\n\0":
'First, don\'t do it!!\n\0',

# Rei Ayanami 
"…あなたは、私が守るわ。\n\0":
'... I will protect you.\n\0',

# Misato Katsuragi 
"レイ、死ぬ気！？\n\0":
'Rei, you mean to die!?\n\0',

# Rei Ayanami 
"碇司令…、私が守ります…。\n\0":
'Commander Ikari... I will protect you.\n\0',

# Gendo Ikari
"よせ、レイ！！\n\0":
'Stop, Rei!!\n\0',

# Rei Ayanami 
"副司令は、私が守ります…。\n\0":
'Deputy Commander, I will protect you...\n\0',

# Kozo Fuyutsuki
"レイ、何をするんだ！？\n自爆する気か！！\n\0":
'Rei, what are you doing?!\nYou\'re going to self-destruct?!\n\0',

# Rei Ayanami 
"…あなたは私が守るわ。\nこれしか…方法がないの…。\n\0":
'???',

# Maya Ibuki 
"レイ、何をするつもりなの！？\nこっちで何とかするわ、だから！！\n\0":
'???',

# Rei Ayanami 
"日向さん…、\n…あなたは、私が守るわ。\n\0":
'Hyuga-san...\n I will protect you.\n\0',

# Makoto Hyuga
"レイ、やめるんだ！！\n僕らに任せるんだ、だから！！\n\0":
'Rei, stop!!\n You can leave things to us!!\n\0',

# Rei Ayanami 
"青葉さん。\nあなたは、私が守るわ。\n\0":
'Aoba-san...\n I will protect you.\n\0',

# Shigeru Aoba
"レイ、どういう意味なんだ。\nレイッ！！\n\0":
'???',

# Rei Ayanami 
"赤木博士…、\nあなたは、私が守ります。\n\0":
'Dr. Akagi...\n I will protect you.\n\0',

# Ritsuko Akagi 
"レイ、自爆する気なの！？\n\0":
'Rei, you\'re going to self-destruct?!\n\0',

# Rei Ayanami 
"加持さん…、\nあなたは、私が守るわ。\n…絶対に。\n\0":
'Kaji-san...\n I will protect you.\n No matter what.\n\0',

# Rei Ayanami 
"相田君…、\nあなたは、私が守るわ。\n\0":
'???',

# Rei Ayanami 
"洞木さん…、\nあなたは、私が守るわ。\n\0":
'???',

# Rei Ayanami 
"鈴原君…、\nあなたは、私が守るわ。\n\0":
'???',

# Rei Ayanami 
"渚君…、\nあなたは、私が守るわ。\nみんなを…お願い。\n\0":
'???',

# Rei Ayanami 
"…さよなら。\n\0":
'... Farewell.\n\0',

# Rei Ayanami 
"………碇司令。▽\n………………。▽\nさよなら…。\n\0":
'???',

# Shinji Ikari
"綾波ぃーーーーーーー！\n\0":
'???',

# Asuka Soryu Langley, Kaworu Nagisa
"ファースト！\n\0":
'First!',

# Toji Suzuhara 
"綾波！？\n綾波ーーーーーーーーーー！！\n\0":
'???',

# Misato Katsuragi, Gendo Ikari, Kozo Fuyutsuki, Maya Ibuki 
"レイ！\n\0":
'Rei!\n\0',

# Makoto Hyuga
"レイ！\nくっそおおお…！！\n\0":
'Rei!\nDamn it...!!\n\0',

# Shigeru Aoba
"レイ！\n嘘だろぉ、レイッ！！\n\0":
'???',

# Ritsuko Akagi 
"レイ！\n…馬鹿よ、私なんかのために…。\n\0":
'???',

# Shigeru Aoba, Male Staff
"………………。▽\nスクリーン回復。\n目標、消失しました…。\n\0":
'............▽\nScreen restored.\nThe target has vanished...\n\0',

# Ritsuko Akagi 
"………レイ。▽\n………………………。▽\nレイ、待っているのよ…。\n\0":
'???',

#
# ./USRDIR/event/bs021.har_EXTRACT/bs021.evs
#
# [Battle: Israfel Killing Blow]
#
# Makoto Hyuga, Male Staff
"目標、再度、\n元の１体に戻ろうとしています！\n\0":
'???',

# Makoto Hyuga
"目標２体、融合！\n\0":
'Both targets have fused!\n\0',

# Male Staff
"目標、１体に戻りました！\n\0":
'The targets have reverted to a single body!\n\0',

# Shinji Ikari
"今だ、行くよ！\n\0":
'It\'s time, let\'s go!\n\0',

# Asuka Soryu Langley
"チャンスよ！！\n\0":
'It\'s our chance!\n\0',

# Rei Ayanami 
"使徒の融合をこちらからも確認。\n行きます！！\n\0":
'???',

# Toji Suzuhara 
"よっしゃ、\n一つになりよったでぇ！！\n\0":
'???',

# Kaworu Nagisa 
"よし、同時攻撃だ！\n\0":
'???',

# Shinji Ikari
"これでケリをつけるよ！！\n\0":
'???',

# Asuka Soryu Langley
"ＯＫ！\n\0":
'???',

# Rei Ayanami 
"行きましょう！！\n\0":
'Let\'s go!!\n\0',

# Toji Suzuhara 
"よっしゃあ！！\nキツイの一発お見舞いしたらぁ！！\n\0":
'???',

# Kaworu Nagisa 
"今だ、奴にとどめを！！\n\0":
'???',

#
# ./USRDIR/event/bs022.har_EXTRACT/bs022.evs
#
# Shigeru Aoba, Male Staff
"目標、移動開始しました！\n\0":
'???',

# Shigeru Aoba, Male Staff
"目標、再び形態変化。\n今度は、一本の紐状になりました。\n\0":
'???',

# Misato Katsuragi 
"目標の攻撃方法がわからないから、\nいきなり接近するのは危険よ。▽\n絶対に相手の攻撃範囲に\n入らないように！\n相手の後ろを取るのよ。▽\n接近戦は危険だから、\n絶対に避けて！！\n\0":
'???',

# Kozo Fuyutsuki
"相手の攻撃パターンが\nわからぬ以上、接近戦は危険だ。▽\n相手の攻撃を避けるため、\n後ろに回り込み、\n遠距離攻撃を仕掛けるんだ。\n\0":
'???',

# Makoto Hyuga
"使徒との接近戦は\n絶対に避けるんだ。▽\n目標の後方からの\n遠距離射撃を繰り返す。▽\nこれが今言える、\nもっとも安全な方法だ。\n\0":
'???',

# Female Staff
"目標の攻撃パターンが\n不明のままなので、\n接近戦を避けて下さい。▽\nそれから、こちらからは\n相手の攻撃範囲に入らぬよう、\n後方より遠距離射撃をして下さい。\n\0":
'???',

# Misato Katsuragi 
"使徒の加粒子砲には\n十分気をつけるのよ！\n\0":
'???',

# Kozo Fuyutsuki
"いいな、相手も撃ってくる事を\n忘れるな！！\n\0":
'???',

# Female Staff
"使徒の加粒子砲には\n気をつけて下さい！\n\0":
'???',

# Misato Katsuragi 
"あの機体には、まだあの子が…。\n\0":
'???',

# Kozo Fuyutsuki
"やむを得ん、倒す他なかろう…。\n\0":
'???',

# Female Staff
"中の子供は…、無事なの…？\n\0":
'???',

# Misato Katsuragi 
"トウジ君、トウジ君！！\n返事をして、トウジ君！！\n\0":
'???',

# Kozo Fuyutsuki, Misato Katsuragi, Male Staff, Gendo Ikari
"パイロットは？\n\0":
'Pilot\'s status?\n\0',

# Female Staff
"参号機パイロットは？\n\0":
'Status of Unit-03\'s pilot?\n\0',

# Makoto Hyuga, Maya Ibuki, Male Staff
"参号機パイロット、\n呼吸、心拍の反応はありますが\n恐らく…。\n\0":
'???',

# Misato Katsuragi 
"何とかして助けなきゃ…。\n\0":
'???',

# Kozo Fuyutsuki
"やむを得ん、\n使徒殲滅が先だ…。\n\0":
'???',

# Female Staff
"…作戦に移行しましょう。\n\0":
'???',

# Shigeru Aoba, Male Staff
"目標、セントラルドグマを降下中！▽\nターミナルドグマに\n向かっています！\n\0":
'???',

# Misato Katsuragi 
"シンジ君。\n早く、彼を止めて！\n\0":
'???',

# Kozo Fuyutsuki
"いかなる方法をもってしても、\n目標のターミナルドグマへの\n侵入を阻止しろ！！\n\0":
'???',

# Female Staff
"初号機パイロットは、\n目標を追撃して下さい！\n\0":
'???',

# Shigeru Aoba, Male Staff
"エヴァシリーズ、\n移動開始しました！\n\0":
'???',

# Misato Katsuragi 
"全部で９機か…。\nいい、必ず全機殲滅するのよ！\n\0":
'???',

# Kozo Fuyutsuki
"全部で９機、全機殲滅しろ！\nいいか、全機殲滅だ！！\n\0":
'???',

# Female Staff
"目標数９、全機殲滅して下さい！！\n\0":
'???',

#
# ./USRDIR/event/bs030.har_EXTRACT/bs030.evs
#
#
# Shinji Ikari
"わぁぁぁぁぁぁぁぁぁぁ！！\n\0":
'???',

# Makoto Hyuga, Male Staff
"エヴァ初号機、限界です。\nエントリープラグ、\n緊急射出します！\n\0":
'???',

# Shigeru Aoba, Male Staff
"回収班より連絡。\n初号機パイロットを発見、\n無事回収しました！\n\0":
'???',

# Asuka Soryu Langley
"うああああああああああ…！！\n\0":
'???',

# Makoto Hyuga, Male Staff
"エヴァ弐号機、限界です。\nエントリープラグ、\n緊急射出します！\n\0":
'???',

# Shigeru Aoba, Male Staff
"回収班より連絡。\n弐号機パイロットを発見、\n無事回収しました！\n\0":
'???',

# Rei Ayanami 
"きゃああああああっ！！！\n\0":
'???',

# Makoto Hyuga, Male Staff
"エヴァ零号機、限界です。\nエントリープラグ、\n緊急射出します！\n\0":
'???',

# Shigeru Aoba, Male Staff
"回収班より連絡。\n零号機パイロットを発見、\n無事回収しました！\n\0":
'???',

# Toji Suzuhara 
"うわぁぁぁぁぁぁぁぁ！\n\0":
'???',

# Makoto Hyuga, Male Staff
"エヴァ参号機、限界です。\nエントリープラグ、\n緊急射出します！\n\0":
'???',

# Shigeru Aoba, Male Staff
"回収班より連絡。\n参号機パイロットを発見、\n無事回収しました！\n\0":
'???',

# Kaworu Nagisa 
"そんな…バカな………………。\n\0":
'???',

# Makoto Hyuga, Male Staff
"エヴァ四号機、限界です。\nエントリープラグ、\n緊急射出します！\n\0":
'???',

# Shigeru Aoba, Male Staff
"回収班より連絡。\n四号機パイロットを発見、\n無事回収しました！\n\0":
'???',

# Makoto Hyuga, Male Staff
"エヴァ両機、活動限界です。\n\0":
'???',

# Kozo Fuyutsuki, Shigeru Aoba
"万策尽きたか…。\n\0":
'???',

#
# ./USRDIR/event/bs031.har_EXTRACT/bs031.evs
#
# [Battle: Angel Down]
#
# Makoto Hyuga, Male Staff
# [NOTE] $e fills in Angel's name.
"第$d使徒、$e。\n殲滅を確認しました！\n\0":
'Destruction of $d Angel, $e,\nconfirmed!\n\0',

#
# ./USRDIR/event/bs032.har_EXTRACT/bs032.evs
#
# [Battle: Eva Series Down]
#
# Makoto Hyuga, Male Staff
"エヴァシリーズ、１機撃破！\n\0":
'First Eva Series unit down!\n\0',

# Makoto Hyuga, Male Staff
"２機目撃破！\n\0":
'Second unit down!\n\0',

# Makoto Hyuga, Male Staff
"３機目撃破！\n\0":
'Third unit down!\n\0',

# Makoto Hyuga, Male Staff
"４機目撃破！\n\0":
'Fourth unit down!\n\0',

# Makoto Hyuga, Male Staff
"５機目撃破！\n\0":
'Fifth unit down!\n\0',

# Shigeru Aoba
"気味の悪い奴等だ。\nまた活動を再開してきたら、\nどうする…。\n\0":
'???',

# Male Staff
"まさか、\nまた活動を再開したら…。\n\0":
'???',

# Makoto Hyuga, Male Staff
"６機目撃破！\n\0":
'Sixth unit down!\n\0',

# Makoto Hyuga, Male Staff
"７機目撃破！\n\0":
'Seventh unit down!\n\0',

# Makoto Hyuga, Male Staff
"８機目撃破！\nあと１機！\n\0":
'Eighth unit down!\n\0',

#
# ./USRDIR/event/bs039.har_EXTRACT/bs039.evs
#
# [Battle: Tabris Battle Aftermath]
#
# Makoto Hyuga, Male Staff
"エヴァ初号機、沈黙しました。\n\0":
'Eva Unit-01 is silent.\n\0',

# Misato Katsuragi, Kozo Fuyutsuki, Gendo Ikari, Maya Ibuki, Female Staff, Toji Suzuhara, Ritsuko Akagi, Makoto Hyuga, Shigeru Aoba, Shinji Ikari,[Text Only - No Designated Speaker], Asuka Soryu Langley, Kaworu Nagisa
"………………………。\n\0":
'???',

# Shinji Ikari
"…カヲル…君。\n\0":
'...Kaworu-kun.\n\0',

#
# ./USRDIR/event/bs042.har_EXTRACT/bs042.evs
#
# Misato Katsuragi 
"初号機の神経接続カット！\n急いで！\n\0":
'???',

# Maya Ibuki, Female Staff
"初号機の神経接続、解除！\n再接続するまでの間は、\n初号機は操作不能になります。\n\0":
'???',

# Misato Katsuragi 
"弐号機の神経接続カット！\n急いで！\n\0":
'???',

# Maya Ibuki, Female Staff
"弐号機の神経接続、解除！\n再接続するまでの間は、\n弐号機は操作不能になります。\n\0":
'???',

# Misato Katsuragi 
"零号機の神経接続カット！\n急いで！\n\0":
'???',

# Maya Ibuki, Female Staff
"零号機の神経接続、解除！\n再接続するまでの間は、\n零号機は操作不能になります。\n\0":
'???',

# Misato Katsuragi 
"参号機の神経接続カット！\n急いで！\n\0":
'???',

# Maya Ibuki, Female Staff
"参号機の神経接続、解除！\n再接続するまでの間は、\n参号機は操作不能になります。\n\0":
'???',

# Misato Katsuragi 
"四号機の神経接続カット！\n急いで！\n\0":
'???',

# Maya Ibuki, Female Staff
"四号機の神経接続、解除！\n再接続するまでの間は、\n四号機は操作不能になります。\n\0":
'???',

# Misato Katsuragi 
"エヴァ両機の神経接続カット！\n急いで！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ両機の神経接続、解除！\n再接続するまでの間は、\nエヴァ両機は操作不能になります。\n\0":
'???',

#
# ./USRDIR/event/bs043.har_EXTRACT/bs043.evs
#
# [Text Only - No Designated Speaker]
"今回の作戦では、$lは\n待機になります。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ミサトからパイロットへ\n作戦が伝達されました。\n\0":
'???',

# [Text Only - No Designated Speaker]
"冬月からパイロットへ\n作戦が伝達されました。\n\0":
'???',

# [Text Only - No Designated Speaker]
"パイロットへ\n作戦が伝達されました。\n\0":
'???',

#
# ./USRDIR/event/bs044.har_EXTRACT/bs044.evs
#
# [Text Only - No Designated Speaker]
"エヴァ初号機は使徒を捕食し、\nΣ機関を取りこみました。▽\n内蔵電源が無限になり、\nアンビリカルケーブル無しでの\n稼動が可能になります。\n\0":
'Eva Unit-01 preyed upon an Angel\nand absorbed its S2 engine.▽\nThe Eva\'s internal power supply is now infinite,\nallowing it to operate with an umbilical cable.\n\0',

#
# ./USRDIR/event/bs058.har_EXTRACT/bs058.evs
#
# Misato Katsuragi 
"シンジ君、聞こえるわね？▽\n早速だけど、あなたには\nこのエヴァンゲリオンで人類の敵、\n使徒と戦ってもらいます。\n\0":
'???',

# Shinji Ikari
"…で、でも。\nどうすればいいんですか？\n\0":
'???',

# Misato Katsuragi 
"ではまず、\nエヴァの操縦方法について\n説明します。▽\nあなたの手元に、\n「アナログパッド」があるでしょ？▽\n操縦は、その「アナログパッド」を\n動かしたい方向へ動かせばいいの。\nやってみて。\n\0":
'???',

#
# ./USRDIR/event/bs059.har_EXTRACT/bs059.evs
#
# Shinji Ikari, Shigeru Aoba, Female Staff
"は、はい！\n\0":
'???',

# Misato Katsuragi 
"すごいわ、シンジ君。\nいいわよ、その調子！\n\0":
'???',

# Misato Katsuragi 
"エヴァは旋回に多少時間が\nかかるけど、我慢して。\nすぐ慣れるわ。\n\0":
'???',

# Shinji Ikari
"あっ、…は、はい。\n何とか…なりそうです。\n\0":
'???',

# Makoto Hyuga
"使徒、初号機の迎撃開始ラインを\n通過しました！\n\0":
'???',

# Misato Katsuragi 
"来たわね、じゃあ次は\n接敵の仕方を説明するわ。▽\n使徒と戦うには、まず使徒と\n接触する必要があります。▽\n私が指示を出して誘導するから、\nそれに従って移動して。\n\0":
'???',

# Misato Katsuragi 
"移動指示はＡ−１、Ｂ−２など\nエリア名で指示を出します。▽\nあなたは、その指示された\nエリアに向かって移動して！\n\0":
'???',

# Shinji Ikari
"でも、エリア名なんて言われても…\n僕、どこかわかりませんよ…。\n\0":
'???',

# Misato Katsuragi 
"エリア名は%1iボタンを押して\n「全域マップを確認する」で\n確認出来るわ。▽\nやってみて！\n\0":
'???',

# ./USRDIR/event/bs060.har_EXTRACT/bs060.evs
# ./USRDIR/event/bs999.har_EXTRACT/bs999.evs (Partial)
#
# Misato Katsuragi 
"シンジ君、\nエヴァの後ろに付いている\nケーブルがあるでしょう？\n\0":
'???',

# Shinji Ikari
"ええ、これは…？\n\0":
'???',

# Misato Katsuragi 
"それはアンビリカルケーブルって\n言って、エヴァの電力供給源なの。\n\0":
'???',

# Shinji Ikari
"エヴァって…、\n電気で動いてるんですか？\n\0":
'???',

# Misato Katsuragi 
"そうよ。▽\nこの第３新東京市の所々に\n設置されている「電源ビル」から\n電力を供給して動いているの。▽\nだから、エヴァはこのケーブルが\n届く範囲までしか、活動出来ないの。\n\0":
'???',

# Misato Katsuragi 
"エヴァは、この第３新東京市の\n所々に設置されている「電源ビル」\nから電力を供給して動いているの。▽\nだから、エヴァは\nこのケーブルが届く範囲までしか、\n活動出来ないの。\n\0":
'???',

# Shinji Ikari
"でも、こんな広い街…。\n使徒が遠くに現れたら\nどうするんですか？\n\0":
'???',

# Misato Katsuragi 
"その時のために、この\n第３新東京市には、「電源ビル」が\n沢山設置されているの。\n\0":
'???',

# Misato Katsuragi 
"各所の電源ビルにケーブルを\n繋ぎかえながら移動すれば、\n移動距離を延ばせるわ。\n\0":
'???',

# Shinji Ikari
"手間がかかるんですね。\n\0":
'???',

# Misato Katsuragi 
"仕方ないわ。\nこれが、今の科学力の限界よ。\n\0":
'???',

# Misato Katsuragi 
"アンビリカルケーブルを他のビルに\n繋ぎ直す時は、その電源ビルの\n側に立って%1iボタン。▽\n「アンビリカルケーブル接続」の\nコマンドを選べばいいわ。▽\n重要な事だから、忘れないようにね。\n\0":
'???',

# Misato Katsuragi 
"アンビリカルケーブルを\n他のビルに繋ぎ直す時は、\nその電源ビルの側に立って%1iボタン。▽\n「アンビリカルケーブル接続」の\nコマンドを選べばいいわ。▽\n重要な事だから、忘れないようにね。\n\0":
'???',

#
# ./USRDIR/event/bs061.har_EXTRACT/bs061.evs
#
# Maya Ibuki 
"エヴァ初号機。\nアンビリカルケーブル、\n残りわずかです。\n\0":
'???',

# Misato Katsuragi 
"シンジ君、エヴァは基本的に\nケーブルの範囲内でしか\n活動できないの。▽\nでも、予備電源を使えば\nケーブル無しでも活動できるわ。\n\0":
'???',

# Shinji Ikari
"そ、そうなんですか。\n\0":
'???',

# Misato Katsuragi 
"ただし、予備電源で活動出来る\n時間はわずかなうえ、電源が\n切れたら、活動停止になるのよ。\n\0":
'???',

# Shinji Ikari
"活動停止？\nそれって、\n動けなくなるって事ですか？\n\0":
'???',

# Misato Katsuragi 
"そう。\nだから、本当にイザという時にしか\n使えないの。▽\nもし、ケーブルの残りが\n無くなったら、…その時の判断は\nあなたに任せるわ。\n\0":
'???',

# Shinji Ikari, Shigeru Aoba, Makoto Hyuga
"…わかりました。\n\0":
'...Understood.\n\0',

#
# ./USRDIR/event/bs062.har_EXTRACT/bs062.evs
#
# Shinji Ikari
"み、見えてきました！！▽\nあれが敵…。\n僕たち人類の敵…、使徒…。\n\0":
'It\'s coming into view!!▽\nThat\'s the enemy...\nThe enemy of us humans... The Angels.\n\0',

# Misato Katsuragi 
"落ち着いて。\nでは、これより使徒に対して\n接近戦を行います。\n\0":
'???',

# Shinji Ikari
"はっ、はい！\n\0":
'???',

# Misato Katsuragi 
"接近戦は、エヴァ周囲の射程に\n使徒を入れ、%1iボタン。▽\nちゃんと射程内に入っていれば、\n攻撃コマンドが選べるわ。▽\nそれから、\n目標を捕らえる位置によって、\n選べる攻撃が変わるから注意して。\n\0":
'???',

# Shinji Ikari
"射程に入れて、%1iボタン…。\n射程に入れて、%1iボタン…。\n射程に入れて、%1iボタン…。\n\0":
'???',

#
# ./USRDIR/event/bs063.har_EXTRACT/bs063.evs
#
# Shinji Ikari
"…あ、当たった！\n\0":
'???',

# Misato Katsuragi 
"スゴイわ、シンジ君。\nその調子！\n\0":
'???',

#
# ./USRDIR/event/bs065.har_EXTRACT/bs065.evs
#
# Misato Katsuragi 
"じゃ、まずは勝利条件と\n敗北条件の説明からね。\n全域マップ、出して！\n\0":
'???',

# Misato Katsuragi 
"使徒は強力な妨害電波を放っていて、\n常に正確な位置を特定することは\nできないの。\n\0":
'???',

# Misato Katsuragi 
"そう、ボヤボヤしてたら\nあっという間に使徒は\nゼロエリアに到達してしまうわ。▽\nだから私達は使徒の移動先を\n予想して、先回りする必要があるの。\n\0":
'???',

# Misato Katsuragi 
"こっちのマップを見て。\n\0":
'???',

# Misato Katsuragi 
"このミニマップに、\n使徒の予想侵攻ルートが\n表示されるわ。\n\0":
'???',

# Misato Katsuragi 
"さっきから気になっているでしょう\nけど、台風の移動予報円みたいなの\nが使徒の予想侵攻ルートよ。▽\nこれを頼りに、使徒を肉眼で\n捕捉できるであろうポイントまで\n私が移動指示を出すわ。\n\0":
'???',

# Misato Katsuragi 
"まっ、難しいけど安心して。\nこう見えても私、\nカンはいい方だから。\n\0":
'???',

# Shinji Ikari, Misato Katsuragi 
"はい！\n\0":
'???',

#
# ./USRDIR/event/bs064.har_EXTRACT/bs064.evs
#
# Shinji Ikari
"いっ、痛い…！？\n…くっ、うわぁぁぁぁ！！\nああああぁぁぁぁぁぁぁぁぁ！！\n\0":
'???',

# Misato Katsuragi 
"シンジ君、それは幻痛よ！！\n初号機の耐久力はまだあるわ、\n落ち着いて！\n\0":
'???',

# Shinji Ikari
"………………………………。▽\n射程に入れて、%1iボタン…。\n射程に入れて、%1iボタン…。\n射程に入れて、%1iボタン…。\n\0":
'???',

#
# ./USRDIR/event/bs065.har_EXTRACT/bs065.evs
#
# Misato Katsuragi 
"じゃ、まずは勝利条件と\n敗北条件の復習からね。\n全域マップ、出して！\n\0":
'???',

# Shigeru Aoba
"了解。\n全域マップ、出ます。\n\0":
'???',

# Misato Katsuragi 
"これが、あなたが乗っている\nエヴァ初号機。\n\0":
'???',

# Misato Katsuragi 
"そして………、\n\0":
'???',

# Misato Katsuragi 
"これが使徒。\n\0":
'This is an Angel.\n\0',

# Misato Katsuragi 
"ここまではいいわね。\n\0":
'???',

# Misato Katsuragi 
"じゃあ、次は使徒の行動目的を\n説明します。▽\n使徒はこの第３新東京市の\n最終防衛ラインである…、\n\0":
'???',

# Misato Katsuragi 
"ここゼロエリアを目指して\n侵攻します。▽\nそして、\nこのゼロエリアの地下にあるのが…、\n\0":
'???',

# Misato Katsuragi 
"我々の拠点、ネルフ本部。▽\nつまり、ゼロエリアを突破され、\nここネルフ本部を落とされると、\nジ・エンド。▽\nこれが敗北条件ってわけね。\nあ、もちろん、あなたのエヴァが\nやられても終わりよ。\n\0":
'???',

# Shinji Ikari
"………はい。\n\0":
'???',

# Misato Katsuragi 
"じゃあ、次に使徒の行動を\n見てみましょう。▽\n説明しやすくするために、\n時間を速めて見せるわね。▽\n使徒の行動シミュレーションを\n走らせて！\n\0":
'???',

# Shigeru Aoba
"使徒行動シミュレーション、\nスタートします。\n\0":
'???',

# Shinji Ikari
"あれっ？▽\n使徒の位置、\nたまにしか映りませんよ。\nどうなってるんですか？\n\0":
'???',

# Shinji Ikari
"それって、使徒と接触するの\n難しくないですか？\n\0":
'???',

# Shinji Ikari
"はぁ………。\n\0":
'???',

# Misato Katsuragi 
"そして、使徒と接触したら\nあなたがエヴァで戦い…、▽\n殲滅すれば、勝利条件達成ってワケ。\nわかった？\n\0":
'???',

# Misato Katsuragi 
"じゃあ、説明ばかりじゃ\n退屈だろうから、\n実践訓練に移りましょうか。\n\0":
'???',

# Misato Katsuragi 
"じゃ、使徒がエヴァ初号機の\n迎撃開始ラインに入る直前から\n始めるわ。\n\0":
'???',

# Shinji Ikari
"迎撃開始ライン？\n\0":
'???',

# Misato Katsuragi 
"あなたの守備範囲みたいなものよ。▽\nそのラインに使徒が侵入したら、\n私が移動指示を出し始めるわ。\nいい？\n\0":
'???',

#
# ./USRDIR/event/bs066.har_EXTRACT/bs066.evs
#
# Shigeru Aoba
"使徒、エヴァ初号機の迎撃開始\nラインに侵入しました！\n\0":
'???',

# Misato Katsuragi 
"んじゃ、「全域マップ」の\n起動方法を説明しとくわ。\n\0":
'???',

# Misato Katsuragi 
"さっきも言ったけど、使徒の位置は\n正確には把握出来ないの。▽\nだから、私の移動指示も\n必ず正しいってわけじゃないのよ。\n\0":
'???',

# Shinji Ikari
"…えぇっ、そうなんですか？\n安心してたのに…。\n\0":
'???',

# Misato Katsuragi 
"だからイザと言う時は、\nあなた自身が使徒の動きを\n読んで判断し、自分で行動して。\n\0":
'???',

# Shinji Ikari
"…はい、…大丈夫かな。\n\0":
'???',

# Misato Katsuragi 
"起動方法は、%1iボタンを押して。▽\nコマンドを呼び出したら\n「全域マップを確認する」を\n選択すれば、起動出来るわ。▽\nわかった？\n\0":
'???',

# Misato Katsuragi 
"よし！\nじゃ、シミュレーションを\n続行するわよ。\n\0":
'???',

#
# ./USRDIR/event/bs067.har_EXTRACT/bs067.evs
#
# Misato Katsuragi 
"シンジ君、\nアンビリカルケーブルの役割は\nちゃんと覚えてる？\n\0":
'???',

# Shinji Ikari
"えっと、エヴァを動かす電源の\n供給ケーブル。▽\nケーブルの長さは有限で、\nその範囲外に移動するには\n他の電源ビルへの繋ぎ変えが必要。▽\n…でした…よね？\n\0":
'???',

# Misato Katsuragi 
"ＯＫ、ＯＫ！\nちゃんと覚えてるわね。▽\nイザという時はケーブルを切断し、\n予備電源のみでの活動も可能。\n\0":
'???',

# Misato Katsuragi 
"ただし、予備電源は少なく、\n切れたら活動停止で、一巻の終わり。▽\n緊急手段として、これもちゃんと\n覚えておいてネ。\n\0":
'???',

# Misato Katsuragi 
"じゃ、引き続き移動指示を行うわよ。\n\0":
'???',

#
# ./USRDIR/event/bs068.har_EXTRACT/bs068.evs
#
# Shinji Ikari
"あの…、\n使徒、発見しました！\n\0":
'???',

# Misato Katsuragi 
"よし、ちゃんと接触出来たわね。▽\nじゃあ、次は接近戦だけど、\nその前に使徒の耐久力の説明を\nしておくわ。\n\0":
'???',

# Misato Katsuragi 
"使徒の耐久力ってのは、\n使徒がダメージに耐えられる力を\n表すもので、▽\nこれを全部削り取れば、\n使徒を殲滅する事が出来るの。\nここまではわかるわね？\n\0":
'???',

# Shinji Ikari
"はい。\nでも、この色が分かれてるのは？\n\0":
'???',

# Misato Katsuragi 
"右側の赤色の領域が、\nΑΤフィールド。\n\0":
'???',

# Shinji Ikari
"ΑΤフィールド？\n\0":
'???',

# Misato Katsuragi 
"まぁ、使徒の防壁みたいなもんね。\n使徒に攻撃を与えた場合、\n右端から減っていくんだけど、▽\nこのΑΤフィールドを\n超えられなければ、\n全くダメージは与えられないの。\n\0":
'???',

# Shinji Ikari
"防壁で阻止されるわけですね。\n\0":
'???',

# Misato Katsuragi 
"そ。\nで、左側の黄色の領域が、耐久力。▽\nΑΤフィールドを超え、ここまで\n到達する威力の攻撃を当てて\n初めてダメージになるの。\n\0":
'???',

# Shinji Ikari
"真中の緑は…、何ですか？\n\0":
'???',

# Misato Katsuragi 
"緑色の領域は、ヘイフリックよ。\n\0":
'???',

# Shinji Ikari
"ヘイフリック？\n\0":
'???',

# Misato Katsuragi 
"ヘイフリックとは、自己修復が\n可能な領域を表しているもので、▽\nこの領域までのダメージは、\nしばらくすると回復しちゃうの。\n\0":
'???',

# Shinji Ikari
"つまり、耐久力を減らすには、\nΑΤフィールドとヘイフリック領域▽\n２つの壁を突破しないと\nいけないわけですね。\n\0":
'???',

# Misato Katsuragi 
"その通りよ。\nそして、エヴァの耐久力も内容は\n全く同じだから、覚えておいてね。▽\nじゃ、次は使徒に接近して！\n\0":
'???',

#
# ./USRDIR/event/bs069.har_EXTRACT/bs069.evs
#
# Shinji Ikari
"あ…、当たった…！\n\0":
'???',

# Misato Katsuragi 
"上手いじゃない、シンジ君。\n\0":
'???',

#
# ./USRDIR/event/bs070.har_EXTRACT/bs070.evs
#
# Shinji Ikari
"こちら、初号機。\n目標を肉眼で発見しました！\n\0":
'???',

# Misato Katsuragi 
"よし、ちゃんと接触出来たわね。▽\nもし、射撃武器を使うときは\n弾数制限があるから注意して。\nいいわね？\n\0":
'???',

# Shinji Ikari, Rei Ayanami, Misato Katsuragi, Shigeru Aoba, Ritsuko Akagi, Makoto Hyuga, Female Staff
"はい。\n\0":
'???',

#
# ./USRDIR/event/bs071.har_EXTRACT/bs071.evs
#
# Shinji Ikari
"ミサトさん、今の…、\n中和ってなんですか？\n\0":
'???',

# Misato Katsuragi 
"エヴァが使徒に接近すると、\n互いのΑΤフィールドが中和され、\nΑΤフィールドが低下するの。\n\0":
'???',

# Shinji Ikari
"互いのって事は………、\nエヴァのΑΤフィールドも！？\n\0":
'???',

# Misato Katsuragi 
"そう、使徒とエヴァ両方の\nΑΤフィールドが低下する、▽\nつまり接近戦は、互いの防壁を\n捨てて戦う、ノーガードでの\n殴り合いみたいなものよ。\n\0":
'???',

# Shinji Ikari
"…こちらのダメージも\n大きいって事ですよね。\n\0":
'???',

# Misato Katsuragi 
"でも、ΑΤフィールドを\n中和しないと、使徒にはあまり\nダメージを与えられないの。▽\nだからΑΤフィールドを中和して、\n接近戦というパターンが\n戦闘のセオリーになるわ。\n\0":
'???',

# Shinji Ikari
"簡単に…言いますね。\n\0":
'???',

# Misato Katsuragi 
"基本的な事よ。\nじゃ、接近戦に移行して。\n\0":
'???',

#
# ./USRDIR/event/bs072.har_EXTRACT/bs072.evs
#
# Misato Katsuragi 
"いいわ。その調子よ。\n\0":
'???',

# Misato Katsuragi 
"攻撃を行うと、しばらくの間\n次の攻撃が行えなくなるから\n気をつけて。▽\nこの攻撃できない間を\nチャージ時間というの。\n\0":
'???',

# Misato Katsuragi 
"このチャージゲージが最大まで\n回復すれば、次の攻撃が行えるわ。▽\nちなみに、チャージが完了しないと\n攻撃できないのは、使徒の場合も\n全く同じよ。わかった？\n\0":
'???',

# Shinji Ikari
"はい、わかりました。\n\0":
'???',

# Misato Katsuragi 
"じゃあ、今まで説明した事を\nしっかり頭に入れて\n使徒を倒してちょうだい。▽\n使徒を倒すことができたら\n今日の訓練は終わりよ。\n頑張ってね！\n\0":
'???',

#
# ./USRDIR/event/bs073.har_EXTRACT/bs073.evs
#
# Shinji Ikari
"やった、倒した！！▽\nミサトさん、倒しましたよ！！\n\0":
'???',

# Misato Katsuragi 
"上出来ィ！！\n予想以上の腕前だわ！！▽\nお疲れさま、\n今日の訓練は終わりよ。▽\n今日はゆっくり休んでちょうだい。\n\0":
'???',

# Misato Katsuragi 
"今日教えた事、\n絶対忘れちゃダメよ。\n\0":
'???',

#
# ./USRDIR/event/bs074.har_EXTRACT/bs074.evs
#
# Misato Katsuragi 
"あっちゃあ〜、\nやっぱ難しかったかしら…。\n\0":
'???',

# Shinji Ikari
"すみません…。\n\0":
'???',

# Misato Katsuragi 
"じゃ、気を取り直して\n復習ついでに、もう一回最初から\nやってみましょうか。\n\0":
'???',

# (Decision Prompt)
"もう一度説明から／もう一度実践から／今日はもうやめておく\0":
'???',

# Shinji Ikari
"はい、やります！\n\0":
'???',

# Misato Katsuragi 
"ＯＫ！\nとことん付き合ってあげるわよ。\n\0":
'???',

# Shinji Ikari
"いえ、\n今日はもう、やめておきます。\n\0":
'???',

# Misato Katsuragi 
"まあ、先日の戦闘といい、\n急な事だらけで疲れているのかもね。\n\0":
'???',

# Shinji Ikari, Toji Suzuhara, Gendo Ikari, Rei Ayanami, Female Staff, Asuka Soryu Langley, Kaworu Nagisa, Hikari Horaki, Ritsuko Akagi, Misato Katsuragi, Kozo Fuyutsuki, Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Ryoji Kaji
"…。\n\0":
'???',

# Misato Katsuragi 
"わかったわ、\nちょっと無理させてごめんなさい。\n今日の訓練は終わりにしましょう。▽\n今日教えた事は忘れないように\nしっかり覚えといてね。\n\0":
'???',

#
# ./USRDIR/event/bs075.har_EXTRACT/bs075.evs
#
# Shigeru Aoba
"使徒、ゼロエリアを突破しました！\n\0":
'???',

# Shinji Ikari
"しまった！\n\0":
'Oh no!\n\0',

# Misato Katsuragi 
"はい、アウト。▽\nゼロエリアに踏み込まれる前に\n倒さないと、街の被害も大きく\nなるのよ。▽\nどう、\nもう１回、最初からやりなおす？\n\0":
'???',

# Shinji Ikari
"…はい、もう一度。\n\0":
'???',

# Misato Katsuragi 
"じゃ、もう一度最初からよ。\n今度こそ頑張ってね！！\n\0":
'???',

# Shinji Ikari
"いえ、\nもう、…いいです。\n\0":
'???',

# Misato Katsuragi 
"でも、実戦じゃ失敗は\n許されないのよ。\nそれは忘れないでいてちょうだい。\n\0":
'???',

# Misato Katsuragi 
"ま、でも疲れていたんでしょ。\nゆっくり休むといいわ。\n\0":
'???',

# Misato Katsuragi 
"じゃあ、今日の訓練は終わり。\n今日教えた事は忘れないように\nちゃんと覚えとくのよ。\n\0":
'???',

#
# ./USRDIR/event/bs076.har_EXTRACT/bs076.evs
#
# Maya Ibuki 
"エヴァ初号機の予備電源、\nゼロです。\nエヴァ初号機活動停止！\n\0":
'???',

# Shinji Ikari
"あぁ、しまった！\n\0":
'???',

# Misato Katsuragi 
"予備電源が切れたら、エヴァは\n活動停止するって言ったでしょ？\n実戦では絶対に避けるべき事態ね。▽\nさてと、\nもう１回、最初からやりなおす？\n\0":
'???',

# Misato Katsuragi 
"じゃ、もう一度最初から。\n今度は今のような失敗は\nないようにね！\n\0":
'???',

# Misato Katsuragi 
"まぁ、\nちょっと疲れているみたいだしね。▽\n体力回復も仕事のうちだから、\n今日は終わりにしましょうか。\n\0":
'???',

# Shinji Ikari
"はい、すみません…。\n\0":
'???',

# Misato Katsuragi 
"その代わり、今日教えた事は\n絶対忘れちゃダメよ。\n\0":
'???',

#
# ./USRDIR/event/bs071.har_EXTRACT/bs079.evs
#
# Misato Katsuragi 
"シンジ君、緊張してる？\n\0":
'???',

# Kozo Fuyutsuki
"シンジ君、\n緊張しているのかね？\n\0":
'???',

# Female Staff
"初号機パイロット、大丈夫ですか？\n緊張しているようですが…。\n\0":
'???',

# Shinji Ikari
"ええ、…少し。\n\0":
'???',

# Misato Katsuragi 
"そりゃそうよね、無理ないわ。\n使徒が接近するまでの間って、\n時間が長く感じるでしょ。▽\nそんな時は%1iボタンを押して！▽\n「退屈しのぎに何か話す」を\n選べるわ。▽\n何か話せば、自然と\n緊張もほぐれるわよ。\n\0":
'???',

# Kozo Fuyutsuki
"使徒が接近するまでの間というのは、\n時間が長く感じられるものだ。▽\nそんな時は%1iボタンを押してみると\nいい。▽\n「退屈しのぎに何か話す」を\n選ぶ事が出来る。▽\n何か話せば、自然と\n緊張もほぐれる事だろう。\n\0":
'???',

# Female Staff
"そんな時は%1iボタンを\n押して下さい。▽\n「退屈しのぎに何か話す」を\n選ぶ事が出来ます。▽\n何か話せば、自然と\n緊張もほぐれますよ。\n\0":
'???',

# Shinji Ikari
"そうですね、わかりました。\n\0":
'???',

#
# ./USRDIR/event/bs082.har_EXTRACT/bs082.evs
#
# Kozo Fuyutsuki
"よろしい。\nでは次に、使徒の動きについてだ。▽\n君は常に次の使徒の位置を\n読まなければならない。\nこれが君の重要な仕事だ。▽\n使徒の動きを読み、状況に応じた\n指示を心がけてもらいたい。\n\0":
'???',

#
# ./USRDIR/event/bs087.har_EXTRACT/bs087.evs
# ./USRDIR/event/bs999.har_EXTRACT/bs999.evs (Partial)
#
# [Battle: Armisael Attack]
#
# Shinji Ikari
"う…わあぁ…、\nな、何だよこれ…。\n何か、何かが入ってくるよ…。\n\0":
'???',

# Asuka Soryu Langley
"う…くぅ…ッ。\n私の中に…私の身体の中に、\n何かが入ってくる…。\n\0":
'???',

# Rei Ayanami 
"………くっ。\n流れ込んでくる…。\n何かが、私に入ってくる…。\n\0":
'???',

# Toji Suzuhara 
"な、何やこれ…。\nワシの身体…、どないなっとんのや。\n何や…、…コレ何や！！\n\0":
'???',

# Kaworu Nagisa 
"うっ…ッ。\n彼は、僕と融合を図る気か…。\n\0":
'???',

# Maya Ibuki, Female Staff
"危険です、機体の生体部品が\n侵食されていきます。\n\0":
'???',

# Ritsuko Akagi 
"機体が接触部から、\n侵食されているわ。\n\0":
'???',

# Shinji Ikari
"助けて…！　僕の身体が…。\nどうしてこんなに…、ねえ、\nだ、誰か…助けてェ…。\n\0":
'???',

# Asuka Soryu Langley
"いやぁぁぁ…！！\n入ってこないで、\n私の身体から出てってェェェ！！\n\0":
'???',

# Rei Ayanami 
"…私じゃない何かが、\n…入ってくる。\n私に…、入ってくる。\n\0":
'???',

# Toji Suzuhara 
"何かがワシに入ってきよる、\nワシの身体に、頭ン中に…。\n身体が、身体がぁ！！\n\0":
'???',

# Kaworu Nagisa 
"このままじゃ、…僕は、\n…僕は、僕じゃなくなってしまう。\n…分離するのは…無理のようだ。\n\0":
'???',

# Misato Katsuragi 
"…今すぐ助けるわ、\n待ってて！！\n\0":
'???',

# Makoto Hyuga
"すぐ助ける、\n待っているんだ！！\n\0":
'???',

# Male Staff
"すぐに救助を！！\n\0":
'???',

# Ritsuko Akagi 
"無理よ、機体、パイロット共々\n使徒と物理的融合を果たしているわ。▽\n分離する事は不可能よ。\nその代わり、機体の自爆を以って\n目標の殲滅は可能だわ。\n\0":
'???',

# Female Staff
"機体、パイロット共々\n使徒と物理的融合を果たしています。▽\n分離する事は不可能です。\n…その代わり、機体の自爆による\n目標の殲滅は…可能です。\n\0":
'???',

# Misato Katsuragi 
"あんた、\n何言ってるかわかってるの！？\nそんな方法は採れないわ！！\n\0":
'???',

# Misato Katsuragi 
"あんた、\n何言ってるか、わかってるの！？\nそんな方法は採れないわ！！\n\0":
'???',

# Maya Ibuki 
"でも、それで子供が\n犠牲になるなんて、\n許される事ではありません！！\n\0":
'???',

# Makoto Hyuga
"馬鹿な事を！！\n他にあるはずだ、助かる方法が。\n\0":
'???',

# Male Staff
"そんな、このまま\n子供を殺すわけにはいかない！！\n\0":
'???',

# Male Staff
"そんな、\nこのまま子供を殺すわけには\nいかない！！\n\0":
'???',

# Ritsuko Akagi 
"決断なさい。\n我々は、使徒殲滅が目的のはずよ。▽\nそれにあの子は…、助からないわ。\n\0":
'???',

# Female Staff
"しかし、サードインパクトを\n起こすわけにはいかないのですよ。▽\nそれに、パイロットはもう\n助からないんです！！\n\0":
'???',

# Misato Katsuragi, Maya Ibuki, Makoto Hyuga, Male Staff, Shinji Ikari, Kaworu Nagisa,[Text Only - No Designated Speaker]
"…………………………………………\n…………………………………………\n…………………………………………。\n\0":
'???',

# Misato Katsuragi 
"ごめんなさい…。\n\0":
'Forgive me...\n\0',

# Maya Ibuki 
"許して…、\n許してちょうだい…。\n\0":
'???',

# Makoto Hyuga
"すまない、\nこうするしかないんだ。\n…許してくれ。\n\0":
'???',

# Male Staff
"今、楽にするから…。\n\0":
'???',

# Shinji Ikari
"ねぇ…、\n僕は助かるの…？\nねぇ…。\n\0":
'???',

# Asuka Soryu Langley
"早くぅ…、\n誰か、助けに来てよぉ…。\n\0":
'???',

# Rei Ayanami 
"…駄目、動けない…。\n\0":
'???',

# Toji Suzuhara 
"…ああ、これ済んだら、\n妹の見舞い行かなアカンのに…。\n早う…、待っとんのに…。\n\0":
'???',

# Kaworu Nagisa 
"思い出の中の人達…、\nどうか、輝きある未来を…。\n\0":
'???',

# Shigeru Aoba, Male Staff
"使徒、殲滅を確認…。\n目標は消失しました。\n\0":
'???',

#
# ./USRDIR/event/bs087.har_EXTRACT/bs088.evs
#
# [Battle: J.A.2 Departure]
#
# Makoto Hyuga, Male Staff
"ΘΑ改、活動限界！！\n機能停止しました！！\n\0":
'???',

# Shiro Tokita
"…あ、…あぁ、\nチクショウめ！！\nここまでなのか…。\n\0":
'???',

# Toji Suzuhara
"オッチャン、\nようやったやんけ！！▽\nこっちゃ、ごっつい助かっとんねん。\nあとはワシがどないかするさかい、\nはよ安全なトコ行き！！\n\0":
'???',

# Asuka Soryu Langley
"そこは危険よ！！\nオジサン、早く逃げて！！\n\0":
'???',

# Shinji Ikari
"おじさん、早く逃げて！！\n\0":
'???',

# Kaworu Nagisa
"早く、早くここから逃げて！\n助けてくれてありがとう、\nあなたの好意は忘れないよ。\n\0":
'???',

# Misato Katsuragi 
"時田さん、パイロットも\nああ言ってるわ。\n早く避難して！！\n\0":
'???',

# Female Staff
"時田さん、そこは危険です。\n早く避難して下さい。\n\0":
'???',

# Shiro Tokita
"………し、しかし。\n\0":
'???',

# Toji Suzuhara
"オッチャン、\nまたええの作ったらよぉ、\n次はワイが勝負したらぁよ。▽\nせやから、今はワシがきばるわ。\n頑張りや、オッチャン。\n楽しみにしとるでぇ！！\n\0":
'???',

# Asuka Soryu Langley
"また新しいロボットを\n作ってらっしゃい！！\n私が勝負してあげるから。\n\0":
'???',

# Shinji Ikari
"今は逃げて！\nそしてまたみんなのために\nΘΑを作ってよ。▽\nだから今は逃げて！！\n\0":
'???',

# Kaworu Nagisa
"今度、あなたが新しいのを作ったら、\n僕が相手をするよ。\n楽しみにしてる。▽\nだから、その時のために\n逃げて下さい！！\n\0":
'???',

# Shiro Tokita
"………。▽\n…勝てないのはやはり、\n人の心…、か。▽\nよし、ここは君に任せた！！\n頑張れよ、頑張れよー！！\n\0":
'???',

#
# ./USRDIR/event/bs092.har_EXTRACT/bs091.evs
# ./USRDIR/event/bs999.har_EXTRACT/bs999.evs (Partial)
#
# [Battle Uplift: Spear of Longinus Used]
#
# Gendo Ikari
"レイ、ドグマを降りて槍を使え。\n\0":
'Rei, go down to Dogma and use the Spear.\n\0',

# Kozo Fuyutsuki
"碇、ロンギヌスの槍か？\n確かに使徒は仕留められるかも\nしれん。▽\nだが、ゼーレの許可なしに\n使うのはめんどうだぞ！\nそれでも使うのか？\n\0":
'???',

# Male Staff
"司令、委員会の許可なしに\n槍を使う事は出来ません。▽\nそれに、アダムとエヴァの接触は\nサードインパクトを引き起こす\n可能性があります。\n\0":
'???',

# (Decision Prompt)
"構わん、やれ。／まだその時ではない。\0":
'???',

# Gendo Ikari
"構わん、ロンギヌスの槍を使え。\nレイ、頼んだぞ。\n\0":
'???',

# Female Staff
"セントラルドグマ、\n１０番から１５番まで開放。\n\0":
'???',

# Male Staff
"第６マルボルジェ、零号機通過。\n\0":
'???',

# Male Staff
"続いて、１６番から２０番、開放。\n\0":
'???',

# Shigeru Aoba, Male Staff
"零号機、地上に出ます。\n\0":
'???',

# Shigeru Aoba, Male Staff
"零号機投てき体勢。\n\0":
'???',

# Shigeru Aoba, Male Staff
"零号機投てき態勢。\n\0":
'???',

# Makoto Hyuga, Male Staff
"目標確認。\n誤差修正良し。\n\0":
'???',

# Maya Ibuki 
"カウントダウン入ります。▽\n１０秒前！\n８、７、６、５、４、３、２、１、\n０！\n\0":
'???',

# Female Staff
"カウントダウン、入ります。▽\n１０秒前！\n８、７、６、５、４、３、２、１、\n０！\n\0":
'???',

# Gendo Ikari
"…。▽\nまぁいい、\n今はまだその時ではないか。\n\0":
'???',

#
# ./USRDIR/event/bs092.har_EXTRACT/bs092.evs
#
# [Battle: Dummy Plug]
#
# Gendo Ikari
"初号機は\nダミープラグに切り替えろ。\n\0":
'Switch Unit-01 over\nto dummy plug.\n\0',

# Gendo Ikari
"弐号機は\nダミープラグに切り替えろ。\n\0":
'Switch Unit-02 over\nto dummy plug.\n\0',

# Gendo Ikari
"零号機は\nダミープラグに切り替えろ。\n\0":
'Switch Unit-00 over\nto dummy plug.\n\0',

# Gendo Ikari
"参号機は\nダミープラグに切り替えろ。\n\0":
'Switch Unit-03 over\nto dummy plug.\n\0',

# Gendo Ikari
"四号機は\nダミープラグに切り替えろ。\n\0":
'Switch Unit-04 over\nto dummy plug.\n\0',

# Gendo Ikari
"エヴァ両機は\nダミープラグに切り替えろ。\n\0":
'Switch both Eva units\nover to dummy plug.\n\0',

# Kozo Fuyutsuki
"碇、ダミープラグの使用は\nお前だけのみならず、委員会の\n許可を得なければならないんだ。▽\nそれに、ゼーレが黙ってはいないぞ！\nそれでも使うのか？\n\0":
'???',

# Male Staff
"しかし、ダミープラグは司令の他、\n委員会の許可が必要です。\n\0":
'???',

# Gendo Ikari
"構わん、やれ。\n\0":
'Doesn\'t matter. Do it.\n\0',

# Maya Ibuki, Female Staff
"初号機のダミーシステム、\n起動します。\n\0":
'Unit-01\'s dummy system\nis starting up.\n\0',

# Shinji Ikari
"父さん…、\nくそっ、やっぱり僕なんか\nいらないんだ…。\n\0":
'???',

# Maya Ibuki, Female Staff
"初号機、ダミーシステムに\n切り替わりました。\n\0":
'Unit-01 has been switched\nover to dummy system.\n\0',

# Maya Ibuki, Female Staff
"弐号機のダミーシステム、\n起動します。\n\0":
'Unit-02\'s dummy system\nis starting up.\n\0',

# Asuka Soryu Langley
"何よ…、\n私じゃ役不足っていうの…？\n\0":
'???',

# Maya Ibuki, Female Staff
"弐号機、ダミーシステムに\n切り替わりました。\n\0":
'Unit-02 has been switched\nover to dummy system.\n\0',

# Maya Ibuki, Female Staff
"零号機のダミーシステム、\n起動します。\n\0":
'Unit-00\'s dummy system\nis starting up.\n\0',

# Rei Ayanami 
"やっぱり私…、\nいらなくなるのね…。\n\0":
'???',

# Maya Ibuki, Female Staff
"零号機、ダミーシステムに\n切り替わりました。\n\0":
'Unit-00 has been switched\nover to dummy system.\n\0',

# Maya Ibuki, Female Staff
"参号機のダミーシステム、\n起動します。\n\0":
'Unit-03\'s dummy system\nis starting up.\n\0',

# Toji Suzuhara 
"くっそぉ、…何や！！\nワイの事、コケにしおってからに！！\n\0":
'???',

# Maya Ibuki, Female Staff
"参号機、ダミーシステムに\n切り替わりました。\n\0":
'Unit-03 has been switched\nover to dummy system.\n\0',

# Maya Ibuki, Female Staff
"四号機のダミーシステム、\n起動します。\n\0":
'Unit-04\'s dummy system\nis starting up.\n\0',

# Kaworu Nagisa 
"僕は…、\n僕は必要じゃなかったんだ…。\n\0":
'They...\nThey didn\'t need me...\n\0',

# Maya Ibuki, Female Staff
"四号機、ダミーシステムに\n切り替わりました。\n\0":
'Unit-04, switched over to dummy system.\n\0',

# Gendo Ikari
"…。▽\nわかった、もう少し待とう。\n\0":
'???',

#
# ./USRDIR/event/bs092.har_EXTRACT/bs094.evs
#
# [Battle: Jet Alone 2 Arrives]
#
# Toji Suzuhara
"くっそー、勝てるんかホンマに…。\n\0":
'???',

# Asuka Soryu Langley
"向こうはΣ機関搭載か…。\n勝てるかしら…。\n\0":
'???',

# Shinji Ikari
"９機…、\nどう考えたって不利だ…。\n\0":
'???',

# Kaworu Nagisa
"９機か…、\n今度こそ、僕の最後かもしれない。\n\0":
'Nine of them?\nMy final moments may be upon me.\n\0',

# Shiro Tokita
"ジェットアローン改、\n起動スタンバイ！！\n\0":
'Jet Alone 2,\nstand by for activation!!\n\0',

# Toji Suzuhara
"な、何やアレ！？\n\0":
'Wh-what\'s that?!\n\0',

# Asuka Soryu Langley
"もう一体来るの…？\n\0":
'The hell is it now...?\0',

# Shinji Ikari
"な、何か降りてくる！？\n\0":
'S-something\'s come down?!\n\0',

# Kaworu Nagisa
"何だ、あれは…。\n\0":
'What is it...?\n\0',

# Misato Katsuragi 
"あれは…、ΘΑ！？\n\0":
'Is that... ΘΑ?!\n\0',

# Female Staff
"これは…、ΘΑ！？\nジェットアローンです！！▽\nジェットアローンと同じ識別番号を\n持つ機体が現れました！！\n\0":
'???',

# Shiro Tokita
"元日本重化学工業共同体代表、\n時田シロウだ。▽\n配備計画は廃案されたが、\nこのジェットアローン改は\n私の意地と執念の賜物だ。▽\n君達の役に立てれば幸いだ、\n使ってくれ…、パスワードは\nあの言葉だ！！\n\0":
'???',

# Misato Katsuragi 
"………。▽\n時田さん、あなた、\nなかなかの男じゃないの。▽\nそれじゃあ\n遠慮なく使わせてもらうわ！！▽\n操作チャンネルを設定して！\nパスワードは「希望」よ！！\n\0":
'???',

# Female Staff
"わかりました、\n操作チャンネルを設定して下さい。\nパスワードは「希望」！！\n\0":
'???',

# Toji Suzuhara, Toji Suzuhara
"助太刀か、\nかっこええのぉ、オッチャン！\nほな、行こかい！！\n\0":
'???',

# Asuka Soryu Langley
"あの人…、こんな時に\n逃げないで…。▽\nよぉし、こうとなったら\n負けてらんないわ！！\n\0":
'???',

# Shinji Ikari
"おじさんは…。\nこんな危険を冒してまでここへ…？▽\nよし、僕だって…、\n僕だってやってやる！！\n\0":
'???',

# Kaworu Nagisa
"何て無謀な人だろう…。\nあれが、リリンの持つ心、\nこんな危険を冒してまで…。▽\nフフ、弱音を吐いている場合じゃ\nなくなったね。\n\0":
'???',

#
# ./USRDIR/event/bs092.har_EXTRACT/bs095.evs
#
# [Battle: Eva Lift-Up]
#
# Makoto Hyuga, Male Staff
"使徒、ジオフロントに侵入。\n本部へ真っ直ぐ接近中！\n\0":
'The Angel has invaded the GeoFront.\nCurrently on a direct trajectory for Headquarters!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ、リフトアップ！\n\0":
'Evas undergoing lift-up!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ、リフトアップ完了。\nパイロットは、迎撃準備を！\n\0":
'Eva lift-up completed.\nPilots are preparing to intercept!\n\0',

#
# ./USRDIR/event/bs096.har_EXTRACT/bs096.evs
#
# [Battle: Charge Gauge]
#
# Misato Katsuragi 
"次の攻撃はチャージが\n完了するまで出来ないわ。▽\nチャージゲージが\n最大まで回復したら、\nまた%1iボタンを押して攻撃よ！\n\0":
'???',

# Shinji Ikari
"はい、分かりました！\n\0":
'Yes, understood!\n\0',

#
# ./USRDIR/event/bs097.har_EXTRACT/bs097.evs
#
# Misato Katsuragi 
"何ですって！？\nこの距離から、だというの…？▽\nヤツの中和距離は\nこちらの予想以上の広さよ。▽\n恐らく、遠距離攻撃で来るわ！！▽\n気をつけなさい！！\n\0":
'???',

# Kozo Fuyutsuki
"この距離から、というのか！？\nいかん、奴は遠距離攻撃をしかけて\nくるつもりだ。▽\n既に射程内に入っていないとも\n限らん。\n油断するな！！\n\0":
'???',

# Female Staff
"そんな！？\n中和距離の範囲が予想以上だわ。▽\n恐らく使徒は、この距離からでも、\n攻撃可能と思われます。▽\n気をつけて下さい！！\n\0":
'???',

#
# ./USRDIR/event/bs098.har_EXTRACT/bs098.evs
#
# Misato Katsuragi 
"ここを自爆させるわ…。\nいい？\n自爆装置、発動。\n\0":
'???',

# Kozo Fuyutsuki
"ここを自爆させる…。\n人類が生き延びるには\nそれしかない…。\n\0":
'???',

# Female Staff
"ここを自爆させましょう。\nサードインパクトを防ぐには、\nそれしかありません。\n\0":
'???',

# Male Staff
"覚悟は、出来ています。\n\0":
'???',

# Misato Katsuragi 
"…自爆装置が作動しない。\nまさか、あの少年が。\n\0":
'???',

# Kozo Fuyutsuki
"自爆装置が解除された…。\nあの少年の力か！！\n\0":
'???',

# Female Staff
"そんな…、自爆装置が作動しない。\nあの少年が止めたの…？\n\0":
'???',

#
# ./USRDIR/event/bs100.har_EXTRACT/bs100.evs
#
# Misato Katsuragi 
"聞こえる？\nたった今、\n新しい武器が配備されたわ。▽\n今回の戦闘から使ってちょうだい。▽\nマゴロク・Ｅ・ソード、\n強力な武器よ。▽\n大丈夫、きっと使いこなせるわ。\n\0":
'???',

# Ritsuko Akagi 
"たった今、\n新しい武器が配備されたわ。▽\nマゴロク・Ｅ・ソード、\n強力な武器よ。\n今回の戦闘から使えるわ。\n\0":
'???',

# Female Staff
"マゴロク・Ｅ・ソード、\n配備完了しました。\n武器庫ビルに収納済みです。\t\t\n\0":
'???',

#
# ./USRDIR/event/bs101.har_EXTRACT/bs101.evs
#
# Shinji Ikari
"あ………。\n\0":
'???',

# Misato Katsuragi 
"シンジ君。\nアンビリカルケーブルの長さは\n常に意識して移動してちょうだい。▽\nケーブルを外しても、エヴァは\n予備電源で活動できるけど、\nそれはわずかな時間だけよ。\n\0":
'???',

# Misato Katsuragi 
"予備電源も切れたエヴァは\n活動停止となり、\nなにも出来なくなってしまうの。\n\0":
'???',

# Misato Katsuragi 
"まぁ、今はシミュレーション。\n言わば、本番で失敗しない為の\n練習でもあるわ。▽\n今の事は、次に活かしましょう。\n\0":
'???',

# Misato Katsuragi 
"さ、これからどうする？\n「アンビリカルケーブル切断」して\n予備電源で活動するか、▽\nそれとも引き返して、不足分の\nケーブルの長さを取り戻すか？▽\nそれとも、それとも一旦切断して、\n近くの電源ビルで\nケーブル接続を行うか？\n\0":
'???',

# Misato Katsuragi 
"その辺りは、シンジ君。\nあなたの判断に任せるわ。\n\0":
'???',

#
# ./USRDIR/event/bs102.har_EXTRACT/bs102.evs
#
# Misato Katsuragi 
"さて、シンジ君。\n前回のシミュレーションの内容は\n覚えているかしら？\n\0":
'???',

# Shinji Ikari
"…はい。▽\nエヴァの移動方法と\nアンビリカルケーブルについて。▽\nΑΤフィールドとヘイフリック、\n耐久力の意味。▽\nそれと、使徒との戦い方…。\n使徒が射程に入ったら、\n%1iボタンで攻撃を選ぶ…。\n\0":
'???',

# Misato Katsuragi 
"ＯＫ。\nやるじゃない、シンジ君。\n完璧よ。\n\0":
'???',

# Misato Katsuragi 
"今回は、\n前回教えきれなかった要素を\n説明するわね。\n\0":
'???',

# Misato Katsuragi 
"では、始めます。▽\nシンジ君。\nこの黄色いビルを注目して。\n\0":
'???',

# Shinji Ikari
"黄色いビル、ですか？\n\0":
'???',

# Misato Katsuragi 
"第３新東京市の所々に\n配置されている、この黄色いビル。▽\nこれは、武器庫ビル。\nこのビルに、エヴァの\n交換用の武器が格納されているわ。\n\0":
'???',

# Shinji Ikari
"黄色いビルは、\n武器庫ビル…。▽\nでも、どうやって交換するんですか？\n\0":
'???',

# Misato Katsuragi 
"アンビリカルケーブルの接続と\n同じよ。▽\nアンビリカルケーブルの接続は、\nどうだったかしら？\n\0":
'???',

# Shinji Ikari
"…武器庫ビルの近くで%1iボタン。\nですか…？\n\0":
'???',

# Misato Katsuragi 
"そう、ご明察！▽\n武器庫ビルの近くで%1iボタン。\n「武器を装備する」のコマンドを\n選べば、武器の交換ができるわ。\n\0":
'???',

# Misato Katsuragi 
"武器庫ビルの中身は、\n全域マップでも確認できるから\n参考にしてね。\n\0":
'???',

# Misato Katsuragi 
"まぁ、体で覚えた方が早いわね。\n一度、近くの武器庫ビルで\n試してみてちょうだい。\n\0":
'???',

#
# ./USRDIR/event/bs103.har_EXTRACT/bs103.evs
#
# Misato Katsuragi 
"はい、ＯＫ！\nそうやって、装備の変更を行うの。\n覚えといてね。\n\0":
'???',

# Misato Katsuragi 
"あと、装備について\nもう一つ大事な事があるの。▽\n使用回数に限界がある装備。\n例えば、パレットライフルは\n弾数が４発なんだけど…。▽\n使用回数が限界になった装備は\n自動的に破棄されます。\n\0":
'???',

# Misato Katsuragi 
"そうなると、武器庫ビルから\n新たな武器を装備しない限り、\n接近戦しかできなくなるわ。\n\0":
'???',

# Misato Katsuragi 
"戦い方は、パイロットである\nあなたに任せるけど、\nこの事は忘れないでね。\n\0":
'???',

#
# ./USRDIR/event/bs104.har_EXTRACT/bs104.evs
#
# Misato Katsuragi 
"じゃあ、続けるわよ。\n\0":
'???',

# Misato Katsuragi 
"さてと。\n次は、こっちの\n水色のビルに注目して。\n\0":
'???',

# Shinji Ikari
"水色のビルですね。\n\0":
'???',

# Misato Katsuragi 
"これは、兵装ビル。\n\0":
'???',

# Shinji Ikari
"兵装ビル…？\n…武器庫ビルと\nどう違うんですか？\n\0":
'???',

# Misato Katsuragi 
"兵装ビルは、\n使徒が近づいた時に、\n自動迎撃する施設よ。\n\0":
'???',

# Shinji Ikari
"自動迎撃…。\n\0":
'???',

# Misato Katsuragi 
"だから、武器庫ビルや\n電源ビルと違って\nシンジ君が何かする必要は無いわ。\n\0":
'???',

# Misato Katsuragi 
"攻撃力はエヴァに比べれば\n全然、大した事ないから、\n使徒を倒すなんて、どだい無理ね。▽\nまぁ、使徒を足止めするくらいには\n役に立つわ。\n\0":
'???',

# Shinji Ikari
"はぁ…。\n\0":
'???',

# Misato Katsuragi 
"その辺にチョロチョロと\n出張って来てる、コレ。\n\0":
'???',

# Misato Katsuragi 
"コレは、国連軍。\n使徒に向かって行って攻撃するの。\n兵装ビルと似たようなもんね。\n\0":
'???',

# Misato Katsuragi 
"攻撃力も、兵装ビルと同じくらい。\nもちろん、シンジ君が何かする\n必要は無いわ。\n\0":
'???',

# Shinji Ikari
"水色は兵装ビルで、\n国連軍も同じ役割…ですね。\n\0":
'???',

# Misato Katsuragi 
"ＯＫ。\nさっきも言ったけど、\n共に、兵力としては期待しないで。▽\n使徒を倒すには、エヴァ無しでは\nありえないんだから。\n\0":
'???',

# Shinji Ikari, Shigeru Aoba, Rei Ayanami, Hikari Horaki
"はい…。\n\0":
'???',

#
# ./USRDIR/event/bs105.har_EXTRACT/bs105.evs
#
# Misato Katsuragi 
"さて、今度はここに注目。\n\0":
'???',

# Misato Katsuragi 
"これは、防御施設。▽\nこの上に居れば、\nシールドが使徒の攻撃を\n軽減してくれるわ。\n\0":
'???',

# Misato Katsuragi 
"使徒を待ち構えて攻撃を仕掛ける時、\nエヴァの耐久力がヤバイと思った時、\nこの防御施設を活用してちょうだい。\n\0":
'???',

#
# ./USRDIR/event/bs106.har_EXTRACT/bs106.evs
#
# Shinji Ikari
"目標、発見しました。\n\0":
'???',

# Misato Katsuragi 
"シンジ君。\nこれまでに説明した、\n使徒との戦い方の基本、覚えてる？\n\0":
'???',

# Shinji Ikari
"あ、はい。▽\n目標を射程に入れて、%1iボタン…。\n\0":
'???',

# Misato Katsuragi 
"ＯＫ。▽\nじゃあ、もう一つ\n大事な要素を伝えます。▽\nシンジ君。\nこのゲージを見てちょうだい。\n\0":
'???',

# Misato Katsuragi 
"「姿勢を構える」は戦闘を有利に\nするための行動で、ほかにも\n「ナイフを構える」などがあるわ。\n\0":
'???',

# Misato Katsuragi 
"これは、インパルス。\n…聞き覚えあるでしょ？\n\0":
'???',

# Shinji Ikari
"インパルス…。▽\n日常生活で特別な行動を起こすのに\n必要となる、「きっかけ」とでも\n言うべき存在…でしたよね？\n\0":
'???',

# Misato Katsuragi 
"エライわ、シンジ君！\nちゃんと覚えてたわね。▽\nでもね、インパルスが行動を起こす\n「きっかけ」なのは、何も\n日常生活に限った事じゃないのよ。\n\0":
'???',

# Misato Katsuragi 
"戦闘でも、インパルスを消費すれば\n特別な行動が実行できるわ。\n\0":
'???',

# Shinji Ikari
"戦闘中の特別な行動…。\nどんな行動があるんですか？\n\0":
'???',

# Misato Katsuragi 
"そうね…。\n例えば「姿勢を構える」が、\nそれにあたるわね。\n\0":
'???',

# Misato Katsuragi 
"「姿勢を構える」は、打撃攻撃の\n威力を高める行動で、使徒を\n目視範囲内に捉えたら選択できるわ。\n\0":
'???',

# Misato Katsuragi 
"あなたは普段の生活の中で\nインパルスをバンバン溜めて、\n戦闘で思う存分活用なさい。\n\0":
'???',

# Misato Katsuragi 
"「姿勢を構える」が実行されて、\nその効果が発動している間は、\nここに、その情報が表示されるの。\n\0":
'???',

#
# ./USRDIR/event/bs107.har_EXTRACT/bs107.evs
#
# [Text Only - No Designated Speaker]
"初号機はΣ機関の能力を得たため、\nアンビリカルケーブルによる\n電源供給が不要となりました。\n\0":
'???',

#
# ./USRDIR/event/bs108.har_EXTRACT/bs108.evs
#
# Misato Katsuragi 
"迎撃開始ラインに入ったわ。\nさあ、２人の連係プレーを\nとくと見せてあげなさい！\n\0":
'???',

# Kozo Fuyutsuki
"勝敗の鍵は、君達２人の活躍に\nかかっている。\n任せたぞ。\n\0":
'???',

# Female Staff
"エヴァ両機、迎撃開始ラインに\n入りました！\n\0":
'???',

#
# ./USRDIR/event/bs999.har_EXTRACT/bs999.evs (Partial)
#
# Misato Katsuragi 
"シンジ君、\n今、使徒の攻撃を受けた時、\nエヴァが光ったでしょ？\n\0":
'???',

# Kozo Fuyutsuki
"今、使徒の攻撃を受けた際に、\nエヴァが光っただろう？\n\0":
'???',

# Female Staff
"今、使徒の攻撃を受けた時、\nエヴァが光りましたね？\n\0":
'???',

# Shinji Ikari
"…はい、今のは？\n\0":
'???',

# Misato Katsuragi 
"エヴァが光るその瞬間は、\n相手の攻撃を防御するチャンスなの。\n\0":
'???',

# Kozo Fuyutsuki
"今のようにエヴァが光る時は、\n使徒の攻撃を防御するチャンス\nなのだよ。\n\0":
'???',

# Female Staff
"あの光る瞬間は、使徒の攻撃を\n防御するチャンスなんです。\n\0":
'???',

# Shinji Ikari
"防御ですか？\n\0":
'???',

# Misato Katsuragi 
"攻撃を受ける時、\nエヴァが光った瞬間に\n%1iボタンを押せばいいの。▽\nそうすれば、使徒の攻撃を防御して、\n無効化する事が出来るわ。▽\n使徒の強力な攻撃を回避したい時に\n狙ってみて。\n\0":
'???',

# Kozo Fuyutsuki
"攻撃を受ける時、\nエヴァが光った瞬間に\n%1iボタンを押せばよい。▽\nそうする事により、使徒の攻撃を\n防御して、無効化する事が出来る。▽\n使徒の強力な攻撃を回避したい時に\n狙ってみてくれ。\n\0":
'???',

# Female Staff
"攻撃を受ける時、エヴァが光った\n瞬間に%1iボタンを押して下さい。▽\nそうすれば、使徒の攻撃を防御して、\n無効化する事が出来ます。▽\n使徒の強力な攻撃を回避したい時に\n狙ってみて下さい。\n\0":
'???',

# Shinji Ikari
"防御は、エヴァが光った時に\n%1iボタン…。▽\nわかりました。\n光った時に%1iボタンですね！\n\0":
'???',

# Shigeru Aoba
"使徒、$fエリアまで、\n移動しました！\n\0":
'???',

# Kozo Fuyutsuki
"いよいよ実戦だな、葛城君。▽\nこの日のために全てを費やしてきた。▽\n１５年前の悲劇を\n再び繰り返す事がないようにな。\n\0":
'???',

# Misato Katsuragi 
"はい、\n重々承知しております。\n\0":
'???',

# Kozo Fuyutsuki
"使徒に勝てるかどうかは、\n君の作戦と指揮にかかっている。▽\n特に、パイロット達に直接指示を\n与える君の仕事は重要だ。▽\nただ、まだ君も不慣れだろうから、\n今回は私が君のサポートを\n行おうと思う。▽\nこの戦闘で実戦の指揮というものを\n肌で感じ、的確な指示を出せる\nようになってくれたまえ。▽\n我々は、一度たりとも負ける\nわけにはいかないのだからな。\n\0":
'???',

# Kozo Fuyutsuki
"ではまず、\n使徒の位置を確認しよう。▽\n「アナログパッド」で画面を動かし\n使徒を画面に捉えてくれ。\n\0":
'???',

# Misato Katsuragi 
"副司令、使徒を画面に捉えました。\n\0":
'???',

# Kozo Fuyutsuki
"よろしい。\nでは次に、使徒の動きについてだ。▽\n知っているとは思うが、\n使徒の位置は電波妨害のため、\n一定時間おきにしか確認出来ない。\n\0":
'???',

# Kozo Fuyutsuki
"だから、君は常に次の使徒の位置を\n読まなければならない。\nこれが君の重要な仕事だ。▽\n使徒の動きを読み、状況に応じた\n指示を心がけてもらいたい。\n\0":
'???',

# Misato Katsuragi 
"はい。\nもちろんです。\n\0":
'Yes.\nOf course.\n\0',

# Shigeru Aoba
"使徒、移動を開始しました。\n\0":
'???',

# Kozo Fuyutsuki
"では、次に君が行う事は\nパイロットへの移動指示だ。▽\nその前に、しばらく使徒の動きを\n観察してみよう。\n\0":
'???',

# Shigeru Aoba
"使徒、初号機の迎撃開始ラインに\n侵入しました。\n\0":
'???',

# Kozo Fuyutsuki
"次は、エヴァの誘導だ。▽\nまず、君はパイロットに\n移動指示を出し、エヴァを使徒の\n場所まで誘導しなければならない。\n\0":
'???',

# Kozo Fuyutsuki
"使徒の位置は一定時間おきにしか\n確認出来ない。▽\n君の読みが悪ければ、接触の\nチャンスを逃す事になってしまう。▽\nもし、接触のチャンスを逃し、\nエヴァが使徒に追いつく事が\n出来なければ…、\n\0":
'???',

# Kozo Fuyutsuki
"ゼロエリアを突破され、ここネルフ\n本部が危機にさらされる事になる。\n十分、肝に銘じておいてくれたまえ。\n\0":
'???',

# Kozo Fuyutsuki
"では、移動指示の出し方だ。▽\n移動させたい場所で%1iボタンを押し、\n選択肢の中から移動指示を与えたい\nエヴァを選ぶ。わかってるな。\n\0":
'???',

# Kozo Fuyutsuki
"では、任せたぞ。\n\0":
'???',

# Kozo Fuyutsuki
"次は戦闘指示だ。\n\0":
'???',

# Kozo Fuyutsuki
"戦闘指示は、\n接近戦、射撃戦、退避。\nこの３つの指示が行える。▽\nエヴァや使徒の耐久力、パイロット\nのΑΤなどの情報を把握し、\n状況に応じ適切な指示を選んでくれ。▽\n方法は「パイロットに指示を与える」\nを選んでパイロットを選び、\n各指示を選ぶだけだ。▽\nいいな、\nでは、指示を出したまえ。\n\0":
'???',

# Kozo Fuyutsuki
"葛城君、君に神経接続切断について\n話しておかなければならない。\n\0":
'???',

# Misato Katsuragi 
"神経接続切断…ですか？\n\0":
'???',

# Kozo Fuyutsuki
"そうだ、パイロットのシンクロ率が\n低い時などに、何としても\nダメージを回避させたい時は…、\n\0":
'???',

# Misato Katsuragi 
"カーソルを、エヴァに合わせて\n%1iボタン…。\n\0":
'???',

# Kozo Fuyutsuki
"その通りだ。▽\n神経接続をカットすれば、\nパイロットへのダメージフィード\nバックを防ぐ事が出来る。▽\nただし、再接続中は\nエヴァが動けなくなる、\nその点は注意したまえ。\n\0":
'???',

# Misato Katsuragi 
"やったわ！\n\0":
'We did it!\n\0',

# Kozo Fuyutsuki
"よくやったな。\n初めてにしては上出来だったよ。\n\0":
'???',

# Misato Katsuragi 
"いえ、パイロットの実力と、\n副司令のサポートのおかげです。\n\0":
'???',

# Kozo Fuyutsuki
"そんな頼りない事を言われては\nこの先困るな。まあいい。▽\n一つだけ、移動指示について\n補足させてもらう。▽\n移動指示は、エヴァを指定ポイント\nに誘導出来る事を利用して、防御\n施設の上で、迎撃する事も出来る。▽\n今後はそういった応用も考慮\nしながら、指揮をとってくれたまえ。\n\0":
'???',

# Misato Katsuragi 
"了解！！\nご指導、ありがとうございました。\n\0":
'???',

#
# ./USRDIR/event/bs999.har_EXTRACT/bs999.evs (Partial)
#
# Misato Katsuragi 
"どうしちゃったって言うのよ、\nこんな時に…。\n\0":
'???',

# Ritsuko Akagi 
"あなた、\nちゃんとあの子の管理やってるの？▽\n指示を与える指揮官と、\n実際に戦場で戦うパイロット。▽\nしっかりした信頼関係がないと\nこんな時に上手くいかず、\n困る事になるのよ。\n\0":
'???',

# Female Staff
"作戦部長、ちゃんとあの子の管理、\nやっておられますか？▽\n指揮官とパイロットはしっかりした\n信頼関係がないと、こんな時に\n困る事になるんですよ。\n\0":
'???',

# Misato Katsuragi 
"やっぱ、相手は子供だしね…。\n\0":
'???',

# Ritsuko Akagi 
"他に理由として考えられるのは…、\nやる気ね。▽\nこの街や、ネルフを守ろうという\n正義感、頑張って人に認められよう、\n誉められようとする名誉欲、▽\nそういうものが欠けると、\nパイロットは戦う目的を見失い、\nやる気を無くしてしまうわ。▽\nあなた、何か心当たりが\nあるんじゃない？\n\0":
'???',

# Female Staff
"他に理由として考えられるのは、\n…やる気ですね。▽\nこの街やネルフを守ろうという\n正義感、頑張って人に認められよう、\n誉められようとする名誉欲、▽\nそういうものが欠けると、\nパイロットは戦う目的を見失い、\nやる気を無くしてしまいます。▽\n何か、心当たりありませんか？\n\0":
'???',

# Misato Katsuragi 
"何にせよ、責任は私にアリね…。\n思春期の心はわかりづらいわ。\n\0":
'???',

#
# ./USRDIR/event/bs999.har_EXTRACT/bs999.evs (Partial)
#
# [Battle: Pilot Refusing Orders]
#
# Shinji Ikari
"嫌です。\n\0":
'No.\n\0',

# Shinji Ikari
"そんな事出来ません。\n\0":
'I can\'t do something like that.\n\0',

# Shinji Ikari
"僕は自分が思う通りにします。\n\0":
'???',

# Shinji Ikari
"その指示は聞けません。\n\0":
'???',

# Kozo Fuyutsuki
"指示に従いたまえ！\n\0":
'???',

# Female Staff
"独断行動は危険です！\n\0":
'???',

# Asuka Soryu Langley
"うるさい！\nアンタの命令なんか聞けないわ。\n\0":
'???',

# Asuka Soryu Langley
"イヤ、\n絶対にイヤ！\n\0":
'???',

# Asuka Soryu Langley
"バカにしないでよ。\n私の事は、私が決めるわ。\n\0":
'???',

# Asuka Soryu Langley
"お断りよ。\n黙って見てりゃいいのよ！\n\0":
'???',

# Misato Katsuragi 
"アスカっ！！\n\0":
'Asuka!!\n\0',

# Kozo Fuyutsuki
"命令を無視するつもりか！！\n\0":
'???',

# Female Staff
"弐号機パイロット、\n命令に従って下さい！\n\0":
'Pilot of Unit-02,\nplease follow your order!\n\0',

# Rei Ayanami 
"…命令は聞けません。\n\0":
'???',

# Rei Ayanami 
"拒否します…。\n\0":
'I refuse...\n\0',

# Rei Ayanami 
"どうするかは、私が決めます。\n\0":
'???',

# Rei Ayanami 
"いいえ。\n私は、独断で行動します。\n\0":
'No. I will act\naccording to my own judgment.\n\0',

# Kozo Fuyutsuki
"命令違反だぞ！！\n\0":
'You\'re violating an order!\n\0',

# Female Staff
"危険です、\n指示に従って下さい。\n\0":
'???',

# Toji Suzuhara 
"そんな命令、聞けまへんわ。\n\0":
'???',

# Toji Suzuhara 
"冗談でしょ？\nお断りしますわ。\n\0":
'This a joke?\nI refuse.\n\0',

# Toji Suzuhara 
"そんなん聞けんわ！\n絶対嫌やわ。\n\0":
'???',

# Toji Suzuhara 
"ワシかて自分で行動出来ます！\n口出さんといて下さい。\n\0":
'???',

# Misato Katsuragi 
"トウジ君っ！！\n\0":
'Toji-kun!!\n\0',

# Kozo Fuyutsuki
"無茶しおって！！\n\0":
'???',

# Female Staff
"参号機パイロット、\n命令違反はいけません。\n\0":
'Pilot of Unit-03,\nyou mustn\'t violate an order.\n\0',

# Kaworu Nagisa 
"その指示には納得出来ませんね。\n\0":
'???',

# Kaworu Nagisa 
"嫌です、\nそれは僕が判断します。\n\0":
'???',

# Kaworu Nagisa 
"知りませんよ、そんな事。\n\0":
'???',

# Kaworu Nagisa 
"その必要はないと思いますけど。\n\0":
'???',

# Kozo Fuyutsuki
"何を言うか！！\n指示通りに行動するんだ！\n\0":
'???',

# Female Staff
"四号機、命令に従って下さい。\n\0":
'Unit-04, please follow your order.\n\0',

#
# ./USRDIR/event/bs999.har_EXTRACT/bs999.evs (Partial)
# 
# Kozo Fuyutsuki
"葛城君、\n作戦の運びは\nどのようになるのかね？\n\0":
'???',

# Misato Katsuragi 
"あ、はい。\n今から設定するところです。\n\0":
'???',

# Kozo Fuyutsuki
"そうか。\nでは、私がいくつか作戦設定に\nついて、アドバイスをしよう。\n\0":
'???',

# Misato Katsuragi 
"はい。\nよろしくお願いします。\n\0":
'???',

# Male Staff
"作戦の目処はつきましたか？\n\0":
'???',

# Misato Katsuragi 
"まあ、\n今から作戦設定するところなの。\n\0":
'???',

# Male Staff
"私でよろしければ、作戦設定に\nついて、アドバイスを行いましょう。\n\0":
'???',

# Misato Katsuragi 
"ええ、お願いするわ。\n\0":
'???',

# Kozo Fuyutsuki
"では、パイロットの選択についてだ。▽\nまず、機体及び、\n搭乗するパイロットの状態を\nよくチェックする事だ。▽\nΑΤが低いパイロットや稼動状況が\n低いエヴァを出撃させても\nあまり戦力にならないからな。▽\nそうして、出撃させるパイロットを\n決めるといい。\n\0":
'???',

# Male Staff
"では、パイロットの選択について\n説明します。▽\nまず、機体及び\n搭乗するパイロットの状態を\nよくチェックしましょう。▽\nΑΤが低いパイロットや稼動状況が\n低いエヴァを出撃させても、\nあまり戦力になりません。▽\nチェックが済んだら、\n作戦に参加させるパイロットを\n選出しましょう。\n\0":
'???',

# Kozo Fuyutsuki
"出撃パイロットを選択した次は、\nエヴァの迎撃ポイントと\n装備の設定だ。▽\n%1iボタンで作戦立案に関する\nコマンドを起動できる。\n試してみたまえ。\n\0":
'???',

# Male Staff
"パイロットの選出の次は、\nエヴァの迎撃ポイントと\n装備の設定です。▽\nアナログパッドでカーソルを動かし、\n%1iボタンでエヴァを選びます。\n\0":
'???',

# Kozo Fuyutsuki
"作戦立案のコマンドでは\nエヴァに対して初期配置場所と\n装備武装の設定が行える。▽\nまずは初号機を配置したい場所で\n「初号機を配置する」を\n選んでみたまえ。▽\n次に武装を設定するといいだろう。\n「初号機に武装する」で\n選択した武器を初号機に装備できる。▽\n国連軍の攻撃機も配置できる。\n使徒の移動経路となるような場所に\n配備して、使徒索敵に役立ててくれ。▽\n作戦立案が終了したら\n「作戦立案終了、次に進む」だ。▽\n作戦内容がパイロットに伝達され、\n作戦が開始される。\n\0":
'???',

# Male Staff
"エヴァに対しては、\n以下の３つの設定が行えます。▽\n迎撃ポイントを設定する、移動。\n装備を設定する、装備。\nエヴァの状態を確認する、情報。▽\n一通り全部試し終わったならば、\n%2iボタンを押して、作戦を決定して\n下さい。\n\0":
'???',

# Kozo Fuyutsuki
"迎撃ポイントの設定は、作戦設定に\nおいて、一番重要な要素だ。▽\n使徒の出現位置や兵装ビルの位置を\n見ながら、どこで、どう使徒を迎撃\nするか想定し、配置する必要がある。▽\nエヴァ以外にも国連軍の配置も行う\n事が出来るから、それらを踏まえ、\n最もよい配置を行ってくれ。\n\0":
'???',

# Male Staff
"迎撃ポイントの設定は、作戦設定に\nおいて、一番重要な要素です。▽\n使徒の出現位置や兵装ビルの位置を\n見ながら、どこで、どう使徒を迎撃\nするか想定し、配置を行います。▽\nエヴァ以外にも国連軍の配置も行う\n事が出来ますので、それらを踏まえ、\n最もよい配置を行って下さい。\n\0":
'???',

# Misato Katsuragi 
"ありがとう、わかったわ。\n\0":
'???',

# Kozo Fuyutsuki
"エヴァの装備は、その重量によって\n装備した時の移動速度が変化する。▽\n要するに、重い武器を持つと、\nその分移動速度が低下してしまう。▽\n装備は、戦闘中に武器庫ビルでも\n交換出来る事を忘れないようにな。▽\n武器の性能をよく見て\n選んでくれたまえ。\n\0":
'???',

# Male Staff
"エヴァの装備は、その重量によって\n装備した時の移動速度が変化します。▽\n重い武器を持つと、その分移動速度\nが低下するんです。▽\nあと、武器の性能をよく見て\n選択して下さい。▽\n装備は、戦闘中に武器庫ビルでも\n交換出来る事をお忘れなく。\n\0":
'???',

# Misato Katsuragi 
"ＯＫ。\n\0":
'???',

# Kozo Fuyutsuki
"この画面で、パイロットのΑΤ、\nシンクロ率やエヴァの各種情報が\n確認出来る。▽\n作戦を立てる時の参考にするといい。\n\0":
'???',

# Male Staff
"この画面で、パイロットのΑΤ、\nシンクロ率やエヴァの各種情報が\n確認出来ます。▽\n作戦を立てる時の参考にすると\nいいでしょう。\n\0":
'???',

# Kozo Fuyutsuki
"葛城君、まだ試していない\nコマンドが残っている。▽\nエヴァを選んで、試していない\nコマンドを使ってみてくれたまえ。\n\0":
'???',

# Kozo Fuyutsuki
"作戦が出来たようだな…。\nこれで、私が教える事は全部伝えた。▽\nあとは、パイロットに\n作戦を伝達して戦闘開始。\n頑張ってくれたまえ、葛城君。\n\0":
'???',

# Misato Katsuragi 
"準備は出来た？\nこれから、今回の作戦を伝達します。\nしっかり、頭に叩き込んでね。\n\0":
'???',

# Female Staff
"準備はよろしいですか？▽\nこれより、今回の作戦を伝達します。\n\0":
'???',

# Misato Katsuragi, Female Staff
"以上が、今回の作戦要綱となります。\n\0":
'???',

#
# ./USRDIR/event/b2s00.har_EXTRACT/b2s00.evs
#
# Misato Katsuragi 
"電波かく乱のために目標を\n消失している状態なの。\n正確な位置の測定は出来ないけど…、▽\nロスト直前までのデータから\nマギが算出した落下予想地点が\nこれよ。\n\0":
'???',

# Female Staff
"電波かく乱のために目標を\n消失している状態にあります。\n正確な位置の測定は出来ませんが…、▽\nロスト直前までのデータから\nマギが算出した落下予想地点が\nこれです。\n\0":
'???',

#
# ./USRDIR/event/b2s01.har_EXTRACT/b2s01.evs
#
# Misato Katsuragi 
"みんな、いいわね。\nもう一度作戦内容を確認します。\n\0":
'???',

# Female Staff
"では、もう一度\n作戦内容を伝えます。\n\0":
'???',

# Misato Katsuragi 
"作戦開始と同時に\nアンビリカルケーブル切断。▽\nあなた達は全体マップに表示される\n使徒の落下予想範囲を目指して\n移動を開始してちょうだい。▽\n落下予想範囲は一定時間毎に\n更新され、より正確な\n落下予想範囲が表示されていきます。▽\n常に最新の落下予想範囲を確認して、\nその地点へ効率よく迅速に移動して。▽\n最終落下ポイントに到着したエヴァは\n「ΑΤフィールド全開」で、\n使徒の落下を阻止。▽\n最初に落下ポイントに到着した\nエヴァは、残りが到着するまで\n持ちこたえてちょうだい。\n\0":
'???',

# Female Staff
"作戦開始と同時に\nアンビリカルケーブル切断。▽\nあなた達は全体マップに表示される\n使徒の落下予想範囲を目指して\n移動を開始してください。▽\n落下予想範囲は一定時間毎に\n更新され、より正確な\n落下予想範囲が表示されていきます。▽\n常に最新の落下予想範囲を確認して、\nその地点へ効率よく迅速に移動。▽\n最終落下ポイントに到着したエヴァは\n「ΑΤフィールド全開」で、\n使徒の落下を阻止。▽\n最初に落下ポイントに到着した\nエヴァは、残りが到着するまで\n持ちこたえてください。\n\0":
'???',

# Shinji Ikari
"使徒の落下を支えきれなかったり、\n落下地点にエヴァの到着が\n間に合わなかったら…？\n\0":
'???',

# Asuka Soryu Langley
"えー、何かアバウトよね。▽\n使徒の落下を支えきれなかったり、\n落下地点にエヴァの到着が\n間に合わなかったら…？\n\0":
'???',

# Rei Ayanami 
"使徒の落下を支えきれなかったり、\n落下地点にエヴァの到着が\n間に合わなかった場合は？\n\0":
'???',

# Toji Suzuhara 
"えー、…まるでバクチやな。▽\nほな、使徒の落下を支えきれへん\nかったり、落下地点にエヴァの\n到着が間に合わんかったら…？\n\0":
'???',

# Kaworu Nagisa 
"質問です。▽\n使徒の落下を支えきれなかったり、\n落下地点にエヴァの到着が\n間に合わなかったら…？\n\0":
'???',

# Misato Katsuragi 
"その時は、何もかも終わりよ。\n以上が作戦です。▽\nそれじゃ、作戦開始！！\n\0":
'???',

# Female Staff
"その時の覚悟はみんな出来ています。\nこんな作戦しか立てられませんが。▽\nそれでは、作戦を開始します！\n\0":
'???',

#
# ./USRDIR/event/b2s02.har_EXTRACT/b2s02.evs
#
# Shigeru Aoba, Male Staff
"エヴァ各機、体内電源０！\n活動限界です！\n\0":
'???',

#
# ./USRDIR/event/b2s05.har_EXTRACT/b2s05.evs
#
# Shinji Ikari, Kaworu Nagisa, Asuka Soryu Langley, Rei Ayanami, Toji Suzuhara
"ΑΤフィールド、全開！！\n\0":
'???',

#
# ./USRDIR/event/b2s06.har_EXTRACT/b2s06.evs
#
# Shinji Ikari
"間に合った！！\nとどめだ！！\n\0":
'???',

# Kaworu Nagisa 
"爆発に備えて！\n行くよ！！\n\0":
'???',

# Asuka Soryu Langley
"こンのぉぉぉ！\nくたばれぇぇぇ！！\n\0":
'???',

# Rei Ayanami 
"零号機、\nコアの攻撃へ移行します！\n\0":
'???',

# Toji Suzuhara 
"ワシのドツキ、\n食らってみぃ！！\n\0":
'???',

#
# ./USRDIR/event/b2s07.har_EXTRACT/b2s07.evs
#
# Asuka Soryu Langley
"ぃいやぁぁぁぁあああ！！\n\0":
'???',

# Rei Ayanami 
"く…ッ！！\n\0":
'???',

# Toji Suzuhara 
"ふんぬぅぅぅぁぁあ！！\n\0":
'???',

# Kaworu Nagisa 
"はッ…！！\n\0":
'???',

# Shinji Ikari
"このおォォォ…！！\n\0":
'???',

#
# ./USRDIR/event/b2s08.har_EXTRACT/b2s08.evs
#
# Asuka Soryu Langley
"もう駄目…！！\n支えきれないわ！！\n\0":
'???',

# Rei Ayanami 
"駄目…、\nもう機体が持ちこたえられない。\n\0":
'???',

# Toji Suzuhara 
"アカン…、くそ…。\nもう、これ以上こらえるんは…。\n\0":
'???',

# Kaworu Nagisa 
"く…、これが精一杯だと言うのに。\nもう、これ以上は…ッ。\n\0":
'???',

# Shinji Ikari
"く…、駄目だっ…！\nこれ以上、力が…ッ！！\n\0":
'???',

#
# ./USRDIR/event/b2s09.har_EXTRACT/b2s09.evs
#
# Shigeru Aoba, Male Staff
"使徒、地表に着弾します！\nエヴァ、間に合いません！\n\0":
'???',

#
# ./USRDIR/event/b2s10.har_EXTRACT/b2s10.evs
#
# Asuka Soryu Langley
"これを失敗したら、\n多分、弐号機を下ろされる。\nミスは許されないわよ、アスカ。\n\0":
'???',

#
# ./USRDIR/event/b2s11.har_EXTRACT/b2s11.evs
#
# Misato Katsuragi 
"今回は、使徒殲滅の為に\nロンギヌスの槍を使用する事に\nなったわ。▽\n槍は、零号機が使用。\n現在、零号機は槍入手のため\nセントラルドグマに向かっています。▽\n他パイロットは、地上にて使徒の\n動向を見ながら待機になります。▽\n以上です。\n作戦開始！\n\0":
'???',

# Female Staff
"今回は、使徒殲滅の為に\nロンギヌスの槍を使用します。▽\n槍は、零号機が使用。\n現在、零号機は槍入手のため\nセントラルドグマに向かっています。▽\n他パイロットは、地上にて使徒の\n動向を見ながら待機。▽\n以上が作戦となります。\nでは、作戦を開始します。\n\0":
'???',

# Shinji Ikari
"まだ、射程外か…。\n綾波が到着するまで…、\nあとどの位なんだ。\n\0":
'???',

# Asuka Soryu Langley
"もうっ！\nファーストが来る前に片付けて\nやるから、さっさと来なさいよ！\n\0":
'???',

# Toji Suzuhara 
"何や…、アイツ。\n街を攻撃するでもなし、\n得体の知れん奴やのー。\n\0":
'???',

# Kaworu Nagisa 
"しばらくは、膠着状態か…。\nこちらから、出るか？\nどうする…。\n\0":
'???',

#
# ./USRDIR/event/b2s14.har_EXTRACT/b2s14.evs
#
# [Battle Uplift: Spear of Longinus Used]
#
# Kozo Fuyutsuki
"碇、まだ早いのではないか？\n\0":
'???',

# Gendo Ikari
"委員会はエヴァシリーズの量産に\n着手した。\nチャンスだ冬月。\n\0":
'???',

# Kozo Fuyutsuki
"しかし、な。\n\0":
'???',

# Gendo Ikari
"時計の針は元に戻らない。\nだが自らの力で進める事は出来る。\n\0":
'???',

# Kozo Fuyutsuki
"老人達が黙ってないぞ。\n\0":
'The old men won\'t keep quiet.\n\0',

# Gendo Ikari
"ゼーレが動く前に、\n全て済まさねばならん。\n今、弐号機を失うのは得策ではない。\n\0":
'???',

# Kozo Fuyutsuki
"かといって、ロンギヌスの槍を\nゼーレの許可なく使用するのは、\n面倒だぞ。\n\0":
'???',

# Gendo Ikari
"理由は存在すればいい。\nそれ以上の意味はない。\n\0":
'???',

# Kozo Fuyutsuki
"理由？\nお前が欲しいのは、口実だろう？\n\0":
'???',

#
# ./USRDIR/event/b2s16.har_EXTRACT/b2s16.evs
#
# Shigeru Aoba, Male Staff
"零号機、投てき体勢。\n\0":
'???',

#
# ./USRDIR/event/b2s17.har_EXTRACT/b2s17.evs
# 
# [Battle: Arael Unleashes Mental Attack]
#

# Misato Katsuragi 
"敵の指向性兵器なの！？\n\0":
'???',

# Female Staff
"敵の指向性兵器！？\n\0":
'???',

# Shigeru Aoba, Male Staff
"いえ、熱エネルギー反応なし！\n\0":
'???',

# Maya Ibuki, Female Staff
"心理グラフが乱れています！\n精神汚染が始まります！\n\0":
'???',

# Ritsuko Akagi 
"使徒が心理攻撃！？\nまさか、使徒に人の心が\n理解出来るの？\n\0":
'???',

# Male Staff
"使徒が心理攻撃！？\n使徒に人の心が理解出来るとでも？\n\0":
'???',

# Shinji Ikari
"く…うぅ、うわああああああ！！\n\0":
'???',

# Asuka Soryu Langley
"うぅ…、ううぅああああ！！\n\0":
'???',

# Toji Suzuhara 
"うわああぁぁぁ！！\n\0":
'???',

# Kaworu Nagisa 
"…これは、…こいつは！？\n\0":
'This... It\'s...?!\n\0',

#
# ./USRDIR/event/b2s18.har_EXTRACT/b2s18.evs
#
# Maya Ibuki, Female Staff
"可視波長のエネルギー波、\n使徒の心理攻撃、来ます！\n\0":
'The Angel is attacking psychically\nwith energy waves on the visible spectrum!\n\0',

#
# ./USRDIR/event/b2s19.har_EXTRACT/b2s19.evs
#
# Maya Ibuki, Female Staff
"パイロット側からのパルス抵抗確認。\n交戦しています。\n\0":
'???',

# Misato Katsuragi 
"零号機が戻ってくるまで、\nパイロットの自我が保たれれば…。\n\0":
'???',

# Misato Katsuragi 
"パイロットの自我、精神力の強さが\n使徒の心理攻撃に対抗出来れば。\n…それに賭けるしかない、今は。\n\0":
'???',

# Male Staff
"零号機が戻ってくるまで、\nパイロットの自我が保たれて\nいれば…。▽\nパイロットの自我、精神力の強さが\n使徒の心理攻撃に対抗出来れば。\n…それに賭けるしかないのか。\n\0":
'???',

#
# ./USRDIR/event/b2s20.har_EXTRACT/b2s20.evs
#
# Shinji Ikari
"来るな…！\n入って来るなーっ！！\n\0":
'???',

# Asuka Soryu Langley
"いや…、来ないで！\n覗かないでーッ！！\n\0":
'???',

# Toji Suzuhara 
"来んな！！\n踏み込んで来るな！！\n来んなーッ！！\n\0":
'???',

# Kaworu Nagisa 
"…呼ぶな。\n僕を、呼ぶな！！\n\0":
'???',

#
# ./USRDIR/event/b2s21.har_EXTRACT/b2s21.evs
#
# [Battle Event: Arael Attack]
#
# Shinji Ikari
"わぁぁぁぁぁっ！！\n行かないで、捨てないで！！\n父さん、父さん！！\n\0":
'Wahhhhh!!\nDon\'t go, don\'t leave me!\Father! Father!!\n\0',

# Shinji Ikari
"母さん、こんなの母さんじゃない！\nこんなところに母さんなんて居ない！\n父さんの、父さんのせいだ！！\n\0":
'???',

# Shinji Ikari
"母さんはどこなの！？\nどこいったの、母さん！！\n\0":
'???',

# Shinji Ikari
"置いていかないで！！\nあんなところに居たくないよ！\n父さんッ！！\n\0":
'???',

# Asuka Soryu Langley
"ママ！！　ママ！！\nお願いだから、ママをやめないで！！\n\0":
'Mama!! Mama!!\nPlease, don\'t stop being my mama!\n\0',

# Asuka Soryu Langley
"ママ！！　やめて！！\nお願いだから私を殺さないで！！\n\0":
'Mama! Stop!!\nPlease don\'t kill me!!\n\0',

# Asuka Soryu Langley
"イヤ！\n私はママの人形じゃない！！\n\0":
'No!\nI\'m not Mama\'s doll!!\n\0',

# Asuka Soryu Langley
"ママ！　ママ！！\nこっちを向いて！！\n私はここなのに！！\n\0":
'Mama! Mama!!\nLook over here!!\nI\'m right here!!\n\0',

# Toji Suzuhara 
"おかん、おかんは眠ってんねや！\nどこ連れてくねん！\nおかんを返せ、返せ！！\n\0":
'???',

# Toji Suzuhara 
"死んでへん、おかんは死んでへん！\nおとん、おかんを\n取り返してくれよ、なぁ！\n\0":
'???',

# Toji Suzuhara 
"俺のおかんや！！\n触るな、触るな！！\n触るなーーー！！\n\0":
'???',

# Toji Suzuhara 
"おとん、おじぃ！！\n何でおかん連れてかれるん！？\n止めろや、止めてぇな！！\t\n\0":
'???',

# Kaworu Nagisa 
"違う！！\n僕は、ヒトと生きるんだ！\nそんな運命は要らない！\n\0":
'???',

# Kaworu Nagisa 
"やめろ、違う！！\n僕はそんな姿じゃない！！\n\0":
'???',

# Kaworu Nagisa 
"嫌だ！！\n槍に刺されるのはもう嫌だ！\n\0":
'No!!\nI don\'t want to be stabbed by the Spear anymore!\n\0',

# Kaworu Nagisa 
"やめろ、僕をどうするつもりだ！\n計画なんか知らない！！\nそんなもの押し付けないでくれ！\n\0":
'???',

#
# ./USRDIR/event/b2s22.har_EXTRACT/b2s22.evs
#
# Shinji Ikari
"嫌だ…、消えてしまう。\n僕は…、どこにも…\n誰からも…。\n\0":
'???',

# Asuka Soryu Langley
"汚された…。\n私の心が汚された。▽\nどうしよう、\n汚されちゃったよぅ…。\n\0":
'???',

# Toji Suzuhara 
"嫌や…、嫌やぁ…。\nそんなん、知らんでもよかったんや。\nそんなん、知りたなかったのに…。\n\0":
'???',

# Kaworu Nagisa 
"僕…、僕は…。\n僕…は……………。\n\0":
'???',

#
# ./USRDIR/event/b2s23.har_EXTRACT/b2s23.evs
#
# Maya Ibuki, Female Staff
"初号機、活動停止！\n\0":
'???',

# Maya Ibuki, Female Staff
"弐号機、活動停止！\n\0":
'???',

# Maya Ibuki, Female Staff
"参号機、活動停止！\n\0":
'???',

# Maya Ibuki, Female Staff
"四号機、活動停止！\n\0":
'???',

#
# ./USRDIR/event/b2s24.har_EXTRACT/b2s24.evs
#
# Misato Katsuragi 
"ちょっと、アスカってば！！\n弐号機はＢ型装備なんだから、\n海の中じゃ勝手がきかないのよ！\n\0":
'???',

# Ritsuko Akagi 
"アスカ…、何て無茶を！！\n弐号機はＢ型装備なのよ、\n海の中じゃ動けないわ！\n\0":
'???',

# Female Staff
"弐号機はＢ型装備なんですよ！？\n水中での戦闘は無理です！\n\0":
'???',

# Asuka Soryu Langley
"ケーブルついてりゃ、\n何とかなるわよ！\n\0":
'???',

#
# ./USRDIR/event/b2s25.har_EXTRACT/b2s25.evs
#
# Shinji Ikari
"様子をうかがってる…。\nこっちは向こうみたいに\n動けないんだ、不利だよ…。\n\0":
'???',

# Asuka Soryu Langley
"どうせ、使徒の狙いはこの弐号機よ。\n向こうが接近した時が\n攻撃のチャンス！▽\n攻撃範囲内に使徒が接近した時、\n%1iボタンでナイフを振れば…。\nダメージを与えられるハズ！\n\0":
'???',

# Shinji Ikari
"う、うまくいくのかなぁ…。\n\0":
'???',

# Asuka Soryu Langley
"何もやらないよりは、\nマシでしょ。\nホラ、来るわよ！！\n\0":
'???',

# Asuka Soryu Langley
"何もやらないよりは、\nマシだわ。\nさあ、かかってらっしゃい！\n\0":
'???',

#
# ./USRDIR/event/b2s26.har_EXTRACT/b2s26.evs
#
# Misato Katsuragi 
"駄目だわ、間に合わない！！\n\0":
'???',

# Shinji Ikari
"ミサトさん！\n弐号機の耐久力が、もう…。\n\0":
'???',

# Misato Katsuragi 
"何ですって…！▽\nアスカ！\nシンジ君！！\n\0":
'???',

#
# ./USRDIR/event/b2s27.har_EXTRACT/b2s27.evs
#
# Asuka Soryu Langley
"ダメ…！\n弐号機の耐久力がもう…。\n\0":
'???',

# Misato Katsuragi 
"何ですって…！\n\0":
'???',

# Ritsuko Akagi 
"もう、限界なの！？\nそんな…。\n\0":
'???',

# Female Staff
"それじゃ、もう…。\n他に手はない…。\n\0":
'???',

#
# ./USRDIR/event/b2s28.har_EXTRACT/b2s28.evs
#
# Shinji Ikari
"ど、どうすればいいの。\nミサトさんっ！\n\0":
'???',

# Ryoji Kaji
"まるで釣りだな。\n\0":
'???',

# Misato Katsuragi 
"…釣り！？\nそうだわ…。▽\nアスカ、シンジ君。\nよく聞いて！\n\0":
'???',

# Misato Katsuragi 
"これから戦艦２隻を自沈させて、\n使徒の体内に突入させます。▽\n艦首主砲塔の直接砲撃、更に自爆、\n目標を撃破します。▽\nあなた達は、それまでに\n目標の口を開口させるのよ！\n\0":
'???',

# Asuka Soryu Langley
"オッケー、ミサト！！▽\nアンタ、聞いた？\n使徒の口を開けさせるの。\nそれだけに専念しなさいよ！\n\0":
'???',

#
# ./USRDIR/event/b2s29.har_EXTRACT/b2s29.evs
#
# Shinji Ikari
"た、食べられたの！？\n\0":
'We got eaten?!\n\0',

# Asuka Soryu Langley
"いや〜〜〜〜ん！！\n\0":
'???',

# Asuka Soryu Langley
"どうすればいいのよ〜。\n\0":
'What do we dooo?\n\0',

# Misato Katsuragi 
"あぁぁ…、まるで釣りだわ。\n\0":
'Huh... It\'s just like fishing.\n\0',

# Misato Katsuragi 
"…釣り！？\nそうだわ…。▽\nアスカ、よく聞いて！\n\0":
'...Fishing?!\nThat\'s it.▽\nAsuka, listen carefully!\n\0',

# Misato Katsuragi 
"これから戦艦２隻を自沈させて、\n使徒の体内に突入させます。▽\n艦首主砲塔の直接砲撃、更に自爆、\n目標を撃破します。▽\nそれまでに、弐号機で\n目標の口を開口させるのよ！\n\0":
'???',

# Female Staff
"まるで釣りだわ。\n\0":
'It\'s just like fishing.\n\0',

# Female Staff
"…釣り！？\nそう、この方法なら…。▽\nアスカさん、いいですか？\n\0":
'???',

# Female Staff
"これから戦艦２隻を自沈させて、\n使徒の体内に突入させます。▽\n艦首主砲塔の直接砲撃、更に自爆、\n目標を撃破します。▽\nそれまでに、弐号機で\n目標の口を開口させてください！\n\0":
'???',

# Asuka Soryu Langley
"オッケー！！\n使徒の口を開けさせるのね！\n\0":
'???',

# Shinji Ikari
"それしか方法は無いんだろっ！\nよぉし…。\n\0":
'???',

# Asuka Soryu Langley
"開け、開け、開け…。\n\0":
'Open, open, open...\n\0',

# Shinji Ikari
"開け、開け、開けッ！！\n\0":
'Open, open, open!!\n\0',

#
# ./USRDIR/event/b2s30.har_EXTRACT/b2s30.evs
#
# Ritsuko Akagi 
"間に合わない！？\n\0":
'???',

# Female Staff
"やっぱり…、無理？\n間に合わないわ！！\n\0":
'???',

#
# ./USRDIR/event/b2s31.har_EXTRACT/b2s31.evs
#
# Misato Katsuragi 
"撃て！！\n\0":
'Fire!!\n\0',

# Female Staff
"砲撃開始！！\n\0":
'Commence bombardment!!\n\0',

# Shinji Ikari
"くっそおおおぉぉぉ！\n\0":
'???',

# Asuka Soryu Langley
"開けぇぇぇぇぇえ！！\n\0":
'Ooopen uuuuup!!\n\0',

#
# ./USRDIR/event/b2s32.har_EXTRACT/b2s32.evs
#
# Ritsuko Akagi, Misato Katsuragi 
"捕獲作戦は中止、使徒殲滅を\n最優先に！▽\n撤収作業をしつつ、\n戦闘準備！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ初号機、限界深度、オーバー。\nプラス１００、…２００。\n\0":
'???',

# Female Staff
"捕獲作戦は中止、使徒殲滅を\n最優先に！▽\n戦闘準備に移ります！\n\0":
'???',

# Maya Ibuki, Female Staff
"第２循環パイプ、\n及びエヴァ各部に亀裂発生。\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ弐号機、限界深度、オーバー。\nプラス１００、…２００。\n\0":
'???',

# Shinji Ikari
"こ、この状態で！？\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ零号機、限界深度、オーバー。\nプラス１００、…２００。\n\0":
'???',

# Asuka Soryu Langley
"待ってました！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ参号機、限界深度、オーバー。\nプラス１００、…２００。\n\0":
'???',

# Ritsuko Akagi 
"まずいわ！\n孵化を始めたのよ。\n予測より早すぎるわ！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ四号機、限界深度、オーバー。\nプラス１００、…２００。\n\0":
'???',

# Toji Suzuhara 
"んな、無茶苦茶ですわ！\n…っか〜、しゃーない。\nハラ決めたるわ！！\n\0":
'???',

# Makoto Hyuga, Male Staff
"これ以上は無理です！\n機体が持ちません！\n\0":
'???',

# Shinji Ikari
"あれだ…。\nあれが使徒だ…。\n\0":
'???',

# Asuka Soryu Langley
"いた。\nいたわ、使徒よ…。\n\0":
'???',

# Male Staff
"まずい！\n使徒が孵化を始めました！\n計算より早いです！\n\0":
'???',

# Rei Ayanami 
"了解！\n\0":
'???',

# Rei Ayanami 
"こちら、零号機。\n使徒を発見しました。\n\0":
'???',

# Toji Suzuhara 
"おった！\nここにいてます。\n使徒です。\n\0":
'???',

# Kaworu Nagisa 
"四号機です。\n使徒を発見しました。\n\0":
'???',

# Misato Katsuragi, Ritsuko Akagi 
"捕獲準備！\n\0":
'???',

# Male Staff
"捕獲準備を！\n\0":
'???',

# Ritsuko Akagi 
"対流で流されているから、\n接触できるチャンスは１度きりよ！\n\0":
'???',

# Misato Katsuragi 
"いい？\n対流で流されているから、\n接触できるチャンスは１度きりよ！\n\0":
'???',

# Female Staff
"対流で流されています。\n接触できるチャンスは１度きりです。\n\0":
'???',

# Shinji Ikari
"はい。▽\n軸線にのったぞ…。\n電磁柵、展開………！？▽\nえっ…、な、何だ！？\n\0":
'???',

# Asuka Soryu Langley
"わかってるわ。▽\n軸線にのったわ。\n電磁柵、展開………！？▽\nな、何よコレェ！？\n\0":
'???',

# Rei Ayanami 
"了解。▽\n電磁柵、展開………！？▽\n待って！\n使徒に変化が…。\n\0":
'???',

# Toji Suzuhara 
"ほな、行きまっせ。▽\n電磁柵、展開………！？▽\nあん！？\nちょ、ちょっと…何や！？\n何が起こってん！？\n\0":
'???',

# Kaworu Nagisa 
"了解。▽\n電磁柵、展開します。▽\nこれは…？\nまずい、目覚めた！？\n\0":
'???',

#
# ./USRDIR/event/b2s33.har_EXTRACT/b2s33.evs
#
# Misato Katsuragi 
"気をつけて、アスカ。▽\n攻撃のタイミングを外すと、\n目標との接触タイミングを\n見失うわよ！\n\0":
'???',

#
# ./USRDIR/event/b2s34.har_EXTRACT/b2s34.evs
#
# Shinji Ikari
"見通しが悪いし、\n何より自由に動けない。▽\n攻撃範囲内に来るのを待って、\n%1iボタン。\nナイフで攻撃するしかないか。\n\0":
'???',

# Asuka Soryu Langley
"チョロチョロ動き回ってェ、もぉ！▽\n攻撃範囲内に来るのを待って、\n%1iボタン。\nナイフで攻撃するしかないわね。\n\0":
'???',

# Rei Ayanami 
"攻撃範囲内に来るのを待って、\n%1iボタン。\nナイフで攻撃するしかないわ。\n\0":
'???',

# Toji Suzuhara 
"ホンマ、ハエみたいに\n動き回りよってからに〜！▽\n攻撃範囲内に来るんを待って、\n%1iボタン。\nナイフで攻撃するしかないか。\n\0":
'???',

# Kaworu Nagisa 
"攻撃範囲内に来るのを待って、\n%1iボタン…。\nナイフで攻撃するしかないか。\n\0":
'???',

# Misato Katsuragi 
"気をつけて。▽\n攻撃のタイミングを外すと、\n目標との接触タイミングを\n見失うわよ！\n\0":
'???',

# Ritsuko Akagi 
"気をつけて。▽\n攻撃のタイミングを外すと、\n目標との接触タイミングを\n見失う事になるわ！\n\0":
'???',

# Female Staff
"攻撃のタイミングを外すと、\n目標との接触タイミングを\n見失います！▽\n気をつけてください。\n\0":
'???',

#
# ./USRDIR/event/b2s35.har_EXTRACT/b2s35.evs
#
# Shinji Ikari
"アスカ、アレだよっ！\n熱膨張！\n\0":
'???',

# Asuka Soryu Langley
"そっか！\nシンジも勉強した甲斐が\nあるじゃん！！\n\0":
'???',

# Asuka Soryu Langley
"冷却液の循環パイプ、\n切断します！\n\0":
'???',

#
# ./USRDIR/event/b2s36.har_EXTRACT/b2s36.evs
#
# Shinji Ikari
"駄目だ。\nナイフじゃ、太刀打ちできない。\n\0":
'???',

# Asuka Soryu Langley
"んもぅ！！\n傷一つ、つけられないの？\n\0":
'???',

# Rei Ayanami 
"このままでは、\n火口に到達してしまう…。\n\0":
'???',

# Toji Suzuhara 
"いい加減に勘弁したれよ！\nどないなっとんねん、\nお前の身体は！？\n\0":
'???',

# Kaworu Nagisa 
"駄目だ、分が悪い。\n機体もそろそろ\nこの環境では…。\n\0":
'???',

# Ritsuko Akagi 
"高温高圧、コレだけの極限状態に\n耐えているのよ。\nプログナイフじゃ駄目だわ。\n\0":
'???',

# Female Staff
"高温高圧の極限状態に耐えている。\nそんな相手にナイフだけでは…。\n\0":
'???',

# Shinji Ikari
"もう、火口だ。\n時間がない…。\n\0":
'???',

# Shinji Ikari
"そうだ、熱膨張…。\n冷却液の循環パイプを使って！\n\0":
'???',

# Asuka Soryu Langley
"そろそろ、火口付近だわ。\nどーすりゃいいのよ。\n\0":
'???',

# Asuka Soryu Langley
"そうだ、これなら上手くいくかも。\n冷却液の循環パイプ、\n切断します！\n\0":
'???',

# Rei Ayanami 
"あまり残り時間がない。\nどうすれば…。\n\0":
'???',

# Rei Ayanami 
"零号機、冷却液の循環パイプを\n切断します！\n\0":
'???',

# Toji Suzuhara 
"あぁ…、アカン。\nそろそろ火口付近や。\n\0":
'???',

# Toji Suzuhara 
"せや、確か理科で習ぅた…。\nイチかバチかじゃ！\nこの冷却液の循環パイプを使ぅて…。\n\0":
'???',

# Kaworu Nagisa 
"こいつを外に出すわけには…。\nだが、どうやって？\n\0":
'???',

# Kaworu Nagisa 
"この方法なら…。\nこの冷却液の循環パイプで…。\n\0":
'???',

# Ritsuko Akagi 
"なるほど。\n冷却液を使徒の体内にねじ込むのね。\n\0":
'???',

# Male Staff
"なるほど。\n冷却液を使徒の体内にねじ込むのか。\n\0":
'???',

#
# ./USRDIR/event/b2s37.har_EXTRACT/b2s37.evs
#
# [Battle Event: Sandalphon/Coolant]
#
# Asuka Soryu Langley
"アンタとは、\nここでお別れよッ！！\n\0":
'???',

# Rei Ayanami 
"冷却液の圧力を全て３番に！\n\0":
'???',

# Kaworu Nagisa 
"このチャンスを逃してなるか！\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley
"冷却液の圧力を全て\n３番に回して、早くっ！\n\0":
'???',

# Toji Suzuhara 
"冷却液の圧力を全部３番に\n回してください、早ぅ！\n\0":
'???',

# Shinji Ikari
"やった、効いてる！！\n\0":
'???',

# Kaworu Nagisa 
"冷却液の圧力を全て\n３番に回してください。\n急いで！\n\0":
'???',

# Toji Suzuhara 
"よっしゃあ！！\n\0":
'???',

#
# ./USRDIR/event/b2s38.har_EXTRACT/b2s38.evs
#
# Shinji Ikari, Toji Suzuhara
"綾波！！\n\0":
'???',

# Shinji Ikari
"トウジ！！\n\0":
'???',

# Shinji Ikari
"アスカ！！\n\0":
'???',

#
# ./USRDIR/event/b2s39.har_EXTRACT/b2s39.evs
#
# Asuka Soryu Langley
"フィフス！！\n\0":
'???',

# Asuka Soryu Langley, Hikari Horaki
"鈴原！！\n\0":
'???',

# Asuka Soryu Langley
"シンジ！！\n\0":
'???',

#
# ./USRDIR/event/b2s40.har_EXTRACT/b2s40.evs
#
# Rei Ayanami 
"フィフス！\n\0":
'Fifth!\n\0',

# Rei Ayanami, Kaworu Nagisa
"セカンド！！\n\0":
'Second!!\n\0',

# Toji Suzuhara , Shinji Ikari, Kaworu Nagisa, Asuka Soryu Langley, Rei Ayanami, Misato Katsuragi, Gendo Ikari, Kozo Fuyutsuki, Ritsuko Akagi, Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Ryoji Kaji, Hikari Horaki, Kensuke Aida, Male Staff
"…！？\n\0":
'???',

# Rei Ayanami 
"鈴原君！！\n\0":
'Suzuhara-kun!!\n\0',

# Rei Ayanami 
"碇君！！\n\0":
'Ikari-kun!!\n\0',

#
# ./USRDIR/event/b2s41.har_EXTRACT/b2s41.evs
#
# Toji Suzuhara 
"カヲル！\n\0":
'???',

# Toji Suzuhara 
"惣流ー！\n\0":
'???',

#
# ./USRDIR/event/b2s43.har_EXTRACT/b2s43.evs
#
# Shinji Ikari
"アスカーーーーー！！\n\0":
'???',

# Shinji Ikari
"綾波！！\n綾波ーーー！！\n\0":
'???',

# Shinji Ikari
"トウジッ！！\n\0":
'Toji!!\n\0',

#
# ./USRDIR/event/b2s45.har_EXTRACT/b2s45.evs
#
# Kaworu Nagisa 
"くっ…。\nライフラインが…。\n\0":
'???',

#
# ./USRDIR/event/b2s46.har_EXTRACT/b2s46.evs
#
# Toji Suzuhara 
"シンジー！！\n\0":
'???',

# Toji Suzuhara 
"惣流！！！\n惣流ーーー！\n\0":
'???',

# Toji Suzuhara 
"綾波！！\n綾波ー！！\n\0":
'???',

# Toji Suzuhara 
"カヲル！\nカヲルー！！\n\0":
'???',

#
# ./USRDIR/event/b2s47.har_EXTRACT/b2s47.evs
#
# Shinji Ikari
"勝ったのに。\nせっかく勝てたっていうのに…。\n\0":
'???',

# Asuka Soryu Langley
"せっかくやったのに。\nヤだな、ここまでなの…。\n\0":
'???',

# Kaworu Nagisa 
"セカンドー！！\n\0":
'Second!!\n\0',

# Rei Ayanami 
"…ワイヤーが。\n\0":
'???',

# Toji Suzuhara 
"ちょ…、それはないやろー！！\n\0":
'???',

# Kaworu Nagisa 
"トウジ君！！\n\0":
'Toji-kun!!\n\0',

#
# ./USRDIR/event/b2s48.har_EXTRACT/b2s48.evs
#
# Asuka Soryu Langley
"バカシンジ…。\n無理しちゃって…。\n\0":
'???',

# Shinji Ikari
"アスカッ！\n大丈夫だから、\n絶対大丈夫だからっ！！\n\0":
'???',

# Misato Katsuragi 
"やった！\nやったわ、シンジ君！\n\0":
'We did it!\n We did it, Shinji-kun!\n\0',

#
# ./USRDIR/event/b2s49.har_EXTRACT/b2s49.evs
#
# Shinji Ikari
"綾波ッ！\n大丈夫だから、\n絶対大丈夫だからっ！！\n\0":
'???',

# Shinji Ikari
"トウジ！！\n大丈夫だから、\n絶対大丈夫だからっ！！\n\0":
'???',

# Shinji Ikari
"カヲル君！！\n大丈夫だから、\n絶対大丈夫だからっ！！\n\0":
'???',

# Rei Ayanami 
"…私を…助けてくれた。\n\0":
'???',

#
# ./USRDIR/event/b2s50.har_EXTRACT/b2s50.evs
#
# Asuka Soryu Langley
"シンジ！！\n最後の最後にヘマやってんじゃ\nないわよ！\n\0":
'???',

# Asuka Soryu Langley
"ファースト！\n最後の最後にヘマやってんじゃ\nないわよ！\n\0":
'???',

# Asuka Soryu Langley
"鈴原！！\n最後の最後にヘマやってんじゃ\nないわよ！\n\0":
'???',

# Asuka Soryu Langley
"フィフス！！\n最後の最後にヘマやってんじゃ\nないわよ！\n\0":
'???',

#
# ./USRDIR/event/b2s51.har_EXTRACT/b2s51.evs
#
# Rei Ayanami 
"碇君。\n間に合ってよかった…。\n\0":
'???',

# Rei Ayanami 
"セカンド！！\n間に合ってよかった…。\n\0":
'???',

# Rei Ayanami 
"鈴原君！！\n間に合ってよかった…。\n\0":
'???',

# Rei Ayanami 
"フィフス！\n間に合ってよかった…。\n\0":
'???',

# Misato Katsuragi 
"やった！\nやったわ！\n\0":
'???',

# Ritsuko Akagi 
"すごいわ…。\nまさに奇跡ね。\n\0":
'???',

# Female Staff
"間に合った。\n二機とも無事です！\n\0":
'???',

# Shinji Ikari
"…た、助かった。\n\0":
'???',

# Asuka Soryu Langley
"バカ…。\n無理しちゃって…。\n\0":
'???',

# Toji Suzuhara 
"ひーん…。\nこれがホンマの地獄に仏やわ〜。\n\0":
'???',

# Kaworu Nagisa 
"僕を…？\n君は、自分の命をかけてまで\n僕を…。\n\0":
'???',

#
# ./USRDIR/event/b2s52.har_EXTRACT/b2s52.evs
#
# Toji Suzuhara 
"シンジ、\nヒヤヒヤさせんなや。\n\0":
'???',

# Toji Suzuhara 
"惣流！！\nヒヤヒヤさせんなや。\n\0":
'???',

# Toji Suzuhara 
"綾波！！\nヒヤヒヤさせんなや。\n\0":
'???',

# Toji Suzuhara 
"カヲル！\nヒヤヒヤさせんなや。\n\0":
'???',

#
# ./USRDIR/event/b2s53.har_EXTRACT/b2s53.evs
#
# Kaworu Nagisa 
"シンジ君！！\nもう、大丈夫だよ。\n\0":
'Shinji-kun!\nYou\'re alright now!\n\0',

# Kaworu Nagisa 
"セカンド！！\nもう、大丈夫だよ。\n\0":
'???',

# Kaworu Nagisa 
"ファースト！\nもう、大丈夫だよ。\n\0":
'???',

# Kaworu Nagisa 
"トウジ君！！\nもう、大丈夫だよ。\n\0":
'???',

#
# ./USRDIR/event/b2s56.har_EXTRACT/b2s56.evs
#
# Misato Katsuragi 
"しかし、アダムとエヴァの接触は\nサードインパクトを引き起こす\n可能性が！▽\nあまりに危険です！\n碇司令、止めてください！\n\0":
'???',

# Misato Katsuragi 
"うそ、欺瞞なのね。\nセカンドインパクトは\n使徒の接触が原因ではないのね。\n\0":
'???',

#
# ./USRDIR/event/b2s57.har_EXTRACT/b2s57.evs
#
# Gendo Ikari
"本作戦において、\nロンギヌスの槍を使用する。▽\nレイ、ドグマを降りて\n槍を使え。\n\0":
'???',

# Gendo Ikari
"他は地上にて待機だ。▽\n使徒の出方を見ながら\n対空迎撃戦の用意！\n大遠距離射撃、準備！\n\0":
'???',

#
# ./USRDIR/event/b2a00.har_EXTRACT/b2a00.evs
#
# Shigeru Aoba, Male Staff
"使徒落下予想範囲、更新します！\n\0":
'???',

#
# ./USRDIR/btl/b2event.har_EXTRACT/b2a01.evs
#
# Shigeru Aoba, Male Staff
"使徒落下最終予想範囲、出ました！\n\0":
'???',

#
# ./USRDIR/event/f088.har_EXTRACT/f088.evs
#
# Ritsuko Akagi 
"今、サード・チルドレンは\nどうしてるの？\n\0":
'How is the Third\nChild doing now?\n\0',

# Misato Katsuragi 
"ぐっすり寝ているわ、私の家で。\nそろそろ起きる頃ね。\n\0":
'???',

# Ritsuko Akagi 
"いい？　わかってるでしょうけど\nエヴァを動かすには、パイロットの\nΑΤの状態が大きく作用するの。▽\n彼のΑΤ高くしときなさいよ！\n\0":
'???',

# Misato Katsuragi 
"それは、彼次第よ。\n\0":
'???',

# Ritsuko Akagi 
"それじゃ、あなたの監督する\n意味がないでしょ！▽\nま、一緒に生活する事が\n逆効果にならない事を祈るわ…。\n\0":
'???',

# Misato Katsuragi 
"ΑΤを上げる基本は\n良好な人間関係か…。\n覚えておくわ。\n\0":
'???',

# Ritsuko Akagi 
"忘れないでね。\n人類の未来もミサト次第よ！\n\0":
'???',

# Misato Katsuragi 
"おはようシンジ君、\n昨夜はよく眠れた？\n\0":
'Morning, Shinji-kun.\n Did you sleep well last night?\n\0',

# Shinji Ikari
"…はい、何とか。\n\0":
'???',

# Misato Katsuragi 
"あらためてよろしく。\n私は葛城ミサト。▽\nシンジ君、あなたは今日から\n私と一緒に生活するのよ。\n\0":
'???',

# Shinji Ikari
"カツラギ、さん…。\n\0":
'???',

# Misato Katsuragi 
"ミサトでいいわ。\nここはあなたの家なんだから、\n遠慮するこたぁないのよ。\n\0":
'???',

# Shinji Ikari
"はい、ミサトさん…。\n\0":
'???',

# Misato Katsuragi 
"あなたはエヴァのパイロットとして、\n今後、この家で生活してもらいます。▽\nモチロン、学生なんだから\n学校にも行ってもらうわよ。▽\nネルフの任務が優先されるけど、\nそれ以外の時は自由に行動して\n構わないわ。\n\0":
'???',

# Misato Katsuragi 
"外へのドアはそこから行けるの。\nこことネルフだったら、\n自由に行き来して構わないわ。▽\n学校は転入届を出しておくから\nもうチョッチ待ってネ。\n\0":
'???',

# Shinji Ikari
"じゃあ、僕はまず\n何をすればいいんですか？\n\0":
'???',

# Misato Katsuragi 
"さっきも言ったでしょ。\nあなたの好きなように\n行動して構わないわ！\n\0":
'???',

# Misato Katsuragi 
"ただし、明日行われる戦闘訓練まで、\nしっかりΑΤを上げること。\n目標はΑΤ５０以上、いいわね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"色んな人、場所の前で\n%1iボタンを押して下さい。▽\nその場の状況で、\n様々な行動を行う事が出来ます。▽\nまた、他の人達と仲が良くなると\n自分のΑΤを上げることができます。▽\n明日行われる戦闘訓練まで、\nがんばってΑΤを上げて下さい。\n\0":
'???',

#
# ./USRDIR/event/f091.har_EXTRACT/f091.evs
#
# Misato Katsuragi 
"昨日のシミュレーションは\nどうだった？\n操縦のコツはつかめたかしら？\n\0":
'???',

# Shinji Ikari
"あんなのでいいのか\n自信がまだ…。\n\0":
'???',

# Misato Katsuragi 
"あなたなら大丈夫、\nすぐに上手くなるわ。▽\nで、どう？\nここでの生活は？\n\0":
'???',

# Shinji Ikari
"…まだ、馴れないし、\nなかなか思う通りにΑΤが\n上がってくれないんです。\n\0":
'???',

# Misato Katsuragi 
"そうね、いろんな人と話したと\n思うけど、中には相手の事を\n怒らせた事もあるんじゃない？▽\n人によっては、その時の機嫌が\n悪かったり、アナタの事を良く\n思っていなかった場合があるわ。▽\nそんな時は時間をおいて、\n別な場所で話し掛けるといいのよ。▽\nもう一つアドバイス。▽\n同じ行動を繰り返すと\n相手を不快にさせたり、\nあなたへの関心は低くなっていくわ。\n\0":
'???',

# Misato Katsuragi 
"恋愛といっしょね。\nマンネリ男は嫌われるのよ。▽\n同じ行動は避け、いろんな行動で\nコミュニケーションしてネ。\n\0":
'???',

# Shinji Ikari
"わかりました…。\n\0":
'???',

# Shinji Ikari
"そういえば、ΑΤが変化しても、\n時間が経ったら勝手に元に戻って\nしまうのは何故なんですか？\n\0":
'???',

# Misato Katsuragi 
"あら、大切なこと\n伝えるのを忘れてたわ。\n\0":
'???',

# Misato Katsuragi 
"ΑΤは、いわば気分みたいなもの、\n楽しい行動で上昇し、不快な行動で\n減少する傾向にあるのよ。▽\nでも、その気分は永遠に続かずに、\n時間が経てば薄れていくの。▽\n勝手にΑΤが変化するのはそのせい。\nいわば、その人のニュートラルな\nΑΤの値に近づいていくの。\n\0":
'???',

# Misato Katsuragi 
"でも楽しい行動が多いほど、\nニュートラルなΑΤは上昇して\nいくわ。▽\nみんなと仲良くして、楽しい気分で\nいれば、あなたのニュートラルな\nΑΤもどんどん上がっていくわよ。\n\0":
'???',

# Shinji Ikari
"うまくやって行けるかな…。\n\0":
'???',

# Misato Katsuragi 
"ちょっと、さっそく\n不安な気持ちにならないの！\nΑΤが下がるわよ！\n\0":
'???',

# Misato Katsuragi 
"そうそう、今日から学校に行ける\nように手続きしといたわ。▽\n学校でも友達作って、\nしっかりΑΤ上げてちょうだい。\n\0":
'???',

#
# ./USRDIR/event/f092.har_EXTRACT/f092.evs
#
# Ritsuko Akagi 
"アラ、シンジ君。\n\0":
'Oh, Shinji-kun.\n\0',

# Shinji Ikari
"どうも…。\n\0":
'???',

# Misato Katsuragi 
"ねえ、レイは？\n退院したんでしょ？\n\0":
'???',

# Ritsuko Akagi 
"ええ、あそこで\n司令と話をしているわ。\n\0":
'???',

# Misato Katsuragi 
"レイ、ちょっと紹介するから\n来てくれる？\n\0":
'???',

# Shinji Ikari
"………？\n\0":
'???',

# Shinji Ikari
"…あの子？\n確かあの時の…。\n\0":
'???',

# Misato Katsuragi 
"彼女は、綾波レイ。\n零号機パイロットよ。\n仲良くしてあげてね。\n\0":
'???',

# Shinji Ikari
"あ、あの僕は…、碇シンジ。\nよろしく…。\n\0":
'???',

# Rei Ayanami, Kaworu Nagisa
"よろしく。\n\0":
'???',

# Ritsuko Akagi 
"零号機の修理も済んだわ。\nいつでも出撃可能よ。\n\0":
'???',

# Misato Katsuragi 
"そぉ、ゴクローサン。\nなるべくなら、しばらく使徒も\n来てほしくないんだけどね…。\n\0":
'???',

# Misato Katsuragi 
"ま、そんな事よりアンタ達さ、\n仲良くやってチョーダイ。▽\nΑΤを上げるのも大切だけど、\n人間関係も良好に。▽\n人間関係が良くなると、同じ行動\nでも相手の反応が良くなったり…、▽\n今まで出来なかった行動が\n出来るようになるわ。▽\nたとえば相手にいきなり\n抱きついちゃったりネ〜。\n\0":
'???',

# Shinji Ikari
"冗談はやめて下さい…！！\n\0":
'Please don\'t joke around!!\n\0',

# Misato Katsuragi 
"あらやだ、照れちゃってるぅ。\nま、とにかくΑΤを上げるためには\n良好な人間関係は不可欠よ。▽\nハイ、だからアンタ達は\n今日からオトモダチ〜！\nいいわね！！\n\0":
'???',

# Shinji Ikari
"…あの、\n\0":
'???',

# Shinji Ikari
"………………ハイ。\n\0":
'???',

#
# ./USRDIR/event/f094.har_EXTRACT/f094.evs
#
# [Text Only - No Designated Speaker]
"これからは、\nこの部屋がシンジの部屋です。\n\0":
'From now on, this will be Shinji\'s room.\n\0',

# [Text Only - No Designated Speaker]
"これまでシンジが生活していた\n部屋は、新たな同居人のアスカが\n使用することになりました。\n\0":
'It\'s been decided that new\n housemate Asuka will use the room\n where Shinji stayed previously.\n\0',

#
# ./USRDIR/event/f095.har_EXTRACT/f095.evs
#
# [Text Only - No Designated Speaker]
"使徒との戦闘による被害で\n第３新東京市はその都市機能を失い、\n住民は全員疎開しました。▽\nこれからの生活は、ネルフ施設の\n「宿舎の自室」で行われます。\n\0":
'???',

# [Text Only - No Designated Speaker]
"使徒との攻防で、\n第３新東京市は都市機能を失い、\n何もない廃墟と化した…。▽\n早朝だというのに、\n疎開用の大型バスが\n何台も通りすぎていく。▽\n自分も、次のバスでこの街から\n出て行かなければならない…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"陽が昇る…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"何もなかった。\n昨日まであった、あの風景。\n何もかもが消えていた。▽\n家族が手を振っている。\nもう、バスが出る時間だ。\nここへ戻る事も、もうないだろう。\n\0":
'???',

# [Text Only - No Designated Speaker]
"強い風が吹いていた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"激しい振動と爆風が\n最後の記憶だった。▽\n何が起こったのかわからなかった。▽\nただ…、▽\nいつも、窓から見る外の世界が\n何もない廃墟になっている…。▽\nそして、\n今まで過ごしていた部屋も\n何も、見当たらない…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"使徒との攻防で、\n第３新東京市は都市機能を失い、\n何もない廃墟と化したのである。▽\n自分と同じく、家を失った人間達が\n列をなして歩いている。\n皆、うつむきながら…。▽\n昔…、同じような光景を\n見たことがあった。▽\n人々が全てを奪い去られたあの日に\n似ていると思った。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そして、あの時のように\n誰かが迎えに来てくれるはずだ。▽\nそう願って、\n流れる人ごみを見つめていた…。▽\nもうすぐ、陽が昇る…。\n\0":
'???',

#
# ./USRDIR/event/f090.har_EXTRACT/f090.evs
#
# Male Staff
"パイロットにも、早く馴れて\nもらえばいいですね。\n\0":
'???',

# Misato Katsuragi 
"ちゃんとパイロットにも、\n使いこなしてもらえるかしら。\n\0":
'???',

# Makoto Hyuga, Male Staff
"支援兵器、到着しました。\n\0":
'???',

# Ritsuko Akagi 
"積み荷の点検、よろしく。\n出力の調整がまだらしいわ、\n早めにチェック可能な状態にして。\n\0":
'???',

# Female Staff
"積み荷の点検を始めましょう。▽\n出力の調整もまだですし、\n早めにチェック可能な状態に\nしておかないと。\n\0":
'???',

# Misato Katsuragi 
"マステマとデュアルソーかあ、\nとんでもない武器ね。\n\0":
'???',

# Male Staff
"マステマとデュアルソーですか…。\n\0":
'The Mastema and Dual Saw...\n\0',

# Makoto Hyuga, Female Staff
"点検が済んだら、\nいよいよ実戦配備です。\n\0":
'???',

#
# ./USRDIR/event/f089.har_EXTRACT/f089.evs
#
# [Battle Uplift: Eva Upgrades]
#
# Kozo Fuyutsuki
"本当にやるんだな…。\nゼーレに対する口実は\n用意しているのか。\n\0":
'???',

# Gendo Ikari
"実戦で証明すればいい。\n\0":
'???',

# Kozo Fuyutsuki
"現場の方は大丈夫か。\n\0":
'???',

# Gendo Ikari
"問題ない。\n全ては赤木博士にまかせてある。\n\0":
'???',

# Misato Katsuragi 
"ちょっと、これはどういう事？\n\0":
'???',

# Ritsuko Akagi 
"その資料に書かれていることが\n全てよ。▽\nエヴァの用途別特殊換装、\nありていにいえば\nエヴァのパワーアップね。\n\0":
'???',

# Misato Katsuragi 
"でも、これは…、\n汎用性を犠牲にした特殊装甲、\n何と戦うつもりなの！\n\0":
'???',

# Ritsuko Akagi 
"…。▽\n安心して、作業は大方終了。\n次の戦闘には間に合わせるわ。\n\0":
'???',

# Shigeru Aoba
"このスペックは一体…。\n\0":
'???',

# Makoto Hyuga
"どうしたっていうんだろう？\n初号機は白兵戦に特化、\n弐号機は筋肉強化…。▽\n零号機にいたってはΑΤの\n積極的中和を行う仕様だよ…。\n\0":
'???',

# Maya Ibuki 
"わ、私は何も聞いてません…。\n\0":
'???',

# Shinji Ikari
"ねえ、アスカは聞いた？\n\0":
'???',

# Asuka Soryu Langley
"エヴァの改装のこと？\n今より強くなるんでしょ。▽\nまあ、パワーアップ出来て\nよかったじゃない。\n\0":
'???',

# Shinji Ikari
"どんな風になるのかなあ…。\n\0":
'???',

# Rei Ayanami 
"作業はほぼ終了しているそうよ。\n次の戦闘には新しい機体で\n出撃出来るわ。\n\0":
'???',

#
# ./USRDIR/event/f067.har_EXTRACT/f067.evs
#
# [Text Only - No Designated Speaker]
"出張計画書の内容に従い、\n京都へ出張した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"京都で指定された場所で待って\nいると、協力者と名乗る女が現われ、\n密かに封筒を手渡した。▽\n受け取った封筒には、\nマルドゥック機関に関係する\n情報が入っていた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"マルドゥック機関に関する情報が、\n最深度情報にあがりました。\n\0":
'???',

#
# ./USRDIR/event/f068.har_EXTRACT/f068.evs
#
# [Text Only - No Designated Speaker]
"出張計画書の内容に従い、\nアメリカへ出張した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"現地の技術者の話を\n色々と聴いてまわった。▽\n話によると、\nΣ機関の研究は実験段階にまで\nこぎつけているらしい。▽\nΣ機関の安定性が保証できれば、\nいつでも実験に入れるとの事だった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"出張計画書の内容に従い、\nアメリカ支部跡を視察した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"かつてネルフ、アメリカ支部で\nあったその場所には巨大な\nクレーターだけが残されていた…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ネルフ本部で入手した\nΣ機関に関する資料を風にまいた。▽\nその書類はバラバラに、\n空高く舞い上がっていった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"Σ機関に関する情報が、\n非公開情報にあがりました。\n\0":
'???',

#
# ./USRDIR/event/f069.har_EXTRACT/f069.evs
#
# [Text Only - No Designated Speaker]
"出張計画書の内容に従い、\n南極を視察した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そこにはロンギヌスの槍を\n発掘した跡が残っていた。▽\nその跡はまるで、\n祭器を飾る祭壇のようだった。▽\nロンギヌスの槍はどのような役割を\n人類補完計画で担うのか…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ロンギヌスの槍に関する情報が、\n非公開情報にあがりました。\n\0":
'???',

#
# ./USRDIR/event/f070.har_EXTRACT/f070.evs
#
# [Text Only - No Designated Speaker]
"出張計画書の内容に従い、\n小笠原沖の視察を行った。\n\0":
'???',

# [Text Only - No Designated Speaker]
"しかし、有効な情報を\n得ることはできなかった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そこでは潜水艦らしき船の\n引き上げが行われていた。▽\n水中モニターで覗うその形状は\n今まで見た事が無く、\n青く、美しい船であった…。▽\nこれが先住民族の技術で作られた\n兵器なのか。\nそしてエヴァは…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"第一始祖民族に関する情報が、\n非公開情報にあがりました。\n\0":
'???',

#
# ./USRDIR/event/f071.har_EXTRACT/f071.evs
#
# [Text Only - No Designated Speaker]
"アスカをよく知る職員から、\n彼女に関する情報を色々聞き出した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"出張計画書の内容に従い、\nネルフ・ドイツ支部を訪問した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"出張計画書の内容に従い、\nセカンド・チルドレンが所属する\nネルフ・ドイツ支部の視察を行った。\n\0":
'???',

# [Text Only - No Designated Speaker]
"過去のデータより\nセカンド・チルドレンに\n関する情報を閲覧した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"セカンド・チルドレンをよく知る\n職員から、彼女に関する情報を\n色々聞き出した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"セカンド・チルドレンに\n関する情報が、\n最深度情報にあがりました。\n\0":
'???',

# [Text Only - No Designated Speaker]
"出張計画書の内容に従い、\nアスカが所属していた\nネルフ・ドイツ支部の視察を行った。\n\0":
'???',

#
# ./USRDIR/event/f072.har_EXTRACT/f072.evs
#
# [Text Only - No Designated Speaker]
"エヴァの構造に関する情報が、\n一般情報から非公開情報に\nあがりました。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ここは知っている、\nエヴァ素体の廃棄場所だ…。▽\n一旦引き返そう…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"何か、よく分からない巨大な\n構造物がある…脊椎のようだが？▽\nここは一旦引き返した方が\nよさそうだ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"通路の先には巨大な骨が\nたくさん横たわっている…。▽\nどうやらここはエヴァの部品、\nいや、廃棄された素体のようだ…。\n\0":
'???',

#
# ./USRDIR/event/f073.har_EXTRACT/f073.evs
#
# [Normal: Exploring Terminal Dogma]
#
# [Text Only - No Designated Speaker]
"第二使徒に関する情報が、\n非公開情報から最深度情報に\nあがりました。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ここは知っている、\nセントラルドグマ、綾波レイの\nクローン体がある部屋だ…。▽\n一旦引き返そう…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"何だろう、この部屋は？\n周囲が水槽のようだが…。▽\nここは一旦引き返した方が\nよさそうだ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"扉を開くと、そこには\n巨大な水槽らしきものがあった。▽\n水槽に近づくと、\n中に人影が見える…。▽\nそこには何人もの\n綾波レイの姿があった…。▽\nレイ達が一斉にこちらを見た。▽\n恐怖に震えながら、\n周囲にある資料を\n片っ端から読み漁った…。\n\0":
'???',

#
# ./USRDIR/event/f074.har_EXTRACT/f074.evs
#
# [Normal: Exploring Terminal Dogma]
#
# [Text Only - No Designated Speaker]
"アダムに関する情報が、\n一般情報から非公開情報に\nあがりました。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ここは知っている、\nアダムが磔にされている場所だ…。\n一旦引き返そう。\n\0":
'???',

# [Text Only - No Designated Speaker]
"これは何なんだろう？\n巨大な十字架のようだが…。\n上部は暗くてよくわからない。▽\n一旦引き返した方がよさそうだ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そこには、巨大な十字架に\n巨人の上半身…が磔られている。▽\nこれがあの…、アダム？\n\0":
'???',

#
# ./USRDIR/event/f075.har_EXTRACT/f075.evs
#
# [Normal: Central Dogma Exploration]
#
# [Text Only - No Designated Speaker]
"ここは知っている、\nダミープラグに関する研究開発が\n行われている部屋だ…。▽\n一旦引き返そう。\n\0":
'???',

# [Text Only - No Designated Speaker]
"通路の先には、\nダクトごしに研究室と\nエントリープラグが見える…。▽\n研究室に侵入し、\n資料を読み漁った…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ダミープラグに関する情報が、\n広報公開情報から一般情報に\nあがりました。\n\0":
'???',

#
# ./USRDIR/event/f076.har_EXTRACT/f076.evs
#
# [Text Only - No Designated Speaker]
"ジオフロントに関する情報が、\n一般情報から非公開情報に\nあがりました。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ここは知っている、\n生物を全く寄せ付けない空間。▽\nジオフロントの\n最下層を形成する死海だ…。▽\n一旦引き返そう。\n\0":
'???',

# [Text Only - No Designated Speaker]
"巨大な空間が広がっている…。\n地底湖だろうか？\nたくさんとがった島もある。▽\n一旦引き返した方がよさそうだ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"長い通路の先に、\n巨大な空間が目の前に広がった。▽\nそこは、巨大な塩の柱が乱立する、\n巨大な地底湖だった。\n\0":
'???',

#
# ./USRDIR/event/f001.har_EXTRACT/f001.evs
#
# [Text Only - No Designated Speaker]
"ミサトの生前の功績を称えて\n二階級特進となった。▽\n授与された階級章をミサトの\n遺影の前に置く。\n\0":
'???',

# Shinji Ikari
"おめでとう、ミサトさん。\n三佐に昇進だって。\n\0":
'???',

# Asuka Soryu Langley
"馬鹿な女。\n死んでから認められて\n何の意味があるのよ。\n\0":
'???',

# Ritsuko Akagi, Asuka Soryu Langley
"ミサト…。\n\0":
'???',

# Ryoji Kaji
"葛城…、こんな昇進よりも\nお前に生きていて欲しかったな。\n\0":
'???',

# Toji Suzuhara 
"ええ人やったな。\n綺麗で、強くて、凛々しくて。\nもう、会えへんのか…。\n\0":
'???',

# Kensuke Aida
"うぅぅー…、\n何でミサトさんが\n死ななきゃなんなかったんだ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"遺影に、ビールを供え、\n手を合わせた。▽\n遺影のミサトは\n何もなかったように笑っている。▽\nその日は、ミサトを偲んで\n食事会を開いた。\n\0":
'???',

# Shinji Ikari
"ねぇ、ミサトさんの襟章、\nいつもと違いますよ。\nひょっとして昇進ですか？\n\0":
'???',

# Asuka Soryu Langley
"ミサトもとうとう昇進か。\n若くして昇進する女は婚期を\n逃すらしいわよ〜。\n\0":
'???',

# Rei Ayanami 
"話、聞きました。\n昇進したんですね…。\n\0":
'???',

# Ritsuko Akagi 
"昇進おめでとう、ミサト。\n\0":
'???',

# Ryoji Kaji
"よぉ、昇進したんだって？\nこりゃ、ますます頭があがらなく\nなるな。\n\0":
'???',

# Toji Suzuhara 
"そないいえば、ミサトさん、\n昇進したんですか？\n\0":
'???',

# Hikari Horaki
"ミサトさん、昇進したんですね。\nおめでとうございます。\n\0":
'???',

# Kensuke Aida
"このたびは、ご昇進\nおめでとうございます！！\n\0":
'???',

# Misato Katsuragi 
"ありがとう…。\nでも、ナンかおめでたいんだか、\nおめでたくないのか…。\n\0":
'???',

# Shinji Ikari
"でも、昇進って事は、\nそれだけミサトさんが\n認められたって事でしょう？\n\0":
'???',

# Asuka Soryu Langley
"嬉しくないの？\n自分の働きがそれだけ\n認められたって事じゃない。\n\0":
'???',

# Rei Ayanami 
"あまり嬉しそうじゃ、ない。\n\0":
'???',

# Ritsuko Akagi 
"あら、嬉しくないの？\n\0":
'???',

# Ryoji Kaji
"あんまり嬉しくなさそうだな。\nどうした？\n\0":
'???',

# Toji Suzuhara 
"あれ？\n昇進、そない嬉しないんですか？\n\0":
'???',

# Hikari Horaki
"昇進、あまり嬉しくないんですか？\n\0":
'???',

# Kensuke Aida
"そんなに嬉しくないんですか？\nせっかく昇進したのに…。\n\0":
'???',

# Misato Katsuragi 
"全然嬉しくないって事はないのよ。\n\0":
'???',

# Misato Katsuragi 
"ただね、これから仕事も増える\nだろうし、責任も重くなるからね。\nチョッチ、プレッシャーよ。\n\0":
'???',

# Kensuke Aida
"よっしゃあ！\n昇進を祝って、パーッと\n祝賀パーティーをしましょう！\n\0":
'???',

# Toji Suzuhara 
"せや！\n祝賀パーティーしましょうよ！\nワシ、お好み焼き、焼きますわ！\n\0":
'???',

# Ryoji Kaji
"まぁ、せっかくなんだ。\nお祝いのパーティーでもしよう。\n俺、ビール買って来るわ。\n\0":
'???',

# Ritsuko Akagi 
"どっちにしろ、おめでたい事よ。\n久しぶりに飲まない？\nお祝いのパーティーなんて、どう？\n\0":
'???',

# Asuka Soryu Langley
"いいじゃん、いいじゃん。\nせっかくだし、パーティーしない？\n昇進祝いパーティーよ。\n\0":
'???',

# Shinji Ikari
"じゃ、今夜はパーティーしましょう。\n大した物は作れませんけど、僕が\n料理します。\n\0":
'???',

# Hikari Horaki
"そうだ！お祝いしましょう。\nせっかくですもの、パーッと\nミサトさんの昇進を祝いましょうよ。\n\0":
'???',

# Rei Ayanami 
"それじゃ、私からもお祝い。\n何か出来る事をやらせて下さい。\n\0":
'???',

# [Text Only - No Designated Speaker]
"１時間後…。\n\0":
'???',

# Pen Pen
"クゥ〜〜〜〜〜〜〜〜〜、\n………………ゲフゥッ。\n\0":
'???',

# Shinji Ikari
"ペンペン、ビールばっかり飲んじゃ\nお腹壊すぞ。\n\0":
'???',

# Asuka Soryu Langley
"ペンペン、ビール飲み過ぎで\nお腹壊してもしらないわよ。\n\0":
'???',

# Rei Ayanami 
"あなた、ビール飲むのね。\n\0":
'???',

# Ritsuko Akagi 
"ペンギンがビール飲んで\n大丈夫なのかしら。\n\0":
'???',

# Ryoji Kaji
"よぅ、ペン公。\nいい飲みっぷりだな。\nホント、ご主人様そっくりだ。\n\0":
'???',

# Toji Suzuhara 
"うへぇ〜、ペンギンがビール\n飲むんかいな…。\n\0":
'???',

# Hikari Horaki
"ペンペン、ビールなんか飲んで\n大丈夫かしら？\n\0":
'???',

# Kensuke Aida
"あっという間にビールのイッキ飲み。\nペンギンなのに、威勢のいい奴…。\n\0":
'???',

# Misato Katsuragi 
"この子は私の晩酌相手なの。\nね〜、ペンペン。\n\0":
'???',

# Pen Pen
"ギャ！\n\0":
'???',

# Toji Suzuhara 
"よっしゃー、鈴原トウジ、\n隠し芸しまーす！！\n\0":
'???',

# Asuka Soryu Langley
"どーせ、腹芸でしょ。\n\0":
'???',

# Toji Suzuhara 
"な、何でわかるんや…？\n\0":
'???',

# Asuka Soryu Langley
"アンタ、掃除の時間にいっつも\nやってるからよ。\nホント、ガキね。見飽きたわ。\n\0":
'???',

# Toji Suzuhara 
"腹だけやないぞ、本日大サービス！\n尻も使うで〜〜〜〜！！\n\0":
'???',

# Asuka Soryu Langley
"ギャーーーーーーーーーーー！！\nこの、ヘンターーーーーーイ！！\n\0":
'???',

# Ritsuko Akagi 
"こんなざっくばらんなパーティーは\n大学時代以来ね。\n\0":
'???',

# Ryoji Kaji
"そうだったな…。\nでも、コンパにはあまり顔を\n出したりしなかったじゃないか。\n\0":
'???',

# Ritsuko Akagi 
"あの頃はね、飲んで騒ぐというのが\n好きになれなかったの。\nバカみたいって思って。\n\0":
'???',

# Ryoji Kaji
"そう？\nお喋りになるのが\n怖かったんじゃないか？\n\0":
'???',

# Ritsuko Akagi 
"あなたのそういうところも\n好きになれなかったわ。\n\0":
'???',

# Ryoji Kaji
"じゃ、今は…？\n\0":
'???',

# Ritsuko Akagi 
"馬鹿ね…。\n\0":
'???',

# Ryoji Kaji
"イテテテテッ！？\nそう、つねるなよ…。\n\0":
'???',

# Ritsuko Akagi 
"ミサト、飲んでる…？\n\0":
'???',

# Misato Katsuragi 
"あ、うん…。\n\0":
'???',

# Ritsuko Akagi 
"これからタイヘンね。\n\0":
'???',

# Misato Katsuragi 
"わかってるわよ…。\n\0":
'???',

# Ritsuko Akagi 
"今日はお喋りじゃないのね。\n\0":
'???',

# Misato Katsuragi 
"そうかもね。\nかなり飲んでるからかしら。\n\0":
'???',

# Ritsuko Akagi 
"安心したわ。\nあなた、何かあると無理に\nはしゃごうとするから。\n\0":
'???',

# Misato Katsuragi 
"へいへい、よくご存知で。\nそれよか、今日はアンタの方が\nお喋りね。\n\0":
'???',

# Shinji Ikari
"綾波、食べてる？\n\0":
'???',

# Rei Ayanami 
"ええ。\n\0":
'???',

# Shinji Ikari
"フライドポテトばかり食べてるね。\n他にも取ろうか？\n\0":
'???',

# Rei Ayanami 
"いいの、これで。\n\0":
'???',

# Hikari Horaki
"そろそろ帰る時間かな…。\n相田君も、家で心配してるんじゃ\nない？\n\0":
'???',

# Kensuke Aida
"いや、今夜は俺一人なの。\nいつもの事さ。\n大概、家にいても一人なんだ。\n\0":
'???',

# Hikari Horaki
"ご飯とかは？\n\0":
'???',

# Kensuke Aida
"適当に買ってすませるよ。\nだけど、今日は楽しいな。\nこんな風にみんなで食事ってのが。\n\0":
'???',

# Asuka Soryu Langley
"シンジ、\nジュースなくなっちゃったわよ。\n買ってきて！\n\0":
'???',

# Shinji Ikari
"自分で行けよ…。\n\0":
'???',

# Asuka Soryu Langley
"だって、今日はアンタが\n厨房担当でしょ？▽\n客の飲み物まで気を配るのも\nアンタの仕事。\n\0":
'???',

# Shinji Ikari
"アスカは客じゃないだろ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"その日は夜遅くまで\nパーティーは続いた。▽\n主役のミサトは先につぶれて\nリビングで大の字になって\n眠っていた。▽\n起こさないように、\n静かに後片付けをして、\nそれからお開きになった。\n\0":
'???',

#
# ./USRDIR/event/f002.har_EXTRACT/f002.evs
#
# [Love Comedy: Pen Pen in Love]
#
# Shinji Ikari
"ペンペン…。\nテレビがどうしたの…？\n\0":
'???',

# Asuka Soryu Langley
"どしたの、ペンペン。\n騒がしーわね。\n\0":
'???',

# Rei Ayanami 
"喜んでるの…。\n\0":
'???',

# Ritsuko Akagi 
"あら、あなたどうしたの？\nずいぶん嬉しそうね…。\n\0":
'???',

# Ryoji Kaji
"こら、テレビにしがみついて\n何してんだ、ペンペン。\n\0":
'???',

# Toji Suzuhara 
"ペン公、何を興奮しとるんや。\n\0":
'???',

# Hikari Horaki
"ペンペンったら、\n何を興奮してるの？\n\0":
'???',

# Kensuke Aida
"引越しのＣＭじゃん。\nこれがどうしたの、ペンペン。\n\0":
'???',

# Shinji Ikari
"今度は元気なくなっちゃって。\nどうしたんだよ、ペンペン。\n\0":
'???',

# Asuka Soryu Langley
"変な子。\n今度はがっくり肩を\n落としちゃって…。\n\0":
'???',

# Rei Ayanami 
"今度は何…？\n悲しいの…？\n\0":
'???',

# Ritsuko Akagi 
"アララ、今度は悲しそう…。\n\0":
'???',

# Ryoji Kaji
"今度は悲しそーな顔して…。\n何か悪いもの食ったか？\n\0":
'???',

# Toji Suzuhara 
"あん？\n何や何や、今度はガッカリして…。\n\0":
'???',

# Hikari Horaki
"ペンペン…、今度は悲しそう。\n変ね、どうしたの…？\n\0":
'???',

# Kensuke Aida
"おいおい…。\nガッカリしてどうしたんだよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ペンペンは、何か思い立ったように\nゴミや、脱ぎ捨てた服を持って\n走った。▽\nペンペンの後をついていくと、\nゴミと衣類で作られた巣が\n出来ていた。\n\0":
'???',

# Shinji Ikari
"あっ…、ペンペン！？\n\0":
'???',

# Asuka Soryu Langley
"わっ！！\nペンペン…、アンタ…。\n\0":
'???',

# Rei Ayanami 
"これ…、あなたが？\n\0":
'???',

# Misato Katsuragi 
"わぁっ！？\nいつの間にこんな…。\n\0":
'???',

# Ritsuko Akagi 
"これは、まさか…。\n\0":
'???',

# Ryoji Kaji
"おぉっ！！\n何だこりゃ！？\n\0":
'???',

# Toji Suzuhara 
"だぁぁ、何やコレ！？\n\0":
'???',

# Hikari Horaki
"ペンペン…、何よコレ！？\n\0":
'???',

# Kensuke Aida
"わっ！！\n何だ、何だコレ！？\n\0":
'???',

# Shinji Ikari
"あれ、\nさっきのＣＭに反応してる。\n\0":
'???',

# Shinji Ikari
"この巣作り…、\nまさか、ペンペンの奴…、発情期？\n\0":
'???',

# Asuka Soryu Langley
"さっきのＣＭじゃない。\nそれにしても、こんな巣作って…。▽\nきっと発情期ね。\n\0":
'???',

# Rei Ayanami 
"発情期ね。\nそれに、さっきのＣＭに\n反応するなんて…。\n\0":
'???',

# Misato Katsuragi 
"この巣作り…。\nひょっとして、発情期？\n\0":
'???',

# Ritsuko Akagi 
"発情期…？\n\0":
'???',

# Ritsuko Akagi 
"まさか、いいえ…、\nそんな事、信じられないわ。\n\0":
'???',

# Ryoji Kaji
"ひょっとして、アイツ…。\n恋の季節かな？\n\0":
'???',

# Toji Suzuhara 
"あいつ、もしかして\nヨメはん迎える用意しとんの\nちゃうか？\n\0":
'???',

# Hikari Horaki
"ペンペンったら、\n発情期なのね…。\n\0":
'???',

# Kensuke Aida
"ややっ、あの巣はまさか…。\n発情期が来たんだな…。\n\0":
'???',

# Shinji Ikari
"そっか、恋のお相手は、\nあの犬なんだな…。\n\0":
'???',

# Asuka Soryu Langley
"ちょっと、ちょっと〜。\nアレは犬でしょ、アンタはペンギン。\n\0":
'???',

# Rei Ayanami 
"あの犬が、好きなの…？\n\0":
'???',

# Ritsuko Akagi 
"犬に恋心を抱くなんて…。\nペンペン、自分の事を\n犬だと思っているの…？\n\0":
'???',

# Ryoji Kaji
"いぃっ！？\nお前の恋の相手、犬なのかよッ！！\n\0":
'???',

# Toji Suzuhara 
"どっひぇぇーーーーー！？\nペンギンが、犬に惚れて\nどないすんじゃ！！\n\0":
'???',

# Hikari Horaki
"やだ…、\nしかも相手が犬だなんて…。\n\0":
'???',

# Kensuke Aida
"マジ！？\n犬に惚れて巣作りしてんのかよ！！\n\0":
'???',

# Shinji Ikari
"かわいそうに…。\nせめて同じ種類の犬に\n会わせてみようかな…。\n\0":
'???',

# Asuka Soryu Langley
"よっぽど思いつめてんのね。\nまー、ちょっと複雑だけど\n何とかしてあげたいかも…。\n\0":
'???',

# Rei Ayanami 
"真剣なのね。\n何とか力になりたいわ。\n\0":
'???',

# Misato Katsuragi 
"まあ、あんただって\n恋くらいはするわよね。\nうーん、犬飼うか…。\n\0":
'???',

# Ritsuko Akagi 
"ここまで特殊なペンギンとはね。\nそうね、何とかしてあげられたら\nいいのだけれど…。\n\0":
'???',

# Ryoji Kaji
"よしよし、お前のその気持ちは\n純粋なんだな。\n応援するよ、ペンペン。\n\0":
'???',

# Toji Suzuhara 
"せやなー…、ほな、\nあのテリアっちゅう犬、\nいっちょ会わせたろか。\n\0":
'???',

# Hikari Horaki
"ペンペンも恋してるんだね。\nちょっと、変だけど、\n恋が叶うといいよね…。\n\0":
'???',

# Kensuke Aida
"へぇ、そういえば\n犬の真似してるなぁ。▽\n何とか結ばれればいいよな。\n\0":
'???',

# [Text Only - No Designated Speaker]
"しばらくペンペンの身の上を\n案じながらテレビを眺めていた\nその時…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"よっぽどショックだったのか、\nペンペンは作った巣を荒らし、\n自分の部屋に走って行った…。\n\0":
'???',

#
# ./USRDIR/event/f003.har_EXTRACT/f003.evs
#
# [Love Comedy: After Initial Defeat by Israfel]
#
# Maya Ibuki 
"二人とも、やめなさい！！\n\0":
'???',

# Makoto Hyuga
"静かにしないか！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"次の出撃までに他のパイロットと\nユニゾン訓練を行い、\nユニゾン値を上げてください。▽\nユニゾン値が高い\nパイロット二人による\n同時荷重攻撃を行います。\n\0":
'???',

# Maya Ibuki, Makoto Hyuga, Female Staff
"同時刻、エヴァでこれを上陸地点にて\n阻止する作戦を立案、実行。\n\0":
'???',

# Maya Ibuki, Makoto Hyuga, Female Staff
"それと並行して、初号機の凍結を\n解除。\n\0":
'???',

# Misato Katsuragi 
"…アンタ達、いいわね、\nよく聞いて。▽\nあなた達パイロットは、\n次の出撃までにユニゾンを\n上げておくこと。▽\nユニゾンが高いパイロット\n二人による同時荷重攻撃により、\n目標を殲滅します。▽\n以上解散！\n\0":
'???',

# Shigeru Aoba
"散々な結果だな。\n\0":
'???',

# Makoto Hyuga
"完敗ですね…。\n\0":
'???',

# Maya Ibuki 
"いいとこなしですね。\n\0":
'???',

# Male Staff
"それにしても、\n派手にやられましたね…。\n\0":
'???',

#
# ./USRDIR/event/f004.har_EXTRACT/f004.evs
#
# [Love Comedy: Onsen Trip]
#
# Shinji Ikari
"あれ？\n出かけるんですか？\n\0":
'???',

# Asuka Soryu Langley
"アラ、お出かけ？\n\0":
'???',

# Rei Ayanami 
"今から、出張ですか？\n\0":
'???',

# Toji Suzuhara
"あれ、\nどっか行きはるんですか？\n\0":
'???',

# Kaworu Nagisa 
"お出かけですか？\n\0":
'???',

# Misato Katsuragi 
"そうなのよ。\n浅間山の地震研究所に\nチョッチね。\n\0":
'???',

# Ritsuko Akagi 
"この間の浅間山地震研究所よ。\n\0":
'???',

# Maya Ibuki 
"ほら、\nこの間の浅間山地震研究所よ。\n\0":
'???',

# Female Staff
"はい。\n先日、使徒が現れた浅間山まで。\n\0":
'???',

# Asuka Soryu Langley
"何しに？\n\0":
'???',

# Toji Suzuhara
"はー、何しにですか？\n\0":
'???',

# Shinji Ikari
"何しに行くんですか？\n\0":
'???',

# Rei Ayanami 
"あそこへ何を？\n\0":
'???',

# Kaworu Nagisa 
"へぇ、何をしに行くんですか？\n\0":
'???',

# Misato Katsuragi 
"向こうから被害報告が来てんの。\n一応、弁償しなきゃいけないし\nその打ち合わせってトコ。\n\0":
'???',

# Ritsuko Akagi 
"研究所から、観測機やその他多くの\n被害報告が来てるのよ。▽\n修理費用はこっち持ちだから\n手続きをしに行くのよ。\n\0":
'???',

# Maya Ibuki 
"使徒を探す時に使った観測機とか\nいろいろ弁償しなくちゃいけない\nのよ。▽\n向こうが請求金額のメドが付いた\nそうだから、ちょっと行かなくちゃ\nいけなくってね。\n\0":
'???',

# Female Staff
"金銭的な後始末ですよ。\n協力してもらったついでに、\n色々壊してしまいましたからね。\n\0":
'???',

# Kaworu Nagisa 
"ふーん…、\nさっき、温泉のパンフレットを\n見てませんでしたか？\n\0":
'???',

# Asuka Soryu Langley
"…ってゆーか、そのカバン。\nこっそり温泉行くつもり\nなんでしょ？\n\0":
'???',

# Shinji Ikari
"で、そんなカバン持って…。\n温泉ですか？\n\0":
'???',

# Toji Suzuhara
"ホンマにそれだけですかぁ？\n温泉、行くんちゃいますのん？\n\0":
'???',

# Rei Ayanami 
"それじゃあ、そのカバンは温泉に\n行くってわけじゃないんですね。\n\0":
'???',

# Misato Katsuragi 
"ぎく！！\n\0":
'???',

# Maya Ibuki 
"ちょ、ちょっと、シーッ！！\n\0":
'???',

# Female Staff
"そ、そんな事は…。\n\0":
'???',

# Shinji Ikari
"…やっぱり。\n\0":
'???',

# Asuka Soryu Langley
"ビンゴ！\n\0":
'Bingo!\n\0',

# Kaworu Nagisa 
"やっぱり温泉ですか。\n\0":
'???',

# Toji Suzuhara
"うわー、仕事より温泉が\nメインなんやないですか。\n\0":
'???',

# Rei Ayanami 
"職権乱用…。\n\0":
'???',

# Misato Katsuragi 
"とにかくこれは仕事なのよ。\n…ったくう！\n付いて来たかったら用意なさい！！\n\0":
'???',

# Ritsuko Akagi 
"…ば、馬鹿言わないの。\nもう…、何なら付いてくる？\n\0":
'???',

# Maya Ibuki 
"しーっ！！▽\n…いいじゃないのォ、私だって\nこんな時でしか温泉なんて\nいけないんだから…。\n\0":
'???',

# Maya Ibuki 
"連れてってあげるから…、\n内緒にしてよ…。\n\0":
'???',

# Female Staff
"………わかりました。\n同行しますか？\n\0":
'???',

# Shinji Ikari
"やった！　温泉か。\n\0":
'???',

# Asuka Soryu Langley
"ワーイ、ワーイ！\n温泉、温泉〜！！\n\0":
'???',

# Rei Ayanami 
"じゃあ、用意します。\n\0":
'???',

# Toji Suzuhara
"ウヒョー、もうけた！！\nほな、行きまひょ、行きまひょ！！\n\0":
'???',

# Kaworu Nagisa 
"じゃ、用意しようかな。\n\0":
'???',

# Shinji Ikari
"そういえば、温泉なんて初めてだ。\n\0":
'???',

# Kaworu Nagisa 
"ここから夕日が見えるね。\nいい眺めだ。\n\0":
'???',

# Toji Suzuhara
"そういや、隣は女湯や。\nくそー、\nどっか見えるとこないんか？\n\0":
'???',

# Asuka Soryu Langley
"うう〜ん、\n泳げちゃうくらい広いわ〜。\n\0":
'???',

# Rei Ayanami 
"気持ちいい…。\n\0":
'???',

# Misato Katsuragi 
"あがったら、ビールが楽しみね。\nあン、もう、しあわせ〜。\n\0":
'???',

# Ritsuko Akagi 
"ほんと、いい気持ち。\n疲れが取れるわ。\n\0":
'???',

# Maya Ibuki 
"極楽気分だわ…。\n幸せ、もうサイコー。\n\0":
'???',

# Female Staff
"さすがにパイロットの分は\n公費じゃ出せないわね…。\n\0":
'???',

# Toji Suzuhara
"お、お、女の声や…。\nぎょうさん入っとるようやな。\n\0":
'???',

# Shinji Ikari
"女の人っていつでも\nにぎやかなんだな。\nお風呂の中でも。\n\0":
'???',

# Kaworu Nagisa 
"向こうも羽を\n伸ばしているんだろうね。\n\0":
'???',

# Toji Suzuhara
"何か、聞こえへんか？\n\0":
'???',

# Toji Suzuhara
"だぁー！！\nさわりっこしとるんや…。\nくっそ〜、ええのう！！\n\0":
'???',

# Shinji Ikari
"さ、さわりあい………！？\n\0":
'???',

# Kaworu Nagisa 
"シンジくん、\n少しのぼせたんじゃないかい？\n\0":
'???',

# Shinji Ikari
"え、いや…。\n\0":
'???',

# Kaworu Nagisa 
"少し上がって、\n風にあたるといいよ。\n\0":
'???',

# Shinji Ikari
"うん、ありがとう…。\n\0":
'???',

# Toji Suzuhara
"風呂上がりっちゅーたら、\nやっぱコーヒー牛乳やろ。\n\0":
'???',

# Toji Suzuhara
"どうしてって、\n昔からそう決まってるやんか。\n\0":
'???',

# Kaworu Nagisa 
"聞いた事ないよ。\n\0":
'???',

# Toji Suzuhara
"こう腰に手ェやってな、\nギューってイッキ飲みするんや。\nサイコーやがな！\n\0":
'???',

# Kaworu Nagisa 
"…僕はいいよ。\n\0":
'???',

# Misato Katsuragi 
"アスカったら、発育いいわね〜。\n\0":
'???',

# Asuka Soryu Langley
"あン、くすぐったいってば。\n\0":
'???',

# Asuka Soryu Langley
"ミサトこそ、お腹はともかく\nここがたるんできたのは\nちょっと問題なんじゃない？\n\0":
'???',

# Misato Katsuragi 
"いた〜っ！\nあ、引っ張らないでよ。\n\0":
'???',

# Ritsuko Akagi 
"それにしてもいい身体ね。\n肌年齢が若いって、\n本当にうらやましいわ。\n\0":
'???',

# Asuka Soryu Langley
"キャ！？\nゾクッってした…。\n\0":
'???',

# Asuka Soryu Langley
"もう、どこ触ってんですか。\n\0":
'???',

# Ritsuko Akagi 
"フフフ、かわいいのね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"例の研究所での仕事は\nほんの数分で済んだ。▽\nほんの短い時間だったけど、\n今日はちょっとした旅行を楽しんだ。\n\0":
'???',
#
# ./USRDIR/event/f005.har_EXTRACT/f005.evs
#
# Misato Katsuragi 
"さてと…、▽\n今日は新しいパイロットと\nエヴァのお迎えだわ。\n\0":
'???',

# Ritsuko Akagi 
"今日はセカンドを迎えに行く日ね。\n\0":
'???',

# Female Staff
"今日はセカンドを\n迎えに行く日だわ。\n\0":
'???',

# Shinji Ikari
"迎えにって、\nどこに行くんですか？\n\0":
'???',

# Rei Ayanami 
"セカンド・チルドレン…、\n弐号機が実戦配備されるのね。\n今は…？\n\0":
'???',

# Maya Ibuki 
"カワイイ女の子だそうじゃ\nないですか。\n今、どこなんですか？\n\0":
'???',

# Toji Suzuhara 
"ほーぉ。\nまだパイロットっておったんや。\n迎えにって、駅かなんかですか？\n\0":
'???',

# Kaworu Nagisa 
"今は、どこへ？\n搬送中なんでしょう？\n\0":
'???',

# Misato Katsuragi 
"横須賀沖の太平洋上、国連艦隊\nオーバー・ザ・レインボウよ。\n\0":
'???',

# Ritsuko Akagi 
"太平洋上の国連艦隊よ。\n\0":
'???',

# Female Staff
"太平洋上の国連艦隊です。\nここからＶＴＯＬで\n移動する事になります。\n\0":
'???',

# Shinji Ikari
"新しい仲間が増えるのか…。\nやっぱり僕と同じ子供なのかな？\n\0":
'???',

# Rei Ayanami 
"私はここで待機ね。\n\0":
'???',

# Misato Katsuragi 
"そろそろ時間だわ。▽\n必要な書類は全部あるわね…。\n色々手続きしないといけないし、\nビールも持ったし。\n\0":
'???',

# Misato Katsuragi 
"んじゃ、行ってまいりま〜す。\n\0":
'???',

# Gendo Ikari
"では、エヴァ弐号機の引継ぎ、\n頼んだぞ。\n\0":
'???',

# Kozo Fuyutsuki
"国連艦隊の軍人には\n失礼のないようにな。▽\n奴等は頭の硬い連中だからな。\n\0":
'???',

# Ritsuko Akagi 
"みんな、留守番頼んだわよ。\n\0":
'???',

# Maya Ibuki 
"では、いってらっしゃい。\n\0":
'???',

# Makoto Hyuga
"あとは、ご心配なく。\n\0":
'???',

# Shigeru Aoba
"留守は僕らに任せて下さい。\n\0":
'???',

# Ryoji Kaji
"じゃ、アスカによろしく\n伝えといてくれ。\n\0":
'???',

# Toji Suzuhara 
"あ〜ぁ、ワイは待機かぁ。\nつまらんのー…。\n\0":
'???',

# Kaworu Nagisa 
"いってらっしゃい。\n\0":
'???',

# Asuka Soryu Langley
"あんた、バカァ？\n決まってんじゃない！\n弐号機でアイツをやっつけるのよ！\n\0":
'???',

# Misato Katsuragi 
"こーなったら、弐号機を起動させて\n使徒を撃退するしかないわ！！\nいいわね、アスカ！！\n\0":
'???',

# Ritsuko Akagi 
"急がないと次の攻撃が来るわ。▽\nアスカ、\nすぐにプラグスーツに着替えて！！\n弐号機は起動準備を。\n\0":
'???',

# Shinji Ikari
"来るよ！！\nあっ、でも武器が…。\n\0":
'???',

# Female Staff
"イチかバチか…。\nどのみちエヴァでなければ\n使徒には勝てないわ。▽\nこうなったら弐号機を\n起動させるしかないわね。\n\0":
'???',

# Asuka Soryu Langley
"とうとう、この時が来たのね。\n…アスカ、行くわよ。\n\0":
'???',

# Asuka Soryu Langley
"そ〜うこなくっちゃ！\nんじゃ、行っくわよ〜！！\n\0":
'???',

# Female Staff
"今の音、使徒からの攻撃ね。\nよりによってこの艦を\n狙ってくるなんて…。\n\0":
'???',

# Ritsuko Akagi 
"来るわ。\nでも、アスカ、あなた武器は！？\n\0":
'???',

# Shinji Ikari
"ちょっ、ちょっ、ちょっとお…。\n僕までプラグスーツに着替えて\nどうするんだよ〜。\n\0":
'???',

# Asuka Soryu Langley
"はっ！\nこんなのプログナイフがあれば\n十分よ！\n\0":
'???',

# Asuka Soryu Langley
"さぁ、かかってらっしゃい！\n三枚におろしてやるわよっ！！\n\0":
'???',

# Asuka Soryu Langley
"ハァ〜イ！\nやっとお迎えね、\n待ちくたびれたわ。▽\n船旅もいい加減、飽きてきた\nところだったのよ。\n\0":
'???',

# Misato Katsuragi 
"元気そうね、アスカ！\nようこそ、日本へ。▽\nしばらく見ないうちに\n大きくなったわね。▽\nこれからはパイロットとしての\n活躍に期待しているわよ。\n\0":
'???',

# Ritsuko Akagi, Female Staff
"あなたがエヴァ弐号機パイロット、\n惣流・アスカ・ラングレーね。\n\0":
'???',

# Asuka Soryu Langley
"港につくまで、\nあとどれくらいかしら？\n\0":
'???',

# Misato Katsuragi 
"まだ、かかるわよ。\nアンタだけＶＴＯＬで連れて\n行くわけにはいかないしね。▽\nもちっとの辛抱よ。\n\0":
'???',

# Ritsuko Akagi 
"そうね、あと何時間かよ。\nせっかくの船旅だから\n残りの時間を楽しんだら？\n\0":
'???',

# Female Staff
"夕方には。▽\nついたら今日はゆっくり\n休んで下さいね。\n\0":
'???',

# Asuka Soryu Langley
"あっそ、つまんない。▽\nんじゃ、私の弐号機でも見る？\n案内するわ。\n\0":
'???',

# Female Staff
"来るわ。\nあっ、でも武器が…。\n\0":
'???',

# Asuka Soryu Langley
"ヘロォ〜、ミサト！！\nひっさしぶりじゃない。\n元気してた？\n\0":
'???',

# Misato Katsuragi 
"モチ元気よ。\nあなたも元気そうね！\nようこそ、日本へ。▽\n彼女がエヴァ弐号機パイロット、\n惣流・アスカ・ラングレーよ。\n\0":
'???',

# Asuka Soryu Langley
"誰？\nあなたが、お迎えのヒト？\n\0":
'???',

# Ritsuko Akagi 
"あなたがアスカね。▽\n彼女がエヴァ弐号機パイロット、\n惣流・アスカ・ラングレーよ。\n\0":
'???',

# Female Staff
"あなたがアスカさんね。▽\n彼女がエヴァ弐号機パイロット、\n惣流・アスカ・ラングレーです。\n\0":
'???',

# Shinji Ikari
"よ、よろしく…。\n\0":
'???',

# Asuka Soryu Langley
"あン？\nあんた、何なのよ。\n\0":
'???',

# Shinji Ikari
"あんた？\n僕は…、碇…シンジ。▽\n初号機パイロットなんだ。\n…一応。\n\0":
'???',

# Asuka Soryu Langley
"ハーァ？\nアンタが初号機パイロット？\nウワサのサード・チルドレン？\n\0":
'???',

# Shinji Ikari
"…そう、だけど。\n\0":
'???',

# Asuka Soryu Langley
"何かつまんない子ね〜。\nこんなのがサード・チルドレン\nだなんてガッカリよ。\n\0":
'???',

# Misato Katsuragi 
"そう？\nでも、彼は訓練ナシでいきなり\n実戦でエヴァを動かしたのよ。\n\0":
'???',

# Ritsuko Akagi 
"そう？\nでも、彼は何の訓練もなしに\nエヴァを実戦で動かしたのよ。\n\0":
'???',

# Female Staff
"あら、でも…。\n彼は何の訓練もなしにエヴァを\n実戦で動かす事が出来たのよ。\n\0":
'???',

# Asuka Soryu Langley
"へーぇ、そう。\nでも、私の弐号機と比べたら\nどうかしら？\n\0":
'???',

# Asuka Soryu Langley
"私の弐号機は、\n実戦用に造られた、世界初の、\n本物のエヴァンゲリオンなのよ。▽\nアンタの初号機や零号機とは\n格が違うのよ！\n\0":
'???',

# Misato Katsuragi 
"そうそう、弐号機。\n見せてもらえるかしら？\n案内してチョーダイ。\n\0":
'???',

# Ritsuko Akagi 
"そうそう、アスカ、弐号機の\nところまで案内してくれる？▽\n大まかなチェックを\nしておきたいのよ。\n\0":
'???',

# Female Staff
"そうだわ、弐号機はどこに？\nちょっと、\n見ておきたいんだけれど…。\n\0":
'???',

# Asuka Soryu Langley
"…すぐ向こうよ。\n見せてあげるからついて来て。\n\0":
'???',

# Misato Katsuragi 
"あ〜、いった〜…。\n何なのよ…って、\nあれ、使徒じゃないの！！▽\n本部じゃなくって\nこの船を狙って…？\n\0":
'???',

# Ritsuko Akagi 
"使徒だわ…！！\nまさか、この船を…。\nそうか、弐号機が目当てなんだわ！\n\0":
'???',

#
# ./USRDIR/event/f023.har_EXTRACT/f023.evs
#
# [Love Comedy: Falling Stars]
#
# Shinji Ikari
"ねえ、\n今夜屋上に行ってみない？▽\nひょっとしたら、\n流星が見られるかもしれないよ。\n\0":
'???',

# Asuka Soryu Langley
"ねえ、\n今夜ガッコの屋上に行かない？▽\n流星が見れるかもしれないわよ。\n\0":
'???',

# Rei Ayanami 
"今夜、一緒に星を見ない？▽\nどこか…、そう、学校の屋上で。\n私、流星を見てみたいの。\n\0":
'???',

# Hikari Horaki
"ねえねえ、\n流星を見てみたいと思わない？▽\n今日なんて、天気もよさそうだし、\n一緒に学校の屋上で見ない？\n\0":
'???',

# Toji Suzuhara 
"なあ、\n今夜、屋上で星でも見ぃへんか？▽\nホラ、あの…、流星が見えるって\n先生とか言うてたやんか。▽\n今日あたりなら見えるんちゃう？\n\0":
'???',

# Kensuke Aida
"屋上で流星を見ない？\n今日が最も多く見れる日なんだ。▽\n俺、前にも見た事があるけど\nスゲー綺麗なんだぜ。\n\0":
'???',

# Kaworu Nagisa 
"今夜、一緒にいて欲しいんだ。\n二人で、星を見たくてね。\n場所は、学校の屋上で。▽\nいいかな…？\n\0":
'???',

# Shinji Ikari
"ああ、僕も見てみたかったんだ。\n…その、今まで星なんて\n興味なかったから。▽\nそうだ、他にも誰か誘っておくよ。\n\0":
'???',

# Asuka Soryu Langley
"ふーん、天体観測？\nいいわ、今夜ね。\n一緒に見ましょ。▽\nそうだ、誰か誘っとく？\n私テキトーに声かけてみるわ。\n\0":
'???',

# Rei Ayanami 
"星…？\nいいわよ。\n皆に連絡しておくわ。\n\0":
'???',

# Hikari Horaki
"ああ、流星群！\n見たいって思っていたの。▽\nええ、行くわ。\nそれじゃあ、\nお家に電話しとかないとね。▽\nそれと、他にも誘っておくわ。\n来てくれるかわからないけど…。\n\0":
'???',

# Toji Suzuhara 
"そーやなー、\nナイターあるしな…。▽\nあ、いや…、行く行く、\n行きますってば！！\n\0":
'???',

# Toji Suzuhara 
"せや、誰か誘うか。\nちょっくら、声かけとくわ。\n\0":
'???',

# Kensuke Aida
"うん、\n俺も見たいと思ってたんだけど…。▽\n一人で見てもなぁって思ってたから、\nちょうど良かったよ。\n何なら他も誘おうよ。\n\0":
'???',

# Kaworu Nagisa 
"いいよ。\n一人より、二人がいいからね。▽\nそうだな…、\n他にも誰か誘っておくよ。\n\0":
'???',

# Shinji Ikari
"じゃあさ、夕飯済ませた頃に\n屋上で待ってるから。\n\0":
'???',

# Asuka Soryu Langley
"じゃあ、私は夕飯済ませたら\n屋上で待ってるわ。\n\0":
'???',

# Rei Ayanami 
"夕食済ませたら、屋上に行くわ。\n\0":
'???',

# Hikari Horaki
"じゃあ、晩御飯が済んだら、\n屋上に集合ね。\nフフフ…。\n\0":
'???',

# Toji Suzuhara 
"ほな、今晩、屋上でな。\n\0":
'???',

# Kensuke Aida
"じゃあ、今夜、屋上で。\n\0":
'???',

# Kaworu Nagisa 
"たくさん見られるといいね。\nじゃあ、今夜屋上で。\n\0":
'???',

# Shinji Ikari
"あ…、来てたんだ。\n\0":
'???',

# Asuka Soryu Langley
"何だ、先に来てるんじゃん。\n\0":
'???',

# Rei Ayanami 
"早かったのね…。\n\0":
'???',

# Hikari Horaki
"あら、\n私より早かったんだ？\n\0":
'???',

# Toji Suzuhara 
"なんや、オマエの方が\n早かったんやな？\n\0":
'???',

# Kensuke Aida
"もー、やっぱり校門で\n待ち合わせた方が良かったよ。▽\n俺も急いで来たのに、\n早かったんだな。\n\0":
'???',

# Kaworu Nagisa 
"僕の方が早いと思ったよ。\n先を越されたね。\n\0":
'???',

# Shinji Ikari
"ほら、理科室から双眼鏡を\n持ってきたよ。▽\n流星、見えるかな？\n\0":
'???',

# Asuka Soryu Langley
"今夜も蒸すわね〜…。\n少しくらい風吹きゃいいのに…。\n\0":
'???',

# Rei Ayanami 
"ここ、\n虫の声がする…。\n\0":
'???',

# Hikari Horaki
"あちこち見てるんだけど、\n流星はまだみたい…。\n\0":
'???',

# Toji Suzuhara 
"見てみぃ、ごっつ刺されたわ。\nあ〜もぉ…、かゆぅてたまらんわ。\n\0":
'???',

# Kensuke Aida
"ああ、来た来た…。\n暗くて静かで…、\nちょっと、心細かったよ。▽\nサバイバルしてる時は暗くて静かな\nところは平気なんだけどさ、\n学校ってのはどうもね…。\n\0":
'???',

# Kaworu Nagisa 
"夜にもなると、\nここも静かでいいね。\n今度は月夜の晩に来てみたいよ。\n\0":
'???',

# Shinji Ikari
"流星を見るには、\n時間が早すぎたのかなぁ…。\n\0":
'???',

# Asuka Soryu Langley
"星なんてじっくり見るの、\n初めてかしら…。\n\0":
'???',

# Rei Ayanami 
"今日は、月がないから。\n星がよく見えるわ…。\n\0":
'???',

# Hikari Horaki
"えーと、確かこっちの方向で\n見られるって…。\n\0":
'???',

# Toji Suzuhara 
"あ、あ、あ！？\n流星！！　…じゃなくって\nありゃ、人工衛星やわ…。\n\0":
'???',

# Kensuke Aida
"星、すごい見えるね。\n天体望遠鏡持ってくれば\nよかったかな？\n\0":
'???',

# Kaworu Nagisa 
"満天の星…。\n上を見れば、こんなにも\nにぎやかなんだね。\n\0":
'???',

# Shinji Ikari
"…あっ。\n\0":
'???',

# Asuka Soryu Langley
"ちょっ、アレ！！\n\0":
'???',

# Rei Ayanami 
"あそこ…。\n\0":
'???',

# Hikari Horaki
"あぁ！！\n\0":
'???',

# Toji Suzuhara 
"わっ！？\n…み、見ぃ見ぃ！！\n\0":
'???',

# Kensuke Aida
"あっ、出たっ！！\n\0":
'???',

# Kaworu Nagisa 
"来たよ…。\n\0":
'???',

# Shinji Ikari
"流星…？▽\nあっ、向こうにも！！\n\0":
'???',

# Asuka Soryu Langley
"こっちにも！！\n\0":
'???',

# Rei Ayanami 
"こっちの方角にも見えたわ。\n\0":
'???',

# Hikari Horaki
"一つ…二つも！！\nこっちの方がすごいわよ！！\n\0":
'???',

# Toji Suzuhara 
"お、お、お、お！！\nで、出たんか！？\n\0":
'???',

# Kensuke Aida
"ほんとだ…。\nあれ、流星痕だね。\n\0":
'???',

# Kaworu Nagisa 
"始まったようだね。\n\0":
'???',

# Shinji Ikari
"ねえ、寝そべって見るってのは\nどう？\n\0":
'???',

# Asuka Soryu Langley
"んっふっふっふ〜。\nひらめいた！！▽\nね、ここに寝そべって見ない？\n\0":
'???',

# Rei Ayanami 
"…そうだわ、\nここで横になって見たら、\nもっと見れるかもしれない。\n\0":
'???',

# Hikari Horaki
"ね、横になって見ない？\nその方が空を見渡せるわよ。\n\0":
'???',

# Toji Suzuhara 
"横にならへんか？▽\nほれ、この方が見やすいやんか。\nぜーんぶ見渡せる。\n\0":
'???',

# Kensuke Aida
"寝そべって見た方がいいよ。\n全体を見渡せるもの。\nほら、そうしてみなよ。\n\0":
'???',

# Kaworu Nagisa 
"君もこうやって、\n寝そべってみない？▽\n空が、よく見えるよ。\n\0":
'???',

# Shinji Ikari
"わ…ぁ、\nこんな空、プラネタリウムでしか\n見た事ないよ。\n\0":
'???',

# Asuka Soryu Langley
"あー、ホント。\n寝て見る方がいいわ。\nあちこち向かずに済むもんね。\n\0":
'???',

# Rei Ayanami 
"…綺麗ね。\n\0":
'???',

# Hikari Horaki
"どんどん流星の数が増えてきた。▽\nすごい…、\nすごい、すごい…。\n\0":
'???',

# Toji Suzuhara 
"あちこち、よう見えるやん。▽\nおぉ、今のでっかいわ。\nすんげー、明るかったわ。\n\0":
'???',

# Kensuke Aida
"吸い込まれそうだね。\n星空に浮かんだような変なカンジ。\n\0":
'???',

# Kaworu Nagisa 
"綺麗なものの前では、\nヒトはとても純粋になるよね。▽\n今の君も…。\n\0":
'???',

# Shinji Ikari
"………。▽\n誘ってくれて嬉しかった。▽\nねえ、もっと見ていたいんだ。\nもう少し遅くなってもいいかな？\n\0":
'???',

# Asuka Soryu Langley
"………。\nね…。▽\n今日は、誘ってくれてアリガト。▽\nもう少し、見てよっか…。\n\0":
'???',

# Rei Ayanami 
"………。▽\n星の光が刺さるよう…。\n不思議な感じ…。▽\n私、もっと見ていたい。▽\nあなたは…？\n\0":
'???',

# Hikari Horaki
"………。▽\n綺麗ね…。▽\nこんなにたくさん見られるなんて\n思わなかった…。▽\nそれになんだか楽しいわ、\nこんな風に隠れるみたいに\nしてるのってワクワクしちゃう。▽\nもう少し…、見ていましょうよ。\n\0":
'???',

# Toji Suzuhara 
"………。▽\nナイター、どっちが勝ったんやろ？\n\0":
'???',

# Toji Suzuhara 
"ま、えーか。それよりももっと、\nいいモン見れたし。▽\nなぁ、なんか落ち着くよなぁ…。▽\nワシ、もう少し、\nこうしときたいんやけど…。\n\0":
'???',

# Kensuke Aida
"………。▽\nピークの時間になれば、\nもっと流星が見れるはずだよ。▽\n少し遅くなるけどさ、\n見る価値あると思うよ。\n\0":
'???',

# Kaworu Nagisa 
"………。▽\n今日、誘ってくれて嬉しかったよ。\n本当に。▽\n僕には、今までこんな体験が\nなかったんだ。▽\nだから、とても楽しいよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"その晩は、遅くまで喋りあった。▽\nどうでもいい、\nとりとめもない事ばかりだったけど、\n言葉が自然に口をついて出た。▽\nそのあと、\n見回りに来た先生に見つかり、\n怒られて屋上を降りた。▽\n帰り道にも星は降っていた。▽\nまた、とりとめもない話をしながら\n上を向いて家に帰った。▽\nこんなお喋りな自分がいたんだと\n何となく不思議な気分になった。\n\0":
'???',

#
# ./USRDIR/event/f029.har_EXTRACT/f029.evs
#
# [Love Comedy: Marriage]
#
# [Text Only - No Designated Speaker]
"何か葉書が落ちている。▽\n葛城ミサト様…。▽\nミサト宛の友人からの\n結婚報告の葉書だ。▽\nそういえば、結婚式に\n出席するとか言ってたっけ…。▽\nとうとう、\n行かずじまいだったんだ…。\n\0":
'???',

# Ryoji Kaji
"おっとごめんよ、\n急いでるんだ。\nどいてくれ、すまない！\n\0":
'???',

# Ritsuko Akagi 
"あら、ごめんなさいね。\n先を急がせて。\n\0":
'???',

# Rei Ayanami 
"……？\n\0":
'???',

# Hikari Horaki
"あんなに急いで…、\n何があるんだろう？\n\0":
'???',

# Toji Suzuhara 
"何や、あない慌てて、\nなんかあるんやろか？\n\0":
'???',

# Kensuke Aida
"どうしたんだろう、\nだいぶ慌ててたけど…。▽\n何かに遅刻しそうなのかな？\n\0":
'???',

# Misato Katsuragi 
"何やってんのよ、遅かったじゃない。\n結婚式に間に合わないじゃない。\n急いで！\n\0":
'???',

# Ritsuko Akagi 
"御祝儀は用意したの？\nんもう、結婚式始まっちゃうわよ。\n待ち合わせするんじゃなかったわ。\n\0":
'???',

# Ryoji Kaji
"結婚式、もうすぐ始まるぞ。\nまさか結婚式がある事、\n忘れてたんじゃないだろうな？\n\0":
'???',

# Shinji Ikari
"あれ、今日は大学の時の友達の\n結婚式に招待されているんじゃ\nなかったっけ…？\n\0":
'???',

# Asuka Soryu Langley
"なにノンキにしてるの？\n今日は知り合いの結婚式に\n出席するんじゃなかったの？\n\0":
'???',

# Rei Ayanami 
"今日は結婚式に参加するんじゃ？\n\0":
'???',

# Hikari Horaki
"あれ？\n今日は結婚式があるとか…。\n時間、まだいいんですか？\n\0":
'???',

# Toji Suzuhara 
"今日は大学の友人の結婚式に\n行くんちゃいますのん？\n間に合うんですか？\n\0":
'???',

# Kensuke Aida
"今日は学生時代の友人の結婚式に\n招待されているんでしょ？▽\n用意とか、しなくていいんですか？\n\0":
'???',

# Misato Katsuragi 
"それがさ、スーツのボタンが\n飛んじゃってさ…。▽\n裁縫道具なんてあったかしら？\n\0":
'???',

# Misato Katsuragi 
"ああ〜ン、やっぱりミエ張って\n小さいサイズを買ったのは\n失敗だったわ。\n\0":
'???',

# Ritsuko Akagi 
"ごめんなさい、\nちょっと仕事で来るのが\n遅れちゃったのよ。\n\0":
'???',

# Ryoji Kaji
"大丈夫、\n披露宴にさえ間にあえばいいさ。▽\n結婚式はどうせ親族しか\n参加出来ないはずだからな。\n\0":
'???',

# Misato Katsuragi 
"急ぎなさいよ、全く。\nあ〜、私も靴出さなくっちゃ！！\n\0":
'???',

# Ritsuko Akagi 
"呆れるわ、全く。\n式場に遅れて入るのは\nゴメンだからね。\n\0":
'???',

# Ryoji Kaji
"まあいいさ。\n結婚式は少しくらい\n待っててもらえる、わけないな。\n\0":
'???',

# Shinji Ikari
"そんなことだから\n結婚も遅れるんですよ。\n\0":
'???',

# Asuka Soryu Langley
"お土産、持ってきてネ〜。\n\0":
'???',

# Hikari Horaki
"結婚式かぁ…。\n憧れちゃうなぁ。\n\0":
'???',

# Toji Suzuhara 
"結婚式といえば、\nメロンが出るんやったな…。▽\n今は、もちっとシャレたモンが\n出るんかな？\n\0":
'???',

# Kensuke Aida
"…とかく大人は大変だなァ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"式場に着いた時には、\nチャペルでの結婚式が\n終ったばかりだった。▽\n会場へ走っている途中、\n偶然にも花嫁の投げたブーケを\nキャッチした。▽\n披露宴のあとの２次会、３次会は\nほとんど同窓会状態になり、\n明け方まで友人達と飲み明かした。\n\0":
'???',

# Misato Katsuragi 
"今夜はチョッチ、\n結婚式で遅くなるから、\n適当にナンか食べといてね。\n\0":
'???',

# Ryoji Kaji
"よお、今夜は結婚式の二次会、\n三次会があるから、\nしばらく連絡はとれないからな。\n\0":
'???',

# Ritsuko Akagi 
"今日は大学の時の友人の\n結婚式があるの。▽\n今日は本部に戻る事はないから、\n何かあったら明日話してね。\n\0":
'???',

# Shinji Ikari
"そうなんだ、結婚式かぁ、\n僕も一度くらいは出席してみたいな。\n\0":
'???',

# Asuka Soryu Langley
"結婚式ねぇ、\n他人の一瞬の幸せに同席して、\nなにが楽しいんだか。\n\0":
'???',

# Misato Katsuragi 
"あら、ごめんなさい。\nチョッチ急いでるの、じゃ！\n\0":
'???',

#
# ./USRDIR/event/f006.har_EXTRACT/f006.evs
#
# [Serious: Second Branch Vanishes]
#
# Male Staff, Makoto Hyuga, Shigeru Aoba, Maya Ibuki, Female Staff
"これは、現在のアメリカ支部の\n状態です。\n静止衛星から確認しました。▽\nエヴァンゲリオン四号機ならびに\n半径８９キロ以内の関連研究施設は\n全て消滅しました。▽\n数千の人間も同じく…。\n\0":
'???',

# Misato Katsuragi 
"どこ行ってたの？\nあなたの留守中に事故発生よ。▽\n数時間前にアメリカ支部が\n跡形もなく消滅したのよ。\n\0":
'???',

# Male Staff
"おそらくは、ドイツで修復した\nΣ機関の搭載実験中の\n事故でしょう。▽\nこのクレーター、爆発ではなく、\n消滅によって出来たものとは…。\nいや、信じられませんね…。\n\0":
'???',

# Misato Katsuragi 
"見て…、静止衛星からの映像。\nこれが、現在のアメリカ支部の\n状態よ。▽\nエヴァンゲリオン四号機ならびに\n半径８９キロ以内の関連研究施設は\n全て消滅。▽\n数千の人間も同じくね…。\n\0":
'???',

# Ritsuko Akagi 
"どこに行ってたの？\nあなたの留守中に\n事故が発生したのよ。▽\nアメリカ支部が数時間前に\n跡形もなく消滅したのよ。\n\0":
'???',

# Makoto Hyuga
"大変ですよ！\nアメリカ支部で事故が発生しました。▽\n奇異な事ですが、アメリカ支部が\n数時間前に跡形もなく消滅したとの\n事です。▽\n詳しく説明をしますので、\nまずはモニターを\n見ていただきます。\n\0":
'???',

# Shigeru Aoba
"あっ、いらしてたんですか？▽\n大変ですよ、\nアメリカ支部が数時間前に\n跡形もなく消滅したとの事です。▽\n詳しく説明をしますので、\nまずはモニターを\n見ていただきます。\n\0":
'???',

# Maya Ibuki 
"どこにいらしてたんですか？\nアメリカ支部で事故発生ですよ。▽\nアメリカ支部が数時間前に突然\n跡形もなく消滅したとの事です。▽\n詳しく説明をしますので、\nまずはこちらのモニターへ、どうぞ。\n\0":
'???',

# Female Staff
"アメリカ支部で事故が発生しました。\nアメリカ支部が数時間前に\n跡形もなく消滅したとの事です。▽\n詳しく説明をしますので、\nまずはモニターを\n見ていただきます。\n\0":
'???',

# Male Staff
"あなたの不在時に事故が\n発生しました。▽\nアメリカ支部が数時間前に\n跡形もなく消滅。▽\n原因は新型動力機関の暴走だと\n思われます。\n\0":
'???',

# Ritsuko Akagi 
"静止衛星からの映像よ。\nこれが現在のアメリカ支部。▽\nエヴァンゲリオン四号機ならびに\n半径８９キロ以内の関連研究施設は\n全て消滅。▽\n数千の人間も同じくね…。\n\0":
'???',

# Misato Katsuragi 
"おそらくは、ドイツで修復した\nΣ機関の搭載実験中の\n事故でしょうね…。▽\nそれにしても、このクレーター、\n爆発ではなく、消滅によって\n出来たものなの…。\n\0":
'???',

# Makoto Hyuga
"おそらくは、ドイツで修復した\nΣ機関の搭載実験中の事故と\n思われますが…。▽\nそれにしても、爆発ではなく、\n消滅とは…。\n\0":
'???',

# Maya Ibuki 
"おそらくは、ドイツで修復した\nΣ機関の搭載実験中の事故と\n思われますが…。▽\nそれにしても、このクレーター、\n爆発ではなく、\n消滅によって出来たと…。\n\0":
'???',

# Female Staff
"おそらくは、ドイツで修復した\nΣ機関の搭載実験中の事故と\n思われますが…。▽\nええ、繰り返しますがこれは、\n爆発ではなく、消滅したものです。\n\0":
'???',

# Ritsuko Akagi 
"おそらくは、ドイツで修復した\nΣ機関の搭載実験中の\n事故でしょうね…。▽\nそれにしても、このクレーター、\n爆発ではなく、消滅によって\n出来たものなの…。▽\n施設や、四号機は…、\n多分ディラックの海に\n飲み込まれたんだと思うわ。\n\0":
'???',

#
# ./USRDIR/event/f007.har_EXTRACT/f007.evs
#
# Toji Suzuhara 
"何で、何でワシなんですか？\n\0":
'???',

# Ritsuko Akagi 
"パイロットは\n誰でもいいというわけじゃないの。▽\nあなたが選ばれたのは、\nあなたにそのパイロットの\n素質が認められたからよ。\n\0":
'???',

# Female Staff
"我々ネルフの組織による\nマルドゥック機関により、\nパイロットの選出を行います。▽\n今回は、あなたがその素質を\n見込まれて選ばれる運びと\nなりました。\n\0":
'???',

# Toji Suzuhara 
"そっか、シンジの奴…、\n好きでなったんやないって\nこういう事やったんか…。\n\0":
'???',

# Ritsuko Akagi 
"あなたのお父さんには、\n既に許可をいただいています。▽\nこの件について、\n引き受けてもらえるかしら？\n\0":
'???',

# Female Staff
"あなたのお父さまには、こちらから\n許可をいただいております。▽\nこの件について、\nお引き受けしていただけますか？\n\0":
'???',

# Toji Suzuhara 
"ほな…、▽\nほな、ワシの入院中の妹…、\n本部の医学部に転院させて\nもらえますか…。\n\0":
'???',

# Ritsuko Akagi 
"お安い御用よ。\n\0":
'???',

# Female Staff
"わかりました。\n手続きはこちらですべて、\n行います。\n\0":
'???',

# Toji Suzuhara 
"これで、妹が治るんやったら…。\nワシの命なんぞ、惜しくないわ。\n\0":
'???',

# Misato Katsuragi 
"鈴原くんじゃない。\n時間までまだ早いのに…。\n\0":
'???',

# Misato Katsuragi 
"あっ、わかった〜！\n私を迎えに来てくれたんでしょ〜。\n\0":
'???',

# Ritsuko Akagi 
"鈴原くん？\nちょうどよかったわね、\n私は今から出るところだったの。▽\nこのまま一緒に松代へ行く？\n\0":
'???',

# Female Staff
"鈴原くん…、\n松代へは現地集合に\nなっていたはずだけど…。▽\nああ、遊びに来たのね。\n私はもう用事が済んだから本部へ\n戻るけど、ちゃんと松代へ行くのよ。\n\0":
'???',

# Toji Suzuhara 
"は、はあ…。\n\0":
'???',

# Misato Katsuragi 
"じゃ、今日はこれから\n松代まで出張に出かけるから、\n後は任せたわよ。\n\0":
'???',

# Shinji Ikari
"そっか、松代で\n起動実験なんですよね。\nじゃ、気をつけて。\n\0":
'???',

# Asuka Soryu Langley
"チェ、ミサトがいないと\nペンペンが夜泣きするのよね…。\n\0":
'???',

# Rei Ayanami 
"新しいエヴァが来たのね…。\n\0":
'???',

# Misato Katsuragi 
"そういや、クレンジング\n買っとくの忘れた！\nあぁん、この忙しい時に…。\n\0":
'???',

# Ritsuko Akagi 
"ミサト、忘れ物！\nホント、そそっかしいわね。\n早く、行くわよ。\n\0":
'???',

# Ryoji Kaji
"フォース・チルドレンも同行か。\n荒れそうだな…。\n\0":
'???',

# Kensuke Aida
"そういやトウジのやつ、\n今日はどこにいったんだ？\n\0":
'???',

# Ritsuko Akagi 
"ねえ、ここに鈴原くん\nいるかしら？\n\0":
'???',

# Female Staff
"こちらに鈴原トウジくんは\n来ていませんか？\n\0":
'???',

# Shinji Ikari
"いいえ、ここには…。\n\0":
'???',

# Shinji Ikari
"何でトウジを探してるんだろ？\n\0":
'???',

# Asuka Soryu Langley
"えー、いませんよー。▽\n………。▽\nもしかして、エヴァ参号機が\n到着したのかしら…。\n\0":
'???',

# Rei Ayanami 
"ここにはいませんが…。▽\n…そう、\n新しいエヴァが来たのね…。\n\0":
'???',

# Ritsuko Akagi 
"………。▽\nここにもいないか…。\nまったく困った子ね…。\n\0":
'???',

# Ryoji Kaji
"ここにはいないぞ。▽\nフォース・チルドレンも同行か、\nこいつは荒れそうだな…。\n\0":
'???',

# Hikari Horaki
"いえ、今日は見てませんよ。▽\nどうしてあの人、\n鈴原を探してるんだろ…。\n\0":
'???',

# Kensuke Aida
"いいえ、いませんよ。▽\n何でトウジを探しているんだろう。\n…まさか。\n\0":
'???',

# [Text Only - No Designated Speaker]
"…ふと、鈴原トウジを思い出した。\nそれだけだった。\n\0":
'???',

# Shinji Ikari
"エヴァ参号機のパイロット、\nどんな子供かな…？\n\0":
'???',

# Asuka Soryu Langley
"知らないわよ、そんなの！\n\0":
'???',

# Kensuke Aida
"なあシンジ、やっぱエヴァの\nパイロットってなりたくて\nなれるもんじゃないのかな…。\n\0":
'???',

# Shinji Ikari
"なりたくなくても、\nなってしまうって事もあるよ…。\n\0":
'???',

# Hikari Horaki
"わたし、明日鈴原のお弁当\n作ってあげるんだ…。\n食べてくれるかな…。\n\0":
'???',

# Makoto Hyuga
"もう実験が始まってる時間だろうな。\n\0":
'???',

# Shigeru Aoba
"慌ててこちらによこしてきた機体だ。\n一筋縄ではいかないんじゃないかな。\n\0":
'???',

# Maya Ibuki 
"…そんなこと私には分かりません！\n\0":
'???',

# Misato Katsuragi 
"思ったより順調のようね。\n中の彼は、今どんな気持ち\nなのかしらね。\n\0":
'???',

# Female Staff
"ここまでは全て順調です。\nこれより、作業をフェイズ２へ\n移行します。\n\0":
'???',

# Misato Katsuragi 
"起動実験中止、全神経接続カット！\n\0":
'???',

# Female Staff
"起動実験中止、回路切断！！\n\0":
'???',

# Matsushiro Staff
"参号機より高エネルギー反応、\n加速度的に高まっています！！\n\0":
'???',

# Female Staff
"早く、本部へ連絡を！！\n\0":
'???',

# Male Staff
"松代より入電！\nエヴァ参号機が暴走した模様です。\n\0":
'???',

# Male Staff
"エヴァ参号機のパルス、\n確認不可！\n\0":
'???',

# Male Staff
"タイヘンです！\n松代より巨大な物体が\nこちらに向かっています！\n\0":
'???',

# Male Staff
"エヴァ参号機です…。\nパターン青、エヴァ参号機\n使徒と判別されました！！\n\0":
'???',

# Male Staff
"エヴァ参号機は現時刻をもって破棄。\n目標を使徒と識別して対処します。\n迎撃地点にエヴァ全機緊急配置！\n\0":
'???',

# Misato Katsuragi 
"しょっぱなから素質を\n見せ付けてくれるじゃないの。▽\nでも、本人はどんな気持ちで\nいるのかしらね？\n\0":
'???',

# Female Staff
"Ａ１０神経接続、異常無し。\nここまでは全て順調です。\n\0":
'???',

# Misato Katsuragi 
"シンクロ率、どう？\n\0":
'???',

# Female Staff
"結果報告をお願いします。\n\0":
'???',

# Misato Katsuragi 
"ま、初めてじゃ、こんなものよねぇ。\n\0":
'???',

# Female Staff
"引き続き、経過を報告して下さい。\n\0":
'???',

# Misato Katsuragi 
"無事実験終了、これで一安心ね。\nエヴァ参号機とトウジくん、\nネルフはあなた達を歓迎するわ。\n\0":
'???',

# Female Staff
"了解。\n実験を終了します。▽\n参号機とパイロットを\n本部へ輸送します。\n\0":
'???',

# Shinji Ikari
"ト、トウジが\nエヴァのパイロット！？\n\0":
'???',

# Asuka Soryu Langley
"ウーソーーーーーー！\n何で、こんな奴が\nエヴァのパイロットなのよ！\n\0":
'???',

# Misato Katsuragi 
"と、いうわけで、今後の作戦には\nトウジくんにも加わってもらうわ。\n\0":
'???',

# Ritsuko Akagi 
"と、いうわけなの。\n今後の作戦にはトウジくんにも\n加わってもらうわ。\n\0":
'???',

# Female Staff
"以上、説明した通りです。\n今後の作戦にはトウジくんにも\n加わってもらいます。\n\0":
'???',

# Toji Suzuhara 
"挨拶の前に…あの、あの…、\nトイレどこ…？▽\nこない広いところ、よう歩かんわ。\n\0":
'???',

# Misato Katsuragi 
"突き当たりを右よ。▽\nフフ、緊張気味みたいね。\n\0":
'???',

# Ritsuko Akagi 
"あら、緊張が解けたのね。\n突き当たりを右に行ったらあるわよ。\n\0":
'???',

# Female Staff
"ああ、突き当たりを\n右に行けばありますよ。\n緊張が解けたんですね。\n\0":
'???',

# Toji Suzuhara 
"あーはははアカーン……、\nもる〜〜〜〜〜〜〜〜〜！！\n\0":
'???',

# Shinji Ikari
"ここもにぎやかになるね。\n\0":
'???',

# Asuka Soryu Langley
"ゲヒン…。\n\0":
'???',

# Kaworu Nagisa 
"フフフ、僕も付き合って\nこようかな。\n\0":
'???',

#
# ./USRDIR/event/f008.har_EXTRACT/f008.evs
#
# [Serious: Eva-03 Mildew]
#
# Toji Suzuhara 
"何や、ワイのエヴァだけ、\nぎょーさん汚れとるやないか。\n感じわる…文句言うたろ。\n\0":
'???',

# Toji Suzuhara 
"ちょー、ワイのエヴァ\nめっちゃ汚いやないですか。\n洗浄かけて掃除したって下さいよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"整備員が一所懸命\nエヴァを洗いました。\n綺麗になっていい気分です。\n\0":
'???',

# Toji Suzuhara 
"なあ、ワイのエヴァ、なんか汚いな\n思って掃除しとったら、赤いカビ\nみたいなのがはえとったんや。▽\nキレイに掃除したら、\nなくなってもうたけどな。\n\0":
'???',

# Toji Suzuhara 
"他のエヴァも汚いから、\n掃除するとええわ。\n\0":
'???',

# Shinji Ikari
"カビ？\nエヴァにカビなんてねぇ。▽\nでも、気持ち悪いし、\n誰かに言って掃除してもらうよ。\n\0":
'???',

# Asuka Soryu Langley
"ほんとにィ〜？\n私の弐号機がカビにやられたなんて\n事になったらいい恥さらしよ。▽\nちょっと、整備員に文句言って\n掃除してもらうわ！\n\0":
'???',

# Rei Ayanami 
"そう、ありがとう。\n整備の人に言って掃除してもらうわ。\n\0":
'???',

# Kaworu Nagisa 
"僕の機体も見ておくよ。\nとりあえず、掃除はしてもらう\n事にするよ。\n\0":
'???',

# Toji Suzuhara 
"あのー、ワイのエヴァ、なんか汚いな\n思って掃除しとったら、赤いカビ\nみたいのがはえとったんですケド。▽\nキレイに掃除したら、\nなくなってもうたんです。▽\n他のエヴァも汚いから、\n掃除するとええですよ。\n\0":
'???',

# Misato Katsuragi 
"やぁ〜だ、バッチィ。\nでも、すぐ洗浄するように\n言わなきゃね。▽\nすぐ、手配するわ。\n\0":
'???',

# Gendo Ikari
"わかった、\n整備班の方には伝えておく。\n\0":
'???',

# Kozo Fuyutsuki
"そうか。\nすぐに整備班を呼んで始末させよう。\n\0":
'???',

# Ritsuko Akagi 
"そう、わかったわ。\n些細な事でもエヴァに\n何かあったらいけないからね。\n\0":
'???',

# Maya Ibuki 
"ええっ、本当？\n大変、整備班に言って\n汚れを除去してもらうわね。\n\0":
'???',

# Makoto Hyuga
"整備班もずさんだなぁ。\nわかった、こっちからもう一度\n清掃を申し出てみるよ。\n\0":
'???',

# Shigeru Aoba
"エヴァの機体にカビ？▽\nおかしいな…、\nとにかく整備の方には\n除去するように言っとくよ。\n\0":
'???',

# Ryoji Kaji
"アレにカビが生えるってのは\n異常な事なんだぞ。▽\n見間違いかもしれんが念のため、\n清掃を頼んでおくよ。\n\0":
'???',

# Ritsuko Akagi 
"来たわねトウジくん、\nじゃあ、エヴァ参号機の起動実験、\n始めるわよ。\n\0":
'???',

# Maya Ibuki 
"来たわねトウジくん。\nエヴァ参号機の起動実験、\n行うわよ。▽\nがんばってネ。\n\0":
'???',

# Female Staff
"トウジ君、\nエヴァ参号機の起動実験、\n行うわよ。\n\0":
'???',

# Toji Suzuhara 
"こう、ジメジメしとると、\nあまり気が進まんなあ。\n\0":
'???',

# Ritsuko Akagi 
"ではトウジくん、始めるわよ。▽\n第一次接続開始…、\n起動用システム作動…、\n稼働電圧臨界…、\n\0":
'???',

# Maya Ibuki 
"ではトウジくん、始めるわね。▽\n第一次接続開始…、\n起動用システム作動…、\n稼働電圧臨界…、\n\0":
'???',

# Female Staff
"ではトウジ君、始めます。▽\n第一次接続開始…、\n起動用システム作動…、\n稼働電圧臨界…、\n\0":
'???',

# Male Staff
"神経パルス良好、基準値クリア…。\n\0":
'???',

# Male Staff
"待って下さい、▽\n…パルス、突然逆流をはじめました！\n\0":
'???',

# Ritsuko Akagi, Maya Ibuki, Female Staff
"実験中止！！\n全神経接続…カット！\n\0":
'???',

# Male Staff
"駄目です、\n体内に高エネルギー反応！\n\0":
'???',

# Makoto Hyuga
"ケイジ内で使徒の反応あり、\nエヴァ参号機が発信源です！\n\0":
'???',

# Maya Ibuki 
"エヴァ参号機、コントロール不能、\nエントリープラグも射出出来ません！\n\0":
'???',

# Gendo Ikari
"エヴァ参号機をケイジから射出しろ。\n\0":
'???',

# Maya Ibuki 
"パイロットが乗ったままです！！\n\0":
'???',

# Gendo Ikari
"かまわん、射出だ。\nエヴァンゲリオン参号機は現時刻を\n持って破棄、目標を使徒と識別する。\n\0":
'???',

# Misato Katsuragi 
"エヴァ参号機が起動実験中に\n使徒の寄生により暴走。▽\n現在参号機は地上に射出。\nこれより迎撃の用意に入ります。\n戦闘配置についてちょうだい！\n\0":
'???',

# Ritsuko Akagi 
"エヴァ参号機が起動実験中に\n暴走を始めたわ。\n使徒に寄生されたようなの。▽\n参号機は地上に射出、\n迎撃の用意に入るから急いで\n戦闘配置についてちょうだい！\n\0":
'???',

# Female Staff
"エヴァ参号機が起動実験中に\n暴走しました。▽\n現在参号機は地上に射出、\n使徒に寄生された模様。▽\n現在ネルフは戦闘態勢に\n入っています。▽\n急いで戦闘配置にお願いします。\n\0":
'???',

# Makoto Hyuga, Shigeru Aoba, Maya Ibuki, Male Staff
"エヴァ参号機、\n起動実験中に暴走しました。▽\nおそらく使徒に寄生されたものだと\n思われます。▽\n参号機は地上に射出、現在ネルフは\n戦闘態勢に入っています。\n急いで戦闘配置にお願いします。\n\0":
'???',

# Ritsuko Akagi 
"エヴァの調子が悪いって\n言ってたじゃない？▽\n機体の洗浄の後、再チェックしたら\n調子よくなってたのよ。\n何だったのかしらね？\n\0":
'???',

# Misato Katsuragi 
"あっ、そうそう。\nエヴァの調子が悪いって\n言ってたじゃない？▽\n機体の洗浄の後、再チェックしたら\n調子よくなってたそうよ。\n一体、何が原因だったのかしらね？\n\0":
'???',

# Female Staff
"エヴァの調子が悪いって\n言ってたでしょう？▽\n機体の洗浄の後、再チェックしたら\n調子がよくなっていたんですよ。\n何だったんでしょうね？\n\0":
'???',

# Maya Ibuki, Shigeru Aoba, Male Staff
"エヴァの調整値に誤差があったので、\n原因を調べていたのですが、\nとうとうわからずじまいです。▽\n今は誤差もなく、\n異常な個所は見られません。▽\n何だったんでしょうね、\n機体の洗浄後に再チェックをしたら\n元に戻っていたんですけど。\n\0":
'???',

# Makoto Hyuga
"エヴァの調整値に誤差があったので、\n原因を調べていたのですが、\nとうとうわからずじまいです。▽\n今は誤差もなく、\n異常な個所は見られませんが…。▽\n何だったんでしょうね、\n機体の洗浄後に再チェックをしたら\n元に戻っていたんですけど。\n\0":
'???',

#
# ./USRDIR/event/f009.har_EXTRACT/f009.evs
#
# [Serious: Eva-04 Summoned]
#
# Kaworu Nagisa 
"やあ、君かい。▽\nちょっと付き合って\nもらえるかな…？\n\0":
'???',

# Kaworu Nagisa 
"今日は君に、面白いものを\n見せてあげたいんだ。\n\0":
'???',

# Shinji Ikari
"僕に…？\n\0":
'To me...?\n\0',

# Asuka Soryu Langley
"なーに？\nあんたの面白いって、\n何かたかがしれてそうなんだけど。\n\0":
'???',

# Rei Ayanami 
"あなたが…？\n\0":
'???',

# Toji Suzuhara 
"何や、ちょっとやそっとの芸じゃ\nワイは納得せえへんで。\nで、何見せてもらえるんや？\n\0":
'???',

# Kaworu Nagisa 
"さ、ここからが良く見えるよ。\n紹介しよう、僕達の新しい仲間だ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"カヲルは、空に向かって\n手を差し出すと指を鳴らした。\n\0":
'???',

# Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Female Staff
"大変です、本部直上に\nマイナスエネルギー電子が\n集中しています！\n\0":
'???',

# Kozo Fuyutsuki
"どうした、何事だ！\n\0":
'???',

# Ritsuko Akagi 
"負のエネルギー？\nまさか、ディラックの海！\n\0":
'Negative energy?\nIt\'s a Dirac Sea!\n\0',

# Misato Katsuragi 
"え、一体どうゆうコトなの！？\n\0":
'???',

# Male Staff
"状況を引き続き\nモニターして下さい！\n\0":
'???',

# Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Female Staff
"本部上空に巨大な物体出現！\n使徒？\n\0":
'???',

# Shinji Ikari
"な、あ、あれは一体…？\n\0":
'???',

# Asuka Soryu Langley
"何アレ！？\nエヴァ…？\n\0":
'What is that?!\nAn Eva...?\n\0',

# Rei Ayanami 
"あれはエヴァ、四号機…。\n\0":
'That\'s Eva Unit-04...\n\0',

# Toji Suzuhara 
"お、お、おい！！\nありゃエヴァやんけ！\n\0":
'???',

# Kaworu Nagisa 
"面白かったかい？▽\nそう、これはアメリカ第２支部の\n消滅と共にディラックの海に消えた\nエヴァ四号機さ。▽\n彼とはいつも呼び合っていた…。\nだから、僕が呼んだんだ。\n\0":
'???',

# Toji Suzuhara 
"何や、ちょっとやそっとの芸じゃ\nワイは納得せえへんで。\nで、何見せてもらるんや？\n\0":
'???',

# Male Staff
"状況を引き続きモニターして\n下さい！\n\0":
'???',

# Misato Katsuragi 
"あれは、四号機！？\nそ、そんな馬鹿な…。\n\0":
'That\'s Unit-04?!\nBut that\'s impossible...\n\0',

# Kozo Fuyutsuki
"あれは、アメリカ支部と共に消滅した\nエヴァ四号機じゃないのか…。\n\0":
'???',

# Ritsuko Akagi 
"そんな、ディラックの海から\n四号機が現われるなんて！\n\0":
'???',

# Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Female Staff
"…な、渚カヲル君より入電。▽\nエヴァ四号機は\n気に入ってもらえたか\nとのことですが…。\n\0":
'???',

# Misato Katsuragi 
"渚くんが…。\n\0":
'???',

# Ritsuko Akagi 
"まさか、\n彼はディラックの海までも\n操作出来るというの…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"なぜか、ふとそこに\n渚カヲルがいたような気がした。\n\0":
'???',

#
# ./USRDIR/event/f010.har_EXTRACT/f010.evs
#
# Gendo Ikari
"これより、エヴァ初号機の起動は\n凍結する。\n委員会の別命があるまではだ。\n\0":
'???',

# Kozo Fuyutsuki
"エヴァ初号機の使用は当面凍結する。\nすまんな、委員会を納得させる\nジェスチャーだよ…。\n\0":
'???',

# Misato Katsuragi 
"人類補完委員会の命により、\n現時刻をもって初号機は凍結、以後\n指示があるまで無期凍結とします。\n\0":
'???',

# Ritsuko Akagi 
"委員会の指示で、\nこれより初号機の使用は\n無期凍結になります。\n\0":
'???',

# Male Staff
"委員会の指示により、\n今後エヴァ初号機の使用は\n凍結されます。\n\0":
'???',

# Gendo Ikari
"これで委員会の奴も、\n少しは大人しくなるだろう。\n\0":
'???',

# Kozo Fuyutsuki
"凍結だけで納得するとは思えんがね。▽\nまあ、あれは不慮の事故だと\n言うしかないが。\n\0":
'???',

# Misato Katsuragi 
"この先も使徒は\n攻めて来るというのに。\n…まいったわね。\n\0":
'???',

# Ritsuko Akagi 
"仕方ないわよ。\nあんな騒ぎの後だもの。\n\0":
'???',

# Asuka Soryu Langley
"初号機がなくったって、大丈夫よ。\nどうせ、上もそう判断したんでしょ。\n\0":
'???',

# Makoto Hyuga
"この時期タダでさえ大変だと\nいうのに、凍結だなんて、\n納得出来ないな。\n\0":
'???',

# Maya Ibuki 
"でも私達、エヴァについてまだ\n知らない事が多すぎるんです。▽\nそう判断をするしか、\nなかったんだと思います…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"以後、エヴァ初号機は\n戦闘に参加出来ません。\n\0":
'???',

#
# ./USRDIR/event/f011.har_EXTRACT/f011.evs
#
# [Serious: Ireul Appears]
#
# Makoto Hyuga
"これは？\n第８７タンパク壁に変質部分が…。\n\0":
'???',

# Maya Ibuki 
"何かしら？\n第８７タンパク壁に変質部分が…。\n\0":
'???',

# Female Staff
"これ、何かしら…？\n第８７タンパク壁に変質部分が…。\n\0":
'???',

# Makoto Hyuga
"…何てことだ。\n\0":
'???',

# Maya Ibuki 
"何これ！？\nそんなまさか！！\n\0":
'???',

# Female Staff
"これは…、大変だわ！\n\0":
'???',

# Makoto Hyuga
"侵食部が爆発的なスピードで、\n増殖していきます！▽\nこれは…、▽\nそんな…、分析パターン青。\n間違いありません、使徒です！！\n\0":
'???',

# Maya Ibuki 
"侵食部が爆発的なスピードで、\n増殖していきます！▽\n解析、出ました…。▽\n何てことなの、分析パターン青。\n使徒です！！\n\0":
'???',

# Female Staff
"侵食部が爆発的なスピードで、\n増殖していきます！▽\nこれは…、▽\n分析パターン青。\n使徒です！！\n\0":
'???',

# Kozo Fuyutsuki
"使徒…、使徒の侵入を許したのか！？\n\0":
'???',

# Makoto Hyuga
"汚染域、さらに拡大。▽\n待って下さい、\nサブ・コンピュータが\nハックされています！\n\0":
'???',

# Makoto Hyuga
"くそ、こんな時に誰が…。▽\n………まさか！？\n\0":
'???',

# Makoto Hyuga
"使徒です、このままマギに\n侵入しようとしています！！\n\0":
'???',

# Maya Ibuki 
"汚染域、さらに拡大。▽\n待って下さい、\nサブ・コンピュータが\nハックされています！▽\nこんな時に誰が…。▽\nえっ、………まさか！？▽\n使徒です、このままマギに\n侵入しようとしています！！\n\0":
'???',

# Female Staff
"汚染域、さらに拡大。▽\n待って下さい、\nサブ・コンピュータが\nハックされています！▽\nこんな時にこんな事、誰が…。▽\n………まさか！？▽\n使徒です、このままマギに\n侵入しようとしています！！\n\0":
'???',

# Makoto Hyuga
"大変です！！\n人工知能メルキオールにより\n自律自爆が提訴されました！！▽\nバルタザールにより、否決。\nカスパーにより、否決。\n\0":
'???',

# Maya Ibuki 
"こ、こんなことって…！？\n人工知能…、メルキオールにより\n自律自爆が提訴されました！！▽\nバルタザールにより、否決。\nカスパーにより、否決。\n\0":
'???',

# Female Staff
"人工知能メルキオールにより\n自律自爆が提訴されました！！▽\nバルタザールにより、否決。\nカスパーにより、否決。▽\nしかし、このままでは６時間後には\nマギの機能が乗っ取られます！\n\0":
'???',

# Misato Katsuragi 
"あなたが早いか、使徒が早いか、\n勝負ってコトね…。\n\0":
'???',

# Makoto Hyuga, Shigeru Aoba, Female Staff
"赤木博士が早いか、使徒が早いか、\n勝負ですね…。\n\0":
'???',

# Maya Ibuki 
"センパイが早いか、使徒が早いか、\n勝負ですね…。\n\0":
'???',

# Asuka Soryu Langley
"えぇ〜、それじゃ今回エヴァでの\n戦闘はナシって事ォ…。\nここでどうしてろって言うのよ！！\n\0":
'???',

# Rei Ayanami 
"この勝負、赤木博士のΑΤが\n勝敗を決めるのね。\n\0":
'???',

# Ryoji Kaji
"こいつはマズッたな…。\n本部から出られないように\nなってやがる…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"リツコのΑΤとインパルスを高く\nして、使徒を撃退して下さい。\n\0":
'???',

# [Text Only - No Designated Speaker]
"自滅促進プログラムの作成を行い、\n使徒を撃退して下さい。\n\0":
'???',

# Kozo Fuyutsuki
"今日はマギの定期検診\nだったかな？\n\0":
'???',

# Toji Suzuhara 
"今日はマギの定期検診\nやったんちゃうかな？\n\0":
'???',

# Kaworu Nagisa 
"今日はマギの定期検診\nだったのかな？\n\0":
'???',

# Makoto Hyuga
"プリブノーボックス周辺の回線、\n調子が悪いと思ったら、\nやはり手抜きがあったとはね…。▽\nもう、修理は済んだのかな。\n\0":
'???',

# Shigeru Aoba
"そういえば…、\nＢ棟の修理工事は終了したのかな？▽\n今日…、ああ、昨日までに\n終ったんだっけ…。\n\0":
'???',

# Maya Ibuki 
"マギの自己診断も終了。▽\n不正なデータが発見されるも、\n自己修復によりこれを解決。\n以後、問題はなし。▽\nさすがマギね。\n\0":
'???',

#
# ./USRDIR/event/f077.har_EXTRACT/f077.evs
#
# Asuka Soryu Langley
"えぇ〜、駄目だったのぉ？\n\0":
'???',

# Rei Ayanami 
"爆発まで、\nあとどのくらいかしら…。\n\0":
'???',

# Misato Katsuragi 
"手強いわね…。\n\0":
'???',

# Ritsuko Akagi 
"一からやり直しね。\nいいわ、見てらっしゃい。\n\0":
'???',

# Makoto Hyuga
"駄目か…。\nでも、残り時間も赤木博士に\n賭けるしかないんだ。\n\0":
'???',

# Shigeru Aoba
"あぁ〜、\nマジ大丈夫なのかなぁ。\n\0":
'???',

# Ryoji Kaji
"まだ時間はある…。\nリッちゃんなら、\n何とかしてくれるさ。\n\0":
'???',

#
# ./USRDIR/event/f078.har_EXTRACT/f078.evs
#
# Ritsuko Akagi 
"プログラムが出来たわ！\n\0":
'???',

# Shinji Ikari
"ま、また失敗…。\n\0":
'???',

# Asuka Soryu Langley
"えぇ〜、\nちょっとマジ大丈夫？\n\0":
'???',

# Rei Ayanami 
"あと３時間…。\n\0":
'Three hours left...\n\0',

# Misato Katsuragi 
"失敗か……。\n\0":
'So we failed...\n\0',

# Ritsuko Akagi 
"今度こそッ！！\n\0":
'???',

# Ritsuko Akagi 
"相当ナメられてるわね。\nいいわ、勝ってみせるわよ。\n\0":
'???',

# Maya Ibuki 
"センパイ…。\n\0":
'Sempai...\n\0',

# Makoto Hyuga
"やっぱり駄目か…。\n\0":
'So it doesn\'t work after all...\n\0',

# Shigeru Aoba
"ΑΤ！！\n赤木博士のΑΤを誰か\n下げたんじゃないのか！？\n\0":
'???',

# Ryoji Kaji
"まだだ、まだ時間はある…。\n頑張れ。\n\0":
'There\'s still time...\n Keep at it.\n\0',

# Makoto Hyuga
"自滅プログラム、\nバルタザールに展開！！▽\nやった！！\n人工知能により\n自律爆破が解除されました。\n\0":
'???',

# Shigeru Aoba
"自滅プログラム、\nバルタザールに展開！！▽\nおっし、やった！！\n人工知能により\n自律爆破が解除されました。\n\0":
'???',

# Maya Ibuki 
"自滅プログラム、\nバルタザールに展開！！▽\nやったわ！！\n人工知能により\n自律爆破が解除されました。\n\0":
'???',

# Misato Katsuragi 
"自滅プログラム、\nバルタザールに展開！！▽\nお見事！！！！\n人工知能により\n自律爆破が解除されたわ。\n\0":
'???',

# Female Staff
"自滅プログラム、\nバルタザールに展開！！▽\nやりました。\n人工知能により\n自律爆破が解除されました。\n\0":
'???',

# Gendo Ikari
"こちらの勝利か…。\n\0":
'???',

# Kozo Fuyutsuki
"赤木博士、ご苦労だった。\n\0":
'Dr. Akagi, good work.\n\0',

# Maya Ibuki 
"さすがセンパイ。\n信じてました！！\n\0":
'That\'s my sempai.\n I believed in you!\n\0',

# Makoto Hyuga
"ふう…、\n生きた心地がしなかったよ。\n\0":
'???',

# Shigeru Aoba
"ハハハ…、\nやった、助かった…。\n助かったんだ…。\n\0":
'Hahaha...\nYou did it. You saved us.\nYou saved us all...\n',

# Ryoji Kaji
"やっぱり君は大した奴だよ。\nリッちゃん。\n\0":
'You really are a hell of a gal,\nRitchan.\n\0',

# Shinji Ikari
"助かった…。\nみんな死なずに済んだんだ…。\n\0":
'???',

# Asuka Soryu Langley
"私達…、助かったんだ…。\n\0":
'We\'ve all been saved...\n\0',

# Rei Ayanami 
"爆発は免れたわ。\nもう安心ね。\n\0":
'???',

# Misato Katsuragi 
"たす…かった…。\nあぁ〜、何かこう、\n疲れがドッと出てきたわ…。\n\0":
'???',

# Ritsuko Akagi 
"さすがに疲れたわ。\n今日はゆっくり休ませて\nもらいましょう。\n\0":
'???',

# Toji Suzuhara 
"ウォー！\nやったぁ！！\nさっすがリツコさんやわ！！▽\nへへ…ん、ふっ、\nもう、ウチ帰れへんと思ったわ…。\n\0":
'???',

# Kaworu Nagisa 
"ト、トウジくん…？\n抱きしめるならもっと優しく。\n苦しいよ…。\n\0":
'???',

# Gendo Ikari
"まあいい、まだ時間はある。\n\0":
'???',

#
# ./USRDIR/event/f079.har_EXTRACT/f079.evs
#
# [Serious: Ireul Attack]
#
# Ritsuko Akagi 
"なんて奴…、\nプロテクトをかけてきたわ！！\n\0":
'???',

# Shinji Ikari
"そ、そんな…、\nもう間に合わないんじゃ…。\n\0":
'???',

# Asuka Soryu Langley
"こんなんトコで\n死ぬのはイヤ〜…。\n\0":
'???',

# Rei Ayanami 
"あと２時間だわ…。\n\0":
'???',

# Misato Katsuragi 
"相手の方が一枚上手だったわね。\n\0":
'???',

# Ritsuko Akagi 
"こうなったら、先を見越して\nプロクテクトを解かないと。\n\0":
'???',

# Makoto Hyuga
"何とかして赤木博士のΑΤを\n上げないと…。\n\0":
'???',

# Shigeru Aoba
"くそー、\nどうしたら赤木博士の\nΑΤが上がるんだ。\n\0":
'???',

#
# ./USRDIR/event/f012.har_EXTRACT/f012.evs
#
# [Serious: Angel Autopsy]
#
# Misato Katsuragi, Ritsuko Akagi 
"さて、そういえばこれから使徒の\n残骸を視察するんだったわ。\n\0":
'???',

# Misato Katsuragi 
"どう、これから使徒の残骸の\n回収作業を視察に行くけど、\nあなたもついてくる？▽\nどんな奴と戦ってるか、\n気になるでしょう？\n\0":
'???',

# Ritsuko Akagi 
"どう、これから使徒の残骸の\n回収作業を視察に行くけど、\nあなたもついてくる？▽\n自分がどんな敵と戦ってるか、\n気になるでしょう？\n\0":
'???',

# Asuka Soryu Langley
"面白そうね、見てみたいわ。\n\0":
'???',

# Rei Ayanami 
"私、行きます…。\n\0":
'???',

# Toji Suzuhara
"どーしよっかな…、\nほな、行っとくか。\n\0":
'???',

# Kaworu Nagisa 
"使徒の死体か…。\n僕も見ておこう。\n\0":
'???',

# Ritsuko Akagi 
"どう、これから使徒残骸の\n回収作業を視察に行くけど、\nついてくる？▽\nどんな敵と戦ってるか、\n気になるでしょう？\n\0":
'???',

# Female Staff
"これから使徒残骸の回収作業の\n視察が行われます。\n視察に随伴してもいいですよ。\n\0":
'???',

# Rei Ayanami 
"私、行きます。\n\0":
'???',

# Toji Suzuhara 
"ほな、行っとこうかな…。\n\0":
'???',

# Kaworu Nagisa 
"使徒の死体…か。\n僕も見ておこう。\n\0":
'???',

# Misato Katsuragi 
"これから使徒の残骸を\n視察に出かけてくるわ。▽\n本部の方、お留守番よろしくねン。\n\0":
'???',

# Ritsuko Akagi 
"これから使徒の残骸を\n視察に出かけてくるわ。\n留守番をたのむわ。\n\0":
'???',

# Female Staff
"これから使徒残骸の\n視察に行ってきます。\n\0":
'???',

# Maya Ibuki, Shigeru Aoba, Female Staff
"了解しました。\n\0":
'???',

# Makoto Hyuga
"早く帰ってきてくださいね。\n\0":
'???',

# Shigeru Aoba
"お土産お願いしますよ。\n\0":
'???',

# Ryoji Kaji
"おう、使徒によろしくな。\n\0":
'???',

# Misato Katsuragi, Ritsuko Akagi, Female Staff
"碇司令、使徒残骸の視察、\n出発の準備が出来ましたが。\n\0":
'???',

# Gendo Ikari
"ああ、わかった。\n今行く。\n\0":
'???',

# Gendo Ikari
"では、行ってくる。\n\0":
'???',

# Misato Katsuragi 
"ではこれより、使徒残骸の\n視察に行ってまいります。\n\0":
'???',

# Ritsuko Akagi 
"では、使徒残骸の視察に\n行ってまいります。\n\0":
'???',

# Female Staff
"では、これより使徒残骸の\n視察に行ってまいります。\n\0":
'???',

# Kozo Fuyutsuki
"ああ、留守は任せてくれ。\n\0":
'???',

# Rei Ayanami 
"よく、こんなにも\n残っていたものね。\n\0":
'???',

# Gendo Ikari
"いいサンプルだ。\n作業を急げ。\n\0":
'???',

# Asuka Soryu Langley
"ちょっと触ってみよっと！\n\0":
'???',

# Toji Suzuhara
"ひょえ〜、でっかいのー。\nこんなんと戦っとったんかい。\n\0":
'???',

# Kaworu Nagisa 
"死んでいるんじゃない、\n停止しているだけだ。\nヒトのように、朽ちる事はなく…。\n\0":
'???',

# Female Staff
"これまでに、何かわかった事は\nありますか？\n\0":
'???',

# Ritsuko Akagi 
"こちらのモニターに出ます。▽\n使徒は粒子と波、両方の性質を\n備える光のような未知の物質で\n構成されているようです。▽\nそしてこれが、使徒独自の\n固有波形パターン。▽\n構成物質の違いはあるものの、\n信号の配置と座標は人間のそれと\n９９．８９％酷似しています。\n\0":
'???',

# Male Staff
"こちらのモニターに出ます。▽\n使徒は粒子と波、両方の性質を\n備える光のような未知の物質で\n構成されているようです。▽\nこれが、使徒独自の\n固有波形パターンです。▽\n構成物質の違いはあるものの、\n信号の配置と座標は人間のそれと\n９９．８９％酷似しています。\n\0":
'???',

# Ritsuko Akagi 
"そうとも言えるわね。\n分析作業が進めば、\n詳しい事はわかるはずよ。\n\0":
'???',

# Toji Suzuhara
"お前、こんな時でも\n何とも思わへんのか？\n\0":
'???',

# Rei Ayanami 
"………。▽\nわからない、でも。▽\n綺麗だと思うわ。\n\0":
'???',

# Toji Suzuhara
"変な奴やのー。\n\0":
'???',

# Asuka Soryu Langley
"コレが同じ生物？\n\0":
'???',

# Kaworu Nagisa 
"使徒から見たら、人間の存在だって\n不思議なモノだと思うよ。\n\0":
'???',

# Female Staff
"そろそろ本部に戻りましょう。▽\nデータはマギに\n送られているはずですから、\n本部で解析作業の続きを行います。\n\0":
'???',

#
# ./USRDIR/event/f013.har_EXTRACT/f013.evs
#
# [Serious: J.A. Event]
#

# Misato Katsuragi 
"さて、今日はアノ、\nΘΑ完成披露記念会だわ。▽\nロボットふぜいが、\n少しは楽しませてくれるかしら。\n\0":
'???',

# Misato Katsuragi 
"アララ…、\n今行こうと思ってたのに\n迎えに来てくれたの？\n\0":
'???',

# Asuka Soryu Langley
"あれ？今日は再開発地域に\n出張じゃなかったんですか？\n\0":
'???',

# Ryoji Kaji
"リッちゃん、今日はΘΑの\nお披露目に御招待されてるんじゃ\nなかったっけ？\n\0":
'???',

# Shinji Ikari
"あれ、リツコさん今日は\n出張じゃなかったんですか？\n\0":
'???',

# Ritsuko Akagi 
"今日の出張に必要な資料を、\nミサトに貸していたのよ。▽\n多分、そこら辺に\n投げやられていると\n思うんだけど…。▽\nああ、これよ。\nさて、時間だわ。\n急がなくちゃ…。\n\0":
'???',

# Misato Katsuragi 
"仕事で旧東京市まで行ってくるわ。\n留守番はペンペンにまかせたわよ。\n\0":
'???',

# Ritsuko Akagi 
"さて、今から出張だわ。\nあんまり気が進まないわね…。\n\0":
'???',

# Shinji Ikari
"そういえば、今日は旧東京の\n再開発地域で式典があるとか。\nスタッフの人達が言ってたな…。\n\0":
'???',

# Asuka Soryu Langley
"今日、旧東京の再開発地域で\n式典があるとか言ってたけど、\n何をやってんのかしら…。\n\0":
'???',

# Ryoji Kaji
"そういえば、今日は旧東京の\n再開発地域で巨大ロボットの\n発表会があるらしいよ。\n\0":
'???',

# Kensuke Aida
"情報によると、エヴァの他にも\n巨大ロボットが作られていて、▽\n今日、そのロボットが\n発表されるらしいよ。\n\0":
'???',

# Rei Ayanami 
"エヴァ以外のロボットが\n作られたらしいわ。▽\n今日は、そのロボットの\n発表会が行われるの。\n\0":
'???',

# Toji Suzuhara 
"エヴァ以外のロボットが\n作られたんやろ。▽\n今日、そのロボットの発表会が\n行われるて聞いたで。\n\0":
'???',

# Hikari Horaki
"エヴァ以外のロボットが\n作られたらしいわね。▽\n今日、そのロボットの発表会が\n行われるんでしょ。\n\0":
'???',

# Shiro Tokita
"本日はお忙しいところ、\n我が日本重化学工業共同体が誇る\n新製品の実演会にお越しいただき、▽\n誠にありがとうございました。▽\n後程実機をご覧いただきますが、\nご質問のある方は、この場にて\nどうぞ。\n\0":
'???',

# Shiro Tokita
"これは、赤木リツコ博士。\nお越しいただけて光栄の至りです。\n\0":
'???',

# Ritsuko Akagi 
"配布されたこの資料によると、\n内燃機関を内蔵とありますが。▽\n格闘戦を前提とした陸戦兵器に\nリアクターを内蔵する事。▽\nこれは、安全面においてリスクが\n大きすぎると思われます。\n\0":
'???',

# Shiro Tokita
"ま、これが本機の大きな特徴でして、\n連続１５０日間の作戦行動が保証\nされております。▽\n５分も動けない決戦兵器よりは\n役に立つと思いますが…。\n\0":
'???',

# Misato Katsuragi, Ritsuko Akagi 
"コントロール、人的制御の問題は？\n\0":
'???',

# Shiro Tokita
"制御不能に陥り、暴走を許す危険\n極まりない決戦兵器よりは、\nより安全だと思いますよ。▽\n制御出来ない兵器など、\nヒステリーを起こした女性と\n同じですよ、手に負えません。\n\0":
'???',

# Misato Katsuragi 
"何よ！\nムカツクぅ！！\n\0":
'???',

# Ritsuko Akagi 
"自分を自慢し、\nほめてもらいたがっている。\nたいした男じゃないわ。\n\0":
'???',

# Shiro Tokita
"お待たせしました。\n皆さん御覧下さい、これがΘΑ\nジェットアローンです。\n\0":
'???',

# [Text Only - No Designated Speaker]
"格納庫のハッチが開き、\n人型の巨大ロボットが姿を現した。▽\nやがてその巨人は、\n会場が固唾を飲む中、\n前進を開始した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"会場にどよめきと拍手が沸き上がる。\n\0":
'???',

# Misato Katsuragi 
"あら、なかなかのハンサムさんね。\n時田には、お似合いだわ。\n\0":
'???',

# Shiro Tokita, Kensuke Aida
"何だ…？\n\0":
'???',

# Misato Katsuragi 
"あらら…、\n早くもトラブル発生。\n\0":
'???',

# Shiro Tokita
"た、大変だ…。\nΘΑの制御が利かない…。\n\0":
'???',

# Misato Katsuragi 
"ふーん、そりゃヒステリーを\n起こした女性より大変ね。▽\n…っと、こうしちゃいられないわ。\n本部へ連絡しなきゃ！！\n\0":
'???',

# Maya Ibuki, Female Staff
"披露試験中の実験機が\n暴走との入電あり。\nエヴァの出動が要請されています！\n\0":
'???',

# Gendo Ikari
"初号機を使え。\n\0":
'???',

# Kozo Fuyutsuki
"わかった、初号機を出撃させろ。\n\0":
'???',

# Male Staff
"初号機を出します。\n\0":
'???',

# Gendo Ikari
"初号機を使え。\n凍結は現時刻をもって解除する。\n\0":
'???',

# Kozo Fuyutsuki
"わかった、初号機を出撃させろ。\n凍結は現時刻をもって解除。\n話は私がつけておく。\n\0":
'???',

# Male Staff
"委員会より凍結解除の了解が\n下りました。\n初号機を出します。\n\0":
'???',

# Misato Katsuragi 
"初号機が到着したわ。\n\0":
'???',

# Shinji Ikari
"何だ、アレ？\nアレがロボットなのか…。\n\0":
'???',

# Shinji Ikari
"あれを、どうすればいいんだろ。\n\0":
'???',

# Misato Katsuragi 
"シンジ君、私よ！！\nあのロボット止めなさい！！▽\nこれ以上、前進させないように\nしてちょうだい。\n\0":
'Shinji-kun, it\'s me!\nYou need to stop that robot!!▽\nこれ以上、前進させないように\nしてちょうだい。\n\0',

# Shinji Ikari
"あの、ロボットを？\n止める…って、大丈夫かな…。\n\0":
'???',

# Shiro Tokita
"何だ…？\nあっ、まずい、このままでは！\n\0":
'???',

# Misato Katsuragi 
"あ、あ、あ、あ〜〜〜〜っ！？\n\0":
'???',

# Ritsuko Akagi 
"ブザマね…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"あまりに突然の出来事だった。\n美しい弧を描いてΘΑは転倒し、\n巨大な砂埃が舞い上がった。▽\n会場は大慌て、\n式典はめちゃくちゃになった。\n\0":
'???',

#
# ./USRDIR/event/f014.har_EXTRACT/f014.evs
#
# [Serious: Kaji Enters]
#
# Kozo Fuyutsuki
"君か…。\n長旅の後なのに、すまないな。\n\0":
'???',

# Ryoji Kaji
"お久しぶりです。\n例の品をお届けに上がりました。\n\0":
'???',

# Ryoji Kaji
"ちょっと、案内を頼んでもいいかい？\nいつ来てもここは迷路みたいだな。\n\0":
'???',

# Kozo Fuyutsuki, Gendo Ikari
"人類補完計画の要、か…。\n\0":
'The keystone of the Human Instrumentality Project, eh...?\n\0',

# Shinji Ikari
"あ、あなたは誰ですか？\n\0":
'W-who are you?\n\0',

# Maya Ibuki 
"あ、あの…どちら様でしょうか？\n\0":
'???',

# Makoto Hyuga
"あ、あの…、どなたですか？\n\0":
'???',

# Shigeru Aoba
"あ、あの…おたく、誰…ですか？\n\0":
'???',

# Toji Suzuhara 
"何や、知らんオッサンやな。\n\0":
'???',

# Kaworu Nagisa 
"どなた？\n\0":
'???',

# Ryoji Kaji
"おっと、これは失礼。\n俺は加持リョウジ。▽\n特務機関ネルフ、特殊監査部に\n所属している。▽\nドイツ支部からここへ\n出向してきたんだ。\nま、今後ともよろしく。\n\0":
'???',

# Gendo Ikari
"これが、アダム…。\n\0":
'This is Adam...\n\0',

# Ryoji Kaji
"ええ、最初の人間アダムですよ。\nすでにここまで復元されています。▽\n硬化ベークライトで\n固めてありますが、生きています。\n間違いなく。\n\0":
'???',

# Ryoji Kaji
"よ、久しぶり。\n元気してたかい。\n\0":
'???',

# Asuka Soryu Langley
"きゃっ！！\n加持さん！\nやっぱり来てくれたのね！\n\0":
'???',

# Misato Katsuragi 
"アンタの顔見たら、元気が失せたわ。\nその顔だけでお腹いっぱいよ。\n\0":
'???',

# Ritsuko Akagi 
"あら、加持君。\n久しぶり、\nやっぱりここに来たのね。\n\0":
'???',

# Ryoji Kaji
"ドイツ支部から本部に\n出向してきたんだよ。▽\nま、これからは色々世話になるよ。\n改めてよろしくな。\n\0":
'???',

# Ryoji Kaji
"ようやく腰がおろせるな。\nああ、ちょっと君。\n\0":
'???',

# Ryoji Kaji
"俺の荷物を頼む。\n丁重に扱ってくれ。\n\0":
'???',

#
# ./USRDIR/event/f015.har_EXTRACT/f015.evs
#
# [Serious: Blackout]
#
# Asuka Soryu Langley
"あら、電気が戻った？\n\0":
'Huh, the power\'s back?\n\0',

# Shinji Ikari
"だから言ったじゃない、\nそのうち回復するって！\n\0":
'???',

# Asuka Soryu Langley
"うるさいわね！\nアンタのそのノーテンキなところ、\nほんっとムカツクわッ！\n\0":
'???',

# Asuka Soryu Langley
"あら、停電？\n\0":
'???',

# Shinji Ikari
"ほんとだ、停電みたいだね。\n\0":
'???',

# Asuka Soryu Langley
"あんたバカァ？\n何のんきなこと言ってるのよ！\n\0":
'???',

# Makoto Hyuga
"使徒の存在は確認できず…。\nはあ、よかった。\n何も起きてなかった…。\n\0":
'???',

# Ritsuko Akagi 
"…私、じゃないわよ。\n\0":
'...It wasn\'t me.\n\0',

# Maya Ibuki 
"でも、センパイが\n起動スイッチを入れた\nタイミングでしたよ…。\n\0":
'???',

# Misato Katsuragi 
"やっとエレベーターが開いたわ…。\nトイレ、トイレ…、\nあらっ！？\n\0":
'???',

# Ryoji Kaji
"さて、今のうちに仕事を\nやらせてもらおうか。\n\0":
'???',

# Misato Katsuragi 
"ちょっと、なんでこんな時に\nトイレのドアが開かないのよ！\n\0":
'???',

# Misato Katsuragi 
"ちょっと、停電って…。\n何でこーゆー時にエレベータが\n止まるのよ！\n\0":
'???',

# Misato Katsuragi 
"誰よ、入ってるの！！\nさっさと、出なさいよ〜！！\n\0":
'???',

# Shigeru Aoba
"だめだ、外とも回線が繋がらない。\n\0":
'???',

# Makoto Hyuga
"まいったな、こんな時に\n使徒が現れたら大変だぞ。\n\0":
'???',

# Rei Ayanami 
"…なに？\n\0":
'???',

# Kaworu Nagisa 
"…君は僕と同じだね。\n\0":
'You\'re the same as me.\n\0',

# Rei Ayanami 
"私は私よ。\nあなたとは違うわ。\n\0":
'I am me.\nI am not you.\n\0',

# Kaworu Nagisa 
"そうだね、今となっては…。\n\0":
'???',

# Kozo Fuyutsuki
"空調もストップか…。\n\0":
'???',

# Gendo Ikari
"なあに、問題は無い。\n\0":
'???',

# Misato Katsuragi 
"ちょっとぉぉぉ…、\n何でこんな時に\nトイレに行きたくなるのよ！\n\0":
'???',

# Toji Suzuhara
"おーい、暑いやないか…。\nクーラーないとかなわんわ…。\n\0":
'???',

# Maya Ibuki 
"だめです。\n電源遮断の原因が特定出来ません。\n\0":
'???',

# Ritsuko Akagi 
"機械的な故障でないのならば、\n…人為的…。\n\0":
'???',

# Shigeru Aoba
"…ついた。\nよし、使徒の確認を急ごう。\n\0":
'???',

# Shigeru Aoba
"使徒の存在、確認できず、か…。\n\0":
'???',

# Makoto Hyuga
"出来れば今日くらい、使徒には\n休んでいてもらいたいもんだよ。\n\0":
'???',

# Kozo Fuyutsuki
"碇…。\nこの騒ぎは仕組まれたものだぞ。\n\0":
'???',

# Gendo Ikari
"かまわん、泳がせておけ。\n\0":
'???',

# Asuka Soryu Langley
"ぐずぐずしないで、今度はこっちよ！\n\0":
'???',

# Shinji Ikari
"そこはさっき通ったよ…。\n\0":
'???',

# Asuka Soryu Langley
"つべこべ言わないで\nさっさと行くのよ！\nあぁ〜、あっつい、汗だくよ。\n\0":
'???',

#
# ./USRDIR/event/f017.har_EXTRACT/f017.evs
#
# Serious: Eva Mass Production Begins
#
# Gendo Ikari
"とうとう老人達も動きはじめたか。▽\nまあいい、\nイニシアチブは今後も\n我々が握り続ける。\n\0":
'???',

# Kozo Fuyutsuki
"碇、エヴァ拾参号機までの\n第２次整備計画が\n開始されたそうだな…。\n\0":
'???',

# Gendo Ikari
"委員会も無理をしている。\nしかし本気のようだな。\n\0":
'???',

# Kozo Fuyutsuki
"我々も、うかうかしては\nいられないな。\n\0":
'???',

# Gendo Ikari
"問題無い…。\nイニシアチブは今後も\n我々が握り続ける。\n\0":
'???',

# Misato Katsuragi 
"エヴァシリーズの量産が\n始まったって、本当？\n\0":
'Is it true they\'ve started\n mass producing the Eva Series?\n\0',

# Ryoji Kaji
"エヴァシリーズの量産が\n始まったそうだな。\n\0":
'It seems mass production of\nthe Eva Series has started.\n\0',

# Female Staff
"エヴァシリーズの量産が始まった\nとの情報が入りましたが、\nこれは…。\n\0":
'???',

# Makoto Hyuga
"ドイツ経由の情報です。\nこのソースに信頼はおけます。\n\0":
'???',

# Maya Ibuki 
"公式ではありませんが、\nそのような情報が\nリリースされているようです。\n\0":
'???',

# Female Staff
"公式の情報ではありませんが、\n複数のルートから、その件に関する\n情報が流れています。\n\0":
'???',

# Female Staff
"エヴァ拾参号機までの\n第２次整備計画が\n開始されたそうです。\n\0":
'???',

# Kozo Fuyutsuki
"ああ、その情報は\nこちらで確認したよ。\nゼーレは本気のようだ。\n\0":
'???',

# Kozo Fuyutsuki
"ゼーレめ…、\nいよいよ行動に出てきたか。\n\0":
'???',

# Ryoji Kaji
"この時期になって、\n量産に着手するとはね。\n何を考えているんだか…。▽\nそこまでの金を動かす理由が\nあるのか…。\n\0":
'???',

# Misato Katsuragi 
"委員会の焦りらしきものを\n感じるわね。▽\nしかも、非公式に…。\n一体何をするつもりなの…。\n\0":
'???',

# Male Staff
"予備戦力の増強であれば、\n非公式に行う理由は\nないはずですが…。▽\nすべては、情報が公開されるまで\nわかりませんね。\n\0":
'???',

# Female Staff
"エヴァ拾参号機までの第２次\n整備計画が開始されたそうです。\n\0":
'???',

# Gendo Ikari
"その情報は確認済みだ。\nゼーレは本気のようだな。\n\0":
'The information has been verified.\nIt seems Seele are serious.\n\0',

#
# ./USRDIR/event/f018.har_EXTRACT/f018.evs
#
# Keel Lorenz
"かねてより危惧されていた\n使徒出現が、\nついに現実の事となった。\n\0":
'???',

# Committeeman A
"まぁ、予想通り、\n世界は大混乱というやつだな。\n\0":
'???',

# Kozo Fuyutsuki, Ritsuko Akagi, Misato Katsuragi, Female Staff
"もちろん真相は控えます。▽\nネルフでは、考え得る限りの\nダミーのシナリオ、及びシミュレー\nションが既に用意してあります。\n\0":
'???',

# Committeeman A
"賛成だな。\nだがそのための\n時間と人と金をどうするか。\n\0":
'???',

# Kozo Fuyutsuki, Ritsuko Akagi, Misato Katsuragi 
"承知しております。\n\0":
'???',

#
# ./USRDIR/event/f019.har_EXTRACT/f019.evs
#
# Keel Lorenz
"先日の戦闘では、ダミーシステムを\n使用したそうだな。\n\0":
'???',

# Committeeman A
"まだ、開発の途中という話では\nなかったかね？\n\0":
'???',

# Gendo Ikari, Kozo Fuyutsuki, Ritsuko Akagi, Misato Katsuragi, Female Staff
"いずれ報告するつもりでしたが、\n今回は緊急を要し、実戦での使用に\n踏み切りました。\n\0":
'???',

# Committeeman C
"ふん。\n成果を聞こうじゃないか。\n\0":
'???',

# Committeeman D
"あれで、上出来なものとは\n言うまいな。\n\0":
'???',

# Gendo Ikari, Kozo Fuyutsuki, Female Staff
"試作の段階ではありましたが。▽\n一部の問題はあるものの、\nダミーシステムの開発は成功です。\n\0":
'???',

# Ritsuko Akagi, Misato Katsuragi 
"試作の段階ではありましたが。▽\n一部の問題はあるものの、\nダミーシステムの開発は\n成功したと言えます。\n\0":
'???',

# Committeeman D
"まあいい。\nこれで、計画の遅れには\n修正が出来たと言えよう。\n\0":
'???',

# Keel Lorenz
"この調子で計画を\n邁進させてくれたまえ。\n\0":
'???',

# Gendo Ikari, Kozo Fuyutsuki, Ritsuko Akagi, Misato Katsuragi, Female Staff
"承知しました。\n\0":
'???',

#
# ./USRDIR/event/f020.har_EXTRACT/f020.evs
#
# [Serious: Seele, After Eva-01 Gets S2]
#
# Seele 03
"エヴァシリーズに\n生まれいずるはずのない、Σ機関。\n\0":
'???',

# Seele 05
"まさか、かような手段で、\n自ら取り込むとはな。\n\0":
'???',

# Seele 06
"我らゼーレのシナリオとは\n大きく違った出来事だよ。\n\0":
'???',

# Seele 09
"この修正、容易ではないぞ。\n\0":
'???',

# Gendo Ikari, Kozo Fuyutsuki, Ritsuko Akagi, Misato Katsuragi, Female Staff
"とは言え、初号機は我々の\n制御下ではありませんでした。▽\nこれは、不慮の事故と\nみなすべきです。\n\0":
'???',

# Seele 02
"Σ機関を自ら搭載した\nエヴァ初号機。\n\0":
'???',

# Seele 03
"それは理論上は無限に稼動する、\n半永久機関を手に入れた事と同義だ。\n\0":
'???',

# Seele 05
"絶対的存在か。\nそんなものを手にしてよいのは\n神だけだ。\n\0":
'???',

# Seele 06
"人はその分を超えてはならん。\n\0":
'???',

# Seele 01
"我々に具象化された神は\n不要なのだよ。▽\nその対策は考えてあるんだろうな？\n\0":
'???',

# Gendo Ikari, Kozo Fuyutsuki, Ritsuko Akagi, Misato Katsuragi, Female Staff
"はい。\n詳しくは追って報告いたします。\n\0":
'???',

#
# ./USRDIR/event/f021.har_EXTRACT/f021.evs
#
# Seele 05,Seele 09
"ロンギヌスの槍、\n回収は我らの手では不可能だよ。\n\0":
'???',

# Seele 04
"ロンギヌスの槍、何故使用した。\n\0":
'???',

# Seele 09,Seele 03
"エヴァシリーズ、\nまだ予定にはそろっていないのだぞ。\n\0":
'???',

# Gendo Ikari, Kozo Fuyutsuki, Ritsuko Akagi, Misato Katsuragi, Female Staff
"使徒殲滅を優先させました。\nやむを得ない事象です。\n\0":
'???',

# Seele 03,Seele 06
"やむを得ないか？\n言い訳にはもっと説得力を\n持たせたまえ。\n\0":
'???',

# Seele 05
"最近の君達の行動には、\n目に余るものがあるな。\n\0":
'???',

# Gendo Ikari
"人類補完計画の前に、\nサードインパクトが起きても\nやむを得ないとは言えませんので。\n\0":
'???',

# Kozo Fuyutsuki, Ritsuko Akagi, Misato Katsuragi 
"人類補完計画の前に、\nサードインパクトが起きても\nやむを得ないとは言えませんからね。\n\0":
'???',

# Female Staff
"槍を使用する以外、\n勝つ手段はありませんでした。▽\nあのままでは、人類補完計画の前に、\nサードインパクトが\n起きていたでしょう。\n\0":
'???',

# Seele 02
"それは詭弁に過ぎん。\n君はあの状況を利用したのでは\nないのかね？\n\0":
'???',

# Gendo Ikari, Kozo Fuyutsuki
"すべては、報告した通りですよ。\nこれ以上、言うべき事はありません。\n\0":
'???',

# Ritsuko Akagi, Misato Katsuragi, Female Staff
"すべては、報告した通りです。\nこれ以上、申し上げる事は\nありません。\n\0":
'???',

#
# ./USRDIR/event/f022.har_EXTRACT/f022.evs
#
# Seele 03
"我々の意見は一致した。\n\0":
'???',

# Seele 09
"君達の計画を\n我々は利用させてもらう。\n\0":
'???',

# Seele 05
"それが一番近道のようだ。\n\0":
'???',

# Gendo Ikari
"意味がわかりかねますな。\n\0":
'???',

# Kozo Fuyutsuki
"意味がわかりかねますが。\n\0":
'???',

# Ritsuko Akagi 
"それは、\nどういった意味なのでしょうか？\n\0":
'???',

# Misato Katsuragi, Female Staff
"それは、どういう意味でしょうか？\n\0":
'???',

# Seele 01
"そのうち我々の真意がわかるだろう。\nそれだけだ。\n下がりたまえ。\n\0":
'???',

#
# ./USRDIR/event/f024.har_EXTRACT/f024.evs
#
# Shinji Ikari
"え、だ、誰なんですか…？\nはっ…、拳銃…！？\n\0":
'???',

# Asuka Soryu Langley
"誰よ、アンタ。\nそこ通しなさいよ。▽\nはっ！？\n…その銃。\n\0":
'???',

# Rei Ayanami 
"私を、消すように言われたの…？\n\0":
'???',

# Misato Katsuragi 
"あなたね。\nここのところ私を\n付け回していたのは…。\n\0":
'???',

# Gendo Ikari
"老人達に\n私を消すように言われたのか？\n\0":
'???',

# Kozo Fuyutsuki
"…そうか。\nとうとう、\n私を消すと判断したようだな。\n\0":
'???',

# Ritsuko Akagi 
"あなた達は…。▽\nそう、\n私はもう用済みというわけね…。\n\0":
'???',

# Maya Ibuki 
"ひっ！？\nい、いや！！\n殺さないで…。\n\0":
'???',

# Makoto Hyuga
"クソッ、お前ら…。\n捕まってたまるか…！！\n\0":
'???',

# Shigeru Aoba
"な、何だよお前ら…。\n\0":
'???',

# Ryoji Kaji
"よ、遅かったじゃないか。\n\0":
'???',

# Toji Suzuhara 
"な、何やそれ…。\nワイを殺すつもりなんか…？\n\0":
'???',

# Kaworu Nagisa 
"僕の存在を\n危険だと判断したんだね…。\n\0":
'???',

# Shinji Ikari
"ウワッ、拳銃！？▽\nぼ、僕を殺すの！？\n\0":
'???',

# Asuka Soryu Langley
"何よ、アンタ達…！？\nその銃で私を殺すってぇの？\n\0":
'???',

# Rei Ayanami 
"私を殺すつもり…？\n\0":
'???',

# Misato Katsuragi 
"誰の命令か知らないけど、\n私を消しに来たようね。\n\0":
'???',

# Gendo Ikari
"老人達に言われて来たか…。\n\0":
'???',

# Kozo Fuyutsuki
"なるほど、老人達は私を消すと\n判断したようだな…。\n\0":
'???',

# Ritsuko Akagi 
"そう、私はもう用済みという\nわけね…。\n\0":
'???',

# Maya Ibuki 
"はっ…、まさか私を…。▽\nだ、誰か…。\nいやぁぁーーッ、殺されるー！！\n\0":
'???',

# Makoto Hyuga
"くそ、お前ら…。▽\nもう少しですべてがわかる\nところなのに…。\n\0":
'???',

# Shigeru Aoba
"あんたらか…。▽\nくそ、ここで死んでたまるか…。\n\0":
'???',

# Hikari Horaki
"誰ですか…？▽\nはっ、拳銃！？\n\0":
'???',

# Toji Suzuhara 
"け、け、け拳銃！？▽\nな、何やお前ら！！\n\0":
'???',

# Kensuke Aida
"何か用ですか…？▽\n拳銃、\n…ほ、本物だ！！\n\0":
'???',

# Kaworu Nagisa 
"僕を排除するように\n言われたんですね。\n\0":
'???',

# Shinji Ikari
"つけられている。\nここから離れた方がよさそうだ。\n\0":
'???',

# Asuka Soryu Langley
"間違いない、私をつけているわ。\nさっさと、まいた方がいいわね。\n\0":
'???',

# Rei Ayanami 
"誰かがつけてきている…。\n逃げた方がいいわね。\n\0":
'???',

# Misato Katsuragi 
"一人…、いえ、二人ね。\n私を狙っているわ。\n始末するか、この場を離れるか…。\n\0":
'???',

# Gendo Ikari
"つけられているな…。\nここからは離れた方がいいな。\n\0":
'???',

# Kozo Fuyutsuki
"つけられているな。\nここからは離れた方が\nいいようだな。\n\0":
'???',

# Ritsuko Akagi 
"どうやら、つけられているようね。\n\0":
'???',

# Maya Ibuki 
"誰か、つけているんだわ。\n私を狙っているのね。\n\0":
'???',

# Makoto Hyuga
"チッ、誰かつけていやがる。\nさっさと、まいちまうか。\n\0":
'???',

# Shigeru Aoba
"さっきから、人の気配が…。\nここは、走った方がよさそうだな。\n\0":
'???',

# Ryoji Kaji
"奴等め…。\n俺を消しに来たんだな。\nそうは行くか。\n\0":
'???',

# Toji Suzuhara 
"ワイの事、絶対に追っとる奴が\nおるな…。\nよっしゃ、走って逃げたろ！！\n\0":
'???',

# Kaworu Nagisa 
"僕をつけている…。\n僕を消すために…。\nまだ、死ぬわけにはいかない。\n\0":
'???',

# Shinji Ikari
"嫌な予感がする…。\n\0":
'???',

# Asuka Soryu Langley
"嫌な予感がする。\n…まさか。\n\0":
'???',

# Rei Ayanami 
"嫌な予感がする。\n\0":
'???',

# Misato Katsuragi 
"何だか、ヤな予感がするわね。\n\0":
'???',

# Gendo Ikari
"悪い予感がする…。\n\0":
'???',

# Kozo Fuyutsuki
"嫌な予感がする。\n何もなければよいが、しかし…。\n\0":
'???',

# Ritsuko Akagi 
"何となく嫌な予感がするわ…。\n\0":
'???',

# Maya Ibuki 
"何だか胸騒ぎが…。▽\nまさか…。\n\0":
'???',

# Makoto Hyuga
"何だか嫌な予感がする。\n…そうだ！！\n\0":
'???',

# Shigeru Aoba
"まさか、今頃…。\n嫌な予感がする。\n\0":
'???',

# Ryoji Kaji
"狙われている事を\n知っているのだろうか。▽\nひょっとすると、\nマズい事になっているかもしれん。\n\0":
'???',

# Toji Suzuhara 
"何や、嫌な予感がするわ…。\n\0":
'???',

# Kaworu Nagisa 
"何だか悪い予感がする。\nひょっとして…。\n\0":
'???',

# Shinji Ikari
"あぶない！\n\0":
'???',

# Rei Ayanami 
"走るわ。\n\0":
'???',

# Misato Katsuragi 
"はやく、こっちへ！！\n\0":
'???',

# Gendo Ikari
"こっちへ走るんだ。\n\0":
'???',

# Kozo Fuyutsuki
"走るぞ。\n\0":
'???',

# Ritsuko Akagi 
"急いでここを離れて、早く！！\n\0":
'???',

# Maya Ibuki 
"あぶない、こっちへ！！\n\0":
'???',

# Makoto Hyuga
"はやく、向こうまで走って！！\n\0":
'???',

# Shigeru Aoba
"早く、こっちへ！\n\0":
'???',

# Ryoji Kaji
"何も言わず、走って！\n\0":
'???',

# Toji Suzuhara 
"危ない！！\n早う、走って！！\n\0":
'???',

# Kaworu Nagisa 
"早く、ここから離れて！！\n\0":
'???',

# Shinji Ikari
"えっ、えっっ！？\n\0":
'???',

# Asuka Soryu Langley
"キャ！\nな、何なのよ！？\n\0":
'???',

# Rei Ayanami 
"どうして、ここに…！？\n\0":
'???',

# Misato Katsuragi 
"ど、どうしてここに…？\n\0":
'???',

# Gendo Ikari
"どうしたというのだ！？\n\0":
'???',

# Kozo Fuyutsuki
"な、何だね…！？\n\0":
'???',

# Ritsuko Akagi 
"ちょっと、いきなり何…！？\n\0":
'???',

# Maya Ibuki 
"ちょ、ちょっと…！？\n\0":
'???',

# Makoto Hyuga
"わぁ、何だ何だ！？\n\0":
'???',

# Shigeru Aoba
"えっ！？\nな、何だ一体！？\n\0":
'???',

# Ryoji Kaji
"おおっと、何なんだ！？\n\0":
'???',

# Hikari Horaki
"キャー！？\n何、何なの！？\n\0":
'???',

# Toji Suzuhara 
"な、何なんや？\nどないしたんや！？\n\0":
'???',

# Kensuke Aida
"わわっ、走るって何！？\n\0":
'???',

# Kaworu Nagisa 
"えっ、一体どこから…！？\n\0":
'???',

#
# ./USRDIR/event/f025.har_EXTRACT/f025.evs
#
# [Text Only - No Designated Speaker]
"$aの目の前に\n黒服の男達が立ちはだかった。\nゆっくりと銃口を向ける。\n\0":
'???',

# Shinji Ikari
"…わぁぁっ！？\nやだ、嫌だよ…！！\n\0":
'???',

# Asuka Soryu Langley
"チッ、いつの間に…。\n\0":
'???',

# Rei Ayanami 
"撃つのね…。\n\0":
'???',

# Misato Katsuragi 
"…くっ、囲まれた！？\n\0":
'???',

# Ritsuko Akagi 
"観念するわよ…。\nそろそろ潮時だと思っていたわ。\n\0":
'???',

# Maya Ibuki 
"う、撃たないで………。\nヒィィィィー…！！\n\0":
'???',

# Makoto Hyuga
"ちくしょう…、\n逃げ道を塞がれたか…。\n\0":
'???',

# Shigeru Aoba
"クソッ、やるってのか…！？\n\0":
'???',

# Ryoji Kaji
"奴等もここまでが我慢の限界か。\n確かにこの陣形なら、\n俺をやれるかもしれんな。\n\0":
'???',

# Toji Suzuhara 
"な、何や！？\nお前ら、ひ、人殺しか！？\n\0":
'???',

# Kaworu Nagisa 
"僕を廃棄しろと、\n…そう言われたんだね。\n\0":
'???',

# Shinji Ikari
"…うわっ！？\n\0":
'???',

# Asuka Soryu Langley
"…私を…、殺すつもりなのね！？\n\0":
'???',

# Misato Katsuragi 
"囲まれた！？\n\0":
'???',

# Ritsuko Akagi 
"私を消しに来たんでしょ。\n誰の判断かしら…？\n\0":
'???',

# Maya Ibuki 
"…やだ、嫌よ！！\nう、撃たないでぇぇ…。\n\0":
'???',

# Makoto Hyuga
"チッ、\nこんなところにいやがったか…。\n\0":
'???',

# Shigeru Aoba
"くそ、\nこんなところでお出迎えかよ！！\n\0":
'???',

# Ryoji Kaji
"さすが…、\nまいたはずだったが\n甘かったようだな。\n\0":
'???',

# Hikari Horaki
"イヤーッ！！\n殺されるーーーーーーーー！！\n\0":
'???',

# Toji Suzuhara 
"わ、ワイを、それで撃つんか！？\n\0":
'???',

# Kensuke Aida
"こ、殺すなんて、\nひ、人違いでしょ…。\n\0":
'???',

# Kaworu Nagisa 
"早めに手を打っておこうと。\n…そういう事かい？\n\0":
'???',

# [Text Only - No Designated Speaker]
"歩いていると、\nふと何かの気配を感じた。\n\0":
'???',

# Shinji Ikari
"まただ、僕を狙ってる…。\n\0":
'???',

# Asuka Soryu Langley
"いる…。\nまた私を探しているんだわ。\n\0":
'???',

# Rei Ayanami 
"火薬の匂い…。\n近くにいるんだわ…、\nここは危険ね。\n\0":
'???',

# Misato Katsuragi 
"いるわね…。\nこっちから攻勢に出るか…。\nいや、今なら逃げられる…。\n\0":
'???',

# Gendo Ikari
"…奴等か。\nまた、追ってきているな。\n\0":
'???',

# Kozo Fuyutsuki
"今なら、逃げ切れるか…？\n\0":
'???',

# Ritsuko Akagi 
"いるわね…。\n今度は、何人で来たのかしら。\nでも、おあいにくさま…。\n\0":
'???',

# Maya Ibuki 
"奴等だわ…！！\n早く、ここから離れないと。\n\0":
'???',

# Makoto Hyuga
"また、いやがるな…。\nさて、走るか。\n\0":
'???',

# Shigeru Aoba
"奴等の気配だ…。\n捕まってたまるか！！\n\0":
'???',

# Ryoji Kaji
"今度は何人だ…？\nまだ、殺されるわけには\nいかないんでね。\n\0":
'???',

# Toji Suzuhara 
"絶対、ワイを追ってきとるわ。\n走った方がええみたいやな。\n\0":
'???',

# Kaworu Nagisa 
"僕を消しに来たか…。\nけど、捕まるつもりはないよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"危険な気配を感じ、\n走ってその場を離れた…。\n\0":
'???',

# Shinji Ikari
"まさか…。\n\0":
'???',

# Asuka Soryu Langley
"今の、まさかアイツを…。\n\0":
'???',

# Rei Ayanami 
"…あれは、ひょっとして。\n\0":
'???',

# Misato Katsuragi 
"今出てったの、まさか…！？\n\0":
'???',

# Gendo Ikari
"奴等は…。\n\0":
'???',

# Kozo Fuyutsuki
"奴等は…。\nいかん、急がねば！！\n\0":
'???',

# Ritsuko Akagi 
"あれは…！？\n\0":
'???',

# Maya Ibuki 
"火薬の匂い…。\nまさか…！！\n\0":
'???',

# Makoto Hyuga
"あいつら、まさか…。\n\0":
'???',

# Shigeru Aoba
"ひょっとして、あいつら…。\n\0":
'???',

# Ryoji Kaji
"まずい、奴等が動き出したか！！\n\0":
'???',

# Toji Suzuhara 
"あの黒服…。\nひょっとして…。\n\0":
'???',

# Kaworu Nagisa 
"まさか…。\nいや、間違いない。\n\0":
'???',

# Shinji Ikari
"ここは、あぶない！\n\0":
'???',

# Asuka Soryu Langley
"早く！！\n走って！！\n\0":
'???',

# Rei Ayanami 
"あそこまで走るわ。\n\0":
'???',

# Misato Katsuragi 
"はやく、こっちへ！！\nその角まで急いで！！\n\0":
'???',

# Gendo Ikari
"こっちへ走るんだ。\n急げ！！\n\0":
'???',

# Kozo Fuyutsuki
"走るぞ。\n全速力でだ！！\n\0":
'???',

# Ritsuko Akagi 
"急いで走って、早く！！\n\0":
'???',

# Maya Ibuki 
"こっちへ、早く！！\n\0":
'???',

# Makoto Hyuga
"あそこまで、走って！！\n\0":
'???',

# Shigeru Aoba
"早く、走って！\n\0":
'???',

# Ryoji Kaji
"走って！\nこっちへ！！\n\0":
'???',

# Toji Suzuhara 
"早う、走って！！\n早う、早う！！\n\0":
'???',

# Kaworu Nagisa 
"走って！！\n\0":
'???',

# Shinji Ikari
"えっっ！？\n\0":
'???',

# Asuka Soryu Langley
"キャあ！？\n\0":
'???',

# Rei Ayanami 
"何…！？\n\0":
'???',

# Misato Katsuragi 
"ど、どうして…？\n\0":
'???',

# Gendo Ikari
"何だ、どうした！？\n\0":
'???',

# Kozo Fuyutsuki
"き、君は…！？\n\0":
'???',

# Ritsuko Akagi 
"何、どうしたのよ…！？\n\0":
'???',

# Maya Ibuki 
"キャッ…！？\n\0":
'???',

# Makoto Hyuga
"いてッ！？\nそんなに掴まなくても…。\n\0":
'???',

# Shigeru Aoba
"えっ！？\nえええええっ！？\n\0":
'???',

# Ryoji Kaji
"な、何なんだ！？\n\0":
'???',

# Hikari Horaki
"キャッ、痛い！！\n\0":
'???',

# Toji Suzuhara 
"どわぁぁ！？\n何なんやッ！！\n\0":
'???',

# Kensuke Aida
"ウワー！？\n走るってどこへー！！\n\0":
'???',

# Kaworu Nagisa 
"手、痛いよ！！\n一体どこへ…！！\n\0":
'???',

#
# ./USRDIR/event/f026.har_EXTRACT/f026.evs
#
# [Text Only - No Designated Speaker]
"$aの目の前に\n黒服の男達が立ちはだかった。\n\0":
'Men in black stood before $a, blocking the way.\n\0',

# Shinji Ikari
"しまった…。\nこんなところで…！！\n\0":
'???',

# Asuka Soryu Langley
"狙われてるのはわかってたのに。\nウカツだったわ…。\n\0":
'???',

# Misato Katsuragi 
"どきなさい！\nアンタ達に殺されるワケにゃあ\nいかないのよ。\n\0":
'???',

# Ritsuko Akagi 
"手が込んでるわね…。\nそんな大人数で囲まなくっても\n私一人くらい殺せるでしょ。\n\0":
'???',

# Maya Ibuki 
"私、何も言ってない。\nだから、だから、殺さないで…。\n\0":
'???',

# Makoto Hyuga
"クソ、１対６か…。\n分が悪いな。\n\0":
'Damn, it\'s one against six...\nThose aren\'t good odds.\n\0',

# Shigeru Aoba
"くそ、囲まれた…。\nイチかバチか、走るしかない！！\n\0":
'???',

# Ryoji Kaji
"今度は何人で来た…？\nずいぶんと、\nてこずらせてきたからな。\n\0":
'???',

# Toji Suzuhara 
"こンのぉ、\n殺られてたまるか！！\n\0":
'???',

# Kaworu Nagisa 
"………逃げないよ。\nさあ、撃つといい。\n\0":
'...I won\'t run.\nGo ahead and shoot me.\n\0',

# [Text Only - No Designated Speaker]
"一発の銃弾が身体を突き飛ばした。▽\n薄れる意識の中で最後に見たものは\n冷たい地面に広がる\n自分の血だまりだった。\n\0":
'I was struck by a single bullet.▽\nThe last thing I saw as my senses dimmed\nwas a puddle of my own blood\nspreading over the cold ground.\n\0',

# Shinji Ikari, Kensuke Aida
"しまった…。\n\0":
'???',

# Asuka Soryu Langley
"くっ…。\n\0":
'???',

# Misato Katsuragi 
"…チィ。\n\0":
'???',

# Maya Ibuki 
"…やだ、殺さないで…。\n殺さないで…。\n\0":
'No, don\'t kill me...\nPlease don\'t kill me...\n\0',

# Makoto Hyuga
"くそ…。\n\0":
'???',

# Shigeru Aoba
"チッ…。\n\0":
'???',

# Ryoji Kaji
"…どうやら、ここまでのようだな。\n\0":
'???',

# Hikari Horaki
"ひ、人を呼ぶわよ…！！\n\0":
'???',

# Toji Suzuhara 
"殺る気やな…。\nほな、こっちから行ったるわ！！\n\0":
'???',

# Kensuke Aida
"くっそぉぉぉ！！\n\0":
'???',

# Kaworu Nagisa 
"抵抗はしない…。\nほら、撃つといいよ。\n僕の気が変わらないうちに…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、何かの気配を感じ、\n周りを見渡した。\n\0":
'All of a sudden, I sensed a presence, and I surveyed my surroundings.\n\0',

# Shinji Ikari
"僕を追ってきたんだな。\nよし、この道は引き返そう。\n\0":
'???',

# Asuka Soryu Langley
"この先に、いるわね。\nそうはいくもんですか…。\n\0":
'???',

# Rei Ayanami 
"この先に、いるみたいね。\n\0":
'???',

# Misato Katsuragi 
"いる。\n待ち伏せするつもりね。\n\0":
'???',

# Gendo Ikari
"…そこに、いるな。\n二人…、いや、三人か…。\n\0":
'There they are.\nTwo, no, three of them...\n\0',

# Kozo Fuyutsuki
"奴等か…、\nその角から追いつめるつもりだな。\nならば…。\n\0":
'???',

# Ritsuko Akagi 
"………いる。▽\n今度は待ち伏せるつもりね。\n\0":
'???',

# Maya Ibuki 
"この先、\n引き返した方がよさそうだわ。\n\0":
'???',

# Makoto Hyuga
"おっと、この先にいるな…。\nここは引き返しておこう…。\n\0":
'???',

# Shigeru Aoba
"またいやがる。\nしつこい野郎だぜ。\nさて、どうやって、まこうか。\n\0":
'???',

# Ryoji Kaji
"いるな…。\nさて、まくにはどっちに走るか…。\n\0":
'???',

# Toji Suzuhara 
"おるんやわ、そこに…。\n今なら、走って逃げれるわ。\n\0":
'???',

# Kaworu Nagisa 
"引き返して、別を行こう。\n\0":
'???',

# [Text Only - No Designated Speaker]
"危険な気配を感じ、\nその場を離れた…。\n\0":
'Sensing a dangerous presence, I got out of there...\n\0',

# [Text Only - No Designated Speaker]
"黒服の男とすれ違った。\n\0":
'The man in black just missed me.\n\0',

# Shinji Ikari
"…あぶない、行かなくちゃ。\n\0":
'???',

# Asuka Soryu Langley
"多分、今のは…。\n\0":
'???',

# Rei Ayanami 
"追った方がよさそうね。\n\0":
'???',

# Misato Katsuragi 
"…ハッ、今のは！？\n\0":
'???',

# Gendo Ikari
"…いかん、あいつらは。\n\0":
'???',

# Kozo Fuyutsuki
"まさか、あいつは…。\n\0":
'???',

# Ritsuko Akagi 
"今のは何かしら…。\n怪しいわね…。\n\0":
'???',

# Maya Ibuki 
"ひょっとして、今のは…。\n\0":
'???',

# Makoto Hyuga
"まずい、\nあいつらが出たという事は…。\n\0":
'???',

# Shigeru Aoba
"ヤバイ、追いつくか…？\n\0":
'???',

# Ryoji Kaji
"あいつら…、殺るつもりだな。\n\0":
'???',

# Toji Suzuhara 
"何や、銃なんか\nしまいよってからに…。\nいや、まてよ、ひょっとして…。\n\0":
'???',

# Kaworu Nagisa 
"このままじゃ危ない…！！\nあいつらを追わないと。\n\0":
'???',

# [Text Only - No Designated Speaker]
"黒服の男を追うと、\n$aをつけているようだった。▽\n危険を察知し、\n急いで$aに駆け寄った。\n\0":
'When I pursued the men in black,\nit looked like they were following $a.▽\nSensing danger, I hurriedly ran over to $a.\n\0',

# Shinji Ikari
"あぶない！\nここを引き返して、走って！！\n\0":
'???',

# Asuka Soryu Langley
"早く！！\n走って、引き返して！！\n\0":
'???',

# Rei Ayanami 
"今来た道を走るわ。\n\0":
'???',

# Misato Katsuragi 
"はやく、こっちへ！！\n人がいる方へ走って！！\n\0":
'???',

# Gendo Ikari
"走れ、早くしろ！！\n\0":
'Get out of here, hurry!\n\0',

# Kozo Fuyutsuki
"こっちへ来るんだ！！\n\0":
'???',

# Ritsuko Akagi 
"引き返して！\n早く、走って！！\n\0":
'???',

# Maya Ibuki 
"ここは危険、走って！！\n早く！！\n\0":
'???',

# Makoto Hyuga
"引き返して、その方が\n安全だ！！\n\0":
'???',

# Shigeru Aoba
"早く走って！！\n手は放さないで！！\n\0":
'???',

# Ryoji Kaji
"今来た道を、そのまま戻って！\n\0":
'???',

# Toji Suzuhara 
"その先はアカン！\nこっちに走って！！\n\0":
'???',

# Kaworu Nagisa 
"走って！！\nこの先は危ない！！\n\0":
'???',

# Shinji Ikari
"わぁっ！？\n一体どこから…？\n\0":
'???',

# Asuka Soryu Langley
"ちょっと、放して！！\n痛いぃ！！\n\0":
'???',

# Rei Ayanami 
"…ッ！？\n\0":
'???',

# Misato Katsuragi 
"えっ、そんな！！\n何がどうなって…！？\n\0":
'???',

# Gendo Ikari
"追手か。\n…すまんな！！\n\0":
'???',

# Kozo Fuyutsuki
"君、まさか奴等が…？\n\0":
'???',

# Ritsuko Akagi 
"ちょっと、\nそんなに引っ張ったら痛い…！！\n\0":
'???',

# Maya Ibuki 
"きゃあ、何っ！？\n\0":
'???',

# Makoto Hyuga
"ウワッ、何だ！？\n\0":
'???',

# Shigeru Aoba
"ちょっ、\nま、待った…！！\n\0":
'???',

# Ryoji Kaji
"いてて！！\n\0":
'???',

# Hikari Horaki
"きゃああ！？\n\0":
'???',

# Toji Suzuhara 
"な、何やわからんけど、\n走るんか！？\n\0":
'???',

# Kensuke Aida
"何、何！？\nま、待ってよ！！\n\0":
'???',

# Kaworu Nagisa 
"痛い…！！\nどこへ連れて行くんだ！？\n\0":
'???',

# [Text Only - No Designated Speaker]
"$aの腕をつかんで、\n全速力でその場を離れた。\n\0":
'I grabbed $\'s arm and\ngot them out of there posthaste.\n\0',

#
# ./USRDIR/event/f027.har_EXTRACT/f027.evs
#
# Shinji Ikari
"………あなただったんですね。\n\0":
'???',

# Asuka Soryu Langley
"私をずっと狙っていたのは、\nアンタだったのね。\n\0":
'???',

# Misato Katsuragi 
"…今度ばかりは、\n逃がさないつもりね。\n\0":
'???',

# Ritsuko Akagi 
"…どうやら、\n逃げられそうにないみたいね。\n\0":
'???',

# Maya Ibuki 
"…いや、▽\n殺さないで………。\n\0":
'???',

# Makoto Hyuga
"クソ、…逃げられないか。\n\0":
'???',

# Shigeru Aoba
"年貢の納め時か…。\n\0":
'???',

# Ryoji Kaji
"おやおや、\n逃げ切れたと思ったんだがね。\nやるじゃないか。\n\0":
'???',

# Toji Suzuhara 
"お前ら………。\n\0":
'You guys......\n\0',

# Kaworu Nagisa 
"逃げたりはしないよ。▽\nそれじゃ、\nさっさと済ませてくれないかな。\n\0":
'???',

# Shinji Ikari
"そんな、こんなところに…。\n\0":
'???',

# Asuka Soryu Langley
"まいたハズだったのに、\nそんな…。\n\0":
'???',

# Misato Katsuragi 
"くっ、\nうまく追い込んだわね…。\n\0":
'???',

# Ritsuko Akagi 
"私を消すなんて、\n思いきった選択をしたものだわ。\n\0":
'???',

# Maya Ibuki 
"嫌、嫌ぁぁあ…！！\n撃たないで、撃たないでぇぇ…！！\n\0":
'???',

# Makoto Hyuga
"くそ、後ろにもか…。\n今度こそ、殺る気だな。\n\0":
'???',

# Shigeru Aoba
"しまった、逃げ道が…。\n\0":
'???',

# Ryoji Kaji
"やれやれ、\nどうやら、\n逃がしてもらえないみたいだな。\n\0":
'???',

# Toji Suzuhara 
"いつから、追ってたんや…。\n\0":
'???',

# Kaworu Nagisa 
"殺るなら、さっさと殺ってくれ。\n出来れば、誰にもわからないように\n始末して欲しい。\n\0":
'???',

# [Text Only - No Designated Speaker]
"誰かが自分をつけているような\n気配がする…。\n\0":
'???',

# Shinji Ikari
"また、つけられているんだ。\n逃げなくちゃ…。\n\0":
'???',

# Asuka Soryu Langley
"フン、\n捕まってたまるもんですか！！\n\0":
'???',

# Rei Ayanami 
"…まただわ。\n誰かがつけてきた。\n\0":
'???',

# Misato Katsuragi 
"…さて、どうやって\n逃げ切ろうかしら。\n\0":
'???',

# Ritsuko Akagi 
"ここからなら、\nまだ逃げ切れるわ。\n\0":
'???',

# Maya Ibuki 
"一気に走れば、\n何とかふりきれるわね…。\n\0":
'???',

# Makoto Hyuga
"囲い込むほど、\n人は集まってないようだな…、\nよし。\n\0":
'???',

# Shigeru Aoba
"後ろの方が多そうだな。\nこのまま先まで走ったほうが\nよさそうだ。\n\0":
'???',

# Ryoji Kaji
"まあ、大丈夫か。\nこの数なら逃げ切れる。\n\0":
'???',

# Toji Suzuhara 
"まだ、そんなに多くはおらんな。\nよっしゃ、走って逃げた方がええわ。\n\0":
'???',

# Kaworu Nagisa 
"まだ、僕を狙っている…。\nしつこい人たちだ。\n\0":
'???',

# Shinji Ikari
"きっと、あれは…。\n\0":
'???',

# Asuka Soryu Langley
"アイツが狙っているのは…。\n\0":
'???',

# Rei Ayanami 
"いけない、彼らはきっと…！\n\0":
'???',

# Misato Katsuragi 
"あれは………。▽\nこのままだと、危ないわ！！\n\0":
'???',

# Gendo Ikari
"…まさか、\n本当だとすると危ないな。\n\0":
'???',

# Kozo Fuyutsuki
"奴等の狙いは、まさか…！！\n\0":
'???',

# Ritsuko Akagi 
"今の、嫌な予感がするわね…。\n\0":
'???',

# Maya Ibuki 
"もしかして…。▽\nどうしよう、助けないと…。\n\0":
'???',

# Makoto Hyuga
"奴等だ、…くそっ。\n奴等をまくにはどうすればいい…？\n\0":
'???',

# Shigeru Aoba
"まだ間に合う。\n奴等が狙っているのは、きっと…。\n\0":
'???',

# Ryoji Kaji
"このままでは殺されるな。\n先回りするか。\n\0":
'???',

# Toji Suzuhara 
"ひょっとしたら、\nひょっとするかもしれへん…。\n後、つけてみな…。\n\0":
'???',

# Kaworu Nagisa 
"彼等が探しているのは、\nもしかして…。\n\0":
'???',

# Shinji Ikari
"あぶない！\nここにいちゃダメだ！！\n\0":
'???',

# Asuka Soryu Langley
"早く！！\n囲まれるわ！！\n\0":
'???',

# Rei Ayanami 
"走るわ。\n追ってくるでしょうけど。\n\0":
'???',

# Misato Katsuragi 
"こっちへ！！\nうまくまくのよ！！\n\0":
'???',

# Gendo Ikari
"走れ！\n\0":
'Hurry!\n\0',

# Kozo Fuyutsuki
"向こうは銃を持っている。\n走れ！！\n\0":
'???',

# Ritsuko Akagi 
"ここを離れて、走るのよ！！\n\0":
'???',

# Maya Ibuki 
"私の手をしっかり握って！\nこっちへ走って！！\n\0":
'???',

# Makoto Hyuga
"走って！！\n立ち止まらずに走って！！\n\0":
'???',

# Shigeru Aoba
"危ない、こっちへ！！\n奴等、先回りしている！！\n\0":
'???',

# Ryoji Kaji
"しばらく我慢して、\n向こうまで走って！！\n\0":
'???',

# Toji Suzuhara 
"さっきから、つけられとる！！\n走って逃げるんや！！\n\0":
'???',

# Kaworu Nagisa 
"行ってはいけない。\nこの先で待ち構えて、\n撃つつもりなんだ！！\n\0":
'???',

# Shinji Ikari
"え、何だって…！？\n\0":
'???',

# Asuka Soryu Langley
"ちょっ、聞こえない。\n何よ！？\n\0":
'???',

# Rei Ayanami 
"うッ、…何なの！？\n\0":
'???',

# Misato Katsuragi 
"そんな、ウカツだったわ。\n追われていたなんて…。\n\0":
'???',

# Gendo Ikari
"奴等がいたのか…！？\n\0":
'???',

# Kozo Fuyutsuki
"君がなぜここに…！！\n\0":
'???',

# Ritsuko Akagi 
"そんなに走って、一体…。\n\0":
'???',

# Maya Ibuki 
"痛い、力をゆるめて…！！\n\0":
'???',

# Makoto Hyuga
"何てこった、\n追われてたなんて！！\n\0":
'???',

# Shigeru Aoba
"いてて、いてて、\nそんなに掴まなくっても…。\n\0":
'???',

# Ryoji Kaji
"今からまこうと思ったのに…、\nま、いいか…。\n\0":
'???',

# Hikari Horaki
"一体、何が…。\nえっ、えっ…！？\n\0":
'???',

# Toji Suzuhara 
"えっ、でも、\n今から行くとこ逆なんやで！！\n\0":
'???',

# Kensuke Aida
"び、びっくりした…。\n…な、どうしてここへ…？\n\0":
'???',

# Kaworu Nagisa 
"えっ！？\nつけていたのは、まさか…！？\n\0":
'???',

#
# ./USRDIR/event/f028.har_EXTRACT/f028.evs
#
# [Text Only - No Designated Speaker]
"$aの目の前に数人の黒服の\n男達が立ちはだかった。\n一斉に銃口を向ける。\n\0":
'???',

# Shinji Ikari
"わ、わぁぁぁぁぁーっ！！\n\0":
'???',

# Asuka Soryu Langley
"ひっ、いやああああああー！！\n\0":
'???',

# Misato Katsuragi 
"くっ、まだ死ねないのよ。\n…まだ。\n\0":
'???',

# Ritsuko Akagi 
"命乞いするつもりもないわ。\n…さあ、撃ったらどう？\n\0":
'???',

# Maya Ibuki 
"ひぃっ、\nう、撃たないで…。\n\0":
'???',

# Makoto Hyuga
"フン、\n知り過ぎた報いか…。\n\0":
'???',

# Shigeru Aoba
"フン、逃げてみせるさ。\nいつものようにな。\n…死んで、たまるかよ。\n\0":
'???',

# Ryoji Kaji
"今度ばかりは確実に消して\nこいと…。\nそう言われたみたいだな。\n\0":
'???',

# Toji Suzuhara 
"あかん、\n逃げ道なくなってもうた…。\n\0":
'???',

# Kaworu Nagisa 
"…あの人が僕を消すと判断したんだ。\n何も言わないよ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"$aの目の前に数人の黒服の\n男達が立ちはだかった。\n\0":
'???',

# Shinji Ikari
"…くそぉ、どうすれば。\n\0":
'???',

# Asuka Soryu Langley
"…こんなところにいたなんて。\n\0":
'???',

# Misato Katsuragi 
"…クッ、\nたいそうなお出迎えだこと。\n\0":
'???',

# Ritsuko Akagi 
"誰に消すように言われたのか、\nそれも教えて\nもらえないのかしら…？\n\0":
'???',

# Maya Ibuki 
"いや、いや、いやっ！！！\n死にたく、死にたくないぃぃ！！\n\0":
'???',

# Makoto Hyuga
"もはや、ここまでか…。\n\0":
'???',

# Shigeru Aoba
"これが俺の最期か。\n…へへ、何てこった。\n\0":
'???',

# Ryoji Kaji
"さすがに、\nこれじゃあ逃げられないな。\n\0":
'???',

# Hikari Horaki
"…それで、私を撃つのね。\n\0":
'???',

# Toji Suzuhara 
"くそぉ、\nこんなところで死ぬんか…！！\n\0":
'???',

# Kensuke Aida
"くっ！！\n\0":
'???',

# Kaworu Nagisa 
"誰が僕を消すと…？▽\nいや、やっぱりいい。\nさあ、早く僕を撃つといい。\n\0":
'???',

# [Text Only - No Designated Speaker]
"自分を狙っているであろう、\nあちこちから怪しい気配がする。\n立ち止まって、辺りを見回す。\n\0":
'???',

# Shinji Ikari
"あれは！？\n\0":
'???',

# Asuka Soryu Langley
"まさか…ね。\nつけてみた方がいいかしら。\n\0":
'???',

# Rei Ayanami 
"後を追った方がよさそうね。\n\0":
'???',

# Misato Katsuragi 
"怪しいわね。\n\0":
'???',

# Gendo Ikari
"…まさか、あいつを狙って。\n\0":
'???',

# Kozo Fuyutsuki
"今のは…。▽\n…早めに手を打った方が\nよさそうだな。\n\0":
'???',

# Ritsuko Akagi 
"…誰を狙ってるつもりかしら。\nひょっとして…。\n\0":
'???',

# Maya Ibuki 
"嫌な予感がするわ…。\n彼らは、ひょっとすると…。\n\0":
'???',

# Makoto Hyuga
"匂うな…。\n後を追ってみるか。\n\0":
'???',

# Shigeru Aoba
"奴等の車…、\nくそ、追いつけるか…。\n\0":
'???',

# Ryoji Kaji
"奴等、\nあいつを狙っているんだな。\n\0":
'???',

# Toji Suzuhara 
"奴等の狙いはきっと…。\nくそ、はよ行かな…。\n\0":
'???',

# Kaworu Nagisa 
"彼等の狙いは、きっと…。▽\nだとしたら、\nこうしてはいられないな。\n\0":
'???',

# Shinji Ikari
"しっかり掴まって！！\n走って！！\n\0":
'???',

# Asuka Soryu Langley
"私に掴まってて、\n早く走って！！\n\0":
'???',

# Rei Ayanami 
"掴まってて。\n…走るわ。\n\0":
'???',

# Misato Katsuragi 
"はやく！！\n急いで走って！！\n\0":
'???',

# Gendo Ikari
"逃げろ、逃げるんだ！！\n\0":
'???',

# Kozo Fuyutsuki
"全速力で走りだせ！\n奴等から逃げるんだ！！\n\0":
'???',

# Ritsuko Akagi 
"そこまで走ったら、人がいるわ。\nそしたら奴等も諦めるわ！！\n走って！！\n\0":
'???',

# Maya Ibuki 
"はやく、一緒に走って！！\n\0":
'???',

# Makoto Hyuga
"案の定だ！\n奴等が狙ってる、早く走って！！\n\0":
'???',

# Shigeru Aoba
"危ない！！\n奴等、銃口を向けていた。\n急いで逃げて！！\n\0":
'???',

# Ryoji Kaji
"こっちだ！！\n全力で走って！！\n\0":
'???',

# Toji Suzuhara 
"アカン、危ない！！\n猛ダッシュで走るんや！！\n\0":
'???',

# Kaworu Nagisa 
"こっちへ！！\n少しきついけど走って！！\n\0":
'???',

# Shinji Ikari
"わぁぁ、\n誰かと思ったらッ！？\n\0":
'???',

# Asuka Soryu Langley
"キャー、\n何すんの！？\n\0":
'???',

# Rei Ayanami 
"…誰！？\n\0":
'???',

# Misato Katsuragi 
"ええっ、こんなところで、\n一体何を！？\n\0":
'???',

# Gendo Ikari
"…走れば、いいんだな。\n\0":
'???',

# Kozo Fuyutsuki
"よくわからんが、\n君にまかせよう。\n\0":
'???',

# Ritsuko Akagi 
"ちょっとッ、\nそんなに早く走れないのに…。\n\0":
'???',

# Maya Ibuki 
"ま、待って、\nそんなに速く走れない…。\n\0":
'???',

# Makoto Hyuga
"まさか、\n追われていたなんて…、！？\n\0":
'???',

# Shigeru Aoba
"奴等が…、\nこっちで逃げれるのか…！？\n\0":
'???',

# Ryoji Kaji
"そっちにまで追われていたとは、\n驚きだよ…。\n\0":
'???',

# Hikari Horaki
"何で、何であんな奴等に\n追われる事になったのよッ！\n\0":
'???',

# Toji Suzuhara 
"うわあぁぁぁ、\nタンマ…、ちょっとタンマ！！\n\0":
'???',

# Kensuke Aida
"チクショウ！！\nどこまで走ればいいんだぁぁ！！\n\0":
'???',

# Kaworu Nagisa 
"僕の事を、\n心配して来てくれたんだ…。\n\0":
'???',

#
# ./USRDIR/event/f062.har_EXTRACT/f062.evs
#
# Seele 03
"ネルフ、そもそも我らゼーレの\n実行機関として結成されし組織。\n\0":
'???',

# Seele 05
"我らのシナリオを実践するために\n用意されたもの。\n\0":
'???',

# Seele 06
"だが、\n奴等は人類補完計画を\n利用しようとしている。\n\0":
'???',

# Seele 09
"左様。\nとんでもない事だよ。\n\0":
'???',

# Seele 02
"そうだ、約束の日の前に。▽\n取り返しのつかぬ事になる前に\nこちらから圧力をかけておく\n必要があるな。\n\0":
'???',

# Seele 01
"奴には、見せしめが必要だ。\n\0":
'???',

#
# ./USRDIR/event/f063.har_EXTRACT/f063.evs
#
# Makoto Hyuga
"こんなところで\n走っちゃ駄目だよ。\n何か用なのかい？\n\0":
'???',

# Kensuke Aida
"よぉ、\n息切らしてどうしたんだ？\n\0":
'???',

# Makoto Hyuga
"こんなところで走っちゃ\nいけませんよ。\n何か用なのでしょうか？\n\0":
'???',

# Shigeru Aoba
"ずいぶん\n慌てているみたいですけど。\n俺に、何か用ですか？\n\0":
'???',

# Ryoji Kaji
"あなたの命を狙うものが\nいるようです。▽\nあまり、人気のない場所に\n行かない方がよろしいかと。\n\0":
'???',

#
# ./USRDIR/event/f064.har_EXTRACT/f064.evs
#
# Shinji Ikari
"…？▽\n今の男の人…。\n何か、起きるかもしれない。\n\0":
'???',

# Asuka Soryu Langley
"…？▽\nあの黒服…、\n何かやらかすつもりなんだわ。\n\0":
'???',

# Rei Ayanami 
"…？▽\n…きっと、\n誰か、狙われているんだわ。\n\0":
'???',

# Misato Katsuragi 
"…？▽\n…まさか、\n奴等が狙っているのは…。\n\0":
'???',

# Gendo Ikari
"…？▽\n…ゼーレから来た客が\n紛れ込んできたようだな。\n\0":
'???',

# Kozo Fuyutsuki
"…？▽\n奴は…、ゼーレが差し向けたのか？\n\0":
'???',

# Ritsuko Akagi 
"…？▽\nあの黒服…、\nここの人間じゃないわね。\n\0":
'???',

# Maya Ibuki 
"…？▽\n今の男、\nネルフの人間じゃないわ。\n\0":
'???',

# Makoto Hyuga
"…？▽\nあいつは…、\nどうも引っかかるな…。\n\0":
'???',

# Shigeru Aoba
"…？▽\n今、奴等が持っていた写真は。\n…まさか！？\n\0":
'???',

# Ryoji Kaji
"…？▽\nさては、ゼーレが送り込んできたか。\n\0":
'???',

# Toji Suzuhara 
"…？▽\n嫌な予感がするわ。\nもしかしたら…。\n\0":
'???',

# Kaworu Nagisa 
"…？▽\n今の男…、\nゼーレが来たか…。\n\0":
'???',

# Shinji Ikari
"どうしたの？\nこんなところに連れ出して。\n\0":
'???',

# Asuka Soryu Langley
"ちょっと、何よ。\nこんなところに連れ出すなんて。\n\0":
'???',

# Rei Ayanami 
"何、\nこんなところに連れ出して…。\n\0":
'???',

# Misato Katsuragi 
"何かあったワケ？\nこんなところに連れ出すなんて…。\n\0":
'???',

# Gendo Ikari
"こんなところに連れ出して、\nどうするつもりだ。\n\0":
'???',

# Kozo Fuyutsuki
"一体何事かね？\nこんなところに連れ出すとは…。\n\0":
'???',

# Ritsuko Akagi 
"一体、何？\nこんなところに連れ出すなんて。\n\0":
'???',

# Maya Ibuki 
"どうしたのよ、\nこんなところに連れ出すなんて。\n\0":
'???',

# Makoto Hyuga
"こんなところに連れ出して、\nどうしたんだい？\n\0":
'???',

# Shigeru Aoba
"おいおい、こんなところに\n連れ出すなんて、どうしたんだよ？\n\0":
'???',

# Ryoji Kaji
"ちょっと待てよ、\nこんなところに連れ出して\n何をするつもりなんだ？\n\0":
'???',

# Hikari Horaki
"あんまり引っ張ると痛いわ。\nこんなところまで連れてきて、\nどうしたのよ。\n\0":
'???',

# Toji Suzuhara 
"なぁ、一体何なんや？\nこないなところに連れ出すなんて…。\n\0":
'???',

# Kensuke Aida
"おい、どうしてこんなところへ\n連れてきたんだよ。\n\0":
'???',

# Kaworu Nagisa 
"どうしたんだい、\nこんなところへ連れ出して。\n\0":
'???',

# Shinji Ikari
"どうしたんですか？\nこんなところに連れ出して。\n\0":
'???',

# Asuka Soryu Langley
"ちょっと、何なんですか？\nこんなところに連れ出すなんて。\n\0":
'???',

# Rei Ayanami 
"何、こんなところに連れ出して…。\nどうしたんですか？\n\0":
'???',

# Misato Katsuragi 
"何かあったんですか？\nこんなところに連れ出すなんて…。\n\0":
'???',

# Ritsuko Akagi 
"一体、何ですか？\nこんなところに連れ出すなんて。\n\0":
'???',

# Maya Ibuki, Kensuke Aida
"どうしたんですか？\nこんなところに連れ出すなんて。\n\0":
'???',

# Makoto Hyuga
"こんなところに連れ出して、\nどうしたんですか？\n\0":
'???',

# Shigeru Aoba
"こんなところに連れ出すなんて、\n何かあったんですか？\n\0":
'???',

# Ryoji Kaji
"ちょっと待って下さいよ、\nこんなところに連れ出して\n何をするつもりですか？\n\0":
'???',

# Hikari Horaki
"あんまり引っ張ると痛いです。\nそれに、こんなところまで連れて\nきて、どうしたんですか。\n\0":
'???',

# Toji Suzuhara 
"あの、一体何ですのん？\nこないなところに連れ出すなんて…。\n\0":
'???',

# Kaworu Nagisa 
"どうしたんですか、\nこんなところへ連れ出して。\n\0":
'???',

# Shinji Ikari
"だって、君を狙っている奴が\nいるみたいなんだよ。\n\0":
'???',

# Asuka Soryu Langley
"アンタを狙って、付け回している\n男がいるのよ！！\n\0":
'???',

# Rei Ayanami 
"あなたをつけ回している男が\nいるわ…。\n\0":
'???',

# Misato Katsuragi 
"あなたの事を狙っている\n男がいるわ。\n\0":
'???',

# Gendo Ikari
"お前の命を狙っている男がいる。\n\0":
'???',

# Kozo Fuyutsuki
"やれやれ、\n気がついていないとはな…。\n君を狙う男がいるようだぞ。\n\0":
'???',

# Ritsuko Akagi 
"あなたを狙っている男がいたわ。\nそいつを追って、\nあなたのところへ来たのよ。\n\0":
'???',

# Maya Ibuki 
"怪しい男が、つけてきているわ。\nあなたを狙って…。\n\0":
'???',

# Makoto Hyuga
"ずっと、君をつけている男が\nいるようなんだ。\n気をつけた方がいい。\n\0":
'???',

# Shigeru Aoba
"複数の男がお前の後をつけている。\n気をつけろ。\n\0":
'???',

# Ryoji Kaji
"どうやら君は狙われているようだ。\n誰かの代わりに…ね。\n\0":
'???',

# Toji Suzuhara 
"うさんくさいカッコした男が、\nつけ狙っとるみたいやぞ。\nせやから、教えに来たんじゃ。\n\0":
'???',

# Kaworu Nagisa 
"君を狙っている男がいる。\n身に覚えはないかもしれないけど、\n気をつけていてくれ。\n\0":
'???',

# Shinji Ikari
"だって、\nあなたを狙っている奴が\nいるみたいなんですよ。\n\0":
'???',

# Asuka Soryu Langley
"あなたを狙って、付け回している\n男がいるんですよ！！\n\0":
'???',

# Rei Ayanami 
"あなたをつけ回している男が\nいるみたいです…。\n\0":
'???',

# Misato Katsuragi 
"あなたの事を狙っている\n男がいるようですが。\n\0":
'???',

# Ritsuko Akagi 
"あなたを狙っている男がいます。\n今は、姿を消しているようですが\nくれぐれも注意なさって下さい。\n\0":
'???',

# Maya Ibuki 
"怪しい男が、つけて来ています。\nあなたを狙って…。\n\0":
'???',

# Makoto Hyuga
"ずっと、あなたをつけている男が\nいるようです。\n気をつけた方がよろしいかと。\n\0":
'???',

# Shigeru Aoba
"複数の男が後をつけているようです。\n気をつけて下さい。\n\0":
'???',

# Ryoji Kaji
"どうやらあなたは狙われている\nようですよ。\n誰かの代わりに…ね。\n\0":
'???',

# Toji Suzuhara 
"うさんくさいカッコした男が、\nつけ狙っとりましたよ。\nせやから、教えに来たんです。\n\0":
'???',

# Kaworu Nagisa 
"あなたを狙っている男がいる。\n身に覚えはないかもしれませんが、\n気をつけていて下さい。\n\0":
'???',

#
# ./USRDIR/event/f065.har_EXTRACT/f065.evs
#
# [Serious: Assassin (Pt.2?)]
#
# Shinji Ikari
"…？▽\nあいつは…、確か前にも。\n\0":
'???',

# Asuka Soryu Langley
"…？▽\n今のは…、アイツだわ…。\n\0":
'???',

# Rei Ayanami 
"…？▽\nあの男…、この間も…。\n\0":
'???',

# Misato Katsuragi 
"…？▽\nひょっとして、この間の…。\n\0":
'???',

# Gendo Ikari
"…？▽\nあいつか。\n性懲りもなく…。\n\0":
'???',

# Kozo Fuyutsuki
"…？▽\n奴は…、ゼーレの刺客だな。\n\0":
'...?▽The fellow\'s a Seele assassin.\n\-',

# Ritsuko Akagi 
"…？▽\nあの男…、今度は誰を…。\n\0":
'???',

# Maya Ibuki 
"…？▽\nあの男が持っていたのは、\n偽造ＩＤ？\nだとしたら…。\n\0":
'???',

# Makoto Hyuga
"…？▽\n待てよ、確かこの間の…。\n\0":
'???',

# Shigeru Aoba
"…？▽\nあいつ！\n…あの男がいるという事は…。\n\0":
'???',

# Ryoji Kaji
"…？▽\nゼーレの差し金か。\nもし、そうならば…。\n\0":
'???',

# Toji Suzuhara 
"…？▽\nアンニャロ…、\nまた誰か狙ってるんか？\n\0":
'???',

# Kaworu Nagisa 
"…？▽\nあの男…、\nゼーレが向けた人間だな…。\n\0":
'???',

# Shinji Ikari
"一体何だよ、\n急いでるのに…。\n\0":
'???',

# Asuka Soryu Langley
"ちょっと、私、\n急いでるんだけど…。\n\0":
'???',

# Rei Ayanami 
"何かしら…？\n私、急いでるんだけど…。\n\0":
'???',

# Misato Katsuragi 
"ねー、急いでるんだけど。\n何か用？\n\0":
'???',

# Gendo Ikari
"私は今忙しい。\n用なら、早く言え。\n\0":
'???',

# Kozo Fuyutsuki
"私は用事があるんだよ。\n話があるなら手短に頼むよ。\n\0":
'???',

# Ritsuko Akagi 
"なあに？\n私、急いでるのよ。\n\0":
'???',

# Maya Ibuki 
"私、急いでるんだけど…。\n用事なの？\n\0":
'???',

# Makoto Hyuga
"まいったな、急いでるんだけど。\n何か用かな…。\n\0":
'???',

# Shigeru Aoba
"俺、急いでるんだけど…。\n何か話があるの？\n\0":
'???',

# Ryoji Kaji
"何か用か？\nちょっと急いでるんだが…。\n\0":
'???',

# Hikari Horaki
"急いでるんだけど…、\n何か用なの？\n\0":
'???',

# Toji Suzuhara 
"ワシ、急いどんのや。\n何か用かいな？\n\0":
'???',

# Kensuke Aida
"何だ、何か用？\n俺、急いでるんだけど。\n\0":
'???',

# Kaworu Nagisa 
"ちょっと急いでるんだけど…。\n僕に何か用だったのかい？\n\0":
'???',

# Shinji Ikari
"一体何ですか、\n僕、急いでるんですけど…。\n\0":
'???',

# Asuka Soryu Langley
"ちょっと、私、\n急いでるんですけど…。\n\0":
'???',

# Rei Ayanami 
"何ですか…？\n私、急いでるんですけど…。\n\0":
'???',

# Misato Katsuragi 
"あのー、私、ちょっと\n急いでるんですけど。\n何か用ですか？\n\0":
'???',

# Ritsuko Akagi 
"何でしょうか？\n私、急いでいるんですが。\n\0":
'???',

# Maya Ibuki 
"私、急ぐんですけど…。\n用事でしょうか？\n\0":
'???',

# Makoto Hyuga
"あの、急いでるんですけど。\n何か用ですかね…。\n\0":
'???',

# Shigeru Aoba
"ちょっと、急いでるんですけど…。\n何か話でも…？\n\0":
'???',

# Ryoji Kaji
"何か用でしょうか？\n今、ちょっと急いでるんですが…。\n\0":
'???',

# Hikari Horaki
"私、急いでるんですけど…、\n何か用ですか？\n\0":
'???',

# Toji Suzuhara 
"ワシ、急ぐんですけど…。\n何か用ですか？\n\0":
'???',

# Kensuke Aida
"何か用ですか？\n俺、急いでるんですけど。\n\0":
'???',

# Kaworu Nagisa 
"ちょっと急いでるんですけど…。\n僕に何か用だったんですか？\n\0":
'???',

# Shinji Ikari
"その…どうしても話さないと\nいけないと思って。▽\n君の命を狙っている男がいるんだよ。\n\0":
'???',

# Asuka Soryu Langley
"その前に話を聞いて！\nアンタの命を狙ってる男がいるわ。\n今も側に。…気を付けなさいよ！\n\0":
'???',

# Rei Ayanami 
"命を狙われてるのよ、あなた。\nきっと、今も覗ってるわ。\n気をつけて…。\n\0":
'???',

# Misato Katsuragi 
"急いでるところを悪かったわね。\nその前に、アンタの事、\n何者かが狙っているのよ。▽\n気を付けなさいよ。\n\0":
'???',

# Gendo Ikari
"それは悪かったな。\nだが、何者かが\nお前の命を狙っている。\n\0":
'???',

# Kozo Fuyutsuki
"そうか、では、気づいていたのかな。\n君の命が狙われている事を…。\n\0":
'???',

# Ritsuko Akagi 
"あまり出歩かない方がいいわよ。\nあなたを狙ってる人間がいるのよ。\n\0":
'???',

# Maya Ibuki 
"でも、これだけは聞いて。\nあなたを殺そうと、\n狙っている男がいるわ。\n\0":
'???',

# Makoto Hyuga
"こっちも君に急用なんだよ。\nいいかい、\n君を狙っている男がいるようだ。▽\nよく、注意して行動するんだ。\nいいな。\n\0":
'???',

# Shigeru Aoba
"そんな事より、いいか、聞け！\nお前、命を狙われてるぞ！！\n\0":
'???',

# Ryoji Kaji
"そりゃ悪かったな。\nだが、お前は命を狙われているんだ。▽\nきっと、今もつけてきているはずだ。\n気をつけろよ。\n\0":
'???',

# Toji Suzuhara 
"せやけどお前、狙われとるんやで。\n悠長にしとる場合やないぞ。\nええか、気ぃつけとけよ…。\n\0":
'???',

# Kaworu Nagisa 
"僕も急ぎだったんだ。\n君が無事か心配だったからね。▽\n君は、命を狙われているんだ。\nある男にね…。\n\0":
'???',

# Shinji Ikari
"その…どうしても話さないと\nいけないと思って。▽\nあなたの命を狙っている男が\nいるみたいなんです。\n\0":
'???',

# Asuka Soryu Langley
"その前に話を聞いて！\nあなたの命を狙ってる男がいるわ。\n今も、きっと側に。▽\n…気をつけて下さいよ！\n\0":
'???',

# Rei Ayanami 
"命を狙われています。\nきっと、今も覗ってるでしょう。\n気をつけて下さい…。\n\0":
'???',

# Misato Katsuragi 
"急いでるところ申し訳ありませんが、\nその前にあなたの命を\n狙っている者がいます。▽\nお気をつけて下さい。\n\0":
'???',

# Gendo Ikari
"それは悪かったな。\nだが、何者かがお前の命を\n狙っている。\n\0":
'???',

# Kozo Fuyutsuki
"そうか、\nでは、気づいていたのかな。\n君の命が狙われている事を…。\n\0":
'???',

# Ritsuko Akagi 
"あまり出歩かない方が\nよろしいですよ。▽\nあなたを狙ってる人間が\nいるようですから。\n\0":
'???',

# Maya Ibuki 
"これだけはお伝えしなければと\n思いまして…。▽\nあなたを殺そうと、狙っている\n男がいるみたいなんです。\n\0":
'???',

# Makoto Hyuga
"こっちも急用なんですよ。\nいいですか、あなたを\n狙っている男がいるようですよ。▽\nよく、注意して行動して下さい。\nいいですね。\n\0":
'???',

# Shigeru Aoba
"そんな事より、聞いて下さい！\n命を狙われています、外出は\n控えてもらえないでしょうか。\n\0":
'???',

# Ryoji Kaji
"そりゃ悪かったですな。\nですが、\n命を狙われているようですよ。▽\nきっと、\n今もつけてきているはずです。\nどうか、お気をつけ下さい。\n\0":
'???',

# Toji Suzuhara 
"せやけど、狙われとるんですよ。\n悠長にしとる場合やないですよ。\nホンマ、気ぃつけといて下さい…。\n\0":
'???',

# Kaworu Nagisa 
"僕もあなたに急ぎの用ですよ。\n無事か心配でしたからね。▽\n命を狙われているようです。\nある男に…。\n\0":
'???',

#
# ./USRDIR/event/f066.har_EXTRACT/f066.evs
#
# Shinji Ikari
"あの男…。\n誰を探しているんだ？\n\0":
'???',

# Asuka Soryu Langley
"あの男…。\n殺し屋だわ…。\n\0":
'That guy...\nHe\'s a hit man...\n\0',

# Rei Ayanami 
"あの男…。\nあとをつけた方がいいわね。\n\0":
'???',

# Misato Katsuragi 
"あの男…、\nネルフの人間じゃないわ。\n私の目は誤魔化せないわよ。\n\0":
'???',

# Gendo Ikari
"あの男…。\nそうか、あの老人達の仕業か。\n\0":
'That man...\nI see, so this is the old men\'s doing.\n\0',

# Kozo Fuyutsuki
"あの男…、\nフン、老人達の雑用係だな。\n\0":
'???',

# Ritsuko Akagi 
"あの男…。\nもしかして…。\n\0":
'???',

# Maya Ibuki 
"あの男…。\nそういえば、\nキナ臭い話になってたわね…。\n\0":
'???',

# Makoto Hyuga
"あの黒服の男は…。\n\0":
'???',

# Shigeru Aoba
"あの男…。\n何かを狙っているようだな。\n\0":
'???',

# Ryoji Kaji
"あの男…。\nゼーレめ、しつこい奴等だ。\n\0":
'???',

# Toji Suzuhara 
"あの男…。\nきっと殺し屋やわ。\n絶対、そうやわ…。\n\0":
'???',

# Kaworu Nagisa 
"あの男は…。\nゼーレが動くとは、厄介だな…。\n\0":
'???',

# Shinji Ikari
"あれ、どうしたの？\n怖い顔しちゃって…。\n\0":
'???',

# Asuka Soryu Langley
"キビシー顔して、どーかしたの？\n\0":
'???',

# Misato Katsuragi 
"どーしたの、真剣な顔\nしちゃって。\n\0":
'???',

# Gendo Ikari
"どうした…。\n\0":
'???',

# Kozo Fuyutsuki
"やあ、君か。\n気配がすると思ったら\n君だったんだな。\n\0":
'???',

# Ritsuko Akagi 
"いつになく、険しい顔ね。\nどうしたのかしら？\n\0":
'???',

# Maya Ibuki 
"フフフ、どうしたの？\nそんなに怖い顔しちゃって。\n\0":
'???',

# Makoto Hyuga
"お、そんなに険しい表情して\nどうしたんだ？\n\0":
'???',

# Shigeru Aoba
"俺、何かした？\nそんなに怖い顔して\nどーしたんだよ。\n\0":
'???',

# Ryoji Kaji
"険しい顔して、どうした？\n俺、何もしてないぞ。\n\0":
'???',

# Hikari Horaki
"ど、どうしたの？\nそんなに怖い顔して…。\n\0":
'???',

# Toji Suzuhara 
"何か、怒ってるんか？\nそないな顔して…。\n\0":
'???',

# Kensuke Aida
"ど、どうしたんだよ…。\n俺に何か怒ってるとか…。\n\0":
'???',

# Kaworu Nagisa 
"その顔、\n何か真剣な話のようだね。\n\0":
'???',

# Shinji Ikari
"どうしたんですか？\nそんなに、怖い顔して…。\n\0":
'???',

# Asuka Soryu Langley
"キビシー顔して、\nどーかしたんですか？\n\0":
'???',

# Rei Ayanami 
"何か…？\n\0":
'???',

# Misato Katsuragi 
"どうしたんですか、\n真剣な顔して…。\n何か深刻な事でも…。\n\0":
'???',

# Ritsuko Akagi 
"いつになく、険しい顔ですね。\nどうしたんですか？\n\0":
'???',

# Maya Ibuki 
"あの、何かありました？\nいえ、あまりにも険しい表情を\nされているものですから…。\n\0":
'???',

# Makoto Hyuga
"あの…、僕、何かしましたか？\nいえ、怖い顔をなさっている\nものですから…。\n\0":
'???',

# Shigeru Aoba
"あの、俺が何か…？\nえ、怒ってらっしゃるんじゃ、\nないんですか？\n\0":
'???',

# Ryoji Kaji
"おや？\n険しい顔して、どうされました？\n\0":
'???',

# Hikari Horaki
"ど、どうしたんですか？\nそんなに怖い顔して…。\n\0":
'???',

# Toji Suzuhara 
"何か、怒ってるんですか？\nそないなコワい顔して…。\n\0":
'???',

# Kensuke Aida
"ど、どうしたんですか…。\n俺に何か怒ってるとか…。\n\0":
'???',

# Kaworu Nagisa 
"その顔は、\n何か真剣な話のようですね。\n\0":
'???',

# Shinji Ikari
"黒服の男を見た？\nそいつが君を狙ってるんだ！\n\0":
'???',

# Asuka Soryu Langley
"黒服の男は？\nそいつ、ずっとアンタを\nつけ狙っているのよ。\n\0":
'???',

# Rei Ayanami 
"黒い服の男が、\nあなたをつけているわ。\n気をつけた方がいいわ。\n\0":
'???',

# Misato Katsuragi 
"気をつけるのよ。\n黒い服の男が\nあなたを狙っているわ。\n\0":
'???',

# Gendo Ikari
"黒服の男が、\nお前の命を狙っている。\n気をつけた方がいい。\n\0":
'???',

# Kozo Fuyutsuki
"黒服の男が、ずっと尾行している。▽\n君は今、\n命を狙われているようだぞ。\n\0":
'???',

# Ritsuko Akagi 
"黒服の男を見なかった？\nそいつが、\nあなたの命を狙っているのよ！\n\0":
'???',

# Maya Ibuki 
"ここから逃げて。\n黒服の男があなたの命を\n狙っているわ！！\n\0":
'???',

# Makoto Hyuga
"黒い服の男が、君をつけている。\nとにかくここを離れよう。\n\0":
'???',

# Shigeru Aoba
"黒服の男が、君を尾行している。\n恐らく、この先でも\n待ち構えているだろう。▽\n一緒にまくから、ついてくるんだ。\nいいな。\n\0":
'???',

# Ryoji Kaji
"黒服の男が君を狙っている。\n気をつけろ、奴はすぐ側にいる。\n\0":
'???',

# Toji Suzuhara 
"黒服の男がお前を狙ってる。\nずっとワイがつけて来たんや。\nよう、周り見て行動せえよ。\n\0":
'???',

# Kaworu Nagisa 
"黒服の男が、君を狙っている。\n彼等は、ネルフの人間じゃない。\nゼーレの人間だ…。\n\0":
'???',

# Shinji Ikari
"黒服の男を見ました？\nそいつがあなたを\n狙ってるみたいなんです！\n\0":
'???',

# Asuka Soryu Langley
"黒服の男は？\nそいつ、ずっとあなたを\nつけ狙っているのよ。\n\0":
'???',

# Rei Ayanami 
"黒い服の男が、\nあなたをつけています。\n気をつけて下さい。\n\0":
'???',

# Misato Katsuragi 
"お気をつけて下さい。\n黒い服の男があなたを狙っています。\n\0":
'???',

# Ritsuko Akagi 
"黒服の男を見ました？\nそいつが、\nあなたの命を狙っているようです。\n\0":
'???',

# Maya Ibuki 
"ここから逃げて下さい。\n黒服の男があなたの命を\n狙っているようなんです！！\n\0":
'???',

# Makoto Hyuga
"黒い服の男が、\nあなたをつけているようです。\nとにかくここを離れましょう。\n\0":
'???',

# Shigeru Aoba
"黒服の男が、\nあなたを尾行している。▽\n恐らく、この先でも\n待ち構えているでしょう。▽\n一緒にまくから、ついて来て下さい。\nいいですね。\n\0":
'???',

# Ryoji Kaji
"黒服の男が\nあなたを狙っているようです。▽\n相手は、\n恐らくゼーレのものと思われます。\n\0":
'???',

# Toji Suzuhara 
"黒服の男が狙ってるみたいですよ。\nずっとワイがつけてきました。\nよう、周り見て注意して下さい。\n\0":
'???',

# Kaworu Nagisa 
"黒服の男が、あなたを狙っています。▽\n奴等は、ネルフの人間じゃない。\nゼーレの人間ですよ…\n\0":
'???',

#
# ./USRDIR/event/f080.har_EXTRACT/f080.evs
#
# Serious: Ireul Attack
#
# Ritsuko Akagi 
"出来たわ…。\n\0":
'???',

# Shinji Ikari
"もう、駄目かも…。\n\0":
'???',

# Asuka Soryu Langley
"変な期待は\nもう、よした方がイイわね…。\nあ〜ぁ。\nあと３０分…。\n\0":
'???',

# Rei Ayanami 
"あと１時間…。\n\0":
'One hour remaining...\n\0',

# Ritsuko Akagi 
"これでおしまいよ！！\n\0":
'???',

# Ritsuko Akagi 
"あと１時間…。\n本当のラストスパートね。\n\0":
'???',

# Maya Ibuki 
"カスパーを乗っ取られるのも\n時間の問題だわ。\nああ、センパイ…。\n\0":
'???',

# Makoto Hyuga
"１時間もあれば大丈夫だ。\n赤木博士なら…、きっと\nプログラムを完成させるはず…だ。\n\0":
'???',

# Shigeru Aoba
"このままじゃ、ホントにここが\n爆破されちまう…。\nあぁ…くそっ。\n\0":
'???',

# Ritsuko Akagi 
"間に合わなかった…！！\n頼りにしていたバルタザールまで\n乗っ取られるなんて！！\n\0":
'???',

# Ryoji Kaji
"次が駄目なら…、\nいよいよみんなと心中か。\nまあ、気長に待つさ。\n\0":
'???',

# Misato Katsuragi 
"私は諦めないわ…。\n\0":
'I won\'t give up...\n\0',

#
# ./USRDIR/event/f081.har_EXTRACT/f081.evs
#
# Makoto Hyuga
"赤木博士！！▽\nカスパー、\n１８秒後に乗っ取られます。\n\0":
'???',

# Maya Ibuki 
"センパイ、急いで下さい！！▽\nカスパー、\n１８秒後に乗っ取られます。\n\0":
'???',

# Misato Katsuragi 
"リツコ！！\nカスパーが乗っ取られるわ。\n急いでっ！！\n\0":
'???',

# Ryoji Kaji
"…リッちゃん、急げ！！▽\nカスパーがやられる！！\n\0":
'???',

# Female Staff
"カスパー、\n１８秒後に乗っ取られます！！\n\0":
'???',


#
# ./USRDIR/event/f082.har_EXTRACT/f082.evs
#
# [Text Only - No Designated Speaker]
"怪しげな黒服の男が、\nまるで誰かを探しているようだ…。\n\0":
'???',

# Shinji Ikari
"…？▽\n何だか…、嫌な予感がする。\n\0":
'???',

# Asuka Soryu Langley
"…？▽\n何か、ニオウわね。\nあの黒服…。\n\0":
'???',

# Rei Ayanami 
"…？▽\nあの男…、誰かを探している。\n\0":
'???',

# Misato Katsuragi 
"…？▽\n誰かを探している。\n…まさか。\n\0":
'???',

# Gendo Ikari
"…？▽\nもしかして、奴は…。\n\0":
'???',

# Kozo Fuyutsuki
"…？▽\n奴は…、ひょっとすると…。\n\0":
'???',

# Ritsuko Akagi 
"…？▽\nあの黒服…。\n\0":
'???',

# Maya Ibuki 
"…？▽\n今の、どうも怪しいわね。\n\0":
'???',

# Makoto Hyuga
"…？▽\n諜報部のヤツか？\nこんなところで…。\n\0":
'???',

# Shigeru Aoba
"…？▽\nまさか…。\n\0":
'???',

# Ryoji Kaji
"…？▽\nあれは、ゼーレの人間？\nもしかして、奴は…。\n\0":
'???',

# Toji Suzuhara 
"…？▽\n何や、怪しい風貌やのー。\n…え、もし、本物やったら…。\n\0":
'???',

# Kaworu Nagisa 
"…？▽\n今の男…、見覚えがある。\nまさか…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"不吉な予感を感じ、$aの\nもとへ走った。\n\0":
'???',

# Shinji Ikari
"ど、どうしたの…？\n息なんか切らしちゃってさ。\n\0":
'???',

# Asuka Soryu Langley
"走って来るなんて、\n何慌ててんの？\n\0":
'???',

# Rei Ayanami, Hikari Horaki, Kaworu Nagisa
"どうしたの？\n\0":
'???',

# Misato Katsuragi 
"どーしたの？\n慌てちゃって。\n\0":
'???',

# Gendo Ikari
"どうした、\n話があるのなら早く言え。\n\0":
'???',

# Kozo Fuyutsuki
"何か用かね…？\n\0":
'???',

# Ritsuko Akagi 
"どうしたの、走って来るなんて。\n\0":
'???',

# Maya Ibuki 
"すごい汗。\nそんなに急いでどうしたの？\n\0":
'???',

# Makoto Hyuga
"こんなところで走っちゃ駄目だよ。\n何か用なのかい？\n\0":
'???',

# Shigeru Aoba
"ずいぶん慌てているみたいだけど。\n俺に、何か用かな？\n\0":
'???',

# Ryoji Kaji
"どうした、\n走り込んで来るなんて…。\n\0":
'???',

# Toji Suzuhara 
"何や、慌てて。\nまず、落ち着きや。\n\0":
'???',

# Kensuke Aida
"よぉ、息切らしてどうしたんだ？\n\0":
'???',

# Shinji Ikari
"ど、どうしたんですか…？\n息なんか切らして…。\n\0":
'???',

# Asuka Soryu Langley
"走って来るなんて、\n何慌てているんですか？\n\0":
'???',

# Rei Ayanami, Hikari Horaki, Kaworu Nagisa
"どうしたんですか？\n\0":
'???',

# Misato Katsuragi 
"どうしたんですか？\nそんなに慌てて。\n\0":
'???',

# Gendo Ikari
"どうした、\n話があるなら早く言え。\n\0":
'???',

# Ritsuko Akagi 
"どうしたんですか、\n走って来るなんて。\n\0":
'???',

# Maya Ibuki 
"すごい汗ですよ。\nそんなに急いでどうしたんですか？\n\0":
'???',

# Makoto Hyuga
"こんなところで\n走っちゃいけませんよ。\n何か用なのでしょうか？\n\0":
'???',

# Shigeru Aoba
"ずいぶん慌てているみたいですけど。\n俺に、何か用ですか？\n\0":
'???',

# Ryoji Kaji
"どうしました、\n走り込んで来るなんて…。\n\0":
'???',

# Toji Suzuhara 
"慌ててどないしたんですか？\nまず落ち着いて下さいよ。\n\0":
'???',

# Kensuke Aida
"あのー、\n息切らしてどうしたんですか？\n\0":
'???',

# Shinji Ikari
"怪しい男が、狙ってるんだ。\n気をつけた方がいい。\n\0":
'???',

# Asuka Soryu Langley
"アンタ、狙われてるわ。\nいい、気をつけるのよ！！\n\0":
'???',

# Rei Ayanami 
"あなたを狙っている人がいるわ。\nそれを、教えたかったの。\n\0":
'???',

# Misato Katsuragi 
"あなたを狙っている男がいるわ。\nいい、気をつけるのよ。\n\0":
'???',

# Gendo Ikari
"気をつけろ。\nお前の命を狙うものがいる。\n\0":
'???',

# Kozo Fuyutsuki
"何もなかったかね？\n君の命を狙うものがいるようだ。\n気をつけたまえ。\n\0":
'???',

# Ritsuko Akagi 
"あなた、狙われているわよ、\n…命を。\n気づかなかったの？\n\0":
'???',

# Maya Ibuki 
"無事だったのね。\nよく聞いて、\nあなたを狙っている人がいるわ。\n\0":
'???',

# Makoto Hyuga
"君を…、探してたんだ。\n君をつけ回している奴が\nいるみたいなんだ。\n\0":
'???',

# Shigeru Aoba
"探したよ…。\nお前を…、狙っている奴がいる。\n本当だ…、気をつけてほしいんだ。\n\0":
'???',

# Ryoji Kaji
"あまり、人気のない場所に行くな。\nつけられているぞ。\n\0":
'???',

# Toji Suzuhara 
"はぁ…、無事やった。\nお前な、狙われてるみたいやぞ。\n\0":
'???',

# Kaworu Nagisa 
"君が狙われてる事を知って…、\n探しに来たんだ。\n\0":
'???',

# Shinji Ikari
"怪しい男が、狙ってます。\n気をつけた方がいいですよ。\n\0":
'???',

# Asuka Soryu Langley
"なんてノンキなのかしら。\n命を狙われてるんですよ。\n\0":
'???',

# Rei Ayanami 
"命を狙っている人がいます。\nそれを、…教えに来ました。\n\0":
'???',

# Misato Katsuragi 
"あなたを狙っている男が\nいるようです。\n気をつけて下さい。\n\0":
'???',

# Ritsuko Akagi 
"あなたの命を狙う者がいます。\nお気を付け下さい。\n\0":
'???',

# Maya Ibuki 
"無事だったのですね。\nよく聞いて下さい、\nあなたを狙っている者がいます。\n\0":
'???',

# Makoto Hyuga
"探してたんですよ。\nあなたをつけ回している奴が\nいるみたいなんで…。\n\0":
'???',

# Shigeru Aoba
"探しましたよ…。\nあなたを…、\n狙っている男がいるようです。▽\nお気をつけ下さい。\n\0":
'???',

# Ryoji Kaji
"あなたの命を\n狙うものがいるようです。▽\nあまり、人気のない場所に\n行かない方がよろしいかと。\n\0":
'???',

# Toji Suzuhara 
"はぁ…、無事やったんですね。\n変な男に、狙われてるみたいですよ。\n\0":
'???',

# Kaworu Nagisa 
"あなたが狙われてる事を知って…、\n探しに来ました。\n\0":
'???',

# [Text Only - No Designated Speaker]
"$aに危険を知らせました。\n\0":
'???',

# [Text Only - No Designated Speaker]
"突然、$aは、黒服の男達に\n囲まれた！！\n\0":
'???',

#
# ./USRDIR/event/f083.har_EXTRACT/f083.evs
#
# [Text Only - No Designated Speaker]
"怪しげな黒服の男が、まるで\n誰かを探しているようだ…。\n\0":
'???',

# Kozo Fuyutsuki
"…？▽\n奴は…、\nゼーレが差し向けたのか？\n\0":
'???',

# Maya Ibuki 
"…？▽\n今の男、ネルフの人間じゃないわ。\n\0":
'???',

# Ryoji Kaji
"…？▽\nさては、\nゼーレが送り込んできたか。\n\0":
'???',

# Rei Ayanami 
"何、こんなところに\n連れ出して…。\n\0":
'???',

# Kensuke Aida
"おい、\nどうしてこんなところへ\n連れてきたんだよ。\n\0":
'???',

# Rei Ayanami 
"何、\nこんなところに連れ出して…。\nどうしたんですか？\n\0":
'???',

# Asuka Soryu Langley
"アンタを狙って、\n付け回している男がいるのよ！！\n\0":
'???',

# Shinji Ikari
"だって、あなたを狙っている奴が\nいるみたいなんですよ。\n\0":
'???',

#
# ./USRDIR/event/f084.har_EXTRACT/f084.evs
#
# Rei Ayanami 
"あの男…、この間も…。\n\0":
'???',

# Shinji Ikari
"その…どうしても話さないと\nいけないと思って。▽\n君の命を狙っている男が\nいるんだよ！\n\0":
'???',

# Rei Ayanami 
"命を狙われてるのよ、あなた。\nきっと、今も伺ってるわ。\n気をつけて…。\n\0":
'???',

# Makoto Hyuga
"こっちも君に急用なんだよ。\nいいかい、君を狙っている男が\nいるようだ。▽\nよく、注意して行動するんだ。\nいいな。\n\0":
'???',

# Ryoji Kaji
"そりゃ悪かったな。\nだが、お前は命を狙われているんだ。▽\nきっと、\n今もつけてきているはずだ。\n気をつけろよ。\n\0":
'???',

# Rei Ayanami 
"命を狙われています。\nきっと、今も伺ってるでしょう。\n気をつけて下さい…。\n\0":
'???',

# Misato Katsuragi 
"急いでるところ申し訳ありませんが、\nその前に…、あなたの命を\n狙っている者がいます。▽\nお気をつけて下さい。\n\0":
'???',

# Makoto Hyuga
"こっちも急用なんですよ。\nいいですか、あなたを狙っている\n男がいるようですよ。▽\nよく、注意して行動して下さい。\nいいですね。\n\0":
'???',

# Shigeru Aoba
"そんな事より、聞いて下さい！\n命を狙われています、\n外出は控えてもらえないでしょうか。\n\0":
'???',

# Kaworu Nagisa 
"僕もあなたに急ぎの用ですよ。\n無事か心配でしたからね。▽\n命を狙われているようです、\nある男に…。\n\0":
'???',

#
# ./USRDIR/event/f085.har_EXTRACT/f085.evs
#
# Misato Katsuragi 
"どーしたの、\n真剣な顔しちゃって。\n\0":
'???',

# Kensuke Aida
"ど、どうしたんですか…？\n俺に何か怒ってるとか…。\n\0":
'???',

# Misato Katsuragi 
"気をつけるのよ。\n黒い服の男があなたを狙っているわ。\n\0":
'???',

# Gendo Ikari
"黒服の男が、お前の命を狙っている。\n気をつけた方がいい。\n\0":
'???',

# Kozo Fuyutsuki
"黒服の男が、ずっと尾行している。▽\n君は今、命を狙われているようだぞ。\n\0":
'???',

# Shinji Ikari
"黒服の男を見ました？\nそいつがあなたを狙ってる\nみたいなんです！\n\0":
'???',

# Ritsuko Akagi 
"黒服の男を見ました？\nそいつが、あなたの命を狙って\nいるようです。\n\0":
'???',

# Shigeru Aoba
"黒服の男が、あなたを尾行している。▽\n恐らく、この先でも\n待ち構えているでしょう。▽\n一緒にまくから、ついて来て下さい。\nいいですね？\n\0":
'???',

# Toji Suzuhara 
"黒服の男が狙っとるみたいですよ。\nずっとワイがつけてきました。\nよう、周り見て注意して下さい。\n\0":
'???',

# Kaworu Nagisa 
"黒服の男が、あなたを狙っています。▽\n彼等は、ネルフの人間じゃない。\nゼーレの人間ですよ…\n\0":
'???',

#
# ./USRDIR/event/f030.har_EXTRACT/f030.evs
#
# Kensuke Aida
"ハハ、今ケンカしてんのが\n委員長の洞木。▽\nもう一人のジャージが\n鈴原トウジっていって\n俺のつれなんだ。▽\nあーぁ、それにしてもコリャ\n自習どころじゃなくなったな。\nいつものことだけど…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"教室では、授業終了のチャイムが\n鳴るまでトウジとヒカリが\n喧嘩を続けていた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"授業中、パソコンのディスプレイに\nクラスメイトからのメールが\n表示された。\n\0":
'???',

# [Text Only - No Designated Speaker]
"「あなたはパイロットですか？\n　Ｙ／Ｎ」\n\0":
'"Are you the pilot?\n Y/N"\n\0',

# [Text Only - No Designated Speaker]
"二列前の女子がこちらを覗っている。\nこのメールは彼女が\n送信したのだろうか。\n\0":
'???',

# [Text Only - No Designated Speaker]
"返事をタイプした。\n\0":
'I typed a response.\n\0',

# [Text Only - No Designated Speaker]
"「はい」\n\0":
'"Yes."\n\0',

# [Text Only - No Designated Speaker]
"送信…。\n\0":
'Transmitting...\n\0',

# [Text Only - No Designated Speaker]
"その途端、教室がどよめいた。\n全員にモニターされていたのか…。\n\0":
'???',

# Hikari Horaki, Male Staff
"静かに！！\n\0":
'???',

# Kensuke Aida
"いいんじゃねーの、委員長。\nどーせ、自習なんだしサ。\n\0":
'???',

# Hikari Horaki
"だから、静かにしておかなくちゃ\nいけないんじゃない。\n\0":
'???',

# Toji Suzuhara 
"おはようさん。\n\0":
'???',

# Hikari Horaki
"鈴原ってば、遅刻よ！\n\0":
'???',

# Toji Suzuhara 
"妹の見舞いや。\n朝からそんな、やいやい言うなや。\n\0":
'???',

# Kensuke Aida
"よ！\n君がパイロットなんだろ？\n\0":
'???',

# Shinji Ikari
"君は…？\n\0":
'???',

# Kensuke Aida
"あー、俺は相田ケンスケ。\nケンスケでいーよ。\n仲良くしようぜ。\n\0":
'???',

# Shinji Ikari
"僕は碇…、碇シンジ。\nあの…、よろしく。\n\0":
'???',

#
# ./USRDIR/event/f031.har_EXTRACT/f031.evs
#
# Shinji Ikari
"ねえねえ、\nさっきの体育の時間に\n女子のことチラチラ見てたよね。\n\0":
'???',

# Toji Suzuhara 
"なあ、お前、体育の時間、\n女子の方ばっかり見てたやろ？\n\0":
'???',

# Kensuke Aida
"なあ、お前さっきの体育の時間、\n女子のことジーと見てただろ？\n\0":
'???',

# Kaworu Nagisa 
"さっきの体育の時間、君はずっと\n女の子ばかり見ていたようだけど…。\n\0":
'???',

# Shinji Ikari
"え？　僕が…？\n\0":
'???',

# Toji Suzuhara 
"な、何や突然…。\n\0":
'???',

# Kensuke Aida
"俺が？\n\0":
'???',

# Kaworu Nagisa 
"そうかい？\n\0":
'???',

# Shinji Ikari
"そうそう、変な目で見てただろ。\n\0":
'???',

# Toji Suzuhara 
"何ちゅーたって、\n第二次成長絶好調、やもんなぁ。\nウヒヒヒヒヒ…。\n\0":
'???',

# Kensuke Aida
"うーん、わかるぜ、お前の気持ち。\nやっぱ、男の子だもんなぁ。\n\0":
'???',

# Kaworu Nagisa 
"興味があるのかい？\n\0":
'Are you interested?\n\0',

# Shinji Ikari
"ねえ、誰が気になるのさ、教えてよ。\n\0":
'???',

# Toji Suzuhara 
"お前も隅に置けんやっちゃな。\nで、誰なんや、気になるんは…。\n\0":
'???',

# Kensuke Aida
"秘密にしといてやるからさ、\n誰なの？\n教えてよ、気になる子をさ…。\n\0":
'???',

# Kaworu Nagisa 
"それで、\n君はどの娘に興味があるのかい？\n\0":
'???',

# Shinji Ikari
"そ、そんなんじゃないよ！\n\0":
'???',

# Toji Suzuhara 
"アホ！\nワシはナイッスバディな\nオネーサマしか興味あらへん。\n\0":
'???',

# Kensuke Aida
"いや、その、あの…。\n\0":
'???',

# Kaworu Nagisa 
"興味があるのは君だろう？\n僕はどちらかというと、\nそういう君に興味があるよ。\n\0":
'???',

# Asuka Soryu Langley
"アンタ、気を付けなさいよ。\n体育の授業中、男子から\n変な目で見られてたわよ。\n\0":
'???',

# Rei Ayanami 
"体育の授業中、\nあなたのことを\n見ていた男子がいたわ。\n\0":
'???',

# Hikari Horaki
"ねえ、さっき体育の授業で\n一部の男子が、あなたのこと、\nジーっと見てたのよ…。\n\0":
'???',

# Asuka Soryu Langley
"ゲッ！！\n何よソレ！！\n\0":
'???',

# Rei Ayanami,[Text Only - No Designated Speaker], Shinji Ikari, Makoto Hyuga
"…？\n\0":
'???',

# Hikari Horaki
"ヤダッ！！\n…それっ、本当？\n\0":
'???',

# Asuka Soryu Langley
"あいつらの頭の中、\n覗いてみたいものね。\n\0":
'???',

# Rei Ayanami 
"でも、別に悪意があるわけでは\nないんでしょう。\n\0":
'???',

# Hikari Horaki
"…ったく、もっと別の事に\n頭を使えないのかしら？\n\0":
'???',

# Asuka Soryu Langley
"そのうち仕返ししてやるわ。\n\0":
'???',

# Rei Ayanami 
"私は別に、気にしないわ。\n\0":
'???',

# Hikari Horaki
"ヤだな…、\nこれからもそんな風に\n見られるなんて…。\n\0":
'???',

#
# ./USRDIR/event/f033.har_EXTRACT/f033.evs
#
# [Students: School Trip]
#
# Asuka Soryu Langley
"ウ〜〜〜。\n\0":
'???',

# Toji Suzuhara
"トホホ…、\nせっかく、旅費の積立て\nしてたのになァ。\n\0":
'???',

# Ritsuko Akagi 
"ちょっと、アレ何かしら？\n\0":
'???',

# Maya Ibuki 
"一体、どうしたんでしょうね？\n\0":
'???',

# Shigeru Aoba
"ああ？\n何してるんだ？\n\0":
'???',

# Male Staff
"何か気まずい感じですね。\nどうしたんでしょうか？\n\0":
'???',

# Misato Katsuragi 
"今日から、修学旅行よ。\nでも、パイロットは使徒襲来に\n備えて待機になってるから。▽\nまぁ、まだ子供だもの。\n機嫌が悪くなるのは仕方ないわよ。\n\0":
'???',

# Makoto Hyuga
"今日から、\n修学旅行だったみたいで…。▽\nとはいえ、使徒襲来に備えて\n旅行に行けないものだから\nずっとあんなカンジで…。\n\0":
'???',

# Ryoji Kaji
"今日から修学旅行だったのさ。▽\n楽しみにしていたみたいだからな、\n行けなかったのが\n相当ショックだったんだろう。▽\nしょうがないサ。\n彼らの留守中に使徒が来ないとも\n限らんからな。\n\0":
'???',

# Female Staff
"ええ、\n今日から修学旅行だったらしくて。▽\n本人は、戦闘待機という事に\nなっていますからね。▽\nまあ、気持ちはわかります。\n\0":
'???',

# Asuka Soryu Langley
"せっかく新しい水着もそろえて、\n準備バッチＯＫだったってのにィ！▽\nしかも、当日に不参加を\n言い渡されるなんてアリ？\n\0":
'???',

# Shinji Ikari
"僕はうすうす、こうなるだろうって\n思ってたけどね。\n\0":
'???',

# Asuka Soryu Langley
"はー、つまんない。\nその上、よりによって、\nこんなつまんない男と一緒だなんて。\n\0":
'???',

# Shinji Ikari
"僕に当たる事はないだろ…。\n\0":
'???',

# Kaworu Nagisa 
"残念だね。\n僕、グループの班長になってたんだ。▽\nこんな事になって、みんなに\n迷惑かけているかもしれない。\n\0":
'???',

# Toji Suzuhara
"ワイかて、旅費出してもうて、\n当日キャンセルやから、\n金返ってけえへん…。\n\0":
'???',

# Kaworu Nagisa 
"そうか、キャンセル料まで\n取られるんだっけ…？\n\0":
'???',

# Toji Suzuhara
"ふひーーーーん…。\n泣きっ面に蜂やがな…。\n\0":
'???',

# Asuka Soryu Langley
"アンタも、ちょっと抗議しなさいよ。\n\0":
'???',

# Rei Ayanami, Shinji Ikari
"何を？\n\0":
'???',

# Asuka Soryu Langley
"アンタ何とも思わないの？\n修学旅行よ。\n\0":
'???',

# Rei Ayanami 
"行けない事、知っていたから。\n\0":
'???',

# Asuka Soryu Langley
"ハン、\nどーせアンタじゃ\n集団行動も出来ないだろうしね。▽\nアンタは行かなくて正解よ。\n\0":
'???',

# Misato Katsuragi 
"い〜い機会だわ。\n本部で勉強合宿でもしましょうか？▽\nここには、腕のいい家庭教師が\nたっくさんいるわよ〜ン。▽\n学校の勉強、遅れてるんでしょう？\nオホホホホ…、よかったわね〜。\n\0":
'???',

# Ritsuko Akagi 
"そう、いい機会だわ。\n本部で勉強合宿でもしましょうか？▽\nここにはいい家庭教師が\nいっぱいいるのよ。\n\0":
'???',

# Female Staff
"これを機会に、\n本部で勉強合宿でもしましょうか？▽\nここには、腕のいい家庭教師が\nたくさんいる事ですし。\n\0":
'???',

# Asuka Soryu Langley
"えーーー！？\n\0":
'???',

# Shinji Ikari
"勉強合宿…。\nこの展開は予想出来なかったな。\n\0":
'???',

# Kaworu Nagisa 
"僕は遠慮します。\n\0":
'???',

# Toji Suzuhara
"待機だけで充分です、ハイ。\nこの上、オベンキョ責めなんて\n殺生や〜…。\n\0":
'???',

#
# ./USRDIR/event/f035.har_EXTRACT/f035.evs
#
# [Text Only - No Designated Speaker]
"今日は学園祭当日。\n様々な出店、催し物が\n生徒主催で行われた。▽\n２年Ａ組は、みんなで色々なものを\n持ち寄ってフリーマーケットの店を\n出す事になった。\n\0":
'???',

# Shinji Ikari
"準備、何とか間に合ったね。\n\0":
'???',

# Asuka Soryu Langley
"フリーマーケットの店は、\n私達のクラスだけみたいね。\n\0":
'???',

# Rei Ayanami 
"私、会計当番だから。\n\0":
'???',

# Hikari Horaki
"ほら、商品の衣類は見やすいように\nたたむかハンガーにつるして。\n\0":
'???',

# Toji Suzuhara 
"他にも見て廻りたいんやけどな。\nああ、一年生の店のタコ焼き\n食いたいわ。\n\0":
'???',

# Kensuke Aida
"俺のゲームソフト、売れるかなぁ？\n\0":
'???',

# Kaworu Nagisa 
"出店の売り上げは、\n寄付する事になってるんだね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"保護者や学校近辺の人の姿も見える。\n学校はたくさんの人であふれて\n大賑わいだ。▽\nだけど、クラスの店の前には\n誰も足を止めようとしない…。\n\0":
'???',

# Misato Katsuragi 
"さっすがに、\nビールは売ってないわね〜。▽\nさて、忌々しい結婚式の引き出物、\nちゃんと始末してくれているかしら。\n\0":
'???',

# Maya Ibuki 
"わぁ、わたあめ！！\n懐かしいわぁ、一つちょうだい。\n\0":
'???',

# Makoto Hyuga
"みんな楽しそうだな。\n学生時代を思い出すなぁ。\n\0":
'???',

# Shigeru Aoba
"向こうはバンドの演奏ステージか。\n粗削りだけど、いい音だ。\n\0":
'???',

# Ryoji Kaji
"さて、２年Ａ組は…。\nまいったな、こう人が多いとは…。\n\0":
'???',

# Female Staff
"クレープっておいしいわぁ。\nあとはかき氷と、タイヤキね。\n\0":
'???',

# Shinji Ikari
"わっ！？\nど、どうしてここに…？\n\0":
'???',

# Asuka Soryu Langley
"ちょっと、どうしてここに？\n\0":
'???',

# Rei Ayanami 
"どうしてここに…？\n\0":
'???',

# Toji Suzuhara 
"ちょっ、\n何してんですか！？\n\0":
'???',

# Kaworu Nagisa 
"ええっ！\nどうしてここに？\n\0":
'???',

# Misato Katsuragi 
"あっ、いたいた！！\nチョッチ見に来てあげたのよ。▽\nどぉ？\nお店の方は。\n全然、お客いないじゃない。▽\n私が持たせた結婚式の\n引き出物だけでも\n売ってしまいなさいよ。\n\0":
'???',

# Maya Ibuki 
"フフフ、楽しそうね。\n私も楽しんでるわ。\n\0":
'???',

# Maya Ibuki 
"ホラ、見て。\nわたあめ、フフフフフフ。\n\0":
'???',

# Maya Ibuki 
"ねえ、でもここ…。\nガラーンとしてて、\nお客さんがいないじゃない。\n\0":
'???',

# Makoto Hyuga
"やあ、ここはフリーマーケットか。▽\nいや、いいねえ。\n僕はね、大学で学園祭の実行委員を\nやっていたんだよ。▽\nそれにしても、\nここはあまりお客がいないねぇ。▽\nもっと客寄せに力を入れないと\n売れないぞ。\n\0":
'???',

# Shigeru Aoba
"よう！\nフリマやってんのか。\n\0":
'???',

# Shigeru Aoba
"しかし、何じゃこれ？\nお菓子のオマケのカード…、\n古い型のケータイ…、▽\nこっちは靴かたっぽ、古雑誌…。\nこれ、売るつもりかよ…。▽\nおまけに客、いねえし…。\n\0":
'???',

# Ryoji Kaji
"仕事の一環さ。\nま、別に監視するつもりなんて\nさらさらないがね。▽\nホラ、差し入れ。\nもっと大きく声を出して\n客引っ張らないと売れないぞ。\n\0":
'???',

# Female Staff
"ちょっと、この近所に\n用事があったから寄ってみたの。\nもうクレープ３つも食べちゃった。▽\nそれにしてもこの店、\nガランとしてるわね。\n\0":
'???',

# Shinji Ikari
"そういや、売れたのは\n女子の手作りクッキーだけだ。\nあとは、誰も何も買ってくれない。\n\0":
'???',

# Asuka Soryu Langley
"こーして見ると、\nまるでいらないモノの\n寄せ集めだもんね…。▽\n私もあんまり買いたいとは\n思わないわね…。\n\0":
'???',

# Rei Ayanami 
"お客、来てなかったのね。\nどうりで、ヒマなはずだわ…。\n\0":
'???',

# Hikari Horaki
"品物の配置が悪いのかしら。\n\0":
'???',

# Hikari Horaki
"ほら、みんな頑張って！！\n手が空いてる人はチラシを配って\nお客さんに呼びかけて！\n\0":
'???',

# Toji Suzuhara 
"だーれも客来ぇへん…。\n売れへんかったら、またウチに\n持って帰らんとアカンのか…。\n\0":
'???',

# Kensuke Aida
"おかしいなぁ…、\nこの店だけ客が来ないよ。\n\0":
'???',

# Kaworu Nagisa 
"客寄せでもしよう。\nこのままじゃ、寄付金が集まらない。\n\0":
'???',

# [Text Only - No Designated Speaker]
"大きい声で呼び込みをしたり、\n品物の配置をかえてみたり…。▽\nクラスのみんなが\n躍起になって頑張っていた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"その成果もあって、\nクラスの出店は、大成功となった。▽\n店の売り上げは、数えた事のない\nほどの金額になり、そのままお金は\n恵まれない子供への寄付金となった。\n\0":
'???',

# Shinji Ikari
"まさか、こんなに売れるなんて…。\n\0":
'???',

# Asuka Soryu Langley
"ホント、売れたわねェ。\n私の作ったアクセサリーなんて、\n完売よ〜。\n\0":
'???',

# Rei Ayanami 
"今日の売り上げ、\n３４万６１９２円…。\n\0":
'???',

# Hikari Horaki
"みんな、よく頑張ったわ。\n\0":
'???',

# Toji Suzuhara 
"ワイの、出したんだけ\n売れ残っとるがな…。\n\0":
'???',

# Kensuke Aida
"楽しかったよね。\n来年もフリーマーケットがいいな。\n\0":
'???',

# Kaworu Nagisa 
"これで寄付が出来るんだね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"帰り道、クラスのみんなの顔は\n充実感をかみ締めてほころんでいた。▽\n疲れたけれど、\nとても楽しい一日だった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"その成果もあり、クラスの出店に\n何とかお客が来るようになった。▽\n予想していたよりも、\nなかなかの売り上げで、\nそのままお金は寄付金になった。\n\0":
'???',

# Shinji Ikari
"やっぱり、客引きって大事なんだな。\n\0":
'???',

# Asuka Soryu Langley
"やっぱり食器とか服とかって\n売れるのね。\n\0":
'???',

# Rei Ayanami 
"今日の売り上げ、\n１８万５３３０円…。\n\0":
'???',

# Hikari Horaki
"これだけ売れれば御の字よ。\nさあ、後片付けしましょ。\n\0":
'???',

# Toji Suzuhara 
"トホホォ…、ワイが出したん\n売れへんどころか壊されとるわ…。\n\0":
'???',

# Kensuke Aida
"やっぱり、食べ物の店って強いねえ。\nここの売り上げの３倍らしいよ。\n\0":
'???',

# Kaworu Nagisa 
"今日は楽しかったな。\n買ってくれなくっても、\n色んなお客さんと話が出来たよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"それなりに楽しい一日だった。▽\n片付けの後、先生のはからいで\n簡単な打ち上げをした。▽\n喉を通るジュースが、\nこんなにおいしいとは思わなかった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"けれども、クラスの出店には\n一向に客は入らず、\n閑古鳥が鳴いていた。▽\n売れ残った商品は\nそれぞれ持ち寄ったものを、\nめいめい持ち帰る事になった。\n\0":
'???',

# Shinji Ikari
"ちっとも売れなかった…。\nこれ、全部持って帰らなきゃ\nいけないんだよな…。\n\0":
'???',

# Asuka Soryu Langley
"…ったくもう！\nフリーマーケットやるなんて\n言ったの誰なのよ！！\n\0":
'???',

# Rei Ayanami 
"本日の売り上げ、\n５７００円…。\n\0":
'???',

# Hikari Horaki
"あんなに頑張ったのに…。\n\0":
'???',

# Toji Suzuhara 
"ワイ、ようけ持ってきたしなぁ…。\nまた、ウチまで持って帰るんか…。\n\0":
'???',

# Kensuke Aida
"チェッ、宣伝頑張ったのになぁ。\nノド、ガラガラだよ…。\n\0":
'???',

# Kaworu Nagisa 
"でも、いい勉強になったな。\n売り上げだけがすべてじゃないしね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"片付けの後の反省会は、\nほとんど聞いていなかった。▽\nただただ疲れて、\nみんな重い足を引きずり、\n家路についた。\n\0":
'???',

#
# ./USRDIR/event/f036.har_EXTRACT/f036.evs
#
# [Students: Shinji Playing Cello]
#
# Shinji Ikari
"…久しぶりに\nチェロでも弾いてみようかな。▽\n荷物を解かなきゃ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"おそらく、\nペンペンがつけたのであろう、\nテレビから拍手の音が聞こえていた。\n\0":
'???',

# Asuka Soryu Langley
"あら、この音はチェロ？\n誰が聴いているのかしら…。\n\0":
'???',

# Rei Ayanami 
"地を流れながら\n染み込んでいくような、\n力強く静かな音…。\n\0":
'???',

# Misato Katsuragi 
"あら？\n何かしら、この音楽…。\n\0":
'???',

# Ritsuko Akagi 
"この音はチェロね…。\nこの家でこんな音楽を\n聴けるとはね…。\n\0":
'???',

# Ryoji Kaji
"チェロの音か。\nはて、どこから聞こえる？\n\0":
'???',

# Hikari Horaki
"チェロの音だわ。\n\0":
'???',

# Kensuke Aida
"おんやぁ、何の音だ？\n\0":
'???',

# Toji Suzuhara 
"何や、この音？\n外まで聞こえとるで。\n\0":
'???',

# [Text Only - No Designated Speaker]
"シンジがチェロを弾いている。\n思わず拍手した。\n\0":
'???',

# Asuka Soryu Langley
"なかなかやるじゃない。\nシンジにこんな才能が\nあったなんてね。\n\0":
'???',

# Shinji Ikari
"ほめられるほどの才能はないよ。▽\nただ、５つの頃から\n続けていただけだよ。\n\0":
'???',

# Asuka Soryu Langley
"それじゃ、\n１０年近く続けてたって事。▽\nそれだけでもすごいじゃない。\nアンタさ、もっと自分に\n自信を持ったら？▽\nそしたら、きっと音が変わるわ。\nせっかく続けてんなら、\nもっと向上心持ちなさいよ。\n\0":
'???',

# Shinji Ikari
"…向上心。▽\nそういえば、そんなつもりで\n練習した事なんてなかったな。▽\nでも、今日は何だか急に\nチェロを弾きたくなったんだ。▽\n何でなんだろうな…。\n\0":
'???',

# Rei Ayanami 
"あなただったのね…。\n\0":
'???',

# Rei Ayanami 
"何かあったの…？\n\0":
'???',

# Rei Ayanami 
"音が当てもなくさまよう感じ。\nきっと、今のあなたがそうだからよ。\n\0":
'???',

# Shinji Ikari
"…そうかな。▽\nそうかもしれない。▽\n何となく、弾いてみようという\n気持ちになったんだ。▽\n自分ではなぜだか、\nわからないんだけど…。\n\0":
'???',

# Rei Ayanami 
"でも、素敵な曲だわ。\n\0":
'???',

# Shinji Ikari
"………あ、ありがとう。\n\0":
'???',

# Misato Katsuragi 
"スッゴイ、シンちゃん。\nとても上手だわ。▽\nその荷物の中身はチェロだったのね。▽\nペンペンもうっとりして\n聴いていたわよ。\n\0":
'???',

# Shinji Ikari
"ミサトさん？\n\0":
'Misato-san?\n\0',

# Misato Katsuragi 
"みんなにも聴かせてあげたら？\n\0":
'???',

# Shinji Ikari
"そんな…、\n誰かに聴かせるほど\n上手くはないですよ。▽\nそれに、\nそんなに好きな事じゃないし…。\n\0":
'???',

# Misato Katsuragi 
"チェロを弾く事が…？\n\0":
'???',

# Shinji Ikari
"自分から始めた事じゃないし。\n前からやめよう、やめようって\n思っていたし。\n\0":
'???',

# Misato Katsuragi 
"でも、今弾いてるじゃない？\n好きなのよ、本当は。\nでしょ？▽\n私は素敵だと思うわ。\nあなたの弾くチェロの音。\n\0":
'???',

# Shinji Ikari
"………。▽\n何となく、今日は弾いてみようと\n思ったんです。▽\n結局、僕が出来る事は、\nこんな事しかないのかもしれない。\n\0":
'???',

# Misato Katsuragi 
"こんな事も出来る、でしょ？\n私にはとても無理な事を\nシンジ君はやってのけるんだもの。▽\nもっと胸を張っていいわよ。\n\0":
'???',

# Shinji Ikari
"ミサトさん…、\nありがとうございます。\n\0":
'???',

# Ritsuko Akagi 
"シンジくんだったの。\n私はてっきり、\nテレビの音だと思ってたのに。▽\nそれだけ、\n素敵な演奏だったってことよ。\n素晴らしかったわ。\n\0":
'???',

# Shinji Ikari
"ありがとうございます…。\n\0":
'???',

# Ritsuko Akagi 
"あら、止める事ないわよ。\n続けてちょうだい。▽\nそれとも私には\n聴かせてくれないのかしら？\n\0":
'???',

# Shinji Ikari
"そんな事はないですけど。\n\0":
'???',

# Ritsuko Akagi 
"そのチェロの音、\nまるで誰かを呼んでいるようね。\n\0":
'???',

# Shinji Ikari
"…え！？\nそうですか…？\n\0":
'???',

# Ritsuko Akagi 
"誰を想っていたのかしら。\n\0":
'???',

# Shinji Ikari
"………。▽\nいえ、僕は…。\n\0":
'???',

# Ryoji Kaji
"よう、なかなかやるじゃないか。\nとても繊細な音だ。▽\n男は、その繊細さがないと\n駄目なんだよ。\nハハハ…。\n\0":
'???',

# Shinji Ikari
"加持さん！？\nいつからそこに…。\n\0":
'???',

# Ryoji Kaji
"ちょっと前に…、ね。\nしばらく聴かせてもらったよ。▽\nおいおい、もうしまうのかい？\n\0":
'???',

# Shinji Ikari
"人に聴かせるほどのものじゃ\nないですから…。\n\0":
'???',

# Ryoji Kaji
"独学でここまで…？\n\0":
'???',

# Shinji Ikari
"いえ。\n５歳の時から習っていたんです。▽\n今はもう、\nレッスンなんてないですけど。\n\0":
'???',

# Ryoji Kaji
"じゃあ、今は純粋に趣味として…？\n\0":
'???',

# Shinji Ikari
"いえ…、そんなにチェロは\n好きじゃないんです。▽\nいつもやめようと思っていたし。▽\nただ、今日はなぜか\n弾いてみようと思って…。\n\0":
'???',

# Ryoji Kaji
"それが君の趣味だからさ。\nだから無意識に、\n心がチェロに向かうんだよ。\n\0":
'???',

# Ryoji Kaji
"悪い事じゃない。\n男は趣味に生きる為に\n生きてるようなもんだ。▽\nそうする事で、自分自身を\nより見つめる事が出来るからな。▽\n君のチェロは深くて柔らかい、\n繊細でいい音だ。\n癒されるよ、君の心に。\n\0":
'???',

# Shinji Ikari
"僕の、心…？\n\0":
'???',

# Ryoji Kaji
"そう、\n君の心が奏でた音だからね。▽\nよければ、もっと聴かせて欲しい。\n\0":
'???',

# Shinji Ikari
"…じゃあ、今度。\nそれまで練習します。\n\0":
'???',

# Hikari Horaki
"ビックリしたわ。\n碇君がチェロを弾くなんて。▽\nそれに、とても上手いのね。\n\0":
'???',

# Shinji Ikari
"委員長…。\n\0":
'???',

# Hikari Horaki
"今度の音楽会、\nソロでやってみない？\n\0":
'???',

# Shinji Ikari
"いいよ…、\nあまり人に聴かせたくないんだ。\n\0":
'???',

# Hikari Horaki
"なぜ？\nこんなに上手なのに。\n\0":
'???',

# Shinji Ikari
"好きじゃないんだ、チェロ。\nただ、何となくやってただけで。\n\0":
'???',

# Hikari Horaki
"何となくじゃ、\n今みたいな音は出せないわ。▽\nそれに、心のどこかで\n誰かに聴いてもらいたいと\n思っていたんじゃない？\n\0":
'???',

# Shinji Ikari
"そんな事ないよ。\n\0":
'???',

# Hikari Horaki
"そう？▽\nでも、素晴らしいものは\nみんなに素晴らしいと\n言われるためにあるのよ。▽\n私、碇君のチェロは\n素晴らしいと思うわ。\nみんなも、きっとそう思うわよ。\n\0":
'???',

# Toji Suzuhara 
"シンジ、お前が弾いとったんか。\nしっかし、でっかいバイオリンやな。\n\0":
'???',

# Shinji Ikari
"これは、チェロだよ。\nちょっと待って、今片づけるから。\n\0":
'???',

# Toji Suzuhara 
"弾いたらええやん。\n\0":
'???',

# Toji Suzuhara 
"もっと聴かせてぇや。\nなんちゅー曲か知らんけど、\nええ曲やな。▽\n他にも弾けるのあるん？\n\0":
'???',

# Shinji Ikari
"うん、まあ…。\n他にも色々とは。\n\0":
'???',

# Toji Suzuhara 
"すごいやん、\nいやいや、謙遜せんでもええで。\nマジ、すごいと思うわ。\n\0":
'???',

# Shinji Ikari
"本当は、好きじゃないんだ。\n…チェロを弾くのは。\n\0":
'???',

# Toji Suzuhara 
"せやけど、嫌な事して\nいい音が出る事はないと思うで。\n\0":
'???',

# Toji Suzuhara 
"なあ、シンジ。\n今のお前、カッコええで。\n\0":
'???',

# Kensuke Aida
"へぇ、\nシンジの意外な一面を\n見たってカンジだな。\n\0":
'???',

# Shinji Ikari
"似合わない？\n\0":
'???',

# Kensuke Aida
"そうは言ってないさ。\n\0":
'???',

# Shinji Ikari
"ごめん、すぐ片づけるから。\n\0":
'???',

# Kensuke Aida
"いや、いいよ。\nせっかくの趣味の時間を\n邪魔したみたいだし。\n\0":
'???',

# Shinji Ikari
"趣味…？\n\0":
'???',

# Kensuke Aida
"違うの？\nすごい熱中して弾いてたじゃないか。\n\0":
'???',

# Shinji Ikari
"そんなんじゃないよ。\n\0":
'???',

# Kensuke Aida
"なあ、進路さ、\n音楽方面にしてみたら？\n向いていると思うよ。▽\n俺、音楽の事って、そんなによく\nわからないけど、今のシンジの\n演奏のすごさはわかるよ。\n\0":
'???',

# Kensuke Aida
"ああ、楽器を使えるなんて\n誰にでも出来る事じゃないよ。▽\nましてや、すべての人が\nいい音を出せるとは限らないしね。\n\0":
'???',

# Shinji Ikari
"そう…かな。\n\0":
'???',

# Asuka Soryu Langley
"あら、この音はチェロ？\n誰が音楽を聴いているのかしら…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"おそらく、ペンペンがつけたので\nあろう、テレビからチェロの音が\n大音量で流れていた。▽\n音を小さくして、テレビからふと\n目を外すと、シンジが弾いていた\nチェロが目にとまった。\n\0":
'???',

#
# ./USRDIR/event/f037.har_EXTRACT/f037.evs
#
# [Text Only - No Designated Speaker]
"削除イベントです。\n\0":
'???',

#
# ./USRDIR/event/f038.har_EXTRACT/f038.evs
#
# Kaworu Nagisa 
"ほら、傷がないか見てあげる。\n\0":
'???',

# [Text Only - No Designated Speaker]
"いたずらに想像を働かせた結果、\n鼻血がすごい勢いで吹き出した。\n\0":
'???',

# Kensuke Aida
"だっ、大丈夫かよ！\n気分は…、気分はどう？\n\0":
'???',

# Toji Suzuhara 
"やっぱ、どっか打ったんやな！？\nしっかりせえ、\n保健室連れてったる！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"教室に入ろうとした瞬間、\n人とぶつかってハデに転倒した。\n\0":
'???',

# Asuka Soryu Langley
"鼻血出てるじゃん！！\nねぇ、しっかりしてよ。\n\0":
'???',

# Shinji Ikari
"いっててて…。\n\0":
'???',

# Asuka Soryu Langley
"んもー、誰よ！！\nいったいわね〜！！\n\0":
'???',

# Hikari Horaki
"こら、\n教室で走り回ってるのは\n誰なのよ！！\n\0":
'???',

# Toji Suzuhara 
"お、重い、重い、重い…。\n\0":
'???',

# Kensuke Aida
"いってぇ…。\n\0":
'???',

# Kaworu Nagisa 
"気をつけてくれよ、\n一体、誰なんだい…。\n\0":
'???',

# Shinji Ikari
"ご、ごめん…。\n\0":
'???',

# Asuka Soryu Langley
"いたたたた、\nごっめ〜ん、大丈夫ゥ！？\n\0":
'???',

# [Text Only - No Designated Speaker]
"ケガは、大した事はなかったけど、\nそのまま、保健室まで\n肩を貸してもらって移動した。▽\n少し気分が悪いフリをすると、\n心配そうに覗き込んでは、\n声をかけてくれた。▽\nそれがとても、おかしくて、\n嬉しくて。▽\n悪いな…、とも思いながら\nそのまま気分が悪いフリを続けた。\n\0":
'???',

# Hikari Horaki
"大変！\n保健室へ行った方がいいわ。\n立てる？\n\0":
'???',

# Rei Ayanami, Female Staff
"大丈夫…？\n\0":
'???',

# Hikari Horaki
"ご、ごめんなさい…。\n\0":
'???',

# Toji Suzuhara 
"す、すまん…。\n\0":
'???',

# Kensuke Aida
"あっちゃー、悪い…。\n\0":
'???',

# Kaworu Nagisa 
"ごめんよ、ケガは？\n\0":
'???',

# Kaworu Nagisa 
"大変だ…。\n僕のせいで、君にケガを…。\n\0":
'???',

# Asuka Soryu Langley
"顔、赤いけど。\nどこか打ったかしら？\n\0":
'???',

# Rei Ayanami 
"どこか打った？\n顔は腫れてない…？\n\0":
'???',

# Hikari Horaki
"ケガは…？\n冷やした方がいいかしら…。\n\0":
'???',

# Rei Ayanami 
"大丈夫…？\nハンカチ、使って。\n\0":
'???',

# Toji Suzuhara 
"意識は…あるようやな。\nホンマ大丈夫なんか？\n\0":
'???',

# Shinji Ikari
"わっ！？\n大変だ、思ったより重傷みたい…。\n\0":
'???',

# Kensuke Aida
"大丈夫、起こそうか…？\n\0":
'???',

#
# ./USRDIR/event/f039.har_EXTRACT/f039.evs
#
# [Students: Comic Collision]
#
# Shinji Ikari
"今日は風が強いな…。\n\0":
'The wind\'s strong today...\n\0',

# Toji Suzuhara 
"風、強いなぁ…。\n\0":
'???',

# Kensuke Aida
"風が強いな…。\nほこりが舞うよ。\n\0":
'???',

# Kaworu Nagisa 
"今日は風が強いな。\n涼しくて気持ちいい…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ぼんやりと窓から外を眺めていた。\n風は疾走を続け、木の葉を勢いよく\n吹き飛ばしていた。▽\nその時…。\n\0":
'???',

# Asuka Soryu Langley
"ギャ〜〜〜！？\n何よこの風〜〜〜〜！！\n\0":
'???',

# Rei Ayanami 
"あっ………。\n\0":
'???',

# Hikari Horaki
"きゃあああ〜〜〜！！\nやだっ、スカートが…。\n\0":
'???',

# Shinji Ikari
"いぃっ！？\n\0":
'???',

# Kensuke Aida
"シャッターチャンス！！\n\0":
'???',

# Toji Suzuhara 
"うおっ！？\n\0":
'???',

# Kaworu Nagisa 
"………あ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"突風が女子達のスカートを\n一斉にめくり上げた。▽\n純白…、ピンク…、スイカ模様…、\nポルカドット…、ストライプ…、▽\n一瞬の出来事なのに、よくもまあ\nこんなに確認出来たと自分でも\n感心した。\n\0":
'???',

# Asuka Soryu Langley
"んもー！！\n丸見えだったじゃないの！！\n\0":
'???',

# Hikari Horaki
"もうっ！\nイヤな風ね！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"あわててスカートを押さえる\n女子達と目が合った。▽\n焦って視線を外したが、女子達は\n鋭くこちらをにらんでいた。▽\n女子達は一言、二言の憎まれ口を\n叩いていたようだったが、\n風が強くて、良く聞こえなかった。\n\0":
'???',

# Asuka Soryu Langley
"今日は風が強いわねー。\n髪、ボサボサになっちゃう\nじゃないの。\n\0":
'???',

# Rei Ayanami 
"風が強いのね。\n\0":
'???',

# Hikari Horaki
"すごい風…。\n窓、閉めた方がいいかしら？\n\0":
'???',

# Asuka Soryu Langley
"いやぁぁぁぁ〜〜ん！！\nスカートがぁぁぁ！！\n\0":
'???',

# Rei Ayanami 
"はっ………。\n\0":
'???',

# Hikari Horaki
"やだっ、スカートが…。\nいやぁぁ〜！！\n\0":
'???',

# Shinji Ikari
"わあっ！？\n\0":
'???',

# Kensuke Aida
"見えた！！\n\0":
'???',

# Toji Suzuhara 
"げっ！？\n\0":
'???',

# Kaworu Nagisa 
"…あらら。\n\0":
'???',

# [Text Only - No Designated Speaker]
"突風が女子達のスカートを\n一斉にめくり上げた。▽\n純白…、ピンク…、スイカ模様…、\nポルカドット…、ストライプ…、▽\n風に舞うスカートを、あわてて手で\n押さえる。\n\0":
'???',

# Asuka Soryu Langley
"ギャ〜〜〜！！\nアンタ達、何見てんのよ！！\n見るんじゃないわよッ！！\n\0":
'???',

# Hikari Horaki
"やだ、もう…！\n何よ、この風〜〜〜。\n\0":
'???',

# [Text Only - No Designated Speaker]
"一部始終を見ていた男子達が\nこちらを見てニヤニヤしている。▽\n恥ずかしい気持ちを怒りに変えて、\n男子に一人一人平手打ちをして\nまわった。▽\n風は相変わらず、強く吹いていた。\n\0":
'???',

#
# ./USRDIR/event/f040.har_EXTRACT/f040.evs
#
# [Father & Son: Yui's Grave]
#
# Shinji Ikari
"父さんを待っていた。\n一緒に母さんの墓参りに\n行く事になっていたからだ。▽\n母さんは、どんな人だったんだろう。\nどんな顔をしてたんだろう。▽\n僕は知らなくても、\n父さんは知ってるんだ…。\n\0":
'???',

# Shinji Ikari
"父さん…、その花…。\n\0":
'Father, those flowers...\n\0',

# Gendo Ikari
"行くぞ。\n\0":
'Let\'s go.\n\0',

# [Text Only - No Designated Speaker]
"どこまでも続く、膨大な数の墓標。\nセカンドインパクトで\n亡くなった人たちの墓である。▽\nその中に碇ユイの墓はあった。\n墓標に花を静かに供える。\n\0":
'???',

# Gendo Ikari
"３年ぶりだな、\n二人でここに立つのは。\n\0":
'???',

# Gendo Ikari
"人は思い出を忘れる事で\n生きて行ける。▽\nだが、\n決して忘れてはならない事もある。▽\nユイは、そのかけがえのないものを\n教えてくれた。▽\n私は、その確認をする為に\nここに来ている。\n\0":
'???',

# Shinji Ikari
"………先生の言ってたとおり、\n全部捨てちゃったんだね。\n\0":
'???',

# Ritsuko Akagi 
"どうしたの、その花は？\n\0":
'???',

# Makoto Hyuga
"おや？\n花なんか抱えてどうしたんだい？\n\0":
'???',

# Shigeru Aoba
"その花、どうしたの？\n誰かにあげるのかい？\n\0":
'???',

# Kozo Fuyutsuki
"その花は…。\n\0":
'Those flowers...\n\0',

# Female Staff
"その花束は…、どうしたんですか？\n\0":
'???',

# Shinji Ikari
"今から、墓参りに行くんです。\n父さんと、母さんの…。\n\0":
'???',

# Ritsuko Akagi 
"墓参り…、そうだったわね。\nいってらっしゃい。\n\0":
'???',

# Makoto Hyuga
"そうか、\nそのための花だったのか。\n\0":
'???',

# Shigeru Aoba
"そうか。\nじゃあ、気を付けて行けよ。\n\0":
'???',

# Kozo Fuyutsuki
"やはりそうか。\n\0":
'???',

# Female Staff
"ああ、そうなんですか…。\nそれでは、\n気を付けて行って下さいね。\n\0":
'???',

# Shinji Ikari
"それじゃ、行ってきます。\n\0":
'???',

# [Text Only - No Designated Speaker]
"どこまでも続く、膨大な数の墓標。\nセカンドインパクトで\n亡くなった人たちの墓である。▽\nその中に碇ユイと\n碇ゲンドウの墓はあった。\n墓標に花を静かに供える。\n\0":
'???',

# Shinji Ikari
"父さんの事も、母さんの事も…、\n結局よく知らないままだったな。▽\n………。▽\nここに来ても、何も…、\n母さんと父さんには何を言ったら\nいいかよくわからないんだ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"しばらく何も言えないまま、\n立ち尽くしていた。▽\n帰ろうと歩き出した時、墓標の影が\nふと父さんの影のように思えた。▽\n振り返ると、\n強い風が吹くだけだった。\n\0":
'???',

# Maya Ibuki 
"碇司令、その花は？\n\0":
'???',

# Ritsuko Akagi 
"あら？\nその花は…？\n\0":
'???',

# Makoto Hyuga
"碇司令、その花束…。\n\0":
'???',

# Shigeru Aoba
"その花束は、どうしたんですか？\n\0":
'???',

# Kozo Fuyutsuki
"その花束は…。\n\0":
'???',

# Gendo Ikari
"ちょっとな…、留守を頼むぞ。\n\0":
'???',

# Maya Ibuki 
"わかりました…。\nそれでは、お気を付けて。\n\0":
'???',

# Ritsuko Akagi 
"わかりました。\n留守中何かあった時は、\n連絡さしあげます。\n\0":
'???',

# Shigeru Aoba
"…はい、承知しました。\n\0":
'???',

# Kozo Fuyutsuki
"…そうか、わかった。\n\0":
'???',

# Female Staff
"承知しました。\nでは、お気を付けて。\n\0":
'???',

# [Text Only - No Designated Speaker]
"しばらく何も言えないまま、\n立ち尽くしていた。▽\n帰ろうと歩き出した時、墓標の影が\nふとユイの影のように思えた。▽\n振り返ると、\n強い風が吹くだけだった。\n\0":
'???',

#
# ./USRDIR/event/e003.har_EXTRACT/e003.evs
#
# Shinji Ikari
"釣れないね…。\n\0":
'???',

# Gendo Ikari
"ああ…。\n\0":
'???',

# Shinji Ikari
"今日、仕事はよかったの…？\n\0":
'???',

# Gendo Ikari
"構わん。\n\0":
'???',

# Shinji Ikari
"………お腹空いたの？\n\0":
'???',

# Gendo Ikari
"朝早かったからな…。\n\0":
'???',

# Shinji Ikari
"僕、弁当作ったよ。\n昼ご飯には早いけど、\n食べようか…。\n\0":
'???',

# Gendo Ikari
"うむ。\n\0":
'???',

# Shinji Ikari
"あの、レバーの甘辛煮とね、\nネギ味噌巻卵焼き。\n…僕が作ったんだ。\n\0":
'???',

# Gendo Ikari, Ryoji Kaji
"そうか。\n\0":
'???',

# Shinji Ikari
"美味しくない…？\n\0":
'???',

# Gendo Ikari
"いや。\n\0":
'???',

# Shinji Ikari
"アハ…、よかった…。\n\0":
'???',

# Shinji Ikari
"父さん、ビール…？\n\0":
'Father, beer...?\n\0',

# Shinji Ikari
"何か、\n父さんがビール飲むところなんて\n初めて見た…。▽\nやっぱり美味しいんだ、\nミサトさんも一日に何本も\n飲んでたもんな…。\n\0":
'???',

# Gendo Ikari
"いずれ、わかる。\nすぐにそうなるさ。\n\0":
'???',

# Gendo Ikari
"（誰も敵ではなかった。）▽\n（他人を隔てていたものが、\n　本当は互いを強く結び付ける\n　ものだと…。）\n\0":
'???',

# Gendo Ikari
"（ユイと出会って、それに\n　気づいていたはずだった。）\n\0":
'???',

# Gendo Ikari
"（だが、シンジ…。\n　お前を見ていて、ようやく\n　それに気づくことが出来た。）▽\n（心から、…感謝している。）\n\0":
'???',

# Shinji Ikari
"………。▽\n（僕は、父さんの事を…、\n　ずっと、憎んでいた。）▽\n（母さんを死なせて、\n　僕を捨てて…。）▽\n（でも、父さんに呼ばれて、\n　ここへ来てから…、）▽\n（憎んでいたはずなのに、\n　僕は、父さんの事を見ていた。）\n\0":
'???',

# Gendo Ikari
"一匹も釣れんな。\n\0":
'???',

# Shinji Ikari
"僕は…、▽\n僕は、楽しいよ。\n\0":
'???',

# Gendo Ikari
"………………。▽\n早く酒が飲めるといいな。\n\0":
'???',

# Shinji Ikari, Maya Ibuki, Hikari Horaki
"…うん。\n\0":
'???',

# Shinji Ikari
"父さん、今日はありがとう。\n\0":
'???',

# Gendo Ikari
"ああ、シンジ。\n今日は、ありがとう…。\n\0":
'???',

#
# ./USRDIR/event/f041.har_EXTRACT/f041.evs
#
# [Dejection: Kaworu Enters]
#
# Toji Suzuhara 
"お前、誰やねん…。\n\0":
'???',

# Kaworu Nagisa 
"歌は心を潤してくれる…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"どこかから歌が聞こえる…。\n\0":
'I hear a song coming from somewhere...\n\0',

# Ritsuko Akagi 
"渚カヲル…。\nわかっているのは、生年月日が\nセカンドインパクトと同一日。\n\0":
'???',

# Maya Ibuki 
"このデータ…、彼のエヴァとの\nシンクロ率のデータが\n異常な数値を示している…。▽\nこれは一体…。\n\0":
'???',

# Makoto Hyuga
"現在、彼は他のパイロットと\n接触中の模様…か。\n\0":
'???',

# Asuka Soryu Langley
"今の歌、アンタなの？\n\0":
'That was you singing?\n\0',

# Kaworu Nagisa 
"そう思わないかい、碇シンジ君。\n\0":
'Don\'t you think so, Shinji Ikari?\n\0',

# Kaworu Nagisa 
"そう思わないかい、アスカさん。\n\0":
'Don\'t you think so, Asuka-san?\n\0',

# Kaworu Nagisa 
"そう思わないかい、ファースト。\n\0":
'Don\'t you think so, First?\n\0',

# Kaworu Nagisa 
"そう思わないかい、鈴原トウジ君。\n\0":
'Don\'t you think so, Toji Suzuhara?\n\0',

# Shinji Ikari
"ど、どうして僕の名を？\n\0":
'???',

# Asuka Soryu Langley
"ちょっと、\nそーゆーアンタは何モンなのよ？\n\0":
'???',

# Rei Ayanami 
"あなた、私と同じ匂いがする…。\n一体、誰…？\n\0":
'That feeling about you, it\'s the same as me...\nWho in the world are you?\n\0',

# Toji Suzuhara 
"ワイを知っとう…て。\n何や、お前誰なん？\n\0":
'???',

# Kaworu Nagisa 
"僕は渚カヲル、\n君と同じ選ばれた子供さ。\n\0":
'I\'m Nagisa Kaworu,\na chosen child same as you.\n\0',

# Shinji Ikari
"渚…くん？\n\0":
'Nagisa...-kun?\n\0',

# Asuka Soryu Langley
"渚カヲルぅ？\n\0":
'Kaworu Nagisa?\n\0',

# Rei Ayanami 
"渚カヲル…？\nあなたもエヴァのパイロットなのね。\n\0":
'Kaworu Nagisa...?\nSo you are an Eva pilot as well.\n\0',

# Toji Suzuhara 
"何や…、\n…っちゅう事はパイロットかいな。▽\nえーと…、渚…。\n\0":
'???',

# Kaworu Nagisa 
"カヲルでいいよ、今後とも宜しく。\n\0":
'???',

# Misato Katsuragi 
"委員会が直に送ってきた、\nこの少年の資料は何…？\n経歴その他、全てが抹消済み…。\n\0":
'???',

# Misato Katsuragi 
"このまま何も起きないわけは\nないわね…。\n\0":
'???',

# Kozo Fuyutsuki
"マルドゥック機関を通さず\n適任者として送り込まれた少年…。\nふに落ちんな。\n\0":
'???',

# Ryoji Kaji
"こいつはシナリオにない展開だな。\n嗅ぎまわるより、\n接触をとってみる方が早いか…。\n\0":
'???',

#
# ./USRDIR/event/f044.har_EXTRACT/f044.evs
#
# [Students: Playing Hooky, Pen Pen Dream]
#
# [Text Only - No Designated Speaker]
"何となく、行く気にならなかった。▽\nバカバカしいとか、\n天気がよかったからとか、\n理由はどうでもよくって…、▽\nただ、何となく…。\n\0":
'???',

# Shinji Ikari
"とうとうサボっちゃったな…。▽\n欠席扱いに…なってるのかな。▽\n……………。\n\0":
'???',

# Pen Pen
"後悔してるかい？\n\0":
'???',

# Pen Pen
"でも、君は学校をサボった。\n理由はどうあれ、自分の意志で。\n\0":
'???',

# Shinji Ikari
"お前、ペンペン…？\n\0":
'Are you Pen Pen?\n\0',

# Pen Pen
"…かもね。\n\0":
'...Could be.\n\0',

# Shinji Ikari
"でも、僕の声だ…。\n夢なのかな…。\n\0":
'But you have my voice...\nSo it\'s a dream, then.\n\0',

# Pen Pen
"かもね。\n君が決めたらいい。▽\n行こうか。\n\0":
'???',

# Shinji Ikari
"待ってよ、どこへ？\n\0":
'???',

# Pen Pen
"君が決めるといい。\nどこかへ行きたかったんだろう？\n\0":
'???',

# Shinji Ikari
"どこも、別に目的はないんだ…。\nただ、ここまで\n出てきてしまっただけで…。\n\0":
'???',

# Pen Pen
"いいや、何かを目指してたんだ、\n探してたんだ。\n\0":
'???',

# Pen Pen
"君が決めるといい。\n\0":
'???',

# Shinji Ikari
"そればっかり。\n\0":
'???',

# Pen Pen
"たとえば、学校。\n\0":
'School, for instance.\n\0',

# Shinji Ikari
"学校はいいよ。\n\0":
'School is fine.\n\0',

# Pen Pen
"そうか、\nじゃあ、よそう。\nちゃんと決められるじゃないか。\n\0":
'???',

# Shinji Ikari
"別に行くところなんて無いよ。\n\0":
'???',

# Pen Pen
"じゃあ、ここでいい。\nそれも君の意志だ。\n\0":
'???',

# Shinji Ikari
"僕、頭がおかしくなったのかな…。\n\0":
'???',

# Pen Pen
"かもね、\nと言えば君は納得するかい？\n\0":
'???',

# Shinji Ikari
"…じゃあ、僕は！？\n\0":
'???',

# Pen Pen
"それは怖いんだね、\n認めたくないんだよね。▽\n大丈夫、おかしくなんかないよ、\nと言えば安心するかな？▽\nでも、そろそろ自分で\n決めたらどうだい？\n\0":
'???',

# Shinji Ikari
"………。▽\nわかったよ、これは夢だ。\n\0":
'???',

# Pen Pen
"ＯＫ。\nじゃあ、夢だ。\n\0":
'OK.\nSo, it\'s a dream.\n\0',

# Pen Pen
"探していたのは、可能性。▽\n何かが変わるかもしれないという、\n期待。\n\0":
'???',

# Shinji Ikari
"…そう、\nそうなんだ、\n何かは見えないけど。\n\0":
'???',

# Pen Pen
"見つかった…？\n\0":
'???',

# Shinji Ikari
"ううん、\n何かがあるような気がしたんだ。\nけれど、何もなかった。▽\nでも、それに出会いたくて\nしょうがなかった。\n\0":
'???',

# Pen Pen
"学校をサボってまで。\n\0":
'???',

# Shinji Ikari
"うん…。\nみんな、こんなバカな事、\nしないよね。\n\0":
'???',

# Pen Pen
"他人の事ばかり気にしてる。\nそれに、本当にバカな事？\n価値のある事とは思わない？\n\0":
'???',

# Shinji Ikari
"そんな見方はした事がなかった。\n\0":
'???',

# Pen Pen
"結果より、その時の決断。\nそれを尊いと思えば、\n後悔はなくなる。\n\0":
'???',

# Shinji Ikari
"学校をサボったのは事実だよ。\n\0":
'???',

# Pen Pen
"それは探し物が\n見つからなかったから。\n期待を裏切られたから。▽\n探しているものが得られたら、\n後悔はなかったはず。▽\n…でも、どっちにしても\nその時の決断は尊い。\n\0":
'???',

# Shinji Ikari
"可能性って…、\n僕の居場所…のハズなんだ。\n\0":
'???',

# Pen Pen
"でも、それをどこにあるのか\n決めるのは、自由。\nとても、簡単な事なのに。\n\0":
'???',

# Shinji Ikari
"よくわからないよ。\n\0":
'???',

# Pen Pen
"わからないふりをしているだけ。▽\nねえ…、\n君は僕が嫌いかい？\n\0":
'???',

# Shinji Ikari
"急に何を聞くのさ…。\n嫌いじゃないよ、\n好きかはわからないけど。\n\0":
'???',

# Pen Pen
"じゃあ、それが今の君の決断だ。▽\nそれに、\n好きになるかもしれないね。\n\0":
'???',

# Pen Pen
"グワッ、グワワワッ！！\n\0":
'???',

# Shinji Ikari
"わぁっ！？\n\0":
'???',

# Shinji Ikari
"あ、あれ…？\nここは僕の部屋…。▽\nペンペン…。\n\0":
'???',

# Pen Pen
"グワ？\n\0":
'???',

# Shinji Ikari
"やっぱり、夢だったのか…。\n\0":
'???',

# Misato Katsuragi 
"シンちゃ〜ん、起きた？\n体の方は大丈夫？▽\nもう、街中で日射病で\n倒れてたのよ。▽\n連絡聞いた時、\nホントに心配しちゃった…。\n\0":
'???',

# Shinji Ikari
"日射病、僕が、ですか…？\n\0":
'???',

# Misato Katsuragi 
"今日は暑かったものねー。\nとにかくたっぷり水分を取って、\nまた寝なさい。\n\0":
'???',

# Shinji Ikari
"………。▽\n…ハイ。\n\0":
'???',

# Asuka Soryu Langley
"バカシンジ、目が覚めた？\nアンタさ、日射病で倒れてたのよ。\nそれも街中で。▽\n学校に連絡があったから、\nクラスメイトがここまで\n運んでくれたのよ。\n\0":
'???',

# Shinji Ikari
"日射病…。\nそう、なんだ…。\n\0":
'???',

# Shinji Ikari
"気分？\n何か少し…、すっきりしたかな。\n\0":
'???',

# Asuka Soryu Langley
"もっかい、寝たら？\n\0":
'???',

# Shinji Ikari
"うん、そうするよ…。\n\0":
'???',

# Rei Ayanami 
"碇君、目が覚めたの…？\n\0":
'???',

# Rei Ayanami 
"日射病で倒れていたのよ。\n覚えてないの？\n\0":
'???',

# Rei Ayanami 
"もう、大丈夫みたいね。▽\nゆっくり眠るといいわ。\n私、帰るから…。\n\0":
'???',

# Shinji Ikari
"僕、学校サボったんだ。\n\0":
'???',

# Rei Ayanami 
"そう。\nあなたがそう決めたんだから\nいいじゃない。\n\0":
'???',

# Shinji Ikari
"そうか、\n………そうだね。\n\0":
'???',

# Rei Ayanami 
"じゃ、私帰るわ…。\nおやすみなさい。\n\0":
'???',

# Shinji Ikari
"おやすみ、\nありがとう。\n\0":
'???',

# Shinji Ikari
"あ、あの…僕は…。\n\0":
'???',

# Female Staff
"登校中に、日射病で倒れたんですよ。\nそれで、すぐスタッフがかけつけて。\n\0":
'???',

# Shinji Ikari
"日射病、覚えてないや…。\n\0":
'???',

# Female Staff
"今夜休めば、もう大丈夫ですよ。\n今日は朝から暑かったから、\n大変でしたね。▽\nそれじゃ、私は帰りますので。\nゆっくりお休み下さい。\n\0":
'???',

# Shinji Ikari
"あの、ご迷惑おかけしました。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ここに来る前に、\n校舎の前でシンジの姿を見た。▽\nてっきり先に\n来ているものだと思った…。\n\0":
'???',

# Asuka Soryu Langley
"あれ、バカシンジのやつ。\n先に来てると思ったのに。\n\0":
'???',

# Rei Ayanami 
"碇君、\n私より先に来ているはずだと\n思ったのに…。\n\0":
'???',

# Hikari Horaki
"碇君…、\n先に来てたと思ったのに。\n\0":
'???',

# Toji Suzuhara 
"シンジのやつ、\n先行ったと思っとったのに。\nトイレかいな？\n\0":
'???',

# Kensuke Aida
"あれ？\nシンジの奴が先だと思ったのに。\nまだ来てないんだ。\n\0":
'???',

# Kaworu Nagisa 
"シンジ君、\n僕より先に来ていた\nはずなんだけどな…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"その日、とうとうシンジは\n教室に現れなかった。\n何かあったのだろうか…。\n\0":
'???',

#
# ./USRDIR/event/f046.har_EXTRACT/f046.evs
#
# [Text Only - No Designated Speaker]
"ふと、郵便受けを見ると、\n封筒が入っていた。\n\0":
'???',

# Rei Ayanami, Asuka Soryu Langley
"…手紙？\n\0":
'???',

# [Text Only - No Designated Speaker]
"知らない差出人、以前ここに\n住んでいた人であろう宛名。\n封を切って、手紙を開く。\n\0":
'???',

# [Text Only - No Designated Speaker]
"何もかも嫌になりました。\nおとうさん、最後に会いたかった。▽\n今まで、ありがとう。\nさようなら、\nごめんなさい。\n\0":
'???',

# Rei Ayanami 
"………。▽\nありがとう…。▽\nさようなら…。▽\nごめんなさい…。▽\n会いたかった…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"レイは、カバンからペンを取り出し、\nノートに字を走らせた。\n\0":
'???',

# Rei Ayanami 
"いつか、あの人が言ったことば。▽\n私にくれたことば。\n\0":
'???',

# [Text Only - No Designated Speaker]
"書いたページを破り、封筒に入れた。\n手紙から宛先を写し、封をする。\n急いで、靴を履いて外へ走った。▽\n切手を貼って、\n封筒をポストに投函する。▽\n生きているなら…、\nまだ生きていてくれるのなら…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"誰もいないレイの部屋に、\n彼女の残り香だけが残っている。\n\0":
'???',

# [Text Only - No Designated Speaker]
"レイが、手に封筒を持っている。\n\0":
'???',

# Shinji Ikari
"綾波に手紙…？\n\0":
'???',

# Hikari Horaki, Shigeru Aoba
"手紙…？\n\0":
'???',

# Toji Suzuhara 
"手紙やん、誰からや？\n\0":
'???',

# Kensuke Aida
"手紙？\n\0":
'???',

# Kaworu Nagisa 
"君に、手紙かい？\n\0":
'???',

# Ritsuko Akagi 
"レイに手紙？\n学校の人から？\n\0":
'???',

# Rei Ayanami 
"知らない人。\n住所はここだけど、宛名が違うの。▽\nきっと、私の前に\nここに住んでた人だわ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"封を切って、手紙を開く。▽\n手紙にはこう書かれていた。\n\0":
'???',

# Shinji Ikari
"これっ、遺書…！？\n\0":
'???',

# Hikari Horaki
"大変、これ遺書だわ。\n\0":
'???',

# Toji Suzuhara 
"ちょっと、これってまさか…。\n\0":
'???',

# Kensuke Aida
"おい、これひょっとして\n遺書じゃないのか？\n\0":
'???',

# Kaworu Nagisa 
"…まさか、遺書？\n\0":
'???',

# Ritsuko Akagi 
"これは遺書だわ。\n\0":
'???',

# Shigeru Aoba
"まさか、イタズラじゃ…。\nでも、本当だったらこれは、\n遺書…。\n\0":
'???',

# Rei Ayanami 
"………。▽\nありがとう…。▽\nさようなら…。▽\nごめんなさい…。▽\n会いたかった…。▽\n………。\n\0":
'???',

# [Text Only - No Designated Speaker]
"書いたページを破り、封筒に入れ、\n宛先を写して封をする。\n\0":
'???',

# [Text Only - No Designated Speaker]
"レイは、靴を履いて外へ走った。\n\0":
'???',

# Shinji Ikari
"綾波っ！！\n\0":
'???',

# Hikari Horaki
"綾波さんっ！！\n\0":
'???',

# Toji Suzuhara 
"おい、綾波！！\n\0":
'???',

# Kensuke Aida
"綾波、どこに行くんだよ！\n\0":
'???',

# Kaworu Nagisa 
"ファースト、君は…。\n\0":
'???',

# Ritsuko Akagi 
"レイ、あなた…。\n\0":
'???',

# Shigeru Aoba, Misato Katsuragi, Gendo Ikari
"レイ！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"レイが走った先は、\n速達用のポストだった。\n切手を貼って、投函する。\n\0":
'???',

# Rei Ayanami 
"………。▽\n生きているのなら…、\nまだ生きていてくれたのなら…。\n\0":
'???',

# Hikari Horaki
"綾波さん…。\n\0":
'???',

# Ritsuko Akagi, Shigeru Aoba, Misato Katsuragi, Gendo Ikari, Kozo Fuyutsuki, Maya Ibuki, Makoto Hyuga
"レイ…。\n\0":
'???',

# Rei Ayanami 
"きっと、大丈夫…。▽\nきっと…。\n\0":
'???',

# Gendo Ikari
"手紙か…？\n\0":
'???',

# Rei Ayanami 
"知らない人。\n住所はここだけど、宛名が違う。▽\nきっと、私の前に\nここに住んでいた人だわ。\n\0":
'???',

# Gendo Ikari
"遺書か…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"レイは、カバンからペンを取り出し、\n何かを書こうとしたが手を止めた。\n顔には困惑の表情が見える。\n\0":
'???',

# Gendo Ikari
"…レイ。\n\0":
'???',

# Yui Ikari [Flashback]
"あら、生きて行こうと思えば、\nどこだって天国になるわよ。▽\nだって、生きているんですもの。\n幸せになるチャンスは\nどこにでもあるわ。\n\0":
'???',

# Gendo Ikari
"レイ、貸してみろ。\n\0":
'???',

# Rei Ayanami 
"それは…、\n以前、私に言ったことば。\nもう、忘れたんだろうと思ってた。\n\0":
'???',

# Gendo Ikari
"これでいいだろう。\n切手を貼って、出すといい。\n\0":
'???',

# Gendo Ikari
"…思い止まっていればいいが。▽\n幸せになるチャンスは\nどこにでもある…か。\n\0":
'???',

#
# ./USRDIR/event/f047.har_EXTRACT/f047.evs
#
# Shinji Ikari
"その箱、何ですか？\n\0":
'???',

# Asuka Soryu Langley
"何これ？\nその箱なーに？\n\0":
'???',

# Rei Ayanami 
"その箱、何が入ってるんですか？\n\0":
'???',

# Pen Pen
"クワ、グワワッ？\n\0":
'???',

# Misato Katsuragi 
"なーに、これ？\n\0":
'???',

# Ritsuko Akagi 
"中には箱庭セットが入ってるわ。\n\0":
'???',

# Misato Katsuragi 
"これをどうするの？\n\0":
'???',

# Ritsuko Akagi 
"時々、パイロットの精神状態を\n知るために、使ってみて。▽\n言葉で伝えきれない\n気持ちの表現を読み取るのよ。\n\0":
'???',

# Misato Katsuragi 
"…私が？\n子供たちに使うの？\n\0":
'???',

# Ritsuko Akagi 
"そう、たまにでいいわ。\nあくまで補助的な事だから。\nあとね、コレ。\n\0":
'???',

# Misato Katsuragi 
"ロールシャッハ？\n\0":
'???',

# Ritsuko Akagi 
"アタリ。\n\0":
'???',

# Misato Katsuragi 
"私は、あの子達を\nそんな目で見るつもりはないわ。\n\0":
'???',

# Ritsuko Akagi 
"それじゃ困るわ、あなたが\n何のために子供と一緒にいるのか\nわからないじゃない。\n\0":
'???',

# Misato Katsuragi 
"こんな物が、\n心を代弁してくれるのかしら…。\n\0":
'???',

# Misato Katsuragi 
"もっとも使うつもりなんて\nさらさらないけど…。\n\0":
'???',

# Misato Katsuragi 
"…こっちがロールシャッハ…か。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、ミサトの姿が頭をよぎった。\n\0":
'???',

# Nursing Staff
"やっと、生活の中で少しずつ\n言葉が出るようになりましたよ。\n\0":
'???',

# Psychiatrist
"わかりました、\n地道に見ましょう。\n今日は、テストをします。\n\0":
'???',

# Misato Katsuragi 
"あ、これは…。\n何でもないの、ガラクタ。\n捨てるもの。▽\nこんなもの、必要ないもの…。\n\0":
'???',

# Psychiatrist
"ミサトちゃん…。\n\0":
'???',

# Misato Katsuragi [Flashback]
"…先生。\n\0":
'???',

# Psychiatrist
"今日はいいものを持ってきたよ。\nほら、箱庭だよ。\n人形もあるんだ。\n\0":
'???',

# Psychiatrist
"おじさん、絵を持ってきたんだ。\nこれを見てくれるかな。\n\0":
'???',

# Psychiatrist
"何に見える…？\n\0":
'???',

# Misato Katsuragi [Flashback]
"光…。\n\0":
'???',

# Misato Katsuragi [Flashback]
"まばゆい光…。\n\0":
'???',

# Misato Katsuragi [Flashback]
"翼…。\n\0":
'???',

# Psychiatrist
"ミサトちゃん？\n\0":
'???',

# Misato Katsuragi [Flashback]
"………うぅ、\nううううう…。▽\n…いや、\nいやあぁぁぁぁぁぁぁぁぁぁ！！\nうわああぁぁあぁあああああっ！！\n\0":
'???',

# Pen Pen
"グワッ！？\n\0":
'???',

# Misato Katsuragi 
"…は、夢…？\n\0":
'???',

# Shinji Ikari
"寝言ですか。\n\0":
'???',

# Asuka Soryu Langley
"なによ、うるさい寝言ね。\n\0":
'???',

# Rei Ayanami 
"どうしたんですか…。\n\0":
'???',

# Pen Pen
"ウクー、グワッ。\n\0":
'???',

# Misato Katsuragi 
"あ、いや…、\nちょっと夢見ちゃって…。\nびっくりした…？\n\0":
'???',

#
# ./USRDIR/event/f048.har_EXTRACT/f048.evs
#
# Gendo Rokubungi
"これは君が興味があると\n言っていたレポートだ。▽\nドイツ語で、すまないが…。\n\0":
'This is the report I said\nwould interest you.▽\nI\'m sorry it\'s in German...\n\0',

# Yui Ikari [Flashback]
"まあ、本当に読む事が出来るなんて。\nありがとうございます、ウフフ…。\n\0":
'Come now, I CAN actually read it!\nThank you so much, hahah.\0',

# Gendo Rokubungi
# A bit uncertain about this... -Reichu
"再び眠りに入った前後の時期時期には\nその原因遺伝子と思われるところが\n急速に変化している。\n\0":
'What seems to be the causal gene\n rapidly changes in the time around which ?it? fell asleep again.\n\0',

# Yui Ikari [Flashback]
"注目すべきところは、ここね。▽\n被験者と長期間接触した人間も\n同様に遺伝子レベルから変化が\n起こっている。▽\n他生物による進化の可能性を\n垣間見る事が出来るわね。\n精神汚染とも言うべき、この…、▽\nごめんなさい、帰ってから\nゆっくり読めるわよね…。\n\0":
'Here\'s where you should take notice.▽\n Change is occurring at the genetic level,\n same as in the people who engaged in\n prolonged contact with the test subject.▽\n One can certainly glimpse the\n evolutionary possibilities via other organisms.\n In what can only be called mental contamination, this...▽\n Forgive me, ever since you got\n back my reading\'s been slow...\n\0',

# Gendo Rokubungi
"構わない。\n喜んでもらえてよかったよ。\n明日は冬月先生と約束があるとか。\n\0":
'Not a problem.\nI\'m glad you\'re pleased. \n Tomorrow you have an appointment with Fuyutsuki-sensei?\n\0',

# Yui Ikari [Flashback]
"ええ、貴船山へ。\n紅葉が綺麗なの、\n六分儀さんも一緒にどうですか？\n\0":
'Yes, to Kibuneyama.\nThe autumn colors are so lovely.\nWhat do you think about going with us, Rokubungi-san?',

# Gendo Rokubungi
"いや、いい。\n傷がまだ痛むんでね。\n\0":
'No, it\'s fine.\nMy injuries still hurt.\n\0',

# Yui Ikari [Flashback]
"そうだったわね…、\nじゃあ、今度一緒に洞川へ\n行きません？\n\0":
'Of course, of course...\n Then, won\'t you go with\nme to Dorogawa soon?\n\0',

# Gendo Rokubungi
"洞川、奈良の吉野の方か。\n遠いな、日帰りは出来ないぞ。\n\0":
'Dorogawa, toward Yoshino in Nara?\nThat\'s too far. I can\'t do a day trip.\n\0',

# Yui Ikari [Flashback]
"だから、連休を使って行くんです。\n渓谷や鍾乳洞が見事なのよ。\n\0":
'So use your days off and go.\n The ravine and limestone cave are magnificent.\n\0',

# Gendo Rokubungi
"………しかし、\n君はいいのか？\n\0":
'...And you\'re sure\nit\'s okay?\n\0',

# Yui Ikari [Flashback]
"連休は困りますか？\n\0":
'Multiple days off are a problem?\n\0',

# Gendo Rokubungi
"いや…、そういうわけじゃないが…。\nああ、…構わない。\n\0":
'No, it\'s not that...\nOh... All right.\n\0',

# Yui Ikari [Flashback]
"それと、君じゃなくて\nユイ、です。\n\0":
'And it\'s not "you",\nit\'s "Yui".\n\0',

# Gendo Rokubungi
"………。▽\nわかった、…ユイ？\n\0":
'......▽\nUnderstood... Yui?\n\0',

# Yui Ikari [Flashback]
"ウフフ、そう。▽\nねえ、先斗町でお団子食べましょう。\n目の前で焼いてくれるのよ。\n\0":
'Hahah, exactly right.▽\nSay, let\'s have some dango in Pontocho.\n They cook them for you on the spot.\n\0',

# Gendo Rokubungi
"わかった、\nじゃあ歩こう。\n………………。▽\nユイ…、\n君が奨励金を受けているという\n組織について聞きたいんだが。\n\0":
'All right,\n we\'ll take a walk then.\n .............▽\n Yui...\n I want to ask you about the organization\n you\'re receiving your grants from.\n\0',

# Yui Ikari [Flashback]
"あら、あなたも\n研究援助を受けたいの？\n\0":
'Oh, you\'re looking to\nget research aid, too?\n\0',

# Gendo Rokubungi
"そのつもりだ。\n今、スポンサーを探している。▽\nそして、出来れば…、\n君…、\nユイにも手伝ってもらいたい。\n\0":
'That\'s the plan.\nI\'m currently looking for a sponsor.▽\n And, if I find one...\nI also want to help you,\n Yui.\n\0',

# Yui Ikari [Flashback]
"ええ、喜んで。\nその話、受けさせてもらいます。\n\0":
'???',

# Gendo Ikari
# Check translation - unsure about meaning of の元に here. -Reichu
"君の願いの元に、\n私の願いも…じきかなう。▽\nユイ、もうすぐ会える…。\n\0":
'My wishes will soon accord\n with the source of your own.▽\n Yui, I\'ll get to see you very soon..\0',

# [Text Only - No Designated Speaker]
# Who is the narrator supposed to be here? Wouldn\'t the flashback be from Gendo\'s game? -Reichu
"ふと、ゲンドウの姿が頭をよぎった。\n\0":
'Suddenly, an image of Gendo crossed my mind.\n\0',

# [Text Only - No Designated Speaker]
"ゲンドウが、\n初号機の前に立っている。▽\nその表情は、\nいつになく穏やかな様子だった。▽\n一体何があったのだろう…。\n\0":
'Gendo, standing\n in front of Unit-01.▽\nHis expression was\n unusually calm.▽\n What could possibly have happened...?\n\0',

#
# ./USRDIR/event/f049.har_EXTRACT/f049.evs
#
# [Character: Fuyutsuki Flashback]
#
# [Text Only - No Designated Speaker]
"激しい子供の泣き声が、聞こえる。\n母親であろう女性が\n幼児を抱いてオロオロしている。▽\n病院には休診の札が掛かっていた。\nあの母親は、\nこの病院を目指していたのだろう。\n\0":
'A baby was crying intensely.\nA woman, surely the mother, paced\nnervously with the child in her arms.▽\nA hanging sign indicated the hospital was closed.\nIt seems the mother had her sights set on this facility.\n\0',

# Kozo Fuyutsuki
"どうか、しましたか？\n\0":
'Is there something I can do?\n\0',

# Baby's Mother
"子供が今までになく\n激しく泣いて…。▽\n何分かおきに泣き止むんですけど、\nまた、激しく泣いて…。\n\0":
'My child has never cried this badly...▽\nShe\'ll stop for a few minutes here and there,\nbut then she\'s bawling again...\n\0',

# Kozo Fuyutsuki
"何分おきかね…？\n\0":
'???',

# Baby's Mother
"２０分…でしょうか。\n泣き止むと、ケロッと\n何事もなかったみたいなのに…。\n\0":
'???',

# Kozo Fuyutsuki
"いかん、それは腸重積だ。\n\0":
'???',

# Baby's Mother
"どうすれば、\nどうすれば治るんですか…。\n\0":
'???',

# Kozo Fuyutsuki
"少し待っているがいい。\n\0":
'???',

# Kozo Fuyutsuki
"私だ。\n中央病院に患者を一人。▽\n小児科医を…、ああ、子供だ。\n腸重積の疑いがある。\n\0":
'It\'s me.\nI have one patient at the central hospital.▽\nIs a pediatrician-- Yes, it\'s a child.\nSuspected invagination of the bowels.\n\0',

# Kozo Fuyutsuki
"後少しの辛抱だ。\nタクシーで、この病院に行きなさい。▽\nそれと、受付けでこの紙を渡せば\nあとは医師にまかせておけばいい、\n治療費も必要ない。\n\0":
'???',

# Baby's Mother
"あ、ありがとうございます…。\n\0":
'Th-thank you very much...\n\0',

# Kozo Fuyutsuki
"礼はいい、急ぐんだ。\n\0":
'No need for that, just hurry.\n\0',

# Baby's Mother, Toji Suzuhara
"ハイ…。\n\0":
'I will.\n\0',

# Kozo Fuyutsuki
"ありがとうございます…か。\n\0":
'"Thank you"...eh?\n\0',

# Yui Ikari [Flashback]
"冬月先生、\nどうもありがとうございました…。▽\n中耳炎だなんて、\n痛がる様子もないから、\nちっとも気づきませんでした…。\n\0":
'???',

# Kozo Fuyutsuki [Flashback]
"膿も出したし、\n痛みも熱も引くだろう。\n消毒は、これを使うといい。\n\0":
'???',

# Yui Ikari [Flashback]
"あ〜らあらあら、シンちゃん。\n今頃になって泣き出して。▽\n冬月先生が見てくれたのよ、\nやっと元気になれるね…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、冬月の姿が頭をよぎった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"冬月がそわそわした様子で\n立っている。\n誰かを待っているのだろうか？\n\0":
'???',

# Male Staff, Shigeru Aoba
"副司令。\n\0":
'Deputy Commander.\n\0',

# Kozo Fuyutsuki
"ああ、君か。\nどうだったかね…。\n\0":
'???',

# Male Staff
"はい、治療も無事済んで、\n２４時間入院させるそうです。\n\0":
'???',

# Kozo Fuyutsuki
"そうか、それはよかった。\nああ、君、すまなかったな。\n\0":
'???',

# Male Staff, Shinji Ikari, Makoto Hyuga
"いえ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"何の話だったのだろうか、\n冬月は安心した様子で歩いていった。\n\0":
'???',

#
# ./USRDIR/event/f050.har_EXTRACT/f050.evs
#
# Naoko Akagi
"母さんは仕事。\n今から出勤なの。\n\0":
'???',

# Ritsuko Akagi [Flashback]
"そう、\n大変なのね。\n\0":
'???',

# Naoko Akagi
"ああ、それとお金ね。\n今夜帰らないから\n何か食べておいて。▽\n早く帰るのよ、\n明日から期末テストでしょう？\n\0":
'???',

# Ritsuko Akagi [Flashback]
"大丈夫、あんなの\n目をつむっても出来るわ。\n\0":
'???',

# Naoko Akagi
"本当に散歩…？\nあなた、時々学校に出ない事も\nあるそうね。▽\n成績がいいから、先生、\n大目に見てくれてるけど…。\n\0":
'???',

# Ritsuko Akagi [Flashback]
"…散歩なんだってば、\nすぐ帰るわよ。\n行ってきます。\n\0":
'???',

# Ritsuko Akagi [Flashback]
"香水の匂い、そのカッコ。\n本当に仕事なの…。▽\n母さん、\nどこへ行くの…。\n\0":
'???',

# Maya Ibuki, Female Staff
"そっち、行き止まりですよ。\n\0":
'???',

# Makoto Hyuga
"そっちは、行き止まりですよ。\n\0":
'???',

# Shigeru Aoba
"あのー、\nそっち、行き止まりですよ。\n\0":
'???',

# Ryoji Kaji
"そっち、行き止まりだよ。\n\0":
'???',

# Misato Katsuragi 
"そっちは、行き止まりじゃない。\n\0":
'???',

# Ritsuko Akagi 
"あ、ああ、そうね。\nそうだったわね…。\nごめんなさい…。\n\0":
'???',

# Ritsuko Akagi 
"………………………。▽\nどこに行くの…か。▽\n母さんは、\nもうどこにも行かないのに…。\n\0":
'???',

# Naoko Akagi
"その頭…どうしちゃったの？\n答えなさい、リッちゃん。▽\n昨夜も家に帰らなかったでしょ。\nどこに行ってたのよ。\n\0":
'???',

# Ritsuko Akagi [Flashback]
"美容院よ。\nどう？\n綺麗な金髪でしょ。\n\0":
'???',

# Naoko Akagi
"明日は卒業式なのよ、\nあなた知事から表彰を受けるって\nいうのに…、その頭…。\n\0":
'???',

# Ritsuko Akagi [Flashback]
"どうせ、母さん来ないでしょ。\n仕事があるから。\n\0":
'???',

# Naoko Akagi
"そんな問題じゃないの。\n来なさい、染め直してあげるから。\n\0":
'???',

# Ritsuko Akagi [Flashback]
"放してよ…、放して！！\nこんな時だけ母親面しないで！！\n\0":
'???',

# Naoko Akagi
"リッちゃん…。\n\0":
'???',

# Ritsuko Akagi 
"反抗したのはあれっきり。\n母さんの事は嫌いじゃなかった。▽\nでも、\n母さんのようになるのが怖かった。\n母さんと違う女でいたかった。\n\0":
'???',

# Ritsuko Akagi 
"でも、\nやっぱり同じ女だったみたいね…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、リツコの姿が頭をよぎった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、目の前にいる\nリツコの髪色が気になった…。▽\n輝くような金色の髪。\nうっすらと香るローズの香りが\n一層、心を惹きつけた。\n\0":
'???',

# Shinji Ikari
"リツコさんって、\nいつから金髪なんですか？\n\0":
'???',

# Asuka Soryu Langley
"ねぇ、リツコさんって、\nいつから金髪なんですか？\n\0":
'???',

# Rei Ayanami 
"赤木博士は、いつから\nそんな髪になったんですか？\n\0":
'???',

# Misato Katsuragi 
"リツコってさぁ、\nその髪いつからだっけ？\n出会った時にはもう金髪だったよね。\n\0":
'???',

# Maya Ibuki 
"センパイって、金髪にしてるのに\nちっとも痛まないですよね。\nいつから金髪にしてるんですか？\n\0":
'???',

# Makoto Hyuga
"いつも綺麗な明るい色ですね、\nその髪。▽\nそういえば、いつから\n金髪にしているんですか？\n\0":
'???',

# Shigeru Aoba
"赤木博士の金髪って、綺麗ですね。\n俺、学生の頃、金髪にしましたけど、\n綺麗な色にはならなかったっスよ。▽\nいつ頃から、そんな風に\nしてるんですか？\n\0":
'???',

# Ryoji Kaji
"リッちゃんさ、\nいつから金髪にしてるんだい？▽\n出会った頃から、ずっとだろ。\n気になってね…。\n\0":
'???',

# Toji Suzuhara 
"リツコさんて、その髪、\nいつから金髪にしてるんですか？\n\0":
'???',

# Kaworu Nagisa 
"髪、綺麗ですね。\n元はそんな色じゃ\nなかったんでしょう？▽\nいつからそんな色に\nしたんですか？\n\0":
'???',

# Ritsuko Akagi 
"………。▽\nそんな事はいつだったか忘れたわ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"リツコは、\n少し不機嫌そうな顔をした。▽\n聞いてはいけない事だったのかも\nしれない。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、リツコを見ると、\nある女性を思い出した…。▽\nマギシステムの開発者、\n赤木ナオコ。▽\n最近になって、\n彼女にはその面影が\n色濃く現れてきたようだ…。\n\0":
'???',

# Kozo Fuyutsuki
"昔、君が高校生の頃、研究所に\n顔を出した時、本当にナオコ君に\n似ていて驚いたよ。▽\n何回か、間違えて声をかけようと\nしたんだがな…。\n\0":
'???',

# Ritsuko Akagi 
"あら、今じゃ、\n間違える事もないでしょう？\nこの髪の色なら。\n\0":
'???',

# Kozo Fuyutsuki
"そうだな、\nだがやはりよく似てきたよ。\nお母さんにな。\n\0":
'???',

# Ritsuko Akagi 
"そうですか…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女は薄く笑って、\n科学者の顔になった…。▽\n誉め言葉のつもりだったが、\n言うべき事ではなかったのかも\nしれない…。\n\0":
'???',

# Naoko Akagi
"所長、碇所長…。\n少しよろしいですか？\nああ、冬月先生もこちらに…。\n\0":
'???',

# Ritsuko Akagi 
"碇司令…。\n\0":
'???',

# Gendo Ikari
"ああ、君か。\n\0":
'???',

# Ritsuko Akagi 
"この書類にサインを…。\nはい、ありがとうございます。\n\0":
'???',

# Ritsuko Akagi 
"さっき、誰と間違えたんですか？\n誰かと勘違いされていたよう\nですけど。\n\0":
'???',

# Gendo Ikari
"いや、そんな事はない。\n\0":
'???',

# Ritsuko Akagi 
"…………。▽\nそうですか。\n\0":
'???',
}
