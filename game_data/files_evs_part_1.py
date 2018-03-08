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
# ./USRDIR/event/a000.har_EXTRACT/a000.evs
#
# Shigeru Aoba, Male Staff
"第$d使徒、第３新東京市\n$fエリア付近に出現。\n\0":
'The $d Angel has appeared in the\n vicinity of Tokyo-3\'s $f area.\n\0',

# Shigeru Aoba, Male Staff
"目標を映像で確認。\n出ます！\n\0":
'Target has been visually verified.\n On-screen!\n\0',

# Misato Katsuragi 
"ほっほぉー、\nこりゃまた、立派な殿方だこと。▽\nここを目指してまっしぐらね。\n\0":
'???',

# Kozo Fuyutsuki
"ゆっくりだが、真っ直ぐここを\n目指しているな。\n\0":
'???',

# Female Staff
"目標、現在の速度を保ったまま\n直上地点を目指しています。\n\0":
'???',

# Makoto Hyuga, Female Staff
"現在、国連軍と交戦中。\nやはり、通常兵器では\n歯が立たないようですね。\n\0":
'???',

# Misato Katsuragi 
"彼の攻撃パターンは？\n\0":
'What about his attack pattern?\n\0',

# Kozo Fuyutsuki
"ヤツの攻撃パターンは？\n\0":
'What about its attack pattern?\n\0',

# Female Staff
"目標の武器となるものは、\n何か見当たりますか？\n\0":
'???',

# Makoto Hyuga
"いえ、今のところ、\nそれらしきものは\n見当たりませんが。▽\nただ、あの前腕部の槍状のものが\n気になりますね…。\n\0":
'???',

# Female Staff
"いえ、今のところ、\nそれらしきものは\n見当たりません。▽\nただ、あの前腕部の槍状のものが\n気にはなりますが…。\n\0":
'???',

# Shigeru Aoba, Male Staff
"市民の避難はすべて終了しました。▽\n国連軍がΝ地雷発動！\n\0":
'???',

# Misato Katsuragi 
"どう、\n足止めくらいにはなったかしら？\n\0":
'???',

# Kozo Fuyutsuki
"どうだ、\n少しは損傷を与えられたか。\n\0":
'???',

# Female Staff
"電波障害のため、\nモニターでは確認出来ません。\n\0":
'???',

# Makoto Hyuga, Female Staff
"爆心地よりエネルギー反応。\n使徒、市街地を攻撃！\n\0":
'???',

# Misato Katsuragi 
"顔が二つに…。\n自己修復機能を\n持ち合わせているようね。\n\0":
'???',

# Kozo Fuyutsuki
"顔が二つに…、自己修復機能か。\nどうやら、あの顔の様なものを\n蘇生させたらしいな。\n\0":
'???',

# Female Staff
"顔面部らしきものが、増えています。\n恐らく、自己修復機能によるもの\nでしょう。\n\0":
'???',

# Makoto Hyuga, Female Staff
"ええ、先程の攻撃もあの目らしき\nところから発せられた、不可視の\n破壊光線によるものと思われます。\n\0":
'???',

# Misato Katsuragi 
"チョッチ、強烈すぎるウインクね。\n機能増幅までも、可能か。▽\nそれじゃ、作戦伝達と\n行きましょうか！！\n\0":
'???',

# Kozo Fuyutsuki
"たいしたものだ。\n機能増幅まで可能とは。\n\0":
'???',

# Kozo Fuyutsuki
"こうしてはおれんな、\n今回の作戦要項を\nパイロットに伝えよう。\n\0":
'???',

# Female Staff
"使徒は、機能を増幅させている\nようですね。▽\nでは、こちらで使徒迎撃のための\n作戦をパイロットに説明します。\n\0":
'???',

#
# ./USRDIR/event/f049.har_EXTRACT/f049.evs
#
# [Text Only - No Designated Speaker]
"激しい子供の泣き声が、聞こえる。\n母親であろう女性が\n幼児を抱いてオロオロしている。▽\n病院には休診の札が掛かっていた。\nあの母親は、\nこの病院を目指していたのだろう。\n\0":
'???',

# Kozo Fuyutsuki
"どうか、しましたか？\n\0":
'???',

# Baby's Mother
"子供が今までになく\n激しく泣いて…。▽\n何分かおきに泣き止むんですけど、\nまた、激しく泣いて…。\n\0":
'???',

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
'???',

# Kozo Fuyutsuki
"後少しの辛抱だ。\nタクシーで、この病院に行きなさい。▽\nそれと、受付けでこの紙を渡せば\nあとは医師にまかせておけばいい、\n治療費も必要ない。\n\0":
'???',

# Baby's Mother
"あ、ありがとうございます…。\n\0":
'???',

# Kozo Fuyutsuki
"礼はいい、急ぐんだ。\n\0":
'???',

# Baby's Mother, Toji Suzuhara
"ハイ…。\n\0":
'???',

# Kozo Fuyutsuki
"ありがとうございます…か。\n\0":
'???',

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

# Male Staff,Shigeru Aoba
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
# ./USRDIR/btl/bevent.har_EXTRACT/ba005.evs
#
# Misato Katsuragi 
"エヴァ両機は\n距離をとって射撃して！\n\0":
'???',

# Kozo Fuyutsuki
"エヴァ両機は距離をとって射撃！\n\0":
'???',

# Misato Katsuragi 
"シンジ君は距離をとって射撃して！\n\0":
'???',

# Kozo Fuyutsuki
"初号機は距離をとって射撃！\n\0":
'???',

# Female Staff
"初号機パイロットは\n距離をとって射撃して下さい！\n\0":
'???',

# Misato Katsuragi 
"アスカは距離をとって射撃して！\n\0":
'???',

# Kozo Fuyutsuki
"弐号機は距離をとって射撃！\n\0":
'???',

# Female Staff
"弐号機パイロットは\n距離をとって射撃して下さい！\n\0":
'???',

# Female Staff
"エヴァ両機は、\n距離をとって射撃して下さい！\n\0":
'???',

# Misato Katsuragi 
"レイは距離をとって射撃して！\n\0":
'???',

# Kozo Fuyutsuki
"零号機は距離をとって射撃！\n\0":
'???',

# Female Staff
"零号機パイロットは\n距離をとって射撃して下さい！\n\0":
'???',

# Misato Katsuragi 
"トウジくんは\n距離をとって射撃して！\n\0":
'???',

# Kozo Fuyutsuki
"参号機は距離をとって射撃！\n\0":
'???',

# Female Staff
"参号機パイロットは\n距離をとって射撃して下さい！\n\0":
'???',

# Misato Katsuragi 
"カヲルくんは\n距離をとって射撃して！\n\0":
'???',

# Kozo Fuyutsuki
"四号機は距離をとって射撃！\n\0":
'???',

# Female Staff
"四号機パイロットは\n距離をとって射撃して下さい！\n\0":
'???',

#
# ./USRDIR/btl/bevent.har_EXTRACT/d052.evs
#
# Shinji Ikari
"わぁぁっ！\n\0":
'???',

# Shinji Ikari
"くぁぁっ！！\n\0":
'???',

# Asuka Soryu Langley
"キャー！\n\0":
'???',

# Asuka Soryu Langley
"きゃうッ！！\n\0":
'???',

# Asuka Soryu Langley
"あああああッ…！！\n\0":
'???',

# Rei Ayanami 
"……っ！\n\0":
'???',

# Rei Ayanami 
"きゃぁぁぁ…！！\n\0":
'???',

# Rei Ayanami 
"くっ…！！\n\0":
'???',

# Toji Suzuhara 
"…んがっ！？\n\0":
'???',

# Toji Suzuhara 
"うあっ…！？\n\0":
'???',

# Kaworu Nagisa 
"………うっ！\n\0":
'???',

# Kaworu Nagisa 
"ぐあっ！！\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk047.evs
#
# Kaworu Nagisa 
"………シンジ君。\n\0":
'...Shinji-kun.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le509.evs
#
# Kaworu Nagisa 
"仕方ないさ。\n当面の間はね。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"リリンの予定調和に\n組み込まれている事へ不満を\n感じているだろ？\n\0":
'???',

#
# ./USRDIR/event/cev0616.har_EXTRACT/cev0616.evs
#
# [Text Only - No Designated Speaker]
"他人の言う事が、遠くにいても\n耳元で聞こえる。\n最近、何となく気付いた事だ。▽\n人が何を考えているのかも\n何となくわかるようになった。\nだからといって、驚きも無かった。▽\n何を言われても、何があっても\nニュートラルな感情を保っている\n自分に、少し驚きはしたのだが。\n\0":
'???',

# Kozo Fuyutsuki
"心を明らかにするのは、\nこんな事なのかもしれないな…。\n\0":
'???',

# Kozo Fuyutsuki, Toji Suzuhara,[Text Only - No Designated Speaker], Female Staff, Misato Katsuragi, Hikari Horaki, Shinji Ikari, Asuka Soryu Langley, Rei Ayanami, Kaworu Nagisa, Ritsuko Akagi, Maya Ibuki, Ryoji Kaji, Shigeru Aoba, Male Staff, Gendo Ikari,(Unknown Id: 1100, Maybe: Receptionist), Kensuke Aida, Makoto Hyuga,Pen Pen,Shinji's Shadow [Leliel],Asuka's Shadow [Leliel],Rei's Shadow [Leliel],Toji's Shadow [Leliel],Kaworu's Shadow [Leliel]
"\0":
'???',

# Shigeru Aoba
"最近の副司令、絶対変だ。\nまるで夢遊病だよ。\n\0":
'???',

# Makoto Hyuga
"ああ…、でも…。\n表情が柔らかくなったと言うか。▽\n以前みたいに近寄り難い感じが\n無くなったと思う。▽\n何かあったのかな…。\n\0":
'???',

# Shigeru Aoba
"俺、女だと思うな。\n\0":
'???',

# Makoto Hyuga
"シッ！！\n副司令が来たぞ！！\n\0":
'???',

# Shigeru Aoba
"うぉ、やべぇ！！\n\0":
'???',

# Kozo Fuyutsuki, Rei Ayanami, Gendo Ikari, Hikari Horaki, Misato Katsuragi, Kensuke Aida,Toji's Sister, Shinji Ikari, Asuka Soryu Langley, Shigeru Aoba, Maya Ibuki, Ritsuko Akagi, Kaworu Nagisa, Makoto Hyuga
"…………………。\n\0":
'???',

#
# ./USRDIR/event/tev0272.har_EXTRACT/tev0272.evs
#
# Misato Katsuragi 
"ここは冷蔵庫。\n私はビール♪\nシンジ君はジュースね。▽\n水分を回復したい時は、\nここでジュースを飲んでネ。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk037.evs
#
# Shinji Ikari
"行くなら本気で戦えよ。\n僕を本気で倒してから行けよ！！\n\0":
'???',

# Kaworu Nagisa 
"わかったよ、シンジ君。\n\0":
'I understand, Shinji-kun.\n\0',

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
# ./USRDIR/event/tev0410.har_EXTRACT/tev0410.evs
#
# Shinji Ikari
"綾波は、何故コレに乗るの？\n\0":
'Ayanami, why do you pilot?\n\0',

# Rei Ayanami 
"…………………。\n絆だから。\n\0":
'......\n Because I\'m connected.\n\0',

# Shinji Ikari
"絆？\n\0":
'Connected?\n\0',

# Rei Ayanami 
"そう、絆。\n\0":
'Yes, connected.\n\0',

# Shinji Ikari
"父さんとの？\n\0":
'To my father?\n\0',

# Rei Ayanami 
"…みんなとの。\n\0":
'...To everyone.\n\0',

# Shinji Ikari
"強いんだな…綾波は。\n\0":
'You\'re strong, Ayanami.\n\0',

# Rei Ayanami 
"私には、他に何もないもの。\n\0":
'I have nothing else.\n\0',

# Shinji Ikari
"他に何もないって？\n\0":
'Nothing else?\n\0',

# Shigeru Aoba, Male Staff
"目標はエヴァ初号機の\n迎撃開始ラインを通過しました！\n\0":
'???',

# Rei Ayanami 
"時間よ。\n行きましょ。\n\0":
'It\'s time.\n Let\'s go.\n\0',

# Shinji Ikari, Toji Suzuhara, Kensuke Aida
"綾波…。\n\0":
'Ayanami...\n\0',

# Rei Ayanami, Kaworu Nagisa
"さよなら。\n\0":
'Farewell.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le133.evs
#
# Shinji Ikari
"自分の事だけで精一杯なんだ。\n他人の事まで考えている\n余裕なんかないよ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"他人は、自分を映し出す\n鏡だからね。▽\n少なからず、他人を意識せずには\nいられないものだよ。▽\nだから、君は僕を無視する事は\n出来ない。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk026.evs
#
# Shinji Ikari
"君が使徒でも構わない。\nだから一緒にいてよ！\n\0":
'???',

# Kaworu Nagisa 
"相容れない存在なんだ。\n悲しいけれど、僕らは共に\n生きる事は出来ないんだよ。\n\0":
'???',

#
# ./USRDIR/event/cev1205.har_EXTRACT/cev1205.evs
#
# Toji Suzuhara 
"あの…、リツコさん？\nワシの妹、治りますよね。\n顔…の傷。\n\0":
'???',

# Ritsuko Akagi 
"顔の傷はね。\n\0":
'???',

# Toji Suzuhara 
"そうですか！？\nえ…？\nあの…、他にも何か？\n\0":
'???',

# Ritsuko Akagi 
"あなたのお父さんは\n知っている事だけど…。\n妹さんはね、重い病気なのよ。\n\0":
'???',

# Toji Suzuhara 
"へ…、病気？\n\0":
'???',

# Ritsuko Akagi 
"具体的な発症が見られる前に、\n検査でわかったの。▽\nこればかりは、骨髄のドナーが\n現れるのを待つしかないわ。\n\0":
'???',

# Toji Suzuhara 
"やたら入院が長引いてたのんて、\n怪我だけやなかったんですね…。▽\nあのっ…、ドナーって。\nワシの…、\nワシのは使えないんですか！？\n\0":
'???',

# Ritsuko Akagi 
"残念ながら、ご家族には\nドナーになりえる者はいないわ。▽\nそれに、傷が治らないと\n効果的な治療が出来ないの。▽\n何にしろ時間がかかるわね。\n\0":
'???',

# Toji Suzuhara 
"そんな…、そんな…。\nあんまりや…。▽\nワシに出来る事は、何もないんか…。\n\0":
'???',

# Ritsuko Akagi 
"あなたにしか守れないのよ、\n妹さんは。▽\n適合するドナーを見つける為にも\n人々を使徒から守らないと\nいけないのよ。\n\0":
'???',

# Toji Suzuhara 
"…妹は長くないんですか？\nその、ドナーが見つからん\nかったら…。\n\0":
'???',

# Ritsuko Akagi 
"本人の体力次第という事も\nあるわ。▽\nはっきりとした事は\n何も言えないのよ。\n外出も、この先難しくなるわ。\n\0":
'???',

# Toji Suzuhara , Gendo Ikari, Kaworu Nagisa, Kensuke Aida, Ritsuko Akagi, Shigeru Aoba, Rei Ayanami, Shinji Ikari, Misato Katsuragi, Female Classmate, Asuka Soryu Langley
"………………。\n\0":
'???',

#
# ./USRDIR/btl/bevent.har_EXTRACT/d080.evs
#
# Shinji Ikari
"このぉ！\n\0":
'???',

# Shinji Ikari
"行けぇ！！\n\0":
'???',

# Shinji Ikari
"よぉし！！\n\0":
'???',

# Asuka Soryu Langley
"見てらっしゃい！！\n\0":
'???',

# Asuka Soryu Langley
"覚悟なさい！！\n\0":
'???',

# Asuka Soryu Langley
"これでも食らえ！！\n\0":
'???',

# Rei Ayanami 
"零号機、行きます…。\n\0":
'???',

# Rei Ayanami 
"今だわ…。\n\0":
'???',

# Rei Ayanami 
"捉えた…。\n\0":
'???',

# Toji Suzuhara 
"容赦せえへんでぇ！！\n\0":
'???',

# Toji Suzuhara 
"おんどりゃああ！！\n\0":
'???',

# Toji Suzuhara 
"なめんなァ！！\n\0":
'???',

# Kaworu Nagisa 
"今だ…。\n\0":
'???',

# Kaworu Nagisa 
"手加減なしだよ…。\n\0":
'???',

# Kaworu Nagisa 
"チャンス！！\n\0":
'???',

#
# ./USRDIR/event/tev0253.har_EXTRACT/tev0253.evs
#
# Ritsuko Akagi 
"横軸が関心の高さを表すの。\n相手方向に近いほど関心が高い。\n無視出来ない相手というわけね。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le111.evs
#
# Shinji Ikari
"いい事なんか無いよ。\nこれ以上嫌われない為に\n何もしない方がいいんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"嫌われないかわりに、\n皆から忘れ去られても？\n自分の存在がなくなっても？\n\0":
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
# ./USRDIR/event/cev1208.har_EXTRACT/cev1208.evs
#
# Female Staff
"血糖値が急激に上昇して\n危険な状態でしたが、\n今は落ち着いています。\n\0":
'???',

# Toji Suzuhara 
"そうですか。▽\nやっぱ、\nワシがいかんかったのですか？▽\n海見たら喜ぶやろうと…。\nそればっかり、ワシは…。\n\0":
'???',

# Female Staff
"今日はゆっくり休ませた方が\nいいと思います。\n面会は短くお願いします。\n\0":
'???',

# Toji's Sister
"帰ってきてくれたんや…。\n\0":
'???',

# Toji Suzuhara 
"当たり前や。\nお前を置いて、死んだりせえへん。\n\0":
'???',

# Toji's Sister, Shinji Ikari, Rei Ayanami
"うん…。\n\0":
'???',

# Toji Suzuhara 
"スマンかったなぁ…。\nほら、汗ふいたる。\n\0":
'???',

# Toji's Sister
"ありがと、兄ちゃん。\n海、行きたいの知ってたんや。▽\n海、キレイやったぁ…。\nめっちゃ嬉しかった…。\n\0":
'???',

# Toji Suzuhara 
"そか…、よかった。\n\0":
'???',

# Toji's Sister
"兄ちゃん。\n\0":
'???',

# Toji Suzuhara 
"何や？\n\0":
'???',

# Toji's Sister
"ウチらを守ってね。\n\0":
'???',

# Toji Suzuhara 
"ああ、きっとな。\n\0":
'???',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba016.evs
#
# Shigeru Aoba, Male Staff
"$fエリア、国連軍、\n掃滅しました！\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le103.evs
#
# Shinji Ikari
"別に、嫌われたっていい。\n全ての人に好かれるなんて、\nそんな事はムリなんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"人は一人でも生きていける。\n楽しい思い出だけを胸に\n生きていける。▽\nけどね、\nそのうちきっと寂しくなるんだ。\n心の渇きに気づくんだ。▽\n他人に興味の無いフリを続けながら。\n\0":
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
# ./USRDIR/event/tev0270.har_EXTRACT/tev0270.evs
#
# Shinji Ikari
"はい…。\nただ…いま…。\n\0":
'???',

# Misato Katsuragi 
"お帰りなさい。\n\0":
'???',

# Misato Katsuragi 
"さ、ここが私のマンション。\nそして、今日からあなたの家よ。\n\0":
'???',

# Misato Katsuragi 
"ただいま〜っと。\nさ、上がって！\n\0":
'???',

# Shinji Ikari, Kensuke Aida
"お邪魔します。\n\0":
'???',

# Misato Katsuragi 
"ただいま、でしょ？\n\0":
'???',

#
# ./USRDIR/event/bb008.har_EXTRACT/bb008.evs
#
# Kozo Fuyutsuki
"…碇。\n\0":
'???',

# Gendo Ikari
"……………………………。▽\nわかっている、初号機を出せ。\n凍結は解除だ！\n\0":
'???',

# Kozo Fuyutsuki
"一刻を争う。\nすぐに初号機を出せ。\n\0":
'???',

# Male Staff
"はっ…！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"初号機の凍結が解除されました。\n初号機が出撃可能になります。\n\0":
'???',

# Gendo Ikari
"初号機を出せ。\n\0":
'???',

# Male Staff
"しかし、初号機は委員会から\n凍結命令が…。\n\0":
'???',

# Gendo Ikari
"出せ…。\n\0":
'???',

# Male Staff
"は、はい。\n初号機、スタンバイさせます！！\n\0":
'???',

# Kozo Fuyutsuki
"初号機を出すんだ。\n\0":
'???',

# Kozo Fuyutsuki
"何のためのエヴァだ…。\n負けてからでは意味が無い。\n委員会には私が言っておく。\n\0":
'???',

# Female Staff
"たった今、委員会の方から\n初号機の凍結解除命令が\n下りました。▽\n整備班が今、セットアップに\n取りかかっています。\n\0":
'???',

# Male Staff
"了解…。\n委員会も出し惜しみは無しって\nことか。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk017.evs
#
# Shinji Ikari
"僕は、君の事を友達だと思ってた。▽\nこんな事にならずに\nずっと友達でいられると思ってた。\n\0":
'???',

# Kaworu Nagisa 
"それは、君の抱いた恐れ。\nそして、希望。▽\n僕は、君達リリンとは\n歩いてはいけないんだ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le316.evs
#
# Rei Ayanami 
"それでも私はエヴァに乗っている。▽\n絆のために、\n人と人の結びつきのために、\n私は戦っている。\n\0":
'???',

# Rei's Shadow [Leliel]
"エヴァで得たものは\nいずれ消え失せるわ。\n絆も消え失せる。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le519.evs
#
# Kaworu Nagisa 
"そう…かもしれない…な。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"フフ…、でも敵は敵だよ？\n彼らも最終的には絶対に\n君を受け入れないだろうね。\n\0":
'???',

#
# ./USRDIR/event/cev1401.har_EXTRACT/cev1401.evs
#
# Female Classmate
"ホラ、委員長の洞木さん、\nあそこのお姉さんって、そーとー\n乱れてるらしいね。\n\0":
'???',

# Female Classmate
"ホントー？\n委員長見てると、すっごい\nマジメな家庭かなーって思うのに。\n\0":
'???',

# Female Classmate
"逆、逆。\nホラ、あそこの高級住宅街に\n住んでてちょーお金持ちなの。▽\nホントは、何でもしたいほーだい\nみたいよ。\n\0":
'???',

# Female Classmate
"で、あそこのお姉さんが何だって？\n\0":
'???',

# Female Classmate
"私のお姉ちゃんの友達、洞木の\n姉キに彼氏取られたんだよ。▽\n半月前に、他の友達の彼氏も\n取ってさ。\nあだ名がピラニアって言うのよ。\n\0":
'???',

# Female Classmate
"あっはっはっは。\n\0":
'???',

# Female Classmate
"だいたい、委員長って\nちょっとエバリすぎ。\n\0":
'???',

# Female Classmate
"そうそう、何様のつもりかっての。\n正義感強そうに見せて、先生に\n媚び売るなっての。\n\0":
'???',

# Hikari Horaki
"よそでやってくれるかしら。\n\0":
'???',

# Female Classmate
"何の話よ…？\n\0":
'???',

# Female Classmate
"ここは教室でしょ、\n私達がいたってかまわないじゃない。\nネ〜ェ。\n\0":
'???',

# Female Classmate
"何なら、あんたが出て行けば？\n\0":
'???',

# Hikari Horaki, Shinji Ikari, Asuka Soryu Langley, Rei Ayanami, Misato Katsuragi, Gendo Ikari, Ritsuko Akagi, Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Ryoji Kaji, Kaworu Nagisa, Toji Suzuhara, Misato Katsuragi [Flashback], Kozo Fuyutsuki,(Unknown Id: 1100, Maybe: Receptionist), Female Staff,Pen Pen
"………。\n\0":
'???',

# Toji Suzuhara 
"やめぇーや、お前ら。\n\0":
'???',

# Female Classmate
"何よ…。\n\0":
'???',

# Female Classmate
"行こ、行こ…。\n\0":
'???',

# Toji Suzuhara 
"けっ、クサレどもが。\n\0":
'???',

# Hikari Horaki
"…。▽\nごめんね、ありがとう。\n\0":
'???',

# Toji Suzuhara 
"別にえーよ、\nあんなんが許せへんだけじゃ。\n\0":
'???',

# Toji Suzuhara 
"ま、気にすんな。\n委員長は、そんな顔似合わへん。\n\0":
'???',

# Hikari Horaki, Shinji Ikari, Misato Katsuragi, Kensuke Aida
"え…？\n\0":
'???',

# Toji Suzuhara 
"小姑みたいにガミガミしとった方が\n委員長らしーわ。\n\0":
'???',

# Hikari Horaki
"…！！▽\nスズハラ〜〜〜〜〜〜〜！\n\0":
'???',

# Toji Suzuhara 
"コワ、ほら来た！！\n逃げるが勝ちや！！\nほな、お疲れさん！！\n\0":
'???',

# Hikari Horaki
"もぉ………。\n\0":
'???',

# [Text Only - No Designated Speaker]
"気が付いたら、遅かった。\nもう、好きになっていた。▽\n誰かを想う力。\nそしてその力を持った時…、\n私は…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"世界すら、\n変わってしまう事に気が付いた。▽\n気持ちを言えなくても。\n伝えられなくても…。\n\0":
'???',

#
# ./USRDIR/event/a002.har_EXTRACT/a002.evs
#
# Shigeru Aoba, Male Staff
"国連艦隊より緊急入電！\n太平洋上にて新型エヴァの部品を\n搬送中、突如使徒が出現。▽\n襲撃を受けた模様です！\n\0":
'???',

# Misato Katsuragi 
"何ですって？\n\0":
'???',

# Kozo Fuyutsuki, Misato Katsuragi 
"何？\n\0":
'???',

# Female Staff, Asuka Soryu Langley
"！？\n\0":
'???',

# Makoto Hyuga, Male Staff
"使徒は新型エヴァの部品を破壊！\nその後、姿を消したようです。\n\0":
'???',

# Misato Katsuragi 
"…エヴァが使徒を\n引き寄せるのかしら。\n\0":
'???',

# Kozo Fuyutsuki
"…使徒め…、\nエヴァが狙いか。\n\0":
'???',

# Female Staff
"…やはり、エヴァが使徒を\n引き寄せるんでしょうか。\n\0":
'???',

# Ritsuko Akagi 
"いずれにせよ、間違いなく来るわね。\n次はココよ。\n\0":
'???',

# Male Staff
"恐らく次はここに来ますね。\n\0":
'???',

# Makoto Hyuga
"これは、国連艦隊の\n戦闘記録分析結果です。▽\n目標は一定距離内に侵入した外敵を、\n加粒子砲で自動排除するものと\n思われます。▽\n展開されるΑΤフィールドは、\n相転移空間を肉眼で確認出来る程、\n超強力なものです。\n\0":
'???',

# Male Staff
"これが、国連艦隊の\n戦闘記録分析結果です。▽\n目標は一定距離内に侵入した外敵を、\n加粒子砲で自動排除するものと\n思われます。▽\n展開されるΑΤフィールドは、\n相転移空間を肉眼で確認出来る程、\n超強力なものです。\n\0":
'???',

# Misato Katsuragi 
"強力な加粒子砲とΑΤフィールド。\n攻守共にパーペキな空中要塞ね。\n\0":
'Its particle cannon and A.T. Field are powerful.\n In terms of offense and defense, it\'s the perfect floating fortress.\n\0',

# Kozo Fuyutsuki
"強力な加粒子砲とΑΤフィールド。\nまさに完璧な空中要塞だな。\n\0":
'Its particle cannon and A.T. Field are potent.\n Truly a consummate floating fortress.\n\0',

# Female Staff
"強力な加粒子砲とΑΤフィールド。\nまさに完璧な空中要塞ですね。\n\0":
'Its particle cannon and A.T. Field are powerful.\n It certainly is a perfect floating fortress.\n\0',

# Makoto Hyuga
"エヴァによる接近戦は\n危険過ぎますね。\nどうします？\n\0":
'???',

# Male Staff
"エヴァによる接近戦は\n危険過ぎます。\nどうしましょうか？\n\0":
'???',

# Misato Katsuragi 
"どうします？\nそうねぇ…。\n\0":
'???',

# Misato Katsuragi 
"んふふ〜、\n私ね、チョッチ、\nやってみたい事があるの。\n\0":
'???',

# Kozo Fuyutsuki
"何も手立てがないわけではない。\nだがな…。\n\0":
'???',

# Female Staff
"…アレを使えば、もしかして…。\n\0":
'???',

# Kozo Fuyutsuki
"目標のレンジ外、\n超長距離からの直接狙撃かね。\n\0":
'???',

# Misato Katsuragi 
"そうです。▽\n加粒子砲を受けずに攻撃する方法は、\n目標のΑΤフィールドを中和せず\nレンジ外からの一点狙撃のみ。▽\nマギによる回答は\n勝算８．７パーセント、\n最も高い数値です。\n\0":
'???',

# Kozo Fuyutsuki, Ryoji Kaji, Gendo Ikari, Shigeru Aoba, Makoto Hyuga, Hikari Horaki, Toji Suzuhara, Maya Ibuki, Misato Katsuragi,Pen Pen
"……………………。\n\0":
'???',

# Kozo Fuyutsuki
"加粒子砲を受けずに攻撃するには、\n目標のΑΤフィールドを中和せず、\nレンジ外から一点狙撃するしかない。\n\0":
'???',

# Male Staff
"目標のレンジ外、\n超長距離からの直接狙撃ですか。\n\0":
'???',

# Misato Katsuragi 
"そうよ。▽\n加粒子砲を受けずに攻撃するには、\n目標のΑΤフィールドを中和せず、\nレンジ外からの一点狙撃しかないわ。\n\0":
'???',

# Male Staff
"目標のレンジ外、\n超長距離からの直接狙撃？\n\0":
'???',

# Female Staff
"目標のΑΤフィールドを中和せず、\nレンジ外からの一点狙撃…。\n確かにその方法しかありませんね。\n\0":
'???',

# Gendo Ikari
"反対する理由はない。\nやりたまえ、葛城君。\n\0":
'???',

# Gendo Ikari
"反対する理由はない。\n後は任せた。\n\0":
'???',

# Gendo Ikari
"了解した。\nでは、早速作戦開始だ。\n\0":
'???',

# Male Staff
"了解しました。\nでは、早速、準備に\n取りかかりましょう。\n\0":
'???',

# Male Staff
"では、早速、準備に\n取りかかりましょう。\n\0":
'???',

# Shigeru Aoba, Male Staff
"第$d使徒、第３新東京市\n$fエリア付近に\n出現しました！\n\0":
'???',

# Misato Katsuragi 
"来たわね。\nポジトロンスナイパーライフルは？\n\0":
'???',

# Kozo Fuyutsuki
"来たな。\nポジトロンスナイパーライフルの\n方はどうだ？\n\0":
'???',

# Male Staff
"こちらは準備ＯＫです。\nポジトロンスナイパーライフルの\n方はどうですか？\n\0":
'???',

# Ritsuko Akagi 
"なんとか間に合いました。\nもしもの時の盾も\n準備が出来ています。\n\0":
'???',

# Ritsuko Akagi 
"なんとか間に合ったわ。\nもしもの時の盾も準備ＯＫよ。\n\0":
'???',

# Maya Ibuki 
"ええ、なんとか間に合いました。\nもしもの時の盾も準備ＯＫです。\n\0":
'???',

# Female Staff
"なんとか間に合いました。\nもしもの時の盾も準備ＯＫです。\n\0":
'???',

# Misato Katsuragi 
"ご苦労様、それじゃぁ…作戦開始よ！\n\0":
'???',

# Kozo Fuyutsuki
"よし、では作戦開始だ！\n\0":
'???',

# Male Staff
"では、作戦開始ですね！\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk053.evs
#
# Kaworu Nagisa 
"ヒトが…、互いを必要と思うのは\nヒトの中にある何かのためなんだ。\nただそれだけのためなんだ。▽\n…でも、その何かに対して、\nヒトはみな、息を呑むほどに純粋だ。\nとても、哀しいほどに…。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le216.evs
#
# Asuka Soryu Langley
"こんなに苦しんでいるのに、\n気が付いてももらえないの？\n\0":
'???',

# Asuka's Shadow [Leliel]
"あなたも他人の苦しみが\n届かない位置にいる。\n\0":
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
# ./USRDIR/event/tev0235.har_EXTRACT/tev0235.evs
#
# Misato Katsuragi 
"感情、コンディション、\n技能、そして…、▽\n空腹、水分、眠気、ＷＣ、風呂の\n５つの体調の状態を見る事が\n出来るの。▽\nそれぞれの体調メーターは、\n時間の経過と共に減少していくわ。▽\nメーターがカラになると、\nもう限界って状態ね。\n\0":
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
# ./USRDIR/event/cev1410.har_EXTRACT/cev1410.evs
#
# Hikari Horaki
"せめて、素直になろう。\n例え気持ちが伝えられなくても。\n好きになってくれなくても。▽\n後悔だけは、しないように…。\n\0":
'???',

#
# ./USRDIR/event/tev1101.har_EXTRACT/tev1101.evs
#
# Ritsuko Akagi 
"長旅ご苦労様でした。\nロンギヌスの槍、\nケイジへの移送終了しました。\n\0":
'???',

# Gendo Ikari
"わかった。\n後の作業はレイに引き継ぐ。\n\0":
'???',

# Gendo Ikari
"レイ、後は任せた。\n\0":
'Rei, I leave the rest to you.\n\0',

# Rei Ayanami 
"はい、碇司令。\n\0":
'Yes sir, Commander Ikari.\n\0',

# Kozo Fuyutsuki
"常に血で濡らされた\nロンギヌスの槍…。\n\0":
'The ever-bloodied Spear of Longinus...\n\0',

# Gendo Ikari
"神を殺し、\nまた神を生む力を持った槍…。\n事は我々のシナリオ通りだよ。\n\0":
'A spear with the power to both kill and birthe gods...\n The situation is in accordance with our scenario.\n\0',

# Misato Katsuragi 
"どう？\nマギの診察は終わった？\n\0":
'???',

# Ritsuko Akagi 
"あと、少しよ。\n\0":
'???',

# Misato Katsuragi 
"さすがね。\n同じものが３つあって大変なのに。\n\0":
'???',

# Maya Ibuki 
"三基とも自己診断モードに\n入りました。▽\n第１２７次定期検診、終了。\n異常なし。\n\0":
'???',

# Ritsuko Akagi, Rei Ayanami, Shigeru Aoba, Kaworu Nagisa
"了解。\n\0":
'???',

# Misato Katsuragi 
"ね、少しは教えてよ。\nマギの事。\n\0":
'???',

# Ritsuko Akagi 
"長い話よ。\nそのわりに面白くない話。\n\0":
'???',

# Ritsuko Akagi 
"人格移植ＯＳって知ってる？\n\0":
'???',

# Misato Katsuragi 
"ええ、第７世代の\n有機コンピュータに個人の人格を\n移植して思考させるシステム。▽\nエヴァの操縦にも使われている\n技術よね。\n\0":
'???',

# Ritsuko Akagi 
"…の、第一号らしいわ。\n母さんが開発した技術だから。\n\0":
'???',

# Misato Katsuragi 
"…お母さんのパターンを\n移植したの？\n\0":
'???',

# Ritsuko Akagi 
"そうね。\n私はシステムアップしただけよ。▽\n基礎理論と本体を作ったのは\n母さんなの。\n\0":
'???',

# Ritsuko Akagi 
"マギは…言ってみれば、\n母さんそのものなのよ。\n\0":
'???',

#
# ./USRDIR/event/f037.har_EXTRACT/f037.evs
#
# [Text Only - No Designated Speaker]
"削除イベントです。\n\0":
'???',

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
# ./USRDIR/event/tev1104.har_EXTRACT/tev1104.evs
#
# Ritsuko Akagi 
"くっ、相手もなかなかのものね。\n計算速度を減速させるので\n精一杯だわ。\n\0":
'???',

# Ritsuko Akagi 
"プログラムが出来たわ。\n\0":
'???',

# Shinji Ikari, Misato Katsuragi 
"そ、そんな…。\n\0":
'N-no way...\n\0',

# Ritsuko Akagi 
"これでどう！？\n\0":
'???',

#
# ./USRDIR/event/bs002.har_EXTRACT/bs002.evs
#
# [Text Only - No Designated Speaker]
"$lが退院しました。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le404.evs
#
# Toji Suzuhara 
"イキって何が悪いねん。\n虚勢張るんのどこがアカンねんな！\n\0":
'???',

# Toji's Shadow [Leliel]
"ほな、\nイキってたんは認めんねんな？▽\n自分が、\n小さい弱い人間やっちゅうのも\n認めたんや。\n\0":
'???',

#
# ./USRDIR/event/tev0242.har_EXTRACT/tev0242.evs
#
# Maya Ibuki 
"同じマップにいる他人の情報が\n画面に表示されているのがわかる？▽\n相手と接する時に\n今どういう状態なのか、\n参考にするといいわよ。\n\0":
'???',

# Maya Ibuki 
"他人に関して、\nより詳しい状態を知るには、▽\nシステムメニューの\nステータスで確認出来るわ。\n\0":
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
# ./USRDIR/btl/tabris.har_EXTRACT/bk031.evs
#
# Shinji Ikari
"どうして？\nカヲル君が使徒なの？\n\0":
'???',

# Kaworu Nagisa 
"言っただろ、\n僕が仕組まれた子供と言う事を。\n\0":
'???',

#
# ./USRDIR/event/cev0706.har_EXTRACT/cev0706.evs
#
# Ryoji Kaji
"どうした、呼び出したりして。\n\0":
'???',

# Ritsuko Akagi 
"仕事の話じゃないわ。\n\0":
'???',

# Ryoji Kaji
"そうか。\nリッちゃんから誘うのは\n初めてだな。\n\0":
'???',

# Ritsuko Akagi 
"…そうね。\n\0":
'???',

# Ryoji Kaji
"理由は聞かないよ。\n昔の君も、理由は聞かなかった。\n\0":
'???',

# Ritsuko Akagi 
"あなたは…。\nいつも、誰かを見ていた\nわけじゃなかったもの。\n\0":
'???',

# Ryoji Kaji
"いや、ああ言うときは誠心誠意\n尽くしてるつもりさ。\n\0":
'???',

# Ritsuko Akagi 
"私…、昔に比べてどう？\n\0":
'???',

# Ryoji Kaji
"ルージュの似合う女に\nなったと思う。\n\0":
'???',

# Ritsuko Akagi 
"魅力的？\n\0":
'???',

# Ryoji Kaji
"ああ…。\n君からそんな質問が\n来るなんてね。\n\0":
'???',

# Ritsuko Akagi 
"そういうの、好きじゃないの？\n\0":
'???',

# Ryoji Kaji
"いや、可愛いよ。\n奇麗だ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"………………………………………\n………………………………………\n………………………………………。\n\0":
'???',

#
# ./USRDIR/event/cev1506.har_EXTRACT/cev1506.evs
#
# [Text Only - No Designated Speaker]
"あの空の向こうへ。\n星の彼方へ。\n僕が来た、あの空間へ。\n\0":
'???',

# Makoto Hyuga, Male Staff
"衛星軌道上に\nΑΤフィールドの発生を確認！\n\0":
'???',

# Misato Katsuragi 
"使徒なの！？\n\0":
'???',

# Female Staff
"使徒ですか！？\n\0":
'???',

# Shigeru Aoba, Male Staff
"目標を映像で捕捉。\n\0":
'???',

# Misato Katsuragi 
"な…！\n彼…が！？\n\0":
'???',

# Female Staff
"あれは…、\nフィフス・チルドレン！？\n\0":
'???',

# Shigeru Aoba, Male Staff
"やはり…、使徒なのか？\nあの苛酷な宇宙環境に、\n生身の身体でいられるなんて…。\n\0":
'???',

# Kaworu Nagisa 
"……………………。▽\n…静かだ。▽\n僕はこの静寂を知っている。\nずっと、昔から…。▽\nこの大きな安らぎを、\n僕は知っている…。▽\n僕が、僕になるずっと前から…。\n\0":
'???',

# ??? [Unnamed Seed of Life]
"君や、君の子孫達の約束の土地。\nそれがあの星だったのかい？\n\0":
'???',

# Kaworu Nagisa 
"………。▽\n誰…？\n\0":
'???',

# ??? [Unnamed Seed of Life]
"僕の声が届いたね。\n君の言葉と姿と声を借りて、\n対話する事を許してほしい。\n\0":
'???',

# Kaworu Nagisa 
"誰なんだい…？\n\0":
'???',

# ??? [Unnamed Seed of Life]
"今となっては名前もない。\n姿もない。\n生命そのものになった存在さ。▽\n君の魂は、\n生命の実を食べ過ぎて、\n昔の事を忘れたようだ…。\n\0":
'???',

# Kaworu Nagisa 
"僕を知ってるの…？\n\0":
'???',

# ??? [Unnamed Seed of Life]
"故郷を同じくした\n種族だからね。\n\0":
'???',

# Kaworu Nagisa 
"第一始祖民族…？\n\0":
'???',

# ??? [Unnamed Seed of Life]
"そうとも言えるね…。▽\n思い出せない？▽\n僕らは故郷の星を失う事を知り、\n別の生きていくべき星を探して\n宇宙のただなかへ旅に出た…。▽\n生命の根源の姿へ自分達を戻し…。\n多くの民と共に、\nひとつへ交じり合いながら…。▽\nいつか、再び増え栄える為にね。\n\0":
'???',

# Kaworu Nagisa 
"僕は知りたいんだ…。\n自分が何者かを…。\n\0":
'???',

# ??? [Unnamed Seed of Life]
"君や僕を含めて、\n故郷の民を乗せたキャリアは\n７つあった。▽\n君や僕は、どこかの星へ着床した後、\n引き連れた民に\nどのような生命として姿を与えるか、▽\n代表してそれを決定する設計者だ。\n\0":
'???',

# Kaworu Nagisa 
"そうだ…。\n僕は目覚め…、使徒を生み出した。▽\n自分を見失った時の為に、\n計画書…裏死海文書を残して…。\n\0":
'???',

# Kaworu Nagisa 
"君も…、どこかの星で栄えて…？\n\0":
'???',

# ??? [Unnamed Seed of Life]
"僕らは、まだ旅の途中だ。▽\nどの星へ辿り着いて、\nどんな生命を創り出すのか。\nまだ、わからない…。\n\0":
'???',

# Kaworu Nagisa 
"僕の星は、同じ故郷の命が\n争いあっている。▽\nひとつの星に、二つのキャリアが\n着床した為に。▽\n本当は争いあうべきでは\nなかったんだ。\nお互い忘れてしまっただけなんだ。\n\0":
'???',

# ??? [Unnamed Seed of Life]
"君がその気なら、\nまた旅をするといい。\n君の民の魂を連れて。\n\0":
'???',

# Kaworu Nagisa 
"どうやって？\n\0":
'???',

# ??? [Unnamed Seed of Life]
"君はその姿を捨てなくては\nならないが。▽\n君の子らも、今の姿を捨てて\nキャリアに戻ればいい。▽\nどうだろう。\n僕と一緒に旅をするのは？\n\0":
'???',

# Kaworu Nagisa 
"ΑΤフィールドを…？\n\0":
'???',

# ??? [Unnamed Seed of Life]
"槍を呼ぶんだ。\n始まりの時を願って。\nそして君の民の魂を導けばいい。\n\0":
'???',

# Makoto Hyuga, Male Staff
"ケイジのエヴァが…、\n消失しました！\n\0":
'???',

# Misato Katsuragi 
"何ですって！？\n\0":
'???',

# Female Staff
"そんな、そんなはずは！？\n\0":
'???',

# Shigeru Aoba, Male Staff
"フィフスもです。\n目標、ロスト！\n\0":
'???',

# Misato Katsuragi, Female Staff
"どういう事…？\n\0":
'???',

# Kaworu Nagisa 
"さあ、行こう。\n僕の子ら。\nそして、リリンのしもべ…。▽\nさよなら、リリス。\nさよなら、リリン。▽\n歌を教えてくれて、ありがとう…。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le408.evs
#
# Toji Suzuhara 
"なんやねんな、演じてるって…。\n\0":
'???',

# Toji's Shadow [Leliel]
"だって、ホンマの自分とちゃうやん。\nめっちゃイキってるイメージ\n作ってるやんか。\n\0":
'???',

#
# ./USRDIR/event/cev1405.har_EXTRACT/cev1405.evs
#
# Rei Ayanami 
"女物の下着。\n\0":
'???',

# Hikari Horaki
"…！？▽\n買わされたの？\n\0":
'???',

# Rei Ayanami 
"お金を持たされて、\n選んできて欲しいって。\n鈴原君に頼まれたの。\n\0":
'???',

# Hikari Horaki
"アイツぅぅぅ〜〜〜！！\nセクハラ、セクハラだわ！！\n\0":
'???',

# Hikari Horaki
"ねえ…、綾波さん？\n\0":
'???',

# Rei Ayanami, Hikari Horaki
"何…？\n\0":
'???',

# Hikari Horaki
"鈴原と…どこに行ったの？▽\nほら、あの…。\n委員長として、ちょっと。▽\n鈴原ってあんまりマジメじゃないし。\n何か…綾波さんが迷惑な事\nされたんじゃないかなーって。\n\0":
'???',

# Rei Ayanami 
"買い物に付き合っただけ。\n\0":
'???',

# Hikari Horaki
"あ、そ、そう…。\n何を…？\n\0":
'???',

#
# ./USRDIR/event/n012.har_EXTRACT/n012.evs
#
# Misato Katsuragi, Female Staff
"これより戦闘結果報告を行います。\n\0":
'???',

# Female Staff, Misato Katsuragi 
"「ロンギヌスの槍」の使用が決断されます。\n\0":
'???',

# Misato Katsuragi, Female Staff
"第$d使徒(angel00の使徒ナンバー音声を使いまわす)\n\0":
'???',

# Misato Katsuragi, Female Staff
"結果、ロンギヌスの槍により、使徒殲滅に成功しますが、\n\0":
'???',

# Misato Katsuragi, Female Staff
"アラエル\n\0":
'???',

# Misato Katsuragi, Female Staff
"槍は第一宇宙速度を突破、月軌道に移行。\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標は衛星軌道上に突如出現\n\0":
'???',

# Misato Katsuragi, Female Staff
"ロンギヌスの槍は回収不能になりました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"超長距離射撃による対空迎撃を試みますが\n\0":
'???',

# Misato Katsuragi, Female Staff
"また、目標の心理攻撃により\n\0":
'???',

# Misato Katsuragi, Female Staff
"出力不足のため、ΑΤフィールドを突破は不可能でした\n\0":
'???',

# Misato Katsuragi, Female Staff
"作戦終了後、パイロットは死亡、\n致命的な損害を受けてしまいました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"以上、報告を終わります。\n\0":
'???',

# Misato Katsuragi, Female Staff
"この後、目標は心理攻撃を展開\n\0":
'???',

# Misato Katsuragi, Female Staff
"パイロットは、目標の心理攻撃に苦しめられます。\n\0":
'???',

# Misato Katsuragi, Female Staff
"この状況を打開するため、\n\0":
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
# ./USRDIR/btl/tabris.har_EXTRACT/bk032.evs
#
# Shinji Ikari
"何で僕の前に現われたの…？\nねえ、どうして…。\n\0":
'???',

# Kaworu Nagisa 
"僕の意思に関係なく、\n君に会うために\n生まれてきたからさ。▽\nでも、自分の意志で、\n君に会うためだったと思いたいよ。\n今は…。\n\0":
'???',

#
# ./USRDIR/event/cev0205.har_EXTRACT/cev0205.evs
#
# Teacher
"今日は、進路調査の\nプリントを渡します。▽\n各自、進路についてのプランを\n書いて提出するように。\n\0":
'???',

# Asuka Soryu Langley
"将来…、将来ねぇ…。\nもう大学出てるんだけどなぁ。\n白紙で出しちゃおうかしら。\n\0":
'???',

# Hikari Horaki
"私は栄養師かな。\nアスカはどうするの？\n\0":
'???',

# Asuka Soryu Langley
"そういえば私…、\n使徒を全部倒した後、\nどうすればいいんだろう。\n\0":
'???',

# Asuka Soryu Langley
"エヴァに乗らなくなった私を\n誰も必要としなくなるのかな…。\n\0":
'???',

# Hikari Horaki
"そんな事ないわよ。▽\nアスカは頭もいいし、\n美人だし。▽\n私達より、色んな可能性を\n持っているじゃない。\n\0":
'???',

# Asuka Soryu Langley
"でも、なりたいものなんて\nないの。▽\nエヴァのパイロットじゃないと\n意味がないのよ。\n\0":
'???',

# Hikari Horaki
"どうして…？\n私、アスカがパイロットでなくても\nきっと友達になってるわ。\n\0":
'???',

# Hikari Horaki
"そうそう、アスカだったら\n芸能界だって夢じゃないわよ。\nモデルとか。\n\0":
'???',

# Asuka Soryu Langley
"安っぽい大衆の為の商品なんかに\nなりたかないわよ。\n\0":
'???',

# Hikari Horaki
"なりたくてもなれない人って\nいるわよ…。\n\0":
'???',

# Asuka Soryu Langley
"なりたくなくてもなる人って\nいるんじゃない？\n\0":
'???',

# Hikari Horaki
"アスカ…。\n最近ちょっと偏屈じゃない？\n\0":
'???',

# Asuka Soryu Langley
"そう…？\n\0":
'???',

#
# ./USRDIR/event/tev0271.har_EXTRACT/tev0271.evs
#
# Misato Katsuragi 
"じゃあ、\n軽く家の中を案内するわね。\n\0":
'???',

# Misato Katsuragi 
"まずはキッチンから。\n\0":
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
'???',

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
'???',

# Maya Ibuki 
"さすがセンパイ。\n信じてました！！\n\0":
'That\'s my sempai.\n I believed in you!\n\0',

# Makoto Hyuga
"ふう…、\n生きた心地がしなかったよ。\n\0":
'???',

# Shigeru Aoba
"ハハハ…、\nやった、助かった…。\n助かったんだ…。\n\0":
'???',

# Ryoji Kaji
"やっぱり君は大した奴だよ。\nリッちゃん。\n\0":
'???',

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
# ./USRDIR/event/n004.har_EXTRACT/n004.evs
#
# Misato Katsuragi, Female Staff
"零号機\n\0":
'Unit-00\n\0',

# Misato Katsuragi, Female Staff
"参号機\n\0":
'???',

# Female Staff, Misato Katsuragi 
"かろうじて、使徒殲滅に成功。\n\0":
'???',

# Misato Katsuragi, Female Staff
"四号機\n\0":
'Unit-04\n\0',

# Misato Katsuragi, Female Staff
"マトリエル\n\0":
'Matarael\n\0',

# Misato Katsuragi, Female Staff
"パイロットの活躍により…\n\0":
'???',

# Misato Katsuragi, Female Staff
"第３新東京市に襲来\n\0":
'???',

# Misato Katsuragi, Female Staff
"使徒の強攻によりパイロット達は\n苦戦を強いられるも\n\0":
'???',

# Misato Katsuragi, Female Staff
"見事、使徒の殲滅に成功しました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標は、強力な溶解液を武器に市街地を侵攻\n\0":
'???',

# Misato Katsuragi, Female Staff
"これを討つべく、エヴァンゲリオン、出動。\n参戦したのは…\n\0":
'???',

# Misato Katsuragi, Female Staff
"初号機\n\0":
'Unit-01\n\0',

# Misato Katsuragi, Female Staff
"しかし、パイロットを失うという\n致命的な損害を受けてしまいました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"以上、報告を終了します。\n\0":
'???',

# Misato Katsuragi, Female Staff
"弐号機\n\0":
'Unit-02\n\0',

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
# ./USRDIR/event/e001.har_EXTRACT/e001.evs
#
# Ryoji Kaji
"………？？？？▽\nここは、葛城…の。\n\0":
'...???? ▽\n This is Katsuragi\'s...\n\0',

# Misato Katsuragi 
"加持くぅん…。\n\0":
'Kaji-kuun...\n\0',

# Ryoji Kaji
"葛城…？\n\0":
'Katsuragi...?\n\0',

# Ritsuko Akagi 
"誰を見てるってワケでもなく、\n私とも…とはね。▽\n私も、同罪ね。\n今日の事は忘れるわ。\n\0":
'???',

# Ryoji Kaji
"リッ…ちゃん…？\n\0":
'Ritchan...?\n\0',

# Rei Ayanami 
"おやすみなさい…。\n\0":
'It\'s time to sleep...\n\0',

# Ryoji Kaji
"…！！！！▽\nやっぱり…、\nサードインパクトが、\nその時が来たのか…？\n\0":
'...!!!!▽\nSo has Third Impact\n finally come after all...?\n\0',

# Ritsuko Akagi 
"レイ、レイなの？\n\0":
'Rei? Rei, is that you?\n\0',

# Shigeru Aoba, Male Staff
"使徒、ゼロエリア到達！\n\0":
'???',

# Hikari Horaki
"綾波さん…？\n\0":
'???',

# Maya Ibuki, Female Staff
"零号機、投擲状態にありません！\n\0":
'???',

# Rei Ayanami 
"…間に合わない。\nいえ、行かなければ…。▽\n私の出来る事は一つだけ…。\n\0":
'???',

# Toji Suzuhara 
"………あ？▽\n何や、病院…？▽\nせや、妹は、妹は無事なんか？\n\0":
'???',

# Toji Suzuhara 
"………？▽\n綾波…、\n何しに来てん…？\n\0":
'???',

# Rei Ayanami 
"かえりましょう。\n\0":
'???',

# Toji Suzuhara 
"帰るて、おい。▽\nおい！！\n何や、何も見えへん…。\n\0":
'???',

# Toji's Sister
"兄ちゃん、帰ろうや。\nなあ、帰ろうよ。\n\0":
'???',

# Toji Suzuhara 
"………お前？\n\0":
'???',

# Asuka Soryu Langley
"…ファースト？\n…誰？\n\0":
'...First?\n Who are you?\n\0',

# Kensuke Aida
"…あれっ？▽\nここは、学校？\n教室…？▽\n何で…、ここへ…。\n\0":
'???',

# Kensuke Aida, Shinji Ikari, Toji Suzuhara
"綾波…？\n\0":
'Ayanami...?\n\0',

# Misato Katsuragi 
"状況は？\n\0":
'???',

# Kozo Fuyutsuki
"どうした、パイロットからの\n信号が消えたぞ！！\n\0":
'???',

# Female Staff
"パイロットとの\n通信が途絶えました。\nこちらからの信号も受付けません！\n\0":
'???',

# Shigeru Aoba, Male Staff
"エヴァ…、活動停止。\nパイロット、………死亡確認。\n\0":
'???',

# Kaworu Nagisa 
"呼んでいる…。\nああ、僕は許されたんだ…。▽\nかえるべき場所が、\n僕にはあったんだ…。\n\0":
'???',

# Kozo Fuyutsuki
"レイ…か？\n\0":
'???',

# Makoto Hyuga, Female Staff
"使徒、ジオフロントに進入！\n依然、侵攻中！\n\0":
'???',

# Gendo Ikari
"レイ、レイなのか！？\n\0":
'???',

# Misato Katsuragi 
"総員、本部から撤退を………、\n急いで！\n\0":
'???',

# Kozo Fuyutsuki
"総員、本部から撤退しろ！\n\0":
'???',

# Makoto Hyuga, Male Staff
"総員、本部から撤退！！\n繰り返す、\n総員、本部から撤退！！\n\0":
'???',

# Shigeru Aoba, Maya Ibuki 
"レイ？\n\0":
'Rei?\n\0',

# Ryoji Kaji, Misato Katsuragi 
"レイ…？\n\0":
'Rei...?\n\0',

# Hikari Horaki
"綾波さん？\n\0":
'Ayanami-san?\n\0',

# Kaworu Nagisa , Asuka Soryu Langley
"ファースト…。\n\0":
'First...\n\0',

# Rei Ayanami 
"かえるの、みんな…。\nそして、また巡り会うの。\n\0":
'???',

# Makoto Hyuga
"君…か？\n\0":
'It\'s... you?\n\0',

# Misato Katsuragi 
"ここは、どこかしら…。\n何も、何もないわ…。\n\0":
'???',

# Hikari Horaki
"…？▽\nここは、教室…？▽\nどうして、ここへ…。\n\0":
'???',

# Makoto Hyuga, Male Staff
"使徒、ネルフ本部に到達！\nここまで、すぐ来ます！\n\0":
'???',

# Misato Katsuragi 
"くっ…………、\nこれまでか………。\n\0":
'???',

# Kozo Fuyutsuki
"もはや、これまでか…。\n\0":
'???',

# Rei Ayanami 
"お帰り…、\nお還りなさい…。\n\0":
'???',

# Shinji Ikari
"ここはどこ…、\nどこだろう？\n\0":
'???',

# Rei Ayanami 
"洞木さん…。\nかえりましょう。\n\0":
'Horaki-san...\n Let\'s go home.\n\0',

# Rei Ayanami 
"…あの光が、私だったもの。\nこの波が、碇君…。\n全てが、私を巡っていく…。\n\0":
'???',

# Gendo Ikari
"ここは…。\n\0":
'???',

# Kozo Fuyutsuki
"何もない…。\n世界は…無に返ったのか？\n\0":
'???',

# Ritsuko Akagi 
"私、死んだのかしら？\n何も、見えない…。\nどこなのかしら…。\n\0":
'Have I died?\n I can\'t see anything...\n I wonder where I am...\n\0',

# Hikari Horaki
"………………。▽\nえ、ええ…。\n\0":
'???',

# Makoto Hyuga
"静かだ…。\nいつからここにいるんだろう。\n真っ暗だ…。\n\0":
'???',

# Shigeru Aoba
"ここは…？\n何で、こんなところに？\n\0":
'???',

# Ryoji Kaji
"ここは…、\n俺は、死んだのか…？\n\0":
'???',

# Hikari Horaki
"ここは、何…？\n何も聞こえない、\nなぜ、何も見えないの？\n\0":
'???',

# Toji Suzuhara 
"何や、ここ…。\n何も、見えへんし…。\n\0":
'???',

# Kensuke Aida
"な、何だココ？\n暗いし、何もないし…。\n\0":
'???',

# Kaworu Nagisa 
"ここは…。\n…そうか、ここは。\n\0":
'???',

# [Text Only - No Designated Speaker]
"使徒は、乳濁色の光の霧へとその\n身体を変容させ、光の束となって\n白い巨人の仮面を刺した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"仮面から漏れる、血のような\n光を浴びて、使徒の光の束は\nヒトの姿を形作っていった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"仮面が粉々に砕け散った。\n赤い夕焼けのような光が\n一面に広がる。\n\0":
'???',

# Rei Ayanami 
"ほら、これがあなただったもの。▽\n全ての生命は、\nここへ過ぎてはやって来る…。\n\0":
'???',

# Rei Ayanami 
"使徒と呼ばれたものも、\nすべてここに。\nあなたと共に…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"人の姿と化した光、使徒とレイが\n巨人の顔の中に、あたかも迎え入れ\nられるように取り込まれていく…。▽\nすっかりレイと光を飲み込んだ白い\n巨人は、磔られていた十字架から、\nずるりと手を引き抜き、動き出した。▽\nそして、巨人の身体が女性の、レイの\nしなやかな身体へと変容する…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"幾多の光、波が通り過ぎていく。\nいや、自分自身が光であり、\n波であった。\n\0":
'???',

# Rei Ayanami 
"今は眠りなさい…。▽\nそして、いつの日かふたたび、\nこの惑星を、生命で覆うのよ。\n\0":
'???',

# Shinji Ikari
"あれ、どうしてここに…？\n\0":
'???',

# Shinji Ikari
"何で…、\nここにいるんだろう…？\n\0":
'???',

# Asuka Soryu Langley
"バカシンジ。\n何よ、ボーッとしちゃってさ。\n\0":
'???',

# Misato Katsuragi 
"シンちゃん。\n\0":
'Shin-chan.\n\0',

# Shinji Ikari
"アスカ…？\nミサトさん…？\n\0":
'Asuka...?\nMisato-san?\n\0',

# Gendo Ikari
"来ていたか、シンジ。\n\0":
'???',

# Shinji Ikari
"父さん…。\n\0":
'Father...\n\0',

# Yui Ikari,Yui Ikari [Flashback]
"シンジ…。\n\0":
'Shinji...\n\0',

# Shinji Ikari
"母さん…。\n\0":
'Mother...\n\0',

# Yui Ikari,Yui Ikari [Flashback]
"シンちゃん…、\n泣いてばかりね。\n\0":
'???',

# Asuka Soryu Langley
"私の部屋…？\n\0":
'My room...?\n\0',

# Asuka Soryu Langley
"あれ、でも私…。\n\0":
'???',

# Misato Katsuragi 
"どうしたのよ、アスカ。\n\0":
'???',

# Ritsuko Akagi 
"あら、アスカ。\n\0":
'Oh, Asuka.\n\0',

# Ryoji Kaji
"今日は元気ないな、\nどうした…？\n\0":
'???',

# Hikari Horaki
"アスカ…、どうかしたの？\n何かあったら話して…。\n\0":
'???',

# Toji Suzuhara 
"今日は、どないしたんや…。\n\0":
'???',

# Kensuke Aida
"アスカがそんな顔するのって\n珍しいね。\n\0":
'???',

# Shinji Ikari
"今、何か言ってなかった…？\n\0":
'???',

# Rei Ayanami 
"何か言いたそう…。\n…違うの？\n\0":
'???',

# Asuka Soryu Langley,Toji's Sister, Maya Ibuki, Shinji Ikari
"……………………………。\n\0":
'???',

# Rei Ayanami 
"ここは、Σ機関の中。\n巡り巡る力の生まれるところ。▽\nかつて、あなただったものが\n他のものと交差するところ。\n\0":
'???',

# Rei Ayanami 
"駄目…、来ては駄目。▽\nそう、許してあげる…。▽\n還るの。▽\n還りなさい…。\n\0":
'???',

# Maya Ibuki 
"真っ暗…。\n何もない…。▽\nここは、どこかしら…。\n\0":
'???',

# Misato Katsuragi 
"…？▽\n私の部屋？▽\nペンペン…？\n\0":
'???',

# Misato Katsuragi 
"何…、待って、\nここは…！？\n\0":
'???',

# Misato Katsuragi 
"私…は、…ここは？\n\0":
'???',

# Gendo Ikari
"ユイ！？▽\nいや、あれは…、かつての…。\n\0":
'???',

# Gendo Ikari
"ここは…、レイの…。▽\nレイ、…レイ！！\n\0":
'???',

# Gendo Ikari
"シンジ…？\n\0":
'???',

# Kozo Fuyutsuki
"…！！！！▽\nここは…、さっきまで私は…？\n\0":
'???',

# Kozo Fuyutsuki
"これは、\nどうしたんだ…！？\n\0":
'???',

# Rei Ayanami 
"相田君…。\nかえりましょう。\n\0":
'Aida-kun...\n Let\'s go home.\n\0',

# Yui Ikari
"…冬月先生。\n\0":
'...Fuyutsuki-sensei.\n\0',

# Kozo Fuyutsuki
"…ユイ君！？\n君か、君なのか！？\n\0":
'???',

# Kozo Fuyutsuki
"…は、\n何が、何が一体…。\n\0":
'???',

# Kensuke Aida
"……………。▽\nあ、ああ…。\n\0":
'...... ▽\n R-right...\n\0',

# Ritsuko Akagi 
"………？▽\nここ…、さっきまで私は…？\n\0":
'???',

# Naoko Akagi [for her one line from the PS2 version],Naoko Akagi
"どこ行くの？\n\0":
'???',

# Ritsuko Akagi, Ritsuko Akagi [Flashback]
"散歩よ。\n母さんこそ、どこに行くの？\n\0":
'???',

# Ritsuko Akagi 
"はっ！？\nな、何、どうしたのよ！！\n何が起こってるの…？\n\0":
'???',

# Maya Ibuki 
"どこに行くんですか？\n\0":
'???',

# Makoto Hyuga
"どこ行かれるんです？\n\0":
'???',

# Shigeru Aoba, Female Staff
"どこに行かれるんですか？\n\0":
'???',

# Ryoji Kaji
"どこに行くんだ？\n\0":
'???',

# Misato Katsuragi 
"どこ行くの…？\n\0":
'???',

# Ritsuko Akagi, Asuka Soryu Langley, Toji Suzuhara, Kaworu Nagisa, Shinji Ikari
"…あ。\n\0":
'???',

# Maya Ibuki 
"…あれ、何でこんなところに？\n\0":
'???',

# Maya Ibuki 
"…えっ？\nそ、そんなはず…。\n\0":
'???',

# Ritsuko Akagi 
"期待してるわよ、\nあなたの卒業論文を見て\n採用させてもらったの。\n\0":
'???',

# Maya Ibuki 
"ハイ、頑張ります！！\n\0":
'???',

# Maya Ibuki 
"センパイ…って、\n呼んでもいいですか？\n\0":
'???',

# Maya Ibuki 
"あれは、私だわ…。\nココに入ったばかりの私…。▽\n夢？\n何が、何が起こってるの…？\n\0":
'???',

# Rei Ayanami 
"かえりましょう…。\n\0":
'???',

# Makoto Hyuga
"な…！？\n何でここに…？▽\n発令所にいたはずなのに！？\n\0":
'???',

# Makoto Hyuga
"えっ、ここは…？\n\0":
'???',

# Misato Katsuragi 
"送ってくれてありがとう。\n\0":
'???',

# Makoto Hyuga
"いえ、構いませんよ。\n\0":
'???',

# Makoto Hyuga
"な、なんだ…？\nあれは、僕…？\n\0":
'???',

# Misato Katsuragi 
"上がってかない？\nお茶くらいだすわ。\n\0":
'???',

# Makoto Hyuga
"えっ…、ああ、\nでも今日は戻ります。\n\0":
'???',

# Misato Katsuragi 
"…そう。\n\0":
'???',

# Makoto Hyuga
"あの時、なぜ誘いを断ったんだろう。\nあんな切ない目を…。\nでも、誘われるままだったら、▽\nミサトさんが見ているのは\n僕じゃないと思い知らされて\nいたかもしれない…。▽\nそれが怖かった…。\n\0":
'???',

# Makoto Hyuga
"………？▽\n何だったんだ、今のは…？\n\0":
'???',

# Shigeru Aoba
"ここは！？\n\0":
'???',

# Shigeru Aoba [Flashback],Shigeru Aoba
"やっぱ駄目だわ。\n俺、才能ないって言われた。\n\0":
'???',

# Teruo Kato
"マジで、音楽やめんのかよ…。\n\0":
'???',

# Shigeru Aoba
"あれ、俺だ…。\n学生時代の…、\n俺と…、テルオ…？\n\0":
'???',

# Shigeru Aoba [Flashback],Shigeru Aoba
"デビューしていい曲かけよ。\n応援するからさ。\n\0":
'???',

# Teruo Kato
"俺がもう一度、事務所に話すから、\n一緒にやろうぜ。\nなあ、シゲル…。\n\0":
'???',

# Shigeru Aoba
"そうだ、あの時…、\nもう一度、音楽をやりたいと\n思った…。▽\n…でも。\n\0":
'???',

# Shigeru Aoba
"うっ…！？\nここは、発令所…？\n\0":
'???',

# Asuka Soryu Langley
"ここ、どこなんだろう…。\n\0":
'???',

#
# ./USRDIR/event/cev0702.har_EXTRACT/cev0702.evs
#
# Shinji Ikari, Makoto Hyuga, Rei Ayanami, Maya Ibuki, Ritsuko Akagi, Shigeru Aoba, Female Staff
"…はい。\n\0":
'???',

# Ritsuko Akagi 
"シンジ君。\nあなたに急ぎの用事があるの。▽\nいいかしら、\nちょっと来てもらっても…。\n\0":
'???',

# Shinji Ikari
"あの…、用って何ですか？\n\0":
'???',

# Ritsuko Akagi 
"フフフ…、あなたのお父さんが\n何をやっているか、知ってる？\n\0":
'???',

# Shinji Ikari
"え、ええ…。\n\0":
'???',

# Ritsuko Akagi 
"違うわ。\n碇司令はね、あなたの知らない\nもっと別の顔を持ってるのよ。▽\n知りたいでしょう？\n今から、あなたに教えてあげるわ。\n車に乗って…。\n\0":
'???',

# Shinji Ikari,Shigeru Aoba
"あの…。\n\0":
'???',

# Ritsuko Akagi 
"あなたも大人になったら、\n碇司令のようになるのかしら。\n\0":
'???',

# Shinji Ikari
"な、何の話ですか…！？\nちょ、ちょっと！！\n\0":
'???',

# Ritsuko Akagi 
"私があの人の一番になれないのなら、\nあなたの一番になってあげる。\n\0":
'???',

# Shinji Ikari
"えっ、えっ…！？\nリ、リツコさぁん！！\n\0":
'???',

#
# ./USRDIR/event/bb003.har_EXTRACT/bb003.evs
#
# Kozo Fuyutsuki
"出撃パイロットを選択した次は、\nエヴァの迎撃ポイントと\n装備の設定だ。▽\n%1iボタンで作戦立案に関する\nコマンドを起動できる。\n試してみたまえ。\n\0":
'???',

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
'Unit-01 has reactivated!!▽\n This is impossible...\n The synch ratio is exceeding 400 percent!\n\0 ',

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
# ./USRDIR/event/n014.har_EXTRACT/n014.evs
#
# Misato Katsuragi, Female Staff
"バルディエル\n\0":
'Bardiel\n\0',

# Misato Katsuragi, Female Staff
"目標はエヴァ参号機の機体に潜み、\n起動実験中にその存在が確認されました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"フォース・チルドレン、鈴原トウジ搭乗のまま、\n参号機を使徒と識別、戦闘を開始。\n\0":
'???',

# Misato Katsuragi, Female Staff
"参戦したのは\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標は、エヴァを操り、\n圧倒的な強さで、その威力を\n見せつけましたが\n\0":
'???',

# Misato Katsuragi, Female Staff
"かろうじて、使徒殲滅に成功しました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"しかし、参号機に搭乗していた\nパイロット、鈴原トウジは死亡\n選出されたばかりの貴重なパイロットを失う、\n苦い結果となりました。\n\0":
'???',

# Misato Katsuragi 
"活動停止…！？\nパイロットからの応答は？\n\0":
'???',

# Female Staff
"パイロットからの応答が\nありません！！\n\0":
'???',

# Shigeru Aoba, Male Staff
"駄目です、\nエヴァ活動停止！！▽\nパイロットからの反応も\nありません。\n\0":
'???',

# Misato Katsuragi, Female Staff
"それじゃ…、\nパイロットは…。\n\0":
'???',

# Makoto Hyuga, Male Staff
"目標は、ここを目指しています！\n依然、侵攻中！\n\0":
'???',

# Misato Katsuragi 
"ここは危険だわ。\n総員撤退！！\n\0":
'???',

# Kozo Fuyutsuki
"総員撤退しろ！\n撤退だ！！\n\0":
'???',

# Female Staff
"総員、撤退して下さい。\n繰り返します、\n総員、撤退して下さい！！\n\0":
'???',

# Makoto Hyuga
"わぁっ、駄目です！！\nま、間にあいません。\n\0":
'???',

# Male Staff
"だ、駄目です…。\n間に合いません…！！\nここまで、すぐ来ます！\n\0":
'???',

# Misato Katsuragi 
"早く、みんな逃げなさい！！\n\0":
'Hurry, everyone get away!!\n\0',

# Kozo Fuyutsuki
"とうとうここまで侵入して\n来たか…。\n\0":
'???',

# Shigeru Aoba
"来た…、\nあの音、間違いない…、奴だ。\n\0":
'???',

# Female Staff
"そんな、ここまで力を\n尽したというのに…。\n\0":
'???',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba043.evs
#
# Shinji Ikari
"こちら初号機です。\n移動指定ポイントに到着しました。\n\0":
'???',

# Asuka Soryu Langley
"弐号機、\n移動指定ポイントに到着！\n\0":
'???',

# Rei Ayanami 
"こちら零号機、\n移動指定ポイントに到着しました。\n\0":
'???',

# Toji Suzuhara 
"こちら参号機、\n移動指定ポイントに着きました。\n\0":
'???',

# Kaworu Nagisa 
"四号機です、\n移動指定ポイントに到着しました。\n\0":
'???',

# Makoto Hyuga, Male Staff
"エヴァ両機、\n移動指定ポイントに到着しました。\n\0":
'???',

#
# ./USRDIR/event/cev0812.har_EXTRACT/cev0812.evs
#
# [Text Only - No Designated Speaker]
"ここしばらくのうちに\n知らない自分に、\nたくさん出会った様な気がする。▽\n自分はこういう事で笑うのだ、\n自分はこういう事で悲しむのだ。▽\n怒る自分、嬉しがる自分。\nどれも自分、伊吹マヤ。▽\nもっと早く気づいて\nあげればよかった。▽\n私は、寂しくて泣いている\n自分にしか気づけなかった。\n\0":
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

# Hikari Horaki,Shigeru Aoba
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
# ./USRDIR/event/cev1701.har_EXTRACT/cev1701.evs
#
# [Text Only - No Designated Speaker]
"この世界を選んだあなたは、\n絶望的な状況に愕然とするだろう。▽\nだが、あなたは、この困難を\n乗り越え、使徒の手から人類を\n守らなければならない。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le421.evs
#
# Toji Suzuhara 
"脱がへん。\nジャージより\n変えなアカンもん一杯あるしな…。\n\0":
'???',

# Toji's Shadow [Leliel]
"周りに期待しすぎちゃう？▽\nジャージ脱がへんと、\n誰も変わった事\n気が付かへんのんとちゃうやろか。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le105.evs
#
# Shinji Ikari
"悪いのは、僕だ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"内罰的だね。\nそうやって、\n他人との距離を広げていく。\n\0":
'???',

# Shinji Ikari
"何もしなければ、\nきっと誰も傷つかないよ。▽\n嫌われる原因を作らなければ\nいいんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"その代わり、何も始まらない。\n何も良くはならないよ。\n\0":
'???',

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
# ./USRDIR/event/levent.har_EXTRACT/le137.evs
#
# Shinji Ikari
"君は僕自身なんだろう？\nどうして思ってもない事を言うのさ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"僕が言うのは、\nいつも君が思っている事。▽\n君は、僕を、自分自身を\n信頼出来ないから、\nあえて欠如させたんだ。\n\0":
'???',

#
# ./USRDIR/event/cev0108.har_EXTRACT/cev0108.evs
#
# [Text Only - No Designated Speaker]
"食堂が焦げ臭い。\n\0":
'???',

# Maya Ibuki 
"あーぁ。\nまた失敗しちゃった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"厨房にマヤの姿が見える。\n\0":
'???',

# Shinji Ikari
"マヤさん。\n何をしてるんですか？\n\0":
'???',

# Maya Ibuki 
"シンジ君…。\nあのね…、\nちょっと…、料理作ってて。\n\0":
'???',

# [Text Only - No Designated Speaker]
"焦げた匂いは、\nオーブンの中からのようだ。\n目を突く様な煙が立ち昇っている。▽\nオーブンの中で炭化したそれは、\nスポンジケーキ…の様だった。\n\0":
'???',

# Maya Ibuki 
"ケーキでも焼いてみようかなと\n思って…。▽\n家にオーブンがないから、\nここを借りて作ってたんだけど。▽\n…失敗しちゃったの。\nこれで４回目。\n\0":
'???',

# [Text Only - No Designated Speaker]
"じわっとマヤさんの目に\n涙が浮かんだ。\n\0":
'???',

# Maya Ibuki 
"私、お裁縫とか、料理とか\nあんまり得意じゃないの。\n\0":
'???',

# [Text Only - No Designated Speaker]
"炭になったスポンジケーキを横目に、\nマヤさんは溜息をついた。▽\nこうやって、\nわざわざ作ろうとしているのは、\n何か訳があるのかもしれない。\n\0":
'???',

# Shinji Ikari
"僕、手伝いますよ。\nえーと、家庭科で習ったから\nわかります。\n\0":
'???',

# Maya Ibuki 
"え…、そんな…、\nいいわよぉ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"マヤさんは、口をすぼめて\n困った様な顔をした。\n何だか子供みたいだ。\n\0":
'???',

# Shinji Ikari
"まず、卵白から泡立てましょう。\n\0":
'???',

# Shinji Ikari
"僕は、粉をふるいにかけますね。\n…って、あぁ！？\n\0":
'???',

# Shinji Ikari
"マヤさん、まだ卵黄も砂糖も\n入れちゃダメですよ。\n\0":
'???',

# Maya Ibuki 
"え、でも…。\n泡立ったし…。\n\0":
'???',

# Shinji Ikari
"まだ表面だけじゃないですか。\n全部、生クリームみたいに\n角が立つまでやるんですよ？\n\0":
'???',

# Maya Ibuki 
"へぇ…、泡立てるって、\nそういう事なんだ。\n\0":
'???',

# Shinji Ikari
"じゃあ、交代しましょう。\n粉をふるってください。\n\0":
'???',

# Maya Ibuki 
"ねえ、どうして粉をふるうの？\n\0":
'???',

# Shinji Ikari
"こうしておかないと、\n泡立てた卵白の泡が\n潰れてしまうんですよ。\n\0":
'???',

# Maya Ibuki 
"へぇ…、メモしておかなきゃ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"仕事熱心なところは、\nどんな時も同じみたいだ。▽\n妙に感心されていて、\n何だか照れる。\n\0":
'???',

# Shinji Ikari
"卵白が泡立ってから、\n砂糖は二回に分けて。\nその後に卵黄を入れるんですよ。\n\0":
'???',

# Maya Ibuki 
"私が作るのと、\n生地のボリュームが違う。\n\0":
'???',

# Shinji Ikari
"ほとんど空気ですよ。\nでも、この卵白の空気が\n大事なんです。\n\0":
'???',

# Maya Ibuki 
"シンジ君、すごいわね…。\n私なんて、こういう女らしい事\n全然やってこなかった。▽\nいつも、勉強勉強。\nそればっかりだったから。\n\0":
'???',

# Shinji Ikari
"でも、僕はマヤさんみたいに\n勉強やってるわけじゃないから。\nおあいこですよ。\n\0":
'???',

# Maya Ibuki 
"ふふ、そうかな。\nじゃあ、今日のお礼に\n個人授業やってあげようか？\n\0":
'???',

# Shinji Ikari
"えーっと、そう…ですね。\nさ、予熱も済んだし\n後は生地を焼くだけです。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ケーキが焼ける、\n甘い匂いがしてきた。\n二人でオーブンを覗き込む。\n\0":
'???',

# Maya Ibuki 
"わぁ、ちゃんと膨らんでる。\n\0":
'???',

# Shinji Ikari
"…いい匂い。\n\0":
'???',

# Shigeru Aoba
"スッゲー、いい匂いすると\n思ったら…。▽\nおぉ、ケーキじゃん。\nマヤちゃんが作ったの？\n\0":
'???',

# Makoto Hyuga
"匂いの正体はこれかぁ…。\nケーキだね。\n\0":
'???',

# Misato Katsuragi 
"ヤダ、おいしそ〜。\n焼きたて？\n一口欲しいわぁ…。\n\0":
'???',

# Ritsuko Akagi 
"あら、マヤなの？\nこれ作ったのは。\n\0":
'???',

# Ryoji Kaji
"へぇ、マヤちゃんらしいね。\n手作りケーキか。\n\0":
'???',

# Maya Ibuki 
"あの、\nこれを作ったのは…。\n\0":
'???',

# Shinji Ikari
"マヤさんの作ったケーキ、\nおいしそうでしょう？\n\0":
'???',

# Maya Ibuki, Misato Katsuragi 
"シンジ君…。\n\0":
'???',

# Shigeru Aoba
"何？\nこれ、食わしてくれるの？\n\0":
'???',

# Maya Ibuki 
"えっと、うん…。\nみんなで食べましょう。\n\0":
'???',

# [Text Only - No Designated Speaker]
"困ったように笑いながら、\nマヤさんが耳打ちした。\n\0":
'???',

# Maya Ibuki 
"ゴメンね、シンジ君。\n\0":
'I\'m sorry, Shinji-kun.\n\0',

# Shinji Ikari
"いいですよ。\n\0":
'???',

# Maya Ibuki 
"ホントはこのケーキ…、\nシンジ君の為に作ろうと\n思ってたの。\n\0":
'???',

# Shinji Ikari
"そうなんですか？\n\0":
'???',

# [Text Only - No Designated Speaker]
"手伝おうとした時の、\nあの困った様な顔の理由。\nそうだったのか…。\n\0":
'???',

# Maya Ibuki 
"今度は一人で作ってみるね。\nシンジ君が教えてくれたように。\n\0":
'???',

# Maya Ibuki 
"だから、楽しみにしてて。\n\0":
'???',

# Shinji Ikari, Makoto Hyuga, Maya Ibuki 
"ハイ。\n\0":
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
# ./USRDIR/event/cev1418.har_EXTRACT/cev1418.evs
#
# Makoto Hyuga
"こいつはエヴァ参号機…。\nいえ、使徒のパターンを\n示しています！！\n\0":
'???',

# Gendo Ikari, Kozo Fuyutsuki
"エヴァ参号機は現時刻をもって破棄。\n目標を使徒と識別して対処する。\n迎撃地点にエヴァ全機緊急配置！\n\0":
'???',

# Misato Katsuragi, Ritsuko Akagi 
"フォース・チルドレン、\n到着しました。\nこれより起動実験を開始します。\n\0":
'???',

# Matsushiro Staff
"中枢神経に異常発生。\n\0":
'???',

# Ritsuko Akagi 
"実験中止、回路切断！！\n\0":
'???',

# Makoto Hyuga, Male Staff
"現場のスタッフは無事のようです！\n至急本部に帰還して下さい！\n\0":
'???',

# Matsushiro Staff
"駄目です、神経切断失敗！\n\0":
'???',

# Ritsuko Akagi, Misato Katsuragi, Female Staff
"緊急活動停止信号を発信！\nエントリープラグを強制射出！\n\0":
'???',

# Shigeru Aoba
"松代より入電！\nエヴァ参号機が暴走した模様。\n\0":
'???',

# Matsushiro Staff
"エントリープラグ挿入、\nメインロック解除。\n\0":
'???',

# Maya Ibuki 
"エヴァ参号機のパルス、\n確認出来ません！\n\0":
'???',

# Matsushiro Staff
"駄目です！\n停止信号及びプラグ排出コード\n認識されません！\n\0":
'???',

# Misato Katsuragi 
"何ですって！\n\0":
'???',

# Ritsuko Akagi 
"順調ね。\nこれなら、即、実戦も可能だわ。\n\0":
'???',

# Shigeru Aoba
"松代より巨大な物体が\nこちらに向かっています！\n\0":
'???',

#
# ./USRDIR/event/n000.har_EXTRACT/n000.evs
#
# Misato Katsuragi, Female Staff
"第$d使徒\n\0":
'???',

# Misato Katsuragi, Female Staff
"サキエル\n\0":
'???',

# Misato Katsuragi, Female Staff
"同市街地にて使徒と交戦を開始。\n\0":
'???',

# Misato Katsuragi, Female Staff
"国連軍、これにΝ地雷を使用。\n\0":
'???',

# Misato Katsuragi 
"しかし、わずかな損傷を\n与えるのみに終わる\n\0":
'???',

# Female Staff
"しかし、わずかに損傷を\n与えるのみとなった\n\0":
'???',

# Misato Katsuragi, Female Staff
"この時、使徒の自己修復機能\n及び機能増幅を確認。\n\0":
'???',

# Misato Katsuragi, Female Staff
"同時刻、エヴァンゲリオン起動。\n参戦したのは…\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le201.evs
#
# Asuka Soryu Langley
"私は、一人で生きるの。\nずっとそう決めてきたの。\nそんな弱音は吐かないわ。\n\0":
'???',

# Asuka's Shadow [Leliel]
"でも、誰かを思わずには\nいられない。▽\nママにしか呼びかけられない事を、\n寂しく思ってるんでしょう。\n\0":
'???',

#
# ./USRDIR/event/tev1902.har_EXTRACT/tev1902.evs
#
# Misato Katsuragi 
"出来そこないの群体として既に行き\n詰まった人類を完全な単体としての\n生物へと人工進化させる補完計画。▽\nまさに理想の世界ね。\nその為にまだ、\n委員会は使うつもりなんだわ。▽\nアダムやネルフではなく、\nあのエヴァを。\n加持君の予想通りにね。\n\0":
'???',

#
# ./USRDIR/event/tev0202.har_EXTRACT/tev0202.evs
#
# Misato Katsuragi 
"ここが、私達の秘密基地、\nネルフ本部。\n世界再建の要となるところよ。▽\nさて、まずは…\n私の仕事部屋へ行きましょうか。\n\0":
'???',

#
# ./USRDIR/event/bs999.har_EXTRACT/bs999.evs
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
'But that\'s--!?\nUnit-01 has reactivated!!▽\n Unit-01\'s synch ratio is ascending radically!\n\0',

# Female Staff
"これは…！？\nエヴァ初号機、再起動！！▽\n初号機のシンクロ率が、\n急激に上昇していきます！\n\0":
'This is--?!\nUnit-01 has reactivated!!▽\n Unit-01\'s synch ratio is ascending radically!\n\0',

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
'... It\'s berserk?!\n\0',

# Male Staff
"まさか…、暴走！？\n\0":
'It can\'t be... berserk?!\n\0',

# Maya Ibuki, Female Staff
"初号機、暴走！！\nパイロットからのコントロールも\n不可能です！\n\0":
'Unit-01 is berserk!!\n It can\'t be controlled by the pilot either!\n\0',

# Shigeru Aoba, Male Staff
"目標、ゼロエリアを突破！\nジオフロントに向かっています！\n\0":
'Target has breached Area Zero!\nIt\’s heading for the GeoFront!\n\-',

# Misato Katsuragi 
"エヴァは、リニアレールから\nジオフロントまで撤退！\n迎撃態勢を取って！\n\0":
'Withdraw the Evas into the\nGeoFront by linear rail!\nPrepare to intercept!\n\0',

# Kozo Fuyutsuki
"エヴァは、リニアレールから\nジオフロントまで撤退！\n迎撃態勢を取れ！\n\0":
'Withdraw the Evas into the\nGeoFront by linear rail!\nPrepare to intercept!\n\0',

# Female Staff
"エヴァは、リニアレールから\nジオフロントまで撤退、\n急いで迎撃にまわってください！\n\0":
'Please withdraw the Evas into the\nGeoFront by linear rail,\nand quickly turn to intercept!\n\0',

# Shigeru Aoba, Male Staff
"目標、ネルフ本部に侵入。\nすぐに、ここまで来ます！\n\0":
'The target has penetrated Nerv H.Q.\n It\'ll be here any second!\n\0',

# Misato Katsuragi, Kozo Fuyutsuki
"総員、本部から撤退！！\n\0":
'???',

# Female Staff
"総員、本部より撤退して下さい！！\n\0":
'???',

# Makoto Hyuga
"き、来ました…。\nうわぁぁぁぁあー！！\n\0":
'???',

# Shigeru Aoba
"あぁっ、き、来たぁぁ！\nわああああああああー！！\n\0":
'???',

# Maya Ibuki 
"っ！　来ました…。\nあああぁぁ！！\n\0":
'???',

# Male Staff
"わぁっ！！\nき、来ました…。\nうわぁぁぁぁぁあ！！\n\0":
'???',

# Misato Katsuragi 
"任せたわよ、シンジ君！\n\0":
'???',

# Misato Katsuragi 
"シンジ君、慎重にね！！\n\0":
'???',

# Misato Katsuragi 
"ＯＫ、\n相手の出方にも気をつけるのよ！！\n\0":
'???',

# Misato Katsuragi 
"シンジ君、戦闘態勢をとって。\n\0":
'???',

# Kozo Fuyutsuki
"初号機に任せたぞ！\n\0":
'???',

# Female Staff
"了解しました。\n注意して戦闘体制に入って下さい。\n\0":
'???',

# Asuka Soryu Langley
"こちら、弐号機。\n目標を肉眼で発見しました！\n\0":
'???',

# Misato Katsuragi 
"アスカ、任せたわよ。\n\0":
'???',

# Misato Katsuragi 
"アスカ、ハメはずしすぎちゃ駄目よ。\n慎重にね。\n\0":
'???',

# Misato Katsuragi 
"アスカ、\n今回の作戦、わかってるわね。\nそれじゃ、任せたわよ！\n\0":
'???',

# Misato Katsuragi 
"ＯＫ、アスカ。\n戦闘態勢に入って。\n\0":
'???',

# Kozo Fuyutsuki
"弐号機に任せたぞ！\n\0":
'???',

# Rei Ayanami 
"こちら、零号機。\n目標を肉眼で捕捉しました！\n\0":
'???',

# Misato Katsuragi 
"レイ、任せたわよ。\n\0":
'???',

# Misato Katsuragi 
"レイ、後はあなたの判断に任せるわ。\n\0":
'???',

# Misato Katsuragi 
"どう、行けそうかしら？\n後は作戦通りに行動して。\n\0":
'???',

# Misato Katsuragi 
"ＯＫ、レイ。\nタイミングを見計らって攻撃して！\n\0":
'???',

# Kozo Fuyutsuki
"任せたぞ。レイ。\n\0":
'???',

# Toji Suzuhara 
"こちら、参号機。\n目標を肉眼で発見しました！\n\0":
'???',

# Misato Katsuragi 
"トウジ君、任せたわよ。\n\0":
'???',

# Misato Katsuragi 
"トウジ君、いい？\n無茶は禁物だからね！\n\0":
'???',

# Misato Katsuragi 
"ここからが本番よ、トウジ君。\n迎撃態勢に入って！！\n\0":
'???',

# Misato Katsuragi 
"いいわね、トウジ君。\nむやみに突き進んでは駄目、\n相手の動きをよく見るのよ！\n\0":
'???',

# Kozo Fuyutsuki
"参号機に任せたぞ！\n\0":
'???',

# Kaworu Nagisa 
"こちら、四号機。\n目標を肉眼で確認しました！\n\0":
'???',

# Misato Katsuragi 
"カヲル君、任せたわよ。\n\0":
'???',

# Misato Katsuragi 
"了解、カヲル君。\n使徒からの攻撃が来るタイミングに\n注意して。\n\0":
'???',

# Misato Katsuragi 
"カヲル君、慎重に。\n後はあなたの腕を信じるわ。\n\0":
'???',

# Misato Katsuragi 
"いいわよ、カヲル君。\n迎撃準備は出来ているでしょうね？\n\0":
'???',

# Kozo Fuyutsuki
"四号機に任せたぞ！\n\0":
'???',

# Shinji Ikari
"…こ、こちら初号機。\nエヴァ三号機を肉眼で確認しました。▽\nまさか、敵の使徒って…。\nあの、三号機…！？\n\0":
'???',

# Asuka Soryu Langley
"来たわ…。▽\nこちら、弐号機。\n肉眼で目標を確認。▽\nチッ、プラグが排出されてない\nみたいね…。\n\0":
'???',

# Rei Ayanami 
"こちら、零号機。\n目標を肉眼で確認…。\n\0":
'???',

# Kaworu Nagisa 
"こちら、四号機…。\n目標である使徒を肉眼で確認…。\n\0":
'???',

# Kozo Fuyutsuki
"…勝ったな。\n\0":
'???',

# Gendo Ikari
"そろそろだな…。\n\0":
'???',

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
"動かへん…。\nああ、何でや…。\n何で動かへんのや…。\n\0":
'???',

# Kaworu Nagisa 
"そんな、動かない…。\n僕に動かせないなんて…。\nなぜだ…！！\n\0":
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

# Maya Ibuki, Female Staff
"エヴァ初号機の予備電源終了。\n活動限界です。\n\0":
'???',

# Shinji Ikari
"そんな、もう…？\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ弐号機の予備電源終了。\n活動限界です。\n\0":
'???',

# Asuka Soryu Langley
"チッ、あと少しあれば…。\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ零号機の予備電源終了。\n活動限界です。\n\0":
'???',

# Rei Ayanami 
"ここまでなの…。\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ参号機の予備電源終了。\n活動限界です。\n\0":
'???',

# Toji Suzuhara 
"…んのォ、\nちっくしょおぉ！！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ四号機の予備電源終了。\n活動限界です。\n\0":
'???',

# Kaworu Nagisa 
"しまった…！！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ両機の予備電源終了。\n活動限界です。\n\0":
'???',

# Shinji Ikari, Toji Suzuhara
"うわぁぁぁぁっ！\n\0":
'???',

# Asuka Soryu Langley
"やっぱりアンタってバカよ！\n私がカタキをとってやるから、\nありがたく思いなさいよ！！\n\0":
'???',

# Rei Ayanami 
"碇君…。\nあれは、私が倒すわ…。\n\0":
'???',

# Toji Suzuhara 
"シンジ、\nあとはワシにまかしとき！\nお前は傷を治すんや！！\n\0":
'???',

# Kaworu Nagisa 
"よくも、シンジ君を！\n僕を本気にさせたね…。\n\0":
'???',

# Asuka Soryu Langley
"キャァァァァァァ！！\n\0":
'???',

# Shinji Ikari
"アスカッ！！\n大丈夫なの！？\n返事してよ、アスカッ！！\n\0":
'???',

# Rei Ayanami 
"…後は任せて。\n\0":
'???',

# Toji Suzuhara 
"惣流！！\nアホが、無茶しよってからに。\n待っとれ、カタキとったるわ！\n\0":
'???',

# Kaworu Nagisa 
"アスカ！！\nすまない、守ってやれなくて…。\n\0":
'???',

# Rei Ayanami 
"っくぅぅぅぅぅ！\n\0":
'???',

# Shinji Ikari
"………綾波！？\nそこは危険だ、早く！！\n誰か、綾波を助けてよ！！\n\0":
'???',

# Asuka Soryu Langley
"バカッ、\nアンタがやられる事ないのにッ！！\n\0":
'???',

# Toji Suzuhara 
"綾波、…くっそぉっ！！\n見とれよ、アイツにはワシが\n千倍にして返したらぁ！！\n\0":
'???',

# Kaworu Nagisa 
"ファースト！！\n無事でいてくれ、無事で…！！\n\0":
'???',

# Shinji Ikari
"トウジ！？\n大丈夫なの、トウジ！？\nねぇ、トウジッ！！\n\0":
'???',

# Asuka Soryu Langley
"バカ鈴原！\n私が戻るまで、死ぬんじゃないわよ、\nいいわねっ！！\n\0":
'???',

# Rei Ayanami 
"鈴原君、死んでは駄目！\n無事でいて…！！\n死なないで、死なないで…。\n\0":
'???',

# Kaworu Nagisa 
"トウジ君、\n僕が守るべきだった…。\nすまない…。\n\0":
'???',

# Kaworu Nagisa 
"…うっ、…ぐ…ごほっ。\n\0":
'???',

# Shinji Ikari
"カヲル君！？\n死んじゃ駄目だ、カヲル君！！\n逃げて！誰かカヲル君を助けてよ！\n\0":
'???',

# Asuka Soryu Langley
"回収班、手当てを急ぎなさいよ！\nあいつを死なせたら、あんたら\n踏み潰すから！！\n\0":
'???',

# Rei Ayanami 
"私が、あなたのカタキを取るわ…。\n\0":
'???',

# Toji Suzuhara 
"カヲルッ！！\nこれが済んだらすぐ行くわ！\n待っとれよ！！\n\0":
'???',

# Makoto Hyuga, Male Staff
"ΑΤフィールドとシンクロ率、\n共に上昇！\n\0":
'???',

# Shinji Ikari
"…来る。\n落ち着け、落ち着いてやれば…。\n\0":
'???',

# Shinji Ikari
"よし、行こう！\n\0":
'???',

# Shinji Ikari
"大丈夫…、\nやれる、うまくやれる…。\n\0":
'???',

# Shigeru Aoba, Male Staff
"目標はエヴァ弐号機の\n迎撃開始ラインを通過しました！\n\0":
'???',

# Asuka Soryu Langley
"来たわね、私の出番よッ！！\n\0":
'???',

# Asuka Soryu Langley
"来なさい、\n私がキメてあげるから！！\n\0":
'???',

# Asuka Soryu Langley
"おあいにくさま。\nアンタは私に倒されるのよッ！\n\0":
'???',

# Shigeru Aoba, Male Staff
"目標はエヴァ零号機の\n迎撃開始ラインを通過しました！\n\0":
'???',

# Rei Ayanami 
"了解。\n零号機、迎撃に向かいます。\n\0":
'???',

# Shigeru Aoba, Male Staff
"目標はエヴァ参号機の\n迎撃開始ラインを通過しました！\n\0":
'???',

# Toji Suzuhara 
"よっしゃぁ、ワシの出番やな！\n\0":
'???',

# Toji Suzuhara 
"ほな、\nいっちょパチキかましたらぁ！！\n\0":
'???',

# Toji Suzuhara 
"けっ、あんなやつ…。\nボコボコにしばいたんねん！！\n\0":
'???',

# Shigeru Aoba, Male Staff
"目標はエヴァ四号機の\n迎撃開始ラインを通過しました！\n\0":
'???',

# Kaworu Nagisa 
"僕の出番だね。\n\0":
'???',

# Kaworu Nagisa 
"君にみんなの未来は渡さない…。\n\0":
'???',

# Kaworu Nagisa 
"僕はリリンの生き様を見続けたい。\nだから倒す…、君を。\n\0":
'???',

# Shigeru Aoba, Male Staff
"目標はエヴァ両機の\n迎撃開始ラインを通過しました！\n\0":
'???',

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

# Shinji Ikari
"ダメだ！\nやっぱりダメだよ、戦えないよ！\n\0":
'???',

# Gendo Ikari
"シンジ、なぜ戦わない？\n\0":
'???',

# Shinji Ikari
"だって…、\n人、人が乗ってるんだよ！\n父さん！\n\0":
'???',

# Shinji Ikari
"だって、トウジが、\nトウジが乗ってるんだよ！\n父さん！\n\0":
'???',

# Gendo Ikari
"構わん。\nそいつは使徒だ。\n我々の敵だ。\n\0":
'???',

# Shinji Ikari
"でも、でも、出来ないよ。\n助けなきゃ！\n人殺しなんて出来ないよ！\n\0":
'???',

# Shinji Ikari
"トウジは、友達なんだ。\n僕の友達なんだ。\n戦えるわけないじゃないか！！\n\0":
'???',

# Gendo Ikari
"お前が死ぬぞ。\n\0":
'???',

# Shinji Ikari
"いいよ。\n人を殺すよりはいいっ！！\n\0":
'???',

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
'???',

# Maya Ibuki, Female Staff
"管制システム、切り替え終了。\n全神経、ダミーシステムへ直結完了。▽\n感情素子の３２．８パーセントが\n不鮮明。\nモニター出来ません。\n\0":
'???',

# Gendo Ikari
"構わん、システム開放。\n攻撃開始。\n\0":
'???',

# Shigeru Aoba, Male Staff
"エヴァ参号機…いえ、\n目標は完全に沈黙しました。\n\0":
'???',

# Makoto Hyuga
"エントリープラグの解体班より連絡。\n生存者を確認！\n\0":
'???',

# Male Staff
"参号機パイロットは…、\n生存確認！\n生きてます！\n\0":
'???',

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

# Shinji Ikari, Misato Katsuragi 
"カヲル君！！\n\0":
'???',

# Shinji Ikari
"待って、カヲル君！\n\0":
'Wait, Kaworu-kun!\n\0',

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

# Makoto Hyuga, Male Staff
"目標、再度、\n元の１体に戻ろうとしています！\n\0":
'???',

# Makoto Hyuga
"目標２体、融合！\n\0":
'Both targets have fused!\n\0',

# Male Staff
"目標、１体に戻りました！\n\0":
'The targets have gone back to a single body!\n\0',

# Shinji Ikari
"今だ、行くよ！\n\0":
'???',

# Asuka Soryu Langley
"チャンスよ！！\n\0":
'???',

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

# Rei Ayanami 
"行きましょう！！\n\0":
'Let\'s go!!\n\0',

# Toji Suzuhara 
"よっしゃあ！！\nキツイの一発お見舞いしたらぁ！！\n\0":
'???',

# Kaworu Nagisa 
"今だ、奴にとどめを！！\n\0":
'???',

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
'???',

# Female Staff
"参号機パイロットは？\n\0":
'???',

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

# Kozo Fuyutsuki,Shigeru Aoba
"万策尽きたか…。\n\0":
'???',

# Makoto Hyuga, Male Staff
"第$d使徒、$e。\n殲滅を確認しました！\n\0":
'???',

# Makoto Hyuga, Male Staff
"エヴァシリーズ、１機撃破！\n\0":
'???',

# Makoto Hyuga, Male Staff
"２機目撃破！\n\0":
'???',

# Makoto Hyuga, Male Staff
"３機目撃破！\n\0":
'???',

# Makoto Hyuga, Male Staff
"４機目撃破！\n\0":
'???',

# Makoto Hyuga, Male Staff
"５機目撃破！\n\0":
'???',

# Shigeru Aoba
"気味の悪い奴等だ。\nまた活動を再開してきたら、\nどうする…。\n\0":
'???',

# Male Staff
"まさか、\nまた活動を再開したら…。\n\0":
'???',

# Makoto Hyuga, Male Staff
"６機目撃破！\n\0":
'???',

# Makoto Hyuga, Male Staff
"７機目撃破！\n\0":
'???',

# Makoto Hyuga, Male Staff
"８機目撃破！\nあと１機！\n\0":
'???',

# Makoto Hyuga, Male Staff
"エヴァ初号機、沈黙しました。\n\0":
'???',

# Misato Katsuragi, Kozo Fuyutsuki, Gendo Ikari, Maya Ibuki, Female Staff, Toji Suzuhara, Ritsuko Akagi, Makoto Hyuga, Shigeru Aoba, Shinji Ikari,[Text Only - No Designated Speaker], Asuka Soryu Langley, Kaworu Nagisa
"………………………。\n\0":
'???',

# Shinji Ikari
"…カヲル…君。\n\0":
'???',

# Shinji Ikari
"…で、でも。\nどうすればいいんですか？\n\0":
'???',

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

# Shinji Ikari, Misato Katsuragi 
"はい！\n\0":
'???',

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

# Maya Ibuki 
"エヴァ初号機。\nアンビリカルケーブル、\n残りわずかです。\n\0":
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

# Shinji Ikari
"…あ、当たった！\n\0":
'???',

# Misato Katsuragi 
"スゴイわ、シンジ君。\nその調子！\n\0":
'???',

# Shinji Ikari
"いっ、痛い…！？\n…くっ、うわぁぁぁぁ！！\nああああぁぁぁぁぁぁぁぁぁ！！\n\0":
'???',

# Misato Katsuragi 
"シンジ君、それは幻痛よ！！\n初号機の耐久力はまだあるわ、\n落ち着いて！\n\0":
'???',

# Shinji Ikari
"………………………………。▽\n射程に入れて、%1iボタン…。\n射程に入れて、%1iボタン…。\n射程に入れて、%1iボタン…。\n\0":
'???',

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
"シンジ君、\nアンビリカルケーブルの役割は\nちゃんと覚えてる？\n\0":
'???',

# Shinji Ikari
"えっと、エヴァを動かす電源の\n供給ケーブル。▽\nケーブルの長さは有限で、\nその範囲外に移動するには\n他の電源ビルへの繋ぎ変えが必要。▽\n…でした…よね？\n\0":
'???',

# Misato Katsuragi 
"じゃ、引き続き移動指示を行うわよ。\n\0":
'???',

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

# Shinji Ikari
"あ…、当たった…！\n\0":
'???',

# Misato Katsuragi 
"上手いじゃない、シンジ君。\n\0":
'???',

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

# Misato Katsuragi 
"いいわ。その調子よ。\n\0":
'???',

# Shinji Ikari
"はい、わかりました。\n\0":
'???',

# Misato Katsuragi 
"あっちゃあ〜、\nやっぱ難しかったかしら…。\n\0":
'???',

# Shinji Ikari
"すみません…。\n\0":
'???',

# Misato Katsuragi 
"じゃ、気を取り直して\n復習ついでに、もう一回最初から\nやってみましょうか。\n\0":
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

# Shigeru Aoba
"使徒、ゼロエリアを突破しました！\n\0":
'???',

# Shinji Ikari
"しまった！\n\0":
'???',

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
'???',

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
'???',

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

# Maya Ibuki 
"でも、それで子供が\n犠牲になるなんて、\n許される事ではありません！！\n\0":
'???',

# Makoto Hyuga
"馬鹿な事を！！\n他にあるはずだ、助かる方法が。\n\0":
'???',

# Male Staff
"そんな、このまま\n子供を殺すわけにはいかない！！\n\0":
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
'???',

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

# Gendo Ikari
"レイ、ドグマを降りて槍を使え。\n\0":
'Rei, go down to Dogma and use the Spear.\n\0',

# Kozo Fuyutsuki
"碇、ロンギヌスの槍か？\n確かに使徒は仕留められるかも\nしれん。▽\nだが、ゼーレの許可なしに\n使うのはめんどうだぞ！\nそれでも使うのか？\n\0":
'???',

# Male Staff
"司令、委員会の許可なしに\n槍を使う事は出来ません。▽\nそれに、アダムとエヴァの接触は\nサードインパクトを引き起こす\n可能性があります。\n\0":
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

# Gendo Ikari
"初号機は\nダミープラグに切り替えろ。\n\0":
'???',

# Gendo Ikari
"弐号機は\nダミープラグに切り替えろ。\n\0":
'???',

# Gendo Ikari
"零号機は\nダミープラグに切り替えろ。\n\0":
'???',

# Gendo Ikari
"参号機は\nダミープラグに切り替えろ。\n\0":
'???',

# Gendo Ikari
"四号機は\nダミープラグに切り替えろ。\n\0":
'???',

# Gendo Ikari
"エヴァ両機は\nダミープラグに切り替えろ。\n\0":
'???',

# Kozo Fuyutsuki
"碇、ダミープラグの使用は\nお前だけのみならず、委員会の\n許可を得なければならないんだ。▽\nそれに、ゼーレが黙ってはいないぞ！\nそれでも使うのか？\n\0":
'???',

# Male Staff
"しかし、ダミープラグは司令の他、\n委員会の許可が必要です。\n\0":
'???',

# Gendo Ikari
"構わん、やれ。\n\0":
'???',

# Maya Ibuki, Female Staff
"初号機のダミーシステム、\n起動します。\n\0":
'???',

# Shinji Ikari
"父さん…、\nくそっ、やっぱり僕なんか\nいらないんだ…。\n\0":
'???',

# Maya Ibuki, Female Staff
"初号機、ダミーシステムに\n切り替わりました。\n\0":
'???',

# Maya Ibuki, Female Staff
"弐号機のダミーシステム、\n起動します。\n\0":
'???',

# Asuka Soryu Langley
"何よ…、\n私じゃ役不足っていうの…？\n\0":
'???',

# Maya Ibuki, Female Staff
"弐号機、ダミーシステムに\n切り替わりました。\n\0":
'???',

# Maya Ibuki, Female Staff
"零号機のダミーシステム、\n起動します。\n\0":
'???',

# Rei Ayanami 
"やっぱり私…、\nいらなくなるのね…。\n\0":
'???',

# Maya Ibuki, Female Staff
"零号機、ダミーシステムに\n切り替わりました。\n\0":
'???',

# Maya Ibuki, Female Staff
"参号機のダミーシステム、\n起動します。\n\0":
'???',

# Toji Suzuhara 
"くっそぉ、…何や！！\nワイの事、コケにしおってからに！！\n\0":
'???',

# Maya Ibuki, Female Staff
"参号機、ダミーシステムに\n切り替わりました。\n\0":
'???',

# Maya Ibuki, Female Staff
"四号機のダミーシステム、\n起動します。\n\0":
'Unit-04\'s dummy system\n has been activated.\n\0',

# Kaworu Nagisa 
"僕は…、\n僕は必要じゃなかったんだ…。\n\0":
'They...\n They didn\'t need me...\n\0',

# Maya Ibuki, Female Staff
"四号機、ダミーシステムに\n切り替わりました。\n\0":
'Unit-04, switched over to dummy system.\n\0',

# Gendo Ikari
"…。▽\nわかった、もう少し待とう。\n\0":
'???',

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
'Nine of them?\n My final moments may be upon me.\n\0',

# Shiro Tokita
"ジェットアローン改、\n起動スタンバイ！！\n\0":
'Jet Alone 2,\n stand by for activation!!\n\0',

# Toji Suzuhara
"な、何やアレ！？\n\0":
'Wh-what\'s that?!\n\0',

# Asuka Soryu Langley
"もう一体来るの…？\n\0":
'The hell is it this time...?\0 ',

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

# Makoto Hyuga, Male Staff
"使徒、ジオフロントに侵入。\n本部へ真っ直ぐ接近中！\n\0":
'The Angel has invaded the GeoFront.\nCurrently on a direct trajectory for Headquarters!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ、リフトアップ！\n\0":
'Evas undergoing lift-up!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ、リフトアップ完了。\nパイロットは、迎撃準備を！\n\0":
'Eva lift-up completed.\nPilots are preparing to intercept!\n\0',

# Misato Katsuragi 
"次の攻撃はチャージが\n完了するまで出来ないわ。▽\nチャージゲージが\n最大まで回復したら、\nまた%1iボタンを押して攻撃よ！\n\0":
'???',

# Shinji Ikari
"はい、分かりました！\n\0":
'???',

# Misato Katsuragi 
"何ですって！？\nこの距離から、だというの…？▽\nヤツの中和距離は\nこちらの予想以上の広さよ。▽\n恐らく、遠距離攻撃で来るわ！！▽\n気をつけなさい！！\n\0":
'???',

# Kozo Fuyutsuki
"この距離から、というのか！？\nいかん、奴は遠距離攻撃をしかけて\nくるつもりだ。▽\n既に射程内に入っていないとも\n限らん。\n油断するな！！\n\0":
'???',

# Female Staff
"そんな！？\n中和距離の範囲が予想以上だわ。▽\n恐らく使徒は、この距離からでも、\n攻撃可能と思われます。▽\n気をつけて下さい！！\n\0":
'???',

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

# Shigeru Aoba, Male Staff
"エヴァ初号機、\nΑΤフィールド中和開始！\n\0":
'???',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\n初号機、残留ΑΤフィールド$h。\n\0":
'???',

# Shigeru Aoba, Male Staff
"エヴァ弐号機、\nΑΤフィールド中和開始！\n\0":
'???',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\n弐号機、残留ΑΤフィールド$h。\n\0":
'???',

# Shigeru Aoba, Male Staff
"エヴァ零号機、\nΑΤフィールド中和開始！\n\0":
'???',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\n零号機、残留ΑΤフィールド$h。\n\0":
'???',

# Shigeru Aoba, Male Staff
"エヴァ参号機、\nΑΤフィールド中和開始！\n\0":
'???',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\n参号機、残留ΑΤフィールド$h。\n\0":
'???',

# Shigeru Aoba, Male Staff
"エヴァ四号機、\nΑΤフィールド中和開始！\n\0":
'???',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\n四号機、残留ΑΤフィールド$h。\n\0":
'???',

# Shigeru Aoba, Male Staff
"エヴァ両機、\nΑΤフィールド中和開始！\n\0":
'???',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\nエヴァ、残留ΑΤフィールド$h。\n\0":
'???',

# Shigeru Aoba, Male Staff
"目標のΑΤフィールド、\n消滅しました！\n\0":
'???',

# Shigeru Aoba
"エヴァ初号機、ΑΤフィールド\n中和距離から離脱しました。\n\0":
'???',

# Male Staff
"エヴァ初号機、ΑΤフィールド\n中和距離から離脱。\n\0":
'???',

# Shigeru Aoba
"エヴァ弐号機、ΑΤフィールド\n中和距離から離脱しました。\n\0":
'???',

# Male Staff
"エヴァ弐号機、ΑΤフィールド\n中和距離から離脱。\n\0":
'???',

# Shigeru Aoba
"エヴァ零号機、ΑΤフィールド\n中和距離から離脱しました。\n\0":
'???',

# Male Staff
"エヴァ零号機、ΑΤフィールド\n中和距離から離脱。\n\0":
'???',

# Shigeru Aoba
"エヴァ参号機、ΑΤフィールド\n中和距離から離脱しました。\n\0":
'???',

# Male Staff
"エヴァ参号機、ΑΤフィールド\n中和距離から離脱。\n\0":
'???',

# Shigeru Aoba
"エヴァ四号機、ΑΤフィールド\n中和距離から離脱しました。\n\0":
'???',

# Male Staff
"エヴァ四号機、ΑΤフィールド\n中和距離から離脱。\n\0":
'???',

# Shigeru Aoba
"エヴァ両機、ΑΤフィールド\n中和距離から離脱しました。\n\0":
'???',

# Male Staff
"エヴァ両機、ΑΤフィールド\n中和距離から離脱。\n\0":
'???',

# Misato Katsuragi 
"シンジ君は退避して！\n\0":
'???',

# Kozo Fuyutsuki
"初号機パイロットはただちに退避！\n\0":
'???',

# Female Staff
"初号機パイロットは\n退避して下さい！\n\0":
'???',

# Misato Katsuragi 
"アスカは退避して！\n\0":
'???',

# Kozo Fuyutsuki
"弐号機パイロットは退避しろ。\n\0":
'???',

# Female Staff
"弐号機パイロットは\n退避して下さい！\n\0":
'???',

# Misato Katsuragi 
"レイは退避して！\n\0":
'???',

# Kozo Fuyutsuki
"零号機パイロットは退避しろ！\n\0":
'???',

# Female Staff
"零号機パイロットは\n退避して下さい！\n\0":
'???',

# Misato Katsuragi 
"トウジ君は退避して！\n\0":
'???',

# Kozo Fuyutsuki
"参号機パイロットは退避だ！\n\0":
'???',

# Female Staff
"参号機パイロットは\n退避して下さい！\n\0":
'???',

# Misato Katsuragi 
"カヲル君は退避して！\n\0":
'???',

# Kozo Fuyutsuki
"四号機パイロットは退避しろ！\n\0":
'???',

# Female Staff
"四号機パイロットは\n退避して下さい！\n\0":
'???',

# Misato Katsuragi 
"エヴァ両機は退避して！\n\0":
'???',

# Kozo Fuyutsuki
"エヴァ両機パイロットは\nただちに退避！\n\0":
'???',

# Female Staff
"エヴァ両機パイロットは\n退避して下さい！\n\0":
'???',

# Misato Katsuragi 
"シンジ君は接近戦に\n移ってちょうだい！\n\0":
'???',

# Kozo Fuyutsuki
"初号機は接近戦に移行しろ！\n\0":
'???',

# Female Staff
"初号機パイロットは\n接近戦に移行して下さい！\n\0":
'???',

# Misato Katsuragi 
"アスカ、あなたは\n接近戦に移ってちょうだい！！\n\0":
'???',

# Kozo Fuyutsuki
"弐号機は接近戦に移行しろ！\n\0":
'???',

# Female Staff
"弐号機パイロットは\n接近戦に移行して下さい！\n\0":
'???',

# Misato Katsuragi 
"レイ、接近戦に移ってちょうだい！\n\0":
'???',

# Kozo Fuyutsuki
"零号機はこれより接近戦に\n移行しろ！\n\0":
'???',

# Female Staff
"零号機パイロットは\n接近戦に移行して下さい！\n\0":
'???',

# Misato Katsuragi 
"トウジ君には接近戦を頼むわ！\n\0":
'???',

# Kozo Fuyutsuki
"参号機、接近戦へ移行しろ！！\n\0":
'???',

# Female Staff
"参号機パイロットは\n接近戦に移行して下さい！\n\0":
'???',

# Misato Katsuragi 
"カヲル君、これから接近戦に\n移ってちょうだい！\n\0":
'???',

# Kozo Fuyutsuki
"四号機は接近戦に移行しろ！\n\0":
'???',

# Female Staff
"四号機パイロットは\n接近戦に移行して下さい！\n\0":
'???',

# Misato Katsuragi 
"エヴァ両機は接近戦に移って！\n\0":
'???',

# Kozo Fuyutsuki
"エヴァ両機、\n接近戦に移行しろ！\n\0":
'???',

# Female Staff
"エヴァ両機パイロットは\n接近戦に移行して下さい！\n\0":
'???',

# Misato Katsuragi 
"シンジ君、射撃開始！\n\0":
'???',

# Kozo Fuyutsuki
"初号機パイロット、\n射撃開始！\n\0":
'???',

# Female Staff
"初号機パイロットは、\n射撃開始！\n\0":
'???',

# Misato Katsuragi 
"アスカ、射撃開始！\n\0":
'???',

# Kozo Fuyutsuki
"弐号機パイロット、\n射撃開始！\n\0":
'???',

# Female Staff
"弐号機パイロットは、\n射撃開始！\n\0":
'???',

# Misato Katsuragi 
"レイ、射撃開始！\n\0":
'???',

# Kozo Fuyutsuki
"零号機パイロット、\n射撃開始！\n\0":
'???',

# Female Staff
"零号機パイロットは、\n射撃開始！\n\0":
'???',

# Misato Katsuragi 
"トウジ君、射撃開始！\n\0":
'???',

# Kozo Fuyutsuki
"参号機パイロット、\n射撃開始！\n\0":
'???',

# Female Staff
"参号機パイロットは、\n射撃開始！\n\0":
'???',

# Misato Katsuragi 
"カヲル君、射撃開始！\n\0":
'???',

# Kozo Fuyutsuki
"四号機パイロット、\n射撃開始！\n\0":
'???',

# Female Staff
"四号機パイロットは、\n射撃開始！\n\0":
'???',

# Misato Katsuragi 
"エヴァ両機、射撃開始！\n\0":
'???',

# Kozo Fuyutsuki
"エヴァ両機パイロット、\n射撃開始！\n\0":
'???',

# Female Staff
"エヴァ両機パイロットは\n射撃開始！\n\0":
'???',

# Misato Katsuragi 
"シンジ君はその場で待機！\n\0":
'???',

# Kozo Fuyutsuki
"初号機パイロットは\nその場で待機だ！\n\0":
'???',

# Female Staff
"初号機パイロットは\nその場で待機して下さい！\n\0":
'???',

# Misato Katsuragi 
"アスカはその場で待機！\n\0":
'???',

# Kozo Fuyutsuki
"弐号機パイロットは\nその場で待機だ！\n\0":
'???',

# Female Staff
"弐号機パイロットは\nその場で待機して下さい！\n\0":
'???',

# Misato Katsuragi 
"レイはその場で待機！\n\0":
'???',

# Kozo Fuyutsuki
"零号機パイロットは\nその場で待機だ！\n\0":
'???',

# Female Staff
"零号機パイロットは\nその場で待機して下さい！\n\0":
'???',

# Misato Katsuragi 
"トウジ君はその場で待機！\n\0":
'???',

# Kozo Fuyutsuki
"参号機パイロットは\nその場で待機だ！\n\0":
'???',

# Female Staff
"参号機パイロットは\nその場で待機して下さい！\n\0":
'???',

# Misato Katsuragi 
"カヲル君はその場で待機！\n\0":
'???',

# Kozo Fuyutsuki
"四号機パイロットは\nその場で待機だ！\n\0":
'???',

# Female Staff
"四号機パイロットは\nその場で待機して下さい！\n\0":
'???',

# Misato Katsuragi 
"エヴァ両機はその場で待機！\n\0":
'???',

# Kozo Fuyutsuki
"エヴァ両機パイロットは\nその場で待機だ！\n\0":
'???',

# Female Staff
"エヴァ両機パイロットは\nその場で待機して下さい！\n\0":
'???',

# Misato Katsuragi 
"初号機、\n$fエリアに移動して！\n\0":
'Unit-01,\n move to Area $f!\n\0',

# Kozo Fuyutsuki
"初号機、\n$fエリアに移動！\n\0":
'Unit-01,\n move to Area $f!\n\0',

# Female Staff
"初号機、$fエリアに\n移動して下さい！\n\0":
'Unit-01, please\n move to Area $f!\n\0',

# Misato Katsuragi 
"弐号機、\n$fエリアに移動して！\n\0":
'Unit-02,\n move to Area $f!\n\0',

# Kozo Fuyutsuki
"弐号機、\n$fエリアに移動！\n\0":
'Unit-02,\n move to Area $f!\n\0',

# Female Staff
"弐号機、$fエリアに\n移動して下さい！\n\0":
'Unit-02, please\n move to Area $f!\n\0',

# Misato Katsuragi 
"零号機、\n$fエリアに移動して！\n\0":
'Unit-00,\n move to Area $f!\n\0',

# Kozo Fuyutsuki
"零号機、\n$fエリアに移動！\n\0":
'Unit-00,\n move to Area $f!\n\0',

# Female Staff
"零号機、$fエリアに\n移動して下さい！\n\0":
'Unit-00, please\n move to Area $f!\n\0',

# Misato Katsuragi 
"参号機、\n$fエリアに移動して！\n\0":
'Unit-03,\n move to Area $f!\n\0',

# Kozo Fuyutsuki
"参号機、\n$fエリアに移動！\n\0":
'Unit-03,\n move to Area $f!\n\0',

# Female Staff
"参号機、$fエリアに\n移動して下さい！\n\0":
'Unit-03, please\n move to Area $f!\n\0',

# Misato Katsuragi 
"四号機、\n$fエリアに移動して！\n\0":
'Unit-04,\n move to Area $f!\n\0',

# Kozo Fuyutsuki
"四号機、\n$fエリアに移動！\n\0":
'Unit-04,\n move to Area $f!\n\0',

# Female Staff
"四号機、$fエリアに\n移動して下さい！\n\0":
'Unit-04, please\n move to Area $f!\n\0',

# Misato Katsuragi 
"エヴァ両機、\n$fエリアに移動して！\n\0":
'Both Evas,\n move to Area $f!\n\0',

# Kozo Fuyutsuki
"エヴァ両機、\n$fエリアに移動！\n\0":
'Both Evas,\n move to Area $f!',

# Female Staff
"エヴァ両機、$fエリアに\n移動して下さい！\n\0":
'Both Evas, please\n move to Area $f!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ初号機の攻撃、\n使徒に$jのダメージ！\n\0":
'Eva Unit-01\'s attack did\n $j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ弐号機の攻撃、\n使徒に$jのダメージ！\n\0":
'Eva Unit-02\'s attack did\n $j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ零号機の攻撃、\n使徒に$jのダメージ！\n\0":
'Eva Unit-00\'s attack did\n $j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ参号機の攻撃、\n使徒に$jのダメージ！\n\0":
'Eva Unit-03\'s attack did\n $j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ四号機の攻撃、\n使徒に$jのダメージ！\n\0":
'Eva Unit-04\'s attack did\n $j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ両機の攻撃、\n使徒に$jのダメージ！\n\0":
'Both Evas\' attacks did\n $j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、初号機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n $j damage to the Unit-01!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、弐号機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n $j damage to the Unit-02!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、零号機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n $j damage to the Unit-00!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、参号機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n $j damage to the Unit-03!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、四号機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n $j damage to the Unit-04!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、エヴァ両機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n $j damage to both Evas!\n\0',

# Makoto Hyuga, Male Staff
"ΑΤフィールドとシンクロ率、\n共に低下！\n\0":
'A.T. Field and synch ratio\n both dropped!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア、兵装ビル、攻撃！\n使徒に$jのダメージ！\n\0":
'???',

# Shigeru Aoba, Male Staff
"$fエリア電源ビル、\n使徒の攻撃により、$jのダメージ！\n\0":
'The power building in Area $f\n received $j damage from the Angel!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア武器庫ビル、\n使徒の攻撃により、$jのダメージ！\n\0":
'The armory building in Area $f\n received $j damage from the Angel!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア兵装ビル、\n使徒の攻撃により、$jのダメージ！\n\0":
'The armament building in Area $f\n received $j damage from the Angel!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア防御施設、\n使徒の攻撃により、$jのダメージ！\n\0":
'The defense facility in Area $f\n received $j damage from the Angel!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア、国連軍、攻撃！\n使徒、$jのダメージ！\n\0":
'Attack by U.N. forces in Area $f!\n $j damage to the Angel!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア、国連軍、\n使徒の攻撃により、$jのダメージ！\n\0":
'U.N. forces in Area $f\n received $j damage from the Angel!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア電源ビル、\n破壊されました！\n\0":
'The power building in Area $f\n has been destroyed!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア武器庫ビル、\n破壊されました！\n\0":
'The armory building in Area $f\n has been destroyed!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア兵装ビル、\n破壊されました！\n\0":
'The armament building in Area $f\n has been destroyed!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア防御施設、\n破壊されました！\n\0":
'The defense facility in Area $f\n has been destroyed!\n\0',

# Maya Ibuki, Female Staff
"エヴァ初号機のアンビリカルケーブル、\n切断しました！\n\0":
'Eva Unit-01\'s umbilical cable\n is disconnected!\n\0',

# Maya Ibuki, Female Staff
"エヴァ弐号機のアンビリカルケーブル、\n切断しました！\n\0":
'Eva Unit-02\'s umbilical cable\n is disconnected!\n\0',

# Maya Ibuki, Female Staff
"エヴァ零号機のアンビリカルケーブル、\n切断しました！\n\0":
'Eva Unit-00\'s umbilical cable\n is disconnected!\n\0',

# Maya Ibuki, Female Staff
"エヴァ参号機のアンビリカルケーブル、\n切断しました！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ四号機のアンビリカルケーブル、\n切断しました！\n\0":
'Eva Unit-04\'s umbilical cable\n is disconnected!\n\0',

# Maya Ibuki, Female Staff
"エヴァ両機のアンビリカルケーブル、\n切断しました！\n\0":
'Both Evas\' umbilical cables\n are disconnected!\n\0',

# Maya Ibuki, Female Staff
"エヴァ初号機、\nアンビリカルケーブル接続。\n\0":
'Eva Unit-01, umbilical cable connected.\n\0',

# Maya Ibuki, Female Staff
"エヴァ弐号機、\nアンビリカルケーブル接続。\n\0":
'Eva Unit-02, umbilical cable connected.\n\0',

# Maya Ibuki, Female Staff
"エヴァ零号機、\nアンビリカルケーブル接続。\n\0":
'Eva Unit-00, umbilical cable connected.\n\0',

# Maya Ibuki, Female Staff
"エヴァ参号機、\nアンビリカルケーブル接続。\n\0":
'Eva Unit-03, umbilical cable connected.\n\0',

# Maya Ibuki, Female Staff
"エヴァ四号機、\nアンビリカルケーブル接続。\n\0":
'Eva Unit-04, umbilical cable connected.\n\0',

# Maya Ibuki, Female Staff
"エヴァ両機、\nアンビリカルケーブル接続。\n\0":
'Both Evas, umbilical cables connected.\n\0',

# Toji Suzuhara 
"動かへん…。ああ、何でや…。\n何で動かへんのや…。\n\0":
'???',

# Kaworu Nagisa 
"そんな、動かない…。\n僕に動かせないなんて…。なぜだ…！！\n\0":
'???',

# Maya Ibuki, Female Staff
"パイロットのシンクロ率が低すぎます！\n…これではエヴァは稼動しません！\n\0":
'???',

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

# Toji Suzuhara 
"ほな、いっちょ\nパチキかましたらぁ！！\n\0":
'???',

# Maya Ibuki 
"エヴァ初号機、\nポジトロンスナイパーライフル発射！\n\0":
'Eva Unit-01 has discharged\n the positron sniper rifle!\n\0',

# Male Staff
"エヴァ初号機、ポジトロンスナイパー\nライフルの発射に成功しました！\n\0":
'Eva Unit-01 successfully discharged\n the positron sniper rifle!\n\0',

# Maya Ibuki 
"エヴァ弐号機、\nポジトロンスナイパーライフル発射！\n\0":
'Eva Unit-02 has discharged\n the positron sniper rifle!\n\0',

# Male Staff
"エヴァ弐号機、ポジトロンスナイパー\nライフルの発射に成功しました！\n\0":
'Eva Unit-02 successfully discharged\n the positron sniper rifle!\n\0',

# Maya Ibuki 
"エヴァ零号機、\nポジトロンスナイパーライフル発射！\n\0":
'Eva Unit-00 has discharged\n the positron sniper rifle!\n\0',

# Male Staff
"エヴァ零号機、ポジトロンスナイパー\nライフルの発射に成功しました！\n\0":
'Eva Unit-00 successfully discharged\n the positron sniper rifle!\n\0',

# Maya Ibuki 
"エヴァ参号機、\nポジトロンスナイパーライフル発射！\n\0":
'Eva Unit-03 has discharged\n the positron sniper rifle!\n\0',

# Male Staff
"エヴァ参号機、ポジトロンスナイパー\nライフルの発射に成功しました！\n\0":
'Eva Unit-03 successfully discharged\n the positron sniper rifle!\n\0',

# Maya Ibuki 
"エヴァ四号機、\nポジトロンスナイパーライフル発射！\n\0":
'Eva Unit-04 has discharged\n the positron sniper rifle!\n\0',

# Male Staff
"エヴァ四号機、ポジトロンスナイパー\nライフルの発射に成功しました！\n\0":
'Eva Unit-04 successfully discharged\n the positron sniper rifle!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ初号機の攻撃、\nエヴァシリーズに$jのダメージ！\n\0":
'Eva Unit-01\'s attack did\n$j damage to Eva Series unit!',

# Makoto Hyuga, Male Staff
"エヴァ弐号機の攻撃、\nエヴァシリーズに$jのダメージ！\n\0":
'Eva Unit-02\'s attack did\n$j damage to Eva Series unit!',

# Makoto Hyuga, Male Staff
"エヴァ零号機の攻撃、\nエヴァシリーズに$jのダメージ！\n\0":
'Eva Unit-00\'s attack did\n$j damage to Eva Series unit!',

# Makoto Hyuga, Male Staff
"エヴァ参号機の攻撃、\nエヴァシリーズに$jのダメージ！\n\0":
'Eva Unit-03\'s attack did\n$j damage to Eva Series unit!',

# Makoto Hyuga, Male Staff
"エヴァ四号機の攻撃、\nエヴァシリーズに$jのダメージ！\n\0":
'Eva Unit-04\'s attack did\n$j damage to Eva Series unit!',

# Makoto Hyuga, Male Staff
"エヴァシリーズの攻撃、\n初号機に$jのダメージ！\n\0":
'Attack by Eva Series unit did\n$j damage to Unit-01!\n\0',

# Makoto Hyuga, Male Staff
"エヴァシリーズの攻撃、\n弐号機に$jのダメージ！\n\0":
'Attack by Eva Series unit did\n$j damage to Unit-02!\n\0',

# Makoto Hyuga, Male Staff
"エヴァシリーズの攻撃、\n零号機に$jのダメージ！\n\0":
'Attack by Eva Series unit did\n$j damage to Unit-00!\n\0',

# Makoto Hyuga, Male Staff
"エヴァシリーズの攻撃、\n参号機に$jのダメージ！\n\0":
'Attack by Eva Series unit did\n$j damage to Unit-03!\n\0',

# Makoto Hyuga, Male Staff
"エヴァシリーズの攻撃、\n四号機に$jのダメージ！\n\0":
'Attack by Eva Series unit did\n$j damage to Unit-04!\n\0',

# Shigeru Aoba, Male Staff
"兵装ビル、攻撃！\n$jのダメージ！\n\0":
'Armory building has attacked!\n It did $j damage!\n\0',

# Shigeru Aoba, Male Staff
"電源ビル、\n$jのダメージ！\n\0":
'Power building has\n taken $j damage!\n\0',

# Shigeru Aoba, Male Staff
"武器庫ビル、\n$jのダメージ！\n\0":
'Armory building has\n taken $j damage!\n\0',

# Shigeru Aoba, Male Staff
"兵装ビル、\n$jのダメージ！\n\0":
'Armament building has\n taken $j damage!\n\0',

# Shigeru Aoba, Male Staff
"防御施設、\n$jのダメージ！\n\0":
'Defense facility has\n taken $j damage!\n\0',

# Shigeru Aoba, Male Staff
"ネルフ本部、\n$jのダメージ！\n\0":
'Nerv H.Q. has\n taken $j damage!\n\0',

# Shigeru Aoba, Male Staff
"電源ビル、エヴァシリーズの\n攻撃により、破壊されました！\n\0":
'Power building has been\n destroyed by the Eva Series!\n\0',

# Shigeru Aoba, Male Staff
"武器庫ビル、エヴァシリーズの\n攻撃により、破壊されました！\n\0":
'Armory building has been\n destroyed by the Eva Series!\n\0',

# Shigeru Aoba, Male Staff
"兵装ビル、エヴァシリーズの\n攻撃により、破壊されました！\n\0":
'Armament building has been\n destroyed by the Eva Series!\n\0',

# Shigeru Aoba, Male Staff
"防御施設、エヴァシリーズの\n攻撃により、破壊されました！\n\0":
'Defense facility has been\n destroyed by the Eva Series!\n\0',

# Makoto Hyuga, Male Staff
"ΘΑ改、攻撃！\n$jのダメージ！\n\0":
'ΘΑ2 has attacked!\n It did $j damage!\n\0',

# Makoto Hyuga, Male Staff
"エヴァシリーズの攻撃、\nΘΑ改に$jのダメージ！\n\0":
'Attack by Eva Series unit\n did $j damage to ΘΑ2!\n\0',

# Shigeru Aoba, Male Staff
"兵装ビル、攻撃！\n使徒に$jのダメージ！\n\0":
'Armament building attacked!\n $j damage to the Angel!\n\0',

# Shigeru Aoba, Male Staff
"国連軍、攻撃！\n使徒、$jのダメージ！\n\0":
'Attack by U.N. forces!\n $j damage to the Angel!\n\0',

# Shigeru Aoba, Male Staff
"国連軍、\n$jのダメージ！\n\0":
'U.N. forces have\n taken $j damage!\n\0',

# Shigeru Aoba, Male Staff
"電源ビル、破壊されました！\n\0":
'Power building has been destroyed!\n\0',

# Shigeru Aoba, Male Staff
"武器庫ビル、破壊されました！\n\0":
'Armory building has been destroyed!\n\0',

# Shigeru Aoba, Male Staff
"兵装ビル、破壊されました！\n\0":
'Armament building has been destroyed!\n\0',

# Shigeru Aoba, Male Staff
"防御施設、破壊されました！\n\0":
'Defense facility has been destroyed!\n\0',

# Shigeru Aoba, Male Staff
"国連軍、\n掃滅しました！\n\0":
'U.N. forces have\n been annihilated!\n\0',

# Shinji Ikari
"嫌です。\n\0":
'???',

# Shinji Ikari
"そんな事出来ません。\n\0":
'???',

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
'???',

# Kozo Fuyutsuki
"命令を無視するつもりか！！\n\0":
'???',

# Female Staff
"弐号機パイロット、\n命令に従って下さい！\n\0":
'???',

# Rei Ayanami 
"…命令は聞けません。\n\0":
'???',

# Rei Ayanami 
"拒否します…。\n\0":
'???',

# Rei Ayanami 
"どうするかは、私が決めます。\n\0":
'???',

# Rei Ayanami 
"いいえ。\n私は、独断で行動します。\n\0":
'???',

# Kozo Fuyutsuki
"命令違反だぞ！！\n\0":
'???',

# Female Staff
"危険です、\n指示に従って下さい。\n\0":
'???',

# Toji Suzuhara 
"そんな命令、聞けまへんわ。\n\0":
'???',

# Toji Suzuhara 
"冗談でしょ？\nお断りしますわ。\n\0":
'???',

# Toji Suzuhara 
"そんなん聞けんわ！\n絶対嫌やわ。\n\0":
'???',

# Toji Suzuhara 
"ワシかて自分で行動出来ます！\n口出さんといて下さい。\n\0":
'???',

# Misato Katsuragi 
"トウジ君っ！！\n\0":
'???',

# Kozo Fuyutsuki
"無茶しおって！！\n\0":
'???',

# Female Staff
"参号機パイロット、\n命令違反はいけません。\n\0":
'???',

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
'???',

# Maya Ibuki, Female Staff
"エヴァ初号機、神経再接続完了！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ弐号機、神経再接続完了！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ零号機、神経再接続完了！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ参号機、神経再接続完了！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ四号機、神経再接続完了！\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ両機、神経再接続完了！\n\0":
'???',

# Shigeru Aoba, Male Staff
"量産機、残留ΑΤフィールド$g。\n初号機、残留ΑΤフィールド$h。\n\0":
'???',

# Shigeru Aoba, Male Staff
"量産機、残留ΑΤフィールド$g。\n弐号機、残留ΑΤフィールド$h。\n\0":
'???',

# Shigeru Aoba, Male Staff
"量産機、残留ΑΤフィールド$g。\n零号機、残留ΑΤフィールド$h。\n\0":
'???',

# Shigeru Aoba, Male Staff
"量産機、残留ΑΤフィールド$g。\n参号機、残留ΑΤフィールド$h。\n\0":
'???',

# Shigeru Aoba, Male Staff
"量産機、残留ΑΤフィールド$g。\n四号機、残留ΑΤフィールド$h。\n\0":
'???',

# Misato Katsuragi 
"初号機、移動して！\n\0":
'???',

# Kozo Fuyutsuki
"初号機、移動！\n\0":
'???',

# Female Staff
"初号機、移動して下さい！\n\0":
'???',

# Misato Katsuragi 
"弐号機、移動して！\n\0":
'???',

# Kozo Fuyutsuki
"弐号機、移動！\n\0":
'???',

# Female Staff
"弐号機、移動して下さい！\n\0":
'???',

# Misato Katsuragi 
"零号機、移動して！\n\0":
'???',

# Kozo Fuyutsuki
"零号機、移動！\n\0":
'???',

# Female Staff
"零号機、移動して下さい！\n\0":
'???',

# Misato Katsuragi 
"参号機、移動して！\n\0":
'???',

# Kozo Fuyutsuki
"参号機、移動！\n\0":
'???',

# Female Staff
"参号機、移動して下さい！\n\0":
'???',

# Misato Katsuragi 
"四号機、移動して！\n\0":
'???',

# Kozo Fuyutsuki
"四号機、移動！\n\0":
'???',

# Female Staff
"四号機、移動して下さい！\n\0":
'???',

# Misato Katsuragi 
"エヴァ両機、移動して！\n\0":
'???',

# Kozo Fuyutsuki
"エヴァ両機、移動！\n\0":
'???',

# Female Staff
"エヴァ両機、移動して下さい！\n\0":
'???',

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

# Shinji Ikari
"裏切ったな…。\n僕の気持ちを裏切ったな！！\n\0":
'???',

# Kaworu Nagisa 
"…シンジ君。▽\n君と同じ仕組まれた子供なんだ。\nそのために僕も君もいる。▽\n君は来てくれた。\n筋書き通りに。\n\0":
'???',

# Shinji Ikari
"そんな事どうでもいいよ！\n信じてたんだ、もっと君とは\n知り合う事が出来るって。\n\0":
'???',

# Kaworu Nagisa 
"だから裏切ったと…？\n僕に何を期待していたんだい。\n\0":
'???',

# Shinji Ikari
"僕の気持ちを踏みにじった…！\n君を信じてたのに…。▽\nでも、カヲル君は最初から\nこうするつもりで僕に近づいたの？\n\0":
'???',

# Kaworu Nagisa 
"僕はただ、さだめ、という流れに\nいるだけさ。▽\n君や、この世界すべての\nリリンのように。\n\0":
'???',

# Shinji Ikari
"僕は今でも…、信じたいんだ。\nカヲル君を…。\n\0":
'???',

# Kaworu Nagisa 
"でも、君は迷っている。\n僕が君達リリンの敵だから。\n\0":
'???',

# Shinji Ikari
"でも、僕は傷ついた。\n君に傷つけられた…。\n\0":
'???',

# Kaworu Nagisa 
"君はすがりたかっただけだ、\n何かに。▽\nヒトは、何かにすがらなければ、\n生きてはいけないからね。\n\0":
'???',

# Shinji Ikari
"僕の…、希望でもあったんだ。\n君と一緒にいたいって思ってたんだ。\n\0":
'???',

# Kaworu Nagisa 
"希望に潜む影に\n気づかなかったんだね。\n自分自身にある、その影に。\n\0":
'???',

# Shinji Ikari
"君を傷つけたくないんだよ！\n\0":
'???',

# Kaworu Nagisa 
"僕も君を傷つけるつもりはないよ。\n\0":
'???',

# Shinji Ikari
"じゃあ、\nじゃあ、こんな事やめてよ！\n\0":
'???',

# Kaworu Nagisa 
"君に会えて、嬉しかったよ。\n本当だよ。▽\nけれど、その時から、\n僕はやすらぎを失ったんだ。▽\n君を知り過ぎたのかもしれない。\n\0":
'???',

# Shinji Ikari
"君も…、\n僕を助けてくれないの？\n\0":
'???',

# Kaworu Nagisa 
"僕は君を、君は僕を救えない。\nいや、みんなそうさ。▽\n救われるかどうかは、\n自分で決めるしかない。\n\0":
'???',

# Shinji Ikari
"人の気持ちなんて\nどうでもいいんだ。\n\0":
'???',

# Kaworu Nagisa 
"僕の気持ちはどうでもいいのかい？\n君達リリンは。\n\0":
'???',

# Shinji Ikari
"だから、戦わないで…。\n一緒にいる事だって出来る。\n\0":
'???',

# Kaworu Nagisa 
"それは出来ない。\nこれが僕らの意志だから。\n\0":
'???',

# Shinji Ikari
"カヲル君、\nどうしてそんな事が言えるの。\n\0":
'???',

# Kaworu Nagisa 
"僕の答えは、\nすでに君の中にあるモノだから。\n\0":
'???',

# Shinji Ikari
"僕は違う！\nただ、君とは戦いたくないだけだ！\n\0":
'???',

# Kaworu Nagisa 
"けれども時間がない。\n君にも僕にも。\n\0":
'???',

# Shinji Ikari
"ごまかさないでよ、\nそうやって僕の気持ちを\nごまかさないでよ！！\n\0":
'???',

# Kaworu Nagisa 
"リリンは、絶望と向き合う事が\n出来ないからね。\n\0":
'???',

# Shinji Ikari
"そうやって、心を閉ざさないでよ！\n\0":
'???',

# Shinji Ikari
"カヲル君も、父さんと同じだ。\n僕を捨てて、利用して！\n\0":
'???',

# Kaworu Nagisa 
"いくつもの現実の断片に\n自分を見る事が出来なければ\n変わらない真実だよ。\n\0":
'???',

# Shinji Ikari
"捨てた、捨てたんだ！\nみんな僕を！！\n君も！！\n\0":
'???',

# Kaworu Nagisa 
"………。▽\n君は、しょうがなく\nエヴァに乗っていたんだね。▽\n捨てられるのが怖くて。▽\nそんな事はないのに。\n\0":
'???',

# Shinji Ikari
"僕は、君が好きだったんだ。\n\0":
'???',

# Kaworu Nagisa 
"でも、僕を受け入れられない。\n\0":
'???',

# Shinji Ikari
"受け入れるさ！！\n受け入れられるよ！！\n\0":
'???',

# Kaworu Nagisa 
"君は自由を受け入れられない。\n自由を与えられると、\n自分がいなくなると恐れている。\n\0":
'???',

# Shinji Ikari
"違う、違う、違う！！\n\0":
'???',

# Kaworu Nagisa 
"自由は解放と拘束。\nシンジ君は、どっちも選べない\nだろう？\n\0":
'???',

# Shinji Ikari
"君を好きになるのは僕の自由だ！\n違うの？\n\0":
'???',

# Kaworu Nagisa 
"…僕が滅びるのも、\nまた自由だ。\n\0":
'???',

# Shinji Ikari
"…そうなんだ。\n僕が嫌いなんだね。\n\0":
'???',

# Kaworu Nagisa 
"いいや、\n恐怖と絶望は、リリン達にも\n不要だという事さ。\n\0":
'???',

# Shinji Ikari
"何で、君まで僕を…、\n僕を傷つけるの…？\n\0":
'???',

# Kaworu Nagisa 
"君が僕という存在を知っただけ。\n傷つけたつもりはないよ。\n\0":
'???',

# Shinji Ikari
"でも、そうじゃないか。\n\0":
'???',

# Kaworu Nagisa 
"拒絶。\nそうやって自分の心を守るしか\nないのかい。\n\0":
'???',

# Shinji Ikari
"どうすればいいの？\n出会った時のように２人が\nなれるには、どうしたらいいの？\n\0":
'???',

# Kaworu Nagisa 
"………。▽\nすべてはリリンの流れのままに。▽\n………………。\n\0":
'???',

# Shinji Ikari
"嘘だよね。\nカヲル君が使徒だったなんて、\n嘘だよね…。\n\0":
'???',

# Kaworu Nagisa 
"僕は使徒としての価値を\n与えられた。▽\nそれが今、僕の存在している\n理由なんだ。\n\0":
'???',

# Shinji Ikari
"…関係ないよ。\nねえ、カヲル君は僕の事\nどう思ってるの…。\n\0":
'???',

# Kaworu Nagisa 
"…好きだよ、シンジ君。\n君の事が。\n\0":
'???',

# Shinji Ikari
"君に嫌われたくないよ。\n\0":
'???',

# Kaworu Nagisa 
"嫌いじゃないよ。\nでも、嫌われると僕に恐怖心を\n抱いている。▽\nヒトを信じられないからだね。\n\0":
'???',

# Shinji Ikari
"僕は、君に出会えた事が\n嬉しかったんだ。▽\n僕が探していたのは\n君だったんだって、嬉しかったんだ。\n\0":
'???',

# Kaworu Nagisa 
"僕も君に出会えて嬉しかったよ。\n同時に、悲しみもあった。\n\0":
'???',

# Kaworu Nagisa 
"でも、どんなに悲しくても\n君の事を忘れる事なんて出来ない。\n\0":
'???',

# Shinji Ikari
"なぜ僕に声をかけたの？\nなぜ僕に近づいたの？\n\0":
'???',

# Kaworu Nagisa 
"興味があったんだよ。\n純粋な想いで君を知って、\n…好きになりたかった。\n\0":
'???',

# Shinji Ikari
"僕たちが争う必要はないよ。\n\0":
'???',

# Kaworu Nagisa 
"そうだね。\nただ、僕は行かなきゃ\nいけないんだ。▽\n死に、そして生き続けるために。\n\0":
'???',

# Shinji Ikari
"カヲル君は、\n生きる事が楽しいの？\n\0":
'???',

# Kaworu Nagisa ,Teruo Kato, Misato Katsuragi, Rei Ayanami, Gendo Ikari, Ryoji Kaji, Shinji Ikari, Hikari Horaki, Maya Ibuki 
"……………。\n\0":
'???',

# Shinji Ikari
"カヲル君、\nもしかして死ぬつもりなの？\n\0":
'???',

# Shinji Ikari
"わからないよ。\n君の意志じゃないのに\n使徒になったなんて。\n\0":
'???',

# Kaworu Nagisa 
"でも、僕が使徒なのは事実さ。\n君の友達という事も。▽\nどうする事も出来ないんだ、\n流れには逆らえない。\n\0":
'???',

# Shinji Ikari
"僕とやり直せるよ。\n違う生き方があるよ、\n僕も、君も。▽\n一緒にやり直そうよ、\nカヲル君…。\n\0":
'???',

# Shinji Ikari
"カヲル君は僕にとって\n必要な人間なんだ。▽\n人類が居なくなるより、\n君が居なくなる方が嫌だよ！！\n\0":
'???',

# Kaworu Nagisa 
"………。▽\nでも、それじゃ、\n僕が寂しいままなんだ。▽\n一人で…。\nずっと一人で…。\n\0":
'???',

# Shinji Ikari
"だから！！\n僕がいるよ、ずっと側にいる！！\n\0":
'???',

# Shinji Ikari
"僕もそうやって逃げてきた。\nでも、いい事なんてなかった。▽\n流れに任せて生きるなんて、\n死んでるのと同じじゃないか。\n\0":
'???',

# Shinji Ikari
"ねえ、僕ともう一度\n友達になってよ。▽\nそして全部…、何もかも\n二人でやりなおそうよ。\n\0":
'???',

# Kaworu Nagisa 
"友達に…？\nもう一度…？\n\0":
'???',

# Shinji Ikari
"卑怯だよ。\n散々、僕に知った風な事を言って…。\n\0":
'???',

# Kaworu Nagisa 
"そうだね、そうかもしれない。\nその事は君に謝らなくちゃ\nいけなかったね…。\n\0":
'???',

# Shinji Ikari
"そんなの信用出来ないよ！！\n\0":
'???',

# Kaworu Nagisa 
"僕が使徒だから…？\n僕は君を友達と思っているよ。\n\0":
'???',

# Shinji Ikari
"行くなら、いっそ僕を殺してよ…。\n\0":
'???',

# Kaworu Nagisa 
"………。▽\nそれが、君の答えだね。\n\0":
'???',

# Shinji Ikari
"君と戦うなら、死んだ方がいい。\n死んだ方がいいよ！！\n\0":
'???',

# Kaworu Nagisa 
"戦いを放棄するのかい？\nこの先に、君達の未来が\nかかっているとしても…？\n\0":
'???',

# Shinji Ikari
"嘘だ！\n全部、それも僕を騙すためだ！\n\0":
'???',

# Kaworu Nagisa 
"…。▽\n僕が嫌いかい？\nそれが君の意志なら、\nしょうがない。\n\0":
'???',

# Shinji Ikari
"行かないで…、\nカヲル君、行かないでよ！！▽\nそしたら、僕も君も\n一人じゃなくなるんだ！！\n\0":
'???',

# Kaworu Nagisa 
"…一人じゃ、なくなる…。\n\0":
'???',

# Shinji Ikari
"カヲル君、\n君とは戦いたくないよ。\n\0":
'???',

# Kaworu Nagisa 
"なぜ？\nじゃあなぜ僕を止めようとするの？\n\0":
'???',

# Shinji Ikari
"君を、傷つけたくないからだよ。\n\0":
'???',

# Kaworu Nagisa 
"君が傷ついても？\n\0":
'???',

# Shinji Ikari
"ああ、そうだよ。\n僕は死んだっていい！\n\0":
'???',

# Kaworu Nagisa 
"嘘だね。\n君は、死ぬのが怖いはずだ。\n\0":
'???',

# Shinji Ikari
"死ぬのは怖いよ。\nでも、それより君を傷つける方が\n怖いよ。\n\0":
'???',

# Kaworu Nagisa 
"…なぜ、そこまで\n僕と戦いたくないんだい？\n\0":
'???',

# Shinji Ikari
"行かないって言ってよ！！\nお願いだよ！\nこのままじゃ、君と戦うことになる。\n\0":
'???',

# Kaworu Nagisa 
"だったら、しょうがないんじゃ\nないかな。▽\n僕も、君と戦うのは\nいい気分じゃないけれど…。\n\0":
'???',

# Shinji Ikari
"命令なんだ。\nこの先に行かせるなって。▽\nこの先へ行くなら、僕は君を\n倒さなくちゃいけないんだ。▽\nそんな事、嫌だよ。\n嫌なんだよ！！\n\0":
'???',

# Kaworu Nagisa 
"僕と戦うのが、怖い…？\n\0":
'???',

# Shinji Ikari
"怖いよ。\n君を失うのが…、怖いよ。\n\0":
'???',

# Kaworu Nagisa 
"君は何も、\n悪くはないのにね…。\n\0":
'???',

# Shinji Ikari
"行かないで…！！\n\0":
'???',

# Kaworu Nagisa 
"…それは君の意思かい？\nそれとも…。\n\0":
'???',

# Shinji Ikari
"僕は、僕はね…、\n君と生きたいんだ…。▽\n君が使徒だとかそんな事は\n関係ない。▽\n他の何でも関係なく、\n君と生きたいんだ。\n\0":
'???',

# Kaworu Nagisa 
"僕と…？\n\0":
'???',

# Kaworu Nagisa 
"…シンジ君にはわからないよ。\n\0":
'???',

# Kaworu Nagisa 
"僕にあったのは、\n…希望という絶望。▽\n人類がたどるべきだった道は\n絶望という希望…。▽\nシンジ君、僕も君が好きだったよ、\n君と希望を見つめたかった…。\nそうする事が出来れば…。\n\0":
'???',

# Kaworu Nagisa 
"………。▽\n僕も未来が見たい。\n君達、人と…、シンジ君の未来を\n見てみたいと思う。▽\n………。▽\nシンジ君…、僕も君と生きよう。\n僕も一緒に戦うよ…。\n\0":
'???',

# Kaworu Nagisa 
"これが………アダム………。\n…いや、…これは、リリス！？\n\0":
'???',

# Kaworu Nagisa 
"僕の還る場所は一つしかない。\nここでは、生きていけない事は無い。\n…でも、…でも僕は。\n\0":
'???',

# Shinji Ikari
"カヲル君、\nみんなカヲル君が好きなんだ。\n僕も…。▽\nもっと話し合おうよ。\n僕ら、きっとわかりあえるよ。\n\0":
'???',

# Shinji Ikari
"わかりあえないの？\nどうしても…？\n\0":
'???',

# Shinji Ikari
"やっぱり、戦うしかないの…？\n\0":
'???',

# Makoto Hyuga, Male Staff
"目標、反応消えました。\n使徒………殲滅しました。\n\0":
'???',

# Makoto Hyuga
"目標、反応消えました。\n使徒………消失しました。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le318.evs
#
# Rei Ayanami 
"私がいた、という記憶は残る。\nみんな、私を忘れない。\n\0":
'???',

# Rei's Shadow [Leliel]
"思い上がりね。\nあなたは誰の記憶にも留まらない。\nただいなくなるだけ。\n\0":
'???',

#
# ./USRDIR/event/cev0815.har_EXTRACT/cev0815.evs
#
# Ritsuko Akagi 
"どう、実験のデータ。\nまとめておいてくれたかしら？\n\0":
'???',

# Maya Ibuki 
"あ、まだ…ちょっと。\n\0":
'???',

# Ritsuko Akagi 
"最近、浮ついてるみたいね。\n\0":
'???',

# Maya Ibuki, Makoto Hyuga
"…すみません。\n\0":
'???',

# Ritsuko Akagi 
"あなたは真面目で出来る人だと、\n思っていたのに。\n\0":
'???',

# Maya Ibuki 
"……………………。▽\nセンパイ…。▽\n…私、センパイに認められたくて\n頑張ってきました。▽\nでも、認められていたのは\n私じゃなく、私の仕事。▽\nなのに私、勝手にセンパイに\n依存していました。▽\nいつか本当の私を\n認めてくれるだろうって。▽\n自分で自分を好きになれないから\nセンパイに依存していました。\n\0":
'???',

# Ritsuko Akagi, Shinji Ikari, Makoto Hyuga, Misato Katsuragi, Hikari Horaki, Gendo Ikari
"…………。\n\0":
'???',

# Maya Ibuki 
"仕事以外での自分の価値は、\n自分で作る事が出来ると\nわかったんです。\n\0":
'???',

# Ritsuko Akagi 
"マヤ…。\n\0":
'???',

# Maya Ibuki 
"あの、今まですみませんでした。▽\nダミーシステムの開発は、まだ\n納得出来ない部分はありますけど、\n…きちんと正面から取り組みます。\n\0":
'???',

# Ritsuko Akagi 
"…そう。\nじゃあ、改めて\n頼りにさせてもらうわ。\n\0":
'???',

#
# ./USRDIR/event/tev1301.har_EXTRACT/tev1301.evs
#
# Kozo Fuyutsuki
"消滅！？\n\0":
'???',

# Kozo Fuyutsuki
"確かに第２支部が\n消滅したんだな！？\n\0":
'???',

# Shigeru Aoba
"はい、全て確認しました。\n「消滅」です。\n\0":
'???',

# Ritsuko Akagi 
"手がかりは\nこの静止衛星からの映像だけで、\nあとは跡形も残ってないのよ。\n\0":
'???',

# Misato Katsuragi 
"ひどいわね。\n\0":
'???',

# Maya Ibuki 
"エヴァンゲリオン四号機ならびに\n半径８９キロ以内の関連研究施設は\n全て消滅しました。▽\n数千の人間も同じく…。\n\0":
'???',

# Shigeru Aoba
"おそらくは、ドイツで修復した\nΣ機関の搭載実験中の事故と\n思われます。▽\nそれにしても、爆発ではなく、\n消滅とは一体…。\n\0":
'???',

# Ritsuko Akagi 
"多分、ディラックの海に\n飲み込まれたんでしょうね。\nこの間の初号機みたいに。\n\0":
'???',

# Misato Katsuragi 
"じゃあ、\nせっかく直したΣ機関も。\n\0":
'???',

# Ritsuko Akagi 
"パーよ。\n夢は潰えたわね。\n\0":
'???',

# Misato Katsuragi 
"よくわからないものを\n無理して使うからよ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le007.evs
#
# Kaworu Nagisa 
"もう、生命維持も限界か。▽\n…………………。\n\0":
'???',

# Kaworu Nagisa 
"僕の魂は僕のものだ。\n身体が滅びても、\nヒトとして生きた事を忘れても。▽\n僕はアダムの運命はもう、\n歩まない…。\n\0":
'???',

# Kaworu Nagisa 
"僕は、ヒトとして生きた。\n死ぬ時もヒトとして死のう。▽\nさよなら…、みんな…。\n\0":
'???',

# Shinji Ikari
"………………………。\nもう、保温も酸素の循環も\n切れてる。\n\0":
'???',

# Shinji Ikari
"寒い…。\n\0":
'???',

# Shinji Ikari
"駄目だ、スーツも限界か。\n\0":
'???',

# Shinji Ikari
"ここまでか。\nもう疲れた。\n何もかも。\n\0":
'???',

# Yui Ikari, Misato Katsuragi, Asuka Soryu Langley
"もういいの？\n\0":
'???',

# Shinji Ikari
"母さん？\n\0":
'Mother?\n\0',

# Shinji Ikari
"もう、いいんだ。\n\0":
'???',

# Yui Ikari
"そう、もういいのね。\nよく頑張ったわね。\n\0":
'???',

# Yui Ikari
"おいで、シンジ。\nあなたがそう決めたのなら、\nずっとここに居てもいいのだから。\n\0":
'???',

# Asuka Soryu Langley
"保温も酸素の循環も\nもう、限界なんだ…。\n\0":
'???',

# Asuka Soryu Langley
"寒いよ…。\n\0":
'???',

# Asuka Soryu Langley
"ママ…。\n\0":
'Mama...\n\0',

# Kyoko Soryu Zeppelin 
"アスカ…。\nアスカちゃん…。\n\0":
'Asuka...\n Asuka-chan...\n\0',

# Asuka Soryu Langley
"ママ？\n\0":
'Mama?\n\0',

# Kyoko Soryu Zeppelin 
"アスカちゃん…。\n\0":
'Asuka-chan...\n\0',

# Asuka Soryu Langley
"ママ…、ママぁ…。\nどこに行ってたの、ママ。▽\nもう行かないで、そばにいて！\nママ…。\n\0":
'???',

# Kyoko Soryu Zeppelin 
"一緒よ、ずっと…。\nでも、それでいいのね？\n\0":
'???',

# Asuka Soryu Langley
"うん、いいの。\nママのところがいいの。\nずっとずっと、一緒にいる。\n\0":
'???',

# Kyoko Soryu Zeppelin 
"そう…、いいのよ。\nママはずっと一緒にいるわ。▽\nアスカちゃん…。\n\0":
'???',

# Rei Ayanami 
"もう、何も見えない。\n何も聞こえない…。▽\n思い出すのは、ただ暗闇の中。\n\0":
'???',

# Rei Ayanami 
"もう、帰してもらえるかしら。\n無へと…帰してもらえるのかしら。\n\0":
'???',

# Rei Ayanami 
"この身体も、もう終わり…。▽\n時間ね…。\n\0":
'???',

# Toji Suzuhara 
"寒ぅ…。\nもう、プラグの機能も\n限界なんやな…。\n\0":
'???',

# Toji Suzuhara 
"……………………。▽\n妹、無事なんかな…。▽\nごめんな。\n兄ちゃん、戻られへんわ。\n\0":
'???',

# Toji Suzuhara 
"おかん…。\nもう、ワシ…。\n\0":
'???',

# Toji's Mother
"しんどかったなぁ、もうええねんで。\n\0":
'???',

# Toji Suzuhara 
"おかん…。\n何か、寒くて眠いんや…。\n\0":
'???',

# Toji's Mother
"さあ眠り…、お母ちゃんが\n温めてあげるわ…。\n\0":
'???',

#
# ./USRDIR/event/tev1004.har_EXTRACT/tev1004.evs
#
# Shigeru Aoba
"電波システム回復。\n南極の碇司令から\n通信が入っています。\n\0":
'???',

# Misato Katsuragi 
"おつなぎして。\n\0":
'???',

# Gendo Ikari
"ご苦労だったな。\n葛城三佐。\n\0":
'???',

# Kozo Fuyutsuki
"ああ、よくやってくれた。\n使徒殲滅が我々の役目だ。▽\n多少の被害はいたしかたない。\n大目に見よう。\n\0":
'???',

# Gendo Ikari
"ところで、\n初号機のパイロットはいるか。\n\0":
'???',

# Gendo Ikari
"話は聞いた。\nよくやったな、シンジ。\n\0":
'???',

# Shinji Ikari
"え？\n…あ、は、はい。\n\0":
'???',

# Gendo Ikari
"では、葛城三佐。\n後の処理は任せる。\n\0":
'???',

# Misato Katsuragi 
"シンジ君。\nこの間、聞いたわよね。▽\n私がどうしてネルフに\n入ったのかを…。\n\0":
'???',

# Misato Katsuragi 
"私の父はね、自分の研究、\n夢に生きる人だったわ。▽\nそんな父を許せなかった。\n憎んでさえいたわ。\n\0":
'???',

# Shinji Ikari
"……………。\n（僕の父さんと同じだ。）\n\0":
'???',

# Misato Katsuragi 
"母や私、家族の事など\n全く構ってくれなかった。▽\n周りの人達は繊細な人だと\n言っていたわ。\n\0":
'???',

# Misato Katsuragi 
"でも、ホントは心の弱い、\n現実から、私達家族という現実から\n逃げてばかりいた人だったのよ。▽\n子供みたいな人だったわ。▽\n母が父と別れた時も、\nすぐに賛成したわ。▽\n母はいつも泣いてばかりだったもの。▽\n父はショックだったみたいだけど、\nその時は自業自得だと笑ったわ。\n\0":
'???',

# Misato Katsuragi 
"けど、最後は私の身代わりになって\n死んだの。\nセカンドインパクトの時にね。\n\0":
'???',

# Misato Katsuragi 
"私にはわからなくなったわ。\n父を憎んでいたのか、\n好きだったのか。▽\nただ一つ、はっきりとしているのは\nセカンドインパクトを引き起こした\n使徒を倒す。\n\0":
'???',

# Misato Katsuragi 
"そのためにネルフに入ったわ。▽\n結局、私はただ父への復讐を\nしたいだけなのかもしれないわ。\n父の呪縛から逃れるために。\n\0":
'???',

# Shinji Ikari
"ミサトさん…、僕…。▽\nいつも何でエヴァに\n乗っているんだろうって。\nそう思っていたんだ。▽\nさっき、父さんの言葉を聞いて\n褒められる事が嬉しいって\n初めてわかったような気がする。\n\0":
'???',

# Shinji Ikari
"僕は、父さんのさっきの言葉を\n聞きたくて、エヴァに\n乗ってるのかもしれないって。▽\nそれがわかったんだ…。\n\0":
'???',

# Misato Katsuragi 
"シンジ君、理由はどうあれ\nあなたは立派にやってるわ。\n人類を救うためではなくとも。▽\nそれは、あなたのお父さんだって\nわかっているわよ。\n\0":
'???',

# Misato Katsuragi 
"胸を張って生きなさい。\nシンジ君。▽\n見て、あなたが守った都市は\n今日も綺麗よ…。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le106.evs
#
# Shinji Ikari
"誰だってそうだ。\n楽しい思い出を大事にして\n生きてるはずだよ。▽\nそれさえあれば、\n生きていけるんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"でも、思い出はそこで終わり。\n同じ思い出ばかりを繋いで、\n何も変われない生き方を歩むのか？\n\0":
'???',

#
# ./USRDIR/event/tev0261.har_EXTRACT/tev0261.evs
#
# Ritsuko Akagi 
"ただし、この範囲を越えて\n人間関係は変動する事はないの。▽\nただ、この範囲も時間の経過や\n相手と関わりあった回数で\nその形と大きさを変化させるわ。\n\0":
'???',

# Ritsuko Akagi 
"これで人間関係に関する説明は\nお終いよ。\n\0":
'???',

#
# ./USRDIR/event/tev0257.har_EXTRACT/tev0257.evs
#
# Ritsuko Akagi 
"次に縦軸、好意についてよ。\n好意は相手への好き嫌いよ。\n\0":
'???',

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
# ./USRDIR/event/tev0701.har_EXTRACT/tev0701.evs
#
# Maya Ibuki, Makoto Hyuga, Female Staff
"本日未明、紀伊半島沖に\n使徒を確認。\n\0":
'???',

# Maya Ibuki 
"同時刻、エヴァでこれを\n上陸地点にて阻止する作戦を立案、\n実行。\n\0":
'???',

# Maya Ibuki, Misato Katsuragi, Female Staff, Makoto Hyuga
"予定時刻、目標と戦闘開始。\n\0":
'???',

# Maya Ibuki, Misato Katsuragi, Female Staff, Makoto Hyuga
"しかし、目標の分離攻撃により\nエヴァ二体の連携は崩れ、\n\0":
'???',

# Maya Ibuki, Misato Katsuragi, Female Staff, Makoto Hyuga
"エヴァ初号機、敗退…。\n\0":
'???',

# Maya Ibuki, Misato Katsuragi, Female Staff, Makoto Hyuga
"エヴァ弐号機、同じく敗退…。\n\0":
'???',

# Maya Ibuki, Makoto Hyuga, Female Staff
"現在目標は、\n国連軍のΝ地雷によって\n組織の２０％を損失。▽\nしかし活動再開まで、そう時間は\nかからないと考えられます。\n\0":
'???',

# Kozo Fuyutsuki
"情けない…。\n\0":
'???',

# Ritsuko Akagi 
"ブザマね。\n\0":
'???',

# Asuka Soryu Langley
"私のせいじゃないわ！！\nバカシンジさえ、私の足を\n引っ張らなければ勝ててたのよ！\n\0":
'???',

# Shinji Ikari
"なっ…、アスカだって作戦を\n無視して僕のせいにするなんて\nずるいじゃないか！！\n\0":
'???',

# Asuka Soryu Langley
"結局、アンタ邪魔なんだもん。\n私は悪くないわ。\n\0":
'???',

# Shinji Ikari
"そんな事言ったって、\n一人で出ても負けてたよ。\nきっと。\n\0":
'???',

# Asuka Soryu Langley
"うるさいわねっっ！！\n\0":
'???',

# Misato Katsuragi 
"黙らっしゃーーーい！！\n\0":
'???',

# Misato Katsuragi 
"…ハァ。\n…とは言ってもねェ。\nどうすりゃいいのかしら…。\n\0":
'???',

# Ritsuko Akagi 
"方法がない…わけじゃないわよ？\n\0":
'???',

# Misato Katsuragi 
"さっすが赤木リツコ博士。\n持つべきものは心優しき旧友ね。\n\0":
'???',

# Ritsuko Akagi 
"残念ながら、\n旧友のピンチを救うのは\n私じゃないわ。▽\nこのアイディアは加持君よ。\nほら、ここに作戦要項があるわ。\n\0":
'???',

# Misato Katsuragi 
"加持が？\n\0":
'???',

# Misato Katsuragi 
"アイツ…。\n\0":
'???',

# Misato Katsuragi 
"…アンタ達、いいわね、\nよく聞いて。▽\nこの使徒の弱点は一つ。\n分離中の核に対する二点同時の\n荷重攻撃、これしかないわ。▽\nつまり、エヴァ二体のタイミングを\n合わせた攻撃手段しかないのよ。▽\n二人の協調、完璧なユニゾンが\n必要なの。\n\0":
'???',

# Asuka Soryu Langley
"でェ、\n私達にどうしろってェ？\n\0":
'???',

# Misato Katsuragi 
"あなた達パイロットは、\n次の出撃までに\nユニゾンを上げておくこと。▽\nいいわね、常に二人一緒に\n行動するよう、心がけて。▽\nユニゾンが高いパイロット二人による\n同時荷重攻撃により、\n目標を殲滅します。▽\n以上解散！\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le508.evs
#
# Kaworu Nagisa 
"計画の進捗確認と、\nゼーレ主導の計画運用をするために\n根回しをしに来たのさ。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"つまり、\nリリンの言いなりだという事だね。\n\0":
'???',

#
# ./USRDIR/event/cev0617.har_EXTRACT/cev0617.evs
#
# [Text Only - No Designated Speaker]
"私は意識を向けた。▽\nここではない、私の現実へ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"…………………………………。\n\0":
'???',

# [Text Only - No Designated Speaker]
"…………………………………\n…………………………………。\n\0":
'???',

# [Text Only - No Designated Speaker]
"…………………………………\n…………………………………\n…………………………………。\n\0":
'???',

# Yui Ikari
"先生、これ以上は、\n肉体の維持に関わりますよ。\n\0":
'???',

# Kozo Fuyutsuki
"私は生命だ。\n生命そのものだよ。\n君と同じさ。\n\0":
'???',

# Yui Ikari
"もう、いいのですか？\n戻られないのですか？\n\0":
'???',

# (Decision Prompt)
"戻らない／戻る\0":
'???',

# Yui Ikari, Shinji Ikari
"そうですか。\n\0":
'???',

# Kozo Fuyutsuki
"教えてくれ。\n人はどうなっていくのだ。\n\0":
'???',

# Yui Ikari
"それはもう、\n先生は知っているはずです。\n\0":
'???',

# Kozo Fuyutsuki
"君の望んだ、人類の姿か？\n\0":
'???',

# Yui Ikari
"問いも答えも\n同じところにあります。▽\nでは、見に行きましょう。\n手を、どうぞ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女が私の手を取った。\n私は強く握り返した。▽\nどうして戻ろうなどと\n思えるだろうか。\n\0":
'???',

# Maya Ibuki, Female Staff
"副司令の服が、\nどうしてここに…？\n濡れてるわ…。\n\0":
'???',

# Maya Ibuki, Female Staff
"これ、この液体…、\nＬＣＬ！？▽\n副司令は…、副司令は…！？\n\0":
'???',

# [Text Only - No Designated Speaker]
"一瞬だけ、初号機の前に佇む\n冬月を見た者がいた。▽\n彼は、初号機へ手を伸ばし、\n次の瞬間には消えていたと言う。\n\0":
'???',

# [Text Only - No Designated Speaker]
"それが、最後の目撃となった。▽\nその後、冬月の姿を見る者は、\n誰もいなかった。\n\0":
'???',

# Yui Ikari
"いずれ会えます。\n先生達や、全ての人々が\nここを訪れるよう…待っています。\n\0":
'???',

# Kozo Fuyutsuki
"もう会えないのか！？\n\0":
'???',

# Yui Ikari
"強く生きてください。\n生きる事は、尊いのですから。\nいつでも、どこにあっても…。\n\0":
'???',

# Kozo Fuyutsuki
"ユイ君！\n\0":
'???',

# Yui Ikari
"その時まで、お元気で。\n先生…。\n\0":
'???',

# Kozo Fuyutsuki
"…ユイ君。\n\0":
'???',

# Kozo Fuyutsuki
"ああ、その時までの\nお別れだ…。\n\0":
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
# ./USRDIR/event/tev1803.har_EXTRACT/tev1803.evs
#
# Gendo Ikari
"我々に与えられた時間は少ない。\nだが、我らの願いを妨げる\nロンギヌスの槍は、既にないのだ。▽\n間もなく最後の使徒が現れるはずだ。\nそれを消せば願いがかなう。\nもうすぐだよ、ユイ。\n\0":
'???',

#
# ./USRDIR/event/cev0605.har_EXTRACT/cev0605.evs
#
# [Text Only - No Designated Speaker]
"彼女の論文を読み返す。\n私には、もはや習慣になっていた。▽\nふと思う。\n彼女は、どういった人類の未来を\n望んでいたのだろうか…。▽\n彼女の望んだ進化…。\n\0":
'???',

# Kozo Fuyutsuki
"あそこには…、京都には\n彼女の論文がいくつか残されては\nいないだろうか。▽\n京都か…。\n出張計画書が必要だな…。\n\0":
'???',

#
# ./USRDIR/event/tev1506.har_EXTRACT/tev1506.evs
#
# Ryoji Kaji
"ご無沙汰です。\n外の見張りには、\nしばらく眠ってもらいました。\n\0":
'???',

# Kozo Fuyutsuki
"いいのかね、\nこの行動は君の命取りになるぞ。\n\0":
'???',

# Ryoji Kaji
"ただ、\n真実に近づきたいだけなんです。\n僕の中のね。\n\0":
'???',

# Intelligence Agent
"ご協力、\nありがとうございました。\n\0":
'???',

# Misato Katsuragi 
"彼は？\n\0":
'What of him?\n\0',

# Intelligence Agent
"私は存じません。\n\0":
'???',

# Ryoji Kaji
"よぉ、遅かったじゃないか。\n\0":
'Yo. A little late, aren\'t you?\n\0',

#
# ./USRDIR/event/f088.har_EXTRACT/f088.evs
#
# Ritsuko Akagi 
"今、サード・チルドレンは\nどうしてるの？\n\0":
'???',

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
# ./USRDIR/btl/bevent.har_EXTRACT/d011.evs
#
# Toji Suzuhara 
"ぎゃあ！！\n\0":
'???',

#
# ./USRDIR/event/cev0707.har_EXTRACT/cev0707.evs
#
# Ritsuko Akagi 
"あら、お買い物？\n\0":
'???',

# Toji Suzuhara 
"リツコさん。\n\0":
'???',

# Kensuke Aida
"こんにちは。\nリツコさん、お仕事は？\n今日はもうＯＦＦなんですか？\n\0":
'???',

# Ritsuko Akagi 
"ほら、見て…。\nストッキング伝線して。\n\0":
'???',

# Ritsuko Akagi 
"気になって\n仕事どころじゃなくって…。\nストッキングを買いにきたの。\n\0":
'???',

# Ritsuko Akagi 
"あら、落としちゃった。\n僕達、取ってくれる？\n\0":
'???',

# Kensuke Aida
"俺が取るッ！！\n\0":
'???',

# Ritsuko Akagi 
"…あら、見えちゃう。\n\0":
'???',

# Ritsuko Akagi 
"あらら…ねえ？\n気絶までしなくても…。\n\0":
'???',

# Ritsuko Akagi 
"ま、いいわ。\nこれで許してあげる♪\n\0":
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
# ./USRDIR/event/b2s02.har_EXTRACT/b2s02.evs
#
# Shigeru Aoba, Male Staff
"エヴァ各機、体内電源０！\n活動限界です！\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le114.evs
#
# Shinji Ikari
"後悔しない人間なんて、\nいないはずだよ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"そう、普通はね。\n後悔があっても乗り越えられるから。▽\nでも、君は後悔のその先の一歩を、\n踏み出せずにいつまでも\n引きずっている。▽\n諦めが悪いね。\n\0":
'???',

# Shinji Ikari
"…状況を変えようなんて\n思わなくても、時間が解決するさ。▽\n人は痛みを忘れるように\n出来てるんだ。\n\0":
'???',

#
# ./USRDIR/event/tev0213.har_EXTRACT/tev0213.evs
#
# Misato Katsuragi 
"おはよう、シンジ君。\n今日も午後から\n戦闘シミュレーションがあるわ。▽\n時間になったら電話をするから、\nネルフ本部に来てちょうだいね。\n\0":
'???',

# Misato Katsuragi 
"そうそう、もう何度か\nシステムメニューに関して\n聞いてるでしょうけど。▽\nシステムメニューに関して\n捕捉しておくわね。\n\0":
'???',

# Shinji Ikari
"%4iボタンで開くメニュー、\nでしたよね…。\n\0":
'???',

# Misato Katsuragi 
"そうよ。▽\nシステムメニューのコマンドで、\n様々な機能を利用したり、\n情報を閲覧する事が出来るの。\n\0":
'???',

# Misato Katsuragi 
"「ステータス」と「人間関係」の\n見方は既に聞いているわね。▽\nここでの快適な生活、\n円滑な人間関係の為に\nちょくちょく確認してね。\n\0":
'???',

# Misato Katsuragi 
"この「機密情報」では、\nあなたが知りえた情報を\n閲覧する事が出来るの。▽\nま、ここの生活に慣れるまでは\nあまり首を突っ込まない事ね。\n\0":
'???',

# Misato Katsuragi 
"「チュートリアル」では、\n生活や戦闘などのガイダンスが\n説明されているの。▽\n今後わからない事があったら、\nプレイの方法とヒントを\n「チュートリアル」で確認してみて。\n\0":
'???',

# Misato Katsuragi 
"「オプション」では、\nゲームのプレイ環境を\n設定する事が出来るわ。▽\n快適にプレイ出来るように\nあなた好みにカスタマイズして。\n\0":
'???',

# Misato Katsuragi 
"「タイトル画面へ」を選ぶと\nゲームが中断されてタイトル画面に\n戻っちゃうから、注意してね。\n\0":
'???',

# Misato Katsuragi 
"そして、この「データセーブ」で\nゲームのセーブが出来るの。▽\n第３新東京市マップか、\nネルフ施設マップで\nセーブすることができるのよ。\n\0":
'???',

# Misato Katsuragi 
"ちなみに、ここでの生活のコツは\nΑΤとインパルスを高く保つ事よ。▽\nただし、ΑΤが高い時は\nインパルスは上がりにくくなるの。▽\n逆に、ΑΤが低いと\nインパルスはバンバン上がるわ。▽\nこの二つのパラメータを\nどのように保つかが\n悩みどころとなるわね。\n\0":
'???',

# Misato Katsuragi 
"んじゃ、説明はオワリ。\n戦闘シミュレーションの時間までは\n自由行動よ。▽\n２時頃に連絡するわね。\n\0":
'???',

#
# ./USRDIR/event/tev0214.har_EXTRACT/tev0214.evs
#
# Misato Katsuragi 
"もしもし、シンジ君？\n戦闘シミュレーションの\n準備がそろそろ終わるわ。▽\nブリーフィングルームで\n待ってるからね。\n\0":
'???',

# Shinji Ikari, Female Staff, Kaworu Nagisa, Toji Suzuhara
"わかりました。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le319.evs
#
# Rei Ayanami 
"消えたりしない。\n永遠に結びつく。\n\0":
'???',

# Rei's Shadow [Leliel]
"一つになりたいのね。\nその人と結びつくのが\nあなたの本当の目的なの？\n\0":
'???',

#
# ./USRDIR/event/cev0705.har_EXTRACT/cev0705.evs
#
# Shigeru Aoba
"…ごくっ。▽\nハイ…。\n\0":
'???',

# Shigeru Aoba
"あの、つきましたよ？\n\0":
'???',

# Ritsuko Akagi 
"ダメ、まだ。\n\0":
'???',

# Shigeru Aoba
"あのー、あのー。\n俺、ヤバいんですケド…。\n\0":
'???',

# Ritsuko Akagi 
"フフ、何が？▽\nヒール、脱がせてくれる？\n青葉君…。\n\0":
'???',

# Shigeru Aoba
"うおー！！\n\0":
'???',

# Ritsuko Akagi 
"がっついちゃって、もう…。\n\0":
'???',

# Ritsuko Akagi 
"青葉クン？\n\0":
'???',

# Shigeru Aoba
"何スか？\n\0":
'???',

# Ritsuko Akagi 
"ヒールのカカトが折れたの。\n抱っこしてくれる？\n\0":
'???',

# Shigeru Aoba
"えっ…！？\nえぇぇぇぇえ！？\n\0":
'???',

# Ritsuko Akagi 
"私の部屋までお願いね。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le409.evs
#
# Toji Suzuhara 
"それがどないしてん？\nなんか文句あるんか？\n\0":
'???',

# Toji's Shadow [Leliel]
"嘘の自分で接してるって事は、や。\nその人を騙してるんと同じ事やな。\n…なんも思わへんの？\n\0":
'???',

#
# ./USRDIR/event/f092.har_EXTRACT/f092.evs
#
# Ritsuko Akagi 
"アラ、シンジ君。\n\0":
'???',

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
'???',

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
# ./USRDIR/event/cev1308.har_EXTRACT/cev1308.evs
#
# Kensuke Aida
"…パパ。\n\0":
'???',

# Kensuke's Father
"あんなパイロットになんて、\nならない方が幸せなんだ。\n\0":
'???',

# Kensuke Aida
"でも、それじゃ俺の友達は\n不幸だって事！？▽\n一緒に戦って、\n助けてあげる事は出来ないの？\n\0":
'???',

# Kensuke's Father
"ケン坊！！\n何度言ったらわかるんだ。\nパパのパソコンを触るんじゃない。\n\0":
'???',

# Kensuke Aida
"…だって、パパ。\nパパは何も教えてくれない\nじゃないか。▽\nママは…、\nママは死んだ後どうなったの？▽\nエヴァのパーツになって\nしまったの？\nパパはそれを許したの？▽\nねえ、俺のクラスって\nパイロット候補の集まりなんだろ？\n教えてよ！！\n\0":
'???',

# Kensuke's Father
"…ケン坊、どこでそんな話を。\n\0":
'???',

# Kensuke Aida
"パパが教えてくれないから、\n自分で調べたんだ。\n\0":
'???',

# Kensuke's Father
"…ケン坊。\n\0":
'???',

# Kensuke Aida
"俺は、エヴァのパイロットに\nなりたいんだ。▽\n最初は…、格好いいからとか\n憧れだけだったけど。▽\nママの魂って奴を、ネルフは\nどうにかして持ってるんだ…。▽\n俺、ママを顔も知らない\n他人のモノにしておきたくなんか\nないんだよッ！\n\0":
'???',

# Kensuke's Father
"ママの事は仕方が無かったんだ。\n組織の中で拒否する事は\n許されなかった。▽\n人類が生存の道を勝ち取る為には\n他の手段は選べなかったんだ。▽\nママの死因は事故だ。\nそれは嘘じゃない。▽\nもう、助からないと判断された矢先、\n当時のネルフの研究機関にママを\n提供しなければならなかった…。\n\0":
'???',

# Kensuke's Father
"…ケン坊、\nパイロットにならずとも、\n支えてあげる事は出来るよ。▽\n諦めるんだ…。\n\0":
'???',

# Kensuke Aida
"だから、葬式の時に\n遺体がなかったの…？\n\0":
'???',

# Kensuke's Father
"そうだ…。▽\nそして、パパはお前が将来エヴァの\nパイロットになる可能性があると\n知らされた時…、▽\n心底、後悔したよ。▽\nもし、ケン坊がパイロットなんかに\nなったら…、命を落とすような事に\nなったらばと。\n\0":
'???',

# Kensuke Aida
"パパ…。\n\0":
'???',

# (Decision Prompt)
"諦める／諦めない\0":
'???',

# Kensuke's Father
"ずっと、後悔をしていた…。\nパパが悪いのさ。▽\n悪魔に妻の魂を売り渡したような\nものだからな。▽\nこうして怯えて暮らさなければ\nならないのは…、結局自分で\n引き起こした事なのだから。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le117.evs
#
# Shinji Ikari
"そんな…、嫌だよ！\n心を覗かれるなんて。\n\0":
'???',

# Shinji's Shadow [Leliel]
"心の中を知られると、\n嫌われるかもしれない。\nそういう思いが君の中にあるわけだ。▽\n他人が自分を傷つけるとばかり\n思ってるけど、どうかな？▽\n自分もまた、他人を傷つける事に\nなるかもしれないんだ。\n\0":
'???',

#
# ./USRDIR/event/tev0504.har_EXTRACT/tev0504.evs
#
# Ritsuko Akagi 
"アレの資料よ。\n簡単に目を通しておいて。\n予定通りに近々やるそうよ。\n\0":
'???',

# Misato Katsuragi 
"わかったわ。\n\0":
'???',

# Misato Katsuragi 
"あ、あぁ…シンジ君ね。\nどうしたの？\n\0":
'???',

# Shinji Ikari
"いえ、\n特に用はないんですけど。▽\n何か…あったんですか？\n\0":
'???',

# Misato Katsuragi 
"んー、仕事の話。\nチョッチ、出張が入る予定なの。\n\0":
'???',

# Shinji Ikari
"へえ、大変…なんですね。\n\0":
'???',

# Shinji Ikari
"（仕事をしてるミサトさん…。\n　家とは…違う顔だ。）\n\0":
'???',

#
# ./USRDIR/event/cev0401.har_EXTRACT/cev0401.evs
#
# Misato Katsuragi 
"私は葛城ミサト。▽\n特務機関ネルフ、\n戦術作戦部作戦局第一課所属。\n\0":
'???',

# Misato Katsuragi 
"セカンドインパクトで父を亡くし、\nそしてまた、１５年ぶりに襲来した\n使徒を討つべくネルフに入所した。\n\0":
'???',

# Misato Katsuragi 
"駄目よ、逃げちゃ。\nお父さんからも…、\n何よりも自分から。\n\0":
'???',

# Misato Katsuragi 
"かまいませんね？\n\0":
'???',

# Kozo Fuyutsuki
"………１５年ぶりだな。\n\0":
'???',

# Gendo Ikari
"ああ、まちがいない。\n使徒だ。\n\0":
'???',

# Misato Katsuragi 
"私の戦いが、始まる…。\n\0":
'???',

# Gendo Ikari
"もちろんだ、\n使徒を倒さぬ限り、我々に\n未来はない。\n\0":
'???',

# Misato Katsuragi 
"碇シンジ君ね。\nごめん、お待たせ！！\n\0":
'???',

# Shinji Ikari
"…あ、あ、あ、あの。\n\0":
'???',

# Misato Katsuragi 
"私はミサト、葛城ミサト。\nあなたを迎えに来たの。\n乗って！！\n\0":
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
# ./USRDIR/event/f033.har_EXTRACT/f033.evs
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
# ./USRDIR/event/cev1006.har_EXTRACT/cev1006.evs
#
# Shigeru Aoba
"結構、被害出てるなぁ…。\n\0":
'???',

# Kozo Fuyutsuki
"まるで他人事だな…。\n\0":
'???',

# Kozo Fuyutsuki
"最近の君はたるんどるな。\n君はもう少し、優秀だと思ったが。\n\0":
'???',

# Shigeru Aoba, Misato Katsuragi 
"申し訳ありません。\n\0":
'???',

# Kozo Fuyutsuki
"しばらく休みなしのつもりで\n仕事をしたまえ。\n\0":
'???',

#
# ./USRDIR/event/tev0403.har_EXTRACT/tev0403.evs
#
# [Text Only - No Designated Speaker]
"レイのＩＤカードを受け取った。\n\0":
'???',

# Ritsuko Akagi 
"何かしら…、シンジ君。\n\0":
'???',

# Shinji Ikari
"父さんの…、手の火傷の事\nなんですけど…。\n\0":
'???',

# Ritsuko Akagi 
"ああ、あれね…。\n気になるの？\n\0":
'???',

# Shinji Ikari
"あの、僕はただ…。\n\0":
'???',

# Ritsuko Akagi 
"あなたがここに来る前に、\n零号機の起動実験があってね。\n\0":
'???',

# Shinji Ikari
"零号機…。\nあの、綾波の…。\n\0":
'???',

# Ritsuko Akagi 
"ところがね、実験中に\n零号機が暴走してね…。\n\0":
'???',

# Ritsuko Akagi 
"パイロットが入っている\nエントリープラグを強制射出\nしたんだけれどハッチが開かなくて。\n\0":
'???',

# Ritsuko Akagi 
"碇司令が、過熱したハッチを\n無理矢理素手でこじ開けたの。\n彼女を助けるために。\n\0":
'???',

# Shinji Ikari
"火傷は…、\nその時に出来た…。▽\n彼女って、やっぱり…、\n綾波ですか？\n\0":
'???',

# Ritsuko Akagi 
"…………………。\nそうよ。\n\0":
'???',

# Shinji Ikari
"……………………。\nそうですか、\nありがとうございました。\n\0":
'???',

# Ritsuko Akagi 
"あ、シンジ君。\nこれをレイに渡してくれる？▽\nレイのＩＤカードよ。\n\0":
'???',

# Shinji Ikari
"僕が、渡すんですか？\n僕、彼女の事何も知らなくて…。▽\n同じエヴァのパイロットという\n事しか…。\n\0":
'???',

# Ritsuko Akagi 
"レイは、いい子よ。\nあなたのお父さんに似て、\nとても不器用だけど。\n\0":
'???',

# Shinji Ikari
"不器用って…何がですか？\n\0":
'???',

# Ritsuko Akagi 
"生きる事が、よ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le412.evs
#
# Toji Suzuhara 
"そんなんしゃあないやん。\n必要な事や。\n\0":
'???',

# Toji's Shadow [Leliel]
"せやから、今さら辞められへん。\nもう、ジャージは脱がれへんねや。\n\0":
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

#
# ./USRDIR/event/tev0277.har_EXTRACT/tev0277.evs
#
# Misato Katsuragi 
"チョッチ、散らかってるけど。\n私の部屋よ。▽\nまあ、ほとんど寝る為だけの\n部屋だけどね。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le104.evs
#
# Shinji Ikari
"僕ばっかりが悪くは無い。\n悪くなくても、\n嫌われる時はあるんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"そうやって、\n他人と距離をおこうとしている。\n楽だからね、傷つかなくていいから。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le510.evs
#
# Kaworu Nagisa 
"フフ、そんなつもりはないよ。\nあくまで協力しているだけさ。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"そうは見えないよ。▽\nこのまま行くと\n自分がどうなるのか…、\n知らないワケじゃないだろう？\n\0":
'???',

#
# ./USRDIR/event/tev0208.har_EXTRACT/tev0208.evs
#
# Misato Katsuragi 
"リツコ。\n\0":
'???',

# Ritsuko Akagi 
"あら、シンジ君が一緒なのね。\n\0":
'???',

# Misato Katsuragi 
"お邪魔だったかしら？\n\0":
'???',

# Ritsuko Akagi 
"構わないわ。▽\nよろしく、シンジ君。\n私は、赤木リツコ。▽\nネルフ本部技術開発部\n技術局一課所属よ。\n\0":
'???',

# Shinji Ikari
"あ、碇シンジです。\nよろしく…。\n\0":
'???',

# Ritsuko Akagi 
"あの後、お父さんとは\n会ったのかしら？\n\0":
'???',

# Misato Katsuragi 
"それがねー、\n司令を探してるんだけど\nどこにもいないのよね。\n\0":
'???',

# Ritsuko Akagi 
"じゃあ、病院ね。\nレイのところだわ。\n\0":
'???',

# Misato Katsuragi 
"あちゃー、行き違いか。\n\0":
'???',

# Shinji Ikari
"いいんです。\n父とはずっと、\n別々に暮らしていたし。▽\nどう関わっていいか、\n僕もわかりませんし。\n\0":
'???',

# Misato Katsuragi, Hikari Horaki, Rei Ayanami
"そう…。\n\0":
'???',

# Ritsuko Akagi 
"じゃあ、あなたには\n人間関係というものを\n教えてあげるわ。▽\n自分が相手をどう思っているか、\n相手が自分をどう思っているか、\n人間関係は関心と好意で決まるわ。▽\n関心は、相手への心の距離。\n好意は、相手への好き嫌い。▽\n二つとも、コミュニケーションに\nよって、変化していくのよ。▽\n誰かと会話をした後など、\n人間関係がどのように変化したのか\n結果が表示されるから参考にして。▽\nちなみにシステムメニューでも\n人間関係を確認する事が出来るの。\n\0":
'???',

# Ritsuko Akagi 
"ためしに、シンジ君とミサトの\n人間関係で説明しましょう。\n\0":
'???',

# Ritsuko Akagi 
"これが人間関係を表すグラフ…、\n関心と好意から構成される表よ。▽\n左側にシンジ君から\nミサトに対する評価が表示されて、▽\n右側にミサトから\nシンジ君への評価が表示されて\nいるわよね。\n\0":
'???',

# Ritsuko Akagi 
"互いの距離が近いと、\n互いに関心が高い状態。\n\0":
'???',

# Ritsuko Akagi 
"互いの距離が離れていると、\n互いに無関心な状態。\n\0":
'???',

# Ritsuko Akagi 
"片方のみが近づいていると\n関心は一方的なものになるわ。▽\nこの例ではミサトがシンジ君を\n一方的に気にかけている事に\nなるわね。\n\0":
'???',

# Ritsuko Akagi 
"上方向にあるほど好意が高い。\nお互い高ければ、仲がいい状態ね。\n\0":
'???',

# Ritsuko Akagi 
"下方向にあるほど好意が低い。\nこうなっちゃうと、\nお互い憎みあっている状態よ。\n\0":
'???',

# Ritsuko Akagi 
"中央に近いほど、\n好意はニュートラルな状態となるわ。\n好きでも嫌いでもない普通な関係ね。\n\0":
'???',

# Ritsuko Akagi 
"この人間関係は、\nお互いの行動で大きく変動し、\n時間の経過でも次第に変化するの。\n\0":
'???',

# Ritsuko Akagi 
"ところで、ミサト。\n彼の部屋へは案内したの？\n\0":
'???',

# Misato Katsuragi 
"碇司令と同居でしょ？\n\0":
'???',

# Ritsuko Akagi 
"彼の個室は用意してあるわよ。\n\0":
'???',

# Misato Katsuragi 
"シンジ君、\nお父さんと一緒じゃなくても\nいいの？\n\0":
'???',

# Shinji Ikari
"いいんです。\n父は、僕に会いたくて\n呼んだわけじゃないみたいですし。\n\0":
'???',

# Misato Katsuragi 
"……………。▽\nじゃあ、私と一緒に…住む？\n\0":
'???',

# Ritsuko Akagi 
"な、何言ってるのよ！\n葛城一尉！\n\0":
'???',

# Misato Katsuragi 
"だーって、まだ中学生なんだし、\n保護者が必要じゃない？\n\0":
'???',

# Ritsuko Akagi 
"そういう問題じゃないでしょ？\n\0":
'???',

# Misato Katsuragi 
"司令には私が許可を\n取っておくわよ。\n\0":
'???',

# Ritsuko Akagi, Asuka Soryu Langley
"ミサト！\n\0":
'???',

# Misato Katsuragi 
"中学生に手を出すほど\n飢えてないわよ！\nじゃあね〜ン♪▽\nさ、今日はもう上がるわ。\n帰りましょ、シンジ君。\n\0":
'???',

# Shinji Ikari
"ちょっ…、ちょっと。\nミサトさん！！\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le108.evs
#
# Shinji Ikari
"自分を大事にしてやれるのは、\n自分しかいないんだ！\n自分を守って何が悪い！\n\0":
'???',

# Shinji's Shadow [Leliel]
"本音が出たね。\n\0":
'???',

# Shinji Ikari
"誰も、誰も守ってくれないもの！\n\0":
'???',

# Shinji's Shadow [Leliel]
"責任転嫁かい？\n\0":
'???',

#
# ./USRDIR/event/b2s16.har_EXTRACT/b2s16.evs
#
# Shigeru Aoba, Male Staff
"零号機、投てき体勢。\n\0":
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
# ./USRDIR/event/cev1102.har_EXTRACT/cev1102.evs
#
# Ryoji Kaji
"必要なのは特殊偽造ＩＤ…。\nこれは自前で作成するか。▽\nあとは副司令や碇司令が持つ\nＩＤをどう入手するかだな。▽\n必要な情報は、\nここで全て手に入るだろう。▽\n真実はネルフにあるはずだ…。\n\0":
'???',

#
# ./USRDIR/event/cev0801.har_EXTRACT/cev0801.evs
#
# [Text Only - No Designated Speaker]
"世界は残酷だ。\n触れたくない、見たくないもの\nばかりが溢れてる。▽\n毒でいっぱい。\n溺れてしまわない様に\n自分は自分で守り抜くの。▽\n触れたくないものに\n触れないでいい様に。▽\n見たくないものを\n見なくてもいい様に。▽\nだから、私には何もない。▽\nがむしゃらに、\n勉強をやっていただけ。▽\nでも、それでよかったの。\n認めてくれる人がいたから。\n\0":
'???',

# [Text Only - No Designated Speaker]
"認めてくれたのは、\nセンパイだけだった。▽\nでも、空っぽな私にあるのは\n有能なオペレーターという価値だけ。▽\n頑張るしかない。\n頑張り続けるしかない。\n私の存在価値はそれしかないの。\n\0":
'???',

# [Text Only - No Designated Speaker]
"寂しい、寂しい。\n寂しくて、おかしくなりそう。▽\nだから、食べるの。\n空っぽの私を埋め尽くす様に。▽\n苦しい、苦しい。\n誰も助けてくれないから、\n私一人でどうにかするの。\n\0":
'???',

# Maya Ibuki 
"…う、…ごほっ。\nごほっ………………。\n\0":
'???',

# Maya Ibuki 
"…はぁ、…はぁ…はぁ。▽\n…………………………。▽\nもう、これっきりだって\n決めたのに。\n\0":
'???',

# [Text Only - No Designated Speaker]
"いつも食べて、吐いて、\nまた空しくなって。\nずっと、その繰り返し。\n\0":
'???',

# Maya Ibuki 
"行かなきゃ…。\n何事もなかったように。▽\n行かなきゃ…、\nあの場所がなくなったら\n私は何もなくなってしまう。\n\0":
'???',

#
# ./USRDIR/event/cev1414.har_EXTRACT/cev1414.evs
#
# Hikari Horaki
"鈴原、欠席なんだ…。\nせっかくお弁当作ってきたのにな。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le130.evs
#
# Shinji Ikari
"他人と上手くやっていくには、\nそうするしかないんだ。▽\n傷つけるつもりも無い。\n相手を不快にさせない為に\nやってるんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"自分でも、そういう行為を\n冷めた目で見てるんじゃない？▽\n計算高い自分に\nどこかで気付いてるハズだよ。\n\0":
'???',

#
# ./USRDIR/event/tev0101.har_EXTRACT/tev0101.evs
#
# Evacuation Announcement
"本日１２時３０分。▽\n\0":
'???',

# Evacuation Announcement
"東海地方を中心とした関東、\n中部全域に特別非常事態宣言が\n発令されました。▽\n\0":
'???',

# Evacuation Announcement
"住民の方々は速やかに指定の\nシェルターへ避難してください。\n繰り返しお伝えします。\n\0":
'???',

# Emergency Phone Announcement
"特別非常事態宣言発令のため、\n現在、全ての回線は\n不通となっております。\n\0":
'???',

# Shinji Ikari
"やっぱり、来るんじゃなかった。\n\0":
'???',

# Shinji Ikari
"駄目か…。\n待ち合わせは無理か。▽\nしょうがない、\nシェルターに行こう。\n\0":
'???',

# Shinji Ikari
"な…んだ、あれ…？\n\0":
'???',

# Kozo Fuyutsuki
"………１５年ぶりだね。\n\0":
'???',

# Shinji Ikari
"特務機関、ネルフ？\n\0":
'???',

# Misato Katsuragi 
"そう、国連直属の非公開組織。\n\0":
'???',

# Shinji Ikari
"父のいるところですね。\n\0":
'???',

# Misato Katsuragi 
"まぁね。\nお父さんの仕事、知ってる？\n\0":
'???',

# Shinji Ikari
"人類を守る大事な仕事だと、\n聞いてはいます…。\n\0":
'???',

# Shinji Ikari
"これから父のところへ\n行くんですか？\n\0":
'???',

# Misato Katsuragi 
"そうね、そうなるわね。\n何か聞いてる？\n\0":
'???',

# Shinji Ikari
"父から聞いているのは、\n用がある…とだけ…。\n\0":
'???',

# Gendo Ikari
"では、後を頼む。\n\0":
'???',

# Kozo Fuyutsuki, Shigeru Aoba, Gendo Ikari, Ryoji Kaji
"ああ。\n\0":
'???',

# Kozo Fuyutsuki
"３年ぶりの、\n親子の対面か…。\n\0":
'???',

# Misato Katsuragi 
"着いたわよ、シンジ君。\n\0":
'???',

# Shinji Ikari
"顔…巨大ロボット？\n\0":
'The face... of a giant robot?\n\0',

# Misato Katsuragi 
"人の作り出した究極の汎用決戦兵器。\n人造人間エヴァンゲリオン。\nその初号機。▽\n建造は極秘裏に行われた。\n我々人類の最後の切り札よ。\n\0":
'???',

# Shinji Ikari
"これも父の仕事ですか？\n\0":
'???',

# Gendo Ikari
"そうだ。\n\0":
'Correct.\n\0',

# Gendo Ikari
"久しぶりだな。\n\0":
'It\'s been a while.\n\0',

# Gendo Ikari
"乗れ。\n出撃だ。\n\0":
'???',

# Shinji Ikari
"…！？▽\n父さん…用って、\nこのために僕を呼んだの？▽\n僕がこれに乗って、\nさっきのと戦えっていうの！？\n\0":
'???',

# Gendo Ikari
"乗るなら早くしろ。\nでなければ帰れ！\n\0":
'???',

# Shinji Ikari
"無理だよ、そんなの！\nこんなの…乗れるわけないよ！\n\0":
'???',

# Gendo Ikari, Misato Katsuragi 
"レイ。\n\0":
'Rei.',

# Gendo Ikari
"予備が使えなくなった。\nもう一度だ。\n\0":
'???',

# Misato Katsuragi 
"駄目よ、逃げちゃ。\nお父さんから…何よりも自分から。\n\0":
'???',

# Shinji Ikari
"逃げちゃ駄目だ。\n逃げちゃ駄目だ。\n逃げちゃ駄目だ………！\n\0":
'I mustn\'t run away.\n I mustn\'t run away.\n I mustn\'t run away...!\n\0',

# Shinji Ikari
"やります。\n僕が乗ります！\n\0":
'I\'ll do it.\n I\'ll pilot it!\n\0',

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
# ./USRDIR/event/b2s21.har_EXTRACT/b2s21.evs
#
# Shinji Ikari
"わぁぁぁぁぁっ！！\n行かないで、捨てないで！！\n父さん、父さん！！\n\0":
'???',

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
'???',

# Asuka Soryu Langley
"ママ！！　やめて！！\nお願いだから私を殺さないで！！\n\0":
'???',

# Asuka Soryu Langley
"イヤ！\n私はママの人形じゃない！！\n\0":
'???',

# Asuka Soryu Langley
"ママ！　ママ！！\nこっちを向いて！！\n私はここなのに！！\n\0":
'???',

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
'???',

# Kaworu Nagisa 
"やめろ、僕をどうするつもりだ！\n計画なんか知らない！！\nそんなもの押し付けないでくれ！\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le210.evs
#
# Asuka Soryu Langley
"一人になるのは他人のせい？\n\0":
'???',

# Asuka's Shadow [Leliel]
"あなたと、あなたの中の他人。\n他人はみんな\nあなたの孤独に気がつけない。\n\0":
'???',

#
# ./USRDIR/event/tev0404.har_EXTRACT/tev0404.evs
#
# [Text Only - No Designated Speaker]
"留守なのだろうか、\nレイの姿はない。▽\n年頃の少女が生活するにしては、\n余りにも殺風景だった。▽\nふと目にしたテーブルの上には、\nレンズにヒビの入った眼鏡がある。\n\0":
'???',

# Shinji Ikari
"眼鏡…？\n綾波の…じゃないよな？\n\0":
'???',

# [Text Only - No Designated Speaker]
"眼鏡を手に取り、かけてみる。\n\0":
'???',

# [Text Only - No Designated Speaker]
"玄関の方で人の気配がした。\n足音がこちらに近づいてくる。\n\0":
'???',

# Rei Ayanami 
"碇君…？\n\0":
'???',

# Shinji Ikari
"あ、綾波…。\n\0":
'???',

# Rei Ayanami 
"それに触らないで。\n\0":
'???',

# [Text Only - No Designated Speaker]
"レイは、強引に奪うように\n眼鏡を取り上げた。\nそのまま、静かにケースへ戻す。\n\0":
'???',

# Shinji Ikari
"あの…、リツコさんから\n新しいＩＤカードを渡すように\n頼まれて…。▽\n届けに来たんだけど…、その、\n返事はないし、鍵は開いてたから…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"シンジは、冷や汗を\nどっと噴出しながら、\nレイにＩＤカードを差し出した。▽\n冷たく、没収するように\nレイが受け取る。\n\0":
'???',

# Shinji Ikari
"大事なものだったんだ、\nその眼鏡…。\nでも、綾波のじゃないよね…。▽\n…………………誰…の？\n\0":
'???',

# Rei Ayanami 
"碇司令。\n\0":
'???',

# Shinji Ikari
"でも、綾波もあれに…、\nエヴァに乗せられてるんだろ？\n怖くないの？\n\0":
'???',

# Rei Ayanami, Asuka Soryu Langley, Kaworu Nagisa
"どうして？\n\0":
'???',

# Shinji Ikari
"あんな…、大怪我までして。\n起動実験の時だって…。\n\0":
'???',

# Rei Ayanami 
"あなた、碇司令の子供でしょ？\n\0":
'???',

# Rei Ayanami 
"信じられないの？\nお父さんの仕事が。\n\0":
'???',

# Shinji Ikari
"当たり前だよ、\nあんな父親。\n\0":
'???',

# [Text Only - No Designated Speaker]
"レイに平手打ちを食わされ、\n呆然とするシンジ。▽\n先程の眼鏡を手に、\nレイは家から出ていった。\n\0":
'???',

#
# ./USRDIR/event/f065.har_EXTRACT/f065.evs
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
'???',

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
# ./USRDIR/event/tev1103.har_EXTRACT/tev1103.evs
#
# Shigeru Aoba
"おや、\n第８７タンパク壁に変質部分が…。\n\0":
'???',

# Shigeru Aoba
"…えっ、これは。\n\0":
'???',

# Ritsuko Akagi 
"何？\n一体どうしたの？\n\0":
'???',

# Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Female Staff
"第８７タンパク壁が\n劣化発熱しています！！\n\0":
'???',

# Ritsuko Akagi 
"何ですって…。\nすぐに、原因を探って！\n\0":
'???',

# Shigeru Aoba
"侵食部が爆発的なスピードで、\n増殖していきます！▽\nこれは…、▽\n何てこった、分析パターン青。\n使徒です！！\n\0":
'???',

# Kozo Fuyutsuki
"使徒…、\n使徒の侵入を許したのか！？\n\0":
'???',

# Kozo Fuyutsuki
"言い訳はいい。▽\nセントラルドグマを物理閉鎖！\nシグマユニットを隔離しろ。\n\0":
'???',

# Shigeru Aoba
"汚染域、さらに拡大。▽\n待って下さい、\nサブ・コンピュータが\nハックされています！▽\nくそ、こんな時に誰が…。\n\0":
'???',

# Shigeru Aoba
"………まさか！？▽\n使徒です、このままマギに\n侵入しようとしています！！\n\0":
'???',

# Ritsuko Akagi 
"彼らはマイクロマシーン、\n細菌サイズの使徒と考えられるわ。▽\nその個体が集まって群れを作り、\nこの短時間で知能回路の形成に\n至るまで、▽\n爆発的な進化を遂げているのよ。\n\0":
'???',

# Shigeru Aoba
"ウワッ！？\n人工知能メルキオールにより\n自律自爆が提訴されました！！▽\nバルタザールにより、否決。\nカスパーにより、否決。\n\0":
'???',

# Shigeru Aoba, Makoto Hyuga, Maya Ibuki 
"しかし、このままでは６時間後には\nマギの機能が乗っ取られます！\n\0":
'???',

# Gendo Ikari
"マギが敵にまわるとはな。\n\0":
'???',

# Misato Katsuragi 
"マギシステムの物理的消去を\n提案します。\n\0":
'???',

# Ritsuko Akagi 
"無理よ。\nマギを切り捨てる事は、\n本部の破棄と同義なのよ。\n\0":
'???',

# Misato Katsuragi 
"では、作戦部から正式に要請するわ。\n\0":
'???',

# Ritsuko Akagi 
"拒否します。\n技術部が解決すべき問題です。\n\0":
'???',

# Misato Katsuragi 
"あなた昔っからそう。\n一人で全部抱え込んで。\n他人を当てにしないのね。\n\0":
'???',

# Ritsuko Akagi 
"勝算はあるわ。▽\n目標がコンピュータそのものなら、\n逆ハックをしかけて自滅促進\nプログラムを送り込む事が出来ます。\n\0":
'???',

# Misato Katsuragi 
"そのプログラム、\n間に合うんでしょうね？▽\nカスパーまで侵されたら、\n終わりなのよ。\n\0":
'???',

# Ritsuko Akagi 
"約束は守るわよ。\n\0":
'???',

# Gendo Ikari, Kozo Fuyutsuki
"君が早いか、使徒が早いか、\n勝負だな…。\n\0":
'???',

# Shinji Ikari
"どうしよう…。\n何かとんでもない事になってる…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"使徒、イロウルとの戦闘中のため、\nデータセーブは行えません。\n\0":
'???',

#
# ./USRDIR/event/tev1305.har_EXTRACT/tev1305.evs
#
# Gendo Ikari
"食事にしよう。\n\0":
'Let\'s eat.\n\0',

# Ritsuko Akagi 
"試作された、ダミープラグです。\nレイの人格が移植されています。▽\nただ、人の心…魂はデジタル化\n出来ません。▽\nあくまでフェイク。\n擬似的なものに過ぎません。▽\nパイロットの思考のマネをする\nただの機械です。\n\0":
'???',

# Gendo Ikari
"信号パターンをエヴァに送り込む。\nエヴァがそこにパイロットがいると\n思い込み、シンクロさえすればいい。▽\n初号機と弐号機には、\nデータを入れておけ。\n\0":
'???',

# Ritsuko Akagi 
"まだ問題が残っていますが。\n\0":
'???',

# Gendo Ikari
"構わん。\nエヴァが動けばいい。\n\0":
'???',

# Gendo Ikari
"参号機の搬送はＵＮに一任してある。\nじき届くだろう。\nあとは君の方でやってくれ。\n\0":
'???',

# Ritsuko Akagi 
"はい。\n調整ならびに起動試験は、\n松代で行います。\n\0":
'???',

# Gendo Ikari
"テストパイロットはどうする。\n\0":
'???',

# Ritsuko Akagi 
"ダミープラグは、まだ危険です。\n今の候補者の中から…、\n\0":
'???',

# Gendo Ikari
"４人目を選ぶか。\n\0":
'???',

# Ritsuko Akagi 
"はい。\n一人速やかに「コア」の準備が\n可能な子供がいます。\n\0":
'???',

# Gendo Ikari
"任せる。\n\0":
'???',

# Gendo Ikari
"上がっていいぞ。\n\0":
'???',

#
# ./USRDIR/event/bs082.har_EXTRACT/bs082.evs
#
# Kozo Fuyutsuki
"よろしい。\nでは次に、使徒の動きについてだ。▽\n君は常に次の使徒の位置を\n読まなければならない。\nこれが君の重要な仕事だ。▽\n使徒の動きを読み、状況に応じた\n指示を心がけてもらいたい。\n\0":
'???',

#
# ./USRDIR/event/tev0802.har_EXTRACT/tev0802.evs
#
# Toji Suzuhara 
"いやー、\nとうとう明日は修学旅行や。▽\nシンジ、お前の分まで楽しんで\nきたるさかいな！\n\0":
'???',

# Kensuke Aida
"残念だよなぁ。▽\nまあ、人類の平和を担う\nエヴァのパイロットだもん。\nしょうがないよな！\n\0":
'???',

# Hikari Horaki
"お土産、買ってくるから。\n楽しみにしててね。\n\0":
'???',

# Toji Suzuhara 
"ほな、おやつ買いにいこ。\nお先するで、お二人さん。\n\0":
'???',

# Asuka Soryu Langley
"いいなぁ…。\n\0":
'???',

# Shinji Ikari
"しょうがないよ。\n待機命令が出てるんだもの。\n\0":
'???',

# Asuka Soryu Langley
"まーぁ、いい子ちゃんだこと。\nヘドが出そう。▽\nところでアンタ、何やってるの？\n\0":
'???',

# Shinji Ikari
"理科の勉強だよ。\n遅れた分、取り戻さなきゃ。\n\0":
'???',

# Asuka Soryu Langley
"ふーん、\nこんな数式に戸惑ってるの？\nちょっと貸して。\n\0":
'???',

# [Text Only - No Designated Speaker]
"アスカが、鉛筆を取り上げ\nいとも簡単に数式を解いていく。▽\n迷いなく進む筆を、\nシンジは呆気に取られながら\n見ていた。\n\0":
'???',

# Shinji Ikari
"これ、かなり難しい問題だよ。\nこんなの出来て、どうして\nテストが出来ないの？\n\0":
'???',

# Asuka Soryu Langley
"漢字、上手く読めないし。\n設問がわからないんだもん。▽\n大学で日本語なんて\n教わらなかったし。\n\0":
'???',

# Shinji Ikari
"大学？\n\0":
'College?\n\0',

# Asuka Soryu Langley
"そ、去年卒業したのよね。\nあ、コレ何て読むの？\n\0":
'???',

# Shinji Ikari
"え、あ…コレは、\n熱膨張に関する問題で…。\n\0":
'???',

# Asuka Soryu Langley
"熱膨張？\n幼稚な事やってるのね。▽\n単純じゃない。\n物ってのは、温めれば膨らんで\n大きくなるし、▽\n冷やせば縮んで小さくなるって\n事じゃない。\n\0":
'???',

# Shinji Ikari
"まあ、そう…だね。\n\0":
'???',

# Asuka Soryu Langley
"もっとシンプルに考えりゃ、\n物事ってそんなに複雑じゃ\nないわよ。\n\0":
'???',

# Shinji Ikari
"…簡単に言うね。\n\0":
'???',

# Asuka Soryu Langley
"ほーらー。\nそうやっていつも、\n考えなくていい事ばかり考える。▽\n自分の事だけ、\n考えられるようになれば、\n少しはオツムもよくなるかもよ？\n\0":
'???',

# Shinji Ikari
"アスカはそうなの？\n\0":
'???',

# Asuka Soryu Langley
"アンタみたいに、\n人に気を遣うヒマがあったらって、\nその程度よ。\n\0":
'???',

#
# ./USRDIR/event/cev1210.har_EXTRACT/cev1210.evs
#
# Makoto Hyuga, Shigeru Aoba, Maya Ibuki, Female Staff
"先程、第２東京から\nＡ−８０１が出ました。▽\n特務機関ネルフの特例による\n法的保護の破棄。▽\n及び指揮権の日本国政府への\n委譲です。\n\0":
'???',

# Kozo Fuyutsuki, Gendo Ikari, Misato Katsuragi, Ryoji Kaji, Male Staff
"やはり人間の敵は、\n同じ人間だったか…。\n\0":
'???',

# Makoto Hyuga,Shigeru Aoba
"人間の敵は、\n同じ人間って事だったのか…。\n\0":
'???',

# Maya Ibuki 
"人間の敵は、\n同じ人間って事なの…。\n\0":
'???',

# Ritsuko Akagi 
"やはり人間の敵は、\n同じ人間だったようね…。\n\0":
'???',

# Toji Suzuhara 
"な、何や、火事かいな。\n何が起こってるんや！？\n\0":
'???',

# JSSDF Staff
"いたぞ、\nエヴァ搭乗パイロットだ。\n\0":
'???',

# Toji Suzuhara 
"………ひっ！？\n\0":
'???',

# JSSDF Staff
"これより、排除する。▽\n…悪く思うなよ。\n\0":
'???',

# Toji Suzuhara 
"あ、あれ、どうもあらへん…。\n生きてる…。\n\0":
'???',

# Misato Katsuragi 
"待たせたわね。\n\0":
'???',

# Ritsuko Akagi 
"ぐずぐずしないで、\n行くわよ。\n\0":
'???',

# Makoto Hyuga
"大丈夫？\n怪我はないかい？\n\0":
'???',

# Shigeru Aoba
"ごめん、遅くなった。\n\0":
'???',

# Maya Ibuki 
"無事だったのね、\nここは危険よ、走って！！\n\0":
'???',

# Toji Suzuhara , Hikari Horaki, Shinji Ikari, Kaworu Nagisa
"ミサトさん…。\n\0":
'Misato-san\n\0',

# Toji Suzuhara , Shinji Ikari, Asuka Soryu Langley, Kaworu Nagisa
"リツコさん…。\n\0":
'Ritsuko-san...\n\0',

# Toji Suzuhara , Shinji Ikari, Asuka Soryu Langley, Kaworu Nagisa
"日向さん…。\n\0":
'Hyuga-san\n\0',

# Toji Suzuhara , Shinji Ikari, Asuka Soryu Langley, Kaworu Nagisa
"青葉さん…。\n\0":
'Aoba-san\n\0',

# Toji Suzuhara , Shinji Ikari, Asuka Soryu Langley, Kaworu Nagisa
"マヤさん…。\n\0":
'Maya-san...\n\0',

# Misato Katsuragi 
"戦略自衛隊が\nここを占拠するために\n侵攻してきたのよ。▽\n発令所まで戻りましょう、\nちょっと待ってね。\n\0":
'???',

# Misato Katsuragi 
"こちら葛城、パイロットに接触。\nただ今より、帰還します。▽\n………。▽\n何…、何ですって…！！\n\0":
'???',

# Ritsuko Akagi 
"戦略自衛隊が、ここを\n占拠するために侵攻してきたのよ。\nここも危ないわ…。▽\n発令所に戻るわよ、\nちょっと待ってなさい。\n\0":
'???',

# Ritsuko Akagi 
"私よ、パイロットを無事保護したわ。\n帰り道を案内して欲しいの。\n………。▽\n何ですって…！！\n\0":
'???',

# Makoto Hyuga
"戦略自衛隊が\nここを占拠するために\n侵攻してきたんだ。▽\nとにかく発令所まで戻ろう。\nちょっと待って…。\n\0":
'???',

# Makoto Hyuga
"日向です、パイロットと接触。\nただ今より帰還します。\n………。▽\nそいつは本当か…！！\n\0":
'???',

# Shigeru Aoba
"戦略自衛隊が\nここを占拠するために\n侵攻してきやがったんだ。▽\n発令所へ急ごう。\nちょっと待ってな…。\n\0":
'???',

# Shigeru Aoba
"青葉です、パイロットを保護。\n今からそちらに向かいます。\n………。▽\n何…、確かなのか…！！\n\0":
'???',

# Maya Ibuki 
"戦略自衛隊が、ここを\n占拠するために侵攻してきたの。\nあちこちで交戦してるわ。▽\n行きましょう、発令所に。\nちょっと連絡するから待っててね。\n\0":
'???',

# Maya Ibuki 
"伊吹です、ただ今より帰還します。\nええ、パイロットも一緒です。\n………。▽\n何ですって…、それじゃ…！！\n\0":
'???',

# Female Staff
"ええ、全部で９機。\nエヴァ量産機、エヴァシリーズです。\nただ今、ネルフ直上を旋回中。\n\0":
'???',

# Toji Suzuhara 
"何か、あったんスか？\n\0":
'???',

# Misato Katsuragi 
"ケイジに向かうわよ。\n\0":
'???',

# Ritsuko Akagi 
"このまま、ケイジに行くわよ。\n\0":
'???',

# Makoto Hyuga
"すまない、君にはこのまま\nエヴァに乗ってもらいたいんだ。\n\0":
'???',

# Shigeru Aoba
"戦闘だ、\nケイジへ急ぐよ。\n\0":
'???',

# Maya Ibuki 
"ごめんなさい、あなたには\nこれからエヴァに乗って戦って\nもらわないといけないの…。\n\0":
'???',

# Toji Suzuhara 
"ひょっとして、使徒？\n\0":
'???',

# Misato Katsuragi 
"エヴァ量産機が投入されたそうよ。\n数は９機。\nあなたの手ですべて消滅させるのよ。\n\0":
'???',

# Ritsuko Akagi 
"エヴァ量産機が９体、\n投入されたわ。▽\nあなたには今から、\nこれを全て殲滅してもらうわ。\n\0":
'???',

# Makoto Hyuga
"量産タイプのエヴァシリーズ９機が\n投入されたらしい。▽\nもうすぐ、ここへ\n侵攻してくるだろう…。▽\nあれを止める事が出来るのは\n君だけだ。\n頼む…、行ってくれないか？\n\0":
'???',

# Shigeru Aoba
"エヴァ量産機が\nここへ投入されたらしい。▽\n君にはすまないが、エヴァで\nすべて消滅させて欲しい。\n数は…、９体だそうだ。\n\0":
'???',

# Maya Ibuki 
"今、エヴァ量産機を発令所の方で\n確認したそうなの。\n全部で９機。▽\nあなたには、エヴァに乗って\n量産機エヴァシリーズを\n全部殲滅して欲しいの。\n\0":
'???',

# Toji Suzuhara 
"９なんて。\nそんな、無茶苦茶な…。\n\0":
'???',

# Misato Katsuragi 
"でも、勝たなきゃいけないの。\nここで行かなければ、負けるだけよ。\n\0":
'???',

# Misato Katsuragi 
"さ、ケイジへ行きましょう。\n\0":
'???',

# Ritsuko Akagi 
"ここでじっとしていれば、\nみんなが死ぬ事になるのよ。\n\0":
'???',

# Ritsuko Akagi 
"行きましょう、ケイジへ。\n\0":
'???',

# Makoto Hyuga
"勇気を出せ！！\n今行かなかったら、みんな、\nみんな死んでしまうんだ。\n\0":
'???',

# Makoto Hyuga
"さあ、ケイジへ急ごう…。\n\0":
'???',

# Shigeru Aoba
"無理かどうかやってみないと\nわかんねぇだろ！！▽\n俺は信じてるよ、君が勝つ事を。\n\0":
'???',

# Shigeru Aoba
"さあ、ケイジまで一緒に行くよ。\n\0":
'???',

# Maya Ibuki 
"私は知ってるわ。\nあなたがどんなに優れた\nパイロットなのかを。▽\n大丈夫、あなたは勝つわ。\n…ね、みんなで待ってるわ。\nあなたが帰ってくるのを。\n\0":
'???',

# Maya Ibuki 
"…さあ、\n急ぎましょう、ケイジへ。\n\0":
'???',

# JSSDF Staff
"発見次第、片づけろ。\n\0":
'???',

# Misato Katsuragi 
"伏せてっ！！\n\0":
'???',

# Ritsuko Akagi 
"頭を低くして。\n\0":
'???',

# Makoto Hyuga
"伏せるんだ。\n\0":
'???',

# Shigeru Aoba
"伏せろっ！！\n\0":
'???',

# Maya Ibuki 
"伏せて！！\n\0":
'???',

# Misato Katsuragi 
"今よ、走りなさい！！\n\0":
'???',

# Ritsuko Akagi 
"今よ、走って！！\n\0":
'???',

# Makoto Hyuga
"先に行け！！\n\0":
'???',

# Shigeru Aoba
"走るんだ、走れ！！\n\0":
'???',

# Maya Ibuki 
"走るのよ、すぐ行くわ！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"ミサトがフロアに設置された\n爆破装置に手をかけた。▽\n自分が遠くに行ったのを確認して、\nパスワードを入力する。\n\0":
'???',

# [Text Only - No Designated Speaker]
"リツコがフロアに設置された\n爆破装置に手をかけた。▽\n自分が遠くに行ったのを確認して、\nパスワードを入力する。\n\0":
'???',

# [Text Only - No Designated Speaker]
"マヤがフロアに設置された\n爆破装置に手をかけた。▽\n自分が遠くに行ったのを確認して、\nパスワードを入力する。\n\0":
'???',

# [Text Only - No Designated Speaker]
"日向がフロアに設置された\n爆破装置に手をかけた。▽\n自分が遠くに行ったのを確認して、\nパスワードを入力する。\n\0":
'???',

# [Text Only - No Designated Speaker]
"青葉がフロアに設置された\n爆破装置に手をかけた。▽\n自分が遠くに行ったのを確認して、\nパスワードを入力する。\n\0":
'???',

# Misato Katsuragi 
"怪我、ないみたいね…。\n\0":
'???',

# Ritsuko Akagi 
"あなたは…無事みたいね…。\n\0":
'???',

# Makoto Hyuga
"よかった、\n君は…、無傷みたいだね。\n\0":
'???',

# Shigeru Aoba
"へへ…、もう大丈夫だ…。\nつつっ…。\n\0":
'???',

# Maya Ibuki 
"大丈夫よ、もうこの先は\n追ってこないでしょうから…。\n\0":
'???',

# Toji Suzuhara 
"…う、撃たれたんですか？\n早う、ワシにおぶさって下さい。\n\0":
'???',

# Misato Katsuragi 
"私なら大丈夫、\n待ってて、このエレベーターで\nケイジに行けるから…。\n\0":
'???',

# Ritsuko Akagi 
"このくらい、何てことないわ。\nかすり傷よ。▽\n待ってなさい、このエレベーターで\nケイジに行けるから…。\n\0":
'???',

# Makoto Hyuga
"待ってろよ、このエレベーターで\nケイジに行けるから。▽\n僕は大丈夫…、一人で発令所に\n戻れるから…。\n\0":
'???',

# Shigeru Aoba
"さあ、このエレベーターを\n使ってケイジへ急ぐんだ…。\n俺は、…今から、戻るから。\n\0":
'???',

# Maya Ibuki 
"大丈夫…、私は大丈夫。\n早く、このエレベーターに乗って\nケイジへ、みんなを助けて…。\n\0":
'???',

# Toji Suzuhara 
"そない言うたかて…。\n\0":
'???',

# Misato Katsuragi 
"行きなさい、命令よ。\n行かなければ、犠牲者が増える。\n急ぎなさい。\n\0":
'???',

# Ritsuko Akagi 
"早くしなさい！！\n\0":
'???',

# Makoto Hyuga
"グズグズしてると、みんな\n助からなくなるんだよっ！！\nいいから、行け！！\n\0":
'???',

# Shigeru Aoba
"いいから、行けよ。\nどのみち助からねえもん、俺。▽\n………。▽\nなあ…、俺、今、\nカッコいいだろ…。▽\nふっ、うなずいてんなよ、嘘つき。\nさっさと行きやがれ。\n\0":
'???',

# Maya Ibuki 
"ごめんね、あとは一人で\n行ってね…。▽\nごめんね…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そう言うとミサトは、ぐらりと傾き\n糸の切れた操り人形のように\n崩れ落ちた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"床にはおびただしい量の\n血だまりが出来ていた…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そう言うとリツコは、ぐらりと傾き\n糸の切れた操り人形のように\n崩れ落ちた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そう言うと日向は、ぐらりと傾き\n糸の切れた操り人形のように\n崩れ落ちた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そう言うと青葉は、ぐらりと傾き\n糸の切れた操り人形のように\n崩れ落ちた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そう言うとマヤは、ぐらりと傾き\n糸の切れた操り人形のように\n崩れ落ちた。\n\0":
'???',

# Toji Suzuhara 
"ほな…、行きます。\n勝って、帰ってきます…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ごめんなさい…。\n何度もそうつぶやいた。▽\n自分なんか、居なくなればいい。\n消えてしまえばいい。▽\nいつもそんな事ばかり考えていた\n自分を、命を捨ててまで助けて\nくれた。▽\nごめんなさい、ありがとう。\nもう、そんな馬鹿な事は考えない。\nそんな迷いには屈しない。▽\nただ今は、この現実を真っ向から\n受け止めよう。\nそして、勝とう…。\n\0":
'???',

# Toji Suzuhara 
"…こちら参号機、\n発進準備お願いします。\n\0":
'???',

# Female Staff
"了解。\nエヴァンゲリオン、起動。\n\0":
'???',

# Misato Katsuragi 
"このエレベーターを使えば\nケイジへ行けるわ。\n乗って。\n\0":
'???',

# Ritsuko Akagi 
"このエレベーターで、\nケイジまで直行するわ。\n乗ってちょうだい。\n\0":
'???',

# Makoto Hyuga
"このエレベーターでなら、\nケイジまですぐだよ。\nさあ、乗って。\n\0":
'???',

# Shigeru Aoba
"このエレベーターを使えば、\nケイジに行ける。\nさあ、乗って。\n\0":
'???',

# Maya Ibuki 
"このエレベーターを使えば\nケイジまでたどり着けるわ。\n乗って。\n\0":
'???',

# Toji Suzuhara 
"…ワシ、一人でですか？\n\0":
'???',

# Misato Katsuragi 
"私は発令所に戻るわ。\nそして、発進準備を進めるわ。\n\0":
'???',

# Ritsuko Akagi 
"ここから先は、あなた一人よ。\n頑張って、勝つのよ…。\n\0":
'???',

# Makoto Hyuga
"僕が一緒に行動出来るのは\nここまでだ。\nじゃ、健闘を祈るよ…。\n\0":
'???',

# Shigeru Aoba
"頑張るんだ、\n俺は発令所に戻る。\nそして、出来る限り君を助ける。\n\0":
'???',

# Maya Ibuki 
"私は発令所に戻るわ。\n大丈夫よ、あなたは勝つわ。\nみんなで待っているから…ネ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"あとはエレベーターの中で\nミサトの無事を祈った。▽\n怖かった。▽\n出来る事といえば、エヴァに乗って\n戦う事しか出来ない。▽\n最後にもう一度だけ、\nみんなの無事を祈った。\n\0":
'???',

# [Text Only - No Designated Speaker]
"あとはエレベーターの中で\nリツコの無事を祈った。▽\n怖かった。▽\n出来る事といえば、エヴァに乗って\n戦う事しか出来ない。▽\n最後にもう一度だけ、\nみんなの無事を祈った。\n\0":
'???',

# [Text Only - No Designated Speaker]
"あとはエレベーターの中で\n日向の無事を祈った。▽\n怖かった。▽\n出来る事といえば、エヴァに乗って\n戦う事しか出来ない。▽\n最後にもう一度だけ、\nみんなの無事を祈った。\n\0":
'???',

# [Text Only - No Designated Speaker]
"あとはエレベーターの中で\n青葉の無事を祈った。▽\n怖かった。▽\n出来る事といえば、エヴァに乗って\n戦う事しか出来ない。▽\n最後にもう一度だけ、\nみんなの無事を祈った。\n\0":
'???',

# [Text Only - No Designated Speaker]
"あとはエレベーターの中で\nマヤの無事を祈った。▽\n怖かった。▽\n出来る事といえば、エヴァに乗って\n戦う事しか出来ない。▽\n最後にもう一度だけ、\nみんなの無事を祈った。\n\0":
'???',

# Female Staff, Makoto Hyuga
"通信が不可能な施設が\n次々と増えています！\n\0":
'???',

# Male Staff,Shigeru Aoba
"進入者の数が多すぎます！\n全てを把握できません！\n\0":
'???',

# Female Staff,Shigeru Aoba
"地下、第３隔壁破壊。\n第二層に侵入されました。\n\0":
'???',

# Kozo Fuyutsuki
"戦自、約一個師団の投入か。\n占拠は時間の問題だな。\n\0":
'???',

# Male Staff
"戦自、約一個師団の投入か。\n占拠は時間の問題のようだな。\n\0":
'???',

# Announcement
"第３ハブステーションの爆発を確認。\n死者多数、損害不明。\n\0":
'???',

# Toji Suzuhara 
"………。▽\nあの…、この事態は\n一体何なんですか…？\n\0":
'???',

# Male Staff
"こちらは第１発令所です。\nたった今、ネルフ直上に\n未確認機、９機を確認しました。\n\0":
'???',

# Male Staff
"あれは、エヴァ…。\nエヴァ量産機、エヴァシリーズです！\n\0":
'???',

# [Text Only - No Designated Speaker]
"必死で走った。▽\n何がどうなっているのかなんて、\nもう、わからない。▽\n走っていく先々には、昨日まで\n会えば挨拶を交わしていた人達が\n息絶えていた。▽\n夢なら覚めてくれと、走りつづけた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"走って、走って…、それでも\n走って気がつけば、ケイジへ続く\nエレベーターの前にいた。\n\0":
'???',

# Toji Suzuhara , Shinji Ikari, Asuka Soryu Langley, Kaworu Nagisa
"………………………………。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ただ、これから何をするべきかは\nわかった。▽\nやるべきことがある。▽\n戦うこと。▽\n妹のために戦うことだ。▽\n行こう。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le136.evs
#
# Shinji Ikari
"君は他人なの？\n\0":
'???',

# Shinji's Shadow [Leliel]
"他人にしているだけだ、君が。▽\n自分自身を隔離し、分離して、\nこれは自分じゃないと\n思い込んでいる。\n\0":
'???',

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
# ./USRDIR/event/tev0278.har_EXTRACT/tev0278.evs
#
# Misato Katsuragi 
"ここがあなたの部屋よ。\n荷物もソッコーでこっちに\n回してもらったから。▽\nシンジ君が寝る時は、\nこの部屋を使って。▽\nまあ、こういった特定の場所で\n%1iボタンを押せば、\nその場に応じた行動を実行出来るわ。▽\n色んな所で試してごらんなさい。\n\0":
'???',

#
# ./USRDIR/event/cev1013.har_EXTRACT/cev1013.evs
#
# [Text Only - No Designated Speaker]
"長い間、迷った。\n行くべきかどうかを。▽\nでも、気が付けば…、\n足は第２新東京市へ向かっていた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"野外ライブ会場へ着くと、\n学生時代の音楽仲間がいた。\n\0":
'???',

# Tadamitsu Otsubo
"やっぱ、ギターは抜きで。\nキーボードでサポートして\nやるしかないよ。\n\0":
'???',

# Mikio Shimaki
"本当に、シゲルは来るのか？\n\0":
'???',

# Yoji Uozumi
"もう、公演まで時間がない。\n夜にゃあ、本番だ。▽\nやっぱ、客のチケットの払い戻しを\n事務所に言った方が…。\n\0":
'???',

# Shigeru Aoba
"よう…。\n\0":
'???',

# Teruo Kato
"シゲル…！！\nシゲルよぉ…来てくれたんだ。\n\0":
'???',

# Tadamitsu Otsubo
"シゲル…。\n\0":
'???',

# Mikio Shimaki
"シゲル、お前…。\n\0":
'???',

# Yoji Uozumi
"シゲル、久しぶりだなぁ。\n\0":
'???',

# Shigeru Aoba
"大体、お前達の曲は聞いたよ。\n何とか出来ると思う。\n\0":
'???',

# Teruo Kato
"シゲル…、お前…。▽\nよし、時間がない。\nみんな、リハーサルだ！\n\0":
'???',

# Maya Ibuki 
"フフ…。\nライブなんて、学生時代以来だわ。\n\0":
'???',

# Asuka Soryu Langley
"今日は、\nコバルトスカイのライブだわ。\n\0":
'???',

# Hikari Horaki
"楽しみね♪\n今からドキドキしちゃう。\n\0":
'???',

# Kensuke Aida
"コバルトスカイのライブ、\n前から４列目ゲットしたんだ。\nへへへ。\n\0":
'???',

# Toji Suzuhara 
"おぉ、すごいやん。\nよっしゃ、授業終わったら\n速攻で出るで。\n\0":
'???',

# Toji Suzuhara 
"シンジ、チケット忘れんと\n持ってきたか？\n\0":
'???',

# Shinji Ikari
"うん…。\n僕、コンサートなんて初めてだ。\n\0":
'???',

# Toji Suzuhara 
"アホ、コンサートちゃう。\nライブや、ライブ。\n\0":
'???',

# Shinji Ikari
"どっちでもいいんじゃない？\n\0":
'???',

# [Text Only - No Designated Speaker]
"リハーサルが終わり、\n日が沈みかけた頃。\nいよいよ会場の時間になった。\n\0":
'???',

# Teruo Kato
"いよいよだな…。\n緊張するか？\n\0":
'???',

# Shigeru Aoba
"バーカ、そんなんじゃ\nロックはやれねぇよ。\n\0":
'???',

# Lordi
"本番、時間です。\n\0":
'???',

# Shigeru Aoba
"おーっし！\n\0":
'???',

# Teruo Kato
"ライブ成功を祈ってェ！\n\0":
'???',

# Everyone
"ファイトォ！\n\0":
'???',

# Teruo Kato
"行くぞォ！！\n\0":
'???',

# Everyone
"おぉ！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"コバルトスカイの演奏は、\n夏の夜空を駆け抜けた。\n\0":
'???',

# Shigeru Aoba
"夢にまで見た、ステージだ。\n俺は…、俺は今…。\n\0":
'???',

# Maya Ibuki 
"…青葉…、君？\nウソ…！！\n青葉君っ！！\n\0":
'???',

# Asuka Soryu Langley
"青葉さん！？\nあれ、青葉さんじゃない！？\n\0":
'???',

# Shinji Ikari
"ギター弾いてるの、青葉さん！？\nすごい、すごいや！！\n青葉さんだ！！\n\0":
'???',

# Maya Ibuki 
"大変…、使徒だわ。\n\0":
'???',

# Asuka Soryu Langley
"召集だわ…。\n今、サイコーだってのに。\nんもぅ！！\n\0":
'???',

# Shinji Ikari
"召集だ。\n戻らなくちゃ。\n\0":
'???',

# Teruo Kato
"行くのか…？\n\0":
'???',

# Teruo Kato
"そうか、頑張れよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"テルオ達が笑った。\n\0":
'???',

# Shigeru Aoba
"俺は、みんなを守るよ。▽\nいつまでも、いいライブが\n出来るように。\nお前達がいい曲出していけるように。▽\n頑張って、いい曲書いてくれ。\n\0":
'???',

# Teruo Kato
"…シゲル。\n\0":
'???',

# [Text Only - No Designated Speaker]
"最後に敬礼をすると、\n皆がきれいに敬礼を返してくれた。\n少し崩れた笑いで、手を振る。▽\n早く戻らねば。\n皆を守る為に。▽\n発令所のあの堅い椅子が、\n俺の場所なんだ。\n\0":
'???',

#
# ./USRDIR/event/cev0111.har_EXTRACT/cev0111.evs
#
# Ryoji Kaji
"よお。\n\0":
'???',

# Shinji Ikari
"あ、加持さん。\nミサトさんは今ちょっと\nいないんですけど…。\n\0":
'???',

# Ryoji Kaji
"いや、近く通ったから。\nただ寄っただけなんだけどな。▽\nスイカ持ってきたんだ。\nこれ、食ってくれ。\n\0":
'???',

# Shinji Ikari
"あ、じゃあ今から切りましょうか。\nどうぞ、上がって下さい。\n\0":
'???',

# Ryoji Kaji
"そういや、彼女とか出来たのか？\n\0":
'???',

# Shinji Ikari
"そんな事あるわけないでしょう？\n勉強だって追いつくのが\nやっとなのに。\n\0":
'???',

# Ryoji Kaji
"おっと、そりゃ勿体無いな。\n恋をしたり、遊んでいられるのは\n学生のうちだけなんだぞ。\n\0":
'???',

# Shinji Ikari
"加持さんでしたら、\nそうだったんでしょうけど。\n僕は違いますよ。\n\0":
'???',

# Ryoji Kaji
"いやいや、健全な男の子としては\n女の子の一人や二人や三人は\n口説き落とせないとな。\n\0":
'???',

# Shinji Ikari
"…そうですか？\n\0":
'???',

# Ryoji Kaji
"…君だって好きな子いるだろ？\nまあ、名前は聞かないでやろう。\nいざって時、どうするんだ？\n\0":
'???',

# Shinji Ikari
"いざって時って…、\n二人っきりて状況ですか…？\n\0":
'???',

# Ryoji Kaji
"ん〜、まあ君の場合はそうかな。\n自発的に二人っきりって状況を\n作れないだろうからな…。▽\n大人には、もっといざっていう\n状況があるものさ…。\n\0":
'???',

# Shinji Ikari
"普通にラブレターとかじゃ\n駄目なんですか？\n\0":
'???',

# Ryoji Kaji
"う〜ん、いいねぇ…。\n\0":
'???',

# Ryoji Kaji
"だけどな、手紙で成立するのは\n相手もたまたまこっちを好きだった\n場合だけだろ？\n\0":
'???',

# Shinji Ikari
"…なるほど…。\n\0":
'???',

# Ryoji Kaji
"その場の空気を作って、\n好きにさせるんだよ。▽\n…まあ、断れない雰囲気を作るって\n感じかな…。\n\0":
'???',

# Shinji Ikari
"そ、それって、無理矢理…。\n\0":
'???',

# Ryoji Kaji
"はは、違うさ。▽\nその場の空気ってのに\n影響されるもんだよ？\n女性って方々は。\n\0":
'???',

# Shinji Ikari
"はぁ…、そんなもんですか…。\n\0":
'???',

# Ryoji Kaji
"ようし、じゃあ実践編だ。\n…俺をよろめかせてみなよ。\n\0":
'???',

# Shinji Ikari
"な、なんで、そうなるんですか！\n\0":
'???',

# Ryoji Kaji
"おいおい、何も俺を口説けって\n言ってるわけじゃない。▽\n女心を理解した俺が、女性の立場で\n聞いてやろうって事だよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"エラい事になったなぁ…。\n僕は内心溜息をついた…、が、\n少し向学心も芽生えてきた…。▽\n確かに、学ぶべき所はあるかも\nしれない…。\n\0":
'???',

# Shinji Ikari
"はあ、じゃあ…、\nええっと…。\nす、好きだっ！\n\0":
'???',

# Ryoji Kaji
"あー、だめだめ！\n気負い過ぎだ。\nもっとサラッと言う。\n\0":
'???',

# Shinji Ikari
"えーっと、じゃあ…。\n好き…です。\n\0":
'???',

# Ryoji Kaji
"うーん、気持ちが入ってないなぁ。\n…いやいや、実際に入れなくていい。\n入ってるように思わせるんだ。\n\0":
'???',

# Shinji Ikari
"う〜ん、やっぱり難しいですよ。\nそんな気分になれないし…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"加持さんは端整な顔を歪め、\n少し考え込んでいる。\nすると…。\n\0":
'???',

# Ryoji Kaji
"ちょっと待ってな…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"イヤな予感がした。\n\0":
'???',

# Ryoji Kaji
"どうだ？\n似合うでしょ？\n\0":
'???',

# [Text Only - No Designated Speaker]
"的中してしまった…。▽\nミサトさんのクローゼットから\n大きめのブラウスと、スカートを\n引っ張り出して来たのだ。▽\nそして髪の毛もカツラ…、じゃなく、\n自前のお下げ髪をほどいて、\n見事なロン毛を手櫛でといている。\n\0":
'???',

# Shinji Ikari
"…もう、やめませんか…？\n\0":
'???',

# Ryoji Kaji
"どうして？　私をここまで\nその気にさせたのに？\n\0":
'???',

# Shinji Ikari
"僕にその気が失せたんです！\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕の知る加持さんは、\n不精髭の似合う、ナイスガイだ。▽\nこんな体格のいい\n裏声のオカマなんかじゃ絶対無い。\n\0":
'???',

# Ryoji Kaji
"ひ、ひどい！\nあなた…、私をこんなにして…。\n責任取ってよ！\n\0":
'???',

# Shinji Ikari
"わぁッ！\nな、何言ってるんですか！\n\0":
'???',

# Ryoji Kaji
"全部あなたの為だったのに…。\nあなたの犠牲になったのに…。\n\0":
'???',

# Shinji Ikari
"わっ、い、イヤだ！\n顔を近づけないで……。\nちょ、ちょっと加持さんっ！\n\0":
'???',

# Ryoji Kaji
"イヤよ、リョウ子って呼んで！\n\0":
'???',

# Shinji Ikari
"リョ、リョウ…、\nじゃないじゃないっ！\nか、勘弁して下さい！\n\0":
'???',

# Ryoji Kaji
"おお…、テンション上がるなぁ…。\n\0":
'???',

# Shinji Ikari
"や、やめて！\n加持さん、脱がないでっ！\n\0":
'???',

# Ryoji Kaji
"断る！\n\0":
'???',

# Shinji Ikari
"ミ、ミサトさーーーーん！\n\0":
'???',

# Misato Katsuragi 
"人の家上がりこんで、\n何やってるのよ！！\nこのヘンタイ！！▽\nホラ、ちょっと来なさいよ！\n来なさいッ！！\n\0":
'???',

# Shinji Ikari
"た、助かった…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"加持さんはミサトさんに呼ばれて、\n部屋に入っていった。▽\nミサトさんの大声が聞こえる。\nそれをなだめる加持さんの声も。▽\n…加持さんは身を持って、\n口説きの悪い見本を示してくれた。▽\n加持さんに深く心の中で感謝して、\nいずれこの教えを役に立てようと、\n僕は自分の部屋に引っ込んだ。\n\0":
'???',

#
# ./USRDIR/event/tev1501.har_EXTRACT/tev1501.evs
#
# Shinji Ikari
"あの時、エヴァに乗ったあと…、\n僕はどうなっていたんだろう。\n\0":
'???',

# Shinji Ikari
"エントリープラグの中にいた\nはずなんだ。▽\n誰かに会ったような気がする。\n誰に会ったんだろう。\n誰かに会ったはずだ…。\n\0":
'???',

# Shinji Ikari
"アスカ…？\n\0":
'???',

# Shinji Ikari
"ミサトさん…？\n\0":
'???',

# Shinji Ikari
"ううん、違う。\nあの時、僕は、\n母さんのにおい…を感じた。\n\0":
'???',

# Gendo Ikari [Flashback]
"セカンドインパクトの後に\n生きていくのか、この子は…。\nこの地獄に…。\n\0":
'???',

# Gendo Ikari [Flashback]
"そうか、そうだったな。\n\0":
'???',

# Shinji Ikari
"父さん…、\n母さん…。\n\0":
'???',

# Misato Katsuragi 
"人類補完計画、\nどこまで進んでるの？\n\0":
'???',

# Misato Katsuragi 
"人を滅ぼすアダム。\n何故、地下に保護されているの？\n\0":
'???',

# Ryoji Kaji
"それが知りたくて\n俺と逢ってるのか？\n\0":
'???',

# Misato Katsuragi 
"それもあるわ、正直ね。\n\0":
'???',

# Ryoji Kaji
"ご婦人に利用されるのも\n光栄の至りだが、\nこんなところじゃ喋れないよ。\n\0":
'???',

# Misato Katsuragi 
"今は、私の希望が伝わればいいの。▽\nネルフ、\nそして、碇司令の本当の目的は何？\n\0":
'???',

# Ryoji Kaji
"こっちが知りたいさ。\n\0":
'???',

# Misato Katsuragi 
"あッ…、▽\nちょっと、変なもの入れないでよ！▽\nこんな時に、もう…何よ。\n\0":
'???',

# Ryoji Kaji
"プレゼントさ。\n８年ぶりの。▽\n最後かもしれないがな。\n\0":
'???',

#
# ./USRDIR/event/tev0233.har_EXTRACT/tev0233.evs
#
# Misato Katsuragi 
"じゃあ、体調について\n説明をしましょう。▽\n%4iボタンを押してごらんなさい。\nシステムメニューを呼び出せるの。\n\0":
'???',

#
# ./USRDIR/event/tev0206.har_EXTRACT/tev0206.evs
#
# Makoto Hyuga
"お疲れ様です、葛城一尉。\nあぁ、彼は…。\n\0":
'???',

# Shinji Ikari
"はじめまして…。\n\0":
'???',

# Makoto Hyuga
"よろしく。\n僕は、日向マコト。▽\n僕の所属は、まあ平たく言えば\n作戦部所属のオペレーターさ。\n\0":
'???',

# Misato Katsuragi 
"じゃあ、日向君。\nここの説明をざっとお願いね。\n\0":
'???',

# Makoto Hyuga
"あ、はい。\nここはネルフ職員が、白兵技能を\n訓練する為の場所なんだよ。\n\0":
'???',

# Shinji Ikari
"白兵技能？\n\0":
'???',

# Makoto Hyuga
"そう、戦闘行動に関わる技能さ。▽\n単純に言えば、白兵技能が\n高ければ高いほど、\n戦闘では有利になる。▽\nシンジ君もパイロットなんだし、\nここで訓練するといい。\n\0":
'???',

# Misato Katsuragi 
"そうね、強制はしないけど\n技能を上げる事は勧めるわ。▽\nシンジ君が鍛えられる技能は４つ。\n事務技能、情報技能、\nココで訓練出来る白兵技能。▽\nもう一つはシンクロ技能よ。\n\0":
'???',

# Makoto Hyuga
"事務技能は、ネルフの事務業務…、\n意見書の作成や、書類の作成の\n成否を判定する為の技能なんだ。▽\nこういった事務全般や、\nシンジ君なら学校の\n授業態度に影響を与える。▽\n事務技能は、事務の仕事や勉強、\n授業で上昇させる事が出来る。\n\0":
'???',

# Misato Katsuragi 
"情報技能は、あまり大きな声じゃ\n言えないけど…ハッキングの\n成否に影響を与える技能よ。\n\0":
'???',

# Misato Katsuragi 
"情報技能は、パソコンのある場所で\n情報技能を訓練する事で上昇するわ。\n\0":
'???',

# Makoto Hyuga
"白兵技能は、パイロットの場合、\n一部の戦闘コマンドに影響を与える。▽\n「姿勢を構える」「狙いをつける」\nといった戦闘コマンドの有効時間が\n白兵技能の高さに比例して長くなる。▽\n白兵技能の訓練はココ、\n射撃場にて行える。▽\n僕らは、パイロットじゃなくても\n自己防衛の為に訓練が必要なんだ。▽\nどんな危険な目に遭うか\nわからないからね。\n\0":
'???',

# Misato Katsuragi 
"シンジ君に最も重要なのは\nシンクロ技能。▽\nこれは、エヴァをよりスムーズに\n扱う為の技能よ。▽\nこの技能を上げていけば、\nエヴァの移動速度が速くなったり、\n使用可能な戦闘行動が増えるわ。\n\0":
'???',

# Misato Katsuragi 
"他にも、参謀技能、開発技能、\nオペレート技能、諜報技能\nなんてのもあるけど。▽\nこれらは、シンジ君には扱えない\n技能になっちゃうわね。\n\0":
'???',

# Makoto Hyuga
"技能レベルの数値は、\n０から９９まで。\nステータス画面で確認出来るよ。\n\0":
'???',

# Misato Katsuragi 
"説明アリガト、日向君。\n\0":
'???',

# Makoto Hyuga
"いやぁ…。\n\0":
'???',

# Misato Katsuragi 
"それじゃ、次に行くわね。▽\n今度は、\n大浴場へ行きましょう。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le220.evs
#
# Asuka Soryu Langley
"みんなも？\n私だけじゃなかったの？\n\0":
'???',

# Asuka's Shadow [Leliel]
"でもあなたは他の人と違う。\n選ばれた人なんでしょう？\n同じじゃないわね。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le110.evs
#
# Shinji Ikari
"傷つかない為には、\n何もしない方がいい。▽\nでも、状況をよくする為には、\n何かをしないといけない。▽\nどっちなんだよ！\nどう生きていけばいいんだ！？\n\0":
'???',

# Shinji's Shadow [Leliel]
"その答えがあったとしても、\n結局不満は残るよ。▽\n君が、他人との恐怖に\n捕らわれているままだったら。\n\0":
'???',

#
# ./USRDIR/event/bs012.har_EXTRACT/bs012.evs
#
# Rei Ayanami 
"…っくぅぅぅぅぅ！\n\0":
'???',

#
# ./USRDIR/event/tev1306.har_EXTRACT/tev1306.evs
#
# Misato Katsuragi 
"４人目？\nフォース・チルドレンが\n見つかったの？\n\0":
'???',

# Ritsuko Akagi 
"そう。▽\n松代での参号機の起動試験。\nテストパイロットには、\n４人目を使うわよ。\n\0":
'???',

# Misato Katsuragi 
"マルドゥック機関からの報告は\n受けてないわよ。\n\0":
'???',

# Ritsuko Akagi 
"正式な書類は明日、届くわ。\n\0":
'???',

# Misato Katsuragi 
"リツコ、私に隠し事してない？\n\0":
'???',

# Ritsuko Akagi, Asuka Soryu Langley
"…別に。\n\0":
'???',

# Misato Katsuragi 
"ま、いいわ。\nで、その選ばれた子ってのは誰？\n\0":
'???',

# Ritsuko Akagi 
"これが資料よ。\n\0":
'???',

# Misato Katsuragi 
"よりにもよって、この子なの？\n\0":
'???',

#
# ./USRDIR/event/n010.har_EXTRACT/n010.evs
#
# Shigeru Aoba, Male Staff
"エヴァ要撃ポイント、\n予想落下地点から大きく\n外れていきます。\n\0":
'???',

# Misato Katsuragi, Female Staff
"エヴァは見事使徒を受け止め\n使徒殲滅に成功しましたが\n\0":
'???',

# Misato Katsuragi, Female Staff
"エヴァによる直接要撃を試みました。\n\0":
'???',

# Female Staff, Misato Katsuragi 
"エヴァは見事使徒を受け止め\n\0":
'???',

# Misato Katsuragi, Female Staff
"サハクィエル\n\0":
'???',

# Misato Katsuragi, Female Staff
"使徒殲滅に成功しました。\n\0":
'???',

# Misato Katsuragi 
"そんな…！？\nマギに要撃ポイント修正を、\n急いで！\n\0":
'???',

# Misato Katsuragi, Female Staff
"インド洋上空衛星軌道上に目標を発見\n\0":
'???',

# Female Staff
"マギに要撃ポイント修正を、\n急いで下さい！\n\0":
'???',

# Male Staff, Makoto Hyuga
"ダメです、現在のエヴァの\nポイントからでは間に合いません！\n\0":
'???',

# Misato Katsuragi, Female Staff
"Ν航空爆雷の効果も空しく\n\0":
'???',

# Misato Katsuragi 
"あきらめないわよ…、\n私はあきらめないわよッ！！\n\0":
'???',

# Shigeru Aoba
"チクショウ、\nこれで終わりなのか！？\n全て、終りになるのかよッ！！\n\0":
'???',

# Makoto Hyuga
"ここまでか…。\nせめて、パイロットだけでも\n無事であれば…。\n\0":
'???',

# Female Staff
"もう、なす術はないの…。\n\0":
'???',

# Misato Katsuragi, Female Staff
"パイロットを失うという\n致命的な損害を受けてしまいました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標は誤差修正しながら、\n組織の一部を落下させ攻撃開始\n\0":
'???',

# Misato Katsuragi, Female Staff
"ネルフ権限における特別宣言Ｄ−１７\nを発令し、半径５０キロメートルの\n全市民の避難を行う\n\0":
'???',

# Misato Katsuragi, Female Staff
"予測通り、目標は\n第３新東京市を目掛け、降下\n\0":
'???',

# Misato Katsuragi, Female Staff
"成層圏より飛来する目標に対し\n\0":
'???',

#
# ./USRDIR/event/f060.har_EXTRACT/f060.evs
#
# [Text Only - No Designated Speaker]
"ふと、アスカの声が\n聞こえた気がした。\n\0":
'???',

# Asuka Soryu Langley
"私は一人で生きるの。▽\n一人でいいの、\nどうせまわりはバカばかり。\n付き合っていられないわ。\n\0":
'???',

# Shinji Ikari
"じゃあ、何でいちいち\nつっかかって来るんだよ。▽\n一人じゃ生きられないからだろ。\n\0":
'???',

# Asuka Soryu Langley
"うるさい！！▽\nこの私が、本当はアンタなんかと\n付き合ったりはしないのよ。\nアンタに付き合ってやってるのよ！\n\0":
'???',

# Rei Ayanami 
"結局、\n一人にならないために、でしょ？\n自分をそうやって守りたいの。\n\0":
'???',

# Asuka Soryu Langley
"うるさい！！\n\0":
'???',

# Shinji Ikari
"そうしないと、自分自身が\n消えてしまうからだろ…。\n\0":
'???',

# Asuka Soryu Langley
"うるさい、うるさい、うるさい！！▽\nみんなキライ、大キライ…。▽\nでも、私…嫌われたくない。\n一人になりたくない…。\n\0":
'???',

#
# ./USRDIR/event/f008.har_EXTRACT/f008.evs
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
# ./USRDIR/event/f094.har_EXTRACT/f094.evs
#
# [Text Only - No Designated Speaker]
"これからは、\nこの部屋がシンジの部屋です。\n\0":
'???',

# [Text Only - No Designated Speaker]
"これまでシンジが生活していた\n部屋は、新たな同居人のアスカが\n使用することになりました。\n\0":
'???',

#
# ./USRDIR/event/tev1507.har_EXTRACT/tev1507.evs
#
# Misato Katsuragi 
"ただいま…。\n\0":
'???',

# Misato Katsuragi, Rei Ayanami
"………！\n\0":
'???',

# Ryoji Kaji
"葛城、俺だ。\n多分この話を聞いてる時は、\n君に多大な迷惑をかけた後だと思う。▽\nすまない。\nリッちゃんにも、すまなかったと\n謝っといてくれ。▽\n葛城、真実は君と共にある。\n迷わず進んでくれ。▽\nもう一度逢える事があったら、\n８年前に言えなかった言葉を言うよ。▽\nじゃ…。\n\0":
'???',

# Shinji Ikari
"…加持さん？\n\0":
'???',

# Ryoji Kaji
"葛城は、戻るよ。\nアイツを頼む。\nシンジ君…。\n\0":
'???',

# Answering Machine
"午後、０時２分です。\n\0":
'???',

# Misato Katsuragi 
"バカ。\nあんた、ホントにバカよ。\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Rei Ayanami, Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Toji Suzuhara
"加持さん…。\n\0":
'???',

# Ryoji Kaji
"君は…真実を知る義務がある。\n\0":
'???',

# Ryoji Kaji
"そして君は、知らなければならない。\n真実を。▽\nお母さんの事も、\n君のお父さんの目的も。\n世界がどうなろうとしているのかを。\n\0":
'???',

# Shinji Ikari
"もう二度と、加持さんには\n会えないのだろう。\nそう深く、静かな確信があった。▽\n加持さんは、僕の忘れていた現実を\n掘り起こしたまま、\nいなくなってしまったんだ…。\n\0":
'???',

#
# ./USRDIR/event/bs058.har_EXTRACT/bs058.evs
#
# Misato Katsuragi 
"シンジ君、聞こえるわね？▽\n早速だけど、あなたには\nこのエヴァンゲリオンで人類の敵、\n使徒と戦ってもらいます。\n\0":
'???',

# Misato Katsuragi 
"ではまず、\nエヴァの操縦方法について\n説明します。▽\nあなたの手元に、\n「アナログパッド」があるでしょ？▽\n操縦は、その「アナログパッド」を\n動かしたい方向へ動かせばいいの。\nやってみて。\n\0":
'???',

#
# ./USRDIR/btl/b2event.har_EXTRACT/d067.evs
#
# Toji Suzuhara 
"しばいたるわ！！\n\0":
'???',

# Toji Suzuhara 
"見とれよ、ワレェ！！\n\0":
'???',

# Toji Suzuhara 
"いっちょ、いわしたろか！！\n\0":
'???',

#
# ./USRDIR/event/cev1206.har_EXTRACT/cev1206.evs
#
# [Text Only - No Designated Speaker]
"妹に悪いと思いながらも、\n折鶴を広げた。\n折り紙には妹の願いが書いてある。\n\0":
'???',

# Toji Suzuhara 
"お兄ちゃんと、\n海に行けますように…。▽\n…あいつ。\n\0":
'???',

# Toji Suzuhara 
"んぁ…？\n飛ばした折鶴や。\nこんな所に落ちたんかいな。\n\0":
'???',

# Toji Suzuhara 
"…………………………。\nうん、願い事書いてある。\n\0":
'???',

#
# ./USRDIR/event/tev1313.har_EXTRACT/tev1313.evs
#
# Misato Katsuragi, Ritsuko Akagi, Ryoji Kaji, Kozo Fuyutsuki, Maya Ibuki, Shigeru Aoba, Makoto Hyuga, Kaworu Nagisa, Female Staff
"シンジ君。\n\0":
'???',

# Shinji Ikari
"ミサトさん！\nよかった、無事だったんですね！\n\0":
'???',

# Misato Katsuragi 
"私は…、ね。\n\0":
'???',

# Misato Katsuragi 
"シンジ君。\nごめんなさい。▽\n私、あなたに大事な事を\n伝えなくっちゃいけなかったのに。\nこんな事に。\n\0":
'???',

# Shinji Ikari
"ミサトさん。\n僕は、僕は人を…。▽\nエヴァが人を…父さんが。\n止めてって頼んだのに…。\n\0":
'???',

# Misato Katsuragi 
"あの、シンジ君。\nごめん、ごめんね。\n\0":
'???',

# Maya Ibuki 
"エントリープラグの\n回収班より、連絡。\n生存者を確認。\n\0":
'???',

# Shinji Ikari
"生きてた？\n\0":
'They\'re alive?\n\0',

# Misato Katsuragi 
"あの、参号機のパイロットは、\nフォース・チルドレンは…。\n\0":
'Unit-03\'s pilot...\n The Fourth Child is...\n\0',

# Shinji Ikari
"…トウジ？\n\0":
'...Toji?\n\0',

# Misato Katsuragi 
"シンジ君。\n…シンジ君！\n\0":
'Shinji-kun.\n Shinji-kun!\n\0',

# Shinji Ikari
"うわぁあああああああああ！！\n\0":
'???',

#
# ./USRDIR/event/tev1508.har_EXTRACT/tev1508.evs
#
# Shinji Ikari
"いえ、本部じゃないんですか？\n家にもいなかったんですけど。\n\0":
'???',

# Makoto Hyuga, Shinji Ikari
"…まさか。\n\0":
'???',

# Makoto Hyuga
"あ、ゴメン。\n何でもない。\nきっと、そのうち戻ってくるよ。\n\0":
'???',

# Makoto Hyuga
"シンジ君、\nミサトさんと連絡がつかないんだ。\n家にいるのかな？\n\0":
'???',

#
# ./USRDIR/event/b2s37.har_EXTRACT/b2s37.evs
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
# ./USRDIR/event/cev1424.har_EXTRACT/cev1424.evs
#
# Hikari Horaki
"鈴原…、大丈夫かな。\nお見舞いとか行きたいけれど。\n一般人は行けない所なんだろうな。\n\0":
'???',

#
# ./USRDIR/event/n008.har_EXTRACT/n008.evs
#
# Misato Katsuragi, Female Staff
"ガギエル\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標はエヴァ弐号機を輸送中の\n太平洋国連艦隊を襲撃。\n\0":
'???',

# Misato Katsuragi, Female Staff
"これに対し、セカンド・チルドレン\n惣流・アスカ・ラングレーは、\n\0":
'???',

# Misato Katsuragi, Female Staff
"エヴァ弐号機を起動し、応戦します。\n\0":
'???',

# Misato Katsuragi, Female Staff
"しかし、Ｂ型装備による、最悪の\n水中戦を強いられることになりました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"この危機的状況を打破するため、\n\0":
'???',

# Misato Katsuragi, Female Staff
"国連残存戦艦二隻による\n零距離射撃作戦を試みます。\n\0":
'???',

# Misato Katsuragi, Female Staff
"作戦要綱は、弐号機が目標の口を開口\n全艦を突入させ、艦首主砲塔の直接砲撃の後\nさらに自爆\n\0":
'???',

# Misato Katsuragi 
"国連軍からの協力を得ながらも、\nかろうじて使徒を撃破する事に成功しました\n\0":
'???',

# Female Staff
"国連軍からの協力を得ながらも、\nかろうじて使徒を迎撃する事に成功しました\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le219.evs
#
# Asuka Soryu Langley
"私が苦しんでいるみたいに、\n他の人も苦しんでいるの？\nそんなハズはないわ。\n\0":
'???',

# Asuka's Shadow [Leliel]
"他人の苦しみを知りたくないから\n距離を取ったのでしょう？▽\n知ってしまえば優しくしてしまう。\n偉そうにできなくなってしまう…。\n\0":
'???',

#
# ./USRDIR/event/tev1108.har_EXTRACT/tev1108.evs
#
# Shinji Ikari, Asuka Soryu Langley, Rei Ayanami, Misato Katsuragi, Gendo Ikari, Ritsuko Akagi, Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Ryoji Kaji, Hikari Horaki
"………！！\n\0":
'???',

# Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Female Staff
"マギ、自律自爆を実行します！\n自爆装置、稼動しました！！\n\0":
'???',

# Shigeru Aoba, Maya Ibuki, Makoto Hyuga, Female Staff
"駄目です、あと３、２、１！▽\nカスパーがやられました！！\n人工知能により\n自律爆破が決議されました！！\n\0":
'???',

# Ritsuko Akagi 
"負けた。\n…完敗だわ。\n\0":
'???',

# Shigeru Aoba
"チィ！！▽\nカスパー、\n１８秒後に乗っ取られます。\n\0":
'???',

# Ritsuko Akagi 
"わかってるわよ！！\n\0":
'???',

# Ritsuko Akagi 
"さあ、マギを返しなさい！！\n\0":
'???',

#
# ./USRDIR/event/cev1103.har_EXTRACT/cev1103.evs
#
# Misato Katsuragi 
"忙しそうね。\n\0":
'???',

# Ryoji Kaji
"いや、そうでもないさ。\n\0":
'???',

# Misato Katsuragi 
"とぼけないで。▽\n日本政府内務省調査部所属、\n加持リョウジ。\nここに来た本当の目的は何？\n\0":
'???',

# Ryoji Kaji
"君に会いに来ただけさ。\nそれじゃ不満かな？\n\0":
'???',

# Misato Katsuragi 
"色々、かぎ回っているよう\nだけど…、あんまり過ぎると\nヤケドじゃすまないわよ。\n\0":
'???',

# Ryoji Kaji
"承知の上さ。\nただ、君に隠し事をしていた事は\n謝るよ。\n\0":
'???',

# Misato Katsuragi 
"政府の狙いは何？\n\0":
'???',

# Ryoji Kaji
"誰に頼まれている事でもないさ。\n俺の独断でね。\n\0":
'???',

# Ryoji Kaji
"俺の動きなんて、\nとっくに気づかれているさ。\n\0":
'???',

# Misato Katsuragi 
"じゃあ、なぜ…。\n\0":
'???',

# Ryoji Kaji
"忠告、ありがとう。\n\0":
'???',

#
# ./USRDIR/event/a007.har_EXTRACT/a007.evs
#
# Kaworu Nagisa 
"さあ、行くよ。\nおいで、アダムの分身、\nそしてリリンのしもべ…。\n\0":
'???',

# Makoto Hyuga, Male Staff
"エヴァ弐号機、起動！\n\0":
'???',

# Misato Katsuragi 
"そんな、バカな！！\nまさか、…アスカなの？\n\0":
'???',

# Kozo Fuyutsuki
"何だと…！？\n\0":
'???',

# Female Staff
"えっ？\n弐号機が！？\n\0":
'???',

# Maya Ibuki, Male Staff
"弐号機にはエントリープラグが\n挿入されていません。\n無人で動いています！\n\0":
'???',

# Misato Katsuragi 
"誰もいない？\nどういう事！！\n\0":
'???',

# Kozo Fuyutsuki
"無人…だと…？\n\0":
'???',

# Female Staff
"そんな事って…。\n\0":
'???',

# Makoto Hyuga, Male Staff
"セントラルドグマに、\nΑΤフィールドの発生を確認！\n\0":
'???',

# Misato Katsuragi 
"弐号機？\n\0":
'???',

# Kozo Fuyutsuki
"弐号機か？\n\0":
'???',

# Makoto Hyuga, Male Staff
"パターン青。\n間違いありません。\n使徒です。\n\0":
'???',

# Kozo Fuyutsuki
"何っ！？\n\0":
'???',

# Misato Katsuragi 
"使徒？\nあの少年が？\n\0":
'???',

# Kozo Fuyutsuki
"ゼーレからの贈り物…。\nそうか、こういう事だったのか。\n\0":
'???',

# Male Staff
"あれは、フィフス・チルドレン…。\n\0":
'???',

# Gendo Ikari
"いかなる方法を以ってしても、\n目標のターミナルドグマへの侵入を\n阻止しろ！\n\0":
'???',

# Kozo Fuyutsuki
"いかなる方法を持ってしても構わん、\n目標のターミナルドグマへの侵入を\n阻止しろ！\n\0":
'???',

# Misato Katsuragi 
"何としてでも\nターミナルドグマの侵入を\n阻止しなければ。\n\0":
'???',

# Female Staff
"早く、\nターミナルドグマの侵入を\n阻止しなければ！\n\0":
'???',

# Kozo Fuyutsuki
"まさか、ゼーレが\n直接送り込んでくるとはな。\n\0":
'???',

# Gendo Ikari
"やはり老人は\n予定を一つ繰り上げるつもりだ。\n我々の手で。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le507.evs
#
# Kaworu Nagisa 
"そうだね。\nでも僕は上手くやっているだろ？\n\0":
'???',

# Kaworu's Shadow [Leliel]
"思い上がりだよ。\n上手くやっているのは、\n壊したくないものがあるから。▽\nそれは弱さの証明さ。\n君はリリンから弱さを学んだだけだ。\n\0":
'???',

#
# ./USRDIR/event/cev0104.har_EXTRACT/cev0104.evs
#
# Misato Katsuragi 
"シンちゃーん！\nちょっと来てー。\n\0":
'???',

# Shinji Ikari
"はぁい。\n\0":
'???',

# Shinji Ikari
"な、何やってるんですか！？\n\0":
'???',

# Misato Katsuragi 
"ん〜、ヨガのエクササイズ…。\n出てきたお腹、\n引っ込めようと思って。▽\nチョッチ…、その本のポーズを\nとりたいんだけど…、\n支えてくれないかしら…。\n\0":
'???',

# Shinji Ikari
"もう、ビール飲むのやめたら\nいいじゃないですか。\nそしたら痩せますよ。\n\0":
'???',

# Misato Katsuragi 
"ヤーダ！\nビール飲めなくなるなんて\n生き地獄だわ。\n\0":
'???',

# Shinji Ikari
"まったく、\n子供じゃないんだから…。▽\nほら、これでいいですか？\nミサトさんも、背中伸ばして！\n\0":
'???',

# Misato Katsuragi 
"えーぃ…ぃぃぃ。\nアン…、辛いぃ…。\nもー、ダメェッ！！\n\0":
'???',

# Shinji Ikari
"あぅ！\n\0":
'???',

# Misato Katsuragi 
"大丈夫、シンちゃん！？\n\0":
'???',

# Shinji Ikari
"は…、はぁい…。\n\0":
'???',

# Misato Katsuragi 
"うーん、いきなり上級者向け\nポーズは無理みたい。\n\0":
'???',

# Shinji Ikari
"は、早くどいてくれませんか…。\n\0":
'???',

# Misato Katsuragi 
"あら、あらあら…。\nそうね、ゴメン…。\n\0":
'???',

# Misato Katsuragi 
"…やっぱ、慣れない事を\nするもんじゃないわね。\n\0":
'???',

# Shinji Ikari
"そうですね。\n\0":
'???',

# Misato Katsuragi 
"あーぁ。\nとりあえずビールでも飲もうかな。\n\0":
'???',

# Shinji Ikari
"またぁ…。\nお腹出ますよ。\n\0":
'???',

# Misato Katsuragi 
"イケズぅ〜〜〜〜。\nお腹出たくらいで、\n私の事嫌いになっちゃうの？\n\0":
'???',

# Shinji Ikari
"そんな事は…ないですよ。\n\0":
'???',

# Misato Katsuragi 
"えっへっへー♪\nだから、シンちゃん大好きよ。\n\0":
'???',

# Shinji Ikari
"…はいはい。\n\0":
'???',

# Misato Katsuragi 
"もし、人類がエヴァを\n必要としなくなっても\nあなたはここにいて。\n\0":
'???',

# Misato Katsuragi 
"…なーんてね、そんな\nワガママは言えないわよね。\nあなたにはあなたの将来があるから。\n\0":
'???',

# Shinji Ikari
"まだ、将来の事なんて\n考えてませんから。\n\0":
'???',

# [Text Only - No Designated Speaker]
"他に何て言えばいいのか\nわからなかった。\n気を利かせたつもりでもなかったし。▽\nミサトさんは、意外と幼い顔をする。\n他でもこんな表情をするのかな…。\n\0":
'???',

# Misato Katsuragi 
"じゃ、さ。\nさっきのヨガ、初心者ポーズから\n始めるから手伝って！\n\0":
'???',

# Shinji Ikari
"ダメだこりゃ…。\n\0":
'???',

#
# ./USRDIR/event/cev1409.har_EXTRACT/cev1409.evs
#
# Asuka Soryu Langley
"ねえ、ヒカリってさ、\n鈴原が好きなの？\n\0":
'???',

# Hikari Horaki
"えぇええぇ！？\nそ、そんな…、私は…。\n\0":
'???',

# Asuka Soryu Langley
"一途な視線っての？\n鈴原の事、よく見てるから。\n\0":
'???',

# Hikari Horaki
"あ、や…、私…。\nみんなにも、バレてるのかな？\n\0":
'???',

# Asuka Soryu Langley
"まー、鈴原本人と相田とシンジの\n３バカトリオは気付いてないわよ。\n\0":
'???',

# Hikari Horaki
"そう…かな？\n碇君、繊細な感じがするし、\nそういうのには敏感なんじゃない？\n\0":
'???',

# Asuka Soryu Langley
"逆、逆！！\nアイツが一番鈍感なんだから。\n人との付き合い方、知らないし。\n\0":
'???',

# Asuka Soryu Langley
"でもさ…、あの万年ジャージの\nどこがいいの？\n\0":
'???',

# Hikari Horaki
"優しいところ…。\n\0":
'???',

# Asuka Soryu Langley
"へー………。\nアイツがねぇ…。▽\nで、告白とかしないの？\n\0":
'???',

# Hikari Horaki
"無理だよ。\n私、嫌われてるもん。\n\0":
'???',

# Asuka Soryu Langley
"じゃあ、\n好きになってもらえるような\n努力をすればいいんじゃない？\n\0":
'???',

# Hikari Horaki
"どうすればいいのかな…。\n\0":
'???',

# Asuka Soryu Langley
"自分の気持ちに\n素直になってみれば？\nスキって気持ちにさ。\n\0":
'???',

#
# ./USRDIR/event/cev1209.har_EXTRACT/cev1209.evs
#
# Toji Suzuhara 
"ドナー、見つかるんかな。\nそう、やたらに見つかるもんでも\nないんやな…。\n\0":
'???',

#
# ./USRDIR/event/cev1607.har_EXTRACT/cev1607.evs
#
# Ryoji Kaji
"わーっ、バカ！！\n何してるんだ、やめろって！\n\0":
'???',

# Toji Suzuhara 
"アカン、アカンて！！\n何さらすんじゃ、やめい！！\n\0":
'???',

# Hikari Horaki
"駄目っ！\nショックだろうけど\n乱暴は駄目よ！！\n\0":
'???',

# Kensuke Aida
"いてーっ！\n八つ当たりすんなよ！！\nいてぇー、いててててて！！\n\0":
'???',

# Rei Ayanami 
"落ち着いて…。\n\0":
'???',

# Pen Pen
"グギャアアアアアアアア！！！\n\0":
'???',

# Delivery Man
"ちわーす。\n\0":
'???',

# Pen Pen
"グワワッ。\n\0":
'???',

# Pen Pen
"グェ〜…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"包みを開けると…………、▽\n何と、犬のぬいぐるみが\n入っていた。\n\0":
'???',

# Pen Pen
"グワーーーー♪\nクワクワ、クワッ！！\n\0":
'???',

# Pen Pen
"クェ〜〜〜〜〜。\n\0":
'???',

# Misato Katsuragi 
"あ、懸賞…当たったの！？\nあらー、ペンペンお気に入りの\nワンちゃんじゃない♪▽\nうーん、どうせならビール券が\n当たって欲しかったのに…。\nんーん、よかったわねぇー。\n\0":
'???',

# Shinji Ikari
"犬のヌイグルミだ。\nペンペン、この犬好きだったっけ。\nよかったね…。\n\0":
'???',

# Asuka Soryu Langley
"犬のヌイグルミだわ。\nあら、これ動くんだ。\nペンペン、これが欲しかったんだ。\n\0":
'???',

# Ritsuko Akagi 
"まっ…、犬のヌイグルミ。\nあぁ、あなたが夢中になってる\nあの犬ね…。\n\0":
'???',

# Ryoji Kaji
"おぉ、犬のヌイグルミか。\nそうかそうか、当たったぞ。\nよかったな、ペンペン。\n\0":
'???',

# Toji Suzuhara 
"お、懸賞当たったんや。\n犬のヌイグルミやんけ！\n運がええのぅ、ペンペン。\n\0":
'???',

# Hikari Horaki
"わぁ、犬のヌイグルミ。\n当たったのね、ペンペン。\nそうそう、これ動くのよね。\n\0":
'???',

# Kensuke Aida
"あ、あの芸する犬のヌイグルミ。\n当たったんだ、お前…。\n頑張った甲斐があったなぁ。\n\0":
'???',

# Rei Ayanami 
"犬…。\nあなた、これが欲しかったのね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"いよいよ、ヌイグルミに\n電源スイッチを入れる。\n\0":
'???',

# Pen Pen
"グワワーーーーー！！\nグワッ、グワッグワー！\n\0":
'???',

# [Text Only - No Designated Speaker]
"伴侶を得た（？）喜びで、\nペンペンは舞い上がった。▽\n…だが、その時テレビが\n衝撃の事実を告白した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"またいい事あるさ。\n頑張れ、ペンペン！\n涙を越えて男になれよ！\n\0":
'???',

# Female Announcer
"さぁ、今日はＣＭやドラマで\n大活躍のカリスマワンちゃん\nモカ君の登場です！！\n\0":
'???',

# Pen Pen
"ギャッ！！\n\0":
'???',

# Misato Katsuragi 
"ちょっ、これさっきの\n犬じゃないの！？\n\0":
'???',

# Shinji Ikari
"あ、あの犬…！！\n\0":
'???',

# Asuka Soryu Langley
"あっ、さっきの犬！\n\0":
'???',

# Ritsuko Akagi 
"さっきの犬だわ…。\n\0":
'???',

# Ryoji Kaji
"お、おい。\nあの犬だぞ、ペンペン！！\n\0":
'???',

# Toji Suzuhara 
"おい、さっきの犬やんけ！！\n\0":
'???',

# Hikari Horaki
"ああっ、この犬！！\n\0":
'???',

# Kensuke Aida
"タイムリー！！\nさっきの犬だぞ！！\n\0":
'???',

# Rei Ayanami 
"…あ、今の犬は。\n\0":
'???',

# Pen Pen
"クゥエ〜〜〜〜〜〜。\n\0":
'???',

# Female Announcer
"モカ君は３歳のオス。\nとってもお利口で様々な演技を\n披露してくれます。\n\0":
'???',

# Pen Pen
"クェ！？\n\0":
'???',

# Misato Katsuragi, Shinji Ikari, Asuka Soryu Langley, Ritsuko Akagi, Ryoji Kaji, Toji Suzuhara, Hikari Horaki, Kensuke Aida, Rei Ayanami
"…オス？\n\0":
'???',

# Female Announcer
"しかも、驚くべき事に\nこの毛皮を脱ぐと…、\n\0":
'???',

# Female Announcer
"モカ君の正体は猫！！\nだったのでーす！！\n\0":
'???',

# Pen Pen
"！！！！！！！！！！！！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"ペンペンの中で、何かが\n音を立てて崩れていった…。\n\0":
'???',

# Pen Pen
"…クゥゥゥゥゥゥゥ！！！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"ペンペンは、暴れまわった！\n\0":
'Pen Pen went on a rampage!\n\0',

# Misato Katsuragi 
"コラ！！\nペンペンったら、やめなさい！！\n\0":
'Hey!!\n Pen Pen, honestly! Quit it!!\n\0',

# Shinji Ikari
"や、やめろよ。\nペンペン〜！！\n\0":
'C-cut it out,\n Pen Pen!!\n\0',

# Asuka Soryu Langley
"ぎゃー、何すんの！？\nよしてよ、ペンペン。\n\0":
'???',

# Ritsuko Akagi 
"ペンペン、何をするの！\nおやめなさい！！\n\0":
'Pen Pen, what are you doing?\n Stop that at once!\n\0'
}
