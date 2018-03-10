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
# ./USRDIR/event/a003.har_EXTRACT/a003.evs
#
# Misato Katsuragi 
"来たわね。\n今度は抜かりないわよ！\n\0":
'???',

# Kozo Fuyutsuki
"来たな。\n\0":
'???',

# Female Staff
"来ましたね。\n\0":
'???',

# Misato Katsuragi 
"今回の作戦は、前も言ったとおり、\nユニゾンが高いパイロット二人によ\nる同時荷重攻撃により、目標を殲滅。▽\nで〜、今回のパイロットは………。\n\0":
'???',

# Kozo Fuyutsuki
"今回のパイロットは………、\n\0":
'???',

# Female Staff
"今回のパイロットは……、\n\0":
'???',

# Misato Katsuragi, Female Staff
"シンジ君と…\n\0":
'Shinji-kun and...\n\0',

# Kozo Fuyutsuki
"碇シンジと…\n\0":
'Shinji Ikari and...\n\0',

# Misato Katsuragi 
"アスカと…\n\0":
'Asuka and...\n\0',

# Kozo Fuyutsuki
"惣流・アスカ・ラングレーと…\n\0":
'Asuka Soryu Langley and...\n\0',

# Female Staff
"アスカさんと…\n\0":
'Asuka-san and...\n\0',

# Misato Katsuragi 
"レイと…\n\0":
'Rei and...\n\0',

# Kozo Fuyutsuki
"綾波レイと…\n\0":
'Rei Ayanami and...\n\0',

# Female Staff
"レイさんと…\n\0":
'???',

# Misato Katsuragi, Female Staff
"トウジ君と…\n\0":
'???',

# Kozo Fuyutsuki
"鈴原トウジと…\n\0":
'???',

# Misato Katsuragi, Female Staff
"カヲル君と…\n\0":
'???',

# Kozo Fuyutsuki
"渚カヲルと…\n\0":
'???',

# Misato Katsuragi 
"アスカ。\n\0":
'???',

# Female Staff
"アスカさん。\n\0":
'???',

# Female Staff
"レイさん。\n\0":
'???',

# Misato Katsuragi, Female Staff
"トウジ君。\n\0":
'???',

# Kozo Fuyutsuki
"鈴原トウジ。\n\0":
'???',

# Misato Katsuragi, Female Staff
"カヲル君。\n\0":
'???',

# Kozo Fuyutsuki
"渚カヲル。\n\0":
'???',

# Misato Katsuragi 
"あなた達、二人にやってもらいます。\n\0":
'???',

# Kozo Fuyutsuki
"君達、二人にやってもらう。\n\0":
'???',

# Female Staff
"この二人にお願いします。\n\0":
'???',

# Shinji Ikari
"え、えぇっ！？\n\0":
'???',

# Asuka Soryu Langley
"まっ、トーゼンよね！！\n\0":
'???',

# Toji Suzuhara 
"あちゃー、当てられてもうた。\n\0":
'???',

# Kaworu Nagisa , Maya Ibuki 
"フフ…。\n\0":
'???',

# Shinji Ikari
"あ、でも、初号機は凍結中で\n出られないんじゃぁ…。\n\0":
'???',

# Misato Katsuragi 
"大丈夫！！\nさっき、ちょうど凍結解除命令が\n降りたのよ。▽\nだから頑張って〜ン、\nシンジ君。\n\0":
'???',

# Kozo Fuyutsuki
"大丈夫だ。\nちょうど、凍結解除命令が\n降りたばかりだ。▽\n頑張ってくれたまえ。\n\0":
'???',

# Female Staff
"それは大丈夫です。\nつい先ほど凍結解除命令が\n降りたそうなんです。▽\n初号機は現在、発進準備を\n進めています。\n\0":
'???',

# Misato Katsuragi 
"今回の作戦の全ては、二人の\nユニゾンにかかってるわ。\nあんた達、任せたわよ！\n\0":
'???',

# Kozo Fuyutsuki
"今回の作戦の全ては、二人の\n協調性にかかっている。\n…頼んだぞ。\n\0":
'???',

# Female Staff
"今回の作戦の勝敗は、二人の\nユニゾンにかかっています。\n頑張って下さい！\n\0":
'???',

# Misato Katsuragi 
"パイロットの人数が足りない。\nこれじゃ、同時荷重攻撃は\n不可能だわ。▽\nああ、ここまでなの…！？\n\0":
'???',

# Kozo Fuyutsuki
"くっ…、パイロットの人数が足らん。\nこれでは、同時荷重攻撃は不可能だ。\nもはや、これまでか…。\n\0":
'???',

# Female Staff
"パイロットの人数が足りません！\nこれでは、同時荷重攻撃の作戦を\n遂行する事が出来ません！！\n\0":
'???',

# Misato Katsuragi 
"パイロットのΑΤがこんな状態じゃ、\nとても同時荷重攻撃なんか\n出来ないわ………。▽\n何とか、何とかならないの！！\nああ、こんな事って…。\n\0":
'???',

# Kozo Fuyutsuki
"パイロットのΑΤがこんな状態では\nとても同時荷重攻撃は無理だ…。\n他に打つ手は…、他に何か…。\n\0":
'???',

# Female Staff
"くっ…、\nパイロットのΑΤがこんな状態では\nとても同時荷重攻撃は無理だわ！！▽\nただ、指をくわえているしか\nないの…。\n\0":
'???',

#
# ./USRDIR/event/b2s17.har_EXTRACT/b2s17.evs
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
# ./USRDIR/event/levent.har_EXTRACT/le006.evs
#
# Misato Katsuragi, Makoto Hyuga
"エヴァの強制サルベージ！？\n\0":
'???',

# Male Staff
"エヴァの強制サルベージですか！？\n\0":
'???',

# Ritsuko Akagi 
"可能と思われる唯一の方法よ。▽\n９２２個、現存する全ての\nΝ爆雷を中心部に投下。▽\nその瞬間的エネルギー量により、\n使徒が形成しているディラックの\n海を破壊するしかないわ。\n\0":
'???',

# Maya Ibuki 
"現在、可能と思われる\n唯一の方法です。▽\n９２２個、現存する全ての\nΝ爆雷を中心部に投下。▽\nその瞬間的エネルギー量により、\n使徒が形成している\nディラックの海を破壊します。\n\0":
'???',

# Female Staff
"現在、可能と思われる唯一の\n方法です。▽\n９２２個、現存する全ての\nΝ爆雷を中心部に投下。▽\nその瞬間的エネルギー量により、\n使徒が形成している\nディラックの海を破壊します。\n\0":
'???',

# Misato Katsuragi 
"でも、これではエヴァの機体がどう\nなるか、パイロットがどうなるか。\n救出作戦とは言えないわ。\n\0":
'???',

# Makoto Hyuga, Male Staff
"でも、それではエヴァの機体が…、\nパイロットだってどうなるか。\n救出作戦とは言い難いのでは…。\n\0":
'???',

# Ritsuko Akagi 
"作戦は、エヴァの機体回収を\n最優先とします。▽\n例えボディが寸断されていても\n構わないわ。▽\nこの際、\nパイロットの生死は問いません。\n\0":
'???',

# Maya Ibuki 
"しかし、他に方法がありません。\n可能性がある事だけでも、\n幸運な事なんですから。\n\0":
'???',

# Female Staff
"他に方法がないんです。\nこのまま何もせずにいれば、\nそれこそパイロットは助かりません。\n\0":
'???',

#
# ./USRDIR/event/n002.har_EXTRACT/n002.evs
#
# Misato Katsuragi, Female Staff
"ラミエル\n\0":
'???',

# Misato Katsuragi, Female Staff
"国連艦隊、新型エヴァの部品を搬送中、\n太平洋上にて、突如使徒が出現。\n襲撃を受けました。\n\0":
'???',

# Female Staff, Misato Katsuragi 
"これにより、目標を第３新東京市にて迎撃\n\0":
'???',

# Misato Katsuragi, Female Staff
"国連艦隊の戦闘記録分析結果により、\n目標は一定距離内に侵入した外敵を、\n加粒子砲で自動排除、展開されるΑΤフィールドは、\n相転移空間を肉眼で確認出来る程、超強力なものでした。\n\0":
'???',

# Misato Katsuragi, Female Staff
"これを踏まえ、ポジトロンスナイパーライフルを使用した、\n長距離からの一点狙撃する作戦を決行\n\0":
'???',

# Misato Katsuragi, Female Staff
"この作戦に参加した機体は…、\n\0":
'???',

#
# ./USRDIR/event/n009.har_EXTRACT/n009.evs
#
# Misato Katsuragi, Female Staff
"これより、Ａ−１７、\n使徒捕獲作戦の結果報告を行います。\n\0":
'???',

# Misato Katsuragi, Female Staff
"浅間山火口内にて発見された使徒を捕獲するため\n\0":
'???',

# Misato Katsuragi, Female Staff
"エヴァ弐号機で火口内に沈降、\n目標への接触を図りました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"サンダルフォン\n\0":
'???',

# Misato Katsuragi, Female Staff
"深度１７８０ｍにて、目標を発見。\n\0":
'???',

# Misato Katsuragi, Female Staff
"捕獲を試みますが、孵化が予想より早く失敗し、\n\0":
'???',

# Misato Katsuragi, Female Staff
"作戦を使徒殲滅に変更します。\n\0":
'???',

# Misato Katsuragi, Female Staff
"高温高圧という不利な状況下での\n戦闘に苦戦を強いられますが、\n\0":
'???',

# Misato Katsuragi, Female Staff
"冷却液による熱膨張を利用した攻撃を敢行し、\n\0":
'???',

# Misato Katsuragi, Female Staff
"使徒殲滅に成功します。\n\0":
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
# ./USRDIR/event/f058.har_EXTRACT/f058.evs
#
# Shinji Ikari
"どうしてみんな、\n僕に優しくしてくれないんだ…。\n\0":
'???',

# Rei Ayanami 
"冷たくされるのは嫌いなの？\n\0":
'???',

# Shinji Ikari
"あたりまえじゃないか！！\n冷たくされるのが\n嬉しい人なんかいないよ！\n\0":
'???',

# Ritsuko Akagi 
"シンジ君は自分の事だけで\n精いっぱいなのね。\n\0":
'???',

# Asuka Soryu Langley
"バカみたい。\n他人の中の自分ばかり気にして。▽\n本当のアンタは何やってるのよ。\nつらい事から目を逸らして、\n逃げて、それだけじゃない。\n\0":
'???',

# Shinji Ikari
"違うよ、ちゃんと向き合ってるさ。\nだから、つらいんだ。\n痛いんだ！！\n\0":
'???',

# Rei Ayanami 
"でも、楽しい事だけを見つめて\n生きる事は出来ない。\n\0":
'???',

# Shinji Ikari
"じゃあ、ずっと僕は一人なのか…。\n\0":
'???',

# Rei Ayanami 
"いいえ、みんなが一人なのよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、シンジの声が\n聞こえた気がした。\n\0":
'???',

#
# ./USRDIR/event/f004.har_EXTRACT/f004.evs
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
'???',

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
# ./USRDIR/event/f015.har_EXTRACT/f015.evs
#
# Asuka Soryu Langley
"あら、電気が戻った？\n\0":
'???',

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
'???',

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
'???',

# Rei Ayanami 
"私は私よ。\nあなたとは違うわ。\n\0":
'???',

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
# ./USRDIR/btl/b2event.har_EXTRACT/b2a01.evs
#
# Shigeru Aoba, Male Staff
"使徒落下最終予想範囲、出ました！\n\0":
'???',

#
# ./USRDIR/event/f011.har_EXTRACT/f011.evs
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
# ./USRDIR/event/f089.har_EXTRACT/f089.evs
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
# ./USRDIR/event/b2s05.har_EXTRACT/b2s05.evs
#
# Shinji Ikari, Kaworu Nagisa, Asuka Soryu Langley, Rei Ayanami, Toji Suzuhara
"ΑΤフィールド、全開！！\n\0":
'???',

#
# ./USRDIR/event/a006.har_EXTRACT/a006.evs
#
# Kozo Fuyutsuki
"それは…、どういう事だ？\n\0":
'???',

# Female Staff
"青からオレンジ…、\nそれはどういう事でしょうか？\n\0":
'???',

# Ritsuko Akagi 
"このまま膠着状態を\n続けるしかないみたいね…。\n\0":
'???',

# Makoto Hyuga
"このまま膠着状態を\n続けるしかないのか…。\n\0":
'???',

# Female Staff
"このまま膠着状態を\n続けるしかないようですね…。\n\0":
'???',

# Ritsuko Akagi 
"相手がどんな出方をして\nくるのか予想が付かない。\n接近戦は危険だわ。\n\0":
'???',

# Kozo Fuyutsuki
"下手に近づくのは危険だな。\n接近戦を避け、十分な距離をとり\nながら攻撃する方がいいだろう。\n\0":
'???',

# Female Staff
"接近戦は避けた方がいいですね。\n目標の攻撃範囲から外れるよう\n常に動き続けた方がよさそうです。\n\0":
'???',

# Makoto Hyuga, Male Staff
"パイロット、準備ＯＫです。\n\0":
'???',

# Misato Katsuragi 
"ええ、すぐ行くわ。\n\0":
'???',

# Kozo Fuyutsuki
"そうか、では作戦を伝えよう。\n\0":
'???',

# Female Staff
"それでは作戦を伝え、\n出撃させましょう。\n\0":
'???',

#
# ./USRDIR/event/f040.har_EXTRACT/f040.evs
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
# ./USRDIR/event/b2s30.har_EXTRACT/b2s30.evs
#
# Ritsuko Akagi 
"間に合わない！？\n\0":
'???',

# Female Staff
"やっぱり…、無理？\n間に合わないわ！！\n\0":
'???',

#
# ./USRDIR/event/f020.har_EXTRACT/f020.evs
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
# ./USRDIR/event/bs066.har_EXTRACT/bs066.evs
#
# Misato Katsuragi 
"よし！\nじゃ、シミュレーションを\n続行するわよ。\n\0":
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
# ./USRDIR/event/a016.har_EXTRACT/a016.evs
#
# Misato Katsuragi 
"今日教えるのは、大きく分けて二つ。\n\0":
'???',

# Misato Katsuragi 
"一つはあなたのΑΤとエヴァの関係。\n\0":
'???',

# Misato Katsuragi 
"もう一つはエヴァとパイロット間の\nフィードバックよ。\n\0":
'???',

# Misato Katsuragi 
"じゃあ、一つ目。\nパイロットのΑΤと\nエヴァの関係から説明するわ。\n\0":
'???',

# Misato Katsuragi 
"パイロットとエヴァとのシンクロ率。\nそして、エヴァのΑΤフィールドの\n強度。▽\nこれらは、パイロット自身の\nΑΤの高さに比例します。▽\nシンクロ率とΑΤフィールドは、\nそれぞれ、エヴァの攻撃力と防御力、\nと考えて良いわ。\n\0":
'???',

# Shinji Ikari
"…じゃあ、僕のΑΤが高いと\nエヴァの攻撃力と防御力が上がる…。\n\0":
'???',

# Misato Katsuragi 
"その通り、さすがネ！\nあなたのΑΤ次第でエヴァは\n強くも弱くもなるってことよ。\n\0":
'???',

# Misato Katsuragi 
"戦闘の技術も大切だけど、\n使徒に勝つにはあなたの心の状態、\nΑΤがより大きな鍵になるの。▽\nだから、エヴァのパイロットは\n日頃からΑΤを高めるよう\n努めないといけないのよ。\n\0":
'???',

# Misato Katsuragi 
"で…、もう一つがエヴァと\nパイロット間のフィードバックね。\n\0":
'???',

# Misato Katsuragi 
"エヴァはあなたが動きを頭の中に\n思い描くだけで操縦出来るでしょ？▽\nそれはエヴァとパイロットの神経を\n接続してあなたのイメージをエヴァ\nにフィードバックしているからなの。\n\0":
'???',

# Misato Katsuragi 
"で、ここからが本題なんだけど、\nエヴァがダメージを受けたとき、\n幻痛が起こるでしょ？\n\0":
'???',

# Shinji Ikari
"ゲンツウ…？\n\0":
'???',

# Misato Katsuragi 
"そ、幻痛。\nエヴァがダメージを受けた時に\nあなたが感じた痛みのこと。▽\n幻痛は、エヴァのダメージが\n神経接続を通じて、あなたに\nフィードバックされて伝わるの。\n\0":
'???',

# Shinji Ikari
"…あの感覚は\nそのために起こるんですね。\n\0":
'???',

# Misato Katsuragi 
"あなたにフィードバックされた\nダメージは不快な記憶を生み、\nあなたのΑΤは低下する。▽\nΑΤが低下すると………、\n\0":
'???',

# Shinji Ikari
"エヴァのシンクロ率と\nΑΤフィールドも落ちてしまう。\n\0":
'???',

# Misato Katsuragi 
"ご名答！\n\0":
'???',

# Misato Katsuragi 
"エヴァの耐久力が残っていても、\nΑΤが落ちればエヴァの戦闘力も\nそれに比例して低下し、\n\0":
'???',

# Misato Katsuragi 
"シンクロ率が３０以下になると、\nもう、エヴァを動かせなくなるわ。\n\0":
'???',

# Shinji Ikari
"…動かせなくなる？\n\0":
'???',

# Misato Katsuragi 
"逆にあなたが使徒に\nダメージを与えると、\n気分が高揚してΑΤが上昇する。\n\0":
'???',

# Misato Katsuragi 
"とにかくエヴァで使徒に勝つため\nには、あなたのΑΤがすごーく\n重要って事をよく覚えておいて。\n\0":
'???',

#
# ./USRDIR/event/n011.har_EXTRACT/n011.evs
#
# Misato Katsuragi, Female Staff
"レリエル\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標は第３新東京市直上に突如出現\n\0":
'???',

# Misato Katsuragi, Female Staff
"エヴァ初号機による牽制攻撃を行うが\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標の本体ともいえるディラックの海に飲み込まれ、\n\0":
'???',

# Misato Katsuragi, Female Staff
"初号機は消失します。\n\0":
'???',

# Misato Katsuragi, Female Staff
"エヴァ初号機救出のため、強制サルベージ作戦を実行。\n\0":
'???',

# Misato Katsuragi, Female Staff
"しかし、サルベージ作戦開始直前、\n\0":
'???',

# Misato Katsuragi, Female Staff
"エヴァ初号機は自ら目標を引き裂き、脱出します。\n\0":
'???',

# Misato Katsuragi, Female Staff
"しかし、どのような方法をもって初号機が脱出できたのか？\n\0":
'???',

# Misato Katsuragi, Female Staff
"詳細は不明。更に現在調査中です\n\0":
'???',

# Misato Katsuragi, Female Staff
"エヴァ初号機救出のため、強制サルベージ作戦を立案。\n\0":
'???',

# Misato Katsuragi, Female Staff
"理論上での策ではありましたが作戦は実行\n\0":
'???',

# Misato Katsuragi, Female Staff
"作戦の結果、エヴァ初号機のサルベージには成功。\n\0":
'???',

# Misato Katsuragi, Female Staff
"しかし、不完全な虚数空間への干渉により、\n\0":
'???',

# Misato Katsuragi, Female Staff
"他のパイロットを失うという、致命的な損害を受けてしまいました。\n\0":
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
# ./USRDIR/btl/tabris.har_EXTRACT/bk058.evs
#
# Shinji Ikari
"カヲル君………、\nどうして…………。\n\0":
'???',

# Shinji Ikari
"………………………。\n僕達…やり直せるよね？\n\0":
'???',

# Shinji Ikari
"……………！？▽\nカヲル君…！！\nカヲル君、カヲル君、カヲル君！！▽\nずるいよ…、そんなのってないよ！\n何で一人で行くんだよ！！！\nワァァァァァァァァーーーーッ！\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le005.evs
#
# Shinji's Shadow [Leliel]
"自分が怖い？\n他人の自分が…。\n\0":
'???',

# Asuka's Shadow [Leliel]
"恐れているのね…。\n一人になる事を。\n\0":
'???',

# Rei's Shadow [Leliel]
"…それで結局、\n何のために生きているの？\n\0":
'???',

# Toji's Shadow [Leliel]
"なあやっぱり、\n自分を演じていくのんって\nしんどいやろ？\n\0":
'???',

# Kaworu's Shadow [Leliel]
"繰り返すよ。\n本来の目的を忘れてはいないかい？\n\0":
'???',

#
# ./USRDIR/event/b2s10.har_EXTRACT/b2s10.evs
#
# Asuka Soryu Langley
"これを失敗したら、\n多分、弐号機を下ろされる。\nミスは許されないわよ、アスカ。\n\0":
'???',

#
# ./USRDIR/event/f013.har_EXTRACT/f013.evs
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
'???',

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
# ./USRDIR/event/f036.har_EXTRACT/f036.evs
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
'???',

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
# ./USRDIR/event/a005.har_EXTRACT/a005.evs
#
# Female Staff
"あぁっ…！！\n\0":
'???',

# Kozo Fuyutsuki
"なんという破壊力だ…。\n防衛ラインの迎撃システムを\n一瞬にして消し去るとは。\n\0":
'???',

# Female Staff
"凄まじい破壊力です。\n防衛ラインの迎撃システムを\n一掃しました。\n\0":
'???',

# Female Staff
"あの破壊力をもってすれば\nジオフロントの特殊装甲板は\n簡単に破壊されてしまいます。\n\0":
'???',

# Kozo Fuyutsuki
"ひとつ誤まれば、被害は甚大だぞ。\n\0":
'???',

# Female Staff
"これは…、\n指揮を間違えば、\n大変な事になりますね…。\n\0":
'???',

# Kozo Fuyutsuki
"一分でも惜しい。\n今から指示をだそう。\n\0":
'???',

# Female Staff
"了解。\nパイロットへの指示後、\nすぐに発進させます。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le521.evs
#
# Kaworu Nagisa 
"そうじゃない！\n僕はヒトを知るために、\nヒトと接していただけだ。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"フフ、そうは見えないよ。▽\nリリンの中は暖かくて、\n気持ちよかったんだろ？\nもう、すべてを忘れてしまうほどに。\n\0":
'???',

#
# ./USRDIR/event/f044.har_EXTRACT/f044.evs
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
'???',

# Pen Pen
"…かもね。\n\0":
'???',

# Shinji Ikari
"でも、僕の声だ…。\n夢なのかな…。\n\0":
'???',

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
'???',

# Shinji Ikari
"学校はいいよ。\n\0":
'???',

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
'???',

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
# ./USRDIR/event/f051.har_EXTRACT/f051.evs
#
# [Character: Scene with Maya]
#
# Girlfriends
"彼氏が、女引っ張り込んできて…、\nね、一日でいいから泊めて。\n\0":
'???',

# Maya Ibuki [Flashback]
"またぁ？\n別れたらって言ったのに…。\nまだ、一緒にいたんだ。\n\0":
'???',

# Girlfriends
"だってさ〜、\n\0":
'???',

# Maya Ibuki [Flashback]
"私がいないと駄目なんだもん、\n…って言うの？▽\nやって行けてるじゃない、\nアンタがいなくっても。\n\0":
'???',

# Girlfriends
"マヤは、そのくらい人を好きに\nなった事がないでしょ。\n\0":
'???',

# Maya Ibuki [Flashback]
"そのくらい好きになって、\n周りが見えなくなる方が怖いわよ。\n\0":
'???',

# Girlfriends
"相変わらずね。\n学生の頃からずっと。\nでも、それじゃあ寂しいでしょ？\n\0":
'???',

# Maya Ibuki [Flashback]
"寂しい？\n\0":
'???',

# Girlfriends
"そ、まず男作りなよ。\nそれにココ、\n男呼ぶ部屋じゃないわよ。▽\nとりあえず、\n今日は私がいるから寂しくないわよ。\n\0":
'???',

# Maya Ibuki 
"何言ってんだか。\n\0":
'???',

# Maya Ibuki 
"………。▽\nでも、寂しさを紛らわすのって\nお金かかるなぁ。▽\n彼氏がいたら、\nそんなに寂しくなくなるのかな…。\n\0":
'???',

# Maya Ibuki 
"男を呼ぶ部屋ねぇ…。▽\nそんなつもりはないけれど、\nとりあえず、お部屋のインテリア\n変えてみようかしら…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、マヤの姿が頭をよぎった。\n\0":
'???',

# Shinji Ikari
"眠そうですね…。\n\0":
'???',

# Asuka Soryu Langley
"すっごいアクビ。\n眠いんですか？\n\0":
'???',

# Rei Ayanami 
"疲れているみたいですね。\n\0":
'???',

# Makoto Hyuga
"目が赤いね。\nどうしたの？\n\0":
'???',

# Shigeru Aoba
"眠そうだな、どうした？\n\0":
'???',

# Toji Suzuhara 
"マヤさーん、\nぼんやりして\nどうしはったんですか？\n\0":
'???',

# Kaworu Nagisa 
"眠そうですね、大丈夫ですか？\n\0":
'???',

# Maya Ibuki 
"大学時代の友人が泊りに来てね、\n色んな話して、あんまり寝てないの。\n\0":
'???',

# Shinji Ikari
"へぇ、楽しかったでしょうね。\n\0":
'???',

# Asuka Soryu Langley
"ふーん、どんな話をしたんですか？\n\0":
'???',

# Rei Ayanami 
"…そうですか。\n\0":
'???',

# Makoto Hyuga
"へえ、女性はお喋りが\n好きだもんなぁ。\n\0":
'???',

# Shigeru Aoba
"へぇ、いいじゃん。\nお喋りが好きなんて、\nマヤも普通の女の子だな。\n\0":
'???',

# Toji Suzuhara 
"マヤさんのお部屋、\nええなぁ〜、お泊りかぁ。\n\0":
'???',

# Kaworu Nagisa 
"それは、楽しかったでしょうね。\n\0":
'???',

# Maya Ibuki 
"私の部屋は、\n男を呼ぶ部屋じゃないって\n言われたのよ。▽\n別に呼ぶつもりなんてないし、\n呼ぶヒマもないわよ。\n\0":
'???',

# Maya Ibuki 
"でもね、人が来る事を\n意識していない生活をするのは\n寂しい事だと思ってね…。\n\0":
'???',

# Maya Ibuki 
"今度辺り、\nみんなで遊びに来て欲しいわ。\nいいかしら？\n\0":
'???',

# Shinji Ikari
"わぁ、いいんですか？\n\0":
'???',

# Asuka Soryu Langley
"じゃあ、なんか料理作って下さい。\n\0":
'???',

# Rei Ayanami 
"じゃあ、そのうちに行きます。\n\0":
'???',

# Makoto Hyuga
"へえ、いいね。\nじゃあ、みんなで\n手巻き寿司パーティーとかしようよ。\n\0":
'???',

# Shigeru Aoba
"ああ、行く行く。▽\nそういや、学生時代以来だよ。\nそんな風に、\n誰かの家で遊ぶってのは。\n\0":
'???',

# Toji Suzuhara 
"ええんですか？\nうわ〜、嬉しいー！\n絶対、行きます〜。\n\0":
'???',

# Kaworu Nagisa 
"そうですね、\nじゃあ今度みんなで\nお邪魔しますよ。\n\0":
'???',

# Maya Ibuki 
"フフフ。\n私も生活にハリが出て嬉しいわ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"昨日は何があったのだろう。▽\nマヤの気持ちを変える何かが\nあったのだろうと思うが、\n本当のところはよくわからない。\n\0":
'???',

# [Text Only - No Designated Speaker]
"マヤが深刻な顔をして、\n何かを読んでいる。▽\nいつもの詩集ではなく、\nインテリア雑誌のようだ。\n\0":
'???',

# Misato Katsuragi 
"何を読んでるのっ？\n\0":
'???',

# Gendo Ikari
"何を見ている。\n\0":
'???',

# Kozo Fuyutsuki
"部屋の模様替えかね？\n\0":
'???',

# Ritsuko Akagi 
"あら、素敵な家具ね。\n\0":
'???',

# Ryoji Kaji
"へぇ、いい部屋だね。\n\0":
'???',

# Maya Ibuki 
"帰って寝るだけの家だから、\n私の部屋、寂しいんですよ。▽\n友人も、そんなんじゃ\nお客が呼べないでしょうって\n言うものですから…。▽\nやっぱり、来客を意識するのと\nしないのでは生活はガラリと\n変わるものだと思うんですよ。\n\0":
'???',

# Misato Katsuragi 
"うんうん、いい事いうわね。\n…私のバアイ、変わらないケド。\n\0":
'???',

# Kozo Fuyutsuki
"ああ、\nそれは君のいう通りだな。\n\0":
'???',

# Ritsuko Akagi 
"本当、そうよね。\n\0":
'???',

# Ryoji Kaji
"おや、模様替えが終ったら\n招待していただけるのかな？\n\0":
'???',

# Maya Ibuki 
"私、寂しがりやなんです。\nでもそれは、自分から寂しい環境を\n作っていたからだと思います。▽\nだから、これで自分を変える\nきっかけにするんです。\n\0":
'???',

# [Text Only - No Designated Speaker]
"マヤは、無邪気に笑うと\nはにかみながら雑誌に視線を戻した。\n\0":
'???',

#
# ./USRDIR/event/b2s33.har_EXTRACT/b2s33.evs
#
# Misato Katsuragi 
"気をつけて、アスカ。▽\n攻撃のタイミングを外すと、\n目標との接触タイミングを\n見失うわよ！\n\0":
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
# ./USRDIR/event/cev0202.har_EXTRACT/cev0202.evs
#
# Shinji Ikari
"えぇぇ…！！\nここに住むって？\n\0":
'???',

# Asuka Soryu Langley
"そ、だからアンタの部屋は\n私が使うわ。\nほら、荷物運び出してよ！\n\0":
'???',

# Shinji Ikari
"そんなぁ…。\nトホホ、先が思いやられるなァ。\n\0":
'???',

# Misato Katsuragi 
"まー、まー。\n二人とも仲良くね。▽\nさ、今日は歓迎パーティーよ。\nパーッとやりましょ♪\nビール、ビール！\n\0":
'???',

#
# ./USRDIR/event/f056.har_EXTRACT/f056.evs
#
# [Character: Scene with Toji]
#
# Toji Suzuhara 
"ほれ、もっと魚食べぇよ。\n\0":
'???',

# Toji's Sister
"あんまり、おいしくない。\n\0":
'???',

# Toji Suzuhara 
"まー、そうやな。\n病院のメシって、\n味付け薄いもんな…。\n\0":
'???',

# Toji's Sister
"兄ちゃん…。\n\0":
'???',

# Toji's Sister
"私…、兄ちゃんの作った\nお好み焼き食べたいわ。▽\nツナがぎょうさん入った、\n兄ちゃんのお好み焼き。\n\0":
'???',

# Toji Suzuhara 
"う…、せやけどここは\n持ち込み禁止やしな…。\n\0":
'???',

# Toji's Sister
"やっぱ、アカンの…？\n\0":
'???',

# Toji Suzuhara 
"治ったら、なんぼでも食えるで。\n\0":
'???',

# Toji's Sister
"せや、兄ちゃんな、コレ。\n\0":
'???',

# Toji Suzuhara 
"千羽鶴やんか…。\nガッコのトモダチが\n持ってきてくれたんか？\n\0":
'???',

# Toji's Sister
"ううん。▽\nウチ、出来る事いうたら、\n折り紙くらいやもん。\n\0":
'???',

# Toji Suzuhara 
"こないいっぱい…。\nお前が折ったんか？\n\0":
'???',

# Toji's Sister
"うん、キレイやろ。\n一つ一つ願い事書いてんねん。▽\n早う、ようなったら、\nお好み焼き食べたい。\n目玉焼きが乗ったヤキソバも。\n\0":
'???',

# Toji Suzuhara 
"ああ、ああ。\n退院出来たら、関東炊きも作る。\n餅入りのタコ焼きも作るわ。\n\0":
'???',

# Toji's Sister
"あはっ、嬉しい。\nあんな、兄ちゃん、\nその千羽鶴逃がして。\n\0":
'???',

# Toji Suzuhara 
"逃がす？\n\0":
'???',

# Toji's Sister
"その鶴、願い事を積んでんねや。\nせやから、叶えてくれるように\n逃がしたって。▽\nな、兄ちゃん…。\n願い事叶ったら、団地の小猫達も\nお母さん、見つかるんよ。▽\n商店街の姉ちゃんも、\n元気な赤ちゃん産めるんや。\nみんなみんな、幸せになるん。▽\n逃がしたってな、兄ちゃん…。\n\0":
'???',

# Hikari Horaki
"鈴原、千羽鶴なんか持って\nどうしたの？\n\0":
'???',

# Kensuke Aida
"何、その千羽鶴？\n\0":
'???',

# Shinji Ikari
"それ、千羽鶴？\n妹に作ったの？\n\0":
'???',

# Kaworu Nagisa 
"たくさんの鳥。\nこれは、千羽鶴だね。\n\0":
'???',

# Asuka Soryu Langley
"なーに、これ？\n折り鶴じゃない。\n千羽鶴ってやつかしら。\n\0":
'???',

# Rei Ayanami 
"これ、千羽鶴ね…。\n\0":
'???',

# Toji Suzuhara 
"キレイやろ、これはな…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"トウジは、教室の窓を開けると、\nバラした千羽鶴を外へ逃がした。\n\0":
'???',

# Toji Suzuhara 
"そら、好きなトコ飛んで行き！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"くるくると様々な色の鶴が、\n願いを乗せて舞う。▽\n金色の鶴が２、３度きらりと光り、\n風に吹き飛ばされていった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、トウジの姿が頭をよぎった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"トウジが窓際に佇んでいる。\n手には、千羽鶴を持って…。\n\0":
'???',

# Shinji Ikari
"千羽鶴じゃないか。\nどうしたの、それ？\n\0":
'???',

# Asuka Soryu Langley
"何でアンタが\n千羽鶴なんか持ってんの？\n\0":
'???',

# Rei Ayanami 
"それは、千羽鶴ね…。\n\0":
'???',

# Hikari Horaki
"鈴原、\nそれ、千羽鶴？\n\0":
'???',

# Kensuke Aida
"トウジ、その千羽鶴は…？\n\0":
'???',

# Kaworu Nagisa 
"千羽鶴だね。\n一体どうしたの？\n\0":
'???',

# Toji Suzuhara 
"ちょっと、手伝ってんか？\n繋いでる糸を取って、\n一羽一羽バラしてくれへん？\n\0":
'???',

# Shinji Ikari
"でも、せっかく作ったのに？\n\0":
'???',

# Asuka Soryu Langley
"えぇ？\nバラしてどーすんの？\n\0":
'???',

# Rei Ayanami 
"でも、どうするの？\n\0":
'???',

# Hikari Horaki
"せっかく作ってあるのに。\nどうして…？\n\0":
'???',

# Kensuke Aida
"はぁ？\nま、いいけどさ。\nどーすんの、コレ。\n\0":
'???',

# Kaworu Nagisa 
"せっかく繋げてあるのにかい？\n\0":
'???',

# Toji Suzuhara 
"逃がしたんねん。\n\0":
'???',

# Shinji Ikari
"…逃がすって、鶴を？\n\0":
'???',

# Asuka Soryu Langley
"これを〜？\n変なの…。\n\0":
'???',

# Rei Ayanami 
"なぜ…？\n\0":
'???',

# Hikari Horaki
"ふ〜ん…。\nほら、貸して。\n手伝うわ。\n\0":
'???',

# Kensuke Aida
"逃がすって、この鶴をかよ？\n\0":
'???',

# Kaworu Nagisa 
"そうか。\nわかった、手伝うよ。\n\0":
'???',

# Toji Suzuhara 
"これ、入院中の妹が、\n自分で折ったんよ。▽\n一羽一羽、全部に願い事が書いて\nあんねんて。\n\0":
'???',

# Toji Suzuhara 
"せやから、叶えてもらうために\nこいつらを逃がしたってって\n言うたんや。\n\0":
'???',

# [Text Only - No Designated Speaker]
"トウジが窓を開ける。\n強い風が吹いていた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"トウジは、教室の窓を開けると、\n千羽鶴を逃がした。▽\nくるくると様々な色の鶴が、\n願いを乗せて舞う。▽\n金色の鶴が２、３度きらりと光り、\n風に吹き飛ばされていった。▽\nあの鶴たちには、どんな願いが\n書いてあったのだろう…。\n\0":
'???',

#
# ./USRDIR/event/f055.har_EXTRACT/f055.evs
#
# [Character: Scene with Hikari]
#
# [Text Only - No Designated Speaker]
"ふと、ヒカリの姿が頭をよぎった。\n\0":
'???',

# Asuka Soryu Langley
"ちょっと、アンタ達こそ\n何様よ。\nこの小市民！\n\0":
'???',

# Kensuke Aida
"おぉ〜、女は怖ぇ〜。\nセンセー、怖いよ〜。\n\0":
'Woooo, women are scaary!\nSensei, I\'m scaared!\n\0',

# Kaworu Nagisa 
"君らが出て行けばいいだろ。\n\0":
'???',

# Shinji Ikari
"委員長を悪く言うな！\n\0":
'Don\'t badmouth the class rep!\n\0',

# Rei Ayanami 
"…あなた達、恥ずかしくないの？\n\0":
'???',

# Asuka Soryu Langley
"あんな、ブス達の言う事なんか\n気にしないでいいわよ。\n\0":
'???',

# Kensuke Aida
"気にするなよ…、イインチョ。\n\0":
'???',

# Kaworu Nagisa 
"あんな人たちの言う事を\n気にする事ないからね。\n\0":
'???',

# Shinji Ikari
"とんでもない奴等だよ。\n一人じゃ何も言えないくせに。\n\0":
'???',

# Rei Ayanami 
"…最低な人達。\n\0":
'???',

# Hikari Horaki
"でも、あの人達が言ってた事\n本当だから…。\n言い返せなくって…。▽\n………。▽\nゴメン、今日は帰る…。\nお姉ちゃん、昨日家に帰らな\nかったし…。\n\0":
'???',

# Kaworu Nagisa 
"幻滅だよ。\nそういう事はやめてくれないかな？\n\0":
'???',

# Female Classmate
"ちょっと、行こ…。\n\0":
'???',

# Female Classmate
"フン。\n\0":
'???',

# Asuka Soryu Langley
"しょせん、ヒカリへのヒガミね。\nヒカリは何も悪くないのに。\n\0":
'???',

# Kensuke Aida
"インシツ…。\n俺、男でよかったぜ。\n\0":
'???',

# Kaworu Nagisa 
"あーぁ、\n何だか急に不愉快になったよ。\n\0":
'???',

# Shinji Ikari
"何が楽しいんだ、\nあんな話ばっかり、一日中…。\n\0":
'???',

# Hikari Horaki
"どうかしたの？\n\0":
'What\'s wrong?\n\0',

# Toji Suzuhara 
"よぉ、イインチョか。\nんにゃ、何でもねーよ。\n\0":
'???',

# Asuka Soryu Langley
"ヒカリ…。\nううん、何でもないわよ。\n\0":
'???',

# Kensuke Aida
"え？\n何でもないよ…。\n\0":
'???',

# Kaworu Nagisa 
"委員長か。\nいや、何でもないよ。\n\0":
'???',

# Shinji Ikari
"ああ、委員長…。\n別に何でもないんだ。\n\0":
'???',

# Rei Ayanami 
"…何でもないわ。\n\0":
'...It\'s nothing.\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba047.evs
#
# Maya Ibuki, Female Staff
"参号機のシールドが\n破壊されました！\n\0":
'Unit-03\'s shield has been destroyed!\n\0',

# Maya Ibuki, Female Staff
"初号機のシールドが\n破壊されました！\n\0":
'Unit-01\'s shield has been destroyed!\n\0',

# Maya Ibuki, Female Staff
"四号機のシールドが\n破壊されました！\n\0":
'Unit-04\'s shield has been destroyed!\n\0',

# Maya Ibuki, Female Staff
"弐号機のシールドが\n破壊されました！\n\0":
'Unit-02\'s shield has been destroyed!\n\0',

# Maya Ibuki, Female Staff
"零号機のシールドが\n破壊されました！\n\0":
'Unit-00\'s shield has been destroyed!\n\0',

#
# ./USRDIR/event/bs060.har_EXTRACT/bs060.evs
#
# Misato Katsuragi 
"エヴァは、この第３新東京市の\n所々に設置されている「電源ビル」\nから電力を供給して動いているの。▽\nだから、エヴァは\nこのケーブルが届く範囲までしか、\n活動出来ないの。\n\0":
'???',

# Misato Katsuragi 
"アンビリカルケーブルを\n他のビルに繋ぎ直す時は、\nその電源ビルの側に立って%1iボタン。▽\n「アンビリカルケーブル接続」の\nコマンドを選べばいいわ。▽\n重要な事だから、忘れないようにね。\n\0":
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
# ./USRDIR/event/cev0300.har_EXTRACT/cev0300.evs
#
# Misato Katsuragi 
"あ、レイ。\nあなたに教えとくことがあったわ。\n大事な話よ。\n\0":
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
# ./USRDIR/event/cev0210.har_EXTRACT/cev0210.evs
#
# [Scenario 2: Asuka - Ending]
#
# Asuka Soryu Langley
# [Note] （非表示）=(Non-Display). Programming instructions?
"泣き声です。（非表示）\n\0":
'Someone\'s crying.（非表示）\n\0',

# Asuka Soryu Langley
"泣いてる…。\n泣いてるのは私だわ。\n\0":
'Crying...\nThe one who\'s crying is me.\n\0',

# Asuka Soryu Langley
"私の願い…。\n\0":
'My wish...\n\0',

# Asuka Soryu Langley
"私が願うのは…。\n\0":
'What I\'m dreaming of...\n\0',

# Asuka Soryu Langley
"泣いては駄目。\n一人で生きなきゃいけないの。\n大人になるの。\n\0":
'???',

# [Text Only - No Designated Speaker]
"大人…？\n今の私は大人？\n\0":
'Grown-up...?\nI\'m grown up now?\n\0',

# Asuka Soryu Langley
"お帰り。\n\0":
'???',

# Ryoji Kaji
"待たずに寝てりゃ\nよかったのに。\n\0":
'???',

# Asuka Soryu Langley
"どうしてそんな事言うの？\n\0":
'???',

# Ryoji Kaji
"大袈裟にがっかりしたりして\n何だよ…。▽\n…何？\n何を俺にして欲しかったんだ？\n\0":
'???',

# Asuka Soryu Langley
"大人になっても、\n寂しいのは変わらないんだ。▽\n受け入れてもらえるわけじゃ\nないんだ。\n\0":
'???',

# Asuka Soryu Langley
"やっぱり一人なんだ。\n\0":
'???',

# Misato Katsuragi 
"自分自身が変わろうと\nしないからよ。\n\0":
'???',

# Shinji Ikari
"ヘンなところばかり\n大人になって。\n\0":
'???',

# Rei Ayanami 
"自分に制限を与えて、\n外へ踏み出せないのね。\n外の世界の可能性に触れたがらない。\n\0":
'???',

# Kyoko Soryu Zeppelin 
"アスカちゃん、\nあなたの好きにしていいのよ？\n\0":
'???',

# Asuka Soryu Langley
"ママ…？\n\0":
'Mama...?\n\0',

# Kyoko Soryu Zeppelin 
"あなたが願う事。\nどうありたいかは自分で\n決めるのよ。\n\0":
'???',

# Rei Ayanami 
"そこから踏み出さなければ\n何も変わらないわ。\n\0":
'???',

# Asuka Soryu Langley
"………。▽\nでも、ここはどこなの？▽\n何もない、誰もいない。\n\0":
'???',

# Asuka Soryu Langley
"こんなものが自由なの？\n\0":
'???',

# Misato Katsuragi 
"全てはあなたの思うまま。\n\0":
'???',

# Ritsuko Akagi 
"それが補完計画。\n\0":
'???',

# Rei Ayanami 
"あなたが踏み出す、\nあなただけの現実。\n\0":
'???',

# Asuka Soryu Langley
"わからない。\n\0":
'???',

# Asuka Soryu Langley
"どんな自分になりたいのか\nわからないの。\n\0":
'???',

# Asuka Soryu Langley
"そうかなぁ…。\n\0":
'???',

# Asuka Soryu Langley
"んー、それもいいな。\nそういえば、他にもやって\nみたい事って…あるかな？\n\0":
'???',

# Hikari Horaki
"何でもいいと思うわ。\n好きな事なら。\nなりたいものがあるのなら。\n\0":
'???',

# Asuka Soryu Langley
"そっか…。\n私は自由なんだ。▽\nただ、私は何も\n選んでこなかっただけなんだわ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"どうして自分を嫌う事ばかり\n考えていたのだろう。▽\n私が、私を大事にしてあげればいい。\n自分をもっと好きになれば、\n私は変わる。▽\n私はそれを知っている。\n\0":
'???',

# Shinji Ikari, Rei Ayanami, Misato Katsuragi, Gendo Ikari, Kozo Fuyutsuki, Ritsuko Akagi, Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Ryoji Kaji, Hikari Horaki, Toji Suzuhara, Kensuke Aida, Kaworu Nagisa
"おめでとう。\n\0":
'Congratulations.\n\0',

# Pen Pen
"クワァ〜、クワァ〜\nクァクァクァ！\n\0":
'???',

# Asuka Soryu Langley
"ありがとう、みんな。\nありがとう、私。▽\nありがとう…。\n約束するわ。\n私、きっと幸せになる。▽\nあなたに、ありがとう…。\n\0":
'???',

#
# ./USRDIR/event/cev0404.har_EXTRACT/cev0404.evs
#
# Misato Katsuragi 
"使徒がいなくなった今、\n司令や委員会の狙いを、\n妨げるものは何もない。▽\nそして、計画が遂行される\n時が来たのね。\nサードインパクトが…。▽\n絶対に、させはしない。▽\n自分達の目的の為に、\n父さんを利用した奴等を\n私は許さない…。\n\0":
'Now that the Angels are gone,\nthere\'s nothing standing in the way of\nthe Commander's and the Committee's goals.▽\nAnd isn\'t it high time they saw their plans through?\n The Third Impact...▽\nI\'ll never let it happen.▽\nI\'ll never forgive them\nfor using Father as\na pawn in their schemes...\n\0',

# Misato Katsuragi 
"…始まるわね。\n\0":
'... It\'s started.\n\0',

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
# ./USRDIR/event/bs072.har_EXTRACT/bs072.evs
#
# Misato Katsuragi 
"攻撃を行うと、しばらくの間\n次の攻撃が行えなくなるから\n気をつけて。▽\nこの攻撃できない間を\nチャージ時間というの。\n\0":
'???',

# Misato Katsuragi 
"このチャージゲージが最大まで\n回復すれば、次の攻撃が行えるわ。▽\nちなみに、チャージが完了しないと\n攻撃できないのは、使徒の場合も\n全く同じよ。わかった？\n\0":
'???',

# Misato Katsuragi 
"じゃあ、今まで説明した事を\nしっかり頭に入れて\n使徒を倒してちょうだい。▽\n使徒を倒すことができたら\n今日の訓練は終わりよ。\n頑張ってね！\n\0":
'???',

#
# ./USRDIR/event/bs006.har_EXTRACT/bs006.evs
#
# Maya Ibuki 
"…っ！\n来ました…。\nあああぁぁ！！\n\0":
'...!\nIt\'s here...\nAahhh!\n\0',

#
# ./USRDIR/event/bs067.har_EXTRACT/bs067.evs
#
# Misato Katsuragi 
"ＯＫ、ＯＫ！\nちゃんと覚えてるわね。▽\nイザという時はケーブルを切断し、\n予備電源のみでの活動も可能。\n\0":
'???',

# Misato Katsuragi 
"ただし、予備電源は少なく、\n切れたら活動停止で、一巻の終わり。▽\n緊急手段として、これもちゃんと\n覚えておいてネ。\n\0":
'???',

#
# ./USRDIR/event/b2s18.har_EXTRACT/b2s18.evs
#
# Maya Ibuki, Female Staff
"可視波長のエネルギー波、\n使徒の心理攻撃、来ます！\n\0":
'The Angel is attacking psychically\nwith energy waves on the visible spectrum!\n\0',

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
# ./USRDIR/event/cev0112.har_EXTRACT/cev0112.evs
#
# [Scenario 2: Shinji - Scene with Hikari]
#
# Hikari Horaki
"碇君、あのね…。\n\0":
'Ikari-kun, I, um...\n\0',

# Hikari Horaki
"…碇君って、音楽得意でしょ？\n\0":
'... Ikari-kun, are you good with music?\n\0',

# Shinji Ikari
"得意って程でもないと思うけど。\n\0":
'???',

# Hikari Horaki
"でも、音符とか\nスラスラ読めるでしょ？\n\0":
'???',

# Shinji Ikari
"まあ、昔チェロやってたから。\n基礎的な事はわかる…のかな？\n\0":
'???',

# Hikari Horaki
"今度の合唱コンクール、\nピアノ伴奏を碇君に\n頼みたかったけど…。▽\n碇君はほら…、パイロットだし\nもしもの時の事を思えば\n頼っちゃダメなんだろうなって。\n\0":
'???',

# Shinji Ikari
"じゃあ、誰が伴奏を担当するの？\n\0":
'???',

# Hikari Horaki
"…私。\nピアノ出来そうな人は\nみんな断られちゃって…。▽\nピアノ…、出来ないのに\n引き受けちゃって。\n\0":
'???',

# [Text Only - No Designated Speaker]
"委員長は、みんなよりも\n何でも出来てすごいなぁって\n思っていたけど…。▽\n出来ない事もあるんだなと\n少し驚いた。\n\0":
'???',

# Hikari Horaki
"小学校の時に、ピアニカ程度なら。\n勉強は自信あるんだけど…。\n音楽はまるでダメ…。▽\nだから、\n碇君なら…教えてくれるかなと\n思って。\n\0":
'???',

# Shinji Ikari
"僕に出来る事なら。\nえーっと…、えっと…。\nまず、指のつかい方。▽\n右はこう…、中指ミの音にきたら\nすぐ親指を次のファに持ってくと\n小指がちゃんとドまで届くよね？▽\n机をピアノに見立てて、\nやってみてごらん。\n\0":
'???',

# Hikari Horaki
"…難しいわ。\n\0":
'???',

# Shinji Ikari
"楽譜見せて。▽\n…えっと、左手の伴奏は、\n和音の連打でいいように\nアレンジしよう。\n\0":
'???',

# Hikari Horaki
"すごい…。\n楽譜を変えちゃうの？\n\0":
'???',

# Shinji Ikari
"そしたら、ラスト以外は\n３つのパターンの和音を\n押さえていればいいんだ。▽\nこう、３拍子のリズムで和音を叩く\nようにして…、右手を合わせていく\n練習を………えっと、何かな？\n\0":
'???',

# Hikari Horaki
"えっ…、あ、ううん。\n何か…見とれちゃうな。\n指先の動き、きれいだから。\n\0":
'???',

# Hikari Horaki
"碇君…の彼女になる人は\nずっと、この指を見て\nいられるんだろうね。\n\0":
'???',

# Hikari Horaki
"いいなぁ…。\nその人きっと、幸せだよ。\n\0":
'???',

# Shinji Ikari
"…？？？\n指先きれいなのがいいの？\n\0":
'???',

# Hikari Horaki
"そうじゃないんだけど…。\nううん、いいの。▽\n指先、見ててもいい？\n\0":
'???',

# [Text Only - No Designated Speaker]
"委員長は、僕の指先を見ている。\n何だか、嬉しそうだ。\n\0":
'???',

# Shinji Ikari
"委員長もやんなきゃダメだよ。\nほら、横に並んで。\n\0":
'???',

# Shinji Ikari
"ねえ、連弾やってるみたいだ。\n\0":
'???',

# Hikari Horaki
"そうね、こう指を動かしている\nだけなのに、何だか\nすごくいい曲を弾いてるみたい。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕には聞こえてきた。\n委員長の指先から奏でられていく\nメロディ。▽\n多分、彼女の伴奏は上手くいく。\n\0":
'???',

# Hikari Horaki
"音楽ってコミュニケーションなのね。\nまるで、手をつないで歩くような\nそんな感じ………。\n\0":
'???',

# Hikari Horaki
"…あ…………………。\n\0":
'???',

# Shinji Ikari
"そう、かな。\nそうかもしれない。\n考えた事なかったけど…。\n\0":
'???',

# Hikari Horaki
"私、楽しいわ。\nよかった、碇君に聞いて。\nありがとう…。\n\0":
'???',

# Hikari Horaki
"ちゃんと弾けるようになったら、\nまた一緒に弾いてくれる？\n今度は本物のピアノで。\n\0":
'???',

# Hikari Horaki
"フフ、よかった。\n碇君の指先を見るのは\n私だけの特権ね。\n\0":
'???',

# Shinji Ikari
"…へ？\n\0":
'???',

# Hikari Horaki
"気にしないで。\nよし、やる気出てきた！\n私、頑張る！\n\0":
'???',

# [Text Only - No Designated Speaker]
"そういえば、一緒に演奏をするって\n言うのは…、委員長が言った様に\n手をつなぐ事に似てるなと思った。▽\n委員長は、楽しそうだったな…。▽\n僕等は、ほんの少しのこの時間に、\n誰にも知られないように、\nそっと手をつないだのだろう。▽\nそう思うと、少し照れた。\n\0":
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
# ./USRDIR/event/cev0304.har_EXTRACT/cev0304.evs
#
# Rei Ayanami 
"誰かが見てる。▽\nいいえ、見ているのは私。\n私が私を見ている。▽\n前にもあった、こんな感覚。\nずっと前、ずっと昔。\n私が私になる前に…。\n\0":
'Someone is looking at me.▽\nNo, the one who\'s looking is me.\nI am looking at myself.▽\nThis feeling, it\'s one I\'ve had before.\nLong ago, deep in the past.\nMe, before I became me...\n\0',

# Rei Ayanami 
# [Note] The playthrough I\'m referencing shows an image of Shinji during this part, so あの人 is being rendered "him". It\'s possible this is variable, though, and changes depending on whoever Rei has the best relationship with at the time. Need to double-check. -Reichu
"あの人を思うと、とても不思議。\n不思議な気持ちになる。▽\nずっと一緒にいたような感じ。\n私が私になる前から。▽\nどうして？\nあの人を見ると、心が動く。\n心…、目に見えないもの。\n\0":
'When I think of him, it\'s very strange.\nA strange feeling.▽\nOf wanting to be with him forever.\nFrom before I became me.▽\nWhy?\nWhen I look at him, my heart is touched...\nMy heart... Something that cannot be seen.\n\0',

#
# ./USRDIR/event/cev0116.har_EXTRACT/cev0116.evs
#
# Kozo Fuyutsuki
"いかないのか…？\n\0":
'???',

#
# ./USRDIR/event/a004.har_EXTRACT/a004.evs
#
# [Angel: Matarael]
#
# Maya Ibuki 
"液体が落ちた箇所が腐食しています。▽\nどうやら使徒の武器は、\nあの強力な溶解液のようですね。\n\0":
'The sites where the liquid fell are being corroded.▽\nIt seems the Angel is using that\npowerful solvent as a weapon.\n\0',

# Male Staff
"液体が落ちた箇所が腐食しています。▽\nどうやら使徒の武器は、\nあの強力な溶解液のようです。\n\0":
'The sites where the liquid fell are being corroded.▽\nIt seems the Angel is using that\npowerful solvent as a weapon.\n\0',

# Misato Katsuragi 
"しかし、これじゃうかつに\n近づけないわね。\n\0":
'???',

# Kozo Fuyutsuki
"ああ、恐らく敵に向かって\n射出するためのものだろう。\n\0":
'???',

# Male Staff
"直上を目指しているという事は…。\nあの液を使って、ジオフロントに\n侵入するつもりでしょうか…！？\n\0":
'???',

# Kozo Fuyutsuki
"足止めを急げ。\nエヴァ、出撃準備！！\n\0":
'???',

# Female Staff
"そのようですね。\nでは、エヴァの出撃準備に移ります。\n\0":
'???',

# Male Staff
"これは、かなり大きいですね。\n\0":
'???',

# Female Staff
"これでは、うかつに近づけませんね。\n\0":
'???',

# Kozo Fuyutsuki
"本体はそんなに大きくはない。\nおそらく、弱点もあそこだろう。\n\0":
'???',

# Female Staff
"目標は速度を速めて、\nこちらに向かっています。\n\0":
'???',

#
# ./USRDIR/event/bs044.har_EXTRACT/bs044.evs
#
# [Text Only - No Designated Speaker]
"エヴァ初号機は使徒を捕食し、\nΣ機関を取りこみました。▽\n内蔵電源が無限になり、\nアンビリカルケーブル無しでの\n稼動が可能になります。\n\0":
'Eva Unit-01 preyed upon an Angel\nand absorbed its S2 engine.▽\nThe Eva\'s internal power supply is now infinite,\nallowing it to operate with an umbilical cable.\n\0',

#
# ./USRDIR/event/b2s53.har_EXTRACT/b2s53.evs
#
# Kaworu Nagisa 
"シンジ君！！\nもう、大丈夫だよ。\n\0":
'???',

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
# ./USRDIR/event/a012.har_EXTRACT/a012.evs
#
# Kozo Fuyutsuki
"衛星軌道上だと？\n\0":
'???',

# Misato Katsuragi 
"こりゃ、またデカそうな…。\n\0":
'???',

# Kozo Fuyutsuki
"最大望遠でこのサイズか。\nこいつはデカいな。\n\0":
'???',

# Male Staff
"これは、また………。\n\0":
'???',

# Kozo Fuyutsuki
"ということは、降下接近の機会を\nうかがっているのか、その必要も\nなく、ここを破壊できるのか。\n\0":
'???',

# Male Staff
"降下接近の機会をうかがってるのか、\nその必要もなく、\nここを破壊できるのか…。\n\0":
'???',

# Female Staff
"こちらの射程距離内まで\n近づいてくれないと、\nどうしようもないですね。▽\nエヴァには、衛星軌道の敵は\n迎撃できませんから。\n\0":
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
# ./USRDIR/event/bs091.har_EXTRACT/bs091.evs
#
# Shigeru Aoba, Male Staff
"零号機投てき体勢。\n\0":
'???',

#
# ./USRDIR/event/f073.har_EXTRACT/f073.evs
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
# ./USRDIR/btl/tabris.har_EXTRACT/bk019.evs
#
# Kaworu Nagisa 
"嫌いじゃないよ。\nでも、嫌われると僕に恐怖心を\n抱いている。▽\nヒトを信じられないからだね。\0":
'???',

#
# ./USRDIR/event/bs009.har_EXTRACT/bs009.evs
#
# [Text Only - No Designated Speaker]
"%1iボタンでコマンドが使える\nようになりました。\n\0":
'???',

#
# ./USRDIR/event/bs001.har_EXTRACT/bs001.evs
#
# [Text Only - No Designated Speaker]
"家出していた$lは\n黒服たちに連れもどされた。\n\0":
'???',

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
# ./USRDIR/event/f014.har_EXTRACT/f014.evs
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
# ./USRDIR/event/b2s41.har_EXTRACT/b2s41.evs
#
# Toji Suzuhara 
"カヲル！\n\0":
'???',

# Toji Suzuhara 
"惣流ー！\n\0":
'???',

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
'???',

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
# ./USRDIR/event/f045.har_EXTRACT/f045.evs
#
# [Text Only - No Designated Speaker]
"ふと、\nアスカの声が聞こえた気がした。\n\0":
'???',

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
# ./USRDIR/event/cev0113.har_EXTRACT/cev0113.evs
#
# Shinji Ikari
"あ、トウジ！\n\0":
'???',

# Toji Suzuhara 
"おお〜、シンジ〜。\nどないしたん？\n\0":
'???',

# Shinji Ikari
"晩御飯…、買おうと思って。\n\0":
'???',

# Toji Suzuhara 
"なんや？\nインスタントラーメンかいな。\nしかも、そんなようさん…。\n\0":
'???',

# Shinji Ikari
"買い置きが無くなっちゃって…。\n\0":
'???',

# Toji Suzuhara 
"あっかんな〜。\nパイロットは体が資本やろ？\nもっとマシなもん喰わんと！\n\0":
'???',

# Shinji Ikari
"うん…、その通りだと思うよ。\nでもお弁当って最近品薄みたいで、\nあんまり売ってないんだよね。\n\0":
'???',

# Toji Suzuhara 
"せやなぁ、スーパーは車やないと\n不便やしなぁ…。\n…あ、せや！\n\0":
'???',

# Toji Suzuhara 
"ほな、ワシんとこで飯喰いや。\n今日、おとんもおじいも\n晩おれへんねん。\n\0":
'???',

# Shinji Ikari
"…いいの？\n\0":
'???',

# Toji Suzuhara 
"お〜、遠慮すんな！\nワシかて料理はちょっとした\nもんなんやで？\n\0":
'???',

# [Text Only - No Designated Speaker]
"そうなのだ。\nトウジは密かにマメに家事を\nするヤツなのだ。▽\nそのくせ、「掃除なんか\n男のするもんやあらへん」などと\n公言してはばからない。▽\nそういって当番を堂々とサボるので\n女子に呆れられている。\n\0":
'???',

# Shinji Ikari
"じゃあ…、\nお邪魔させてもらおうかな。\n\0":
'???',

# Toji Suzuhara 
"へへ、ほなアレや、\nお菓子とかも買うとかんと…。\nえーっと、プリン、プリンっと。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕らは会計をすませ、\nトウジの家に向かった。\n\0":
'???',

# Toji Suzuhara 
"…ほな、ちょっと待っとけよ。\nあ、まだお菓子開けたりしたら\nアカンで？\n\0":
'???',

# Shinji Ikari
"…しないよ。\nご飯の後なんだろ？\nあ、何か手伝おうか？\n\0":
'???',

# Toji Suzuhara 
"おう、エエ子やのう。\nほんならキャベツ千切りしといて。\nあと、ネギもみじん切りで。\n\0":
'???',

# [Text Only - No Designated Speaker]
"トウジは小麦粉を溶いている。\n…どうやらお好み焼きを\n作るみたいだ。\n\0":
'???',

# Toji Suzuhara 
"さてっと、山芋下ろして…。\nだし汁足して…。\n…よっしゃ、キャベツ貸せや。\n\0":
'???',

# [Text Only - No Designated Speaker]
"普段の不器用ぶりはどこに行ったの\nやら…、作り慣れているらしく、\n手際よく調理を進めている。\n\0":
'???',

# Toji Suzuhara 
"ほんなら、焼き入れたらんとな。\n\0":
'???',

# [Text Only - No Designated Speaker]
"熱したホットプレートの上に\n練った粉（キャベツ和え）が\n落とされた。▽\nジュッっと水分が蒸発する音を\n立てる。\n\0":
'???',

# Toji Suzuhara 
"よおし、お好み焼きは結構焼くのに\n時間かかりよるからな。\nその間に、米炊いとかんと。\n\0":
'???',

# Shinji Ikari
"え？　なんで？\n\0":
'???',

# Toji Suzuhara 
"…なんでやあらへんやろ？\nご飯無しで、どないすんねんな。\n\0":
'???',

# Shinji Ikari
"…だって、お好み焼きじゃないの？\n\0":
'???',

# Toji Suzuhara 
"ああ、見ての通りやで？\n\0":
'???',

# Shinji Ikari
"じゃあなんでご飯がいるの？\n\0":
'???',

# Toji Suzuhara 
"ははっ、アホやなぁ…。\nええか、シンちゃん？\nご飯はおかずと一緒に食うやろ？\n\0":
'???',

# Shinji Ikari
"お好み焼きをおかずにするの？\n…それっておかしくない？\n\0":
'???',

# Toji Suzuhara 
"…どういう事やねん…。\nお好み焼きはおかずやろ？\n\0":
'???',

# Shinji Ikari
"そんなわけないじゃないか！\n炭水化物同士じゃ栄養が\n偏りすぎだよ！▽\n第一、マシなもの食べろって\n言ったじゃないか。\n\0":
'???',

# Toji Suzuhara 
"ああ？　…なんやお前、\n鈴原家の伝統メニューにケチ\nつけようっちゅうんか…。▽\n…しかも、お手製お好み焼きが\nコンビニのカップ麺以下っちゅう\n評価か…。\n\0":
'???',

# Shinji Ikari
"あ、いや…。\n\0":
'???',

# Toji Suzuhara 
"もう、ええ…。\n何も喰わさへん。\n帰れ。\n\0":
'???',

# Shinji Ikari
"……………………。\nお邪魔しました。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕は、\n随分傲慢な事を言ってしまった。▽\n自分の狭量さを棚上げして、他所の\nお宅が長年築き上げた食文化を\n全否定してしまったのだ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"落ち込んでしまった…。\n家への足取りは当然重く、\nトボトボと部屋に帰りついた。\n\0":
'???',

# Shinji Ikari
"明日トウジに謝らなきゃ…。\n…でも話を聞いてくれるかな…。\n\0":
'???',

# Shinji Ikari
"あ！　そういえば…。\nコンビニ寄ればよかったなぁ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ストックが無いから買いに\n行ったんだった…。▽\nでももう一度、外に出る気には\nどうしてもならなかった。\n\0":
'???',

# Shinji Ikari
"はぁ…、散々だなぁ…。\n\0":
'???',

# Shinji Ikari
"ん？　ミサトさん…かな？\nはぁい！\n\0":
'???',

# Toji Suzuhara 
"…あの…、鈴原やけど…。\n\0":
'???',

# Shinji Ikari
"………！\nい、今、開けるよ！\n\0":
'???',

# [Text Only - No Designated Speaker]
"通話機から玄関に向かう短い廊下で、\n僕はどんな表情をするべきかを\n真剣に検討した。▽\n…でも、何が最良の選択か\n判断がつかず、結局困り顔のまま\nドアを開けてしまった。\n\0":
'???',

# Shinji Ikari
"…あ、やぁ…。\n\0":
'???',

# Toji Suzuhara 
"…これ……。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そういってトウジが手渡したものは、\n焼きたてのお好み焼きだった。\nタッパー越しにも熱が伝わってくる。▽\n見れば、トウジの肩が上下している。\nわざわざ走って来てくれたのだろう。\n\0":
'???',

# Shinji Ikari
"あ、ありがとう…。\n…ごめん…ね？\n\0":
'???',

# Toji Suzuhara 
"…いや、かめへん。\nそれより、味わって喰えよ？\nタッパーは明日、洗って返せ。\n\0":
'???',

# Shinji Ikari
"うん、わかった。\n…あがっていってよ。\n一緒に食べようよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"トウジはわざとらしく肩を竦めた。\n\0":
'???',

# Toji Suzuhara 
"はっ、遠慮しとくわ。\nだって、米炊いてへんのやろ？\nそんなん、マナーなってないわ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕等はお互いの顔を見合わせて\n微笑んだ。\nどうやら仲直りできたみたいだ。▽\nトウジの心からの親切に、\n僕は自分が恥ずかしくなった。\n\0":
'???',

# Toji Suzuhara 
"あと…、これ。\n食後に喰えよ？\n\0":
'???',

# [Text Only - No Designated Speaker]
"さっきコンビニで買ったプリンも\n渡してくれた。▽\nそしてトウジは「ほな」と行って\n帰って行ってしまった。\n\0":
'???',

# Shinji Ikari
"……………、\nまた明日。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕は引き止めなかった。\nぶっきらぼうな所は、\n彼流の照れ隠しなのだから。▽\nお好み焼きでケンカするなんて\n馬鹿らしい…、と、トウジが\n大きく譲歩してくれたのだ。▽\n僕は大いにカッコつけて\nもらいたいと思った。\n\0":
'???',

# [Text Only - No Designated Speaker]
"さっそく冷凍していたご飯を\n暖めて、お好み焼きと一緒に\n食べてみた。\n\0":
'???',

# Shinji Ikari
"あ、イケる…かな？\n\0":
'???',

# [Text Only - No Designated Speaker]
"とても美味しいお好み焼きだった。\nソースの味、そして生地の本来の\n甘味が、よくご飯に合うと思った。▽\n…………………。▽\nでも、やっぱり僕は別々に食べたい。\n悪くはなかったけど…。\nまあ、何となく…、そう思った。▽\n…こういえば、きっとトウジは\n怒らなかったんだろうな。\n\0":
'???',

#
# ./USRDIR/event/f041.har_EXTRACT/f041.evs
#
# Toji Suzuhara 
"お前、誰やねん…。\n\0":
'???',

# Kaworu Nagisa 
"歌は心を潤してくれる…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"どこかから歌が聞こえる…。\n\0":
'???',

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
'???',

# Kaworu Nagisa 
"そう思わないかい、碇シンジ君。\n\0":
'???',

# Kaworu Nagisa 
"そう思わないかい、アスカさん。\n\0":
'???',

# Kaworu Nagisa 
"そう思わないかい、ファースト。\n\0":
'???',

# Kaworu Nagisa 
"そう思わないかい、鈴原トウジ君。\n\0":
'???',

# Shinji Ikari
"ど、どうして僕の名を？\n\0":
'???',

# Asuka Soryu Langley
"ちょっと、\nそーゆーアンタは何モンなのよ？\n\0":
'???',

# Rei Ayanami 
"あなた、私と同じ匂いがする…。\n一体、誰…？\n\0":
'???',

# Toji Suzuhara 
"ワイを知っとう…て。\n何や、お前誰なん？\n\0":
'???',

# Kaworu Nagisa 
"僕は渚カヲル、\n君と同じ選ばれた子供さ。\n\0":
'???',

# Shinji Ikari
"渚…くん？\n\0":
'???',

# Asuka Soryu Langley
"渚カヲルぅ？\n\0":
'???',

# Rei Ayanami 
"渚カヲル…？\nあなたもエヴァのパイロットなのね。\n\0":
'???',

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
# ./USRDIR/event/f002.har_EXTRACT/f002.evs
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
# ./USRDIR/event/f023.har_EXTRACT/f023.evs
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
# ./USRDIR/event/f074.har_EXTRACT/f074.evs
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
# ./USRDIR/event/cev0101.har_EXTRACT/cev0101.evs
#
# [Text Only - No Designated Speaker]
"どうでもいいんだ。\n自分も、他人も、この世界も。\n適当に、漂うように生きて死ぬ。▽\n何も変わらない。▽\nただ、ずっと同じ毎日が続くだけ。▽\n続くだけなんだ…。\n\0":
'???',

#
# ./USRDIR/event/cev0102.har_EXTRACT/cev0102.evs
#
# Asuka Soryu Langley
"シーンジッ！！\n\0":
'???',

# Asuka Soryu Langley
"どうして、洗濯する時\nブラとショーツをネットに\n入れといてくれないのよ！！▽\n…ったくもー、レースの部分が\nほどけちゃってるじゃない！\n\0":
'???',

# Shinji Ikari
"そ、そんな事言ったって、\nネットに入れておかなかった\nアスカが悪いんだろ？\n\0":
'???',

# Asuka Soryu Langley
"ハァ！？\nアンタには、\n配慮ってモノがないワケ？▽\nあぁ、もう\nブラのワイヤーだって、\n曲がっちゃって…！！\n\0":
'???',

# Shinji Ikari
"ゴ、ゴメン…。\n\0":
'???',

# Asuka Soryu Langley
"弁償してよ。\nものすごーく高かったんだから。\n\0":
'???',

# Shinji Ikari
"そんな…、無茶苦茶だよ。\n\0":
'???',

# Asuka Soryu Langley
"無理だって言うの？\nふーん。▽\nそれじゃ、私の奴隷に\nなんなさいよ！\n\0":
'???',

# Shinji Ikari
"奴隷…？\n\0":
'???',

# Asuka Soryu Langley
"まずは、\nペディキュアやって。\n\0":
'???',

# Shinji Ikari
"ペ、ペディキュア？\n何だよ、それ…。\n\0":
'???',

# Asuka Soryu Langley
"足の化粧よ。\n足の爪に、\n上手にマニキュア塗って！\n\0":
'???',

# Asuka Soryu Langley
"手際よくやんなさいよ。\n\0":
'???',

# Shinji Ikari
"もー、黙ってて。\n動かないでよ。\n\0":
'???',

# Asuka Soryu Langley
"あんッ！！\nくすぐったいっ！！\n\0":
'???',

# Shinji Ikari
"あぁぁぁ…、\n爪からはみ出したよ。\n\0":
'???',

# Shinji Ikari
"いった…。\n蹴る事ないだろ！▽\n…っつ…、唇切れた…。\n\0":
'???',

# Asuka Soryu Langley
"…そんなに痛がる事ないでしょ。\n大げさね。\n\0":
'???',

# Asuka Soryu Langley
"まあ、…ちょっとは\nやりすぎだったかも\nしれないけどさ。▽\n見せてみなさいよ。\n\0":
'???',

# Shinji Ikari
"見せたってしょうがないだろ。\n唇なんかにテープ張って\n置けないし。\n\0":
'???',

# Asuka Soryu Langley
"ワセリンでも塗った方がいいわ。\nホラ、上向いて。\n\0":
'???',

# Shinji Ikari
"いいよ。\n\0":
'???',

# Asuka Soryu Langley
"せっかく人が親切に\nしてやってんのに！\n動かないッ！\n\0":
'???',

# Shinji Ikari
"わぁぁぁぁ…。\n\0":
'???',

# Asuka Soryu Langley
"ホラ、おとなしくする。\n\0":
'???',

# [Text Only - No Designated Speaker]
"アスカの白い指が、\n僕の唇の上をすべる。▽\n他人に唇を触られるのは…、\n何だかヘンな気持ちだ。\n\0":
'???',

# Shinji Ikari
"ま、まだ…？\n\0":
'???',

# Asuka Soryu Langley
"まだ！\n\0":
'???',

# Pen Pen
"グワッ。\n\0":
'???',

# Asuka Soryu Langley
"キャッ！！\nあっは〜ん、いた〜い。\nペンペンがお尻つついた！\n\0":
'???',

# Shinji Ikari
"んむー！！\nアスカ、もういいって。\nどいて、どいてよ！\n\0":
'???',

# Asuka Soryu Langley
"やぁだ、\nモゾモゾ顔を動かさないで！\n\0":
'???',

# [Text Only - No Designated Speaker]
"アスカが顔に覆い被さって\n息が出来ない。\n\0":
'???',

# Pen Pen
"クア！！\n\0":
'???',

# Shinji Ikari
"痛ッ！？\n\0":
'???',

# [Text Only - No Designated Speaker]
"今度はペンペンが僕をつついた。\n\0":
'???',

# Asuka Soryu Langley
"アンッ、もう！\n突き上げないでェ！\n\0":
'???',

# Shinji Ikari
"ちょっ…、ちょっと…。\n\0":
'???',

# Shinji Ikari
"いてててて…。\nやっと解放された。\n\0":
'???',

# Pen Pen
"クゥァァァ、クゥァァァ、\nクァッ、クァッ、クァッ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ペンペンが何かをくわえている。▽\n干しておいたアスカの下着だ。▽\n下着のスパンコールやレースを、\nくちばしで引きちぎっている。\n\0":
'???',

# Asuka Soryu Langley
"あ…、ひょっとして\n私の下着をあんなにしたの…。\nペンペン？\n\0":
'???',

# Shinji Ikari
"そうみたい。\nビーズとか、\n光るものが気になるんだ。\n\0":
'???',

# Shinji Ikari
"あぁ！？\nじゃあ、アスカの奴隷なんかに\nなる必要なかったんじゃ…。\n\0":
'???',

# Asuka Soryu Langley
"そ、そうね。\nあはははは…。\n\0":
'???',

# Shinji Ikari
"何なんだよ、も〜〜〜。\nトホホ…。\n\0":
'???',

#
# ./USRDIR/event/cev0103.har_EXTRACT/cev0103.evs
#
# Rei Ayanami 
"碇君。▽\n私、宇宙人なの。\n\0":
'???',

# Shinji Ikari
"へっ…！？\n\0":
'???',

# Rei Ayanami 
"宇宙人なの。\n\0":
'???',

# Shinji Ikari
"宇宙人…。\n\0":
'???',

# Shinji Ikari
"綾波、疲れ…溜まってるんじゃ\nないかな。\n\0":
'???',

# Rei Ayanami 
"宇宙から来て、\nこの星の人間じゃないのなら\n宇宙人なんでしょう？\n\0":
'???',

# Shinji Ikari
"まあ………、そうだね。\n\0":
'???',

# Rei Ayanami 
"私、クローンなの。\n\0":
'???',

# Shinji Ikari
"ぶっ…！！▽\nさっき、宇宙人って\n言ったじゃないか！？\n\0":
'???',

# Rei Ayanami 
"でも、そうなの…。\n\0":
'???',

# Shinji Ikari
"何だか僕が疲れてきたよ。\n\0":
'???',

# Shinji Ikari
"綾波も…、\nそういう冗談言うんだね。\n\0":
'???',

# Rei Ayanami 
"そう？\n碇君には\n教えておきたかったの。▽\n好きだから。\n\0":
'???',

# Rei Ayanami 
"一緒にいたいのは、\n好きだって事でしょう？\n\0":
'???',

# Shinji Ikari
"そう…だね…。\n\0":
'???',

# Rei Ayanami 
"碇君は、私の事好き？\n\0":
'???',

# Shinji Ikari
"え…、えーと、▽\nえーっと。▽\nまあ…、好き、かな？\n\0":
'???',

# Rei Ayanami 
"じゃあ、耳掻きしてあげる。\n\0":
'???',

# Shinji Ikari
"…？？？\nどうして耳掻きなの？\n\0":
'???',

# Rei Ayanami 
"横になって。\n\0":
'???',

# [Text Only - No Designated Speaker]
"何だかよくわからないまま、\n耳掻きをしてもらった。\n\0":
'???',

# Shinji Ikari
"くすぐったいよ…。\n\0":
'???',

# Shinji Ikari
"うん…。▽\nねえ、何で耳掻きなの？\n\0":
'???',

# Rei Ayanami 
"好きな人には、\nするものなんでしょう？\n\0":
'???',

# Shinji Ikari
"よくわからないよ…。\n\0":
'???',

# Rei Ayanami 
"碇司令、\nいつもやってもらってたって。\n\0":
'???',

# Shinji Ikari
"…誰に！？\n\0":
'???',

# Rei Ayanami 
"碇君の、お母さん…。\n\0":
'???',

# Shinji Ikari
"……………………。▽\nそうなんだ。\n僕にはそんなの、\n想像出来ないけどね。▽\nそうなんだ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"父さんは、母さんの事を\nちゃんと好きだったのかな。\nそんな事をぼんやり考えた。\n\0":
'???',

# Rei Ayanami 
"仕上げ。\n息、吹きかけるわね。\n…ふー…っ。\n\0":
'???',

# Shinji Ikari
"わ、わぁぁッ！？\n\0":
'???',

# Shinji Ikari
"……………あ、綾波。▽\nひょっとしてそういう事、\n他の人にもした事ある？\n父さん…、とか…。\n\0":
'???',

# Rei Ayanami 
"ううん、碇君だけ。\n好きだから。\n好きな人にしかしないわ。\n\0":
'???',

# Shinji Ikari
"そう…。\nなら、いいけど。\n（何がいいのかわかんないケド。）\n\0":
'???',

# Rei Ayanami 
"嫌だった…？\n\0":
'???',

# Rei Ayanami 
"そう、よかった…。\n\0":
'???',

# Shinji Ikari
"さっきの冗談だよね？\n宇宙人とか…。\n\0":
'???',

# Shinji Ikari
"いや、いいよ。\n綾波だったら、宇宙人でも。\n\0":
'???',

#
# ./USRDIR/event/cev0105.har_EXTRACT/cev0105.evs
#
# [Text Only - No Designated Speaker]
"なんだろう…。\nどこからか…、猫の鳴き声が…。\n\0":
'???',

# Shinji Ikari
"ここから…かな？\n\0":
'???',

# [Text Only - No Designated Speaker]
"リツコさんの研究室だった。\n\0":
'???',

# Shinji Ikari
"すいません、いきなり…。\nなんだか猫の鳴き声が\n聞こえたもので…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"その時、リツコさんの顔は\n何だかバツが悪そうだった。▽\nイタズラを見つかった\n子供のような、そんな感じで。\n\0":
'???',

# Ritsuko Akagi 
"…聞こえてた？\n\0":
'???',

# [Text Only - No Designated Speaker]
"リツコさんが手招きする。\n僕は書類が山と積まれた机を\n回り込んだ。\n\0":
'???',

# Shinji Ikari
"わぁ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕は思わず声をあげてしまった。\n子猫だ…。\nそれも二匹…。\n\0":
'???',

# Shinji Ikari
"まだ赤ちゃん…ですね。\nお母さんと、はぐれちゃったん\nでしょうか？\n\0":
'???',

# Ritsuko Akagi 
"ダンボール箱の中に\nタオルが敷いてあったから…。\n多分、捨てられたのね。▽\n…疎開する家族が多いから。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そう言いながらリツコさんは、\nいとおしそうに、子猫達を\n眺めていた。▽\nあの普段のキツさからは\n想像もつかない程の\n優しい表情だった。\n\0":
'???',

# Shinji Ikari
"あの…、ここで飼うんですか？\n\0":
'???',

# [Text Only - No Designated Speaker]
"猫をあやしていたリツコさんの手が、\n空中で静止した。\nそしてフゥッと溜息をついた。\n\0":
'???',

# Ritsuko Akagi 
"…そんなわけには行かないわよね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女の整えられた眉毛が、\nキリキリと寄せられた。\n奇麗な顔だ。\n\0":
'???',

# Shinji Ikari
"じゃあ、どうしましょう…。\n僕んち…、ペンペンいるし…。\n\0":
'???',

# Ritsuko Akagi 
"私の家でも、飼えないわ…。\n\0":
'???',

# Ritsuko Akagi 
"やっぱり元の所へ、戻す他\nないのかしら…。\n\0":
'???',

# Shinji Ikari
"じゃあ、里親になってくれる人を\n探しましょうよ。\n僕、手伝いますから…。\n\0":
'???',

# Ritsuko Akagi 
"そうね。▽\nこの子達の為にも、\nそのくらいの努力は\nしてあげないと…。\n\0":
'???',

# Shinji Ikari
"すみません、この猫\n飼ってもらえませんか？\n\0":
'???',

# [Text Only - No Designated Speaker]
"何時間も粘ったけれど、\n猫を引き取ってくれる人は\n現れなかった。\n\0":
'???',

# Ritsuko Akagi 
"そうね…。\nやっぱり元の場所に\n置いておいた方がいいのかしらね。▽\nあんまり一緒にいると、\n本当に離れられなくなって\nしまうから…。\n\0":
'???',

# Shinji Ikari
"それがわかってても、\n連れてきてしまったんですね。▽\n何か…、リツコさんにしては\n意外だな…。\n\0":
'???',

# Ritsuko Akagi, Shinji Ikari
"そう？\n\0":
'???',

# Shinji Ikari
"あ、いえ、すみません…。\n\0":
'???',

# Ritsuko Akagi 
"いいのよ。\n周りからも、普段の私は\n事務的な人間に見えるみたいだし。▽\n私は科学者だもの。\nそれでいいとも思っているから。\n\0":
'???',

# [Text Only - No Designated Speaker]
"リツコさんの、\n何か割り切れないような表情。\n\0":
'???',

# Ritsuko Akagi 
"科学者としての私を、\n必要としている人がいるから。▽\n私はどこかで、科学者じゃない\n私自身になれる場所を\n求めていたのかもしれない。\n\0":
'???',

# Ritsuko Akagi 
"そのせいで、この猫にも\n迷惑をかけてしまったみたいね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕の知っているリツコさんとは\n違う顔。\n\0":
'???',

# Shinji Ikari
"僕、そういう風に猫を可愛がる\nリツコさん…好きだな。▽\n別に科学者とかじゃなくっても、\n僕は…今のリツコさんが。\n\0":
'???',

# Ritsuko Akagi 
"子供が何を言ってるのよ。▽\nフ…。\nでも、ありがと。▽\nあなたが大人になったら、\nまたそんな風に言って\nくれるのかしら？\n\0":
'???',

# Shinji Ikari
"…え…っと。\n僕…。\n\0":
'???',

# Ritsuko Akagi 
"子供が無理してそういう事を\n言うもんじゃないわ。\n不器用なのね、あなたも。\n\0":
'???',

# [Text Only - No Designated Speaker]
"リツコさんが、困ったように笑って、\n子猫を抱き上げた。▽\n猫を箱に戻し、立ち去ろうとした時\n一人の少女が近寄ってきた。\n\0":
'???',

# Girl
"よかった、無事だったんだ。\nごめんね、捨てたりしてごめんね。\n\0":
'???',

# Shinji Ikari
"あ…。\n元の飼い主かな…。\n\0":
'???',

# Ritsuko Akagi 
"…そうみたいね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"寂しそうな、ほっとしたような\nリツコさんの笑み。\n\0":
'???',

# Ritsuko Akagi 
"可愛がってもらうのよ。\n\0":
'???',

# Shinji Ikari
"リツコさんも…。\n寂しい時は寂しいって言えば\n僕が可愛がってあげますよ。\n\0":
'???',

# Ritsuko Akagi 
"あなたが大人になったらね。\n\0":
'???',

#
# ./USRDIR/event/cev0115.har_EXTRACT/cev0115.evs
#
# [Text Only - No Designated Speaker]
"カヲル君は、\n何かを悩んでいるようだ。\n\0":
'???',

# Shinji Ikari
"どうしたの、カヲル君。\n\0":
'???',

# Kaworu Nagisa 
"あ、うん。\n今度、学校で進路相談があるだろ。\n\0":
'???',

# Shinji Ikari
"ああ、あるねぇ。\nそういえば、そんなのが。\n\0":
'???',

# Kaworu Nagisa 
"僕に、将来を選べる自由なんて\nあるのかなって。\n\0":
'???',

# Kaworu Nagisa 
"僕は生かされているんだ。\n自分で、自分の思うように\n生きる事は許されないんだ。\n\0":
'???',

# Shinji Ikari
"そんな…、父さんとかが\nそう決めたの？\n\0":
'???',

# Kaworu Nagisa 
"ネルフの人達じゃないよ。\n\0":
'???',

# Kaworu Nagisa 
"まあ、いいさ。\n今こうしてシンジ君と一緒に\nいられるのでも充分幸せだし。\n\0":
'???',

# Shinji Ikari
"カヲル君、何になりたいの？\n\0":
'???',

# Kaworu Nagisa 
"もし、願いが叶うのなら…。\nメークアップアーティストに\nなりたいんだ。\n\0":
'???',

# Shinji Ikari
"え…、どんな仕事なの？\n\0":
'???',

# Kaworu Nagisa 
"人に化粧をしてあげて、\nその人の魅力を引き出して\nより美しくしてあげる仕事さ。\n\0":
'???',

# Shinji Ikari
"ちゃんと将来の事考えてるんだ。\nいいなぁ…、すごいなぁ…。▽\n僕にはちゃんとした目標なんて\nないもの。\n\0":
'???',

# Shinji Ikari
"でも、僕、カヲル君を\n応援するよ。\n夢が叶うように。\n\0":
'???',

# Kaworu Nagisa 
"ありがとう。\nじゃあ、お願いがあるんだけど。\n僕の練習台になってくれないかな？\n\0":
'???',

# Shinji Ikari
"へ？\n練習台…？\n\0":
'???',

# Kaworu Nagisa 
"君は、元がいいから。\nきっとメイク映えすると思う。▽\n僕が、キレイにしてあげるよ…。\n\0":
'???',

# Shinji Ikari
"えぇ！？\n僕、男だよ！\n化粧なんて、ちょっとそれは…。\n\0":
'???',

# Kaworu Nagisa 
"僕の夢、応援してくれるんだろ？\n\0":
'???',

# Shinji Ikari
"…えーと、それは。\n…………………しょうがないなぁ。\nどうぞ…。\n\0":
'???',

# Kaworu Nagisa 
"じゃあ…まず、ふき取り化粧水で\n皮脂を取って…、保湿化粧水と\n美容液で肌を整えて…。\n\0":
'???',

# Shinji Ikari
"え…、何か一杯持ってるね。\n\0":
'???',

# Kaworu Nagisa 
"うん、給料で買ったんだ。いつもは\n自分で試してるんだけど。他人に\n試すのはシンジ君が初めてだよ。\n\0":
'???',

# Shinji Ikari
"そ、そお…？\n\0":
'???',

# Kaworu Nagisa 
"この下地はね、内側から肌が\n輝くようになるんだ。▽\nえっと、ファンデはリキッド。\nピンク系を２種類混ぜて…。▽\nで、パウダーをＯＮ。\nハイライトはラメ入りを…。\n\0":
'???',

# Shinji Ikari
"僕、ど、どうなってるの…。\n\0":
'???',

# Kaworu Nagisa 
"キレイになってるよ、シンジ君。\n\0":
'???',

# Shinji Ikari
"そうなんだ…。\n\0":
'???',

# Kaworu Nagisa 
"アイホールはグリーンベース。\nブルーを重ねて、次はマスカラ…。\nチークは、幸せになれるピンク色。▽\n唇はね、グロスの重ね付けで。\nオレンジとピンクがいいな。▽\nフフ…、キレイ。\n美味しそうなフルーツみたいだ。▽\nきっと食べたら、甘酸っぱい味が\nするんだろうね。\n\0":
'???',

# Shinji Ikari
"出来た…の？\n\0":
'???',

# Kaworu Nagisa 
"うん。\n鏡見て…。\n\0":
'???',

# Shinji Ikari
"何か…、\n誰かに似てるような気がする。▽\n綾波…？\nまさか…ね。\n\0":
'???',

# Kaworu Nagisa 
"今日のは上出来だ、フフフ。▽\n今度はもっと、クールで\nロマンティックなメイクを\nしてあげるね。\n\0":
'???',

# Shinji Ikari
"えぇぇ…、またするの？\n\0":
'???',

# Kaworu Nagisa 
"僕の夢を応援してくれるんだろ？\n大丈夫、絶対にキレイにするから。\n…ね？\n\0":
'???',

# Shinji Ikari
"わかったよ。\nだけど、みんなには内緒にしてよ。\n\0":
'???',

# Kaworu Nagisa 
"うん。\nこれは、僕達二人だけのヒミツさ。\n\0":
'???',

#
# ./USRDIR/event/cev0307.har_EXTRACT/cev0307.evs
#
# Rei Ayanami 
"私は…、私の生き方は…。\n私の望みは……………。\n\0":
'???',

# Rei Ayanami 
"私の役目は決まっている…。\n目的を知ろうと知らずとも…、\n誰かの為に生きる事なんだわ。\n\0":
'???',

# Rei Ayanami 
"心が騒ぐ。\n今まで、私の心には碇司令しか\nいなかったのに。▽\n他の人や…、たくさんの出来事が\n私を変えていく。\n\0":
'???',

# Rei Ayanami 
"私は、還らなければならないの？\n誰かの為に…、誰の為に…？\n\0":
'???',

#
# ./USRDIR/event/cev0405.har_EXTRACT/cev0405.evs
#
# Ryoji Kaji
"ああ、これからだ。\n\0":
'???',

# Misato Katsuragi 
"パイロットの回収作業、\n急いで！！▽\nそれから、総員退避。\n\0":
'???',

# Maya Ibuki 
"あれ…は、何…。\nレイ！？\n\0":
'???',

# Makoto Hyuga, Male Staff
"退避ですか？\n\0":
'???',

# Misato Katsuragi 
"半径２０キロ以内の全市民にも\n避難勧告を。▽\nパイロットを救出後、\nエヴァには自爆プログラムを\n急いで！\n\0":
'???',

# Male Staff
"あれは何だ…。\nファースト…！？\n\0":
'???',

# Gendo Ikari
"人類の母、リリスとの融合を\n果たし、すべてを始まりに還す。\n\0":
'???',

# Seele 01
"リリスが…、我等の願いが…\n去っていく…。\n\0":
'???',

# Seele 02
"エヴァを連れ去る気か！？\n神への道が…閉ざされてしまう。\n\0":
'???',

# Seele 05
"こんな…、こんな事は\n計画にはないのだぞ！\n\0":
'???',

# Keel Lorenz
"神が、去るか…。\n\0":
'???',

# Misato Katsuragi 
"させません。\n\0":
'???',

# Misato Katsuragi 
"ネルフを、\nそして父を利用したあなたを\n私は許さない…。\n\0":
'???',

# Misato Katsuragi 
"私の戦いはもう…、終わったの…。\n\0":
'???',

# Misato Katsuragi 
"もう、終わったのね。\n全部…、何もかも…。\n\0":
'???',

# Ryoji Kaji
"本当に立ち向かわなくては\nならないものは、\nいくらでもある。▽\n俺も、君も…。\n\0":
'???',

# Misato Katsuragi 
"これからなのね…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"傷口の紅が、身体を伝う。\n膝を突いて、空を見上げた。\n\0":
'???',

# Misato Katsuragi 
"世界は生き続けるわ。\nどんな事になろうとも。\n一人一人が生きようとする限り。▽\n誰にも侵せない。\n生きていこうとするその思いだけは。▽\n…………………………。\n\0":
'???',

# Misato Katsuragi 
"レイ…。\nどこへでも行きなさい。\nあなたは自分の為に生きられるわ。\n\0":
'???',

# Rei Ayanami 
"…いいえ。\n私は還るわ。\n私が元いた、あの闇の中へ。▽\n…さよなら。\n\0":
'???',

# Misato Katsuragi 
"………れた。\nもう…、疲れたわ。▽\n父さん…、みんな…。\nもう、終わったの。\n全部…、何もかも…。\n\0":
'???',

# Rei Ayanami 
"ここは、大丈夫。\nこの星は、私の子らは大丈夫…。\n\0":
'???',

#
# ./USRDIR/event/cev0601.har_EXTRACT/cev0601.evs
#
# Kozo Fuyutsuki
"例えば、このケース。\n一人の男を被験者として、\n実験を行ったものだ。▽\n誘導催眠において、\n火傷をしたという擬似的な\n記憶を作り出した。▽\n明確な火傷の状況を与えると、\n実験後、身体に火傷の跡が現れた。▽\n一種の体験を作り出し、他人が\nその意識、記憶に干渉する事は\n現在も研究が行われており…。▽\n人は、普段体験している現実と違う\nもう一つの現実を生み出す可能性を\n持っているものだと思われる。\n\0":
'???',

# Kozo Fuyutsuki
"時間だ。\n続きは来週にしよう。\n\0":
'???',

# Kozo Fuyutsuki
"あの時、\n私はただの大学講師だった。\n\0":
'???',

# Kozo Fuyutsuki
"生物同士による、\n意識のリンクの可能性か。▽\nグループを作った意識が\n進化を喚起させる…ふむ。\n\0":
'???',

# Kozo Fuyutsuki
"はい、どうぞ。\n\0":
'???',

# Kozo Fuyutsuki
"ちょうど今、読ませてもらったよ。\n２、３疑問が残るが面白い着眼点だ。▽\n久しぶりに刺激のある\nレポートだったよ。\n\0":
'???',

# Yui Ikari
"ありがとうございます。\n\0":
'Thank you very much.\n\0',

# [Text Only - No Designated Speaker]
"彼女からは、\nラベンダーの香りがした。\n\0":
'???',

# Kozo Fuyutsuki
"碇ユイ君…だったね？\n君はこの先どうするつもりかね。▽\n就職か？\nそれとも大学院に進んで、\n研究室に入るつもりかな？▽\n推薦状が必要なら、いつでも書くよ。\n\0":
'???',

# Yui Ikari
"まだそこまで考えてはいません。\nそれに第３の選択もあるんじゃ\nありません？\n\0":
'???',

# Kozo Fuyutsuki
"第３の選択？\n\0":
'A third option?\n\0',

# Yui Ikari
"家庭に入ろうかと思ってるんですよ。\nいい人がいればの話ですけど。\n\0":
'???',

# Kozo Fuyutsuki
"それが、彼女…、\n碇ユイとの出会いだった。\n\0":
'???',

#
# ./USRDIR/event/cev0602.har_EXTRACT/cev0602.evs
#
# Kozo Fuyutsuki
"そのバックボーンとなる組織を\nゼーレと言う。\n\0":
'???',

# Kozo Fuyutsuki
"碇…か。\n\0":
'???',

# Kozo Fuyutsuki
"だが、碇の思惑がどうあれ…、\n彼女は碇と共に歩く事を\n選んだのだ。\n\0":
'???',

# Kozo Fuyutsuki
"彼女は…、私には到底、\n届く事の出来ない存在だった。\n\0":
'???',

# Kozo Fuyutsuki
"そういえば、あの男の第一印象は\nイヤな男だったな…。▽\nだが、その男に連れ添う\n女性の名を知った時、\n私は驚きを隠せなかった。\n\0":
'???',

# Kozo Fuyutsuki
"彼は、彼女…碇ユイの才能と\nそのバックボーンを目当てに\n近づいたと仲間内では言われていた。\n\0":
'???',

# Kozo Fuyutsuki
"彼女は、そのゼーレ有力者の一人の\n子女であり、碇はそこに目をつけた。\n\0":
'???',

#
# ./USRDIR/event/cev0603.har_EXTRACT/cev0603.evs
#
# Kozo Fuyutsuki
"だが、彼女はもういない。\n\0":
'???',

# Kozo Fuyutsuki
"人類補完計画。\n碇が提案したその計画に私は賭けた。▽\n人々の心を一つにし、安らぎの時を\n永遠に生きる。▽\n初号機に宿る彼女の魂さえも\n一つにして…。\n\0":
'???',

# Kozo Fuyutsuki
"２００４年、エヴァ初号機との\n接触実験で被験者となった彼女は、\nそのまま帰らぬ人となった。\n\0":
'???',

# Kozo Fuyutsuki
"久しぶりに、\nあの論文を手に取った。▽\n彼女…、碇ユイの\nあの論文だ。▽\n生物同士による、\n意識のリンクの可能性。▽\nそれぞれ色が違うというのに、\n群れ集まって花のような擬態を\n作り上げる虫がいる。▽\nその虫達の共同体から、一つの\n意識が構成されているという\n仮説があるのだ。▽\n彼女は人間、また他生物も\n同じように意識の繋がりを持ち…、▽\nそれらが干渉しあう事で、\n進化の糸口を生み出すと言う\nものだった。▽\n生物の変性意識を人工的に\n作り出し…、それらを一つにまとめ、\n進化させる。▽\n人類補完計画の雛型となる\n理論となっていた。\n\0":
'???',

#
# ./USRDIR/event/cev0604.har_EXTRACT/cev0604.evs
#
# Kozo Fuyutsuki
"永遠の存在であるエヴァ。\n今や、彼女と言う魂を得て、\n神となったのだろう。\n\0":
'???',

# [Text Only - No Designated Speaker]
"人々の心の隙間を埋める補完計画。▽\nゼーレは、サードインパクトに\nより全人類を完全な単体生物へと\n進化させるべくこの計画に乗り、▽\n私と碇は、全人類の心を互いに\n補完する事をこの計画の目的とした。▽\n我々は、ゼーレの老人達を\n欺きながら、お互い異とした\n目的を歩んでいるのだ。▽\n全ての使徒を倒す、その時まで。\n\0":
'???',

# [Text Only - No Designated Speaker]
"絶対的な存在である神の元へ\n我々は向かう事が出来るのか。▽\n例え賭けであったとしても…、\n彼女に再び会う為には\n私はこの計画に臨む他なかった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"…彼女は、\n人類が生きた証となるべく\n初号機に残った。▽\n彼女はここにいる。\nこの初号機の中に。▽\nだが、我々人間には\n手の届かぬところだ。▽\n魂がどこにあるのかわからない。\n人の心なども、どこにあるのかも。▽\nだが、人類はその魂の存在を\nずっと探し続けていた。\n同時に神の存在も。▽\n人は、不死を願って魂の存在を\nあるものとし、死後永遠の存在で\nあるべく神を必要としたのだ。▽\nだが、科学の力は魂の存在を\n証明した。▽\nそして再び、\n人は神を必要としている。\n\0":
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
# ./USRDIR/event/cev0606.har_EXTRACT/cev0606.evs
#
# Kozo Fuyutsuki
"私は京都へ向かった。\nかつて、彼女と出会ったあの土地へ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"大学には、多くの論文が\n保管されている。▽\n彼女のものを探すのは、\n結構骨が折れた。\n\0":
'???',

# Kozo Fuyutsuki
"これか…？\n碇ユイ。\nこれだ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女に会えたような喜びだった。\n静かに、彼女の論文をめくる。\n\0":
'???',

# Kozo Fuyutsuki
"故意に変性意識を\n生み出すには…。▽\n…これは、エヴァとの\nシンクロを促すための\n基礎理論であったものか…？▽\n自己の意識の拡大と\n他者への意識の干渉…。\n精神汚染…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女との再会を喜ぶような気持ちで、\nゆっくりとページをめくっていった。\nなんと充実した時間だろう。▽\nこの論文が書かれた時点ではまだ、\n改良の余地はあった。▽\nだが、変性意識を作り出す条件は\nそう難しい事ではない。▽\nエヴァのパイロットはこれらの\nフォローを受けてシンクロ状態を\n作り出すのだ。▽\n私は、彼女の論文を持ち帰った。\n\0":
'???',

#
# ./USRDIR/event/cev0607.har_EXTRACT/cev0607.evs
#
# [Text Only - No Designated Speaker]
"人体にある特定の\n温度、匂い、音による刺激を\n送り込む事で変性意識を作り出す。▽\nしかし、自分一人で行うとなると\nこの研究は難しい。▽\n一歩間違えば、精神を破壊する\n危険性もある。▽\n被験者、観察者が必要だ。▽\nだが、意を決して\nこの実験は私一人で行う事にした。\n\0":
'???',

# Kozo Fuyutsuki
"必要な機材はそろった。\n始めよう。\n\0":
'???',

# Kozo Fuyutsuki
"この方向で調整を行っていこう。\n\0":
'???',

# Kozo Fuyutsuki
"悪夢を見たような、嫌な気分だ。\n実験は失敗か…。\n\0":
'???',

#
# ./USRDIR/event/cev0608.har_EXTRACT/cev0608.evs
#
# [Text Only - No Designated Speaker]
"私は、実験を繰り返した。▽\nこの実験は、ひどく精神力を\n消費した。▽\n実験の後は、無気力状態とでも\n言おうか…ひどく思考力が落ちた。▽\nだが、私はこの実験を止める事は\nしなかった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"不思議な感覚があった。▽\n身体の輪郭がぼやけ、\nどこまでも自分が広がるような\n感覚を体験する。▽\n波間に漂うような感覚に\n身を任せ、私は意識の移ろいを\n感じていた…すると。\n\0":
'???',

# [Text Only - No Designated Speaker]
"突然、別の空間に放り込まれた\nような浮遊感を感じた。\n目の前に様々な映像が現れる。\n\0":
'???',

# Kozo Fuyutsuki
"これは、走馬灯か…？\n\0":
'???',

# [Text Only - No Designated Speaker]
"過去から今までの時間が\n全て噴出し、溢れかえった。\nこれが、変性意識の状態なのか。▽\n私は、かつて己が体験してきた\n時間の中に溺れた。\nそしてその中に…彼女はいた。\n\0":
'???',

# Yui Ikari
"失礼します。\n\0":
'???',

# Kozo Fuyutsuki
"君が碇君？\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女に出会ったあの時、\nそのままだった。\nラベンダーの香りがする。\n\0":
'???',

# [Text Only - No Designated Speaker]
"その一つの場面に、\n意識をあわせようとするが\nどうも上手くいかない。▽\n彼女がいる場面に手を伸ばそうと\nしたが、まるで急流に押し流される\nように遠ざかってしまう。\n\0":
'???',

# [Text Only - No Designated Speaker]
"目が覚めた。▽\nそして、実験後の何ともいえない\n疲労感に襲われた。▽\n一つわかった事がある。▽\n最も安定した意識の状態へと\n繋がる為には強靭な精神力を\n必要とする。▽\n実験後は、次の実験の為に\n自分の精神状態を\n高めなくてはならない。\n\0":
'???',

# [Text Only - No Designated Speaker]
"実験を誤ると、\nとても不快な症状が現れる。\n吐き気、めまい、倦怠感。▽\nどうやら、\n今回は失敗だったようだ。▽\n一つわかった事がある。▽\n最も安定した意識の状態へと\n繋がる為には強靭な精神力を\n必要とする。▽\n実験後は、次の実験の為に\n自分の精神状態を\n高めなくてはならない。\n\0":
'???',

#
# ./USRDIR/event/cev0609.har_EXTRACT/cev0609.evs
#
# [Text Only - No Designated Speaker]
"どうやら、\n今回も失敗だったようだ。▽\n最も安定した意識の状態へと\n繋がる為には強靭な精神力を\n必要とする。▽\n実験後は、次の実験の為に\n自分の精神状態を\n高めなくてはならない。\n\0":
'???',

# [Text Only - No Designated Speaker]
"私は、実験を繰り返した。\n\0":
'???',

#
# ./USRDIR/event/cev0611.har_EXTRACT/cev0611.evs
#
# [Text Only - No Designated Speaker]
"目が覚めた。▽\nそして、実験後の何ともいえない\n疲労感に襲われた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"不思議な感覚があった。▽\n身体の輪郭がぼやけ、\nどこまでも自分が広がるような\n間隔を体験する。▽\n波間に漂うような感覚に\n身を任せ、私は意識の移ろいを\n感じていた…すると。\n\0":
'???',

#
# ./USRDIR/event/cev0612.har_EXTRACT/cev0612.evs
#
# Kozo Fuyutsuki
"ラベンダーの香り…？\nああ、アロマオイルか。▽\n…これは、\n実験に使えないだろうか。\n\0":
'???',

#
# ./USRDIR/event/cev0613.har_EXTRACT/cev0613.evs
#
# Kozo Fuyutsuki
"ユイ君、ユイ君…？\n\0":
'???',

# [Text Only - No Designated Speaker]
"実験を始める前に、\nアロマオイルを開封する。▽\n部屋中がラベンダーの香りに\n満たされた。▽\nこの思惑は予想外の成果を\n生み出した。\n\0":
'???',

# Kozo Fuyutsuki
"意識が広がるのを感じる。\n\0":
'???',

# [Text Only - No Designated Speaker]
"前回に比べ、よりリアルな\nヴィジョンが溢れるのを\n私は見た。▽\nラベンダーの香りが、\n私を彼女との出会いの時間へと\n導いた。▽\nヴィジョンの中の私と彼女。\nそれを他人のように自分自身は\n見るのだった。▽\nそれだけでもよかった。\nだが…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"夢だったのだろうか。\nだが、私は言い知れぬ恍惚感の中\n意識を覚ました…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"何者かが、自分自身に意識を\n向けているような気がした。\nこちらも意識を向ける。\n\0":
'???',

# Kozo Fuyutsuki
"…君…は？\n\0":
'???',

# [Text Only - No Designated Speaker]
"静かな驚きと共に、\n私は喜びを隠せずにいた。\n\0":
'???',

# Yui Ikari
"冬月先生。\n\0":
'???',

# Kozo Fuyutsuki
"ユイ君…。\n\0":
'???',

# Yui Ikari
"ご自身で、\nここまで来られたのですね？\n\0":
'???',

# Kozo Fuyutsuki
"ここは？\n\0":
'???',

# Yui Ikari
"ここは、人々の意識が混ざり合う\nところ…とでも言いましょうか。▽\n人間や全ての生物は自分自身の中に\nこの場所を持っています。▽\nここには時間も空間もありません。\n過去も未来も全て、あるのです。\n\0":
'???',

# Kozo Fuyutsuki
"君はここにいたのかね？\n\0":
'???',

# Yui Ikari
"そう、とも言えますし、\n違う、とも言えます。▽\nしかし、人類はこの段階まで\n来る事が出来ません。▽\n人々の意識が、\nここに気付かないからです。\n\0":
'???',

# Kozo Fuyutsuki
"気付かないとは？\n\0":
'???',

# Yui Ikari
"精神を、心を明らかに\n出来ないからです。▽\n喜び、怒り、苦しみ、悲しみ…、\nこれらの感情に、人の思考は\nとらわれてしまいます。▽\nですが、心をありのままに\n受け止め…、見る事が出来る人は\nここへ来る事が出来ます。\n\0":
'???',

# Kozo Fuyutsuki
"では、人類補完計画は…。\n人工的に人類をこのステージへ\n導くもの…か。\n\0":
'???',

# Yui Ikari
"それは、もう一歩先の段階に\nなります。▽\nですが、あの計画がなかったと\nしても、一人一人に気付きがあれば\nいずれここへ来る事になります。▽\nここは、全ての意識と交じり合う\n場と共に、冬月先生…\n…あなたの中に存在する場所です。\n\0":
'???',

# Kozo Fuyutsuki
"私の…？\n\0":
'???',

# Yui Ikari
"人と、人の希望の数だけ\n現実はあります…。▽\n冬月先生は私を求め、\nそしてここまで来られた。\n先生の現実です…。\n\0":
'???',

#
# ./USRDIR/event/cev0614.har_EXTRACT/cev0614.evs
#
# Kozo Fuyutsuki
"神…。\n人は神になり得るのか。\n自分自身の力で。\n\0":
'???',

# [Text Only - No Designated Speaker]
"人々を導く必要など\n無いのだろう。\n選べばよいのだ、自分自身で。\n\0":
'???',

# [Text Only - No Designated Speaker]
"あの実験は夢だったのか。\nだが、今もあの時の彼女の声は\nはっきりと覚えている。▽\n声は、とてつもない現実感を\n保ったまま、私の中を駆け巡る。▽\n今いるこの現実が、薄っぺらくすら\n感じてしまう。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女はあの世界にいるのだ。▽\nこの初号機の中にいながら、\nあらゆる世界に偏在している\nのではないだろうか。\n\0":
'???',

# [Text Only - No Designated Speaker]
"私は、一つの思いに心を\n動かされた。\n\0":
'???',

#
# ./USRDIR/event/cev0615.har_EXTRACT/cev0615.evs
#
# [Text Only - No Designated Speaker]
"突然、目の前が暗くなった。▽\n人が集まってくる。\n\0":
'???',

# [Text Only - No Designated Speaker]
"実験の繰り返しのせいだろうか。▽\n実験に必要な環境を揃えなくても\n「あの感覚」を私は呼び覚ます事が\n出来た。▽\n私は意識が広がるままに任せた。\n彼女がいるのだ。\n何を恐れる事があるだろう。\n\0":
'???',

# Yui Ikari
"冬月先生？\n\0":
'Fuyutsuki-sensei?\n\0',

# Kozo Fuyutsuki
"君か…。\n\0":
'???',

# Yui Ikari
"お戻りにならないのですか？▽\n変性意識状態を日常的に起こすと\n肉体へのフィードバックに負担が\nかかります。\n\0":
'???',

# Kozo Fuyutsuki
"構わない。▽\nいや、もうこの状態を\n知ってしまったら…元には\n戻れないよ。\n\0":
'???',

# Yui Ikari
"個人の自由意志が、\n全てを決めます。\n\0":
'???',

# Kozo Fuyutsuki
"そうだ。\nここが私の現実だ。▽\nだが、もっと知りたいんだ。\nこの世界の事を。\n\0":
'???',

# Yui Ikari
"それはどの世界でも同じ。\n全ては流れのままに。\n答えと真実は自分の中に…。\n\0":
'???',

# Kozo Fuyutsuki
"………ここは。▽\nそうか…。\n戻ってきてしまったか…。\n\0":
'???'

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
'Why are the deputy\ncommander\'s clothes here?\nThey\'re wet...\n\0',

# Maya Ibuki, Female Staff
"これ、この液体…、\nＬＣＬ！？▽\n副司令は…、副司令は…！？\n\0":
'This-This fluid...\nL.C.L.?!▽\The deputy commander, he\'s...?!\n\0',

# [Text Only - No Designated Speaker]
# How does と言う affect the meaning here? -Reichu
"一瞬だけ、初号機の前に佇む\n冬月を見た者がいた。▽\n彼は、初号機へ手を伸ばし、\n次の瞬間には消えていたと言う。\n\0":
'For just a moment, someone saw\nFuyutsuki standing in front of Unit-01.▽\nHe extended his hands to Unit-01,\nand disappeared an instant later.\n\0',

# [Text Only - No Designated Speaker]
"それが、最後の目撃となった。▽\nその後、冬月の姿を見る者は、\n誰もいなかった。\n\0":
'That was to be the last sighting.▽\nEver since then,\nno one has seen Fuyutsuki.\n\0',

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
'Yui-kun!\n\0',

# Yui Ikari
"その時まで、お元気で。\n先生…。\n\0":
'???',

# Kozo Fuyutsuki
"…ユイ君。\n\0":
'...Yui-kun.\n\0',

# Kozo Fuyutsuki
"ああ、その時までの\nお別れだ…。\n\0":
'???',

#
# ./USRDIR/event/cev0701.har_EXTRACT/cev0701.evs
#
# Ritsuko Akagi 
"もう、戻られますか？\n\0":
'???',

# Ritsuko Akagi 
"病院？\nレイのところでしょう。\n\0":
'???',

# Gendo Ikari
"………ああ。\n\0":
'???',

# Gendo Ikari
"君も戻りたまえ。\n私は、もう行く。\n\0":
'???',

# Ritsuko Akagi 
"勝手ね、本当に。\n少しだけ、このけだるさの余韻を\n味わわせてくれてもいいのに。▽\nもし、私があなただけのものじゃ\nなくなったら…。\nどんな顔をしてくれるのかしらね。▽\n見てみたいわ…。\n\0":
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

# Shinji Ikari, Shigeru Aoba
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
# ./USRDIR/event/cev0703.har_EXTRACT/cev0703.evs
#
# Ritsuko Akagi 
"あの男もそろそろ刈入れ時ね。\n今日は逃がさないわよ。\n\0":
'???',

# Ritsuko Akagi 
"副司令…。\n\0":
'???',

# Kozo Fuyutsuki
"赤木君か…。\n何だね？\n\0":
'???',

# Ritsuko Akagi 
"お話があるのですが。\n私の研究室まで、\nいらしてくださいませんか？\n\0":
'???',

# Kozo Fuyutsuki
"ふむ、よかろう。\n\0":
'???',

# Ritsuko Akagi 
"生前の母の事です…。\n副司令から見て、\nどんな女性でしたか？\n\0":
'???',

# Kozo Fuyutsuki
"赤木ナオコ君かね？\n\0":
'???',

# Ritsuko Akagi 
"母の命日が近いもので。\n思えば一緒に過ごした思い出が\nないものですから…。\n\0":
'???',

# Kozo Fuyutsuki
"そうか…。\nしかし、何から話せばよいかな。\n\0":
'???',

# Ritsuko Akagi 
"母は美しい女性でしたか。\n\0":
'???',

# Kozo Fuyutsuki
"…あまりそんな事には\n気が付かない性格でね。\nだが、優秀ではあったよ。\n\0":
'???',

# Ritsuko Akagi 
"では、私はどうですか…。\n\0":
'???',

# Kozo Fuyutsuki
"あ、赤木君…、君は…。\n\0":
'???',

# Ritsuko Akagi 
"副司令も…、きっかけを\n待っていたのでしょう？\nフフフフフ…。\n\0":
'???',

# Kozo Fuyutsuki
"赤木君…。\n\0":
'???',

# Ritsuko Akagi 
"フフフフフフ…。\n\0":
'???',

# Ritsuko Akagi 
"なかなか立派でしたわよ、\n副司令…。\n\0":
'???',

#
# ./USRDIR/event/cev0704.har_EXTRACT/cev0704.evs
#
# Ritsuko Akagi 
"いいのよ、怒らないから。\n\0":
'???',

# Makoto Hyuga
"そ、その美しい唇であります！\n\0":
'???',

# Ritsuko Akagi 
"ねえ、ミサトのどこが好きだった？\nミサトを見ている時は、ミサトの\nどこを見ていたのかしら。\n\0":
'???',

# Makoto Hyuga
"め、めっそうもない事…。\n\0":
'???',

# Ritsuko Akagi 
"ミサトと私…。\nどっちの唇がキレイ？\n\0":
'???',

# Makoto Hyuga
"…えーと、ですね。\nえぇと、えぇと…、その…。\n\0":
'...Uhhh, hard to say.\nUhhh, ummm... I...\n\0',

# Ritsuko Akagi 
"言えないの？\n悪い人ね…。\nこっちへいらっしゃい。\n\0":
'???',

# Ritsuko Akagi 
"じゃあ、仕返しにあなたのを\n見せてもらうわね。\n\0":
'???',

# Makoto Hyuga
"あっ…！？\n赤木博士…ッ！！\n葛城さーーーーーん！！\n\0":
'???',

# Ritsuko Akagi 
"彼女の名を呼ぶの？\nフフフ、可愛いわね。\n\0":
'???',

# Ritsuko Akagi 
"フフ…、ウブなのね。\n\0":
'???',

# Makoto Hyuga
"あっ…、赤木博士。\n\0":
'Um... Dr. Akagi.\n\0',

# Ritsuko Akagi 
"ねえ、今どこを見てたの？\n\0":
'???',

# Ritsuko Akagi 
"私を見ていたでしょう？\n私のどこを見ていたのかしら。\n\0":
'???',

# Makoto Hyuga
"いえ、僕は…その。\n\0":
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
'Still no good.\n\0',

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
'Aoba-kun?\n\0',

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
# ./USRDIR/event/cev0707.har_EXTRACT/cev0707.evs
#
# Ritsuko Akagi 
"あら、お買い物？\n\0":
'???',

# Toji Suzuhara 
"リツコさん。\n\0":
'Ritsuko-san.\n\0',

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
# ./USRDIR/event/cev0708.har_EXTRACT/cev0708.evs
#
# Kaworu Nagisa 
"あなたは…罪な人だ。\n僕が、この衝動を抑える苦しみを\n知っていながら…。\n\0":
'???',

# Ritsuko Akagi 
"だったら…、二人で堕ちましょう。\n\0":
'???',

# Kaworu Nagisa 
"赤木博士…。\n\0":
'???',

# Ritsuko Akagi 
"カヲル君…。\n\0":
'???',

# Ritsuko Akagi 
"あなたの白く透き通るような肌。\nうらやましいわ…。\n\0":
'???',

# Kaworu Nagisa 
"…あんまり、見ないでください。\n\0":
'???',

# Ritsuko Akagi 
"あら、どうして？\n\0":
'???',

#
# ./USRDIR/event/cev0709.har_EXTRACT/cev0709.evs
#
# Maya Ibuki 
"私…、私センパイの事を思って\n毎晩…。\n\0":
'???',

# Ritsuko Akagi 
"ふぅん、どうしてるの？\n\0":
'???',

# Ritsuko Akagi 
"フフフ…、楽しいわ。\n私、あんな男の為に\n何を我慢していたのかしら。▽\nそうね、だったらいっそ…。\n\0":
'???',

# Maya Ibuki 
"センパイ♪\n実験のデータ、\n報告書にまとめておきました。\n\0":
'???',

# Ritsuko Akagi 
"そう、ありがと…。\n私の可愛いマヤ…。\n\0":
'???',

# Maya Ibuki 
"センパイ…？\n\0":
'Sempai...?\n\0',

# Ritsuko Akagi 
"フフフ…、拒まないのね？\n\0":
'???',

#
# ./USRDIR/event/cev0710.har_EXTRACT/cev0710.evs
#
# [Text Only - No Designated Speaker]
"この男…、まだ私が従順でいると\n思っているのね。\n憐れな男だわ…。\n\0":
'???',

# Gendo Ikari
"赤木博士…。\n後で私の部屋に…。\n\0":
'???',

# Ritsuko Akagi 
"お断りしますわ。\n仕事の話じゃないのでしょう？\n\0":
'???',

# Gendo Ikari
"拒むつもりか？\n\0":
'???',

# Ritsuko Akagi 
"あなたの代わりなんて、\nいくらでもいるのよ。▽\n何が、人類補完計画よ。\n今の私には微々たる事だわ。\nええ、どうでもいい事よ。\n\0":
'???',

# Ritsuko Akagi 
"でも、あなたに\n私は捨てられない。\n私の力が必要なのね。\n\0":
'???',

# Gendo Ikari
"…………………………。▽\n…何が望みだ。\n\0":
'???',

# Ritsuko Akagi 
"あーっはっはっは。\n本当に一人じゃ何も出来ないのね。\n可哀想な人。▽\nそう…、あなたには\n私の人生を弄んだ償いを\nしていただきますわ。▽\nそうよ、ひざまずいて\n私という炎に焼かれるのよ。\n\0":
'???',

# Ritsuko Akagi 
"私は勝ったわ。▽\nこの男にも、母さんにも。\nまだまだよ。\nあなたの償いはこれからなんだから。▽\n身も心も…、焦がしてあげる…。\n女は炎…、遊びで近づくと\nヤケドするわよ…。\n\0":
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
# ./USRDIR/event/cev0802.har_EXTRACT/cev0802.evs
#
# Shigeru Aoba
"日向、見ろよ。\nこのグラビアアイドル。\n\0":
'???',

# Makoto Hyuga
"スタイルいいよなぁ。\n\0":
'???',

# Shigeru Aoba
"うぉー！\nこれなんて、バーンでボーンだよ。\nこんな彼女、いたらなぁ…。\n\0":
'???',

# Maya Ibuki 
"バカみたい…。\n\0":
'???',

# Shigeru Aoba
"まぁまぁ、ひがむなよ。\nマヤちゃん。\n\0":
'???',

# Maya Ibuki 
"ひがんでなんか、\nいませんよーっだ！▽\nなーによ、大の男が\nえっちぃな雑誌眺めて\nデレデレしちゃって！\n\0":
'???',

# Shigeru Aoba
"今のご時世、普通の男性週刊誌に、\nグラビア載ってて当たり前なんだぜ。▽\nマヤちゃん、\n何にも知らないんだもんな。\n\0":
'???',

# Misato Katsuragi 
"何見てるの？\nあらら…、イイ身体。\n\0":
'???',

# Misato Katsuragi 
"私も若い頃はねェ…、ハァ。\n\0":
'???',

# Makoto Hyuga
"いえいえ、ミサトさんには\n誰もかないませんよ。\n\0":
'???',

# Misato Katsuragi 
"またまたぁ〜。\nオネーサンをからかわないの。\n\0":
'???',

# Maya Ibuki 
"…………………………。▽\n（バカみたい…。）\n\0":
'???',

# Misato Katsuragi 
"マヤちゃんだって、\nいい脚してるわよね♪\n\0":
'???',

# Maya Ibuki 
"やめてください…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"嫌、嫌！\nそんな目で見ないでよ。▽\nそこのバカ男の目をこっちに\n向けさせないでよ。▽\n私は、そういう存在じゃない。\n怖い、怖い。\n大嫌い。▽\n汚い世界が大嫌い。▽\n窒息しそう…。▽\nまともなのは、センパイだけ。\nセンパイだけだ…。\n\0":
'???',

#
# ./USRDIR/event/cev0803.har_EXTRACT/cev0803.evs
#
# Maya Ibuki 
"食べちゃだめ…、\n食べちゃだめ…。▽\nああ、でも、止まらないよ…。▽\n寂しさでいっぱいになる前に\n食べないと…。\n心が、汚い世界に飲み込まれる…。\n\0":
'???',

# Maya Ibuki 
"まただ…。\nこんなに食べて…。▽\n吐き出さなきゃ…。\nどうして、こんな苦しい目に\nあわなきゃいけないんだろう。\n\0":
'???',

#
# ./USRDIR/event/cev0804.har_EXTRACT/cev0804.evs
#
# Maya Ibuki 
"別に、構いません。\n\0":
'It\'s not a big deal.\n\0',

# Shigeru Aoba
"うわー、可愛くねぇー…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"私…、いつも笑顔でいる\nつもりだったのに。▽\nどうしてそんなに、\n人を遠ざけているんだろう。▽\nやっぱり…、何にも持ってない\n空っぽの笑顔だって、\n見抜かれているかもしれない。\n\0":
'???',

# Shigeru Aoba
"マヤちゃんさぁ…。\nもう少し、\n愛想よく出来ないのかなぁ？\n\0":
'???',

# Maya Ibuki 
"えっ…。\n\0":
'???',

# Shigeru Aoba
"何ていうか、シャレ通じねーの。\nもう少し、柔軟になっても\nいいんじゃない？\n\0":
'???',

# Maya Ibuki 
"青葉君がいつも言っている事って\n…洒落にするには\n非常識すぎませんか？\n\0":
'???',

# Shigeru Aoba
"…駄目だこりゃ。\nそんなカタブツだと、\n一生独身だぜ。\n\0":
'???',

#
# ./USRDIR/event/cev0805.har_EXTRACT/cev0805.evs
#
# [Text Only - No Designated Speaker]
"尊敬出来るのは、\nセンパイだけだ。▽\n仕事にひたむきで、\n私情を決して仕事に持ち込まない。▽\n冷たくもあるけれど、\n完璧をいつも貫き通す。\nそして、みんなに認められている。▽\n私も、ああなりたい。\nセンパイみたいに。\n\0":
'???',

# Maya Ibuki 
"センパイ♪\n休憩ですか？\n\0":
'???',

# Ritsuko Akagi 
"ちょうどよかったわ、マヤ。\nこれに目を通しておいて。\n\0":
'???',

# Maya Ibuki 
"これ…ダミープラグ？\n新しい研究ですか？\n\0":
'???',

# Ritsuko Akagi 
"適格者が存在せずとも、\nエヴァの起動を可能にする\nシステムよ。▽\nその書類は、計画書。\n\0":
'???',

# Maya Ibuki 
"あの…、これにある…\n媒体…ダミーというのは\nどういうものなんですか？\n\0":
'???',

# Ritsuko Akagi 
"それをあなたに見せるわ。\n付いてきて。\n\0":
'???',

# Maya Ibuki 
"迷いそうですね。\n\0":
'???',

# Ritsuko Akagi 
"頻繁に通う事になるから\n慣れるわよ。\n\0":
'???',

# Ritsuko Akagi 
"あなたには、このＩＤカードを\n渡しておくわ。▽\n研究材料は、この先にあるの。\n\0":
'???',

# Ritsuko Akagi 
"明かりをつけるわ。\n\0":
'???',

# Maya Ibuki 
"…セン、…パイ！？\n\0":
'???',

# Ritsuko Akagi 
"ただの人形よ。\nクローンなの。\n\0":
'???',

# Maya Ibuki 
"研究材料って…。\n\0":
'???',

# Ritsuko Akagi 
"そう。\nこれにレイのパターンを\n移植するのよ。▽\n実用化が出来れば、\n適格者が欠けても…。\n\0":
'???',

# Maya Ibuki 
"こんな事をしてまで、ですか？\n\0":
'???',

# Ritsuko Akagi 
"そうよ、人類が生き延びる為には\nどんな可能性にも\n賭けなくてはならない。▽\nそうでしょ？\n私達の仕事は。\n\0":
'???',

# Maya Ibuki 
"…それは、そうですけど。\n…でも。\n\0":
'???',

# Ritsuko Akagi 
"納得出来ないのはわかるわ。\n生きていれば、目を背けてばかり\nいられない事もある。▽\n目を背けて抗おうとする方が\n自分を苦しめる事にもなるのよ。\n\0":
'???',

# Ritsuko Akagi 
"じゃあ、計画書どおり\n順次実験は行っていくわ。\n頼りにしてるわよ、マヤ。\n\0":
'???',

#
# ./USRDIR/event/cev0806.har_EXTRACT/cev0806.evs
#
# [Text Only - No Designated Speaker]
"食べて、吐いて、食べて…\nアレを思い出すたびに\n身体が世界を拒否しようとする。\n\0":
'???',

# Maya Ibuki 
"苦しい。\n助けて。▽\n寂しい、寂しいよぅ。\n誰か、助けて…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"私は…、\nたった一つの心の寄り所を\n失ってしまった。▽\n心が、身体が\nぐずぐずと腐れて行くような感じ。\n\0":
'???',

# Maya Ibuki 
"どうしたらいいんだろう…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"でも、どうしようも出来ないんだ。\n朝になったら、何もなかった様に\n笑っていなきゃいけないんだ。▽\n笑っていなきゃ…。\n誰も私を必要としなくなる。\n例え、空っぽの笑顔でも…。\n\0":
'???',

# Maya Ibuki 
"ごほっ…。\nう…ぅ………。\n\0":
'???',

# [Text Only - No Designated Speaker]
"見てはいけない。\n見てはいけないものだったんだ。\nあんなもの…。\n\0":
'???',

# Maya Ibuki 
"どうしよう、逃げられない…。\nセンパイを裏切る事なんて\n出来ない…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"甘かった。\n私は本当に、\nセンパイに憧れていただけだった。▽\n何も知らずに…。\n\0":
'???',

# Maya Ibuki 
"私、汚れちゃうのかなぁ…。\nお母さん…、お母さん…。\n\0":
'???',

#
# ./USRDIR/event/cev0807.har_EXTRACT/cev0807.evs
#
# Shigeru Aoba
"マヤちゃん？\n\0":
'???',

# Maya Ibuki 
"何…？\nまた、可愛くないって\n言いに来たの？\n\0":
'???',

# Shigeru Aoba
"あのな…。\n\0":
'???',

# Shigeru Aoba
"いや、そんなんじゃないよ。\n元気、なさそうだから。\nいつも笑ってるのに。\n\0":
'???',

# Shigeru Aoba
"何かあったのかなって\n思って。\n\0":
'???',

# Maya Ibuki 
"………さいよ。\n\0":
'???',

# Shigeru Aoba, Shinji Ikari
"え？\n\0":
'???',

# Maya Ibuki 
"そんな無理矢理に笑顔を要求したり、\n愛想よくしろとか言わないで\nくださいよ！！▽\n私には何にも無いんだから、\nそんなに器用じゃないから！！\n\0":
'???',

# Shigeru Aoba
"マヤちゃん…。\nあの…。\n\0":
'???',

# Maya Ibuki 
"…………………………。▽\nごめんなさい。\n\0":
'???',

# Shigeru Aoba
"仕事…大変なの？\n\0":
'???',

# Shigeru Aoba
"グチぐらい、いつでも聞くのに。\n\0":
'???',

# Maya Ibuki 
"イヤ。\nみっともないから。\n\0":
'???',

# Shigeru Aoba
"俺なんて、しょっちゅうグチばっか。\nじゃあ俺、みっともないのかなー。▽\nでも、やってられねーもん。\nグチったりでもしなきゃさ。\n\0":
'???',

# Maya Ibuki 
"何を言っていいのか、\nわからないの。\n\0":
'???',

# Shigeru Aoba
"…ふーん。\nじゃあ、俺の携帯ナンバー。▽\n何言っていいか、\nわかるようになったら\n電話して。\n\0":
'???',

# Shigeru Aoba
"ひょっとしたら俺、\n笑わせる事くらい、\n出来るかもしれないから。▽\nじゃ…。\n\0":
'???',

# Maya Ibuki 
"青葉君…。\n\0":
'???',

#
# ./USRDIR/event/cev0809.har_EXTRACT/cev0809.evs
#
# [Text Only - No Designated Speaker]
"いつになったら、\n安らぎは得られるんだろう。▽\nいつになったら、\n誰かが助けてくれるんだろう。\n\0":
'???',

# Maya Ibuki 
"苦しい、苦しいよぉ…。\nお母さん…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"空っぽの私を見てもらっても、\nちっとも嬉しくない。▽\n本当の私は、\nここで泣いているのに。\n苦しくて叫び続けているのに。\n\0":
'???',

#
# ./USRDIR/event/cev0810.har_EXTRACT/cev0810.evs
#
# [Text Only - No Designated Speaker]
"何だかわからない。\nわけも無く電話をかけて、\nわけも無く来てしまった。▽\nどうすればいいのか、\nわからないけど…。▽\n助けてもらえるなんて、\n思わないけど…。▽\n私は、すがるように来てしまった。▽\nみっともなく…。\n\0":
'???',

# Shigeru Aoba
"マヤちゃん。\nよかった、来てくれた。\n\0":
'Maya-chan.\nI\'m glad you\'re here.\n\0',

# Maya Ibuki 
"………ごめんね。\n\0":
'......I\'m sorry.\n\0',

# Shigeru Aoba
"いいんだ。\nさ、行こう。\n\0":
'It\'s okay.\nShall we go?\n\0',

# Maya Ibuki 
"どこに？\n\0":
'Where?\n\0',

# Shigeru Aoba
"何か食いに。\n元気ない時は、\n何か食うのが一番だよ。\n\0":
'???',

# Shigeru Aoba
"よく、食べるねぇ。\n\0":
'???',

# Maya Ibuki 
"…そう、かな…。\n\0":
'???',

# Shigeru Aoba
"あ、今少し笑った。\nハハッ…。\n\0":
'Oh, you smiled a little.\n Hahah...\n\0',

# Maya Ibuki 
"ぁ…。\n\0":
'???',

# Shigeru Aoba
"別に、笑いたい時に\n笑えばいいんだよ。\n無理しなくてさ。▽\n俺もみんなも、\nそういうマヤちゃんが\n好きだから。\n\0":
'???',

# Maya Ibuki 
"そう…なの？\nでも、私…冗談とかあんまり\nわからないし。▽\nカタブツだって、青葉君も\n言ってたじゃない。\n\0":
'???',

# Shigeru Aoba
"そういう所もあるよね。\nでも、それがマヤちゃんの\n全てじゃないじゃん。\n\0":
'???',

# Maya Ibuki 
"…がうの。▽\n違うの。\n私には何もないの。\n\0":
'???',

# Shigeru Aoba
"そんな事ないよ。▽\nオペレーターとしても\n優秀だし、赤木博士にも\n信用されてるし。\n\0":
'???',

# Maya Ibuki 
"それだけなの、私には。\n仕事から離れたら、\n私には何もないの。\n\0":
'???',

# Shigeru Aoba
"俺、今こうして一緒にメシ\n食ってんの、楽しいけど。\nマヤちゃんと。▽\nヤなヤツとか、どうでもいい\nヤツには電話番号も教えないよ。▽\nマヤちゃんは、自分自身の魅力を\n知らないだけさ。▽\n人って、自分が可愛いって\n少しずうずうしい方がいいんだよ。\n度が過ぎるとアレだけどね。\n\0":
'???',

# Maya Ibuki 
"自分自身の魅力？\n\0":
'???',

# Shigeru Aoba
"何もないと思うなら、\nそこから始めたらいいさ。▽\n自分の事を可愛がれないと、\n人を好きになれない。▽\nもっとさ、積極的に人と話すとか\n話題を増やすとか\n人とぶつかってみたら？\n\0":
'???',

# Maya Ibuki 
"出来るかな？\n\0":
'???',

# Shigeru Aoba
"誰かを好きになると、\n変われるよ。\nいや、変わるね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"青葉君はずっと笑っていた。\n楽しそうだった。▽\n青葉君の世界にも、嫌なものが\nあるかもしれないけれど、▽\nそんなに悪いものばかりじゃ\nないのかとも…思った。\n\0":
'???',

# [Text Only - No Designated Speaker]
"家に着いて、お腹に手を当てた。▽\n青葉君が焼いてくれたお好み焼きで\n私のお腹は少し膨れていた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"今日は、\n吐きたいとは思わなかった。▽\n楽しかった事は全部、\nこのまま消化して、私の時間に\nなっていく気がした。\n\0":
'???',

# Maya Ibuki 
"好きになろう。\nもう一度。\n自分から。\n\0":
'???',

#
# ./USRDIR/event/cev0812.har_EXTRACT/cev0812.evs
#
# [Text Only - No Designated Speaker]
"ここしばらくのうちに\n知らない自分に、\nたくさん出会った様な気がする。▽\n自分はこういう事で笑うのだ、\n自分はこういう事で悲しむのだ。▽\n怒る自分、嬉しがる自分。\nどれも自分、伊吹マヤ。▽\nもっと早く気づいて\nあげればよかった。▽\n私は、寂しくて泣いている\n自分にしか気づけなかった。\n\0":
'???',

#
# ./USRDIR/event/cev0813.har_EXTRACT/cev0813.evs
#
# [Text Only - No Designated Speaker]
"あの時、\n青葉君が言ったあの言葉…。▽\n何となくわかる気がする。\n\0":
'???',

# [Text Only - No Designated Speaker]
"食べなくても気分がいい。\n何も食べなくても、\n心は大丈夫みたい。▽\n食べ物じゃなくても、\n心は埋めていける。▽\n私の心は、私の心で\n空っぽを埋め尽くす。\nそのうち、溢れ出るほどに。▽\n溢れ出た私の心が、\n色んな事を企てる。▽\n私は…、\n恋を知ったのかもしれない。\n\0":
'???',

# Maya Ibuki 
"青葉君。▽\n私…、変わったのかな。\n\0":
'???',

#
# ./USRDIR/event/cev0814.har_EXTRACT/cev0814.evs
#
# Shigeru Aoba
"よう、マヤちゃん。\n\0":
'???',

# Maya Ibuki 
"ねぇ…、私変わったかな？\n\0":
'???',

# Shigeru Aoba
"うんにゃ。\n\0":
'???',

# Maya Ibuki 
"……………………。▽\nそう…。\n\0":
'???',

# Shigeru Aoba
"マヤちゃんは、\nマヤちゃんだよ。▽\n変わったかどうかは\n自分で決める事さ。\n自分は、自分でしか変えれない。\n\0":
'???',

# Maya Ibuki 
"自分、で…？\n\0":
'???',

# Shigeru Aoba
"で、どう？\n自分は変わったと思う？\n\0":
'???',

# Shigeru Aoba
"そっか。\nじゃあ、変わったんだ。\n\0":
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
# ./USRDIR/event/cev0817.har_EXTRACT/cev0817.evs
#
# [Text Only - No Designated Speaker]
"どうしよう。\n約束しちゃった。\nどうしよう…。▽\nでも、変わるんだ。\n私は、もっと変われるの。\n\0":
'???',

# Maya Ibuki 
"明日、出会えるんだもん。\nまだ知らない自分自身に。\nもっともっと、これからもずっと。\n\0":
'???',

# Shigeru Aoba
"待った？\n\0":
'???',

# Maya Ibuki 
"ううん。\n今、来たばっかり。\n\0":
'???',

# Shigeru Aoba
"俺、車で来たんだ。\nドライブでも行く？\n\0":
'???',

# Maya Ibuki 
"…デートみたいね。\n\0":
'???',

# Shigeru Aoba
"デートだろ？\n\0":
'???',

# Shigeru Aoba
"ハハハッ…。▽\nさ、行こう。\n\0":
'???',

# Maya Ibuki, Shinji Ikari
"うん。\n\0":
'???',

# Maya Ibuki 
"あのね、青葉君。\nありがとう。\n\0":
'???',

# Shigeru Aoba
"えー、何で？\n\0":
'???',

# Maya Ibuki 
"だって、\n変わるきっかけをくれたの\n青葉君なんだもん。\n\0":
'???',

# Shigeru Aoba
"そぉ？\n\0":
'???',

# Maya Ibuki 
"青葉君が、言ったでしょ？\n誰かを好きになると変わるって。▽\n私、変われたよ…、\n青葉君のおかげで。\n\0":
'???',

# Shigeru Aoba
"えー、何か今の\n聞こえなかった。\n\0":
'???',

# Maya Ibuki 
"…ううん、いいの。\n何でもない！▽\n…何でもないの。\n\0":
'???',

# Shigeru Aoba
"あ、ひとつ言おうと思ってた。\nこの間、俺に自分が変わったか\nとか聞いてただろ？\n\0":
'???',

# Shigeru Aoba
"かわいくなった。\n\0":
'???',

# Shigeru Aoba
"前よりずっと、かわいくなった。\nちゃーんと、変わったって\n言ってんの。\n\0":
'???',

# Maya Ibuki 
"…………………！！\n\0":
'???',

# Shigeru Aoba
"ほら、トンネル。\nあの先はもう海だ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"言葉は要らなかった。▽\n二人で、笑って声をあげた。▽\nトンネルの先に光が見える。▽\n新しくも知らない自分に出会った\n「私達」を祝福する様に、\n光が近づいてくる。\n\0":
'???',

# [Text Only - No Designated Speaker]
"海の匂いがする。▽\n眩しかった。\n\0":
'???',

#
# ./USRDIR/event/cev0901.har_EXTRACT/cev0901.evs
#
# [Text Only - No Designated Speaker]
"好きになっては\nいけない人だった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女の心には、\nすでに一人の男がいたからだ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そんな彼女の隙を、\n僕は一度だけ、\n見た事があった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"いつも気丈なその人は…、\nこんな顔をするものなのかと\n僕を驚かせ、ひどく惹きつけた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女は…その心の隙間を\nまざまざ僕に見せ付けて、\n何もないままその時は終わった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕に勇気がなかっただけだ。\n\0":
'???',

#
# ./USRDIR/event/cev0902.har_EXTRACT/cev0902.evs
#
# Makoto Hyuga
"ご存知でしたか？\n\0":
'???',

# Misato Katsuragi 
"いえ、ありがとう。\nいつも、悪いわね。\n\0":
'???',

# Makoto Hyuga
"僕も事実を知りたいんで。\n葛城さんの力になっているなら\n僕も嬉しいんですけどね。\n\0":
'???',

# Makoto Hyuga
"まだ、情報は得られそうです。\n感触、ありそうなんですよね。\n探ってみましょうか？\n\0":
'???',

# Misato Katsuragi 
"そうね…、お願いするわ。\n\0":
'???',

# Misato Katsuragi 
"あら、電話。\n\0":
'???',

# Makoto Hyuga
"加持さんですか？\n\0":
'???',

# Misato Katsuragi 
"じゃあ、またね。\n日向君。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女と特別な関係になるのは\nこの時だけだ。▽\n彼女は、ネルフに隠された\n真実を追っている。▽\n僕は、その彼女の手伝いを\nやっているだけだが。\n無論、二人だけの秘密だ。▽\n情報を集めるのは、\n決して安全とはいえない。▽\n彼女と会う口実が、\n僕にとっての報酬になる。\n\0":
'???',

# [Text Only - No Designated Speaker]
"口実を必要とせずに、彼のように\nああやって電話をかけられるのは、\n僕には雲の上みたいな話だ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕は、彼女が喜ぶ顔が見れたら\nそれでいい…。\n\0":
'???',

# Makoto Hyuga
"さて、と…。\n情報を集めないとな…。\n\0":
'???',

#
# ./USRDIR/event/cev0903.har_EXTRACT/cev0903.evs
#
# Misato Katsuragi 
"ありがとう。\n今回チョッチ、\nヤバかったんじゃない？\n\0":
'???',

# Makoto Hyuga
"まあ、毎回そうですよ。\n\0":
'???',

# Misato Katsuragi 
"ごめんなさいね…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"葛城調査隊…、\n彼女の父親についての情報を\n話すのは心苦しかった。▽\n彼女の過去を無断で覗いたような\nそんな後ろめたさがあった。▽\n彼女は強く、そして寂しい人だと\n勝手な推測をしてしまう自分に\nふと、気づかされる。▽\n彼女は戦っている。\n戦いながら生きている。▽\n少なくとも、\n僕の前では隙を見せない。▽\nあの時…、隙を見せたあの時の\n彼女の気持ちは、\nどんなものだったのだろう。\n\0":
'???',

# Misato Katsuragi 
"ねえ、日向君…。\n私、父の敵を討ちたいの。\n\0":
'???',

# Makoto Hyuga
"仇…ですか？\n\0":
'???',

# Misato Katsuragi 
"そう。▽\n私は、人類を守る為じゃなく、\n父を殺した使徒を倒す為に\nネルフに入ったんだわ。▽\n自分で…気づかなかったけど、\nやっぱり、そう思っていたのよ。\n\0":
'???',

# Misato Katsuragi 
"軽蔑する…？\n\0":
'???',

# Makoto Hyuga
"…いえ。\nあなたは優秀な上司です。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女なら…、部下に\n…こんな事は話さないだろう。▽\nこの立場にいながら、\n私情を持ち込むなど絶対に\n知られてはならない事だ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"優秀な上司。▽\n僕は嘘を言った。▽\nもちろん、彼女は優秀な上司だ。▽\nただ、勇気がなくて\n僕はその言葉を使ってしまった。▽\n本当はすぐにでも、\n抱きしめるべきだったのかも\nしれない。\n\0":
'???',

# Makoto Hyuga
"あのっ…。▽\n…………………………………………\n…………………………………………\n…………………………………………。\n\0":
'???',

# Misato Katsuragi 
"ごめんなさいね。\nこんな事、言うんじゃなかった。\n\0":
'???',

# Makoto Hyuga
"………………………。▽\nいいんですよ、僕は。▽\n必…要、としてくれるのなら。▽\nあなたは、抱えすぎですよ。\n何もかもを…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"その震える肩に手を置こうか、\n迷うほんのわずかな時間が\nとても長く感じた。▽\n彼…、加持さんならば、\n難なく彼女を受け止めて\nいただろうに。▽\n僕ときたら、ただこうやって\n彼女の声を聞くばかりだ。\n\0":
'???',

# Misato Katsuragi 
"あなたにまで甘えて…私。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女は…自分を恥じている。\n僕はその思いを受け止めるべきだと\n思った。\n\0":
'???',

# Makoto Hyuga
"葛城さん…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"利口ぶったやり方だったのか、\nそんな事までは頭が回らなかった。▽\n僕は彼女を車で連れ出して、\n後はただ、お互いズルくて\n甘ったるい時間を過ごした。\n\0":
'???',

# Makoto Hyuga
"…何か、僕。\n…すみませんでした。\n\0":
'???',

# Misato Katsuragi 
"謝らないで。▽\nたかだかこんな事で、\nあなたが悪いと思う事、ないわよ。▽\n私こそ…ごめんね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女は眠そうに笑っていた。▽\n窓の外の、朝焼け。\n高く、曖昧な表情の空色は\n彼女みたいだと、ふと思った。\n\0":
'???',

# [Text Only - No Designated Speaker]
"それから僕達は、\nもう触れ合う事無く\nいつもの顔に戻った。\n\0":
'???',

#
# ./USRDIR/event/cev0904.har_EXTRACT/cev0904.evs
#
# [Text Only - No Designated Speaker]
"少し、気まずい思いだった。\n何もなかったような振りをして、\n彼女の顔色をうかがった。▽\n自分のずるさ。▽\n僕は…彼女の隙を探している。\n\0":
'???',

#
# ./USRDIR/event/cev0905.har_EXTRACT/cev0905.evs
#
# [Text Only - No Designated Speaker]
"葛城さんとの出来事を知ったら、\nシンジ君は僕をどう思うだろうか。▽\nそんな事を考えながら、\n僕はすました顔で\nやり過ごしていた。\n\0":
'???',

#
# ./USRDIR/event/cev0906.har_EXTRACT/cev0906.evs
#
# [Text Only - No Designated Speaker]
"葛城さんとの出来事を知ったら、\nアスカは僕をどう思うだろうか。▽\nそんな事を考えながら、\n僕はすました顔で\nやり過ごしていた。\n\0":
'???',

#
# ./USRDIR/event/cev0907.har_EXTRACT/cev0907.evs
#
# [Text Only - No Designated Speaker]
"あれから、何度か彼女が\n僕に隙を見せた。▽\n遊びのように\nじゃれつく事もあった。▽\nそして、何事もなかったように\n上司と部下に戻るのだ。▽\nお互い、真意は語らず、\nズルくて甘い時間に\n流されるままだった。▽\n彼女は戦っている。\n僕は、全てを持って彼女を\n支えていられればいい。▽\n始めはそうだったが、\n僕の衝動は膨らむばかりだった。▽\n夜中に目を覚まし、彼女を思う。\n何もためらわずに、この腕の中に\n彼女を抱きしめられるのなら…。▽\nそして、彼女を支えるという\n言い訳を利用している自分に\n気づかされるのだった。\n\0":
'???',

# Makoto Hyuga
"変わってない。\n僕は、口実ばかりを求めている。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女の心の中に、\n僕はいるのだろうか。\n\0":
'???',

#
# ./USRDIR/event/cev0908.har_EXTRACT/cev0908.evs
#
# [Text Only - No Designated Speaker]
"いかにもそれらしい理由を\nつけられて、彼女の死は\n皆に知らされた。▽\n僕にはわかっていた。\n知り過ぎた報いで、\n彼女は消されたのだと。▽\n僕には…何も出来なかった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"宅配が届いていた。\n実家からだ。▽\nダンボールの封を剥がし、\n隙間に指を入れる。▽\n封を指で裂きながら、\nこんな風に、\n僕は彼女の隙に押し入り、▽\n彼女を腕の中に抱いた時を\n思い出した。▽\n中には衣類と、適当に食料が\n入っていた。▽\nそして、隠れるように\n手紙が一枚入っていた。\n\0":
'???',

# Makoto Hyuga
"…この字は？\n\0":
'???',

# [Text Only - No Designated Speaker]
"間違いなかった。\n彼女の手紙だ。▽\nこの荷物は、\n彼女によって工作されたものだった。\n\0":
'???',

# Misato Katsuragi 
"日向君へ▽\nありがとう。\nあの時、一人の女でいさせてくれて。\n\0":
'???',

# Misato Katsuragi 
"ひょっとしたら、\nこれを読んでいる時にはもう\n会えなくなってるかも知れない。▽\nだから、一言。\nあなたに、ありがとう。▽\nいい恋をしてね。\n私みたいな女に\nつかまっちゃダメよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女は、\n本当に手の届かないところへ\n行ってしまった…。\n\0":
'???',

#
# ./USRDIR/event/cev0911.har_EXTRACT/cev0911.evs
#
# [Text Only - No Designated Speaker]
"しばらくの沈黙の後、\n僕は彼女を抱きしめた。▽\n抵抗はなかった。▽\nきっと、曖昧なまま\nまた時間は過ぎるのだろう。▽\n彼女は、僕の腕の中にいる。▽\n僕はもう、口実を必要としない。\n僕らは曖昧なまま、\nずっと続いていくのだ。▽\nずっと…。\n\0":
'???',

# Misato Katsuragi 
"ゴメン、待った…。\n\0":
'???',

# Misato Katsuragi 
"いつも悪いわね。\n今日はどんな情報かしら…。\n\0":
'???',

# Makoto Hyuga
"もう、止めてください。\n\0":
'???',

# Makoto Hyuga
"もう、こんな情報を\n集めたりするのは…。\n止めてください。\n\0":
'???',

# Misato Katsuragi 
"日向君…。▽\nごめん、私も今まで\n無理をさせたみたいね。▽\nあなたまで、\nこんな危険な事に巻き込んで…。▽\nあなたに頼むのは、\nもうこれっきりに…。\n\0":
'???',

# Makoto Hyuga
"僕は、葛城さんに…！\nこういう事を\n止めてもらいたいんです。▽\nこれ以上は危険ですよ、\nこんな…。\n\0":
'???',

# Misato Katsuragi 
"承知の上よ。\n\0":
'???',

# Makoto Hyuga
"僕は、あなたを失いたくない。\nあなたを失えば、\n僕はきっと後悔する。\n\0":
'???',

# [Text Only - No Designated Speaker]
"隙なんて微塵もない、\nいつもの戦う彼女の顔。\n\0":
'???',

# Misato Katsuragi 
"自分勝手ね。\nそれは、私も同じか…。\n\0":
'???',

# Makoto Hyuga
"あなたに会う口実だと思って、\n今まで協力してきました。▽\nでも、僕の口実の為に\nあなたがいなくなったりしたら。\nいなくなったりしたら、僕は…。\n\0":
'???',

# Misato Katsuragi 
"日向君…。\n\0":
'???',

# Makoto Hyuga
"そんな口実とか無しに、\n僕はあなたの傍にいたくて…。\nあなたを支えて…。▽\n………………………。\n\0":
'???',

#
# ./USRDIR/event/cev1001.har_EXTRACT/cev1001.evs
#
# Shigeru Aoba
"やっぱりあの道を選んでいたら、\n俺は今頃どうしていただろうか。\n時々ふと思う事がある。▽\nあの道…、というのは\nミュージシャンになるはずだった道。▽\n大学時代にやっていたバンドが、\n卒業と同時にプロデビュー\nする事になった。▽\nだが、俺はならなかった。\nなれなかったと言った方が\nいいかも知れない。\n\0":
'???',

# Maya Ibuki 
"おはよう、青葉君。\nまた、ギター持ってる。\n\0":
'???',

# Shigeru Aoba
"だって、これ俺の恋人だぜ。\n置いてく訳にはいかねーだろ。\n\0":
'???',

# Maya Ibuki 
"はいはい。\nもう、何言ってるんだか。\nちゃんと仕事もしてくださいよ。▽\n最近、私用メールとか\n多いみたいですし。▽\nその恋人ばかり相手にしてる\nようですしー。\n\0":
'???',

# Shigeru Aoba
"さってと、今日も仕事だ仕事。\n\0":
'???',

# Maya Ibuki 
"もうちょっと、仕事に誇りを持って\nくださいよ。▽\n青葉君のその席が欲しくても、\n得られなかった人って\n沢山いたんだから。\n\0":
'???',

# Teruo Kato
"あー、お前の代わりの\nギタリストと会わされた。\nで、これでユニット組んでくれって。▽\nユニット名も勝手に変えられてさ、\n「コバルトスカイ」だってよ。\nダッサイの！！▽\n………。▽\nシゲル…さ、\n一緒にやれると思ってたのに、\n本当にいいのかよ？▽\nギターで、食っていくって\nいっつも言ってただろ。▽\nプロデビューのチャンスなんだぜ。\n\0":
'???',

# Shigeru Aoba
"なーんかね、なんつーか…。▽\nま、いいや。\n仕事、仕事。\n\0":
'???',

# Maya Ibuki 
"一番優秀だったから、\nその席にいられるんですよ。\n\0":
'???',

# Shigeru Aoba
"１２１６分の１の合格率、だろ？\n別に俺、この立場に胡座かいてる\nわけじゃねぇよ。▽\nただ、思うんだよなー。\nホントに俺がこんな役職で\nよかったのかなーって。▽\nむしろ、もったいないというか。\n\0":
'???',

# Shigeru Aoba
"マヤちゃんは、\n肩に力入りすぎだっつーの。\n\0":
'???',

#
# ./USRDIR/event/cev1003.har_EXTRACT/cev1003.evs
#
# Street T.V.
"ホントね、ミュージシャンって\n幸せですよ。\n世界は大変な事になってますけど。▽\nまあ、ボクらは歌作って\n世界のヘイワの為に戦うっスよ。\n\0":
'???',

# Shigeru Aoba
"…ふーん。\n売れてんじゃん、テルオ。\n\0":
'???',

# Street T.V.
"で、いよいよ今日ですよ。\nええ、新曲発売。▽\nもう聴いていただけましたか？\nボクの自信作。▽\nこの新曲と共に、沖縄から\n北海道まで全国ツアーですよ。\n嵐吹き起こしますよ、もう！\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、街頭テレビに目が行った。▽\nテレビに映っていたのは、\n学生時代のバンド仲間のユニット\n「コバルトスカイ」だった。▽\n喋っているのは、\n自分の代わりに事務所が用意した、\nギタリスト…。\n\0":
'???',

# Shigeru Aoba
"使徒さえ来なきゃ、\n街も賑やかなもんだな…。\n\0":
'???',

#
# ./USRDIR/event/cev1004.har_EXTRACT/cev1004.evs
#
# Shigeru Aoba
"あ？\n仕事はちゃんとやってるよ。\n\0":
'???',

# Maya Ibuki 
"ううん、違う違う。\n今弾いてた曲、\nコバルトスカイの新曲でしょ？\n\0":
'???',

# Shigeru Aoba
"んなわきゃないだろ？\n俺、邦楽聞かねーもん。\n\0":
'???',

# Maya Ibuki 
"えぇ？\n違うんだ。\n\0":
'???',

# Maya Ibuki 
"私、ＣＤ買ったのよ。\nコバルトスカイの新曲。\nあの曲だと思ったんだけどなぁ。\n\0":
'???',

# Shigeru Aoba
"…ミーハーだなー、\nマヤちゃんは。\n\0":
'???',

# Maya Ibuki 
"あのギタリストのカズキって、\nカッコイイし。▽\n今度の新曲とかも、\n手がけてるんだって。\n\0":
'???',

#
# ./USRDIR/event/cev1005.har_EXTRACT/cev1005.evs
#
# Shigeru Aoba
"今、何時だ？\nテレビでも観るか…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ぼんやりとテレビを眺めていると、\nコバルトスカイの新曲が\n流れてきた。▽\nよく知っている。\n終わりから初めまで。\n歌詞さえも。\n\0":
'???',

# Shigeru Aoba
"は…？\n新曲ってコレかよ。▽\n俺が学生時代に作った\n曲じゃねぇか！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"呆気にとられていると、\nあのギタリストが顔を出した。\n\0":
'???',

# Host [for Aoba's scenario]
"コバルトスカイの皆さん、\n演奏お疲れ様でした。\nいい歌でしたねー。\n\0":
'???',

# Kazuki Anami [for Aoba's scenario]
"でっしょ〜。\nミリオンヒット狙いますよ。\n\0":
'???',

# Host [for Aoba's scenario]
"今回、この曲を手がけられたのは\nこちらギターのカズキさんですか？\n\0":
'???',

# Kazuki Anami [for Aoba's scenario]
"ええ。\n自分の中でずっと温めてたもので。▽\n難産でしたけど、ようやく皆様に\nお聞かせする事が出来て、ホント\nメンバー全員ハッピーです、イェイ。▽\nな、テルオ。\n\0":
'???',

# Teruo Kato
"…あの曲は……………。\nあのー…、そうですね…。\n\0":
'???',

# Host [for Aoba's scenario]
"ベースのテルオさん、\n緊張してらっしゃいますねー？\n\0":
'???',

# Teruo Kato
"……………………いえ。\n急に売れ出したんで\nちょっと緊張して…。\n\0":
'???',

# Kazuki Anami [for Aoba's scenario]
"あ、まあまあ、ボクが\nトーク担当ですから。\n\0":
'???',

# Shigeru Aoba
"…パクリじゃねーか。\n\0":
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
# ./USRDIR/event/cev1007.har_EXTRACT/cev1007.evs
#
# Maya Ibuki 
"ほらー、見てくださいよ。\nコバルトスカイのライブチケット\n手に入れたんですよ！！\n\0":
'???',

# Shigeru Aoba
"ふーん。\n\0":
'???',

# Maya Ibuki 
"ツアー最終日。\n第２新東京市で野外ライブですって。\n\0":
'???',

# Shigeru Aoba
"マヤちゃん。\n今の仕事、楽しい？\n\0":
'???',

# Maya Ibuki 
"何、おかしな事聞くんですか？▽\n責任重いし、キツい事が多いけれど\nやりがいがあって…。\n私にはコレしかないと思ってます。\n\0":
'???',

# Shigeru Aoba
"そっか、よかったじゃん。\n\0":
'???',

# Maya Ibuki 
"青葉君は？\n\0":
'???',

# Shigeru Aoba
"楽しいわけじゃないけど。\n給料いいし。\nまあ、悪くはないかな。\n\0":
'???',

# Maya Ibuki 
"そういうのって、\n頑張ってる他のスタッフに対して\n失礼だと思いますけど。\n\0":
'???',

# Shigeru Aoba
"んー、そうね。\n\0":
'???',

# Maya Ibuki 
"最近、変ですよ…。\n\0":
'???',

#
# ./USRDIR/event/cev1008.har_EXTRACT/cev1008.evs
#
# Teruo Kato
"…シゲル？\nシゲルだろっ！？\n\0":
'???',

# Shigeru Aoba
"テルオ…。\n\0":
'???',

# Teruo Kato
"あは…、元気そうじゃないか。\n\0":
'???',

# Shigeru Aoba
"久しぶり。\n新曲、売れてんじゃん。\n\0":
'???',

# Teruo Kato
"あ………。\nアレ…、だろ…？\nシゲルが学生時代に作った曲…。▽\nやっぱ、怒ってるのか…？\n\0":
'???',

# Shigeru Aoba
"いや…、あの業界じゃ\nよくある話なんだろ。\n\0":
'???',

# Teruo Kato
"ん…、曲、書けなくて。\nお前が作った曲を弾いてたら、\n事務所がコレは売れるって。▽\nでも、事務所から組まされた\nギターの奴がウリになってるから\nアイツが作曲した事にされて…。\n\0":
'???',

# Shigeru Aoba
"でも、夢叶って\n良かったじゃないか。▽\n憧れのミュージシャンにさ。\nしかも、今や売れっ子だしな。\n\0":
'???',

# Teruo Kato
"…ごめん。\nシゲル、本当に済まなかった。\nあれは、お前の曲なのに…。\n\0":
'???',

# Shigeru Aoba
"いいよ、もう。\nそれより、今度飲もうぜ。\n携帯番号教えとくからさ。\n\0":
'???',

# Teruo Kato
"…シゲル。\nあぁ、そうだな。\n\0":
'???',

# Shigeru Aoba
"当分休みもらえそうに\nないけど。\nま、時間作るようにするから。\n\0":
'???',

#
# ./USRDIR/event/cev1009.har_EXTRACT/cev1009.evs
#
# Shigeru Aoba
"あの時…、\nもう一度、音楽をやりたいと\n思った…。▽\n…でも。\n\0":
'???',

# Shigeru Aoba
"結局、諦めた。\n自分から逃げ出したんだ。▽\n俺は、今ここにいる。\nギタリストじゃなく、\n特務機関ネルフの人間として。\n\0":
'???',

#
# ./USRDIR/event/cev1010.har_EXTRACT/cev1010.evs
#
# Shigeru Aoba
"はい。\nあぁ、テルオか？\n\0":
'???',

# Teruo Kato
"シゲル…、お前…。▽\nギターやらない？\n\0":
'???',

# Shigeru Aoba
"はぁッ！？\n\0":
'???',

# Teruo Kato
"ツアー移動中に、非常警戒が出て。\nシェルターに避難したけど、\nそこで事故がおきて…。▽\nギタリストが入院して\nしまったんだ。\n\0":
'???',

# Shigeru Aoba
"でも、俺は…。\nまるっきり部外者だぜ。\n\0":
'???',

# Teruo Kato
"お前しか出来ない。\n頼む！！▽\n第２新東京市でのライブ、\n出てくれよ。▽\nお前の腕見りゃ、事務所も\n納得してくれる。\n\0":
'???',

# Shigeru Aoba
"バカ、冷静になれよ。\n\0":
'???',

# Teruo Kato
"ライブ当日、\nお前が来るの…待ってるから。\n\0":
'???',

#
# ./USRDIR/event/cev1011.har_EXTRACT/cev1011.evs
#
# Kozo Fuyutsuki
"何だね？\n\0":
'???',

# Shigeru Aoba
"実は…、\n有休を頂きたいんですけど。\n\0":
'???',

# Kozo Fuyutsuki
"わかった。\n休暇届の書類は、\n総務課にでも回しておきたまえ。\n\0":
'???',

# Kozo Fuyutsuki
"君の最近の仕事振りでは、\n認めるわけにはいかんな。▽\nもっとも、その分取替えして\nくれるというのなら別だがね。\n\0":
'???',

#
# ./USRDIR/event/cev1012.har_EXTRACT/cev1012.evs
#
# Kozo Fuyutsuki
"君か。\nどうやら仕事の方は頑張って\nくれたようだな。▽\n有休は認めよう。\n休暇届の書類は、\n総務課にでも回しておきたまえ。\n\0":
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
# ./USRDIR/event/cev1101.har_EXTRACT/cev1101.evs
#
# Ryoji Kaji
"俺は、セカンドインパクトを\n故意に引き起こした連中と、\nそれらにまつわる真実を追っている。▽\n古より世界を動かしていると\n言われる権力者の集団、ゼーレ。▽\nそして、ゼーレと密接な繋がりを\n持つ、ネルフ総司令、碇ゲンドウ。▽\n全ての真実に手を伸ばすために、\n俺は奴等に近づく事になった…。\n\0":
'???',

# Female Staff
"では、これがここの\nＩＤカードになります。\n\0":
'???',

# Ryoji Kaji
"しかしまるで迷路だな。\nこりゃ、慣れるまでに\nしばらくかかりそうだよ。\n\0":
'???',

# Female Staff
"それじゃ、私は失礼します。\n\0":
'???',

# Ryoji Kaji
"ああ、案内ありがとう。\nこれはお礼のチップ。\n\0":
'???',

# Female Staff
"あら、要りませんよ。\n\0":
'???',

# Ryoji Kaji
"じゃあ、お礼のキスは…？\n\0":
'How about a thank-you kiss...?\n\0',

# Misato Katsuragi 
"お久しぶりねぇ。\n用なら私が伺うわ。\n\0":
'???',

# Ryoji Kaji
"おっほぉ、そんなに\n怖い顔するなって…。▽\nひっさしぶりだなぁ、\nまた一段と綺麗に\nなったじゃないか。\n\0":
'???',

# Misato Katsuragi 
"その軽〜いところ、相変わらずね。\nで、ここへは何をしに？\n\0":
'???',

# Ryoji Kaji
"碇司令から、こっちに\n出向の辞令が出てね。▽\nこっちの特殊監査部に\n配属されたのさ。▽\nま、仲良くしようや、\n昔みたいにね。\n\0":
'???',

# Misato Katsuragi 
"馬鹿！\n触んないでよ！！\n\0":
'???',

# Ryoji Kaji
"そんじゃ、碇司令に挨拶してくるわ。▽\n落ち着いたら、酒でも付き合えよ！\n\0":
'???',

# Misato Katsuragi 
"………バカ。\n\0":
'???',

# Ryoji Kaji
"加持です。\nただ今、到着いたしました。\n\0":
'???',

# Gendo Ikari
"よく来たな。\n\0":
'???',

# Kozo Fuyutsuki
"長旅の後なのに、すまないな。\n\0":
'???',

# Ryoji Kaji
"お久しぶりです、\n例の品をお届けに上がりました。\n\0":
'???',

# Kozo Fuyutsuki
"これがあのアダム…。\n\0":
'This is -the- Adam...\n\0',

# Ryoji Kaji
"ええ、最初の人間アダムですよ。\nすでにここまで復元されています。▽\n硬化ベークライトで固めて\nありますが、生きています。\n間違いなく。\n\0":
'Yes, it\'s Adam, the first human.\nIt\'s already been restored this far.▽\nIt\'s frozen in cured Bakelite, but it\'s still alive.\nNo doubt about that.\n\0',

# Gendo Ikari
"人類補完計画の要か…。\n\0":
'So the Human Instrumentality Project hinges upon this...\n\0',

#
# ./USRDIR/event/cev1102.har_EXTRACT/cev1102.evs
#
# Ryoji Kaji
"必要なのは特殊偽造ＩＤ…。\nこれは自前で作成するか。▽\nあとは副司令や碇司令が持つ\nＩＤをどう入手するかだな。▽\n必要な情報は、\nここで全て手に入るだろう。▽\n真実はネルフにあるはずだ…。\n\0":
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
# ./USRDIR/event/cev1104.har_EXTRACT/cev1104.evs
#
# Ryoji Kaji
"じゃあ、君は強くなったんだな。\n安心したよ。\n\0":
'???',

# Ritsuko Akagi 
"死ぬ気？\n\0":
'???',

# Ryoji Kaji
"…ハハッ。\n\0":
'???',

# Ritsuko Akagi 
"全てを知って、\nそれからどうするの？▽\nあなたが何を考えているのか\nわからないけど、これ以上の\n詮索は止めた方がいいわよ。\n\0":
'???',

# Ryoji Kaji
"そりゃ、どうも。\n\0":
'???',

# Ritsuko Akagi 
"何でもお見通しなのよ、上は。\nもしあなたがいなくなれば、\n悲しむ人がいるでしょうしね。\n\0":
'???',

# Ryoji Kaji
"俺が死んだら、\n泣いてくれるのかい？\n\0":
'???',

# Ritsuko Akagi 
"どうかしら。\nそれだけの付き合いだったもの。▽\n傷をなめあっただけでしょ。\n私達。\n\0":
'???',

#
# ./USRDIR/event/cev1105.har_EXTRACT/cev1105.evs
#
# Misato Katsuragi 
"あなたの本当の目的は何？\n\0":
'???',

# Ryoji Kaji
"君さ。\n\0":
'???',

# Misato Katsuragi 
"ごまかさないで。\n何をしようとしてるの？\n\0":
'???',

# Ryoji Kaji
"１０年先も君が\n笑っていられるようにさ。\n\0":
'???',

# Misato Katsuragi 
"いつも本心は言わないのね。\n\0":
'???',

# Ryoji Kaji
"だから、\n愛想つかされるんだろうな。\n\0":
'???',

# Misato Katsuragi 
"別れてほしかったんでしょ。\nだから、切り出しただけよ。\n私から。▽\n今回もそう。\n私を遠ざけている。▽\nどうしていつも、本当の事を\n言ってくれないの…？\n\0":
'???',

# Ryoji Kaji
"済まないな、いつも。\nその胸の中でずっと安らいで\nいたいが、俺は進まないといけない。\n\0":
'???',

# Misato Katsuragi 
"どこへ行く気？\n\0":
'Where do you plan to go?\n\0',

# Ryoji Kaji
"全てが終わったら、\n戻ってくるよ。▽\nその時は、\n俺を受け入れてくれるか？\n\0":
'???',

# Ryoji Kaji
"ウソさ。\n忘れてくれ、今のは。\n\0":
'???',

#
# ./USRDIR/event/cev1106.har_EXTRACT/cev1106.evs
#
# [Text Only - No Designated Speaker]
"二人は続かなかった。\n多分、それでよかったのだ。▽\n俺も、彼女も、\nそれぞれの道を歩んだ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"セカンドインパクトが起きた\nあの日…。▽\n今でも、何も知らなかった\nあの頃の夢を見る。▽\nあの脅威を前に成す術もなく、\n死ぬのを待つしかなかった人々。▽\n俺は家族を失い、\nあの混乱の時代を生き延びた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"世界が落ち着きを\n取り戻した頃…。▽\nセカンドインパクトが、何者かの\n陰謀によって故意に引き起こされた\nものだと説を唱える者が現れ始めた。▽\n誰が、何の為に。▽\n荒唐無稽な話だと思ったが、\nもし本当に故意に引き起こされたり\nしたものならばと…。▽\n俺は、全てを失う事になった原因を\n自分自身で確かめたくなった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そしてここ、ネルフ…。\n真実は、必ずここにある。▽\nセカンドインパクトが\n引き起こされたその真意を、\n俺は確かめなければならない。\n\0":
'???',

# Ryoji Kaji
"奴らは…、何を狙っている…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そんな中、出会ったのが\n葛城だった。▽\n俺達はすぐに恋に落ち、\n愛し合い、お互い過去の傷を\n癒しあった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"彼女はセカンドインパクトを\n間近で見た、\nただ一人の人間だった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ネルフ特殊監査部、\n日本政府内務省、\nそして、ゼーレ。▽\n俺は、全てを欺きながら\nこの３つ組織に潜り込んでいる。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そして、俺は知った。▽\nあの惨事が、人の手によって\n引き起こされた事を。\n\0":
'???',

#
# ./USRDIR/event/cev1107.har_EXTRACT/cev1107.evs
#
# Ryoji Kaji
"裏切ったり、裏切られたりも\nここまでだ。▽\n長かったな…。\n\0":
'???',

# Ryoji Kaji
"残された時間も少ない。\n帰る場所もない。▽\n発つとするか…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"頃合いだ。\n真実も手元に揃った。▽\n奴等のシナリオを覆すには\n急がなければならない。▽\nそれが、\n途方もない道であったとしても…。\n\0":
'???',

# Misato Katsuragi 
"待って！！\n\0":
'???',

# Ryoji Kaji
"…葛城！？\n\0":
'???',

# Misato Katsuragi 
"行くの…？\n\0":
'???',

# Ryoji Kaji
"じゃあな。\nそういう表情もイイが、\n君は笑ってろ…ずっとな。\n\0":
'???',

# Misato Katsuragi 
"私も行くわ。\n\0":
'???',

# Ryoji Kaji
"馬鹿言うな。\n\0":
'???',

# Misato Katsuragi 
"いつまで遠ざけるのよ。\n優しくして、また放っておいて。\nいつも、いつも。▽\n前もあなたは何も言わなかった。\nだから、あの時…\n別れを切り出したのよ。▽\n今度も…、あなたは何も\n言ってくれない。▽\nだから、私が言うわ。\nあなたに付いて行く。\n\0":
'???',

# Ryoji Kaji
"葛城…。\n\0":
'???',

# Misato Katsuragi 
"一人で、行ってしまわないでよ。\n\0":
'???',

# Ryoji Kaji
"君にはやるべき事がある。\nそれは君にしか出来ない事だ。\n本部のみんなを守ってくれ。\n\0":
'???',

# Misato Katsuragi 
"…加持君。\n\0":
'???',

# Ryoji Kaji
"待っていてくれ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"「待っていてくれ。」▽\n俺は、最後の最後に\n自分の甘さ、ずるさを\n彼女に押し付けた。▽\n許してくれ…、これが最後だよ。\n本当に最後だ、葛城…。▽\n次に会う時は、\n君を正面から受け止めよう。\n\0":
'???',

# Ryoji Kaji
"戦いは、これからだ。\n\0":
'???',

#
# ./USRDIR/event/cev1201.har_EXTRACT/cev1201.evs
#
# Toji Suzuhara 
"傷、だいぶいい感じやな。\nもう退院してもええくらいや。\n\0":
'???',

# Toji's Sister
"うん。\nちょっとお熱が出たりするけど。\nもう大丈夫や。\n\0":
'???',

# Toji Suzuhara 
"あと、ちょっとかぁ。\nスマンなぁ、もうちっと\nしっかり面倒見てやれたら…。\n\0":
'???',

# Toji's Sister
"ええねん。\n兄ちゃん、こないして来てくれる。\nそれだけでええねん。\n\0":
'???',

# Toji Suzuhara 
"スマンな…。\n\0":
'???',

# Toji's Sister
"ウチな…、\n顔の傷、このままなんやろ？\nこれ以上は治らへんて。\n\0":
'???',

# Toji Suzuhara 
"そんな事あるか…。\n\0":
'???',

# Toji's Sister
"すごくお金がかかるんやて。\nあと、ここの病院でも\nそこまでの治療は出来へんねんて。\n\0":
'???',

# Toji Suzuhara 
"そんな事あらへん！\nええか、お前の傷はワシが治したる。\n約束や…、兄ちゃん約束する！！\n\0":
'???',

# Toji's Sister
"ん…、おおきに。\n兄ちゃん…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"妹が重傷を負った。▽\nシンジの乗るエヴァが暴走して\n避難所は崩れ、瓦礫の下敷きに\nなって。▽\n始めは許せんかった。\n妹をあんな目に合わせたヤツを。▽\nせやけど、シンジがエヴァに\n乗って苦しんでる姿を見て…、\nワシも見方が変わった。▽\n許すも何も、あいつはワシら\n人類の存亡を賭けて戦ってる。▽\nワシらには到底無理な事を\nシンジはやってくれている。▽\nわかってる…、わかってるけど。▽\n妹に出来た傷は、完全に\n消えてしまわないらしい。\n\0":
'???',

# Toji Suzuhara 
"ああ言うてしもたけど、\nどないしたもんやろな…。\n\0":
'???',

#
# ./USRDIR/event/cev1202.har_EXTRACT/cev1202.evs
#
# Toji Suzuhara 
"どや、ご飯食べたか？\n\0":
'???',

# Toji Suzuhara 
"もうすぐ退院やな。\nはよ、退院して\n外出なアカンな。\n\0":
'???',

# Toji's Sister
"………。▽\n嫌や。\n\0":
'???',

# Toji Suzuhara 
"何でぇな。▽\nあ、そや。\n退院したら、兄ちゃんが\n遊園地連れてったるさかい。\n\0":
'???',

# Toji's Sister
"いい…。\n\0":
'???',

# Toji Suzuhara 
"ほな、水族館がええかな。\n\0":
'???',

# Toji's Sister
"お外、行きたない。\n傷、見られたくないもん。\n\0":
'???',

# Toji Suzuhara 
"なー、せやから兄ちゃんが\n治したる言うたやんか。\n\0":
'???',

# Toji's Sister
"…どうやって？\n\0":
'???',

# Toji Suzuhara 
"そら…、そうやな…。\nうーん…。\n\0":
'???',

# Toji's Sister
"…………………………。▽\nゴメン。\nちゃんと治るんだよね。\nわかってる…ゴメンな。\n\0":
'???',

# Toji Suzuhara 
"お前………。\n\0":
'???',

#
# ./USRDIR/event/cev1204.har_EXTRACT/cev1204.evs
#
# [Text Only - No Designated Speaker]
"教室の窓を開けて、バラした\n千羽鶴を外へ逃がした。\n\0":
'???',

# Toji Suzuhara 
"願い、叶うとええな。\n\0":
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
# ./USRDIR/event/cev1207.har_EXTRACT/cev1207.evs
#
# Toji Suzuhara 
"お前が一番行きたい所や。\n\0":
'???',

# Toji Suzuhara 
"兄ちゃん、兄ちゃんな、\n絶対お前が大きくなるまで\n一緒におったる。▽\nお前をもらいに来た男に\nパチキかましてから、\nちゃんと嫁に送り出したる！！\n\0":
'???',

# Toji Suzuhara 
"あいつ、海行きたいて…。\nそない書いてあったな。\n\0":
'???',

# Toji Suzuhara 
"よっしゃ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"陽が傾いてきた。\nまだだ、あと少し。\n汗まみれでペダルを漕ぐ。\n\0":
'???',

# Toji Suzuhara 
"あと少しや。\nこの坂降りて、カーブ過ぎたら…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"夕暮れの海は、\nどこまでが海か、どこまでが空か\nわからないくらい同じ色に染まる。▽\n目を細めた。▽\n陽は今日という日に\nしがみつこうとしながら沈み、\n海の波間を光らせていた。\n\0":
'???',

# Toji Suzuhara 
"待ってろ、待ってろ。\n兄ちゃんが、願い叶えたる…！\n\0":
'???',

# Toji's Sister
"兄ちゃん！？\n学校やったんちゃうん？\n\0":
'???',

# Toji Suzuhara 
"ええねん、はよ行こう。\n\0":
'???',

# Toji's Sister
"どこ…て？\n\0":
'???',

# Toji Suzuhara 
"ええから。\n看護師見つかる前に行くで。\n\0":
'???',

# [Text Only - No Designated Speaker]
"妹を担いで走った。\n病院にあった自転車を拝借して\n妹を後ろに乗せた。▽\nペダルを目一杯に漕ぎ出す。\n\0":
'???',

# Toji's Sister
"どこに行くーん？\n\0":
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
# ./USRDIR/event/cev1209.har_EXTRACT/cev1209.evs
#
# Toji Suzuhara 
"ドナー、見つかるんかな。\nそう、やたらに見つかるもんでも\nないんやな…。\n\0":
'???',

#
# ./USRDIR/event/cev1211.har_EXTRACT/cev1211.evs
#
# [Text Only - No Designated Speaker]
"………。▽\n………………。▽\n………………………。\n\0":
'???',

# [Text Only - No Designated Speaker]
"必死で戦って、戦って…。\n後の事はよく覚えていない。▽\n綾波がいたような気がする。\n妹もいたような気がする。\n\0":
'???',

# Toji Suzuhara 
"ええかげん、夢から覚めんと。▽\n妹が待ってる。▽\nどこや…？\nどこやろう、ここは。\n\0":
'???',

# [Text Only - No Designated Speaker]
"心のありったけを。▽\n心のありったけを、君に。\n\0":
'???',

# Toji Suzuhara 
"綾波か？\n何て？\nここどこやって？\n\0":
'???',

# Toji Suzuhara 
"そんな言うても、ようわからへん。\nワシ、妹の所へ帰りたいねん。\n案内してくれよ。\n\0":
'???',

# Rei Ayanami 
"その現実に、焦点を当てなさい…。\n\0":
'???',

# Toji Suzuhara 
"いや、何でもあらへん。▽\n帽子被っとき。\nベッピン肌なのに、\n焼けてまうで。\n\0":
'???',

# Toji Suzuhara 
"何やったっけ…。\n発令所ではそんな事言うてたなぁ。\n夢か何かやったんかなぁ。\n\0":
'???',

# Toji's Sister
"兄ちゃーん、起きーな！\n\0":
'???',

# Rei Ayanami 
"………あなたね。▽\n私たちの可能性を、\nアダムの子らから守ってくれた。▽\nあなたの現実は、\nあなただけのもの。▽\n何も決まってはいないわ。\n始まってもいない。▽\nここにあるのは無限の可能性。\n永遠の現実。\n\0":
'???',

# Toji Suzuhara 
"わぁぁっ！？▽\nな、何や、お前か…。\n\0":
'???',

# Toji's Sister
"おかんかて、怒ってるで。\n何度起こしたかて、起きん。\nもう、起こしたらへんって。\n\0":
'???',

# Toji Suzuhara 
"兄ちゃん、\nちゃんと起きれるっちゅーに。▽\n…って、わぁぁ…アカン！\nこんな時間…遅刻や。\n\0":
'???',

# Toji Suzuhara 
"どう言うこっちゃ。\n\0":
'???',

# Toji Suzuhara 
"行ってきます。\n\0":
'???',

# Rei Ayanami 
"全ての人は選択出来る。\n自分がなりたいものに。▽\n自分というものと\n自分の現実を限定しないで。▽\nあなたは何を選ぶの…？\n\0":
'???',

# Toji's Sister
"兄ちゃん、弁当忘れたら\nアカンでー！\n\0":
'???',

# Toji Suzuhara 
"おぉ、サンキュ。\n今日もあっついなぁ。\n明日から、お前も夏休みやな。\n\0":
'???',

# Toji's Sister
"うん、みんなで海行こな。\nおとんもおかんもおじいも\n兄ちゃんも一緒に！\n\0":
'???',

# Toji Suzuhara 
"……………………あ。\n\0":
'???',

# Toji's Sister
"どないしてん？\n\0":
'???',

# Toji Suzuhara 
"ワシか…？\nワシは………。\n\0":
'???',

# Toji's Sister
"ありがと、兄ちゃん。\nいつもいつも。\n\0":
'???',

# Toji Suzuhara 
"ほな、行ってくるわ。\n\0":
'???',

# Toji's Sister
"うん、行ってらっしゃい。\nお兄ちゃん！！\n\0":
'???',

#
# ./USRDIR/event/cev1212.har_EXTRACT/cev1212.evs
#
# Toji Suzuhara 
"…！？\nくそ、使徒か…。\n\0":
'???',

# Toji's Sister
"何の音…？\n\0":
'???',

# Toji Suzuhara 
"…さあな、\nただのサイレンやろ。\n\0":
'???',

# Toji's Sister
"そやない、ポケットから。\n電話ちゃうんかなぁ。\n\0":
'???',

# Toji Suzuhara 
"（くそ、本部からか…。）\n気にせんでええ。\n\0":
'???',

# Toji Suzuhara 
"（ここで戻った方が\n　一生後悔するわい…。）▽\nそら、海や！！\n\0":
'???',

# Toji Suzuhara 
"見てみ、ほら。\n海やぞ！！\n\0":
'???',

# Toji Suzuhara 
"どないしてん？\nなあ、おい！！\nどないしたんや！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"妹は抱きついたまま\nぐったりとしていた。\n\0":
'???',

# Toji Suzuhara 
"おい！！\n………熱が！？▽\nくそ、連れ出したんは\n間違いだったんか。▽\n…………………………。\n\0":
'???',

# [Text Only - No Designated Speaker]
"途方に暮れていると、\nネルフのＶＴＯＬが現れた。\n\0":
'???',

# Female Staff
"参号機をリニアレールで\nこちらに搬送中です。▽\nプラグスーツに着替えて\n指示に従って出撃してください！\n\0":
'???',

# Female Staff
"妹さんは、\nすぐ病院へ搬送します。\n\0":
'???',

# Toji's Sister
"兄ちゃん…。\nあのロボットの…？\n\0":
'???',

# Toji Suzuhara 
"黙っとって悪かったな。\n…待っとれよ。\n\0":
'???',

# Toji's Sister
"嫌や…。\nウチも一緒に行く。\n\0":
'???',

# Toji Suzuhara 
"アカンて。\nお前、大人しく待っとれ。\n大丈夫や、…な？\n\0":
'???',

# Toji Suzuhara 
"エヴァ参号機、出撃します！\n\0":
'???',

#
# ./USRDIR/event/cev1302.har_EXTRACT/cev1302.evs
#
# Kensuke Aida
"なあなあ、シンジ。\nどうだった？\nジェットアローン。\n\0":
'???',

# Shinji Ikari
"何で、ケンスケが知ってるの？\n\0":
'???',

# Kensuke Aida
"パパのパソコン見たんだ。\nパパもあの時、\nスタッフに加わってたらしいし。▽\nあれ止めたの、シンジなんだろ？\n\0":
'???',

# Kensuke Aida
"ああ、いいよなぁ…。\n俺もエヴァのパイロットに\nなりたいよ。▽\nシンジに加えてトウジまで\nパイロットだなんて。▽\nなぁ、どうやったら\nなれるもんなんだろ…？\n\0":
'???',

# Shinji Ikari
"僕は…、知らないよ。\nなりたくてなったんじゃないから。\n\0":
'???',

# Kensuke Aida
"まあな、そうだよな。\nあーぁ。\n\0":
'???',

# Shinji Ikari
"僕は、ミサトさんやスタッフの\n人達から言われた通りに\nやるだけなんだ。▽\nそういうの知ってるのは、\nスタッフだけだよ。\n\0":
'???',

# Kensuke Aida
"ふぅん、やっぱそうか。\n\0":
'???',

# Kensuke Aida
"……………………。▽\n（シンジに近いスタッフに接近して\n　いけば…、色んな情報を得る事が\n　出来るかもしれない。）▽\n（もしかすると、パイロットに\n　だって…、なるチャンスが\n　あるかもしれない。）\n\0":
'???',

# Kensuke Aida
"よし！\nチャンスがないわけじゃ\nないかもな。\n\0":
'???',

#
# ./USRDIR/event/cev1303.har_EXTRACT/cev1303.evs
#
# Kensuke Aida
"まずは情報集めだ。\nネルフのスタッフに近づいて、\n色んな情報を聞き出すんだ。▽\n自分に何が足りないのか、\nどうすればパイロットになれるか。\nそれを知る事が出来れば…。▽\nようし、頑張るぞ！\n\0":
'???',

#
# ./USRDIR/event/cev1304.har_EXTRACT/cev1304.evs
#
# Kensuke Aida
"エヴァが何なのか…。\nただの人間が作ったロボット\nなんかじゃないみたいだ…。▽\n早速データを見せてもらうか。\nえーと、なになに…。▽\nコアにはパイロットの母の魂が\n入れられており、\nこれを介在にして操縦が出来………。\n\0":
'???',

# Kensuke Aida
"…何だ、これ。\n魂って何だよ…。▽\nじゃあ、\n初号機にはシンジの母親が…、\n弐号機には惣流の…。▽\nあいつら…、\n何も知らされないはずだ…。\nこんな事って…。\n\0":
'???',

#
# ./USRDIR/event/cev1305.har_EXTRACT/cev1305.evs
#
# Kensuke Aida
"マルドゥック機関。\nエヴァのパイロット選出を目的に、\n設けられた謎の機関。▽\nふうん…、そうは言ってもね。\n何を基準にパイロットを選んで\nいるんだか。▽\nえと、続きは…っと？\n\0":
'???',

# Kensuke Aida
"…何だこれ？▽\n学校…クラスメイトの名簿…。\nエヴァンゲリオンパイロット\n適格者候補？▽\nこれって、クラスメイト全員が\n適格者であるって事なのか！？\nそうか、だからトウジも…。\n\0":
'???',

#
# ./USRDIR/event/cev1306.har_EXTRACT/cev1306.evs
#
# Kensuke Aida
"このクラスメイト全員が、\nエヴァパイロットの適格者…。▽\nじゃあ、俺にだって素質は\n充分にあるはずだ…。\n\0":
'???',

#
# ./USRDIR/event/cev1307.har_EXTRACT/cev1307.evs
#
# Kensuke Aida
"パイロットが…エヴァを扱う為には\n母親の魂が必要…。▽\nママの魂なんてのが…、\n本当にあるとしたら。\nあるとしたら…。\n\0":
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
# ./USRDIR/event/cev1309.har_EXTRACT/cev1309.evs
#
# Announcement
"ただいま、東海地方を中心に\n非常事態宣言が発令されました。▽\n住民の皆様は、速やかに\n指定のシェルターへ\n避難してください。\n\0":
'???',

# Kensuke Aida
"使徒だ…。\nくそ…、\n俺がパイロットだったら…。\n\0":
'???',

# Shigeru Aoba, Male Staff
"目標は防衛線にて交戦中。\n\0":
'???',

# Makoto Hyuga
"ああっ…！！\n\0":
'???',

# Misato Katsuragi 
"なんて破壊力…。\nあれだけの迎撃システムを\n一瞬にして消し去るなんて。\n\0":
'???',

# Makoto Hyuga
"まずい、あの破壊力をもってすれば\nジオフロントの特殊装甲板は簡単に\n破壊されてしまう…。\n\0":
'???',

# Misato Katsuragi 
"こいつは強敵だわ。\n遺書を書く暇もなさそうね。\n\0":
'???',

# Shigeru Aoba, Male Staff
"国連軍に、\n足止めを要請しておきます。\n\0":
'???',

# Maya Ibuki, Female Staff
"エヴァ、起動準備整いました。\n\0":
'???',

# Makoto Hyuga, Male Staff
"パイロット準備ＯＫ。\nパイロットに作戦の指示を\nお願いします。\n\0":
'???',

# Misato Katsuragi 
"時は一刻を争うわ。▽\nヤツがゼロエリアに\n到達するのが先か。\nエヴァが使徒を倒すのが先か。\n\0":
'???',

# Misato Katsuragi, Female Staff
"ゼルエル\n\0":
'???',

# Misato Katsuragi 
"防衛線にて迎撃システムにより\n交戦するが、\n\0":
'???',

# Misato Katsuragi 
"目標は、驚異的な破壊力を持って\nこれを一掃、\n\0":
'???',

# Misato Katsuragi 
"ただちにエヴァを出撃させ、\n市街地にて目標と交戦、\n本作戦に出動したエヴァは…\n\0":
'???',

#
# ./USRDIR/event/cev1310.har_EXTRACT/cev1310.evs
#
# Hikari Horaki
"起立、礼。\n\0":
'???',

#
# ./USRDIR/event/cev1311.har_EXTRACT/cev1311.evs
#
# Asuka Soryu Langley
"相田…。\n\0":
'???',

# Kensuke Aida
"惣流か。\n\0":
'???',

# Kensuke Aida
"…知ってるよ。\n使徒と戦って、そして…。\nトウジは死んだんだろ。\n\0":
'???',

# Kensuke Aida
"…知らないわけがないだろ。\nアイツ、俺達を守ったんだ。▽\n………………………。\n\0":
'???',

#
# ./USRDIR/event/cev1312.har_EXTRACT/cev1312.evs
#
# Kensuke Aida
"トウジ…。\n考えが甘かった…。▽\nパイロットになりたいなんて、\n今思うと…すごく怖い。▽\nごめん、トウジ…。\nトウジがパイロットになった時、\nひどく羨んだりして…。\n\0":
'???',

# Kensuke's Father
"ケン坊…。\nどうしたんだ…？\n\0":
'???',

# Kensuke Aida
"トウジが…。\nクラスメイトのトウジが…。\n\0":
'???',

# Kensuke's Father
"…………………。▽\nケン坊はパパが絶対守ってやる。\n絶対に…。▽\n例え何もかもを敵に回しても。\nそれがママとの約束だったから。▽\n……………………。\n\0":
'???',

# Kensuke Aida
"パパ…？\n\0":
'Papa...?\n\0',

#
# ./USRDIR/event/cev1313.har_EXTRACT/cev1313.evs
#
# School Broadcast
"２年Ａ組の相田。\n相田ケンスケ。\n至急、校長室まで。\n\0":
'???',

# Kensuke Aida
"…？\n何だろう…。\n\0":
'???',

# Kensuke Aida
"どうしようもない大きな力を前に\nその運命を受け入れるしか\n道はないようだった。▽\nそして…、パイロットに\n憧れていた頃の自分を\n懐かしく思った…。\n\0":
'???',

# Ritsuko Akagi 
"我々ネルフの組織による\nマルドゥック機関により、\nパイロットの選出を行った結果、▽\n今回は、あなたがその素質を\n見込まれて選ばれる運びと\nなりました。\n\0":
'???',

# Kensuke Aida
"あ…、あ………。\n\0":
'???',

# Ritsuko Akagi 
"どう？\n引き受けてくれるかしら？\n\0":
'???',

# Ritsuko Akagi 
"お父さんにも、この件に関して\n了承は得てあります。\n\0":
'???',

# Kensuke Aida
"パパが？\nそんなはず…。\n\0":
'???',

# Teacher
"相田。\nお父さんが事故で危険な状態だ。\nすぐに、病院へ！！\n\0":
'???',

# Kensuke Aida
"…パパが！？\n\0":
'???',

# Ritsuko Akagi 
"…………………。▽\nそれじゃあ、\n今日のところは失礼します。\n\0":
'???',

# [Text Only - No Designated Speaker]
"多分、パパは自分のために\n戦ってくれたのだろう。\nでも…\n\0":
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
# ./USRDIR/event/cev1402.har_EXTRACT/cev1402.evs
#
# Toji Suzuhara 
"よぉ、委員長。\n\0":
'???',

# Hikari Horaki
"鈴原？\n\0":
'Suzuhara?\n\0',

# Toji Suzuhara 
"放課後、ヒマか？\nちょっと付き合ってくれへんか？\n\0":
'???',

# Hikari Horaki
"何よ…。\nなーんか、よからぬ事を\n企んでない？\n\0":
'???',

# Toji Suzuhara 
"アホ、そっちこそ何やねん。\nワシをそんなに悪モンに\nしたいんか？▽\nもう、ええわ。▽\nえーと、綾波。\nちょい放課後付き合ってぇな。\n\0":
'???',

#
# ./USRDIR/event/cev1403.har_EXTRACT/cev1403.evs
#
# Toji Suzuhara 
"ほな、綾波。\nちょっと付き合ぅてくれるか？\n\0":
'???',

# Rei Ayanami 
"…どこか、行くの？\n\0":
'???',

# Toji Suzuhara 
"んー、ちょっと人には\n言えんところなんやけど…。\n\0":
'???',

# Hikari Horaki
"鈴原！\n掃除当番サボって\nどこ行くつもりなの？\n\0":
'???',

# Toji Suzuhara 
"自分には関係あらへん。▽\n他にもサボっとる奴おるやん。\nワシだけにそんな、\n突っかかってくんなや。\n\0":
'???',

#
# ./USRDIR/event/cev1404.har_EXTRACT/cev1404.evs
#
# Hikari Horaki
"別に悪者にしたいわけじゃ\nないのにな…。\n何かいつも、ムキになっちゃう。▽\n…素直に、なりたいなぁ。\n\0":
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
# ./USRDIR/event/cev1406.har_EXTRACT/cev1406.evs
#
# Hikari Horaki
"スズハラぁ〜〜〜〜！！\n\0":
'???',

# Toji Suzuhara 
"何や、今日は怒られるような\n悪い事してへんぞ。\n\0":
'???',

# Hikari Horaki
"綾波さんを、\nどこに付き合わせたかと思ったら！\n女性下着売り場ですってェェェ！？\n\0":
'???',

# Toji Suzuhara 
"そうや。\n\0":
'???',

# Hikari Horaki
"何、トーゼンって顔してるのよ！\nそれセクハラよ、セクハラ！！\nもう、サイッテェ！！\n\0":
'???',

# Toji Suzuhara 
"…ワシが行って、\n買うわけにはアカンやろ。\n\0":
'???',

# Hikari Horaki
"何、このヘンタイ！！\n何でそんなものが必要なのよ！\n\0":
'???',

# Toji Suzuhara 
"入院しとる妹の着替えや。\nワシじゃ女モンのセンス、\nわからへんしな。\n\0":
'???',

# Toji Suzuhara 
"ま、えーよ。\nどうせワシの事、悪人や思ぅて\n監視しとるんやろうし。▽\n最初は委員長に選んでもらおうと\n思って声かけたんやけどな。\n綾波で正解やったわ。▽\nそないに、ギャーギャー\n言われる事もなかったしな。▽\nケッ…。\n恥かかすな、アホゥ。\n\0":
'???',

# Hikari Horaki
"ごめ………。\n\0":
'???',

# Toji Suzuhara 
"えーよ、タコ！\n\0":
'???',

#
# ./USRDIR/event/cev1407.har_EXTRACT/cev1407.evs
#
# Toji Suzuhara 
"…………………。▽\n何や、また説教か。\n\0":
'???',

#
# ./USRDIR/event/cev1408.har_EXTRACT/cev1408.evs
#
# Hikari Horaki
"駄目だなぁ…、駄目だなぁ。\nきっと鈴原、私の事\n嫌いになったんだ…。▽\nどうしよう…。\n\0":
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
# ./USRDIR/event/cev1410.har_EXTRACT/cev1410.evs
#
# Hikari Horaki
"せめて、素直になろう。\n例え気持ちが伝えられなくても。\n好きになってくれなくても。▽\n後悔だけは、しないように…。\n\0":
'???',

#
# ./USRDIR/event/cev1411.har_EXTRACT/cev1411.evs
#
# Kensuke Aida
"何かやったの？\n\0":
'???',

# Kensuke Aida
"さー？▽\nところでさ、シンジ。\nちょいと気になる情報を\n仕入れたんだけど。\n\0":
'???',

# Kensuke Aida
"そう、アメリカで建造中だった奴さ。\n完成したんだろ？▽\n隠さなきゃならない事情も\nわかるけど。\nな、教えてくれよ。\n\0":
'???',

# Kensuke Aida
"パイロットはまだ決まって\nないんだろ？\n\0":
'???',

# Kensuke Aida
"俺にやらせてくんないかなぁ、\nミサトさん。▽\nな、シンジからも頼んでくれよ！\n乗りたいんだよ、エヴァに。\n\0":
'???',

# Kensuke Aida
"…………………。▽\nじゃ、四号機が欠番になった話は？\n\0":
'???',

#
# ./USRDIR/event/cev1412.har_EXTRACT/cev1412.evs
#
# Hikari Horaki
"ねえ、鈴原。\n校長室に呼び出されたのって\n何だったの？\n\0":
'???',

# Toji Suzuhara 
"悪い事はしてへん。\n\0":
'???',

# Hikari Horaki
"…うん。\nそれは、信じてる…。\n\0":
'???',

#
# ./USRDIR/event/cev1413.har_EXTRACT/cev1413.evs
#
# Hikari Horaki
"鈴原…、校長室に呼ばれたの\n何だったんだろう？▽\nあの後…元気ないみたいだった。▽\nどうすればいいかな。\n何がいいかな。\n元気出してくれるには…。▽\nお弁当とか作ったら…。▽\nでも、受け取ってくれるかなぁ…。\n\0":
'???',

#
# ./USRDIR/event/cev1414.har_EXTRACT/cev1414.evs
#
# Hikari Horaki
"鈴原、欠席なんだ…。\nせっかくお弁当作ってきたのにな。\n\0":
'???',

#
# ./USRDIR/event/cev1415.har_EXTRACT/cev1415.evs
#
# Hikari Horaki
"鈴原、明日は学校来るかなぁ。\nどんなお弁当にしよう。\n\0":
'???',

#
# ./USRDIR/event/cev1416.har_EXTRACT/cev1416.evs
#
# Hikari Horaki
"駄目だ…。\n意気地なしだな、私…。▽\n寂しそうな背中。\nどこに行くんだろう…。\n\0":
'???',

# Hikari Horaki
"鈴原！\n\0":
'???',

# Toji Suzuhara 
"委員長か…。\n\0":
'???',

# Hikari Horaki
"どうしたの？\nそれに、そんな荷物…。\n\0":
'???',

# Toji Suzuhara 
"…ん。\n２、３日ばかり、ちょっとな。▽\n理由、今は言えへんけど。\n戻ったら、委員長にも話すわ。\n\0":
'???',

# Toji Suzuhara 
"…怒らへんのやな。\n悪さしよーとしとるとか。\n\0":
'???',

# Hikari Horaki
"…ううん。\nそんなんじゃないんでしょ？\n\0":
'???',

# Toji Suzuhara 
"…ん。▽\nほな、ワシ急ぐから。\n\0":
'???',

# Hikari Horaki
"あ…。▽\n（どうしよう、渡さなきゃ。\n　鈴原の為に作ったお弁当…。\n　早く渡さなきゃ、行っちゃう…。）\n\0":
'???',

# Hikari Horaki
"す、鈴原、待って！！\n\0":
'???',

# Toji Suzuhara 
"…あ？\n\0":
'???',

# Hikari Horaki
"お弁当作ったの。\nその、食べてもらいたくて！\n\0":
'???',

# Toji Suzuhara 
"……………ぉ。\nサンキュー。▽\nワシ…、頑張るわ。\n\0":
'???',

# Hikari Horaki
"が…、\n頑張ってね。▽\n何しに行くか、わからないけど。\n鈴原、頑張って！！\n\0":
'???',

# Toji Suzuhara 
"ああ…。\nおおきに、委員長。\n\0":
'???',

#
# ./USRDIR/event/cev1417.har_EXTRACT/cev1417.evs
#
# Matsushiro Staff
"…シンクロ率、起動値クリア！\n\0":
'???',

# Ritsuko Akagi 
"まあ、最初はこんなものね。\n\0":
'???',

# Matsushiro Staff
"現在、シンクロ率８。\nシンクロ率、にぶいながらも\n引き続き上昇を続けています。\n\0":
'???',

# Matsushiro Staff
"エントリープラグ固定完了。▽\n第一次接続開始。\n\0":
'???',

# Ritsuko Akagi 
"機体、パイロットともに\n期待出来そうね。\n\0":
'???',

# Matsushiro Staff
"全神経、いい感じで\nつながっています。\n\0":
'???',

# Ritsuko Akagi 
"ＯＫ、テスト終了よ。\nそれじゃあ、参号機は\n本部へ納入します。\n\0":
'???',

# Matsushiro Staff
"絶対境界線突破、\n双方向回線開きます。▽\nハーモニクス正常、\nシンクロ率算出します。\n\0":
'???',

# Ritsuko Akagi 
"さて、問題はここから。\n調子、どうかしら？\n\0":
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
# ./USRDIR/event/cev1419.har_EXTRACT/cev1419.evs
#
# Hikari Horaki
"鈴原…。\n\0":
'???',

# Toji Suzuhara 
"委員長。\n弁当、サンキューな。\nウマかったわ。\n\0":
'???',

# Hikari Horaki
"あ、ありがとう…。\n\0":
'???',

# Toji Suzuhara 
"へ？\nありがとうて、言うんはこっちや。\n変な奴やのー。\n\0":
'???',

# Hikari Horaki
"ううん、な、何でもないの。\n\0":
'???',

# Toji Suzuhara 
"あんな、屋上…来てくれるか？\n\0":
'???',

# Hikari Horaki
"…！？▽\nあ、何…？\n\0":
'???',

# Toji Suzuhara 
"言わなアカン事あんねん。\n委員長に。\n\0":
'???',

# Hikari Horaki
"…う、うん。\n\0":
'???',

# Toji Suzuhara 
"あんな…、ワシ…。\n\0":
'???',

# Hikari Horaki
"わ、私も覚悟出来てるから。\nでも、やっぱり中学生だし\n友達から始めるとか…その…。\n\0":
'???',

# Toji Suzuhara 
"エヴァのパイロット、\nやる事になってん…。\n\0":
'???',

# Hikari Horaki
"交換日記くらいなら、\nその…大丈夫かなって…、\n\0":
'???',

# Hikari Horaki
"………………え？\n\0":
'???',

# Hikari Horaki
"そう…なの？\n\0":
'???',

# Toji Suzuhara 
"ワシ、妹の見舞いとかで\n遅刻多いし…、▽\nその上、この先ガッコ休むんも\n多くなると思う…。\n\0":
'???',

# Hikari Horaki
"断れなかったの…？\n\0":
'???',

# Toji Suzuhara 
"妹、ネルフ本部の病院に\n転院させてくれるんや。▽\nその方がいい治療受けられる\nやろうし。\n\0":
'???',

# Hikari Horaki
"だけど、あんなのに乗って…。\n死ぬかもしれないじゃない！▽\nそ…、そしたら…、▽\nそしたら、妹さんは誰が\n見てあげるの！？\n\0":
'???',

# Toji Suzuhara 
"そン時は…、委員長。\n自分が支えたってくれへんか？\n\0":
'???',

# Toji Suzuhara 
"頼むわ…。\n\0":
'???',

# Hikari Horaki
"うん、わかった。\n無理…、しないでね。\n\0":
'???',

# Toji Suzuhara 
"ほな、ワシ、これから\n妹の見舞い行くから。\nまたな。\n\0":
'???',

# Hikari Horaki
"…………………。▽\n鈴原…。\n\0":
'???',

#
# ./USRDIR/event/cev1420.har_EXTRACT/cev1420.evs
#
# Teacher
"なお、昨日が通夜となりましたので\n本日、放課後に葬儀となります。▽\n授業を切り上げて、\n皆さん葬儀の方へ出席する事に\nなります。\n\0":
'???',

#
# ./USRDIR/event/cev1421.har_EXTRACT/cev1421.evs
#
# Asuka Soryu Langley
"アイツ…、エヴァに乗ってたの。\nパイロットになって、\n起動実験の最中に…。▽\nアイツの機体が使徒に…。▽\n公式には、鈴原は交通事故って\n死因になってるけど…、本当は…。\n\0":
'???',

# Hikari Horaki
"………………。▽\nな…んで。\nどうしてなのよ！？\n何で、鈴原がそんな…。\n\0":
'???',

# Asuka Soryu Langley
"ヒカリ、あのね…。\n\0":
'???',

# Hikari Horaki
"事故だなんて。\nあの時、引っ張っててでも\n学校に連れて行ったら…。\n\0":
'???',

#
# ./USRDIR/event/cev1422.har_EXTRACT/cev1422.evs
#
# Hikari Horaki
"鈴原…。\nここを出ていかなくっちゃ\nいけないんだ。▽\n鈴原と出会った場所なのにね。\n大事な大事な場所なのに…。▽\n……………。▽\nさよなら…。\n\0":
'???',

#
# ./USRDIR/event/cev1423.har_EXTRACT/cev1423.evs
#
# Kensuke Aida
"ほら来た。▽\nやっぱ、人類の未来を担う\nパイロットとなると、\n監視されてるものなんだな。\n\0":
'???',

# Toji Suzuhara 
"おわーーーーッ！？\n\0":
'???',

# Hikari Horaki
"鈴原…、大丈夫！？\n\0":
'Suzuhara... you\'re okay?!\n\0',

# Kensuke Aida
"階段から足滑らせて\n転んだんだ…。\n\0":
'???',

# Hikari Horaki
"意識が無い。\nき、救急車…。\n\0":
'???',

# Kensuke Aida
"落ち着いて、委員長。▽\n大丈夫だよ。\nアイツはパイロットだから、\n最良の治療をしてもらえる。▽\nすぐ、ネルフの医療スタッフが\n来るはずだよ。\n\0":
'???',

#
# ./USRDIR/event/cev1424.har_EXTRACT/cev1424.evs
#
# Hikari Horaki
"鈴原…、大丈夫かな。\nお見舞いとか行きたいけれど。\n一般人は行けない所なんだろうな。\n\0":
'???',

#
# ./USRDIR/event/cev1425.har_EXTRACT/cev1425.evs
#
# Asuka Soryu Langley
"鈴原？\nあぁ、本部の病院にいるわ。▽\n何か、やっぱり打ち所が\n悪かったのかな。▽\n意識…戻らないんだって。\n\0":
'???',

# Rei Ayanami 
"鈴原君？\n本部の病院に入院しているわ。\n彼、昏睡状態だそうよ。\n\0":
'???',

# Shinji Ikari
"トウジ…、大丈夫かな。\n本部の病院にいるんだけどね。\n意識が戻らないんだって。\n\0":
'???',

# Kaworu Nagisa 
"トウジ君は…、僕も心配なんだ。\n本部の病院にいるけれども。\n意識が戻らないらしいんだ。\n\0":
'???',

# Hikari Horaki
"お見舞いとか行っちゃ…、\n駄目なのかな…。\n\0":
'???',

# Asuka Soryu Langley
"身内ならね…。\n\0":
'???',

# Rei Ayanami 
"家族なら…。\n許可は出るけど…。\n\0":
'???',

# Shinji Ikari
"家族とかだったら…。\n\0":
'???',

# Kaworu Nagisa 
"家族だったら…。\n\0":
'???',

# Hikari Horaki
"無理なんだ…。\n\0":
'???',

# Asuka Soryu Langley
"職員の人から、\n一筆書いてもらえば\nいいんだけどねー。▽\nミサトとか…。\n\0":
'???',

# Rei Ayanami 
"ネルフ職員から、\n許可証を書いてもらえば\n病院には入れるわ。\n\0":
'???',

# Shinji Ikari
"ミサトさんから、\n許可証を作ってもらうとか\nどうかなぁ…。\n\0":
'???',

# Kaworu Nagisa 
"多分、ミサトさんから\n許可証でも書いてもらえば…。\n大丈夫だと思うよ。\n\0":
'???',

# Hikari Horaki
"ホント！？\n私、ミサトさんに頼んでみる。\n\0":
'???',

#
# ./USRDIR/event/cev1426.har_EXTRACT/cev1426.evs
#
# Misato Katsuragi 
"ひょっとして…彼の恋人…？\n\0":
'???',

# Hikari Horaki
"な…、そんな！\n\0":
'???',

# Misato Katsuragi 
"そうだったら、\n連れて行ってもいいかなって\n思ったの。▽\n彼に呼びかけてくれれば、\nひょっとしたら意識も\n戻るんじゃないかって。▽\n非科学的だけど、\n家族や大事な人からの呼びかけで\n回復に繋がる症例が多いから。\n\0":
'???',

# Hikari Horaki
"…恋人とかじゃ、ありません。▽\nでも…、彼には…会いたいです。\nお願いします。\n\0":
'???',

# Misato Katsuragi 
"…わかったわ。\nただし、会話も記録されるし、\n面会時間も限られるけど。▽\nそれでもいい？\n\0":
'???',

# Hikari Horaki
"あ、ありがとうございます！！\n\0":
'???',

# Misato Katsuragi 
"じゃあ、これ。\nこれを持っていきなさい。\nこの文書を受付で見せて。▽\n彼を、お願いね…。\n\0":
'???',

# Hikari Horaki
"…はい！\n\0":
'???',

# Misato Katsuragi 
"（ひょっとしたら、\n　そういう仲なのかもね。）\n\0":
'???',

# Misato Katsuragi 
"あら、洞木さん…だっけ？\n\0":
'???',

# Hikari Horaki
"あの…、\n鈴原君のお見舞いに行きたいんです。\n駄目ですか？\n\0":
'???',

# Misato Katsuragi 
"関係者以外は、\n彼に会わせる事にはいかないの。\n\0":
'???',

# Hikari Horaki
"…あの、許可証とかがないと\n駄目ですか？\n\0":
'???',

# Misato Katsuragi 
"んー…。\n\0":
'???',

#
# ./USRDIR/event/cev1427.har_EXTRACT/cev1427.evs
#
# Hikari Horaki
"あの…、これ。\n\0":
'Umm... here.\n\0',

# Receptionist
"はい、面会ですね。\n伺っております。\nご案内します。\n\0":
'???',

# Nurse
"面会は五分だから。\nそれから、お見舞い品は\n渡してはいけません。\n\0":
'???',

# Hikari Horaki
"鈴原…。▽\nバカ、さっさと起きてよ。\n鈴原いないと…さみしいじゃない…。\n\0":
'???',

# Hikari Horaki
"…………………。▽\n私ね…、鈴原が好きだよ。\n悪口言われて、かばってくれた時\n本当に嬉しかった。▽\n…………………好き。\n\0":
'???',

# Toji Suzuhara 
"………………あ？\n何…、何て…？\n\0":
'???',

# Hikari Horaki
"す、鈴原！？\n\0":
'???',

# Toji Suzuhara 
"委員長やん…。\n何やココ？\nワシ、入院してるんか？\n\0":
'???',

# Hikari Horaki
"そ、そうよ。\n学校の階段で転んで。\n大変だったのよ。\n\0":
'???',

# Toji Suzuhara 
"そか…。\nみんなに迷惑かけたな。▽\nで、何か言うてへんかった…？\nさっき…。\n\0":
'???',

# Hikari Horaki
"ううん、何でも！\n何でもない、名前呼んだだけ。\n\0":
'???',

# Nurse
"面会時間は過ぎましたので…、▽\n意識が戻ったの！？\nすぐに、連絡を…。\n\0":
'???',

# Toji Suzuhara 
"…？？？▽\nそないに寝てたんかな…。\nワシ…。\n\0":
'???',

# Hikari Horaki
"意識、しばらくなかったんだって。\n\0":
'???',

# Toji Suzuhara 
"アツツ…、ギブスはめてる？\n骨折までしとったんかいな。\n\0":
'???',

# Misato Katsuragi 
"トウジ君？\n目が覚めたんですって！？\nやっぱり、カンが当たったわ。\n\0":
'???',

# Toji Suzuhara 
"ミサトさん。\nへ？\nカンて…？\n\0":
'???',

# Misato Katsuragi 
"使徒が現れたの。\n無理は承知の上よ。▽\nでも、今回の作戦にはあなたが\n必要なの。▽\n迎えをよこすわ。\nお願い、本部まで急いで！\n\0":
'???',

# Toji Suzuhara 
"出撃や。\n\0":
'???',

# Hikari Horaki
"そんな。\nその身体じゃ無理よ。\n\0":
'???',

# Toji Suzuhara 
"アホゥ…、ワシなら大丈夫や。\n\0":
'???',

# Hikari Horaki
"（どうしよう…。\n　鈴原に何かあったら。）▽\n（ひょっとしたら、\n　もう会えなくなるかもしれない。）\n\0":
'???',

# Hikari Horaki
"行かないで！！\n行かせない！！\n\0":
'???',

# Toji Suzuhara 
"お前…。\n\0":
'???',

# Hikari Horaki
"鈴原、死んじゃうわ。\nあんな危ない事！▽\n鈴原いなくなったら、\n私、私………。\n\0":
'???',

# Toji Suzuhara 
"…………………。▽\n大丈夫や、戻る。\n約束する。\n委員長の為に…。\n\0":
'???',

# Hikari Horaki, Makoto Hyuga
"…え。\n\0":
'???',

# Toji Suzuhara 
"約束するわ。\n好きやから。\n委員長が好きやから。\n\0":
'???',

# Toji Suzuhara 
"帰ったら、返事聞かせてや。▽\nほな、ワシ…行くわ。\n委員長も早いとこ、避難せぇよ。\n\0":
'???',

# Hikari Horaki
"バカ。\n私の方が、ずっと前から\n好きだったんだからね…。\n\0":
'???',

# Toji Suzuhara 
"へ？\n\0":
'???',

# Hikari Horaki
"ずっと好きだったんだからね！！\n\0":
'???',

# Misato Katsuragi 
"トウジ君、トウジ君！！\n早く…、もう出たの？\nトウジくーん！！\n\0":
'???',

# Hikari Horaki
"やっと素直になれた。\n鈴原の前で…。\n\0":
'???',

# Hikari Horaki
"大好き、鈴原…。\n\0":
'???',

# Hikari Horaki
"（でも、言えない。\n　ここで気持ち伝えても…、鈴原を\n　止める事は出来ないもの…。）\n\0":
'???',

# Toji Suzuhara 
"ほな、ワシ…行くわ。\nじゃあな、委員長。\n早いとこ、避難せぇよ。\n\0":
'???',

#
# ./USRDIR/event/cev1428.har_EXTRACT/cev1428.evs
#
# Teacher
"えー、まず皆さんには\n大変悲しいお知らせがあります。\n鈴原トウジ君が亡くなりました。\n\0":
'???',

# Teacher
"鈴原君は、先日事故に遭い\n病院へ運ばれましたが、\n昨夜亡くなったそうです…。\n\0":
'???',

# Hikari Horaki
"…そ…んな。\n\0":
'???',

#
# ./USRDIR/event/cev1429.har_EXTRACT/cev1429.evs
#
# Asuka Soryu Langley
"…ヒカリ。\n\0":
'???',

# Hikari Horaki
"うわぁぁぁぁぁぁぁぁぁぁ！！\n\0":
'???',

# Asuka Soryu Langley
"ヒカリ…。\n\0":
'???',

# Hikari Horaki
"せっかく素直になれると思ったんだ。\n後悔しない様に頑張ったんだ。\nでも…。\n\0":
'???',

# Hikari Horaki
"信じられない。\n遺体も、無いままのお葬式なんて。\n\0":
'???',

# Asuka Soryu Langley
"鈴原ね、\n事故って言ってあるけど。\n本当は…。\n\0":
'???',

# Hikari Horaki
"…知ってる。\nエヴァの中だったんでしょ…。▽\n彼が行くまで、一緒だったの。\nあの時、引き止めていれば\n私…、私…！！\n\0":
'???',

#
# ./USRDIR/event/cev1501.har_EXTRACT/cev1501.evs
#
# Misato Katsuragi 
"結果、\n碇シンジ、鈴原トウジ両名による、\n目標の説得に成功。\n\0":
'???',

# Misato Katsuragi 
"第３使徒\n\0":
'???',

# Misato Katsuragi 
"以後「渚カヲル」は従来通り、\n\0":
'???',

# Misato Katsuragi, Female Staff
"タブリス\n\0":
'???',

# Misato Katsuragi 
"セントラルドグマに突如出現した\n使徒の正体は、\n\0":
'???',

# Misato Katsuragi, Female Staff
"フィフス・チルドレン\n「渚・カヲル」であることが判明。\n\0":
'???',

# Misato Katsuragi 
"フィフス・チルドレンとして\nエヴァパイロットを\n続行することになりました。\n\0":
'???',

# Misato Katsuragi 
"目標はターミナルドグマを目指して\n侵攻しました。\n\0":
'???',

# Misato Katsuragi 
"初号機パイロット、碇シンジ及び、\n参号機パイロット、鈴原トウジが\n目標を追撃。\n\0":
'???',

# Misato Katsuragi 
"接触に成功し、目標に対し説得を\n試みます。\n\0":
'???',

#
# ./USRDIR/event/cev1502.har_EXTRACT/cev1502.evs
#
# Kaworu Nagisa 
"…闇の中。▽\n…白い月。▽\n僕が僕になる前のこと…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"いつから僕は、\n僕になったのだろう…。▽\nヒト…、リリン…。\nヒトの中で僕は生きている。▽\nあそこで死んでもよかったんだ。\n使徒として。▽\nでも…。\n僕は、生きていく事を選択した。▽\n生きる、意味。▽\nリリンであれ、使徒であれ…\nそれは同じかもしれないけど。\n\0":
'???',

# Kaworu Nagisa 
"…………………………。▽\n忘れてしまおう。\n何もかも。▽\n僕は、ヒトとして生きる事を\n選んだんだ…。\n\0":
'???',

#
# ./USRDIR/event/cev1503.har_EXTRACT/cev1503.evs
#
# [Text Only - No Designated Speaker]
"僕…。▽\n僕は…、渚カヲル。\nタブリス。\nアダム…。▽\nどれも、\nヒトがそう呼んだだけだ。▽\n僕の姿。▽\nヒトの形。\n魂がとらわれている器。\nヒトが用意した姿。▽\n仕組まれた姿。\n仕組まれた子供。▽\n本当の僕はどこにある。\n僕の本当の身体はどこにある。\n\0":
'???',

# Kaworu Nagisa 
"いや…、知ってどうするんだ。\n知って…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"でも、僕が何者なのか。\nその思いは膨らむばかりだ。▽\n僕を生み出した、第一始祖民族。\nあの老人達は…、碇司令は\nその秘密を知っているんだろうか。\n\0":
'???',

# Kaworu Nagisa 
"僕はどこから来て…。▽\nどこへ行くのだろう…。▽\n第一始祖民族…か。\n何の為に…、僕を…創った？\n\0":
'???',

#
# ./USRDIR/event/cev1504.har_EXTRACT/cev1504.evs
#
# [Text Only - No Designated Speaker]
"この星空の彼方。\nずっと向こう。\n僕を送り出した神がいる。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ゼーレは、神になろうとした。\n人類の補完、不老不死の存在。▽\nでも、本当の神は違う。\n僕や、リリスを創り出した存在。\n第一始祖民族…。\n\0":
'???',

#
# ./USRDIR/event/cev1505.har_EXTRACT/cev1505.evs
#
# Kaworu Nagisa 
"僕は誰だ。\n何者なんだ…。▽\n渚カヲル。\nタブリス。\nアダム…。▽\n僕は、何かを知っている。\n何かを…知っている。\n\0":
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
# ./USRDIR/event/cev1601.har_EXTRACT/cev1601.evs
#
# [Text Only - No Designated Speaker]
"ペンペンがテレビを食い入るように\n観ている。▽\nブラウン管の中には艶っぽい顔の\nヨークシャーテリアが荷物を\n引っ張っている。▽\n引越しのＣＭのようだ…。\n\0":
'???',

# Pen Pen
"ギャギャッ、ギャギャギャッ！！\n\0":
'???',

# Misato Katsuragi 
"ペンペンったら、\nはしゃいじゃってどうしたの？\n\0":
'???',

# Pen Pen
"ギャーーーーーーーーーーー！\n\0":
'???',

# Pen Pen
"クゥゥゥゥ…。\n\0":
'???',

# Misato Katsuragi 
"今度は、目一杯ヘコんじゃって\nどうしたの…？\n\0":
'???',

# Pen Pen
"クェーーー。\n\0":
'???',

# Pen Pen
"ギャッ、ギャギャッ！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"テレビからさっきと\n同じＣＭが流れてきた。\nペンペンが素早くテレビまで走る。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ペンペンは、\nどうやらブラウン管の中の犬に\n恋をしているようだ。\n\0":
'???',

# Misato Katsuragi 
"ペンペン、あのね…。\nあれはワンちゃんなの。\nそしてあなたはペンギン。▽\n結ばれない恋なのよ…。\n\0":
'???',

# Pen Pen
"クーゥ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ペンペンは、\n切なそうに溜息をついた。\n恋わずらいだろうか、元気がない。\n\0":
'???',

# T.V. Commercial
"いよいよキャンペーン開始！\nこちらの製品のシールを集めて送ると\n５０００名に素敵なプレゼントが！▽\n特賞６０名様に、\n沖縄旅行プレゼント！！\n\0":
'???',

# Misato Katsuragi 
"あらー、いいわよねー沖縄。\n\0":
'???',

# T.V. Commercial
"Ａ賞は５０００円分のビール券！\n\0":
'???',

# Misato Katsuragi 
"あ、ビール券はいいわね〜。\nでも、いつも集め損なうのよね、\nこういうクーポンものって。▽\nウチのビールとジュースに\nシール付いてたかも〜。\n\0":
'???',

# T.V. Commercial
"Ｂ賞は今大人気の犬のモカちゃんの\n動く、喋る、芸をするヌイグルミ！▽\nＣ賞は人気お笑い芸人「生爪」の\n特製ストラップ！！\n\0":
'???',

# Pen Pen
"………ギャ！？\n\0":
'???',

# Misato Katsuragi 
"あっ、さっきのワンコ。\nあの、ミョーなストラップ。\n欲しい人いるのかしら？\n\0":
'???',

# Pen Pen
"グワグワ、グワッ！\n\0":
'???',

# [Text Only - No Designated Speaker]
"ペンペンは思った。\nジュースのシールを集めれば、\nあの犬が来て幸せになれるのだ。\n\0":
'???',

#
# ./USRDIR/event/cev1606.har_EXTRACT/cev1606.evs
#
# [Text Only - No Designated Speaker]
"また、振り出しに戻った…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"包みを開けると、\nお笑い芸人「生爪」の\nストラップが入っていた。\n\0":
'???',

# Pen Pen
"…クゥア〜〜〜。\n\0":
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
'Hey!!\nPen Pen, honestly! Quit it!!\n\0',

# Shinji Ikari
"や、やめろよ。\nペンペン〜！！\n\0":
'C-Cut it out,\nPen Pen!!\n\0',

# Asuka Soryu Langley
"ぎゃー、何すんの！？\nよしてよ、ペンペン。\n\0":
'???',

# Ritsuko Akagi 
"ペンペン、何をするの！\nおやめなさい！！\n\0":
'Pen Pen, what are you doing?\nStop that at once!\n\0'

#
# ./USRDIR/event/cev1701.har_EXTRACT/cev1701.evs
#
# [Text Only - No Designated Speaker]
"この世界を選んだあなたは、\n絶望的な状況に愕然とするだろう。▽\nだが、あなたは、この困難を\n乗り越え、使徒の手から人類を\n守らなければならない。\n\0":
'???',

#
# ./USRDIR/event/f000.har_EXTRACT/f000.evs
#
# Shinji Ikari
"使徒、襲来\n\0":
'???',

# Shinji Ikari
"でも、この世界が好き\n\0":
'???',

# Hikari Horaki
"（どうしよう、渡さなきゃ。\n　鈴原の為に作ったお弁当…。\n　早く渡さなきゃ、行っちゃう…。）\n\0":
'???',

# Hikari Horaki
"（ひょっとしたら、\n　もう会えなくなるかもしれない。）\n\0":
'???',

# Rei Ayanami 
"国２３４５６７８９０１２３４５６、\n１２３４５６７８９０１２３４５６、\n１２３４５６７８９０１２３４５６、\n\n\0":
'???',

# Kyoko Soryu Zeppelin 
"国２３４５６７８９０１２３４５６、\n１２３４５６７８９０１２３４５６、\n１２３４５６７８９０１２３４５６、\n\0":
'???',

# Shinji Ikari
"シンジ／通常／\n\0":
'???',

# Shinji's Shadow [Leliel]
"シンジ２／通常／\n\0":
'???',

# Shinji's Shadow [Leliel]
"シンジ２／怒り／\n\0":
'???',

# Shinji's Shadow [Leliel]
"シンジ２／悲しみ／\n\0":
'???',

# Shinji's Shadow [Leliel]
"シンジ２／笑い／\n\0":
'???',

# Shinji's Shadow [Leliel]
"シンジ２／真剣／\n\0":
'???',

# Shinji's Shadow [Leliel]
"シンジ２／発情／\n\0":
'???',

# Shinji's Shadow [Leliel]
"シンジ２／困惑／\n\0":
'???',

# Asuka's Shadow [Leliel]
"アスカ２／通常／\n\0":
'???',

# Asuka's Shadow [Leliel]
"アスカ２／怒り／\n\0":
'???',

# Asuka's Shadow [Leliel]
"アスカ２／悲しみ／\n\0":
'???',

# Asuka's Shadow [Leliel]
"アスカ２／笑い／\n\n\0":
'???',

# Asuka's Shadow [Leliel]
"アスカ２／真剣／\n\0":
'???',

# Asuka's Shadow [Leliel]
"アスカ２／発情／\n\0":
'???',

# Asuka's Shadow [Leliel]
"アスカ２／困惑／\n\0":
'???',

# Rei's Shadow [Leliel]
"レイ２／通常／\n\0":
'???',

# Rei's Shadow [Leliel]
"レイ２／怒り／\n\0":
'???',

# Rei's Shadow [Leliel]
"レイ２／悲しみ／\n\0":
'???',

# Rei's Shadow [Leliel]
"レイ２／笑い／\n\0":
'???',

# Rei's Shadow [Leliel]
"レイ２／真剣／\n\0":
'???',

# Rei's Shadow [Leliel]
"レイ２／発情／\n\0":
'???',

# Rei's Shadow [Leliel]
"レイ２／困惑／\n\0":
'???',

# Toji's Shadow [Leliel]
"トウジ２／通常／\n\0":
'???',

# Toji's Shadow [Leliel]
"トウジ２／怒り／\n\0":
'???',

# Toji's Shadow [Leliel]
"トウジ２／悲しみ／\n\0":
'???',

# Toji's Shadow [Leliel]
"トウジ２／笑い／\n\0":
'???',

# Toji's Shadow [Leliel]
"トウジ２／真剣／\n\0":
'???',

# Toji's Shadow [Leliel]
"トウジ２／発情／\n\0":
'???',

# Toji's Shadow [Leliel]
"トウジ２／困惑／\n\0":
'???',

# Kaworu's Shadow [Leliel]
"カヲル２／通常／\n\0":
'???',

# Kaworu's Shadow [Leliel]
"カヲル２／怒り／\n\0":
'???',

# Kaworu's Shadow [Leliel]
"カヲル２／悲しみ／\n\0":
'???',

# Kaworu's Shadow [Leliel]
"カヲル２／笑い／\n\0":
'???',

# Kaworu's Shadow [Leliel]
"カヲル２／真剣／\n\0":
'???',

# Kaworu's Shadow [Leliel]
"カヲル２／発情／\n\0":
'???',

# Kaworu's Shadow [Leliel]
"カヲル２／困惑／\n\0":
'???',

# Shinji Ikari
"１２３４５６７８９０１２３４５６、\n１２３４５６７８９０１２３４５６、\n１２３４５６７８９０１２３４５６、\n\0":
'???',

# Shinji Ikari
"出張計画書の内容に従い、事\n出張計画書の内容に従い、事\n出張計画書の内容に従い、事\n\0":
'???',

# Shinji Ikari
"使徒襲来\n１２３４５６７８９０１２３４５６、▽\n出張計画書の内容に従い、\nアメリカへ出張した。▽\n現地の技術者の話を\n色々と聴いてまわった。▽\n話によると、\nΣ機関の研究は実験段階にまで\nこぎつけているらしい。▽\nΣ機関の安定性が保証できれば、\nいつでも実験に入れるとの事だった。▽\nネルフ本部で入手した\nΣ機関に関する資料を風にまいた。\n\0":
'???',

# Shinji Ikari
"その書類はバラバラに、\n空高く舞い上がっていった。▽\nではトウジくん、始めるわよ。▽\n第一次接続開始…、\n起動用システム作動…、\n稼働電圧臨界…、▽\nケイジ内で使徒の反応あり、\nエヴァ参号機が発信源です！▽\nかまわん、射出だ。\nエヴァンゲリオン参号機は現時刻を\n持って破棄、目標を使徒と識別する。\n\0":
'???',

# Shinji Ikari
"エヴァ参号機が起動実験中に\n使徒の寄生により暴走。▽\n現在参号機は地上に射出。\nこれより迎撃の用意に入ります。\n戦闘配置についてちょうだい！▽\n父さんを待っていた。\n一緒に母さんの墓参りに\n行く事になっていたからだ。▽\n母さんは、どんな人だったんだろう。\nどんな顔をしていたんだろう。▽\n僕は知らなくても、\n父さんは知っているんだ…。▽\n人は思い出を忘れる事で\n生きて行ける。▽\nだが、\n決して忘れてはならない事もある。▽\nユイはそのかけがえのないものを\n教えてくれた。\n\0":
'???',

# Shinji Ikari
"私は、その確認をする為に\nここに来ている。▽\n人は思い出を忘れる事で\n生きて行ける。▽\nだが、\n決して忘れてはならない事もある。▽\nユイはそのかけがえのないものを\n教えてくれた。▽\n私は、その確認をする為に\nここに来ている。▽\n憂鬱、エヴァ、第３新東京市、\n人類補完計画、葛城、畳、掲示、\nおしまい。\n\n\0":
'???',

# Shinji Ikari
"９機…、\nどう考えたって不利だ…。\n\n\0":
'???',

# Ritsuko Akagi 
"リツコ普通\n\0":
'Ritsuko Normal\n\0',

# Naoko Akagi
"ゲスト（赤木ナオコ）\n\0":
'Guest (Naoko Akagi)\n\0',

# Ritsuko Akagi [Flashback], Ritsuko Akagi 
"リツコ：回想普通\n\0":
'Ritsuko: Flashback Normal\n\0',

# Naoko Akagi
"ゲスト（回想赤木ナオコ）\n\0":
'Guest (Flashback Naoko Akagi)\n\0',

# Rei Ayanami 
"０（ゼロ）とＯ（オー）\n\0":
'0 (Zero) and O (Oh)\n\0',

# Misato Katsuragi, Misato Katsuragi [Flashback]
"ミサト：回想普通\n\0":
'Misato: Flashback Normal\n\0',

# Misato Katsuragi, Misato Katsuragi [Flashback]
"ミサト：回想悲しみ\n\0":
'???',

# Maya Ibuki, Maya Ibuki [Flashback]
"マヤ：回想普通\n\0":
'Maya: Flashback Normal\n\0',

# Maya Ibuki, Maya Ibuki [Flashback]
"マヤ：回想笑い\n\0":
'???',

# Maya Ibuki, Maya Ibuki [Flashback]
"マヤ：回想発情\n\0":
'???',

# Makoto Hyuga, Makoto Hyuga [Flashback]
"日向：回想笑い\n\0":
'???',

# Makoto Hyuga, Makoto Hyuga [Flashback]
"日向：回想発情\n\0":
'???',

# Pen Pen
"ペンペン：ネガポジ驚き\n\0":
'???',

# Shinji Ikari
"Ｐ普通\n\0":
'P Normal\n\0',

# Shinji Ikari, Asuka Soryu Langley, Rei Ayanami,Toji Suzuhara, Kaworu Nagisa
"Ｐ真剣\n\0":
'???',

# Shinji Ikari
"Ｐダメージ\n\0":
'P Damage\n\0',

# Shinji Ikari
"Ｐ俯き\n\0":
'???',

# Shinji Ikari
"Ｐ雄叫び\n\0":
'???',

# Shinji Ikari
"Ｐダメージ制服\n\0":
'???',

# Shinji Ikari
"Ｐ俯き制服\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Rei Ayanami, Toji Suzuhara, Kaworu Nagisa
"プラグスーツ普通\n\0":
'Plugsuit Normal\n\0',

# Shinji Ikari, Asuka Soryu Langley, Rei Ayanami, Toji Suzuhara
"プラグスーツ真剣\n\0":
'???',

# Shinji Ikari
"制服コネクター通常\n\0":
'???',

# Shinji Ikari
"赤プラグスーツ通常\n\0":
'???',

# Asuka Soryu Langley
"サマードレス普通\n\0":
'Summer Dress Normal\n\0',

# Asuka Soryu Langley
"サマードレス笑い\n\0":
'???',

# Asuka Soryu Langley
"サマードレス怒り\n\0":
'Summer Dress Angry\n\0',

# Rei Ayanami 
"ハダカ普通\n\0":
'Naked Normal\n\0',

# Kaworu Nagisa 
"プラグスーツ真剣\n\n\0":
'???',

# [Text Only - No Designated Speaker]
"ΘΑ戦失敗\n\0":
'???',

# Shigeru Aoba
"なんかセリフ\n\0":
'???',

# [Text Only - No Designated Speaker]
"イベント９５に分岐\n\0":
'???',

# [Text Only - No Designated Speaker]
"クロスフェード普通\n\0":
'Crossfade Normal\n\0',

# [Text Only - No Designated Speaker]
"クロスフェード早く\n\0":
'Crossfade Fast\n\0',

# Shinji Ikari
"通常の表情変更\n\0":
'???',

# Shinji Ikari
"次、クロスフェードしない\n\0":
'???',

# Shinji Ikari
"どお？\n\0":
'???',

# Shinji Ikari [Flashback]
"回想シンジ\n\0":
'Flashback Shinji\n\0',

# Misato Katsuragi [Flashback]
"回想ミサト\n\0":
'Flashback Misato\n\0',

# Gendo Ikari [Flashback]
"回想ゲンドウ\n\0":
'Flashback Gendo\n\0',

# Kozo Fuyutsuki [Flashback]
"回想冬月\n\0":
'Flashback Fuyutsuki\n\0',

# Ritsuko Akagi [Flashback]
"回想リツコ\n\0":
'Flashback Ritsuko\n\0',

# Maya Ibuki [Flashback]
"回想マヤ\n\0":
'Flashback Maya\n\0',

# Makoto Hyuga [Flashback]
"回想日向\n\0":
'Flashback Hyuga\n\0',

# Shigeru Aoba [Flashback]
"回想青葉\n\0":
'Flashback Aoba\n\0',

# Yui Ikari [Flashback]
"回想ユイ\n\0":
'Flashback Yui\n\0',

# Seele 01
"ゲスト（０１）\n\0":
'Guest (01)\n\0',

# Kensuke Aida [Flashback]
"回想ケンスケ\n\0":
'Flashback Kensuke\n\0',

# Shinji Ikari
"シンジ\n\0":
'Shinji\n\0',

# Asuka Soryu Langley
"アスカ\n\0":
'???',

# Rei Ayanami 
"レイ\n\0":
'???',

# Misato Katsuragi 
"ミサト\n\0":
'???',

# Gendo Ikari
"ゲンドウ\n\0":
'???',

# Kozo Fuyutsuki
"冬月\n\0":
'???',

# Ritsuko Akagi 
"リツコ\n\0":
'???',

# Maya Ibuki 
"マヤ\n\0":
'???',

# Makoto Hyuga
"日向\n\0":
'???',

# Shigeru Aoba
"青葉\n\0":
'???',

# Ryoji Kaji
"加持\n\0":
'???',

# Hikari Horaki
"ヒカリ\n\0":
'???',

# Toji Suzuhara 
"トウジ\n\0":
'???',

# Kensuke Aida
"ケンスケ\n\0":
'???',

# Kaworu Nagisa 
"カヲル\n\0":
'???',

# Pen Pen
"ペンペン\n\0":
'???',

# Male Staff
"ダミーくん\n\0":
'Dummy-kun\n\0',

# Female Staff
"ダミーさん\n\0":
'Dummy-san\n\0',

# Clerk
"店員\n\0":
'???',

# Keel Lorenz
"キール\n\0":
'???',

# Shiro Tokita
"時田\n\0":
'Tokita\n\0',

# Yui Ikari
"ユイ\n\0":
'???',

# Keel Lorenz
"ゲスト（キール）\n\0":
'???',

# Shiro Tokita
"ゲスト（時田）\n\0":
'Guest (Tokita)\n\0',

# Yui Ikari
"ゲスト（ユイ）\n\0":
'???',

# [Text Only - No Designated Speaker]
"アナ\n\0":
'Announcement\n\0',

# [Text Only - No Designated Speaker]
"ナレ\n\0":
'Narration\n\0',

# [Text Only - No Designated Speaker]
"（ナレ）\n\0":
'(Narration)\n\0',

# Kensuke's Father
"ゲスト（ケンスケパパ）\n\0":
'???',

# Toji's Sister
"ゲスト（トウジの妹）\n\0":
'???',

# T.V. Talent
"ゲスト（テレビの女性の声）\n\0":
'???',

# Nursing Staff
"ゲスト（男）\n\0":
'Guest (Man)\n\0',

# Psychiatrist
"ゲスト（精神科男）\n\0":
'???',

# Baby's Mother
"ゲスト（母親）\n\0":
'Guest (Mother)\n\0',

# Female Classmate
"ゲスト（クラス女子１）\n\0":
'???',

# Female Classmate
"ゲスト（クラス女子２）\n\0":
'???',

# Female Classmate
"ゲスト（クラス女子３）\n\0":
'???',

# Announcement
"ゲスト（アナウンス女性ボイス）\n\0":
'???',

# Teruo Kato
"ゲスト（テルオ）\n\0":
'???',

# Female Announcer
"ゲスト（女子アナ）\n\0":
'???',

# Committeeman A
"ゲスト（委員会Ａ）\n\0":
'???',

# Committeeman B
"ゲスト（委員会Ｂ）\n\0":
'???',

# Committeeman C
"ゲスト（委員会Ｃ）\n\0":
'???',

# Committeeman D
"ゲスト（委員会Ｄ）\n\0":
'???',

# Seele 02
"ゲスト（０２）\n\0":
'???',

# Seele 03
"ゲスト（０３）\n\0":
'???',

# Seele 04
"ゲスト（０４）\n\0":
'???',

# Seele 05
"ゲスト（０５）\n\0":
'???',

# Seele 06
"ゲスト（０６）\n\0":
'???',

# Seele 09
"ゲスト（０９）\n\0":
'???',

# JSSDF Staff
"ゲスト（戦自隊員）\n\0":
'???',

# Radio Voice [JSSDF]
"ゲスト（戦自隊員・無線）\n\0":
'???',

# Local Announcement
"ゲスト（館内アナウンス）\n\0":
'???',

# Girlfriends
"ゲスト（女友達）\n\0":
'???',

# Matsushiro Staff
"ゲスト（松代職員）\n\0":
'???',

# Toji Suzuhara 
"この後「ＢＧＭ：０６」\n\0":
'???',

# Toji Suzuhara
"この後「ＢＧＭ：ストップ」\n\0":
'???',

# Asuka Soryu Langley, Shinji Ikari
"この後「ＢＧＭ：０４」\n\0":
'???',

# Asuka Soryu Langley
"この後「ＢＧＭ：フェードアウト」\n\0":
'???',

# Shinji Ikari
"この後\n「ＢＧＭ：フェードアウト 120」\n\0":
'???',

# Toji Suzuhara
"ランダムなパイロットのセリフ\n\n\0":
'Random Pilot Dialogue\n\0',

# Asuka Soryu Langley, Shinji Ikari, Kaworu Nagisa
"ランダムなパイロットのセリフ\n\0":
'Random Pilot Dialogue\n\0',

# Toji Suzuhara
"重要なパイロットのセリフ\n\n\0":
'Important Pilot Dialogue\n\n\0',

# Asuka Soryu Langley, Shinji Ikari, Kaworu Nagisa
"重要なパイロットのセリフ\n\0":
'Important Pilot Dialogue\n\n\0',

# Toji Suzuhara
"パイロットのセリフ（上位優先）\n\n\0":
'???',

# Asuka Soryu Langley, Shinji Ikari, Kaworu Nagisa
"パイロットのセリフ（上位優先）\n\0":
'???',

# Toji Suzuhara
"以下のキャラのセリフ（ランダム）\n\n\0":
'???',

# Asuka Soryu Langley, Shinji Ikari, Kaworu Nagisa
"以下のキャラのセリフ（ランダム）\n\0":
'???',

# Shigeru Aoba
"次のセリフは青葉の声付き\n\0":
'???',

# Makoto Hyuga
"%1iボタン、%2iボタン、\n%3iボタン、%4iボタン。\n\0":
'%1i Button, %2i Button, \n%3i Button, %4i Button.\n\0',

# Rei Ayanami 
"エロテスト（大）\n\0":
'???',

# Shinji Ikari
"エロ？\n\0":
'???',

# Ritsuko Akagi 
"普通？\n\0":
'Normal?\n\0',

# Ritsuko Akagi 
"外普通？\n\0":
'???',
}
