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
# ./USRDIR/event/f059.har_EXTRACT/f059.evs
#
# [Text Only - No Designated Speaker]
"ふと、ミサトの声が\n聞こえた気がした。\n\0":
'???',

# Shinji Ikari
"僕を、利用したんでしょう？\n自分の心の隙間をごまかすために\n僕を引き取ったんでしょう？\n\0":
'???',

# Misato Katsuragi 
"それは…、違うわ。\n決してそんなつもりで一緒に\n暮らしているわけじゃないわ。\n\0":
'???',

# Asuka Soryu Langley
"とかなんとか言っちゃって。\n男を利用して生きているじゃないの。▽\nしかも、\n自分の寂しさを紛らわすために。\n\0":
'???',

# Ritsuko Akagi 
"そうよ、あなたはいつもそう。\n誰かにしがみつかないと\n生きていけない。▽\n寂しい、見つめて欲しいと思う心が\n今のあなたを作っているのよ。\n楽しそうな自分を演じているの。\n\0":
'???',

# Misato Katsuragi 
"…不安なのよ。\n独りでいるのは不安なのよ。\n\0":
'???',

# Ryoji Kaji
"俺も、寂しさの埋め合わせ\nだったのか？\n\0":
'???',

# Misato Katsuragi 
"そんなことない…。\nでも、誰かが側にいてくれないと\n自分の形を確かめられないの。\n\0":
'???',

# Misato Katsuragi 
"不安…。▽\n不安なの…。▽\n不安なんだわ…。\nまた、しばらく、不安なんだわ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le119.evs
#
# Shinji Ikari
"僕は誰も傷つけてない。\n何も言っていない。\n\0":
'???',

# Shinji's Shadow [Leliel]
"そうやって、\n他人と距離をおこうとしてる。▽\nまず、それで誰かを傷つけている。\n自分自身もね。\n\0":
'???',

#
# ./USRDIR/event/tev1401.har_EXTRACT/tev1401.evs
#
# Makoto Hyuga
"しかし、シンジ君。\nああしなければ、\n君がやられていたぞ。\n\0":
'???',

# Shigeru Aoba
"今の彼なら、\nやりかねませんね。\n\0":
'???',

# Intelligence Agent
"出たまえ、碇シンジ君。\n総司令がお会いになる。\n\0":
'???',

# Gendo Ikari
"来たか、シンジ。\n\0":
'???',

# Gendo Ikari
"さて…、▽\n命令違反、エヴァの私的所有、\n稚拙な恫喝。\nこれらは全て犯罪行為だ。\n\0":
'???',

# Gendo Ikari
"何か言いたい事があるか？\n\0":
'???',

# Shinji Ikari
"はい。▽\n僕はもう、エヴァには\n乗りたくありません。\nここにも居たくありません。\n\0":
'???',

# Gendo Ikari
"では、出ていけ。\n\0":
'???',

# Shinji Ikari
"はい。\nもと居たところに帰ります。\n\0":
'???',

# Gendo Ikari
"また逃げ出すのか。\n\0":
'???',

# Gendo Ikari
"お前には失望した。\nもう会う事もあるまい。\n\0":
'???',

# Shinji Ikari
"はい、そのつもりです。\n\0":
'???',

# Shinji Ikari
"今まで…お世話になりました。\n\0":
'???',

# Misato Katsuragi 
"本当に出ていくの？\nもう一度考え直す事は…。\n\0":
'???',

# Shinji Ikari
"いいえ、それはありませんよ。\n\0":
'???',

# Misato Katsuragi 
"そうやって、\n愛想ばっかりついてると\nこれから先、辛いわよ。\n\0":
'???',

# Shinji Ikari
"それはミサトさんの生き方です。\n僕には出来ません。\n\0":
'???',

# Misato Katsuragi 
"わかってると思うけど、\nこれから先、あなたの行動には\nかなりの制限がつくから。\n\0":
'???',

# Shinji Ikari
"はい。あの…。\n\0":
'???',

# Shinji Ikari
"一つだけ教えてください。\n何故、トウジなんですか？\nフォース・チルドレンが。\n\0":
'???',

# Misato Katsuragi 
"第４次選抜候補者は、\n全てあなたのクラスメイト\nだったのよ。▽\n私も最近知ったわ。\n全て仕組まれていた事だったのよ。\n\0":
'???',

# Shinji Ikari
"みんなが…クラスのみんなが。\n\0":
'???',

# Misato Katsuragi 
"鈴原君の事はいくら言葉で謝っても\n「ごめん」で取り消される\nミスではないわ。\n\0":
'???',

# Misato Katsuragi 
"でも、シンジ君。\n正直、私はあなたに自分の夢、\n願い、目的を重ねていたわ。▽\nそれが、あなたの\n重荷になっているのも知ってる。▽\nでも私達は、ネルフの皆は、\nあなたに未来を託すしか\nなかったのよ。▽\nそれだけは覚えておいてね。\n\0":
'???',

# Shinji Ikari
"勝手な言い分ですね。\n\0":
'???',

# Misato Katsuragi 
"それはわかってるわ。▽\n本部までのパスコードと\nあなたの部屋は\nそのままにしておくから。\n\0":
'???',

# Shinji Ikari
"無駄ですよ。\n片付けておいてください。\n僕はもう、エヴァには乗りません。\n\0":
'???',

#
# ./USRDIR/event/cev0204.har_EXTRACT/cev0204.evs
#
# Asuka Soryu Langley
"あ〜ぁ、なんか面白いの、\nやってないかな…。\n\0":
'???',

# Pen Pen
"グワ。\n\0":
'???',

# T.V. Talent
"それじゃ次のお悩み、行きましょう。\n恋のお悩みのようですね。▽\nえー、私は好きな人が２人います。\nどっちも好きで選べません。\n\0":
'???',

# Asuka Soryu Langley
"………バッカみたい。\nそれって、どっちも好きじゃ\nないんじゃない。\n\0":
'???',

# T.V. Talent
"どっちも選べないけど、２人には\n私の事を好きになって欲しいんです。\nどうすればいいんでしょうか？\n\0":
'???',

# Asuka Soryu Langley
"だったら、飛びっきりの\n美人にならない限り無理ね。\nそしたら嫌でも群がって来るわよ。\n\0":
'???',

# T.V. Talent
"まあ付き合ってみないと見えて\nこない事もあるから、２人とも\n友達として様子を見るとか…。\n\0":
'???',

# Asuka Soryu Langley
"それか男にとって、\n都合のいい女になる事ね。\nもっとも惨めな生き方よ。▽\nそれにしても、どーしてこんな\nいい加減なアドバイスするのよ。\n\0":
'???',

# Pen Pen
"グーワ？\n\0":
'???',

# Asuka Soryu Langley
"パパだって、今のママのために\n変わってしまった。\nみんな、みんな変わってく。▽\n私は誰かのために生きるなんて\n絶対イヤ。▽\n好かれるために、自分自身を\n押し殺すなんて馬鹿げてる。\n一人で生きる方がマシよ。\n\0":
'???',

# Pen Pen
"グワッ…。\n\0":
'???',

# Asuka Soryu Langley
"アンタはさ、生きているだけで\n好かれてるんだから。\n心配しなくってもいいわよ。\n\0":
'???',

# T.V. Talent
"そういえば知ってる？\n独り言多い人は、\n寂しがりやなんだって。\n\0":
'???',

# Asuka Soryu Langley
"ヤな気分、もう寝るわよ。\n\0":
'???',

# Asuka Soryu Langley
"ママ…。\n私の本当のママ…。\n\0":
'???',

# Asuka Soryu Langley
"ママ…、こっち向いて。\n私、選ばれたんだよ。\n人類を守るエリートパイロットに。▽\nママ！！　ママ！！\n\0":
'???',

# Kyoko Soryu Zeppelin 
"アスカちゃん。\nママね、今日はあなたの\n大好物を作ったよ。\n\0":
'???',

# Kyoko Soryu Zeppelin 
"ほら、好き嫌いしていると\nあそこのお姉ちゃんに笑われますよ。\n\0":
'???',

# Asuka Soryu Langley
"ママ、こっちを向いて。\nその人形は私じゃない。\n私はここよ。▽\nママ…！！\n\0":
'???',

# Asuka Soryu Langley
"ママ、何で死んじゃったの…？\nどうして…私を置いて…。\nママ………。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le207.evs
#
# Asuka Soryu Langley
"ママは私を捨てたの？\n\0":
'???',

# Asuka's Shadow [Leliel]
"ママは、\n自分の中の私を愛していたわ。\nそれだけよ。\n\0":
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
# ./USRDIR/event/tev0901.har_EXTRACT/tev0901.evs
#
# Makoto Hyuga
"かなりの巨体ですね。\n\0":
'???',

# Misato Katsuragi 
"サイケデリックなクモね。\n虫酸が走るわ。\n\0":
'???',

# Misato Katsuragi 
"ずいぶん地味な方法ね。\nでも、そうはさせないわ。▽\nエヴァ、発進準備！！\n\0":
'???',

# Maya Ibuki, Male Staff
"あの、目のようなところから、\n何か液体らしきものが流れています。\n\0":
'???',

# Ritsuko Akagi 
"液体が落ちた箇所が腐食しているわ。▽\nどうやら使徒の武器は、\nあの強力な溶解液のようね。\n\0":
'???',

# Misato Katsuragi 
"タラタラおツユ流しちゃって\n下品な攻撃だこと。\n\0":
'???',

# Shigeru Aoba
"直上を目指しているという事は…。\nあの液を使って、ジオフロントに\n侵入するつもりか…！？\n\0":
'???',

#
# ./USRDIR/event/tev0223.har_EXTRACT/tev0223.evs
#
# Misato Katsuragi 
"ホラ、「椅子に座る」という\n行動が出たでしょ？\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le116.evs
#
# Shinji Ikari
"怖いのは…。\n他人からはどう映ってるか\nわかりっこないから。▽\n僕も、他人の中の僕も\n一緒かもしれないけど。▽\n他人からの見方は違うもの。\nわからないから、怖いんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"でも、他人の中の自分を\nまざまざと見れたとしても、\n恐怖は取り除かれはしないよ。▽\n君は、他人に心を覗かれても\n怖くはない？\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le501.evs
#
# Kaworu Nagisa 
"フフフ、決まってるだろう？\n彷徨った魂が、本来の肉体に宿る…。\nつまりアダムに還る事さ。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"構わないのかい？\n君が交じるリリン達の多くを、\n裏切る結果になってしまうだろう。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le214.evs
#
# Asuka Soryu Langley
"イヤよ…、一人で苦しむのは嫌…。\nどうすれば\n他人に気が付いてもらえるの？\n\0":
'???',

# Asuka's Shadow [Leliel]
"すべてを捨ててしまえば、\n哀れんでもらえる…。▽\nでもあなたは\n何も手放したくないのでしょ？\n\0":
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
# ./USRDIR/event/tev1206.har_EXTRACT/tev1206.evs
#
# Misato Katsuragi, Rei Ayanami
"動かないで。\n\0":
'Don\'t move.\n\0',

# Ryoji Kaji
"よォ、君か…。\n\0":
'???',

# Misato Katsuragi 
"これがあなたの本当の仕事？\nそれともアルバイトかしら？\n\0":
'???',

# Ryoji Kaji
"どっちかな？\n\0":
'???',

# Misato Katsuragi 
"特務機関ネルフ、\n特殊監査部所属、加持リョウジ。▽\n同時に日本政府内務省、\n調査部所属、\n加持リョウジでもあるわけね。\n\0":
'???',

# Ryoji Kaji
"君にもバレバレか。\n\0":
'???',

# Misato Katsuragi 
"ネルフを甘く見ないで！\n\0":
'???',

# Ryoji Kaji
"碇司令の命令かい？\n\0":
'???',

# Misato Katsuragi 
"いいえ、私の独断よ。\nこれ以上、バイトを続けると\n死ぬわ。\n\0":
'???',

# Ryoji Kaji
"碇司令は俺を利用してる。\nまだ、いけるさ。▽\nだが、君に\n隠し事をしていたのは謝るよ。\nただね…、▽\n碇司令やリッちゃんは\n君に隠し事をしている。\nそれがこれさ。\n\0":
'???',

# Misato Katsuragi 
"…………！？▽\nこれは………？\n\0":
'???',

# Misato Katsuragi 
"エヴァ…、いえ、まさか…。\n\0":
'???',

# Ryoji Kaji
"そう。\n人類補完計画、Ｅ計画、\nその全ての要であり、▽\nあのセカンドインパクトを\n起こした物体「アダム」だ。\n\0":
'???',

# Misato Katsuragi 
"第壱使徒…、\nアダムがここに？\n\0":
'???',

# Misato Katsuragi 
"確かに、\nネルフは私が考えているほど\n甘くないわね。\n\0":
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
# ./USRDIR/event/cev0203.har_EXTRACT/cev0203.evs
#
# Shinji Ikari
"いけない、電話鳴ってる。\nはい、もしもし。\n\0":
'???',

# Shinji Ikari
"何語？\nこれ、アスカにかな…？▽\nアスカ、いる？\nひょっとして、家族なんじゃない？\n\0":
'???',

# Misato Katsuragi 
"おっと、電話電話…。\nはいはーい、もしもしー？▽\n…ああ、\nイヒ・ビン・カツラギ。▽\nアスカー、\nドイツのお母さんからよ。\n\0":
'???',

# Asuka Soryu Langley
"いないって言って。\n出たくないの。\n\0":
'???',

# Shinji Ikari
"せっかくの電話なのに。\nどうしたんだよアスカ…。\n\0":
'???',

# Misato Katsuragi 
"んもう、しょうがない子ね。\n\0":
'???',

# Asuka Soryu Langley
"………後で、私から\nかけるからほっといて！\n\0":
'???',

#
# ./USRDIR/event/f009.har_EXTRACT/f009.evs
#
# Kaworu Nagisa 
"やあ、君かい。▽\nちょっと付き合って\nもらえるかな…？\n\0":
'???',

# Kaworu Nagisa 
"今日は君に、面白いものを\n見せてあげたいんだ。\n\0":
'???',

# Shinji Ikari
"僕に…？\n\0":
'???',

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
'???',

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
'???',

# Rei Ayanami 
"あれはエヴァ、四号機…。\n\0":
'???',

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
'???',

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
# ./USRDIR/event/tev1601.har_EXTRACT/tev1601.evs
#
# Ritsuko Akagi 
"聞こえる、アスカ？\nシンクロ率が低下してるわよ。\nいつも通り、余計な事を考えずに。\n\0":
'???',

# Asuka Soryu Langley
"やってるわよ！！\n\0":
'???',

# Maya Ibuki 
"最近のアスカのシンクロ率、\n下がる一方ですね。\n\0":
'???',

# Ritsuko Akagi 
"困ったわね、\nこの余裕のない時に。\n\0":
'???',

# Misato Katsuragi 
"無理ないわよ。\nあんな負け方しちゃ。▽\n…というより、\nシンジ君に負けたと\n思い込んでる方が大きいわね。\n\0":
'???',

# Asuka Soryu Langley
"人類を守る、エリートパイロット。▽\nなのに…。▽\n使徒を倒してきたのは、\nほとんどがあのバカシンジ。▽\n私…、……………。▽\nママ………。\n\0":
'???',

# Maya Ibuki 
"シンクログラフ、\n起動指数ギリギリです。\n\0":
'???',

# Ritsuko Akagi 
"そう…。\n弐号機のコア、\n変更もやむなしかしらね。\n\0":
'???',

# Misato Katsuragi 
"あのアダムより生まれしモノ、\nエヴァシリーズ。▽\nセカンドインパクトを引き起こした\n原因たるものを流用しなければ、\n私達は使徒に勝てない。▽\n逆に生きるためには、\n自分達を滅ぼそうとしたものをも\n利用する。▽\nそれが人間なのね。\nやはり、私はエヴァを\n憎んでいるのかもしれない。▽\n父の仇か。\n\0":
'???',

# Makoto Hyuga
"葛城さん。\n\0":
'???',

# Misato Katsuragi 
"エヴァ拾参号機までの建造を開始？\n世界７箇所で？\n\0":
'???',

# Makoto Hyuga
"上海経由の情報です。\nソースに信頼はおけます。\n\0":
'???',

# Misato Katsuragi 
"何故この時期に、\n量産を急ぐの？\n\0":
'???',

# Makoto Hyuga
"エヴァを過去に２機も失い、\n現在は２機も大破ですから。▽\n第２次整備に向けて、予備戦力の\n増強を急いでいるのでは？\n\0":
'???',

# Misato Katsuragi 
"どうかしら。▽\nここにしても、\nドイツで建造中の伍、六号機の\nパーツを回してもらってるのよ。▽\n最近、随分と金が動いているわね。\n\0":
'???',

# Makoto Hyuga
"ここに来て予算倍増ですからね。\nそれだけ上も切羽詰っているって\n事でしょうか。\n\0":
'???',

# Misato Katsuragi 
"委員会の焦りらしきものを\n感じるわね。\n\0":
'???',

# Makoto Hyuga
"では、委員会が今までのように\n単独ではなく、複数同時展開の\nケースを設定したものでしょうか？\n\0":
'???',

# Misato Katsuragi 
"そうね。\nでも、非公式に行う理由がないわ。\n何か別の目的があるのよ。\n\0":
'???',

#
# ./USRDIR/event/tev1202.har_EXTRACT/tev1202.evs
#
# Toji Suzuhara 
"あーもー、今日は日直や…。\nしかも、こんな般若娘と一緒やがな。\n\0":
'???',

# Asuka Soryu Langley
"私だって、アンタみたいな猿と\n組むのはゴメンよ。\n\0":
'???',

# Asuka Soryu Langley
"でェ、シンジ。\nハンニャって何よ？\n\0":
'???',

# Kensuke Aida
"オッソロシイ顔した鬼女って\nイミだよ。\n\0":
'???',

# Asuka Soryu Langley
"ハァ？\n目ェ腐ってんじゃないの？\n\0":
'???',

# Asuka Soryu Langley
"この私のどこ見て、\n鬼女なんて言ってんのよ！\n\0":
'???',

# Toji Suzuhara 
"ほーれ、その顔じゃ。\nそのうち、ツノ生えてくるんと\nちゃうか〜、般若〜！\n\0":
'???',

# Hikari Horaki
"バカ鈴原！！\nまた騒いだりして！！\n\0":
'???',

# Toji Suzuhara 
"おわっ、般若が増えた！？\nこうなったら、\n逃げるが勝ちや！！\n\0":
'???',

# Hikari Horaki
"あっ、鈴原っ！\n逃げ足ばっかり速いんだから！\n\0":
'???',

# Shinji Ikari
"委員長…どうしたの？\n\0":
'???',

# Hikari Horaki
"え、ううん…。\n\0":
'???',

# Asuka Soryu Langley
"ちょっと、バカシンジ。\n察してやんなさいよ。\nヒカリはね…。\n\0":
'???',

# Hikari Horaki
"あ、わ、私…、\nいつも怒ってばっかりだから、\n般若なんて言われても仕方が無いし。\n\0":
'???',

# Shinji Ikari
"どうして、顔が赤いの？\n\0":
'???',

# Asuka Soryu Langley
"アンタ、バカァ？\nまったくもー…、ドンカン！\n\0":
'???',

# Shinji Ikari
"…？\nえぇぇ？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le515.evs
#
# Kaworu Nagisa 
"…何だろうね…。\nフフ、思い出せないよ。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"ごまかしているね。\n本当はわかってるんだろ？\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le008.evs
#
# Shinji Ikari
"会いたい。▽\nもう、一度。\n\0":
'???',

# Kyoko Soryu Zeppelin 
"あなたを待っている人がいるわ。\n\0":
'???',

# Kyoko Soryu Zeppelin 
"あなたはまだ、生きるのよ。\nアスカ。\nさあ、行きましょう。\n\0":
'???',

# ??? [Lilith]
"そうはいかないわ。\n\0":
'???',

# Rei Ayanami, Shinji Ikari
"誰…？\n\0":
'???',

# ??? [Lilith]
"生命の実をこの手に…。\nアダムの民から奪い返すまでは。\n\0":
'???',

# Toji's Mother
"泣いたらアカンよ…。\nさあ、帰るで…。\n\0":
'???',

# Kaworu Nagisa 
"だが、この一度だけ。\n僕はアダムになろう…。\nヒトであり続けるために！\n\0":
'???',

# Makoto Hyuga, Female Staff
"爆雷投下、６０秒前。\n\0":
'???',

# Ritsuko Akagi, Female Staff
"エヴァの機能は既に\n停止していたはず。\nなぜ、エヴァにあんな力が…！▽\n人の息の届かぬところに…、\nエヴァに心があるというの！？\n\0":
'???',

# Shigeru Aoba, Male Staff
"目標、殲滅を確認しました。\nパイロット、無事です！\n\0":
'???',

#
# ./USRDIR/event/n001.har_EXTRACT/n001.evs
#
# Misato Katsuragi, Female Staff
"シャムシエル\n\0":
'???',

# Misato Katsuragi, Female Staff
"使徒が市街地に攻撃を行い\n\0":
'???',

# Misato Katsuragi, Female Staff
"委員会からのエヴァ出撃要請を受け\n\0":
'???',

# Misato Katsuragi, Female Staff
"エヴァンゲリオン起動。\n参戦したのは…\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le416.evs
#
# Toji Suzuhara 
"けど、素のワシ…、\nよう見せられへん。\n\0":
'???',

# Toji's Shadow [Leliel]
"なんや、すっぴんやったら\n人前に出られへんか？▽\n今さらジャージ着てない\n鈴原トウジになられへんか？\n\0":
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
# ./USRDIR/event/b2s14.har_EXTRACT/b2s14.evs
#
# Kozo Fuyutsuki
"理由？\nお前が欲しいのは、口実だろう？\n\0":
'???',

# Gendo Ikari
"理由は存在すればいい。\nそれ以上の意味はない。\n\0":
'???',

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
'???',

# Gendo Ikari
"ゼーレが動く前に、\n全て済まさねばならん。\n今、弐号機を失うのは得策ではない。\n\0":
'???',

# Kozo Fuyutsuki
"かといって、ロンギヌスの槍を\nゼーレの許可なく使用するのは、\n面倒だぞ。\n\0":
'???',

#
# ./USRDIR/event/f075.har_EXTRACT/f075.evs
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
'???',

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
# ./USRDIR/event/levent.har_EXTRACT/le120.evs
#
# Shinji Ikari
"人を傷つけた事はあると思う。\n心の中に仕舞い込んだ言葉を\nうっかり出したりして。\n\0":
'???',

# Shinji's Shadow [Leliel]
"バカな事をしたと？\n\0":
'???',

# Shinji Ikari
"嫌われたかもしれない。\n\0":
'???',

# Shinji's Shadow [Leliel]
"それで、人と関わる事を\n快く思わないと…。▽\nじゃあ、もう他人に対する\n恐怖しか残らないね。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le002.evs
#
# Shinji Ikari
"た、助けて…。\n助けてっ…！！\nどうすれば、これ…わぁぁぁ…。\n\0":
'???',

# Toji Suzuhara 
"わわっ、何や！？\n何なんや、これ？\nどないなってんねん！？\n\0":
'???',

# Misato Katsuragi 
"どう？\n相手の動きは。\n\0":
'???',

# Male Staff
"使徒の動きはどうでしょうか？\n\0":
'???',

# Shigeru Aoba, Female Staff
"いまだ沈黙を続けています。\n\0":
'???',

# Shinji Ikari
"僕が先手を打ちます。\n\0":
'???',

# Asuka Soryu Langley
"何よ、こっちから出てやりゃ\nいいのよ。\n行くわよッ！！\n\0":
'???',

# Rei Ayanami 
"零号機、\n先制攻撃に出ます。\n\0":
'???',

# Toji Suzuhara 
"えぇい、待ってられへんわ。\nこっちから撃って出たる！\n\0":
'???',

# Kaworu Nagisa 
"今のうちに、\n仕留められるなら…。\n四号機、行きます。\n\0":
'???',

# Kaworu Nagisa 
"影…！？\nこれは…！\n\0":
'???',

# Misato Katsuragi 
"ちょっと、待ちなさい！\n危険だわ！！\n\0":
'???',

# Male Staff
"危険です。\n待機態勢に戻ってください！\n\0":
'???',

# Ritsuko Akagi 
"そこは危険だわ！\n影から離れて！！\n\0":
'???',

# Makoto Hyuga, Female Staff
"使徒、消失しました！\n\0":
'???',

# Asuka Soryu Langley
"影…！？\nちょっとッ！！\n足元が…何コレェ！？\n\0":
'???',

# Ritsuko Akagi 
"消えた！？\nどういう事！？\n\0":
'???',

# Male Staff
"消失！？\n反応は…！？\n\0":
'???',

# Rei Ayanami 
"身動きが取れない…。\n吸い込まれる…！？\n\0":
'???',

# Toji Suzuhara 
"あぁぁぁ…。\n沈む、沈んでまう…。\n抜けられへん………。\n\0":
'???',

# Rei Ayanami 
"影が…！？\n\0":
'???',

# Male Staff
"影から離れてください！\n危険です！\n\0":
'???',

# Misato Katsuragi 
"影から離れて！！\n逃げてッ！！\n\0":
'???',

# Makoto Hyuga, Female Staff
"パターン青！\n初号機の真下ですっ！\n\0":
'???',

# Makoto Hyuga, Female Staff
"パターン青！\n弐号機の真下ですっ！\n\0":
'???',

# Shinji Ikari
"か…、影が？\n何だよこれ！？\nおかしいよ…！\n\0":
'???',

# Makoto Hyuga, Female Staff
"パターン青！\n零号機の真下ですっ！\n\0":
'???',

# Makoto Hyuga, Female Staff
"パターン青！\n参号機の真下ですっ！\n\0":
'???',

# Asuka Soryu Langley
"やだ…！！\n沈む、沈んじゃう！！\n誰か！　どうにか出来ないの…。\n\0":
'???',

# Makoto Hyuga, Female Staff
"パターン青！\n四号機の真下ですっ！\n\0":
'???',

# Kaworu Nagisa 
"くっ…、しまった。\n捕らえられたか………。\n\0":
'???',

#
# ./USRDIR/event/cev0207.har_EXTRACT/cev0207.evs
#
# Asuka Soryu Langley
"ママ…。\n私はエヴァの為だけに\nいるの？▽\nママ…。\n\0":
'???',

#
# ./USRDIR/event/tev0402.har_EXTRACT/tev0402.evs
#
# Misato Katsuragi 
"どう、これから使徒残骸の\n回収作業を視察に行くけど、\nついてくる？▽\nどんな奴と戦ってるか、\n気になるでしょう？\n\0":
'???',

# Shinji Ikari
"だ、大丈夫ですか？\n近づいても…。\n\0":
'???',

# Shinji Ikari
"これが、僕たちの敵なのか…。\n\0":
'???',

# Misato Katsuragi 
"じき、分析の結果が出るはずだわ。\n\0":
'???',

# Ritsuko Akagi 
"すごいわ。\nこれは理想的なサンプルよ。\n\0":
'???',

# Gendo Ikari
"何か、わかった事は。\n\0":
'???',

# Shinji Ikari
"父さん…、来てたんだ…。\n\0":
'???',

# Shinji Ikari
"………？▽\nあの手…、火傷かな？\n\0":
'???',

# Ritsuko Akagi 
"こちらのモニターに出ます。▽\n使徒は粒子と波、両方の性質を\n備える光のような未知の物質で\n構成されているようです。▽\nそしてこれが、\n使徒独自の固有波形パターン。▽\n構成物質の違いはあるものの、\n信号の配置と座標は人間のそれと\n９９．８９％酷似しています。\n\0":
'???',

# Shinji Ikari
"よくわかりませんが、それって…。\n人間に…近いということですか？\n\0":
'???',

# Ritsuko Akagi 
"そうとも言えるわね。\n分析作業が進めば、詳しい事は\nわかるはずよ。\n\0":
'???',

# Ritsuko Akagi 
"さ、本部に戻りましょう。▽\nデータはマギに\n送られているはずだわ。\n私もゆっくり見せてもらいましょう。\n\0":
'???',

#
# ./USRDIR/event/tev0276.har_EXTRACT/tev0276.evs
#
# Misato Katsuragi 
"ここが、お風呂よ。\n他人が入っていなければ\nいつ使っても構わないわ。\n\0":
'???',

#
# ./USRDIR/event/bs092.har_EXTRACT/bs092.evs
#
# (Decision Prompt)
"構わん、やれ。／まだその時ではない。\0":
'???',

#
# ./USRDIR/event/cev1310.har_EXTRACT/cev1310.evs
#
# Hikari Horaki
"起立、礼。\n\0":
'???',

# Teacher
"えー、まず皆さんには\n大変悲しいお知らせがあります。▽\n先日、鈴原トウジ君が\n亡くなりました。\n\0":
'???',

# Kensuke Aida, Hikari Horaki, Maya Ibuki 
"え…。\n\0":
'???',

# Teacher
"鈴原君は、事故に遭い\n病院へ運ばれましたが、\n昨夜亡くなったそうです…。\n\0":
'???',

# Kensuke Aida
"…あいつが！？\n\0":
'???',

# Teacher
"なお、本日放課後に\n葬儀となります。▽\n授業を切り上げて、\n皆さん葬儀の方へ出席する事に\nなります。\n\0":
'???',

#
# ./USRDIR/event/cev1415.har_EXTRACT/cev1415.evs
#
# Hikari Horaki
"鈴原、明日は学校来るかなぁ。\nどんなお弁当にしよう。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le317.evs
#
# Rei Ayanami 
"あるわ。\n私はここにいる。\n想いもここにあるもの。\n\0":
'???',

# Rei's Shadow [Leliel]
"想いは移ろいやすいものよ。\nそんなものを根拠にするの？\n相手の気持ちも変わっていく。\n\0":
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
# ./USRDIR/event/tev1207.har_EXTRACT/tev1207.evs
#
# Maya Ibuki, Male Staff
"マギは判断を保留しています。\n\0":
'???',

# Misato Katsuragi 
"何もかもが不明…。\nとりあえず、様子をうかがいつつ、\n市街地から引き離しましょう。\n\0":
'???',

# Misato Katsuragi 
"どーなってんの？\n富士の電波観測所は？\n\0":
'???',

# Shigeru Aoba, Female Staff
"探知していません。\n真上にいきなり現れました。\n\0":
'???',

# Shigeru Aoba, Male Staff
"使徒、第３新東京市直上に出現！\n\0":
'???',

# Makoto Hyuga, Male Staff
"パターンオレンジ。\nΑΤフィールド反応無し。\n\0":
'???',

# Ritsuko Akagi 
"どういう事？\nΑΤフィールドがないなんて。\n新種の使徒！？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le218.evs
#
# Asuka Soryu Langley
"誰かに手を差し伸べて欲しい。\n誰かの手に届く位置にいて欲しい…。\n\0":
'???',

# Asuka's Shadow [Leliel]
"エヴァを駆り、使徒を倒す…。\nそのために選ばれたあなたを、\n誰も近くになんか置かないわ。\n\0":
'???',

#
# ./USRDIR/event/tev0216.har_EXTRACT/tev0216.evs
#
# Misato Katsuragi 
"さて、今からネルフ施設を案内する\n前に、快適に生活していく秘訣を\nあなたに教えるわね。\n\0":
'???',

# Misato Katsuragi 
"まずは「行動」から。\nあなたが取れる行動は、\n数多くあるわ。▽\n人と話す。\n食事をとる。\n技能を訓練する…などね。▽\n行動の基本は、%1iボタン。\n\0":
'???',

#
# ./USRDIR/event/tev0405.har_EXTRACT/tev0405.evs
#
# Shigeru Aoba
"第３新東京市の北西５０キロの上空に\n全長３００メートルを超える機影を\n発見！▽\n時速１００キロで、\n市街地に向かって進行中！\n\0":
'???',

# Gendo Ikari
"総員、第一種戦闘配置。\n\0":
'???',

# Shigeru Aoba
"敵は第一次防衛網を突破。\n間もなくＣエリアに到達します。\n\0":
'???',

# Misato Katsuragi 
"初号機、発進準備！\n\0":
'???',

# Shigeru Aoba
"敵内部に高エネルギー反応を確認。\n初号機に向けて収束中です！！\n\0":
'???',

# Misato Katsuragi 
"シンジ君！　よけて！！\n\0":
'???',

# Shinji Ikari
"うぁぁぁああああ\n\0":
'???',

# Misato Katsuragi 
"戻してっ！！\n早くっ！\n\0":
'???',

# Shigeru Aoba
"目標、沈黙。\n\0":
'???',

# Misato Katsuragi 
"シンジ君は！？\n\0":
'???',

# Makoto Hyuga
"生きてます！\n\0":
'???',

# Maya Ibuki 
"初号機回収。\nケイジへ。\n\0":
'???',

# Shinji Ikari
"ここは…？▽\n病院だ…。\n\0":
'???',

# Shinji Ikari
"使徒は…？\n僕は…何もしていない。\n\0":
'???',

# Rei Ayanami 
"目が覚めた？\n\0":
'???',

# Rei Ayanami 
"食事。\nこれ、食べて。\n\0":
'???',

# Shinji Ikari
"何も…食べたくない。\n\0":
'???',

# Rei Ayanami 
"食べた方がいいわ。\nまた、出撃だから。\n\0":
'???',

# Shinji Ikari
"また、アレに乗らなきゃ\nならないのかな？\n\0":
'???',

# Rei Ayanami 
"ええ、そうよ。\n\0":
'???',

# Shinji Ikari
"僕は…嫌だ。\n\0":
'???',

# Rei Ayanami 
"…乗らないの？\n\0":
'???',

# Shinji Ikari
"綾波はまだ、アレに乗って\n怖い目にあった事がないから、\nそんな事言えるんだ。▽\nもう、あんな思い、\nしたくない…。\n\0":
'???',

# Rei Ayanami 
"じゃ、寝てたら…。\n\0":
'???',

# Shinji Ikari
"寝てたらって…。\n\0":
'???',

# Rei Ayanami 
"私が行くわ。\n\0":
'???',

# Rei Ayanami 
"じゃ、葛城一尉と赤木博士が\n待ってるから。\n\0":
'???',

# Shinji Ikari
"あ…ちょっと。\n\0":
'???',

# Rei Ayanami 
"さよなら…。\n\0":
'???',

# Makoto Hyuga
"これが、分析結果です。▽\n目標は一定距離内に侵入した外敵を、\n加粒子砲で自動排除するものと\n思われます。▽\n展開されるΑΤフィールドは、\n相転移空間を肉眼で確認出来る程、\n超強力なものです。\n\0":
'???',

# Misato Katsuragi 
"強力な加粒子砲とΑΤフィールド。\n攻守共にパーペキな空中要塞ね。\nで、問題のシールドは？\n\0":
'???',

# Makoto Hyuga
"現在、目標は我々の直上、\n第３新東京市ゼロエリアに侵攻。▽\n直径、１７．５メートルの\n巨大シールドがジオフロント内の\nネルフ本部へ向かい、穿孔中です。▽\n敵はここ、ネルフ本部へ直接攻撃を\n仕掛けてくるつもりですね。\n\0":
'???',

# Misato Katsuragi 
"んふふ〜。\n私ね、チョッチ、\nやってみたい事があるの。\n\0":
'???',

# Kozo Fuyutsuki
"目標のレンジ外、超長距離からの\n直接狙撃かね。\n\0":
'???',

# Misato Katsuragi 
"そうです。▽\n加粒子砲を受けずに攻撃する方法は、\n目標のΑΤフィールドを中和せず\nレンジ外からの一点狙撃のみ。▽\nマギによる回答は勝算８．７％。\n最も高い数値です。\n\0":
'???',

# Makoto Hyuga
"ポジトロンライフル、\n準備完了です。\n\0":
'???',

# Misato Katsuragi 
"それじゃあ、作戦開始よ。▽\nシンジ君は初号機で砲手を担当。\nレイは零号機で防御を担当して。▽\nそれからシンジ君。\n\0":
'???',

# Misato Katsuragi 
"一度発射すると冷却や最充填、\nプラグ交換で次に撃てるまで\n時間がかかるから。\n\0":
'???',

# Shinji Ikari
"じゃあ、もし外れて\n敵が撃ち返して来たら？\n\0":
'???',

# Ritsuko Akagi 
"今は余計な事は考えないで\n一撃で撃破する事だけを\n考えなさい。\n\0":
'???',

#
# ./USRDIR/event/tev1311.har_EXTRACT/tev1311.evs
#
# Shinji Ikari
"目標…、\n目標の使徒って…。\nエヴァじゃないですか！？\n\0":
'The target...\n The target Angel...\n It\'s not an Eva?!\n\0',

# Gendo Ikari
"あれはもう、\nエヴァ参号機ではない。\n…使徒だ。\n\0":
'That is no longer\n Eva Unit-03.\n It\'s an Angel.\n\0',

# Asuka Soryu Langley
"プラグが見える。\nパイロットはあの中なんだわ。\nまさか使徒に乗っ取られるなんてね。\n\0":
'???',

# Shinji Ikari
"そんな！\nじゃあ、あの中には\n僕達と同じような子供が…。\n\0":
'???',

# Asuka Soryu Langley
"きゃああああああ！！\n\0":
'???',

# Shinji Ikari, Misato Katsuragi 
"アスカッ！！\n\0":
'Asuka!!\n\0',

# Shigeru Aoba
"エヴァ弐号機、完全に沈黙。\n目標移動、零号機へ。\n\0":
'Eva Unit-02 has gone completely silent.\n Target is moving toward Unit-02.\n\0',

# Rei Ayanami 
"はっ…。\n\0":
'???',

# Rei Ayanami 
"あぁぁぁぁ…！！\n\0":
'Ahhhhhh!!\n\0',

# Shigeru Aoba
"エヴァ零号機、沈黙しました。\n回収班、急いでください！\n\0":
'???',

# Gendo Ikari
"シンジ、目標は接近中だ。\nお前が倒せ。\n\0":
'???',

# Shinji Ikari
"でも、目標って言ったって。▽\n人が乗ってるんじゃないの？▽\n同い年の子供が…。\n\0":
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
'???',

#
# ./USRDIR/event/cev0114.har_EXTRACT/cev0114.evs
#
# [Text Only - No Designated Speaker]
"ケンスケが、大事そうに\nカメラを抱えている。\n\0":
'???',

# Shinji Ikari
"そのカメラ。\n新しいの買ったの？\n\0":
'???',

# Kensuke Aida
"うん。\n小遣い前借りしてね。\n\0":
'???',

# Shinji Ikari
"ケンスケって、\nいつも何を撮ったりしてるの？\nやっぱ、戦艦とかなの？\n\0":
'???',

# Kensuke Aida
"まぁね。\n\0":
'???',

# Shinji Ikari
"人とか、撮らないの？\n\0":
'???',

# Kensuke Aida
"んー、そういや…ないなぁ。\n誰かをモデルにしたりとかは。\n\0":
'???',

# Shinji Ikari
"何で、撮るのが好きなの？\n\0":
'???',

# Kensuke Aida
"何でかなぁ…、写真って、\n好きなモノを、好きなように\n切り取ってるっていうか…。▽\n自分もいつ死ぬかわからないし、\nその時まで好きなモノを\n貪欲に集めていたいっていうか…。\n\0":
'???',

# Shinji Ikari
"そうか、そうだよね。\nいつ死ぬ目にあうか\nわからないからっての、わかるよ。\n\0":
'???',

# Kensuke Aida
"あ…、別にシンジを責めてる\nわけじゃないよ。▽\nシンジが頑張って、俺達を\n守ってくれてるって知ってるから。\n\0":
'???',

# Kensuke Aida
"………………………あ。\nそうだ…。\nシンジ、ちょっと付き合えよ。\n\0":
'???',

# Shinji Ikari
"どこへ？\n\0":
'???',

# Kensuke Aida
"いいから…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕等は教室を抜け出した。\n朝の鮮やかな青空と風。\n白い入道雲。▽\nケンスケが案内してくれた先は\n学校の裏にある山だった。▽\n自分の背丈よりも高い草を\n掻き分けて先を急ぐ。▽\n進んでも、進んでも草ばかりだ。\nむせ返るような、草いきれ。▽\n草のトンネルを抜けたケンスケが\n声をあげた。\n\0":
'???',

# Kensuke Aida
"シンジ、こっち。\n\0":
'???',

# Shinji Ikari, Kensuke Aida, Ritsuko Akagi, Maya Ibuki 
"あ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"一面の向日葵。\nケンスケと僕以外、誰もいない。▽\n遠くにセミの声が聞こえる以外は\n本当に静かだ。\n別世界の様だった。\n\0":
'???',

# Kensuke Aida
"今、こんな花が咲いてるけど\n俺の膝丈ぐらいの時に\nココ見つけたんだ。▽\n俺の大好きな、ヒミツの場所。\n\0":
'???',

# [Text Only - No Designated Speaker]
"疾走する風。\n一斉に波打つ黄金の海。\n\0":
'???',

# Shinji Ikari
"わぁ…、すごい…。\n\0":
'???',

# Kensuke Aida
"シンジー！\n\0":
'???',

# Kensuke Aida
"ハハハハハッ…。\nいいの撮れた。\n\0":
'???',

# Shinji Ikari
"今の、撮ったの？\n\0":
'???',

# Kensuke Aida
"ああ、いいのが撮れたよ。\n大好きな場所に立つ、大事な友達。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ケンスケが指でフレームを作って、\nカメラを構えるようにして僕を見た。\n白い歯を見せて笑う。\n\0":
'???',

# Shinji Ikari
"もう、撮らないの？\n\0":
'???',

# Kensuke Aida
"俺の目のフィルムに焼くの。\nこの風景。\nずっと、忘れないように。\n\0":
'???',

# [Text Only - No Designated Speaker]
"また風が吹いた。▽\n僕も指でフレームを作った。▽\nずっと、今日のケンスケを\n胸に焼き付けておけるように。\n\0":
'???',

#
# ./USRDIR/event/f061.har_EXTRACT/f061.evs
#
# [Text Only - No Designated Speaker]
"振り向けば、\nそこにレイが立っているような、\nそんな気がした…。\n\0":
'???',

# Rei Ayanami 
"私、\nどうしてここへ\n帰るのかしら。▽\nここが私の家だから。\nあの人に与えられた場所だから。\n\0":
'???',

# Rei Ayanami 
"与えられた場所、\nエヴァ零号機。\nそこも帰る場所。▽\n用意されていた場所。\n用意されていた私。▽\n本当の私は何？▽\n知らない私。▽\n私の中にもう一人の私がいる。▽\n私が本当に帰る場所がある。▽\nそれは、どこに…？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le142.evs
#
# Shinji Ikari
"じゃあ、何で僕を傷つけるんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"僕は君にとっての真実だ。▽\n君は自分に正直でないから、\n否定的に捉えてるだけだよ。\n他人の中の僕も、君の中の僕も。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le320.evs
#
# Rei Ayanami 
"結ばれた絆は変わらない。\n\0":
'???',

# Rei's Shadow [Leliel]
"変わらない…。\nあなたはそう思い込みたいだけ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le221.evs
#
# Asuka Soryu Langley
"私は違うわ…。\nだって私は他の人と違うんだもの…。\n\0":
'???',

# Asuka's Shadow [Leliel]
"孤独に凍えているあなたを知ったら、\n誰もそうは思わないでしょうね。\nやはり誰も近づけない方がいいわ。\n\0":
'???',

#
# ./USRDIR/event/cev0905.har_EXTRACT/cev0905.evs
#
# [Text Only - No Designated Speaker]
"葛城さんとの出来事を知ったら、\nシンジ君は僕をどう思うだろうか。▽\nそんな事を考えながら、\n僕はすました顔で\nやり過ごしていた。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le009.evs
#
# Shinji Ikari
"ミサトさん？\nミサトさん！？\nミサトさ………………。\n\0":
'???',

#
# ./USRDIR/event/tev1703.har_EXTRACT/tev1703.evs
#
# Makoto Hyuga, Male Staff
"目標のΑΤフィールドは依然、健在。▽\nパターン、青からオレンジへ\n周期的に変化しています。\n\0":
'???',

# Misato Katsuragi 
"どういう事？\n\0":
'???',

# Maya Ibuki, Male Staff
"マギは解答不能を提示しています。▽\nただ、あの形は固定形態でない事は\n確かですね。\n\0":
'???',

# Misato Katsuragi, Kozo Fuyutsuki
"このまま膠着状態を\n続けるしかないか…。\n\0":
'???',

# Misato Katsuragi 
"真っ向から勝負するのは危険だわ。\n接近戦は避けた方がよさそうね。\n\0":
'???',

# Gendo Ikari
"零号機発進。\n迎撃位置。\n\0":
'???',

# Makoto Hyuga
"弐号機は現在位置で待機を。\n\0":
'???',

# Gendo Ikari
"いや、発進準備だ。\n\0":
'???',

# Makoto Hyuga
"司令。\n\0":
'???',

# Gendo Ikari
"構わん。\nおとりぐらいには役に立つ。\n\0":
'???',

#
# ./USRDIR/event/f039.har_EXTRACT/f039.evs
#
# Shinji Ikari
"今日は風が強いな…。\n\0":
'???',

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
# ./USRDIR/event/tev0243.har_EXTRACT/tev0243.evs
#
# Maya Ibuki 
"このステータスで\nあなたの状態だけではなく、\n他の人の状態も確認出来るの。\n\0":
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
# ./USRDIR/event/tev1205.har_EXTRACT/tev1205.evs
#
# Misato Katsuragi 
"いい結婚式だったわね。\n\0":
'???',

# Ryoji Kaji
"学生の頃と違って、\nみんな家庭を持つ歳に\nなったんだな…。\n\0":
'???',

# Ritsuko Akagi 
"ホント。\nお互い、最後の一人には\nなりたくないわね。▽\nあなた達二人、\nここらで結婚すれば？\n\0":
'???',

# Misato Katsuragi 
"リツコにしちゃ、\n珍しいジョーダンね。▽\n今は、あの子達の子守りで\n手ェいっぱいよ。▽\nチョッチ、ごめん。\n化粧直してくるわ。\n\0":
'???',

# Ritsuko Akagi 
"あら、逃げちゃ駄目よ？\n\0":
'???',

# Misato Katsuragi 
"ちゃんと戻ってくるわよ。\n\0":
'???',

# Ritsuko Akagi 
"ミサト、今日ははしゃいでるわね。\nちょっと飲みすぎなんじゃない？\n\0":
'???',

# Ryoji Kaji
"そうだな。\n今日は浮かれるために\n飲んでるんだろ。▽\nいつもは自分を抑えるために\n飲んでるんだろうけど。\n\0":
'???',

# Ritsuko Akagi 
"やっぱり、一緒に暮らしてた人は\n違うわね。\n言葉の重みが。\n\0":
'???',

# Ryoji Kaji
"あれは暮らしというより\n共同生活だな。\nママゴトさ…現実は甘くない。\n\0":
'???',

# Ritsuko Akagi 
"それにしても、ミサトがスカートに\nヒール履くなんて、学生時代には\n考えられなかったわ。\n\0":
'???',

# Ryoji Kaji
"ヒールを履くようになったのは\n彼女と別れて…その後か。▽\nお互い、知らない時間と夜が\n増えた事を知らされたよ。\n\0":
'???',

# Ritsuko Akagi 
"ところで。\n京都、何しに行ってたの？\n\0":
'???',

# Ryoji Kaji
"あれ？\n出張したのは松代だよ。\n\0":
'???',

# Ritsuko Akagi 
"とぼけてもムダ。\nあまり深追いすると、\nヤケドするわよ。▽\nこれは、友人としての忠告。\n\0":
'???',

# Ryoji Kaji
"友人ね…。\n昔の事は、さらりと返せる。\nキミは強いな。\n\0":
'???',

# Ritsuko Akagi 
"あなた、\nただ寂しかっただけでしょ。\n\0":
'???',

# Ryoji Kaji
"そう言うキミは？\n今は寂しくない…？\n\0":
'???',

# Misato Katsuragi 
"変わってないのね。\nその軽ぅ〜いところ。\n\0":
'???',

# Ryoji Kaji
"おっと、戻ってきたか。\n\0":
'???',

# Ritsuko Akagi 
"さて、そろそろ\nおいとまするわね。\n\0":
'???',

# Misato Katsuragi, Ritsuko Akagi, Rei Ayanami
"そう。\n\0":
'???',

# Ryoji Kaji
"残念だな。\nもう少しゆっくり出来ると\n思ったのに。\n\0":
'???',

# Ritsuko Akagi 
"じゃ、ミサトの事\nよろしくね。\n\0":
'???',

# Misato Katsuragi 
"加持君、私…変わったかな？\n\0":
'???',

# Ryoji Kaji
"綺麗になった。\n\0":
'???',

# Misato Katsuragi 
"ごめんね、\nあの時一方的に別れ話して。▽\n他に好きな人が出来たってのは、\nあれウソ。\nバレてた？\n\0":
'???',

# Ryoji Kaji
"…いや。\n\0":
'???',

# Misato Katsuragi 
"ただ逃げただけなの。\n父親という呪縛から\n逃げ出しただけ。\n\0":
'???',

# Misato Katsuragi 
"加持君、\n私の父さんに似てる。▽\n私、男に父親を求めていたのねって\n気付いて…怖くなったの。▽\n…………。\nゴメンね。\n酒の勢いでこんな話…。▽\n父を憎んでいた私が、\n父によく似た人を好きになる。▽\n全てを吹っ切るつもりで\nネルフを選んだけど…、\nでも、それも父のいた組織。▽\n結局、使徒に復讐する事で\nみんな誤魔化してきたんだわ。▽\nその上…、こうやって\n都合のいい時ばっかり\n男にすがろうとする。▽\n一緒に暮らしていた時だって…、\nそうやってあなたを利用していた\nだけかもしれないわ…。\n\0":
'???',

# Ryoji Kaji
"もういい…。\n\0":
'???',

# Misato Katsuragi 
"私…シンジ君と同じ\n子供なのよ。▽\nなのに…、嫌なところばかり\n大人に…女になって…。▽\nそんな自分に嫌気が差すわ。\n\0":
'???',

# Ryoji Kaji
"もういい！\n\0":
'???',

# Ryoji Kaji
"俺は、それでも\n後悔していない。\n君と一緒に過ごした日々を。\n\0":
'???',

# Misato Katsuragi 
"加持君…。\n\0":
'Kaji-kun...\n\0',

# Ryoji Kaji
"俺は、あの時の思い出だけで\nこれからも生きていける。\n何が起きようとも…。▽\nだから…、もう言わなくていい。\n\0":
'???',

#
# ./USRDIR/event/tev0222.har_EXTRACT/tev0222.evs
#
# Misato Katsuragi 
"ここで%1iボタンを押すと、\n\0":
'When you press the %1i button here,\n\0',

#
# ./USRDIR/event/a010.har_EXTRACT/a010.evs
#
# Female Staff
"マギによる演算結果でも\n勝率は０．００００１パーセント。▽\nしかし、ここを放棄する以外、\n他に手がありません。\n\0":
'???',

# Male Staff
"では、パイロットに非常召集を。\n準備が出来次第、\n作戦を開始しましょう。\n\0":
'???',

# Shigeru Aoba, Male Staff
"エヴァで使徒を\n受け止めるんですか？\n\0":
'???',

# Makoto Hyuga, Male Staff
"使徒、インド洋上空、\n衛星軌道上に突如出現！\n\0":
'???',

# Misato Katsuragi 
"そうよ。▽\n目標の落下予測地点にエヴァを\n配置し、ΑΤフィールド最大で\n直接使徒を受け止めるの。\n\0":
'???',

# Kozo Fuyutsuki
"そうだ。▽\n目標の落下予測地点にエヴァを\n配置し、ΑΤフィールド最大で\n直接使徒を受け止める。\n\0":
'???',

# Female Staff
"目標の落下予測地点にエヴァを\n配置し、ΑΤフィールドで\n直接使徒を受け止めます。\n\0":
'???',

# Male Staff, Makoto Hyuga
"しかし、こんなに落下予想範囲が\n広くては…。\n\0":
'???',

# Ritsuko Akagi 
"エヴァの初期配置を\n外した時点でアウト。▽\n当たる確率はざっと計算して………、\n万に一つもないわよ。\nどうするの？\n\0":
'???',

# Makoto Hyuga
"こりゃ、すごい！\n\0":
'That\'s amazing!\n\0',

# Female Staff
"これは…すごい！\n\0":
'That is... incredible!\n\0',

# Ritsuko Akagi 
"エヴァの初期配置を\n外した時点でアウト。▽\n当たる確率はざっと計算して………、\n万に一つもありません。\nどうなさるおつもりですか？\n\0":
'???',

# Misato Katsuragi 
"常識を疑うわね。\n\0":
'???',

# Kozo Fuyutsuki
"また、無茶なヤツだな。\n\0":
'???',

# Male Staff
"常識を疑いますね。\n\0":
'???',

# Ritsuko Akagi 
"エヴァの初期配置を\n外した時点でアウト。▽\n当たる確率はざっと計算して………、\n万に一つもない。\n\0":
'???',

# Male Staff
"エヴァの初期配置を\n外した時点でアウト。▽\n当たる確率は………、\n万に一つもない。\n\0":
'???',

# Misato Katsuragi 
"可能性はゼロ、じゃないのよ。\n他に方法がなければ\nやるしかないわ。\n\0":
'???',

# Misato Katsuragi 
"大した破壊力ね。\nさっすがΑΤフィールド。\n\0":
'???',

# Kozo Fuyutsuki
"大した破壊力だな。\nやはりΑΤフィールドか。\n\0":
'???',

# Female Staff
"スゴイ破壊力ですね。\nさすがはΑΤフィールド。\n\0":
'???',

# Ritsuko Akagi 
"パイロットに非常召集を。\n準備が出来次第、\n作戦を開始しましょう。\n\0":
'???',

# Maya Ibuki, Female Staff
"落下のエネルギーをも\n利用しています。▽\n使徒そのものが\n爆弾みたいなものですね。\n\0":
'???',

# Ritsuko Akagi 
"とりあえず、\n初弾は太平洋に大ハズレ。\nだけど徐々に狙いを定めてきてるわ。\n\0":
'???',

# Female Staff
"とりあえず、初弾は\n太平洋に落下していますが…、▽\n徐々に狙いが\n正確になってきています。\n\0":
'???',

# Misato Katsuragi 
"来るわね、多分。\n\0":
'???',

# Kozo Fuyutsuki
"…来るな。\n\0":
'???',

# Male Staff
"来ますね、多分。\n\0":
'???',

# Kozo Fuyutsuki
"だが、使徒殲滅が我々の仕事だ。\n…これに賭けよう。\n\0":
'???',

# Ritsuko Akagi 
"ええ、次はここに、本体ごとね。\nどうするの？\n\0":
'???',

# Ritsuko Akagi 
"次はここに、本体ごと。\nどうします？\n\0":
'???',

# Ritsuko Akagi 
"次はここに、本体ごとね。\nどうしようかしら？\n\0":
'???',

# Female Staff
"次はここに本体ごと。\nいったい、どうすれば………？\n\0":
'???',

#
# ./USRDIR/event/tev1504.har_EXTRACT/tev1504.evs
#
# Asuka Soryu Langley
"加持さん、どこにいるの？\nアンタ、知ってる？\nここ最近、見ないんだけど。\n\0":
'???',

# Shinji Ikari
"ううん？\nミサトさんなら\n知ってるんじゃない？\n\0":
'???',

# Asuka Soryu Langley
"そのミサトもいないから\nアンタに聞いてるんじゃないの。\n\0":
'???',

# Shinji Ikari
"一緒なんじゃないのかな？\n\0":
'???',

# Asuka Soryu Langley
"だったら余計、困るのよ！！\nバカ！！\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le132.evs
#
# Shinji Ikari
"だって、どうしようもないんだ。\n他人の中の僕までは\n変えられないもの。\n\0":
'???',

# Shinji's Shadow [Leliel]
"自分が変わろうとは思わない？\n他人の中の自分を変える為に。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le307.evs
#
# Rei Ayanami 
"果たした役割はデータとして残る。\n\0":
'???',

# Rei's Shadow [Leliel]
"ただの数値の羅列が残るだけ。\n人の想いに関わる事はできない。\n\0":
'???',

#
# ./USRDIR/event/f054.har_EXTRACT/f054.evs
#
# Male Staff
"加持さん。\n総務部に買い物頼まれてた\nでしょう？▽\nこちら、ですよね？\n\0":
'???',

# Ryoji Kaji
"ああ、サンキュー。\n重たいのに、すまないな。\n\0":
'???',

# Male Staff
"ところで…、\nそれ、肥料ですよね…。\n何に使うんですか？\n\0":
'???',

# Ryoji Kaji
"ま、ちょっと使うんだ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ジオフロントの一角に加持が\n作った小さな家庭菜園がある。▽\nずっしりと重く、見事なスイカが\nたくさん実っている。\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley
"加持さん？\n\0":
'???',

# Toji Suzuhara
"加持さん…、やないですか？\n\0":
'???',

# Kaworu Nagisa 
"いいスイカですね。\n\0":
'???',

# Rei Ayanami 
"スイカ…？\n\0":
'???',

# Female Staff
"スイカ畑…？\n\0":
'???',

# Ryoji Kaji
"君か。\n散歩かい？\n\0":
'???',

# Shinji Ikari
"こんなところで、\n何をしているんですか？\n\0":
'???',

# Asuka Soryu Langley
"何をしてるんですか？\n\0":
'???',

# Toji Suzuhara
"こんなトコで、\n何してはるんですか？\n\0":
'???',

# Kaworu Nagisa 
"ここは、加持さんの畑ですか？\n\0":
'???',

# Rei Ayanami 
"これ、育てているんですか？\n\0":
'???',

# Female Staff
"これは全部、加持さんが？\n\0":
'???',

# Ryoji Kaji
"俺の畑さ。▽\nちょいと間借りさせてもらってね。\n毎日こうやって、\n世話してやってるのさ。▽\nスイカ、食べるかい？\nこれは俺の自信作。\nすぐ、切ってやるよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"スイカをかじると、\nあふれるように果汁が飛び出した。\n二つ、三つ、地面に染みを作る。\n\0":
'???',

# Shinji Ikari
"おいしい…です。\n\0":
'???',

# Asuka Soryu Langley
"少し、ぬるいけど、\nおいしい…。\n\0":
'???',

# Toji Suzuhara
"わ、甘っ！\n\0":
'???',

# Kaworu Nagisa 
"おいしいですね。\n\0":
'???',

# Rei Ayanami 
"…おいしい。\n\0":
'???',

# Female Staff
"わぁ、おいしい…。\n\0":
'???',

# Ryoji Kaji
"何かを育てるっていうのが\n俺の趣味なんだ。\n誰にもナイショだったんだがね。▽\n何かを育てるというのは、\n大変な事だが、それより新しい\n発見を得る方が多いんだよ。\n\0":
'???',

# Ryoji Kaji
"多くを学ばされるよ。\n世界はちゃんと生きる力を\n与えるように出来ているんだな。▽\nこいつらが育っていくのを見ると\nそれがよくわかる…。\n\0":
'???',

# Ryoji Kaji
"戻ろうか、\n俺も仕事があるんでね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、加持の姿が頭をよぎった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"加持が、重そうな荷物を担いで\n歩いている。\n\0":
'???',

# Shinji Ikari
"加持さんだ…。\nどこに行くんだろう？\n\0":
'???',

# Asuka Soryu Langley
"あっ、加持さんだ！\nドコに行くのかしら？\n\0":
'???',

# Misato Katsuragi 
"うん？\nあんな荷物持って、\nどこに行くつもりかしら？\n\0":
'???',

# Ritsuko Akagi 
"どこへ行くのかしら？\n何なのあの荷物…。\n\0":
'???',

# Maya Ibuki 
"なぁに、あの大荷物。\nどこ行くつもりかしら？\n\0":
'???',

# Makoto Hyuga, Kaworu Nagisa
"加持さん…？\n\0":
'???',

# Shigeru Aoba
"あれ、加持さんか…？\n\0":
'???',

# Toji Suzuhara 
"加持さんや。\n何やねん、あの荷物。\n\0":
'???',

# Kaworu Nagisa 
"加持さんだ。\nどこへ行くのだろう。\n\0":
'???',

# [Text Only - No Designated Speaker]
"あとをつけていくと、\nジオフロント内に\n小さな家庭菜園があった。▽\n加持が大きな荷物の中から\n藁を取り出し、スイカの下に\n丁寧に敷き詰めていく。\n\0":
'???',

# Misato Katsuragi, Ritsuko Akagi 
"加持くん。\n\0":
'???',

# Ryoji Kaji
"よう、\nここなら誰にも見つからないと\n思ったけど、見つかっちまったな。▽\nようこそ、俺の畑へ。\nちょうどスイカが収穫の時期でね。\nそこの花も、来週には咲くだろう。\n\0":
'???',

# Shinji Ikari
"でも、どうしてこんな事を？\n\0":
'???',

# Asuka Soryu Langley
"畑仕事なんて…、どうして？\n\0":
'???',

# Misato Katsuragi 
"アンタにこんな才能が\nあったとはね。\n\0":
'???',

# Ritsuko Akagi 
"全然、知らなかったわ。\nこんな畑があるなんて…。\n\0":
'???',

# Maya Ibuki 
"まあっ、こっちにはトマト…。\n綺麗…。\n\0":
'???',

# Makoto Hyuga
"これ、加持さんが一人で？\n\0":
'???',

# Shigeru Aoba
"ここに畑があったなんて。\nへぇー、これはオクラかな？\n\0":
'???',

# Toji Suzuhara 
"これ、食えるんですよね？\nあんま、害虫もおらんし、\nええ環境でしょうね。\n\0":
'???',

# Kaworu Nagisa 
"でも、なぜ畑なんか\n作ったんですか？\n\0":
'???',

# Ryoji Kaji
"俺の趣味なんだよ。\nこうやって、何かを育てると\nいうのがね。▽\n何かを育てるというのは、\n大変な事だが、新しい発見を\n得る事もある。▽\nこいつらには多くを学ばされるよ。▽\n世界はちゃんと生きる力を\n与えるように出来ていることを。▽\nこいつらが育っていくのを見ると\nそれがよくわかるんだ…。\n\0":
'???',

# Ryoji Kaji
"スイカ、食べて行ってくれ。\n俺の自信作なんでね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"加持が手際よくスイカを切り分ける。▽\nスイカをかじると\nたくさんの果汁が溢れ出し、\n地面に二つ三つの染みを作った。\n\0":
'???',

# Shinji Ikari
"甘い…。\n\0":
'???',

# Asuka Soryu Langley
"わぁ、おいしー！\n\0":
'???',

# Rei Ayanami 
"…甘い、おいしい。\n\0":
'???',

# Misato Katsuragi 
"何か、懐かしい味…。\nおいしいわ。\n\0":
'???',

# Ritsuko Akagi 
"昔のスイカの味ね。\nおいしいわ…。\n\0":
'???',

# Maya Ibuki 
"冷えてなくてもおいしい…。\n水気たっぷりで。\n\0":
'???',

# Makoto Hyuga
"あっ、おいしいですねぇ…。\n\0":
'???',

# Shigeru Aoba
"イケますね。\nうまいですよ。\n\0":
'???',

# Toji Suzuhara 
"うわ、うま〜。\nごっつ、甘い。\n\0":
'???',

# Kaworu Nagisa 
"おいしいです。\nもう少しもらってもいいですか？\n\0":
'???',

# Ryoji Kaji
"ウマイだろ？\nそら、おかわりしろ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"加持はそう言うと、\n再び畑仕事を始めた。▽\nそこは、水と土の優しい匂いがした。\n\0":
'???',

# Gendo Ikari, Kozo Fuyutsuki
"あいつか、どこへ行くつもりだ？\n\0":
'???',

# Gendo Ikari
"これは、畑か…。\n\0":
'???',

# Kozo Fuyutsuki
"見事なスイカだな…。\n\0":
'???',

# Ryoji Kaji
"ここなら誰にも見つからないと\n思ったんですけど、\nあっさり見つかりましたね。▽\nようこそ、私の畑へ。\nちょうどスイカが収穫の時期でね。\nその花も、来週には咲くんですよ。\n\0":
'???',

# Gendo Ikari
"君が畑仕事とはな。\n\0":
'???',

# Kozo Fuyutsuki
"しかし、いつの間にこんな物を。\n\0":
'???',

# Ryoji Kaji
"私の趣味です。\nこうやって、何かを育てると\nいうのがね。▽\n何かを育てるというのは、\n大変な事ですが、新しい発見を\n得る事もあります。▽\nこいつらには実に多くを\n学ばされましたよ。▽\n世界はちゃんと生きる力を\n与えるように出来ていることを。▽\nこいつらが育っていくのを見ると\nそれがよくわかるんです…。\n\0":
'???',

# Ryoji Kaji
"お一ついかがですか？\nどうぞ、スイカを食べて行って\n下さい。▽\n私の自信作なんでね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"加持が手際よくスイカを切り分ける。▽\nスイカをかじると\nたくさんの果汁が溢れ出し、\n地面に二つ、三つの染みを作った。\n\0":
'???',

# Gendo Ikari
"ぬるいが、いい味だ。\n\0":
'???',

# Kozo Fuyutsuki
"このスイカは懐かしい味がするよ。▽\n思えば昔の野菜は、こんな\n滋味あふれる味をしていたな。\n\0":
'???',

# Ryoji Kaji
"もう一つ、いかがですか？\n\0":
'???',

#
# ./USRDIR/event/tev0234.har_EXTRACT/tev0234.evs
#
# Misato Katsuragi 
"で、この中の\nステータスを選ぶと…。\n\0":
'???',

#
# ./USRDIR/event/tev1203.har_EXTRACT/tev1203.evs
#
# Kensuke Aida
"さーて、\n終わった終わった。\n\0":
'???',

# Toji Suzuhara 
"なあ、ヤキソバ食いに行かへん？\nシンジ、お前もどや？\n\0":
'???',

# Shinji Ikari
"あ、僕は…行くところがあるんだ。\nまた今度誘ってよ…。\n\0":
'???',

# Kensuke Aida
"あ、じゃあなシンジ。\n\0":
'???',

# Toji Suzuhara 
"おう、お疲れさん。\n\0":
'???',

# Shinji Ikari
"じゃあ…。\n\0":
'???',

# Shinji Ikari
"あの日の思い出は…、\n僕が逃げ出した事…。▽\n母さんが眠ってる墓に\n伯父さんと叔母さんが\n連れて行ってくれた…。▽\nそれから…父さんがいた。▽\n父さんが怖かった。\n何で怖かったのか、\nそれは覚えていないけれど。▽\n顔もわからない母さん。▽\nもう会えない母さん。▽\nあそこに行っても、\n母さんは何も満たしては\nくれなかった。▽\nだから、逃げ出した。\n怖かった。▽\n僕と父さんは、あの時会っても…、▽\n結局、何も始まらなかった…。\n\0":
'???',

# Shinji Ikari
"そうだ、ここだ…。\nやっぱり、寂しいところだな。\n\0":
'???',

# [Text Only - No Designated Speaker]
"どこまでも続く、膨大な数の墓標。\nセカンドインパクトで\n亡くなった人達の墓である。▽\n遠くに人影が見える。\nシンジの母、碇ユイの墓前に…。\n\0":
'???',

# Shinji Ikari
"父…さん？\n\0":
'???',

# Gendo Ikari
"シンジか…。\n\0":
'???',

# Shinji Ikari
"………来ていたんだ。\n\0":
'???',

# Shinji Ikari
"僕は…、\nあの時逃げ出して…、\nその後は来ていない。▽\nここに母さんが眠ってるなんて\nピンと来ないんだ。\n顔も覚えてないのに。\n\0":
'???',

# Gendo Ikari
"人は思い出を忘れる事で\n生きて行ける。▽\nだが、\n決して忘れてはならない事もある。▽\nユイは、\nそのかけがえのないものを\n教えてくれた。▽\n私は、その確認をする為に\nここに来ている。\n\0":
'???',

# Shinji Ikari
"写真とかないの？\n\0":
'???',

# Gendo Ikari
"残ってはいない。\nこの墓もただの飾りだ。\n遺体はない。\n\0":
'???',

# Shinji Ikari
"全部…捨てたって。\nそう伯父さんから聞いてたけど。\n本当だったんだ…。\n\0":
'???',

# Gendo Ikari
"全ては心の中だ。\n今はそれでいい。\n\0":
'???',

# Gendo Ikari
"時間だ。\n先に帰る。\n\0":
'???',

# Shinji Ikari
"あの、父さん…。\n\0":
'???',

# Gendo Ikari
"…何だ？\n\0":
'???',

# Shinji Ikari
"今日は、嬉しかった。\n父さんと話せて。\n\0":
'???',

# Gendo Ikari, Toji Suzuhara
"そうか…。\n\0":
'???',

#
# ./USRDIR/event/cev1404.har_EXTRACT/cev1404.evs
#
# Hikari Horaki
"別に悪者にしたいわけじゃ\nないのにな…。\n何かいつも、ムキになっちゃう。▽\n…素直に、なりたいなぁ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le217.evs
#
# Asuka Soryu Langley
"こんなに苦しんでいるのに…。\n他人って冷たいのね…。\n\0":
'???',

# Asuka's Shadow [Leliel]
"みんなその冷たさに耐えているのよ。\n\0":
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
# ./USRDIR/event/cev0403.har_EXTRACT/cev0403.evs
#
# Misato Katsuragi 
"碇司令は…。\nセカンドインパクトが\n起こる事を知っていた…。▽\n父さんを利用して…。\n\0":
'???',

# Misato Katsuragi 
"ネルフはまだ、\n何かを隠している。▽\n一体何が…、\nこれから起ころうとしているの。\n\0":
'???',

#
# ./USRDIR/event/cev0110.har_EXTRACT/cev0110.evs
#
# [Text Only - No Designated Speaker]
"ごきげんな様子で青葉が歩いて来る。\n鼻歌を歌って、リズムを取って\nまさしくノリノリって感じだ。\n\0":
'???',

# Shigeru Aoba
"よぉ、シンジ君！\n\0":
'???',

# Shinji Ikari
"あ、青葉さん。\n何だか、機嫌良さそうですね。\n\0":
'???',

# Shigeru Aoba
"ああ、もう、自分の才能が怖い…。\n俺は天才かもしれない…。\n\0":
'???',

# Shinji Ikari
"ええっと…、お仕事が上手く\nいってるんですか？\n\0":
'???',

# Shigeru Aoba
"はは…、仕事はいつも快調さ。\n…あ、そうだ。\nシンジ君は楽器出来たんだよな？\n\0":
'???',

# Shinji Ikari
"はい、チェロですけど。\n\0":
'???',

# Shigeru Aoba
"ちょうどいい。\nちょっと来てくれ！\n\0":
'???',

# Shinji Ikari
"え、ええ？　あっ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕は返事をする間も無く、\n青葉さんに手を引かれて\n連れて行かれた。\n\0":
'???',

# Shigeru Aoba
"じゃ、これ持って…。\n\0":
'???',

# Shinji Ikari
"ベースギター…ですね。\n\0":
'???',

# Shigeru Aoba
"ああ、音階はチェロと同じだ。\n何となくわかるだろ？\n\0":
'???',

# Shinji Ikari
"はあ、まあ…。\nええっとピックを使うんですよね？\n\0":
'???',

# Shigeru Aoba
"そうそう、じゃあＥでブルースでも\nやってみようか。\nコードはわかるか？\n\0":
'???',

# Shinji Ikari
"ええっと…？\n\0":
'???',

# Shigeru Aoba
"ＥとＡとＢのループだ。\n指は…ソコじゃない…。\n一本上の弦の…、そう、ソコだ。\n\0":
'???',

# Shinji Ikari
"…う、うまく出来るかな…。\n\0":
'???',

# Shigeru Aoba
"はは…、ま、気楽にやってくれ。\nじゃあテンポはミディアムで…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕は、おそるおそる\n言われた音を四拍子で\n弾き始めた。▽\nその単調な音に乗っかかるように\n青葉さんの弾くギターの音が\n被さった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"…ほんの数秒合わせただけなのに、\n楽しい…。▽\n思わず青葉さんを見ると、\n「どうだ？」と言いたげに\n青葉さんはウインクをした。▽\n………………………。\n………………………。\n１６小節を終え、僕達は手を止めた。\n\0":
'???',

# Shigeru Aoba
"ん〜、やっぱブルースはいいねぇ…。\n\0":
'???',

# Shinji Ikari
"…僕、こんなの初めてだったけど…、\nベースも結構、面白いですね。\n\0":
'???',

# Shigeru Aoba
"だろ？　やっぱ一度ハマると\n止められないよなぁ。\n\0":
'???',

# Shigeru Aoba
"シンジ君、俺ね…。\n本当はネルフの職員じゃなくって\nミュージシャンになりたかったんだ。\n\0":
'???',

# Shinji Ikari
"えっ…！？\n\0":
'???',

# Shigeru Aoba
"そうは見えないってか？\nハハハ、まあ、\n結局、夢に終わったんだけどさ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"青葉さんは、やや自嘲気味に笑った。\n少し、寂しそうにも見える。\n\0":
'???',

# Shinji Ikari
"…今でも…ミュージシャンに\nなりたいんですか？\n\0":
'???',

# Shigeru Aoba
"はは、まぁ…な。\n\0":
'???',

# Shigeru Aoba
"でも俺には今、ちゃんとこうして\nオペレーターとしての生き方が\nあるわけだし。\n\0":
'???',

# Shinji Ikari
"そう…かもしれませんけど…。\nでも、すっごい上手だと思いました。\nさっきの演奏。\n\0":
'???',

# Shigeru Aoba
"はは、ありがとよ。\n一応、学生時代に一度プロから\n声がかかった腕だからな。\n\0":
'???',

# Shinji Ikari
"そうなんですか！？\nすごいや…。\n\0":
'???',

# Shigeru Aoba
"…結局、ネルフを選んじまったが、\n音楽は一日も忘れた事は無いさ。▽\n…ま、いずれ使徒がいない\n平和な世の中になったら、\n路上ででも歌うさ。▽\nロックンロールは心の中に。\nこの火はまだ、\n消えちゃあいないさ。\n\0":
'???',

# Shinji Ikari
"あ、そういうのいいですね…。\nちょっと僕、憧れるな…。\n\0":
'???',

# Shigeru Aoba
"そうかそうか、なら遠慮すんな。\n俺の横でベース弾けばいい。\n\0":
'???',

# Shinji Ikari
"僕がですか…？\n出来るかな…。\n\0":
'???',

# Shinji Ikari
"でも、さっきの演奏…、\n本当に楽しかったです。\n\0":
'???',

# Shigeru Aoba
"…でも、そのためには\nシンジ君に頑張ってもらって、\n使徒を倒してもらわないとな…。\n\0":
'???',

# Shinji Ikari
"…はい…。\nそうですね！\n\0":
'???',

# Shinji Ikari
"僕、必ず青葉さんを\nミュージシャンに\n戻してみせます！\n\0":
'???',

# [Text Only - No Designated Speaker]
"そうして青葉さんは、\nまたギターを手に取った。\n僕もベースに手を伸ばす。\n\0":
'???',

# Shigeru Aoba
"今度は循環コードでやってみるか。\n指の位置はソコと…、ソコと…\nあ、いや、もう１フレット手前だ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"青葉さんの奏でるアルペジオに\n僕の奏でる低音が絡みつく。▽\n僕は…、再び音とひとつになる\n感覚を捉え始めていた。\n\0":
'???',

# Shigeru Aoba
"調子出てきたな！\nじゃ、もっと行くぜ？\n\0":
'???',

# [Text Only - No Designated Speaker]
"ギターが滑り出すように\nアドリブを奏でた。▽\n僕はただ、余計な事をせず、\n青葉さんの音に重なり合わせる\n事だけに専念した。\n\0":
'???',

# Shigeru Aoba
"ははっ！　いいねぇ！\n乗ってきたね！\n\0":
'???',

# [Text Only - No Designated Speaker]
"青葉さんのギターが突如変わった。\n切り刻むような、高速のリフ。\n\0":
'???',

# Shigeru Aoba
"ホゥっ！\n\0":
'???',

# [Text Only - No Designated Speaker]
"青葉さんは、\n長い髪を振り乱しながら、\n完全に曲とひとつになっている。\n\0":
'???',

# Shinji Ikari
"青葉さん…？\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕の声はもう、\n届かないみたいだった。▽\nまるで、幾千の観客の声が\n青葉さんを包んでいるような、\nそんな錯覚…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"僕は、とりあえず手を止めずに\n適当に合わそうとしたけれど…、\n途中で諦めてしまった。▽\n青葉さんの演奏から、\n何か冒しがたいものを\n感じたからだった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"青葉さんがいるステージに\n僕も続きたかった。▽\nまだまだ、青葉さんには遠いけれど。\nそれでも、追いつきたいと思った。▽\n輝いている青葉さんを見て、\n僕は、もう一度演奏を始めた。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le143.evs
#
# Shinji Ikari
"何を求めるの…僕に。\n\0":
'???',

# Shinji's Shadow [Leliel]
"他人からではなく、\n自分自身による価値。\n\0":
'???',

# Shinji Ikari
"わからないよ…。\n\0":
'???',

# Shinji's Shadow [Leliel]
"それが、君自身が望む事だ。\n価値は誰も与えてはくれない。\n自分以外の誰も。\n\0":
'???',

#
# ./USRDIR/event/b2s09.har_EXTRACT/b2s09.evs
#
# Shigeru Aoba, Male Staff
"使徒、地表に着弾します！\nエヴァ、間に合いません！\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le406.evs
#
# Toji Suzuhara 
"それがどないしてん！\n見栄ぐらい張らせろや。\n\0":
'???',

# Toji's Shadow [Leliel]
"な〜んや、\nやっぱり自覚あったんやん…。\n\0":
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
# ./USRDIR/event/tev1901.har_EXTRACT/tev1901.evs
#
# Keel Lorenz
"約束の時が来た。\nロンギヌスの槍を失った今、\nリリスによる補完は出来ぬ。▽\n唯一、リリスの分身たる、\nエヴァ初号機による遂行を願うぞ。\n\0":
'???',

# Gendo Ikari
"ゼーレのシナリオとは違いますが。\n\0":
'???',

# Kozo Fuyutsuki
"人は、エヴァを生み出す為に\nその存在があったのです。\n\0":
'???',

# Gendo Ikari
"人は、新たな世界へと\n進むべきなのです。\nその為のエヴァシリーズです。\n\0":
'???',

# Seele 06
"我らはヒトの形を捨ててまで、\nエヴァという名の箱舟に\n乗る事はない。\n\0":
'???',

# Seele 05
"これは通過儀礼なのだ。\n閉塞した人類が再生するための。\n\0":
'???',

# Seele 09
"滅びの宿命は、新生の喜びでもある。\n\0":
'???',

# Seele 06
"神もヒトも全ての生命が\n「死」を以って\nやがて一つになる為に。\n\0":
'???',

# Gendo Ikari
"死は何も生みませんよ。\n\0":
'???',

# Keel Lorenz
"死は、君達に与えよう。\n\0":
'???',

# Kozo Fuyutsuki
"人は、生きていこうとするところに\nその存在がある。▽\nそれが、自らエヴァに残った\n彼女の願いだからな。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le004.evs
#
# Shinji's Shadow [Leliel]
"気分はどう？\n\0":
'???',

# Shinji Ikari, Rei Ayanami
"…誰？\n\0":
'???',

# Shinji's Shadow [Leliel], Kozo Fuyutsuki
"碇シンジ。\n\0":
'???',

# Shinji Ikari
"それは、僕だ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"僕は君だよ。\n人は自分の中に\nもう一人の自分を持っている。▽\n自分というのは\n常に、二人で出来ているものなのさ。\n\0":
'???',

# Shinji Ikari
"二人？\n\0":
'???',

# Shinji's Shadow [Leliel]
"実際に見られる自分と\nそれを見つめている自分だよ。▽\n碇シンジという人物だって\n何人もいるんだ。▽\n他人の心の中にいる、碇シンジ。\n皆それぞれ違う碇シンジだけど、\nどれも本物の碇シンジさ。\n\0":
'???',

# Shinji Ikari
"何で、出てきたんだ…。\n\0":
'???',

# Shinji's Shadow [Leliel]
"怖いんだろう？\n他人の中の自分が。\n\0":
'???',

# Asuka's Shadow [Leliel]
"寂しいの？\n\0":
'???',

# Asuka Soryu Langley
"誰？\n\0":
'Who is it?\n\0',

# Asuka's Shadow [Leliel], Kozo Fuyutsuki
"惣流・アスカ・ラングレー。\n\0":
'Asuka Soryu Langley.\n\0',

# Asuka Soryu Langley
"それは私。\n私が惣流・アスカ・ラングレーよ。\n\0":
'That\'s me.\nI am Asuka Soryu Langley.\n\0',

# Asuka's Shadow [Leliel]
"そうよ。\nあなたも、そう。\n惣流・アスカ・ラングレー。▽\nあなたの中のアスカ。\nみんなの中のアスカ。\nそれが私。▽\nいつも心の奥底で泣いている。\n\0":
'???',

# Asuka's Shadow [Leliel]
"いつも…、\n一人になる事を恐れている。\n\0":
'???',

# Rei Ayanami 
"あなたは誰？\n\0":
'Who are you?\n\0',

# Rei's Shadow [Leliel], Kozo Fuyutsuki
"綾波レイ。\n\0":
'Rei Ayanami.\n\0',

# Rei Ayanami 
"あなたも綾波レイなの？\n\0":
'You are also Rei Ayanami?\n\0',

# Rei's Shadow [Leliel]
"そう、みんなが綾波レイと呼ぶもの。\n偽りの魂と作られた体を持つ、\n人のマネをしている物体。\n\0":
'???',

# Rei Ayanami 
"それが私…。\nあなたは本当の私…。\nいつも私を見つめている私？\n\0":
'???',

# Rei's Shadow [Leliel]
"あなたの暗くて見えない心を\n私は知りたい…。▽\nあなたは、一体\n何のために生きているの？\n\0":
'???',

# Toji's Shadow [Leliel]
"…なあ。\n\0":
'???',

# Toji Suzuhara 
"…って、なんやねん！\n\0":
'???',

# Toji's Shadow [Leliel]
"なんやねんて、誰に言うとうねん！\n\0":
'???',

# Toji Suzuhara 
"ワシやんか…。\nなんや、えらい男前や思たわ。\nんで何の用事やねん、ああ？\n\0":
'???',

# Toji's Shadow [Leliel]
"ああって、\n何自分自身にイキってんねん？\nま、自分相手やからキレれんのか。▽\nホンマはヘタレやもんな…。\n周りにヘタレ隠すんに必死やもんな。\n…なんか見苦しいわ。\n\0":
'???',

# Toji Suzuhara 
"なっ…。\n\0":
'???',

# Toji's Shadow [Leliel]
"なあ、ずーっと自分を\n演じ続けていかなあかんのって、\nちょっとしんどないか？\n\0":
'???',

# Kaworu's Shadow [Leliel]
"フフ…\n\0":
'Heh heh...\n\0',

# Kaworu Nagisa 
"これは…？\n\0":
'???',

# Kaworu's Shadow [Leliel]
"僕がわかるかい？\n\0":
'???',

# Kaworu Nagisa 
"…己の内面。\n弱い部分と向き合うなんて、\n未熟なリリンどもの風習だね…。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"その未熟なリリンの物真似が\n上手になったね。\n内面の弱さまで再現してるんだから。\n\0":
'???',

# Kaworu Nagisa 
"………。\n一体、何しに現れたの？\n\0":
'???',

# Kaworu's Shadow [Leliel]
"フフ…。\n確認だよ。\n本来の目的を忘れてはいないかい？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le516.evs
#
# Kaworu Nagisa 
"当然だよ。\nフフ、わかってはいるんだけどね…。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"ずいぶん曖昧な態度だね。\nリリンに感化されすぎたかな。\n\0":
'???',

#
# ./USRDIR/event/tev1307.har_EXTRACT/tev1307.evs
#
# School Broadcast
"２年Ａ組の鈴原トウジ。\n鈴原トウジ。\n至急、校長室まで。\n\0":
'???',

# Kensuke Aida
"何か、やったの？\n\0":
'???',

# Toji Suzuhara 
"心当たりないわ。\nほな、ちょい行って来る。\n\0":
'???',

# Shinji Ikari
"何だろうね、トウジ。\n\0":
'???',

# Kensuke Aida
"さー？\n\0":
'Well?\n\0',

# Kensuke Aida
"ところでさ、シンジ。\nちょいと気になる情報を\n仕入れたんだけど。\n\0":
'???',

# Shinji Ikari
"エヴァ参号機？\n\0":
'???',

# Kensuke Aida
"そう、アメリカで建造中だった奴さ。\n完成したんだろ？▽\n隠さなきゃならない事情も\nわかるけど。\nなあ、教えてくれよ。\n\0":
'???',

# Shinji Ikari
"ホントに聞いてないよ。\n\0":
'???',

# Kensuke Aida
"松代の第２実験場で\n起動実験をやるって噂、\n知らないのか？\n\0":
'???',

# Shinji Ikari
"知らないよ。\n\0":
'???',

# Kensuke Aida
"パイロットはまだ\n決まってないんだろ？\n\0":
'???',

# Shinji Ikari
"わからないよ、そんなの。\n\0":
'???',

# Kensuke Aida
"俺にやらせてくんないかなぁ、\nミサトさん。\n\0":
'???',

# Kensuke Aida
"な、シンジからも頼んでくれよ！\n乗りたいんだよ、エヴァに。\n\0":
'???',

# Shinji Ikari
"ホントに知らないんだよ。\n\0":
'???',

# Kensuke Aida
"じゃ、四号機が欠番になった話は？\n\0":
'???',

# Shinji Ikari
"何、それ？\n\0":
'???',

# Kensuke Aida
"ホントにこれも知らないのか？▽\n第２支部ごと吹き飛んだって、\nパパのところは大騒ぎだった\nみたいだぜ。\n\0":
'???',

# Shinji Ikari
"ミサトさんからは、何も聞いてない。\n\0":
'???',

# Kensuke Aida
"あ、やっぱ末端のパイロットには\n関係ないからな。▽\n言わないって事は、\n知らなくてもいい事なんだろ。\n\0":
'???',

# Kensuke Aida
"すまなかったな、変な事聞いて。\nしかし、トウジの奴遅いなぁ。\n\0":
'???',

# Shinji Ikari
"トウジ、\n校長室に呼び出されたのって\n何だったの？\n\0":
'???',

# Toji Suzuhara 
"ん…、ああ。\nそのうち教えたるわ。\n\0":
'???',

#
# ./USRDIR/event/f087.har_EXTRACT/f087.evs
#
# Asuka Soryu Langley
"バカシンジ、\n何よ、ボーッとしちゃってさ。\n\0":
'???',

# Misato Katsuragi 
"シンちゃん、\n疲れてるんじゃないの。\nダイジョーブ？\n\0":
'???',

# Pen Pen
"グワァ。\n\0":
'???',

# Shinji Ikari
"ウワッ！？\n\0":
'???',

# Asuka Soryu Langley
"やっぱり、最近変よ。\n\0":
'???',

# Misato Katsuragi 
"あれから調子はどうなの…？\n何かとね、こっちは心配だから…。\n\0":
'???',

# Pen Pen
"クー。\n\0":
'???',

# Shinji Ikari
"ううん、僕は何も…。\n大丈夫…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、シンジの声が\n聞こえた気がした…。\n\0":
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
# ./USRDIR/event/tev0211.har_EXTRACT/tev0211.evs
#
# Misato Katsuragi 
"あら、すごいじゃない。\nもうΑΤがこんなに上がったの？▽\nそうね、もうこんな時間だし、\nそろそろ寝た方がいいわね。\n\0":
'???',

# Misato Katsuragi 
"あら、ちゃんとΑΤは\n高く保たれているわね。\nいいわよ、その調子。▽\nさ、今日はもう寝ましょう。\nあなたも疲れたでしょ？▽\nそれじゃ、お休みなさい。\n\0":
'???',

# Misato Katsuragi 
"あら、大丈夫？\nΑΤがあまり高くなっていないわよ？▽\nΑΤは、せめて５０くらいには\n保っておいて欲しいわね。\n\0":
'???',

# Misato Katsuragi 
"さ、今日はもう寝ましょう。\nあなたも疲れたでしょ？\n\0":
'???',

# Misato Katsuragi 
"それじゃ、お休みなさい。\n\0":
'???',

# Misato Katsuragi 
"あら、大丈夫？\nΑΤ、だいぶ低くなっているわ…。▽\nんー、普段からΑΤは\n５０以上は欲しいものね。\n明日から頑張ってちょうだい。\n\0":
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
# ./USRDIR/event/f086.har_EXTRACT/f086.evs
#
# Shinji Ikari
"…。▽\n不思議だな…。\n家に帰れるって事が。▽\nまた、生きてここに帰って。\n何もなかったように\nいつもの生活があるなんて。\n\0":
'???',

# Shinji Ikari
"それは幸せなのかな…。▽\nそれを幸せっていうのかな…。\n\0":
'???',

# Shinji Ikari
"…誰の？\n僕の幸せ…。\n違う…。▽\n生きている限り、\n結局、嫌いな事と一緒に生きて\nいかないといけないんだ。▽\n生きていると\n嫌な事ばかりなんだ。\n\0":
'???',

# Shinji Ikari
"でも、僕は敵を倒して、\nまたこの生活へ戻ってきた…。▽\n何で帰って来たんだろう…。\n\0":
'???',

# Shinji Ikari
"みんなが喜ぶから。\n使徒を倒すとみんなが喜ぶから。\n\0":
'???',

# Shinji Ikari
"…それじゃ、\n僕じゃなくても出来る事だ。▽\n嫌ならやめてもよかったんだ。▽\nでも、捨て切れないんだ。\n\0":
'???',

# Shinji Ikari
"違う…。\n会いたいと、思うんだ。\nそう、思ったんだ…。\n\0":
'???',

# Shinji Ikari
"僕は、会えると信じて\nここに帰るんだ…。\n\0":
'???',

#
# ./USRDIR/event/tev1109.har_EXTRACT/tev1109.evs
#
# [Text Only - No Designated Speaker]
"発令所が、喝采で沸いた。\nリツコは、今までの気迫を\n解放するように、息をついた。\n\0":
'???',

# Misato Katsuragi 
"お疲れさん。\n約束、守ってくれたのね。▽\nやっぱり、マギが\nお母さんだったから？\n\0":
'???',

# Ritsuko Akagi 
"違うと思うわ。\n母さんの事、\nそんなに好きじゃなかったから。▽\n科学者としての判断ね。\n\0":
'???',

# Ritsuko Akagi 
"母さんが死ぬ前の晩、言ってたわ。\nマギは三人の自分なんだって。\n\0":
'???',

# Ritsuko Akagi 
"科学者としての自分、\n母としての自分、\n女としての自分。▽\nその三人がせめぎあっているのが、\nマギなのよ。\n\0":
'???',

# Ritsuko Akagi 
"人の持つジレンマを\nワザと残したのね。▽\n皆同じものだと思ってるけど、\n実はプログラムを\n微妙に変えてあるの。\n\0":
'???',

# Misato Katsuragi 
"…そうなんだ。\n\0":
'???',

# Ritsuko Akagi 
"私は母親にはなれそうもないから、\n母としての母さんはわからないわ。▽\nけど、科学者としてのあの人は\n尊敬もしていた。▽\nでもね、女としては\n憎んでさえいたのよ。\n\0":
'???',

# Misato Katsuragi 
"今日は、おしゃべりじゃない？\n\0":
'???',

# Ritsuko Akagi 
"たまにはね…。▽\nカスパーは、女としてのパターンが\nインプットされていたの。▽\n最後まで女でいる事を守ったのね。\nほんと…、母さんらしいわ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le202.evs
#
# Asuka Soryu Langley
"寂しくなんかない。\nみんなバカばかりだもの。\n一緒にいたくないバカばかり。\n\0":
'???',

# Asuka's Shadow [Leliel]
"他人を見下す事で、\n自分が優位だという\n救いの場が欲しいのよ。▽\n寂しいから。\n一人になった時の\n逃げ道が必要だったのよ。\n\0":
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
# ./USRDIR/event/b2s57.har_EXTRACT/b2s57.evs
#
# Gendo Ikari
"本作戦において、\nロンギヌスの槍を使用する。▽\nレイ、ドグマを降りて\n槍を使え。\n\0":
'???',

# Gendo Ikari
"他は地上にて待機だ。▽\n使徒の出方を見ながら\n対空迎撃戦の用意！\n大遠距離射撃、準備！\n\0":
'???',

#
# ./USRDIR/event/f012.har_EXTRACT/f012.evs
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
# ./USRDIR/event/f006.har_EXTRACT/f006.evs
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
# ./USRDIR/event/n013.har_EXTRACT/n013.evs
#
# Misato Katsuragi 
"全プログラムを消去する作戦を実行します。\n\0":
'???',

# Misato Katsuragi 
"しかし、ΘΑは自動停止しました\n\0":
'???',

# Misato Katsuragi 
"これより、ΘΑ暴走事件の報告を行います\n\0":
'???',

# Misato Katsuragi 
"日本重科学工業共同体が開発した\n使徒迎撃用ロボット、ジェット・アローン、ΘΑは\n\0":
'???',

# Misato Katsuragi 
"しかし、プログラムは変更されており、\n\0":
'???',

# Misato Katsuragi 
"披露会場にて、起動テスト中、\n機体が突如制御不能になり、暴走。\n\0":
'???',

# Misato Katsuragi 
"プログラム消去パスワードは拒否されました。\n\0":
'???',

# Misato Katsuragi 
"今回の事件は、何者かの手により\n仕組まれた可能性が高いと思われます。\n\0":
'???',

# Misato Katsuragi 
"制御棒の作動不能、\n炉心融解の危険、\n自動停止０．００００２％の確率\n\0":
'???',

# Misato Katsuragi 
"作戦を変更し、強制的に制御棒を動かしますが、\n\0":
'???',

# Misato Katsuragi 
"それとは無関係にΘΑは活動を停止しました\n\0":
'???',

# Misato Katsuragi 
"以上の事から、私の独断でΘΑを停止させるべく内部に直接進入し、\n\0":
'???',

#
# ./USRDIR/event/cev0303.har_EXTRACT/cev0303.evs
#
# Female Staff
"ロンギヌスの槍、松代より到着。\nジオフロント内へ移送します。\n\0":
'???',

# Kozo Fuyutsuki
"来たか。\n碇、人類補完計画どおりに\n計画を進めるんだろう。\n\0":
'???',

# Gendo Ikari
"もちろんだ。\n計画は問題無く進められる。\n\0":
'???',

# Male Staff
"ロンギヌスの槍、\nケイジへの移送終了しました。\n\0":
'???',

# Rei Ayanami 
"私、ためらってる…？\nなぜ…、どうして…？\nこの槍を、刺すだけでいいのに。\n\0":
'???',

# Rei Ayanami 
"でも…。\nそれが私の役目なら…！\n\0":
'???',

# Gendo Ikari
"来たか。\n\0":
'???',

# Gendo Ikari
"ご苦労。\n後の作業はレイに引き継ぐ。\n\0":
'???',

# Gendo Ikari
"レイ、後は頼むぞ。\n\0":
'???',

# Gendo Ikari
"神を殺し、\nまた神を生む力を持った\nロンギヌスの槍…か。\n\0":
'???',

# Kozo Fuyutsuki
"とうとうきたな。\nロンギヌスの槍…。\n\0":
'???',

# Kozo Fuyutsuki
"ご苦労、後の作業はレイに引き継ぐ。\n後は任せたぞ、レイ。\n\0":
'???',

# Rei Ayanami 
"はい、冬月副司令。\n\0":
'???',

# Kozo Fuyutsuki
"ここまでは、\nゼーレのシナリオ通りだな。\n…さて。\n\0":
'???',

# Female Staff
"零号機パイロットは、\nロンギヌスの槍の最終移送を\nお願いします。\n\0":
'???',

# Male Staff
"ロンギヌスの槍の移送作業、\n完了しました。\n\0":
'???',

# Female Staff
"了解、人類補完委員会への\n作業完了報告を行います。\n\0":
'???',

#
# ./USRDIR/event/cev0906.har_EXTRACT/cev0906.evs
#
# [Text Only - No Designated Speaker]
"葛城さんとの出来事を知ったら、\nアスカは僕をどう思うだろうか。▽\nそんな事を考えながら、\n僕はすました顔で\nやり過ごしていた。\n\0":
'???',

#
# ./USRDIR/event/bs062.har_EXTRACT/bs062.evs
#
# Shinji Ikari
"み、見えてきました！！▽\nあれが敵…。\n僕たち人類の敵…、使徒…。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le513.evs
#
# Kaworu Nagisa 
"そう、上手く事が運ぶのかな。\nなかなか予定通りには\nいかないと思うけど。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"リリンの僕を軽視すべきじゃないよ。\n予定通りになったらどうするのか…。▽\nきちんと考えておく必要は\nあると思うね。\n\0":
'???',

#
# ./USRDIR/event/cev0209.har_EXTRACT/cev0209.evs
#
# Asuka Soryu Langley
"使徒も全部倒して…。\n私の役目…、終わったのね。\nこれからどうすればいいんだろう。\n\0":
'???',

#
# ./USRDIR/event/tev0221.har_EXTRACT/tev0221.evs
#
# Misato Katsuragi 
"この場合、他人に関わろうとする\n行動は、相手との距離によって\n選択肢が変化するのがわかるわね？\n\0":
'???',

# Misato Katsuragi 
"次に、特定の場所で起こす\n行動について説明するわね。▽\nマップの各所には、何らかの行動を\n行えるトイレの様な場所や\n冷蔵庫の様な物などがあるわ。▽\nそこで%1iボタンを押すと、\n行動選択肢にその場所で\n出来る行動が表示されます。\n\0":
'???',

# Misato Katsuragi 
"そうね、この私の部屋では…。\nシンジ君、このデスクの\n椅子の所へ来てちょうだい。\n\0":
'???',

#
# ./USRDIR/event/f017.har_EXTRACT/f017.evs
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
'???',

#
# ./USRDIR/event/b2s45.har_EXTRACT/b2s45.evs
#
# Kaworu Nagisa 
"くっ…。\nライフラインが…。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le145.evs
#
# Shinji Ikari
"君は…、本当は何者なんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"碇シンジ。\n君だよ。\n\0":
'???',

# Shinji Ikari
"信じられないな。\n\0":
'???',

# Shinji's Shadow [Leliel]
"自分を信頼していないからね。\n\0":
'???',

#
# ./USRDIR/event/f080.har_EXTRACT/f080.evs
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
'???',

#
# ./USRDIR/event/cev0309.har_EXTRACT/cev0309.evs
#
# Rei Ayanami 
"自分の場所は…、自分で見つける。\n私にはその場所が、あるわ…。\n\0":
'???',

# Rei Ayanami 
"待っている人がいる。\n会いたい人がいる。\n\0":
'There is someone waiting for me.\nSomeone I want to see.\n\0',

# [Text Only - No Designated Speaker]
"声がした。\n碇くんの声。\n\0":
'I heard a voice.\nIkari-kun\'s voice.\n\0',

# [Text Only - No Designated Speaker]
"声がした。\nセカンドの声。\n\0":
'I heard a voice.\nThe Second\'s voice.\n\0',

# [Text Only - No Designated Speaker]
"声がした。\nフィフスの声。\n\0":
'I heard a voice.\nThe Fifth\'s voice.\n\0',

# [Text Only - No Designated Speaker]
"声がした。\n私の声。\n\0":
'I heard a voice.\nMy own voice.\n\0',

# [Text Only - No Designated Speaker]
"声がした。\n葛城三佐の声。\n\0":
'I heard a voice.\nMajor Katsuragi\'s voice.\n\0',

# [Text Only - No Designated Speaker]
"声がした。\n葛城一尉の声。\n\0":
'I heard a voice.\nCaptain Katsuragi\'s voice.\n\0',

# [Text Only - No Designated Speaker]
"声がした。\n赤木博士の声。\n\0":
'I heard a voice.\nDr. Akagi\'s voice.\n\0',

# [Text Only - No Designated Speaker]
"会いたい。\n素直にそう思って、駆け出した。\n\0":
'???',

# [Text Only - No Designated Speaker]
"私の心。\n心の向かう先。\n心の向こうのあの人に…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"声がした。\n鈴原くんの声。\n\0":
'I heard a voice.\nSuzuhara-kun\'s voice.\n\0',

# Gendo Ikari
"いよいよその時が来た。\nさあ、行こう、レイ。\n\0":
'???',

# (Decision Prompt)
"ゲンドウについていく／ゲンドウを拒む\0":
'Go along with Gendo／Reject Gendo\0',

# Rei Ayanami 
"いいえ…。\n私は行かないわ…。\n\0":
'No...\nI\'m not going.\n\0',

# Gendo Ikari
"レイ…！\n\0":
'Rei...!\n\0',

# Rei Ayanami 
"私は、与えられた役目の為に\n生きたくない。\n\0":
'???',

# Gendo Ikari
"待ってくれ、レイ！！\n\0":
'Wait for me, Rei!!\n\0',

# Rei Ayanami 
"碇司令…。▽\n人の心を…、\nありがとうございます。▽\nさようなら…。\n\0":
'Command Ikari...▽\nThank you,\n for my human heart.▽\nFarewell...\n\0',

# Gendo Ikari
"レ、レイ…。\n待て、待つんだ、\n待ってくれ、レイ！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"声がした。\n青葉二尉の声。\n\0":
'I heard a voice.\nLt. Aoba\'s voice.\n\0',

# [Text Only - No Designated Speaker]
"声がした。\n相田くんの声。\n\0":
'I heard a voice.\nAida-kun\'s voice.\n\0',

# Shigeru Aoba
"ターミナルドグマより\n高エネルギー体が上昇中！\n人の影なのか、これは？\n\0":
'???',

# Maya Ibuki 
"ターミナルドグマより\n高エネルギー体が上昇中！\n何これ…、人の影？\n\0":
'???',

# Makoto Hyuga
"ターミナルドグマより\n高エネルギー体が上昇中！\n人の影か、何だこいつは？\n\0":
'???',

# Male Staff
"ターミナルドグマより\n高エネルギー体が上昇中！\n人の影のようですが…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"声がした。\n碇司令の声。\n\0":
'I heard a voice.\nCommander Ikari\'s voice.\n\0',

# [Text Only - No Designated Speaker]
"声がした。\nペンペンの声。\n\0":
'I heard a voice.\nPen Pen\'s voice.\n\0',

# Makoto Hyuga, Shigeru Aoba
"分析パターン青！\nまさか、使徒！？▽\nいや、違う。\nヒト、人間です！！\n\0":
'Analysis pattern blue!\nIt can\'t be...an Angel?!▽\nNo, something else.\nIt\'s a person, a human!!\n\0',

# Maya Ibuki 
"分析パターン青！\n…使徒！？▽\nいえ、違う。\nこれ…、ヒト、人間です！！\n\0":
'Analysis pattern blue!\n...An Angel?!▽\nNo, something else.\nIt\'s... a person, a human!!\n\0',

# Female Staff
"分析パターン青！\n使徒！？▽\n違う、これは…、\nヒト、人間です！！\n\0":
'Analysis pattern blue!\n...An Angel?!▽\nNo, it\'s...\nA person, a human!!\n\0',

# [Text Only - No Designated Speaker]
"声がした。\n副司令の声。\n\0":
'I heard a voice.\nThe deputy commander\'s voice.\n\0',

# ??? [Lilith]
"どこへ行くの…。\nあなたが還る場所は、\nここしかないのよ。\n\0":
'???',

# ??? [Lilith]
"私に還りなさい…。\n\0":
'Please return to me...\n\0',

# Rei Ayanami 
"私の役割は…、\n私の生き方は自分で決める。▽\n例え…、長くは生きられなくとも…。\n\0":
'???',

# Rei Ayanami 
"生命の実なんて要らない。\n私は、あなたじゃない。\n私は私。▽\n私は残された時間を、\n自分の意志で生きるわ。\n\0":
'???',

# ??? [Lilith]
"早く…、この身体に…。\n戻って…、\n生命の実を…………………。\n\0":
'Hurry... Return...\nto this body...\nGive me the Fruit of Life......\n\0',

# [Text Only - No Designated Speaker]
"声がした。\n加持さんの声。\n\0":
'I heard a voice.\nKaji-san\'s voice.\n\0',

# [Text Only - No Designated Speaker]
"声がした。\n日向二尉の声。\n\0":
'I heard a voice.\nLt. Hyuga\'s voice.\n\0',

# ??? [Lilith]
"もう、あなたの還る場所は…。\n\0":
'The place you belong is already...\n\0',

# Rei Ayanami 
"溶けていく…。\n\0":
'...melting away.\n\0',

# ??? [Lilith]
"…生命の……………………………\n………………実を…………………\n………………………………………。\n\0":
'The Fruit.........\n.....of Life....\n....Give to.......\n\0\',

# [Text Only - No Designated Speaker]
"声がした。\n伊吹二尉の声。\n\0":
'I heard a voice.n\Lt. Ibuki\'s voice.\n\0',

# [Text Only - No Designated Speaker]
"声がした。\n洞木さんの声。\n\0":
'I heard a voice.\nHoraki-san\'s voice.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le134.evs
#
# Shinji Ikari
"それは自分を殺すって事だ。\n自分という存在を他人の都合に\nあわせるだけだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"自分の中に、\nそれほど譲れないものが\nあるわけじゃないだろ？▽\nただ、傷つきたくないから、\nそういう言い訳をしてるんだ。\n変わる事を恐れてるだけなんだ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le517.evs
#
# Kaworu Nagisa 
"今は…、忘れておきたいんだ…。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"リリンと交わる事に\n耽溺しているようだね。\nフフ、背徳的だ…。\n\0":
'???',

#
# ./USRDIR/event/n005.har_EXTRACT/n005.evs
#
# Misato Katsuragi, Female Staff
"驚異的な攻撃力を持つ使徒に対し\n必死の応戦を行い、\n\0":
'???',

# Misato Katsuragi, Female Staff
"防衛線にて迎撃システムにより交戦するが、\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標は、驚異的な破壊力を持ってこれを一掃、\n\0":
'???',

# Misato Katsuragi, Female Staff
"ただちにエヴァを出撃させ、市街地にて目標と交戦、\n本作戦に出動したエヴァは…\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le518.evs
#
# Kaworu Nagisa 
"いや、僕はアダムだ。\n種の役割を果たすつもりさ。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"フフ、本心の言葉じゃないね。\n…いや、自分を言い聞かせようと\nしているのか。\n\0":
'???',

#
# ./USRDIR/event/tev1904.har_EXTRACT/tev1904.evs
#
# Kozo Fuyutsuki
"使徒の持つ生命の実と、\nヒトの持つ知恵の実。\nその両方を手に入れた。▽\nそして今や、命の胎芽たる\n生命の樹へと還元している。\n\0":
'???',

# Kozo Fuyutsuki
"この先に、サードインパクトの\n無からヒトを救う箱舟となるか、\nヒトを滅ぼす悪魔となるのか。▽\n未来は碇の息子に委ねられたな。\n\0":
'???',

# Keel Lorenz
"遂に、\n我らの願いが始まる。\n\0":
'???',

# Seele 04
"我等人類に福音をもたらす、\n真の姿に。\n\0":
'???',

# Seele 09
"等しき死と祈りを持って、\n人々を真の姿に。\n\0":
'???',

# Keel Lorenz
"それは、魂の安らぎである。▽\nでは、儀式を始めよう。\n\0":
'???',

# Shigeru Aoba
"リリスよりのアンチΑΤフィールド、\nさらに拡大！\n物質化されます！\n\0":
'???',

# Makoto Hyuga
"アンチΑΤフィールド、\n臨界点を突破！\n\0":
'???',

# Shigeru Aoba
"駄目です！\nこのままでは個体生命の形が\n維持出来ません！\n\0":
'???',

# Kozo Fuyutsuki
"ガフの部屋が開く。\n世界の始まりと終局の扉が。\n遂に開いてしまうか。\n\0":
'???',

# Rei Ayanami 
"そして、真実は心の中にある。\n\0":
'???',

# Asuka Soryu Langley
"気持ち悪い。\n\0":
'???',

# Rei Ayanami 
"ここはＬＣＬの海。\n生命の源の海の中。\n\0":
'???',

# Makoto Hyuga
"エヴァ初号機、\n量産機に拘引されていきます。\n\0":
'???',

# Shigeru Aoba
"高度１万２千、さらに上昇中！\n\0":
'???',

# Kozo Fuyutsuki
"ゼーレめ、\n初号機をヨリシロとするつもりか。\n\0":
'???',

# Shigeru Aoba
"エヴァシリーズ、\nΣ機関を解放！\n\0":
'???',

# Shinji Ikari
"う…、ううぅ、ううううぅ。\n\0":
'???',

# Makoto Hyuga
"次元測定値が反転！\nマイナスを示しています。▽\n観測不能。\n数値化出来ません。\n\0":
'???',

# Rei Ayanami 
"何を願うの？\n\0":
'???',

# Kozo Fuyutsuki
"アンチΑΤフィールドか。\n\0":
'???',

# Shinji Ikari
"綾波？\nここは？\n\0":
'???',

# Maya Ibuki 
"全ての現象が、\n１５年前と酷似してる。▽\nじゃあ、これって、\nやっぱりサードインパクトの\n前兆なの？\n\0":
'???',

# Rei Ayanami 
"ΑΤフィールドを失った、\n自分の形を失った世界。▽\nどこまでが自分で、\nどこからが他人なのかわからない、\n曖昧な世界。\n\0":
'???',

# Rei Ayanami 
"どこまでも自分で、\nどこにも自分が居なくなってる\n脆弱な世界。\n\0":
'???',

# Shinji Ikari
"僕は死んだの？\n\0":
'???',

# Kozo Fuyutsuki
"人類の生命の源たるリリスの卵、\n黒き月。▽\n今更、その殻の中へと\n還る事は望まぬ。\nだが、それもリリス次第か。\n\0":
'???',

# Shinji Ikari
"でも、これは違う。\n違うと思う。\n\0":
'???',

# Rei Ayanami 
"他人の存在を今一度望めば、\n再び心の壁が\n全ての人々を引き離すわ。▽\nまた、他人の恐怖が始まるのよ。\n\0":
'???',

# Shinji Ikari
"…いいんだ。\n\0":
'???',

# Shigeru Aoba
"エヴァシリーズの\nΑΤフィールドが共鳴！\n\0":
'???',

# Kaworu Nagisa 
"ヒトの心が自分自身の形を\n造り出しているからね。\n\0":
'???',

# Shinji Ikari, Misato Katsuragi 
"…ありがとう。\n\0":
'???',

# Shinji Ikari
"あそこではイヤな事しか\nなかった気がする。▽\nだから、\nきっと逃げ出してもよかったんだ。\n\0":
'???',

# Shinji Ikari
"でも、逃げたところにも\nいい事はなかった。▽\nだって僕が居ないもの。\n誰も居ないのと同じだもの。\n\0":
'???',

# Makoto Hyuga
"更に、増幅しています！！\n\0":
'???',

# Gendo Ikari
"アダムとリリスの、\n禁じられた融合。\n\0":
'The forbidden fusion\n of Adam and Lilith.\n\0',

# Kaworu Nagisa 
"再びΑΤフィールドが、\n君や他人を傷つけてもいいのかい？\n\0":
'???',

# Shinji Ikari
"構わない。▽\nでも、僕の心の中にいる君達は、\n…何？\n\0":
'???',

# Rei Ayanami 
"希望なのよ。\nヒトは互いにわかり合えるかも\nしれない、という事の。\n\0":
'???',

# Kaworu Nagisa 
"好きだという言葉と共にね。\n\0":
'???',

# Shinji Ikari
"だけどそれは見せ掛けなんだ。\n自分勝手な思い込みなんだ。\n祈りみたいなものなんだ。▽\nずっと続くはずはないんだ。\nいつかは裏切られるんだ。\n僕を見捨てるんだ。\n\0":
'???',

# Shinji Ikari
"でも僕は、\nもう一度会いたいと思った。▽\nその時の気持ちは本当だと、\n思うから。\n\0":
'???',

# Gendo Ikari
"欠けた心の補完。\n不要な身体を捨て、\n全ての魂を今、ひとつに。\n\0":
'???',

# Gendo Ikari
"そして、ユイのもとへ行こう。\n\0":
'And then, we\'ll go where Yui is.\n\0',

# Gendo Ikari
"始めよう、レイ。\nΑΤフィールドを、\n心の壁を解き放つのだ…。\n\0":
'Let\'s begin, Rei.\n Release the wall of your heart,\n your A.T. Field...\n\0',

# Gendo Ikari
"どうした、レイ。\n\0":
'What it is, Rei?\n\0',

# Rei Ayanami 
"私はあなたの人形じゃない。▽\n私はあなたじゃないもの。\n\0":
'???',

# Gendo Ikari
"頼む！\n待ってくれレイ！！\n\0":
'Please!\n Wait for me, Rei!!\n\0',

# Rei Ayanami 
"だめ。\n碇君が呼んでる。\n\0":
'I can\'t.\nIkari-kun is calling.\n\0',

# Rei Ayanami 
"だから、見失った自分は、\n自分の力で取り戻すのよ。▽\n例え、自分の言葉を失っても。\n他人の言葉に取り込まれても。▽\n自らの心で\n自分自身をイメージ出来れば\n誰もがヒトの形に戻れるわ。\n\0":
'???',

# Yui Ikari
"心配ないわよ。▽\n全ての生命には\n復元しようとする力がある。\n生きていこうとする心がある。▽\n生きていこうとさえ思えば…、\nどこだって天国になるわ。\n\0":
'???',

# Yui Ikari
"だって、生きているんですもの。\n幸せになるチャンスは、\nどこにでもあるわ。▽\n太陽と、月と、地球がある限り、\n大丈夫…。\n\0":
'???',

# Rei Ayanami 
"闇の入り口、\nそして、闇の終り。\nそこは、私が帰る場所。▽\n…ただいま。\n\0":
'???',

# Rei Ayanami 
"そして、新たなイメージが\nそのヒトの心も形も変えていくわ。▽\nイメージが、想像する力が、\n自分達の未来を、\n時の流れを造り出しているもの。\n\0":
'???',

# Shinji Ikari
"うん、母さん…。▽\nさよなら…、母さん…。\n\0":
'???',

# Rei Ayanami 
"いいえ、\n全てが一つになっているだけ。▽\nこれがあなたの望んだ世界、\nそのものよ。\n\0":
'???',

# Maya Ibuki 
"レ…イ………？▽\nひ…ぃぁ、\nいやあああぁああ！\nいいぃやああああああ！！\n\0":
'???',

# Shinji Ikari
"綾波………レイ！？\n\0":
'Ayanami..... Rei?\n\0',

# Shinji Ikari
"…………………………………………\n…………………………………………\n……………………………………！？\n\0":
'???',

# Shinji Ikari
"うわああああああああああああ！！\n\0":
'WAAAAHHHHHHHHHH!!\n\0',

# Kaworu Nagisa 
"ただ、ヒトは自分自身の意思で\n動かなければ、何も変わらない。\n\0":
'???',

# Yui Ikari
"もういいのね？\n\0":
'???',

# Shinji Ikari
"幸せがどこにあるのか…\nまだわからない。▽\nだけど、ここにいて、\n生まれて来てどうだったのかは\nこれからも考え続ける。\n\0":
'???',

# Shinji Ikari
"だけど、それも当たり前の事に\n何度も気付くだけなんだ。\n自分が自分でいるために。▽\nでも、母さんは…、▽\n母さんはどうするの？\n\0":
'???',

# Yui Ikari
"シンジや父さんや…、\nみんなが生きた証。▽\n生きていこうとする\nその証のために…。\n\0":
'???',

# Keel Lorenz
"エヴァンゲリオン初号機\nパイロットの欠けた自我を持って\n人々の補完を。▽\n三度の報いの時が、今…。\n\0":
'???',

# Kaworu Nagisa 
"現実は知らないところに。\n夢は現実の中に。\n\0":
'???',

# Asuka Soryu Langley
"…ぐ…ぐぐぅ…ぅ\n\0":
'???',

#
# ./USRDIR/event/cev0402.har_EXTRACT/cev0402.evs
#
# [Text Only - No Designated Speaker]
"使徒との戦いが終わるまで…、\n私はきっと、\n父の姿を追い求めてしまう。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ただ、父の復讐の為だけに\n私は戦っているのかもしれない。▽\nそうやって、\n父からの呪縛を誤魔化す為に。\n\0":
'???',

# Misato Katsuragi 
"いつもいつも、\n母さんは泣いていた。▽\n家に帰らない父さんを\n待ちながら…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"父さんはいつも笑っていた。\nなのに、いつも遠くて。\n母さんや私からは遠くて。▽\n自分の夢の中にばかり\n生きる父を…私は憎んでいた。▽\n嫌いだった。\n家族を放って、笑っていられる\n父が許せなかった。▽\nだけど、最後には、\nセカンドインパクトのあの日には\n私をかばって…父は死んだ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"父を憎んでいたはずなのに、\nあの時の父の顔を忘れられない。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ずっと、ずっと、\nあの父の姿を追い求めている\n私がいる。\n\0":
'???',

# [Text Only - No Designated Speaker]
"私は、セカンドインパクトを\n起こした使徒を倒す為に、\nネルフに入った。\n\0":
'???',

# [Text Only - No Designated Speaker]
"でも、本当は…\n父を求めて、\n父と同じ組織のネルフに入った。\n\0":
'???',

#
# ./USRDIR/event/cev0200.har_EXTRACT/cev0200.evs
#
# Misato Katsuragi 
"あ、アスカ。\nあなたに教えとく事があったわ。\n大事な話よ。\n\0":
'???',

# Asuka Soryu Langley
"なあに？\n\0":
'???',

# Misato Katsuragi 
"画面のここを見て。\n\0":
'???',

# Misato Katsuragi 
"いつ使徒が現れるか、\n大体の目安になるから。▽\n使徒が現れるまでの時間を\n有効に使って、ΑΤやインパルス、\n技能なんかを上げていけばいいわ。\n\0":
'???',

# Asuka Soryu Langley
"あ、そ。\nわかったわ。\n\0":
'???',

# Misato Katsuragi 
"この表示は警戒態勢を表すデフコン、\nディフェンス・コンディションよ。▽\nデフコンは５段階で表現され、\nここでは使徒が出現するまでの\n残りの時間を表すの。\n\0":
'???',

# Misato Katsuragi 
"デフコンは５からカウントが\n開始され、使徒が出現する直前に\nデフコンは１となるわ。\n\0":
'???',

#
# ./USRDIR/event/bs061.har_EXTRACT/bs061.evs
#
# Misato Katsuragi 
"シンジ君、エヴァは基本的に\nケーブルの範囲内でしか\n活動できないの。▽\nでも、予備電源を使えば\nケーブル無しでも活動できるわ。\n\0":
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
# ./USRDIR/event/cev0208.har_EXTRACT/cev0208.evs
#
# Asuka Soryu Langley
"ママ…。\nママ………？\n\0":
'???',

# [Text Only - No Designated Speaker]
"ママに会ったような気がする。\n柔らかくて暖かいママの腕の中。▽\n知らないのに。\n抱きしめられた事なんて\n一度もないのに。▽\n確かに残るママの腕の感触。\n\0":
'???',

# Asuka Soryu Langley
"エヴァの中で…、あの時、\nママが助けてくれた気がする。▽\nママが見ていたような気がする。\n\0":
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
# ./USRDIR/event/cev1408.har_EXTRACT/cev1408.evs
#
# Hikari Horaki
"駄目だなぁ…、駄目だなぁ。\nきっと鈴原、私の事\n嫌いになったんだ…。▽\nどうしよう…。\n\0":
'???',

#
# ./USRDIR/event/tev0236.har_EXTRACT/tev0236.evs
#
# Misato Katsuragi 
"例えば、この空腹。\nお腹が空いていくと、\nここのメーターが減ります。▽\nコレを回復するには、\nさっきの様に食事をとればいいわ。▽\n食堂での食事以外でも、アイテムで\n回復させる事も出来るのよ。\n\0":
'???',

# Misato Katsuragi 
"他も大体同じ。\n\0":
'???',

# Misato Katsuragi 
"水分を回復するには、\n飲み物を飲む。\n\0":
'???',

# Misato Katsuragi 
"眠気を回復するには、\n部屋で眠る。\n\0":
'???',

# Misato Katsuragi 
"ＷＣを回復するには、\nトイレで用を足す。\n\0":
'???',

# Misato Katsuragi 
"風呂を回復するには、\nお風呂に入る。\n\0":
'???',

# Misato Katsuragi 
"そうすれば、\n体調管理はバッチリよ！\n\0":
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
# ./USRDIR/event/tev1405.har_EXTRACT/tev1405.evs
#
# Misato Katsuragi 
"…！！▽\nシンジ君…。\nシンジ君！！\n\0":
'???',

# Maya Ibuki 
"サルベージ計画の要項、\nたった１ヶ月で作成出来るなんて、\nさっすがセンパイですね。\n\0":
'???',

# Ritsuko Akagi 
"残念ながら、原案は私じゃないわ。\nこれは１０年前に、\n既に実験済みのデータなのよ。\n\0":
'???',

# Maya Ibuki 
"そんな事があったんですか？\nエヴァの開発中に。\n\0":
'???',

# Ritsuko Akagi 
"まだ、ここに入る前の出来事よ。\n母さんは立ち会ったらしいけど。\n私は、そのデータしか知らないわ。\n\0":
'???',

# Maya Ibuki 
"その時の結果は、\nどうだったんですか？\n\0":
'???',

# Ritsuko Akagi 
"失敗したらしいわ。\n\0":
'???',

# Misato Katsuragi 
"ケイジに拘束、\n大丈夫でしょうね？\n\0":
'???',

# Makoto Hyuga
"内部に熱、電子、電磁波、\n他、化学エネルギー反応無し。\nΣ機関は完全停止しています。\n\0":
'???',

# Misato Katsuragi 
"にもかかわらず、\nこの初号機は過去３度も動いたわ。▽\n目に見える状況だけでは、\nうかつには触れないわよ。\n\0":
'???',

# Makoto Hyuga
"うかつに手を出すと、\n何をされるかわからない。\n葛城さんと同じですね。\n\0":
'???',

# Maya Ibuki 
"駄目です！\nプラグが排出されます！\n\0":
'???',

# Maya Ibuki 
"エヴァ、信号を拒絶！\n\0":
'???',

# Makoto Hyuga
"プラグ内、圧力上昇！\n\0":
'???',

# Ritsuko Akagi 
"作業中止！\n電源落として！！\n\0":
'???',

# Ryoji Kaji
"いやはや、\nこの展開は予想外ですな。▽\n委員会、いえゼーレの方には\nどう、言い訳つけるつもりです？\n\0":
'???',

# Kozo Fuyutsuki
"初号機は我々の制御下ではなかった。\nこれは不慮の事故だよ。\n\0":
'???',

# Gendo Ikari
"よって、初号機は凍結。\n委員会の別命があるまではだ。\n\0":
'???',

# Ryoji Kaji
"ご子息を取り込まれたままですか？\n\0":
'???',

# Misato Katsuragi 
"人一人助けられなくて、\n何が科学よ…。▽\nシンジ君を返して！▽\n返してよっ！！\n\0":
'???',

# Ritsuko Akagi 
"これがシンクロ率４００％の正体。\n\0":
'???',

# Misato Katsuragi 
"そんな…。\nシンジ君は一体どうなったのよ！？\n\0":
'???',

# Ritsuko Akagi 
"エヴァ初号機に\n取り込まれてしまったわ。\n\0":
'???',

# Misato Katsuragi 
"何よそれ。\nエヴァって何なのよ！？\n\0":
'???',

# Ritsuko Akagi 
"人の造り出した、\n人に近い形をした物体、\nとしか言いようがないわね。\n\0":
'???',

# Misato Katsuragi 
"人の造り出した？▽\nあの時、南極で拾ったものを\nただコピーしただけじゃないの。\nオリジナルが聞いて呆れるわ。\n\0":
'???',

# Ritsuko Akagi 
"ただのコピーとは違うわ。\n人の意思が込められているもの。\n\0":
'???',

# Misato Katsuragi 
"これも誰かの意思だって言うの？\n\0":
'???',

# Misato Katsuragi 
"シンジ君のサルベージ計画？\n\0":
'???',

# Maya Ibuki 
"シンジ君の肉体は、自我境界線を\n失って、細胞がエントリープラグの\n中を漂っている状態と推測されます。\n\0":
'???',

# Ritsuko Akagi 
"シンジ君の精神、\n魂とでも呼ぶべきものも\n一緒にね。▽\nシンジ君を構成していた物質は全て、\nプラグ内に保存されているし、魂と\n呼ぶべきモノもそこに存在している。▽\nつまり、彼の身体を再構成し\n精神を定着させるという計画なの。▽\n現に彼の自我イメージは、\nプラグスーツを\n擬似的に実体化させているわ。\n\0":
'???',

#
# ./USRDIR/event/cev0612.har_EXTRACT/cev0612.evs
#
# Kozo Fuyutsuki
"ラベンダーの香り…？\nああ、アロマオイルか。▽\n…これは、\n実験に使えないだろうか。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le512.evs
#
# Kaworu Nagisa 
"くっ…、\n言うなっ！\n\0":
'???',

# Kaworu's Shadow [Leliel]
"フフ…、見て見ぬふりかい？\n自分の事なのに…。▽\nともかく、\n今後君はどうするつもりなのかな？\n\0":
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
# ./USRDIR/event/cev0308.har_EXTRACT/cev0308.evs
#
# Rei Ayanami 
"月明かり。\n夜の風。\n水の匂い…。▽\nまどろみ漂う眠りの海。\n\0":
'???',

# Rei Ayanami,[Text Only - No Designated Speaker]
"私が私でなくなる感じ。\n私の形がわからなくなる瞬間。▽\n…。▽\n………。▽\n………………。\n\0":
'???',

# [Text Only - No Designated Speaker], Misato Katsuragi, Ritsuko Akagi, Makoto Hyuga, Shigeru Aoba, Maya Ibuki, Gendo Ikari, Kozo Fuyutsuki, Ryoji Kaji
"…！！\n\0":
'???',

# Rei Ayanami 
"夢…？\n今のが夢…？▽\n夢の中の私…、知らない私…。\nどうしてあんな夢を…。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le138.evs
#
# Shinji Ikari
"変わると…、\n今までの僕がなくなるんだ。▽\nせっかく積み上げていた楽しい事が、\n何でもない事に変わってしまうかも\nしれない。\n\0":
'???',

# Shinji's Shadow [Leliel]
"人は皆、変わるよ。\n本当に必要なものを見つめる為に、\n不要になった思い出は手放すものさ。\n\0":
'???',

# Shinji Ikari
"僕の事を忘れる人も…？\n\0":
'???',

# Shinji's Shadow [Leliel]
"いるだろうね。\n人は、昔の自分自身でさえ\n簡単に忘れてしまうものさ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le401.evs
#
# Toji Suzuhara 
"しんどいことあるかいな！\nエエ加減にせぇよ！\n\0":
'???',

# Toji's Shadow [Leliel]
"何、ハッタリかましてんねん。\n全部わかってんねんで？\nええやん、ホンマの自分出したら。▽\n周りの人、みんなエエ人やで？\n\0":
'???',

#
# ./USRDIR/event/b2a00.har_EXTRACT/b2a00.evs
#
# Shigeru Aoba, Male Staff
"使徒落下予想範囲、更新します！\n\0":
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
# ./USRDIR/event/tev1704.har_EXTRACT/tev1704.evs
#
# Asuka Soryu Langley
"はん、\n私が出たって足手まといな\nだけじゃないの？▽\nどうでもいいわよ、もう。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le010.evs
#
# Ritsuko Akagi 
"何てものを…、\n何てものをコピーしたの、私達は。\n\0":
'???',

# Misato Katsuragi 
"エヴァが、ただの第壱使徒の\nコピーじゃない事はわかる。▽\nでも、ネルフは使徒を全て倒した後\nエヴァをどうするつもりなの。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le303.evs
#
# Rei Ayanami 
"私には、果たすべき役割がある。\n\0":
'???',

# Rei's Shadow [Leliel]
"果たし終わったら、残るものは何？\n\0":
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
# ./USRDIR/event/tev1402.har_EXTRACT/tev1402.evs
#
# Kensuke Aida
"シンジ、ここから出ていくって\nホントか？\n\0":
'???',

# Kensuke Aida
"ホントなんだな。\nでも、何故だよ。\n何故、今更逃げんだよ。\n\0":
'???',

# Kensuke Aida
"俺はお前に憧れてたんだ。\nうらやましいよ。\n俺達とは違うんだからな。▽\nチキショウ…、\nトウジまでエヴァに乗れるってのに。\n俺は…。\n\0":
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
# ./USRDIR/event/a011.har_EXTRACT/a011.evs
#
# Kozo Fuyutsuki
"富士の電波観測所はどうした？\n\0":
'???',

# Male Staff
"富士の電波観測所の方は？\n\0":
'???',

# Kozo Fuyutsuki
"何もかもが不明というわけか。\nとりあえず、様子をうかがいつつ、\n市街地から引き離すしかあるまい。\n\0":
'???',

# Female Staff
"何もかもが不明。\nとりあえず、エヴァの発進準備を\n急ぎましょう。\n\0":
'???',

# Female Staff
"ΑΤフィールドがないなんて！？\nどういう事でしょうか…。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le407.evs
#
# Toji Suzuhara 
"ちゃうわい！\nワシはそんな見栄っぱりやない。\n\0":
'???',

# Toji's Shadow [Leliel]
"せやけど、\nオマエそないに運動得意ちゃうやん。▽\nせやのにジャージ着こんでからに…。\nそれがハッタリやっちゅうとうねん。\n\0":
'???',

#
# ./USRDIR/event/cev0501.har_EXTRACT/cev0501.evs
#
# Keel Lorenz
"かねてより危惧されていた使徒\n出現が、ついに現実の事となった。\n\0":
'???',

# Committeeman A
"まぁ、予想通り、世界は大混乱、\nというやつだな。\n\0":
'???',

# Committeeman B
"フン。\n１５年前と同じか。\n\0":
'???',

# Committeeman C
"予測しえない出来事に対しては、\n昔からパニック以外の手段を\n持たないのが我々人間ですからね。\n\0":
'???',

# Committeeman D
"ゲシュタルト崩壊かね。\n当然の事だよ。\n\0":
'???',

# Keel Lorenz
"かといって、\n何もしないわけにはいかん。\n\0":
'???',

# Committeeman A
"そうですな。\n今やエヴァの存在までも\n周知の事実となってしまった。▽\n今日まで隠蔽していた\nネルフの組織活動も\nある程度は、公開せざるを得ない。\n\0":
'???',

# Gendo Ikari, Kozo Fuyutsuki, Ritsuko Akagi, Misato Katsuragi, Female Staff
"使徒の正体、襲来の理由。\n発表しなければならない事は\n山ほどあります。\n\0":
'???',

# Committeeman B
"ハハハ、\n相手の正体もわからずにかね？\n\0":
'???',

# Gendo Ikari
"もちろん真相は控えます。▽\nが、ネルフでは、考え得る限りの\nダミーのシナリオ、及びシミュレー\nションが既に用意してあります。\n\0":
'???',

# Committeeman C
"まさか、再び現れるとはな。\n\0":
'???',

# Committeeman A
"だが、皮肉な事に我々は、この時の\nために巨額の先行投資をしている。\n\0":
'???',

# Committeeman D
"左様。\n現れませんでした、\nではすまされませんぞ。\n\0":
'???',

# Committeeman B
"ネルフとエヴァ、\n無駄にはなりませんでしたな。\n\0":
'???',

# Keel Lorenz
"そいつはわからんよ。\n役に立たなければ、同じ事だ。▽\nいずれにせよ、\nセカンドインパクト。▽\nあの悲劇を繰り返すわけにはいかん。\n\0":
'???',

# Committeeman A
"賛成だな。\nだがそのための時間と\n人と金をどうするか。\n\0":
'???',

# Committeeman D
"頭の痛い問題だな。\n\0":
'???',

# Keel Lorenz
"では、ご苦労だったな。\nあとは委員会の仕事だ。▽\n君たちネルフには\n絶大な権限が委譲されている。▽\n今後の進展に期待してるぞ。\n\0":
'???',

# Gendo Ikari
"わかっています。\n\0":
'???',

# Gendo Ikari
"ユイ…。▽\n全ては、これからだ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le121.evs
#
# Shinji Ikari
"みんな心を隠しすぎるんだ。\nお互いを理解したくないんだよ。▽\n心を隠しているうちは、\n打ち解けるわけが無いんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"自分自身が心を隠しておきながら、\nどうしてそんな事が言えるんだ？\n\0":
'???',

#
# ./USRDIR/event/bs087.har_EXTRACT/bs087.evs
#
# Misato Katsuragi 
"あんた、\n何言ってるか、わかってるの！？\nそんな方法は採れないわ！！\n\0":
'???',

# Male Staff
"そんな、\nこのまま子供を殺すわけには\nいかない！！\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le212.evs
#
# Asuka Soryu Langley
"私はエリートよ。\n選ばれた人間は孤独な存在…。\n誰にも頼りたくないわ。\n\0":
'???',

# Asuka's Shadow [Leliel]
"結局その虚栄心が一番大事なのね…。\n\0":
'???',

#
# ./USRDIR/event/n003.har_EXTRACT/n003.evs
#
# Misato Katsuragi, Female Staff
"その間、２体のエヴァを使用した\n同時荷重攻撃の作戦を立案。\n作戦に使用された機体は…、\n\0":
'???',

# Misato Katsuragi, Female Staff
"イスラフェル\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標は第３新東京市に再侵攻し\n\0":
'???',

# Misato Katsuragi, Female Staff
"同時刻、エヴァでこれを上陸地点にて\n阻止する作戦を立案し、これを実行。\n\0":
'???',

# Misato Katsuragi, Female Staff
"作戦開始後、再び一体に融合\n\0":
'???',

# Misato Katsuragi, Female Staff
"この時、目標は、国連軍の\nΝ地雷によって組織の２０％を損失。\n侵攻を一時押さえる事になりました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"パイロットの同時荷重攻撃により…\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le506.evs
#
# Kaworu Nagisa 
"そうかな？\nアダム側にリリンへの関心が\nまだ不足しているんじゃないかな。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"相互理解をすれば、\n一つの種になれると？▽\n自分でも本気で思ってもいない事を\n口にしないでほしいな。\n\0":
'???',

#
# ./USRDIR/event/a001.har_EXTRACT/a001.evs
#
# Makoto Hyuga, Male Staff
"目標は、超低高度で進行中。\n\0":
'???',

# Misato Katsuragi 
"こちらへ向かっている事以外は\n大きな動きは見られないわね。\n\0":
'???',

# Kozo Fuyutsuki
"こちらへ向かっている事以外は\n大きな動きはないようだが…。\n\0":
'???',

# Female Staff
"こちらへ向かっている事以外は\n大きな動きは見られません。\n\0":
'???',

# Shigeru Aoba, Male Staff
"中央ブロック、収容。\n第６ブロック、閉鎖。\n全館収容完了。▽\n政府及び関係各省へ通達終了。\n\0":
'???',

# Misato Katsuragi 
"あれが、戦闘形態かしら？\n\0":
'???',

# Kozo Fuyutsuki
"あれが、戦闘形態か？\n\0":
'???',

# Female Staff
"あれが、戦闘形態でしょうか？\n\0":
'???',

# Makoto Hyuga, Male Staff
"使徒が進行に障害となるビルを\n破壊しました！▽\n腕部らしきところから出た\n触手によるものです。\n\0":
'???',

# Misato Katsuragi 
"あれが武器ってワケね。\nビルを分断するなんて\n大した破壊力だわ。\n\0":
'???',

# Kozo Fuyutsuki
"あの触手が武器というわけだな。\n\0":
'???',

# Female Staff
"あの触手が、武器という事ですね。\n\0":
'???',

# Makoto Hyuga, Male Staff
"委員会から、\nエヴァの出撃要請が出ました！\n\0":
'???',

# Misato Katsuragi 
"うるさい奴等ね。\n言われなくても出撃させるわよ。\n\0":
'???',

# Kozo Fuyutsuki
"わかっている。\n出撃準備を急げ。\n\0":
'???',

# Female Staff
"了解。\nエヴァ、出撃準備に入ります。\n\0":
'???',

# Makoto Hyuga, Male Staff
"それでは作戦の指揮をお願いします。\n\0":
'???',

# Kozo Fuyutsuki
"了解した。\n\0":
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
# ./USRDIR/event/tev0227.har_EXTRACT/tev0227.evs
#
# Misato Katsuragi 
"部下のΑΤを上げるのも\n上司の仕事！\n\0":
'???',

# Shinji Ikari
"…ΑΤって、何ですか？\n\0":
'???',

# Misato Katsuragi 
"あらら…、大変。\n肝心な事を教えてなかったわね。\n一番重要なパラメータよ。\n\0":
'???',

# Misato Katsuragi 
"ΑΤとは、テンションの様なもの、\n…と思ってちょうだい。\n\0":
'???',

# Shinji Ikari
"テンションですか？\n\0":
'???',

# Misato Katsuragi 
"ΑΤが低い程テンションは沈みこみ、\nΑΤが高い程テンションは高揚して\nいる状態を表すの。\n\0":
'???',

# Shinji Ikari
"じゃあ、さっきの青葉さんは、\n沈み込んでΑΤが低かった事に\nなるんですね？\n\0":
'???',

# Misato Katsuragi 
"そういう事になるわね。\n\0":
'???',

# Misato Katsuragi 
"あなたの現在のΑΤ値は、\n画面のここに表示されているわ。▽\nΑΤは普段の生活や戦闘での\n行動で増減し、\n０から１００の値で表現されるの。▽\nΑΤの変動には、\n常に気をつけていてね。\n\0":
'???',

# Shinji Ikari
"そんなに重要な事ですか？\n\0":
'???',

# Misato Katsuragi 
"何言ってるの！？▽\nΑΤが低かったら、\nエヴァは動かせないどころか\n行動の選択に規制がかかるのよ！\n\0":
'???',

# Shinji Ikari
"そ、そうなんですか…？\n\0":
'???',

# Misato Katsuragi 
"ΑΤが低い時こそ\n出来る行動ってのもあるけど…。\n\0":
'???',

# Misato Katsuragi 
"普段から目安として、５０くらい。\n普通の状態を保っておいて\n欲しいわねー。\n\0":
'???',

# Shinji Ikari
"あの、ミサトさん。\nΑΤの横に表示してある\nインパルスって…？\n\0":
'???',

# Misato Katsuragi 
"そう、これはインパルス。\n衝動力、もしくは動機とでも\n言えばいいかしら。▽\n特殊な行動を実行する為の\n「後押し・きっかけ」を表すの。▽\nインパルスは何かしらの行動により\n蓄積されていくパラメータよ。▽\nインパルスの特徴として、\nΑΤが低い程、辛い体験を行う程\nインパルスは上がりやすくなるの。▽\nインパルスを消費する事で、\n特定の行動や戦闘行動が出来るわ。\n\0":
'???',

# Misato Katsuragi 
"まぁ…、溜まったうっぷんを\nここぞという時吐き出して、\n上手く有効利用しなさいって事よ。\n\0":
'???',

# Misato Katsuragi 
"次は、チョッチ小腹も空いたし\n食堂に行きましょっか。\n\0":
'???',

#
# ./USRDIR/event/tev0240.har_EXTRACT/tev0240.evs
#
# Misato Katsuragi 
"トイレはこっち。\nネルフのトイレはここって\n覚えておいてね。\n\0":
'???',

# Misato Katsuragi 
"チョッチ待ってて。\n\0":
'???',

#
# ./USRDIR/event/cev1303.har_EXTRACT/cev1303.evs
#
# Kensuke Aida
"まずは情報集めだ。\nネルフのスタッフに近づいて、\n色んな情報を聞き出すんだ。▽\n自分に何が足りないのか、\nどうすればパイロットになれるか。\nそれを知る事が出来れば…。▽\nようし、頑張るぞ！\n\0":
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
# ./USRDIR/event/n006.har_EXTRACT/n006.evs
#
# Misato Katsuragi, Female Staff
"アルミサエル\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標は、ΑΤフィールドの反応は\nあるものの、青からオレンジへと\nパターンの変化が周期的に観測され、\n\0":
'???',

# Misato Katsuragi, Female Staff
"マギは回答不能を提示…。\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標のデータが少ない上に、不明な点も多く、\n目標の動きもない事から膠着状態が続きました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"しかし、目標はその形態を変化。\nその後、ゆっくりと移動を開始。\n\0":
'???',

# Misato Katsuragi, Female Staff
"これと同時にエヴァンゲリオン、起動。\n参戦したのは…、\n\0":
'???',

# Misato Katsuragi, Female Staff
"敵の攻撃方法が不明のまま\n出撃という運びとなり、\n接近戦を避けつつ交戦。\n\0":
'???',

# Misato Katsuragi, Female Staff
"本作戦は長期戦となり、\nパイロットは苦戦を強いられるが\n\0":
'???',

# Misato Katsuragi, Female Staff
"無事、作戦は完遂され、\n使徒は殲滅しました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"しかし、突如として目標はエヴァに接触。\n機体への侵食を開始。\n\0":
'???',

# Misato Katsuragi, Female Staff
"目標はエヴァ及び、パイロットと生体融合を果たし、\n分離不能と判断されました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"結果、機体を破棄し、\n使徒殲滅のために自爆装置を発動\n\0":
'???',

# Misato Katsuragi, Female Staff
"機体とともに、目標は殲滅…。\n\0":
'???',

# Misato Katsuragi, Female Staff
"続いて、パイロットの死亡も確認されました…。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le309.evs
#
# Rei Ayanami 
"それでいい、それで構わない。\n私が生き、ここにいる。\n\0":
'???',

# Rei's Shadow [Leliel]
"ただ生きていたいだけなら、\n危険なパイロットを\n辞めなければならない。\n\0":
'???',

#
# ./USRDIR/event/tev1003.har_EXTRACT/tev1003.evs
#
# Kozo Fuyutsuki
"その傲慢が１５年前の悲劇、\nセカンドインパクトを\n引き起こしたのだ。\n\0":
'???',

# Kozo Fuyutsuki
"結果、この有様だ。▽\n与えられた罰にしては、\nあまりにも大きすぎる。\nまさに死海そのものだよ。\n\0":
'???',

# Gendo Ikari
"だが、原罪の汚れなき、\n浄化された世界だ。\n\0":
'???',

# Kozo Fuyutsuki
"俺は罪にまみれていても、\n人が生きている世界を望むよ。\n\0":
'???',

# Naval Officer
"報告します。\nネルフ本部より入電。▽\nインド洋上空衛星軌道上に\n使徒、発見！\n\0":
'???',

# [Text Only - No Designated Speaker]
"かつては氷に覆われていた\n南極大陸。▽\n海水は赤く染まり、\n無数の塩の柱が突き出ている。▽\nまさに死の海といえるそのただ中を、\n大型巡洋艦と数隻の艦隊が\n進んでいく。\n\0":
'???',

# Kozo Fuyutsuki
"いかなる生命の存在も許さない\n死の世界、南極。\nいや、地獄というべきかな。\n\0":
'???',

# Gendo Ikari
"だが、我々人類は\nこうしてここに立っている。\n生物として、生きたままだ。\n\0":
'???',

# Kozo Fuyutsuki
"科学の力で守られているからな。\n\0":
'???',

# Gendo Ikari
"科学は人の力だよ。\n\0":
'???',

#
# ./USRDIR/event/tev1002.har_EXTRACT/tev1002.evs
#
# Shinji Ikari
"綾波…、来てたんだ。\n\0":
'???',

# Rei Ayanami 
"シンクロテストがあったから。\n\0":
'???',

# Shinji Ikari
"今日は…、\n父さんと一緒じゃないんだね。\n\0":
'???',

# Rei Ayanami 
"なぜ？\n\0":
'???',

# Shinji Ikari
"いつも一緒に\nいるように見えるから…。▽\nごめん…、\n憶測だけでそんな事を言って。\n\0":
'???',

# Shinji Ikari
"でも、綾波の方が…、\n僕より父さんの事は\n詳しいんじゃないかな。▽\nいっぱい話…してるじゃないか。\n\0":
'???',

# Rei Ayanami 
"そう…かしら？\n仕事の話しかしないわ。▽\n私も何も知らない。\n碇司令の事。\n碇君の方が…きっと知ってる。\n\0":
'???',

# Shinji Ikari
"そんな事ないよ。\n僕はまだ…何も知らない。\n\0":
'???',

# Shinji Ikari
"ここで父さんが何をしてるのか、\nどこにいるかとか…。\n\0":
'???',

# Rei Ayanami 
"碇司令は今、\n南極に行っているわ。\n\0":
'???',

# Shinji Ikari
"ほら、\nやっぱり綾波の方が\n詳しいじゃないか。\n\0":
'???',

# Rei Ayanami 
"私が知っているのは、\nそういう事だけ。▽\nそれ以上の事は、\n何も知らないわ。\n\0":
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
# ./USRDIR/event/tev0210.har_EXTRACT/tev0210.evs
#
# Misato Katsuragi 
"「テーブルに着く」をして\n「食事をする」を行う事で\n食事が出来るわ。▽\nお腹が空いたら、\nここで腹ごしらえしてちょうだい。\n\0":
'???',

# Misato Katsuragi 
"テレビは自由にどうぞ。\n好きな時間に観ていいのよ。\n\0":
'???',

# Misato Katsuragi 
"で、トイレがココよ。\nここやネルフ以外にも、あちこちに\nトイレはあるから利用してね。\n\0":
'???',

# Misato Katsuragi 
"ここがあなたの部屋よ。\n荷物もソッコーでこっちに\n回してもらったから。▽\nシンジ君が寝る時は、こっちの\n部屋を使って。▽\nまあ、これらの行動は\nこういった特定の場に行って\n%1iボタンを押せば実行出来るわ。▽\n色んな所で試してごらんなさい。\n\0":
'???',

# Pen Pen
"グワァ！\n\0":
'???',

# Shinji Ikari
"わっ！\nペ、ペンギン！？\n\0":
'???',

# Misato Katsuragi 
"あぁ、彼はペンペン。\n新種の温泉ペンギンよ。▽\n私の同居人なの。\n仲良くしてね。\n\0":
'???',

# Shinji Ikari
"え、えーっと…。▽\nよろしく…。\n\0":
'???',

# Pen Pen
"ギャ♪\n\0":
'???',

# Misato Katsuragi 
"じゃあ、寝るにはまだ早いから、\nΑΤを高く保つ練習をしましょう。▽\n私やペンペンに話し掛けたり、\n色んなアクションを試してみて。\n体調も自己管理でね。▽\nコミュニケーションを取りたいなら、\n話し掛けたい相手に近づいて、\n%1iボタンを押すのよ。\n\0":
'???',

#
# ./USRDIR/event/f057.har_EXTRACT/f057.evs
#
# Kensuke Aida [Flashback]
"パパ、今日は何時に帰るの？\n\0":
'???',

# Kensuke's Father
"いやー、ケンスケ。\n今日は泊りになりそうだよ。\n\0":
'???',

# Kensuke Aida [Flashback]
"今日は、じゃなくって\n今日もだろ？▽\nそれに、今日はイタリア料理\n食べに連れて行ってくれる\n約束したじゃんか。\n\0":
'???',

# Kensuke's Father
"今日、行けなくっても\n店は逃げたりしないさ。▽\nそれよりケン坊、\nパパのパソコンまた触っただろ？▽\n勝手にパパの仕事を\n見るんじゃないぞ。\n\0":
'???',

# Kensuke Aida [Flashback]
"わかったよ、パパ。\nちょっと、ゲームをさせて\nもらっただけだよ。\n\0":
'???',

# Kensuke's Father
"ケン坊…。\n\0":
'???',

# Kensuke Aida [Flashback]
"なに、パパ。\n\0":
'???',

# Kensuke's Father
"エヴァのパイロットはケン坊の\nクラスメイトだそうだな…。\n\0":
'???',

# Kensuke Aida [Flashback]
"うん、トモダチなんだ。\n俺も、パイロットになりたいって\n頼んでるけど…、駄目みたい。\n\0":
'???',

# Kensuke's Father
"パパはな…、ケンスケにはあんな\nモノには乗らずに大人になって\n欲しいと思っている…。\n\0":
'???',

# Kensuke Aida [Flashback], Shinji Ikari, Maya Ibuki 
"…え？\n\0":
'???',

# Kensuke's Father
"それじゃ、パパは行くよ。\nあさっての朝は、\nフレンチトーストを食べに行こう。\n\0":
'???',

# Kensuke Aida [Flashback]
"えっ、ホント？\nバナナブレッドもつけてね！\n約束だよ、パパ。\n\0":
'???',

# Kensuke Aida
"…っても…、エヴァに乗ったって、\n乗らなくったって、\n大人になれるよ…。▽\nパパ、\n何を言いたかったんだろう…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、ケンスケの姿が頭によぎった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ケンスケは、雑誌を読んでいる。\nいつものミリタリー雑誌…ではなく、\nグルメガイド雑誌のようだ。\n\0":
'???',

# Shinji Ikari
"第３新東京市エリア版\nグルメガイド？▽\nケンスケ、\nどーしてこんな本読んでるの？\n\0":
'???',

# Asuka Soryu Langley
"あら、この店の…、おいしそ〜。\n\0":
'???',

# Rei Ayanami 
"いつものミリタリー雑誌じゃ\nないのね。\n\0":
'???',

# Hikari Horaki
"わぁ、高そうなお店。\nこんなところに行くの？\n\0":
'???',

# Toji Suzuhara 
"オッヒョ〜、うまそ〜。\nところで、何でお前が\nこんな本読んどるんや？\n\0":
'???',

# Toji Suzuhara 
"いつも、読むのってモデルガンとか\n戦艦とかそんなんばっかやんけ。\n\0":
'???',

# Kaworu Nagisa 
"へえ、色んな店があるんだね。\n\0":
'???',

# Kensuke Aida
"パパと久しぶりに外食するんだ。\n二人で食事なんてめったにないから\nとびきりおいしいのを食べようって。\n\0":
'???',

# Shinji Ikari
"へえ、いいなぁ。\n\0":
'???',

# Asuka Soryu Langley
"へー、この中華の店とか\nどお？\n\0":
'???',

# Rei Ayanami 
"そう、そうなの。\n\0":
'???',

# Hikari Horaki
"いいわね、家族との食事が\n一番楽しいもの。\n\0":
'???',

# Toji Suzuhara 
"へー、\nワイ、こんなこじゃれた店\n行った事ないわ…。▽\n商店街のお好み焼きか、\n焼き肉くらいかのー。\n\0":
'???',

# Kaworu Nagisa 
"へぇ、それはいい事だね。\n\0":
'???',

# Kensuke Aida
"パパ、仕事が忙しくてさ、\nあんまり家で顔合わす事がないんだ。▽\nだから、こんな機会じゃなきゃ\n話せないしね。\n\0":
'???',

# Shinji Ikari
"家族か、いいな…。\n会ったらどんな話するの？\n\0":
'???',

# Asuka Soryu Langley
"へー、親子の仲がいいのね。\nどんな話してるの。\n\0":
'???',

# Rei Ayanami 
"どんな話をするの？\n\0":
'???',

# Hikari Horaki
"お父さんとはどんな話を？\n\0":
'???',

# Toji Suzuhara 
"ふーん、親父とどんな話\nするん？\n\0":
'???',

# Kaworu Nagisa 
"君は、お父さんと\nどんな話をするの？\n\0":
'???',

# Kensuke Aida
"大した事は話さないよ。\n\0":
'???',

# Kensuke Aida
"でも、まあ学校の事とか\n話すかな。▽\nそんなに気を使わなくっても\n何でも話すから。\n\0":
'???',

# Kensuke Aida
"でも、仕事の話はしないかな。\nあんまりしたがらないんだ…。\n\0":
'???',

# Shinji Ikari
"話すのも嫌なほど、\n大変なんだよ。▽\nあのさ、\n何かプレゼントしてみたら？\nヒゲ…剃りとか。\n\0":
'???',

# Asuka Soryu Langley
"ツライ仕事してるからなんじゃ\nない？▽\nアンタがねぎらってあげたら？\n会った時にプレゼントするとかさ。\n\0":
'???',

# Rei Ayanami 
"そう、お父さん、\nネルフの職員だったわね。▽\n何かあげたら？\nお父さんに、いつもの感謝の気持ち。\n\0":
'???',

# Hikari Horaki
"そうだわ。\nお父さんにプレゼントしたら？▽\n靴下とか、ハンカチ。\n仕事大変だねって、\nいつもありがとうって。\n\0":
'???',

# Toji Suzuhara 
"せや、プレゼントしてやれよ。\n親父によ、日頃の感謝みたいなの。\n喜ぶんちゃう？\n\0":
'???',

# Kaworu Nagisa 
"プレゼントなんてどう？\nお父さんにだよ。▽\nきっと、喜ぶと思うよ。\n\0":
'???',

# Kensuke Aida
"いい考えだね！\nウン、そうするよ。\nパパを驚かせよう！！\n\0":
'???',

# Kensuke Aida
"何がいいかな、\n一緒に考えてくれる？\n\0":
'???',

# Shinji Ikari
"うん、いいよ。\n\0":
'???',

# Asuka Soryu Langley
"私にまっかせて〜！\n\0":
'???',

# Rei Ayanami 
"いいわ。\n何がいいかしら。\n\0":
'???',

# Hikari Horaki
"そうね、予算はいくらぐらい？\n\0":
'???',

# Toji Suzuhara 
"やっぱ、肩叩き券かな〜。\n…アカンか？\n\0":
'???',

# Kaworu Nagisa 
"気持ちがこもっていれば何でも\nいいと思うよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"その後もケンスケは、\n父親の事を楽しそうに話した。\nおよそ反抗期とは縁遠いほどに。▽\nケンスケも寂しかったんだなと\n思った。\nそして、少しうらやましくも思った。\n\0":
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
# ./USRDIR/event/f053.har_EXTRACT/f053.evs
#
# Shigeru Aoba [Flashback]
"テルオ、また講義サボリかよ。\n\0":
'???',

# Teruo Kato
"よう、シゲルじゃん。\n今日は休講だったんだよ。▽\nそうだ、キリコに聞いたよ。\nお前、内定もらったんだって？\n\0":
'???',

# Shigeru Aoba [Flashback]
"ああ、まさか受かると思って\nなかったけどさ。\n\0":
'???',

# Teruo Kato
"そっかー、よかったな。▽\nシゲルはさ、俺達よりも出来るし、\n色々活躍出来ると思うよ。\n\0":
'???',

# Shigeru Aoba [Flashback]
"それよりさ、\n事務所と契約したんだろ。\nどうなんだ？\n\0":
'???',

# Teruo Kato
"あー、お前の代わり\n…のギタリストと会わされた。\nで、これでユニット組んでくれって。▽\nユニット名も勝手に変えられてさ、\n「コバルトスカイ」だってよ。\nダッサイの！！▽\n………。▽\nシゲル…さ、\n一緒にやれると思ってたのに、\n本当にいいのかよ？▽\nギターで、食っていくって\nいっつも言ってただろ。▽\nプロデビューのチャンスなんだぜ。\n\0":
'???',

# Shigeru Aoba [Flashback]
"………。▽\n俺、本当は事務所からギターの\n才能ないって言われてね。\nだから、俺は外されたんだ。▽\n…それに、音楽で食っていく\nなんて考えていたら…、\n\0":
'???',

# Shigeru Aoba
"俺が、大人になれねーしな。\n\0":
'???',

# Kozo Fuyutsuki
"何を言っている…？\n\0":
'???',

# Ritsuko Akagi, Shinji Ikari
"どうしたの…？\n\0":
'???',

# Maya Ibuki 
"何さっきからブツブツと…？\n\0":
'???',

# Makoto Hyuga
"よう、何言ってるんだ？\n\0":
'???',

# Misato Katsuragi 
"青葉クン、どーしたの？\n\0":
'???',

# Ryoji Kaji
"何が大人になれないって？\n\0":
'???',

# Toji Suzuhara
"ハァ？\n\0":
'???',

# Asuka Soryu Langley
"その、自虐的な笑いはナニ？\nまさか、フラれたのかしら？\n\0":
'???',

# Kaworu Nagisa 
"大人がどうとかって、\n何ですか？\n\0":
'???',

# Female Staff
"何の話なんです、それ？\n\0":
'???',

# Shigeru Aoba
"あ、いや…、\n独り言で…。\nこれは、何でも…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、青葉の姿が頭によぎった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ここへ来る途中に、\n素敵な歌を聴いた。▽\n今日発売の「コバルトスカイ」と\nいうユニットの新曲だ。▽\nけれども、ずいぶん前から\nその曲を知っていた。▽\n青葉シゲルがいつも\nこの曲を弾いていたからだ。\n\0":
'???',

# Shinji Ikari
"青葉さんのいつも弾いている曲、\n今日聴きました。\nあれって…。\n\0":
'???',

# Asuka Soryu Langley
"青葉さんがギターで\nいつも弾いてる曲。\n何ていうんですか？\n\0":
'???',

# Rei Ayanami 
"青葉さんがいつも弾いてる曲。\n私、ここに来る途中で聴きました。\n\0":
'???',

# Maya Ibuki 
"ギターでいつも弾いてる曲、\nテレビで聴いたんですよ。▽\nでも、新曲なのに\n何で知ってるんですか？\n\0":
'???',

# Makoto Hyuga
"なぁ、\nいつもギターで弾いてる曲さぁ、\nここに来る時、テレビで聴いたんだ。▽\n新曲らしいけど、\n何で君があの曲知ってるの？\n\0":
'???',

# Toji Suzuhara 
"青葉さん、\nいつもギター弾いてはる時の曲、\n今日、新曲でテレビに出てましたよ。\n\0":
'???',

# Kaworu Nagisa 
"青葉さんのいつも弾いている曲、\nテレビで聴きました。▽\nでも、新曲って言うから、\n青葉さんは知らないはずなのに…。\n\0":
'???',

# Shigeru Aoba
"ひょっとして、\n「コバルトスカイ」っていう\nユニットの？\n\0":
'???',

# Shigeru Aoba
"へへへ、あれはね、\n実は俺が作った曲なんだ。\n\0":
'???',

# Shinji Ikari
"えぇっ！？\nほ、本当なんですか！？\n\0":
'???',

# Asuka Soryu Langley
"うそっ！？\nすっごーい！！\n\0":
'???',

# Rei Ayanami 
"本当、ですか？\n\0":
'???',

# Maya Ibuki 
"うそっ！？\nど、どうして、何でなんですか！！\n\0":
'???',

# Makoto Hyuga
"えーーーーーっ！？\nそれ、本当なのかい！？\n\0":
'???',

# Toji Suzuhara 
"ま、マジっすか！？\n\0":
'???',

# Kaworu Nagisa 
"すごい、\nすごいじゃないですか！！\n\0":
'???',

# Shigeru Aoba
"なーんてな、ウソだよ。\nそんな事があるわけないだろ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"青葉は笑って否定したが、\nその後、少し自嘲の笑みを見せた。\n本当は、何かを隠しているようだ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"青葉が、ギターを抱えて歩いている。▽\nヒマな時はいつもギターを手に\n歌っているようだ。\n\0":
'???',

# Misato Katsuragi 
"いつも、そのギターと一緒なのね。\n\0":
'???',

# Gendo Ikari
"毎日、持ち帰っているようだが、\nそんなに大事なものなのか？\n\0":
'???',

# Kozo Fuyutsuki
"重そうだな。▽\nしかし、肌身離さず持ち歩くとは\n君にとってよほど、\n大事なものなんだね。\n\0":
'???',

# Ritsuko Akagi 
"あら、ギタリストさん。\n休憩かしら？\n今からギターを弾くのね。\n\0":
'???',

# Ryoji Kaji
"君は本当にそのギターが\n好きなんだね。▽\n俺なら、そんな重いモノ持って\n出勤なんてとても出来ないよ。\n\0":
'???',

# Shigeru Aoba
"ああ、こいつはね、\nもう恋人みたいなもんですよ。▽\n高校２年の時に買って、\nそれからずっと一緒ですね。▽\n本当は、こいつで食っていこう\nなんて思っていた頃もありましたよ。▽\nまあ、夢に終わりましたけど…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"青葉は少し寂しそうに笑って、\nそれから大袈裟なほど敬礼をして、\n歩いていった。\n\0":
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
# ./USRDIR/event/f026.har_EXTRACT/f026.evs
#
# [Text Only - No Designated Speaker]
"$aの目の前に\n黒服の男達が立ちはだかった。\n\0":
'???',

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
'???',

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
'???',

# [Text Only - No Designated Speaker]
"一発の銃弾が身体を突き飛ばした。▽\n薄れる意識の中で最後に見たものは\n冷たい地面に広がる\n自分の血だまりだった。\n\0":
'???',

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
'???',

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
'???',

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
'???',

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
'???',

# [Text Only - No Designated Speaker]
"黒服の男とすれ違った。\n\0":
'???',

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
'???',

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
'???',

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
'???',

#
# ./USRDIR/event/cev0106.har_EXTRACT/cev0106.evs
#
# Gendo Ikari
"シンジ、\n何を突っ立っている。\n\0":
'???',

# [Text Only - No Designated Speaker]
"クラス中がまた、\nざわつき始めた。▽\nもう、帰りたい…。\n\0":
'???',

# Shinji Ikari
"…出来るわけないよ。\n出来るわけないよ！！\nこんな状況で…！▽\n来るなら普通に来てよ、\n父さん…。\n\0":
'???',

# Shinji Ikari
"理由になってないよ、父さん！\n\0":
'???',

# Gendo Ikari
"時間だ。\n先に帰るぞ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"今日は父兄参観だ。▽\nクラスメイトの親族で\n教室はごった返しだ。\n\0":
'???',

# Hikari Horaki
"あっ…、お父さん。\nこっち見てる…。\n\0":
'???',

# Toji Suzuhara 
"わ、オジーが来とるやん。\nアカン、マジメしとかんと\nカミナリ落ちるわ。\n\0":
'???',

# Kensuke Aida
"パパだ。\n来てくれたんだ！\n\0":
'???',

# [Text Only - No Designated Speaker]
"もちろん、\n父さんはこんな所に\n来てくれるわけもなく…。\n\0":
'???',

# Kensuke Aida, Hikari Horaki, Toji Suzuhara, Kaworu Nagisa, Asuka Soryu Langley, Rei Ayanami, Shinji Ikari,[Text Only - No Designated Speaker], Maya Ibuki 
"…………………………。\n\0":
'???',

# Kensuke Aida
"こ、校庭にＶＴＯＬ！？\nすげぇ！！\n\0":
'???',

# Hikari Horaki
"校庭に、戦闘機が…？\n\0":
'???',

# Toji Suzuhara 
"な、何や！？\n何で校庭に戦闘機が！！\n\0":
'???',

# Kaworu Nagisa 
"ＶＴＯＬ重戦闘機。\nネルフ専用機だ…。\nどうして学校なんかに？\n\0":
'???',

# Asuka Soryu Langley
"え、何なの？\nこんな所にＶＴＯＬが。\n何か緊急事態なの！？\n\0":
'???',

# Rei Ayanami 
"碇司令だわ…。\n\0":
'???',

# Shinji Ikari
"……………………。▽\n帰って、寝よう…。\n\0":
'???',

# Shinji Ikari
"…えぇぇぇぇ！？\nと、父さん！？\n\0":
'???',

# [Text Only - No Designated Speaker]
"…しまった、…つい。▽\n一斉にクラスメイトや父兄の視線が\n僕に集中する。▽\n針のムシロっていうのは、この事だ。\n\0":
'???',

# Kensuke Aida
"シンジの、お父さん…。\n\0":
'???',

# Hikari Horaki
"碇君の…、お父さん。\n\0":
'???',

# Toji Suzuhara 
"シンジ…、\nオマエのおとん、すげぇ…。\n\0":
'???',

# Kaworu Nagisa 
"碇司令、そうかシンジ君の\n授業を参観しに来たのか。\n\0":
'???',

# Asuka Soryu Langley
"ウソ…、大ゲサ…。\n\0":
'???',

# Shinji Ikari
"ハハ…、ハハハ…。\nねえ、みんな。\n授業…続けようか…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"…そうは言っても、\nなかなかみんな落ち着かない。\n先生までも、緊張している。\n\0":
'???',

# Teacher
"じゃあ、この問題わかる人…。\n\0":
'???',

# Shinji Ikari
"（こんな状況で、\n　何が出来るってんだ…。）\n\0":
'???',

# Gendo Ikari
"シンジ。\n何故、手を上げない。\n\0":
'???',

# [Text Only - No Designated Speaker]
"小一時間、トイレで泣いた。▽\n父さんが来てくれたのは\n嬉しかったけど…。▽\nやっぱり僕と父さんの間には、\n隔たりがあるのだと…。\nそれを痛感させられてしまった。\n\0":
'???',

# Teacher
"…じ、じゃあ、碇君…。\n前に出てやってみるかね？\n\0":
'???',

# Shinji Ikari
"あの…、僕は…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"おずおずと席を立つ事しか\n出来なかった。▽\n父さんが…見ている。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le514.evs
#
# Kaworu Nagisa 
"大丈夫さ。\n僕は生を諦めるつもりはないよ。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"それは\nリリンを全滅させるって意味だね。▽\nその後、\n君の生の意味を知るものはいるの？\n君一人で生き永らえてどうするの？\n\0":
'???',

#
# ./USRDIR/event/bs074.har_EXTRACT/bs074.evs
#
# (Decision Prompt)
"もう一度説明から／もう一度実践から／今日はもうやめておく\0":
'???',

# Misato Katsuragi 
"わかったわ、\nちょっと無理させてごめんなさい。\n今日の訓練は終わりにしましょう。▽\n今日教えた事は忘れないように\nしっかり覚えといてね。\n\0":
'???',

#
# ./USRDIR/event/cev0117.har_EXTRACT/cev0117.evs
#
# Maya Ibuki, Makoto Hyuga, Shigeru Aoba
"エヴァシリーズ、沈黙…！！\n\0":
'The Eva Series has gone silent!\n\0',

# Kozo Fuyutsuki
"…勝ったか。\n\0":
'Did we win?\n\0',

# Makoto Hyuga
"よくやった…、\nあのエヴァシリーズに勝つなんて。\n\0":
'???',

# Shigeru Aoba
"やった！！\n勝ったぜ！！\n\0":
'???',

# Maya Ibuki, Female Staff
"早く、機体とパイロットの\n回収を急ぎましょう。\n\0":
'???',

# Shinji Ikari
"僕は………、▽\n僕は………………。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ここに来てすぐの時は、\n仕方なくエヴァに乗ってた。▽\nそうするしか、僕に価値はなく、\nそれが、ずっと続くと思っていた。▽\nでも………。▽\nいつの間にか僕は…、\n自分の意志でエヴァに乗るように\nなっていた。\n\0":
'???',

# Shinji Ikari
"大事なもの…。\n\0":
'???',

# Shinji Ikari
"大好きなもの…。\n\0":
'???',

# Shinji Ikari
"僕が守りたかったもの…。\n\0":
'???',

# Shinji Ikari
"僕を変えていってくれたもの…。\n\0":
'???',

# Shinji Ikari
"僕が変えていったこと…。\n\0":
'???',

# Shinji Ikari
"痛みも知ったけど…、\n\0":
'???',

# Shinji Ikari
"でもこの世界が好きなんだ。\n\0":
'???',

# Shinji Ikari
"僕は、ここにいたい。\n僕がいて、みんながいる\n大好きなこの世界に。\n\0":
'???',

# Asuka Soryu Langley
"バカシンジ。\n\0":
'???',

# Rei Ayanami 
"碇君…。\n\0":
'???',

# Pen Pen
"クァ、グァ、\nクァックァックァ〜。\n\0":
'???',

# Toji Suzuhara 
"シンジ。\n\0":
'???',

# Kensuke Aida
"シンジ！\n\0":
'???',

# Hikari Horaki
"碇君。\n\0":
'???',

# Gendo Ikari
"シンジ…。\nよくやったな。\n\0":
'???',

# Shinji Ikari
"よかった…。\nみんなが…無事で。\n\0":
'???',

# [Text Only - No Designated Speaker]
"いつものみんなの顔。\n守りたかった人達…。\n\0":
'???',

# Shinji Ikari
"僕…、この世界が好きだ。\nみんながいるこの世界が。▽\n…父さん？\n\0":
'???',

# Shinji Ikari
"ありがとう。\n僕、父さんが呼んでくれた\nおかげで…。\n\0":
'???',

# Gendo Ikari
"シンジ…。▽\nありがとう。\n\0":
'???',

# Shinji Ikari
"ありがとう、父さん。\n\0":
'???',

# [Text Only - No Designated Speaker]
"不安や寂しさ、辛さは、\nいつか消える日が来る。\n\0":
'???',

# [Text Only - No Designated Speaker]
"足元を見れば、小さな幸せが\n溢れている事に気づく日が来る。\n\0":
'???',

# [Text Only - No Designated Speaker]
"この先もずっと、ずっと…、\n僕はこの世界を抱きしめながら\n生きるのだろう。\n\0":
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
'???',

# Shinji Ikari
"開け、開け、開けッ！！\n\0":
'???',

#
# ./USRDIR/event/tev0501.har_EXTRACT/tev0501.evs
#
# Gendo Ikari
"…また君に借りが出来たな。\n\0":
'???',

# ??? [Kaji on phone]
"返すつもりないんでしょ？▽\n彼らが情報公開法をタテに\n迫ってきた資料ですが、ダミーも\n混ぜてあしらっておきました。▽\n政府は裏で法的整備を進めてますが、\n近日中に頓挫の予定です。▽\nで、どうです？\n例の計画の方も、\nこっちで手を打ちましょうか？\n\0":
'???',

# Gendo Ikari
"いや、君の資料を見る限り、\n問題はなかろう。\n\0":
'???',

# ??? [Kaji on phone]
"では、シナリオ通りに。\n\0":
'???',

# [Text Only - No Designated Speaker]
"こうして授業を受けていると、\n自分がエヴァのパイロットだと\nいう事が嘘のようだ。▽\nクラスを見回すと、あの使徒と\n呼ばれる存在の襲来でほとんどの\n生徒は疎開し、人数はまばらだった。▽\nそして、改めて…、今までの事が\n現実だったんだという思いが\n頭をもたげてくるのだ。▽\n自分がエヴァのパイロットなんだと\n再び認識する…。\n\0":
'???',

# Teacher
"２０世紀最後の年、\n宇宙より飛来した大質量の隕石が\n南極に衝突、▽\n氷の大陸を一瞬にして\n溶解させたのであります。▽\n海洋の水位は上昇し、地軸も曲がり、\n生物の存在をも脅かす異常気象が\n世界中を襲いました。▽\nそして、数千種の生物と共に、\n人類の半分が永遠に失われたので\nあります。▽\nこれが世に言う、\nセカンドインパクトであります。\n\0":
'???',

# Kensuke Aida
"シンジ、屋上行こうぜ。\n国連軍の航空演習のコースが\n学校の真上なんだ。▽\nそろそろ時間なんだよ。\n\0":
'???',

# Shinji Ikari
"授業中じゃないか。\n\0":
'???',

# Kensuke Aida
"あの先生、セカンドインパクトの\n話になったら止まらないんだ。▽\nいいよ、いいよ。\n毎回話す事、同じなんだもん。\n\0":
'???',

# Toji Suzuhara 
"ほな、行くで。\nそーっとな！\n\0":
'???',

# Shinji Ikari
"もぉ…。\n\0":
'???',

# Toji Suzuhara 
"あー、ええ天気や。\n\0":
'???',

# Shinji Ikari
"こういうの、\nしょっちゅうやってるの？\n\0":
'???',

# Kensuke Aida
"まあ…。\nあの先生がセカンドインパクトの\n話を始めたらね。▽\nま、後で委員長から\n説教食らうぐらいさ。\n\0":
'???',

# Toji Suzuhara 
"ホンマ、あの女うるさいわ。\nミサトさんとは大違いやな。\n\0":
'???',

# Kensuke Aida
"美人だし。\nネルフの作戦担当でさ。\nかーっこいいよな。\n\0":
'???',

# Toji Suzuhara 
"あんな姉さん、\nワシも欲しーわ。\n\0":
'???',

# Shinji Ikari
"意外とガサツだよ。\n部屋とか汚いし、ビールばっかり\n飲んでだらしないし。▽\n僕は、トウジやケンスケみたく、\n家族が一緒の方が…。\n\0":
'???',

# Kensuke Aida
"俺、父親と二人暮しだよ。\n滅多に顔も合わさない。\nいっつも仕事で家にいないし。\n\0":
'???',

# Toji Suzuhara 
"ワシも、家族は\nおとんとおじんと妹やけど…。▽\nまぁ、妹は入院中やろ。\nおとんとおじんは仕事で、\n家族集合ちゅうんは滅多にないな。\n\0":
'???',

# Kensuke Aida
"だから、やっぱりうらやましいよ。▽\nだらしないところってのは、\nきっと、他人の俺達には見せない\n無防備な姿なんだよ。▽\nミサトさんは、シンジが家族だから\nそんな風に無防備になれるのさ。\n\0":
'???',

# Toji Suzuhara 
"俺らよりも、家族らしい家族が\nおるんや。\nしかも、ごっついベッピンさんの。\n\0":
'???',

# Kensuke Aida
"そー、そー。\nあんな綺麗な人と住んでて\nエヴァを操縦出来るんだ。▽\nうらやましいよ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le302.evs
#
# Rei Ayanami 
"私、自分がわからない。\n\0":
'I don\'t understand myself.\n\0',

# Rei's Shadow [Leliel]
"自分という存在に興味が無いのね。\n生きる事を放棄している。\n\0":
'???',

#
# ./USRDIR/event/tev1309.har_EXTRACT/tev1309.evs
#
# Misato Katsuragi 
"じゃあ、出張で\nしばらく家を空けるけど、\n戸締りとかヨロシクね。\n\0":
'???',

# Shinji Ikari
"あの、松代ですか？\n参号機の起動実験なんでしょ。\n\0":
'???',

# Misato Katsuragi 
"知ってるの？\n\0":
'???',

# Shinji Ikari
"あの、パイロットは\n決まったんですか？\n\0":
'???',

# Ritsuko Akagi 
"ミサト、急いで。\nまだ支度してるの？\n\0":
'???',

# Misato Katsuragi 
"じゃあ…、帰ったら話すわ。\n\0":
'???',

# Ritsuko Akagi 
"そう、じゃあシンジ君は\nまだパイロットが誰か\n知らないわけね。\n\0":
'???',

# Misato Katsuragi 
"とうとう言い出せなかったわ。\n四号機の事故の後でもあるし。\n\0":
'???',

# Ritsuko Akagi 
"しっかりしなさいよ。\n自分で保護者、\n買って出たんじゃない。\n\0":
'???',

# Misato Katsuragi 
"そうなんだけどねぇ…。\n彼が自分からシンジ君に\n言い出すかもしれないし…。\n\0":
'???',

# Ritsuko Akagi 
"それはないわね。\n人に自慢するほど、\n喜んでもなかったもの。\n\0":
'???',

# Ritsuko Akagi 
"入院治療中の妹を本部の医学部に\n転院させてくれって言うのが\n彼が出した条件だったのよ。\n\0":
'???',

# Ritsuko Akagi 
"さあ、行くわよ。\n\0":
'???',

# Hikari Horaki
"す…、鈴原。\n\0":
'Su-Suzuhara.\n\0',

# Toji Suzuhara 
"何や、委員長やないけ。\n\0":
'???',

# Hikari Horaki
"また…妹さんの見舞い？\n\0":
'???',

# Toji Suzuhara 
"うんにゃ、ちょっとな…。▽\n委員長こそ、何でここおるん。\nこっちは、お前ンとこから\n学校と反対方向やんか。\n\0":
'???',

# Hikari Horaki
"…そ、そっちこそ。\n通学カバンも持たずに。\n学校サボる気なの…！\n\0":
'???',

# Toji Suzuhara 
"ちゃうわ。\nお前にも、そのうち話すし。\nほな、行くわ。\n\0":
'???',

# Hikari Horaki
"あ……………。▽\n待って！！\n\0":
'???',

# Toji Suzuhara 
"説教やったら、帰って聞くわ。\n\0":
'???',

# Hikari Horaki
"そうじゃなくって、コレっ！\nお弁当…。\n\0":
'???',

# Toji Suzuhara 
"弁当て何やねん、唐突に。\n何や仕込んどるんとちゃうか。\n\0":
'???',

# Hikari Horaki
"もうっ、そんな事するわけ\nないでしょ！！\n\0":
'???',

# Hikari Horaki
"鈴原が、いつもコンビニ弁当\nばっかりだから…。\n\0":
'???',

# Toji Suzuhara 
"は…、そか…。\n…おおきに。\nせやけど、要らんわ。\n\0":
'???',

# Hikari Horaki
"え………………。\n\0":
'???',

# Toji Suzuhara 
"何か…、胸一杯でなぁ。\n食われへんと思う。▽\nせやから…、\nまた今度作っといてくれよ。\n\0":
'???',

# Hikari Horaki
"う、うん。\n\0":
'???',

# Toji Suzuhara 
"じゃあな、委員長…。\n\0":
'???',

# Ritsuko Akagi 
"機体の準備も順調ね。\nこれだと即、実戦も可能だわ。\n\0":
'???',

# Misato Katsuragi 
"ふぅん、そう。\nよかったわね。\n\0":
'???',

# Ritsuko Akagi 
"気のない返事ね。\nこの機体も納入されれば、\nあなたの直轄部隊に配属されるのよ。\n\0":
'???',

# Misato Katsuragi 
"エヴァを４機も独占…か。\nその気になれば、\n世界を滅ぼせるわね。\n\0":
'???',

# Female Staff
"フォース・チルドレン、\n到着しました。\n起動実験の開始、お願いします。\n\0":
'???',

# Kensuke Aida
"そうか。\n今日が、参号機の起動実験なんだ。\n\0":
'???',

# Shinji Ikari
"うん。\nミサトさんも松代に行ってるよ。\n\0":
'???',

# Kensuke Aida
"いいなぁ。\n誰が乗るのかなぁ。\n\0":
'???',

# Kensuke Aida
"トウジの奴かな。\n今日、休んでるし。\n\0":
'???',

# Makoto Hyuga
"もう実験が始まってる\n時間だろうな。\n\0":
'???',

# Shigeru Aoba
"慌ててこちらによこしてきた\n機体だ。\n一筋縄ではいかないんじゃないかな。\n\0":
'???',

# Ryoji Kaji
"フォース・チルドレンが\nこの子と言うことは、\nエヴァ参号機のコアは…。\n\0":
'???',

# Maya Ibuki 
"…そんな事、\n私にはわかりません！\n\0":
'???',

# Toji Suzuhara 
"すまんな、転校生。\nワシはお前を殴らないかん。\n殴っとかな、気が済まへんのや。▽\nお前のせいで妹は…。\n\0":
'???',

# Shinji Ikari
"僕だって、\n乗りたくて乗ってるわけじゃ\nないのに…。\n\0":
'???',

# Ritsuko Akagi 
"どうしたの！？\n\0":
'???',

# Ritsuko Akagi 
"何ですって！！\n\0":
'???',

# Kozo Fuyutsuki
"松代で爆発事故！？\n\0":
'???',

# Gendo Ikari
"被害は？\n\0":
'???',

# Makoto Hyuga
"地下の仮設ケイジは消滅しましたが、\n幸い、第２実験場の施設は\n原形を留めています。\n\0":
'???',

# Shigeru Aoba
"連絡は未だ取れません。\nですが、生存者の可能性は、\n大です。\n\0":
'???',

# Gendo Ikari
"救助部隊を直ちに派遣。\n戦自が介入する前に全て処理しろ。\n\0":
'???',

# Makoto Hyuga
"事故現場に未確認物体を発見。\n映像、捉えました。\n\0":
'???',

# Kozo Fuyutsuki
"やはり、これか。\n\0":
'???',

# Gendo Ikari
"活動停止信号を発信。\nエントリープラグを強制射出。\n\0":
'???',

# Maya Ibuki 
"駄目です。\n停止信号及びプラグ排出コード、\n認識しません。\n\0":
'???',

# Makoto Hyuga
"呼吸、心拍の反応はありますが、\n恐らく…。\n\0":
'???',

# Shinji Ikari
"ミサトさんは？\n\0":
'???',

# Rei Ayanami 
"まだ、連絡取れない。\n\0":
'???',

# Shinji Ikari
"そんな、どうしよう？\n\0":
'???',

# Asuka Soryu Langley
"何、グジグジ言ってんのよ。\n今、私達が心配したって、\n何もならないでしょ？\n\0":
'???',

# Shinji Ikari
"でも、\n使徒相手に僕らだけで。\n\0":
'???',

# Rei Ayanami 
"今は、碇司令が\n直接指揮をとってるわ。\n\0":
'???',

# Shinji Ikari
"父さんが？\n\0":
'Father is?\n\0',

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
# ./USRDIR/event/cev0100.har_EXTRACT/cev0100.evs
#
# Misato Katsuragi 
"あ、シンジ君。\nあなたに教えとく事があったわ。\n大事な話よ。\n\0":
'???',

# Shinji Ikari
"何ですか？\n\0":
'???',

#
# ./USRDIR/event/bs021.har_EXTRACT/bs021.evs
#
# Asuka Soryu Langley
"ＯＫ！\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le502.evs
#
# Kaworu Nagisa 
"構わないよ。\nそのために僕は\nゼーレの計画に乗ったんだから。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"ネルフに来て得たもの、知ったもの、\n感じたもの、触れたもの…。\nすべて失う事になっても？\n\0":
'???',

#
# ./USRDIR/event/tev0401.har_EXTRACT/tev0401.evs
#
# Misato Katsuragi 
"はーい。\nどちら様ですかー？\n\0":
'???',

# Toji Suzuhara 
"ごっつ、ベッピンさんや…。\n\0":
'???',

# Misato Katsuragi 
"あ…。\nシンジ君のクラスメイト？\n\0":
'???',

# Kensuke Aida
"あ、はい。\n\0":
'???',

# Toji Suzuhara 
"そそそ、そうです！\n碇君のクラスメイトの\n鈴原トウジ言います！\n\0":
'???',

# Kensuke Aida
"相田ケンスケです。\n\0":
'???',

# Misato Katsuragi 
"よかった、\nちゃんとお友達が出来たのね。▽\nわざわざ、誘いにきてくれて\nアリガト。\n呼んでくるから、チョッチまってね。\n\0":
'???',

# Kensuke Aida
"トウジ、今更隠れるなよ。\n\0":
'???',

# Toji Suzuhara 
"…逃げも隠れもせえへんわ。\n\0":
'???',

# Misato Katsuragi 
"シンジ君、お友達。\n迎えに来てるわよ。\n\0":
'???',

# Shinji Ikari
"え、僕、友達なんか…。\n\0":
'???',

# Kensuke Aida
"よう。\n俺、相田ケンスケ。\nで、こっちは…。▽\nトウジ、隠れてないで出て来いよ。\n\0":
'???',

# Toji Suzuhara 
"……………………。\nよぉ…。\n\0":
'???',

# Kensuke Aida
"コイツ、鈴原トウジ。\nお前に言いたい事があるって。\n\0":
'???',

# Toji Suzuhara 
"…すまん、転校生。\nお前の事、何も知らんと\n殴ったりして…。\n\0":
'???',

# Kensuke Aida
"こいつ、妹に説教されたんだ。\nみんなが助かったのは、\nあのロボットのお陰なんだって。▽\n小学生低学年に説教されてさ。\nトウジ、反省してるんだよ。\n\0":
'???',

# Toji Suzuhara 
"せやから、ワシを殴れ！\nワシはここで、筋通さなアカン。\n\0":
'???',

# Shinji Ikari
"（殴られなきゃいけないのは僕だ。\n　僕は卑怯で、臆病で、ずるくて、\n　弱虫で…。）▽\n（僕にはエヴァに乗る資格なんて\n　ないんだ。）▽\n（最初にエヴァに乗ったのも、\n　この町を救おうとか、\n　人類のために戦おうとか…。）▽\n（そんなカッコイイ理由じゃ\n　なくて…。）\n\0":
'???',

# Misato Katsuragi 
"ちょっと…！\n殴ったの、殴れっての、\n一体どういう事？\n\0":
'???',

# Toji Suzuhara 
"男と男の筋って奴ですわ。▽\n早ぅ、殴らんかい！\n\0":
'???',

# Toji Suzuhara 
"ワシの気持ちの問題でもあるんや。\n頼む…！\n\0":
'???',

# Shinji Ikari
"…！\n\0":
'???',

# Toji Suzuhara 
"おっほー、イテテテテ…。\n自分、やるやん。\n\0":
'???',

# Kensuke Aida
"じゃ、学校行こうか。\n俺は、相田ケンスケ。\nよろしく。\n\0":
'???',

# Toji Suzuhara 
"イテテ…。\nワシは、鈴原トウジ。\nよろしくな。\n\0":
'???',

# Shinji Ikari
"あ…、僕は…。\n碇シンジ。\nよろしく…。\n\0":
'???',

# Misato Katsuragi 
"…さあ、３人とも遅刻するわよ。\n学校、行ってらっしゃい。\n\0":
'???',

# Kensuke Aida, Toji Suzuhara
"行ってきます！\n\0":
'???',

# Shinji Ikari
"…あの、▽\n行ってきます。\n\0":
'???',

# Misato Katsuragi 
"はい♪\n行ってらっしゃい。\n\0":
'???',

# Misato Katsuragi 
"まあ、何かあったんだろうけど。\n友達はちゃんと出来たみたいね。\n\0":
'???',

#
# ./USRDIR/event/tev1706.har_EXTRACT/tev1706.evs
#
# Rei Ayanami 
"…！！▽\nこれは、私の心？\n碇君と一緒になりたい？▽\n…………………。\nだめ…。\n\0":
'???',

# Maya Ibuki 
"ΑΤフィールド反転！\n一気に侵食されます！\n\0":
'???',

# Ritsuko Akagi 
"使徒を押さえ込むつもり？\n\0":
'???',

# Misato Katsuragi 
"レイ、機体は捨てて逃げて！\n\0":
'???',

# Rei Ayanami 
"だめ。\n私がいなくなったら\nΑΤフィールドが消えてしまう。▽\nだから、だめ。\n\0":
'???',

# Misato Katsuragi 
"レイ、死ぬ気？\n\0":
'???',

#
# ./USRDIR/event/e004.har_EXTRACT/e004.evs
#
# Female Staff
"エヴァシリーズ、沈黙しました！\n\0":
'???',

# Misato Katsuragi 
"やった…。\nやったわ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"発令所の中では、勝利の喜びと\n安堵の声で沸き上がった。\n\0":
'???',

# Misato Katsuragi 
"さ、パイロットの回収作業に\n入るわよ。\n急いで！！\n\0":
'???',

# Kaworu Nagisa 
"人の心は人にしか開けない。▽\n僕の役目は終ったよ…。\nリリス…、\nこれでいいかい？\n\0":
'???',

# Ritsuko Akagi 
"…勝ったのね。\n\0":
'???',

# Maya Ibuki 
"勝った…、勝ったのね！！\n\0":
'???',

# Seele 01
"不要な身体を捨て、神と一つに。\n我々の導きにより、全ての生命を\n終末と再生の道を。\n\0":
'???',

# Ryoji Kaji
"勝ったな…。\nゼーレのシナリオも\n無に帰す時が来たか…。\n\0":
'???',

# Kaworu Nagisa 
"すべては流れのままに…。\n僕は、彼女に許されるのだろうか…。\n\0":
'???',

# Makoto Hyuga, Shigeru Aoba
"早く、機体とパイロットの\n回収を。\n\0":
'???',

# [Text Only - No Designated Speaker]
"人々はΑΤフィールドを失い、\n生命誕生前のＬＣＬと化していく。▽\n人々の魂だけが、頼りなく\n漂うように地表を流れゆく…。\n\0":
'???',

# Maya Ibuki 
"…！？▽\nそんな、倒したはずの\nエヴァシリーズが…。▽\nエヴァシリーズ、Σ機関を解放。\nこれは、セカンドインパクトの\n初期現象と同じだわ！！▽\nアンチΑΤフィールド、\n物質化します。\n\0":
'???',

# Makoto Hyuga
"…！？▽\n倒したはずのエヴァシリーズが…。▽\nエヴァシリーズ、Σ機関を解放。\nこれは、セカンドインパクトの\n初期現象と同じだ！！▽\nアンチΑΤフィールド、\n物質化します。\n\0":
'???',

# Shigeru Aoba
"…！？▽\nまさか、倒したはずの\nエヴァシリーズが…。▽\nエヴァシリーズ、Σ機関を解放。\nセカンドインパクトの初期現象と\n同じ現象が起こっています！！▽\nアンチΑΤフィールド、物質化！\n\0":
'???',

# Female Staff
"…！？▽\nそんな、倒したはずの\nエヴァシリーズが…。▽\nエヴァシリーズ、\nΣ機関を解放します！▽\nこれは、セカンドインパクトの初期\n現象と同じ事が起きています！！▽\nエヴァシリーズ、Σ機関を解放。\nアンチΑΤフィールド、\n物質化します。\n\0":
'???',

# Rei Ayanami 
"ほら、これがあなただったもの。▽\n全ての生命は、ここへ\n過ぎてはやって来る…。\n\0":
'???',

# Kaworu Nagisa 
"本来の姿を思い出す事になるのか。\nリリスを認識出来なければ\n無へと消える事になる。\n\0":
'???',

# Kaworu Nagisa 
"そしてリリス、\n君はそれを願ってはいない。▽\nそうだろう…？\n\0":
'???',

# Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Female Staff
"アンチΑΤフィールド、\n臨界点を突破！▽\nこのままでは、個体生命の形が\n維持できません！\n\0":
'???',

# Kaworu Nagisa 
"…リリス、\n…そうか、僕は許されるのか。▽\nありがとう、リリン…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"カヲルの周りを漂う赤い光を最初に、\n地球の全体から赤い光が\n初号機をめがけて流れていく。\n\0":
'???',

# Rei Ayanami 
"ありがとう。\nあなたが教えてくれた。▽\nそれは、夢…、▽\nそれは、涙…、▽\nそれは、痛み…、▽\nそれは、安らぎ…。▽\nあなたと共に、\nみんなここにあるわ…。\n\0":
'???',

# Rei Ayanami, Misato Katsuragi 
"ありがとう…。\n\0":
'???',

#
# ./USRDIR/event/bs076.har_EXTRACT/bs076.evs
#
# Misato Katsuragi 
"その代わり、今日教えた事は\n絶対忘れちゃダメよ。\n\0":
'???',

#
# ./USRDIR/event/tev1503.har_EXTRACT/tev1503.evs
#
# Intelligence Agent
"今より２時間前です。\nジオフロント西の第８区間を最後に\n消息を断っています。\n\0":
'???',

# Misato Katsuragi 
"うちの所内じゃない。\nあなた達諜報部は\n何をやってたの？\n\0":
'???',

# Intelligence Agent
"随行者に内報及び、\n先導者がいます。\nその人物に裏をかかれました。\n\0":
'???',

# Misato Katsuragi 
"諜報二課をケムにまける\nだけのヤツ？\nまさかアイツが！？\n\0":
'???',

# Intelligence Agent
"加持リョウジ。\nこの事件の首謀者と思われる\n人物です。\n\0":
'???',

# Misato Katsuragi 
"で、私のところに来たわけね。\n\0":
'???',

# Intelligence Agent
"ご理解が早く助かります。▽\n作戦課長を疑うのは、同じ職場の\n人間として心苦しいのですが\nこれも仕事ですので。\n\0":
'???',

# Misato Katsuragi 
"彼と私の経歴を考えれば、\n当然の処置でしょうね。\n\0":
'???',

# Intelligence Agent
"ご協力感謝します。\n\0":
'???',

# Seele 06
"議題としている問題が\n急務なのでね。\nやむなくの処置だ。\n\0":
'???',

# Seele 03
"わかってくれたまえ。\n\0":
'???',

# Kozo Fuyutsuki
"委員会ではなく、\nゼーレのお出ましとは…。\n\0":
'???',

# Seele 05
"我々は、新たな神を\n造るつもりはないのだ。\n\0":
'???',

# Seele 09
"冬月先生、ご協力を願いますよ。\n\0":
'???',

# Seele 02
"Σ機関を自ら搭載し、\n絶対的存在を手にした\nエヴァンゲリオン初号機。\n\0":
'???',

# Seele 03
"我々に具象化された神は\n不要なのだよ。\n\0":
'???',

# Seele 01
"神を造ってはいかん。\n\0":
'???',

# Seele 06
"ましてあの男に、\n神を手渡すわけにはいかんよ。\n\0":
'???',

# Seele 03
"碇、信用に足る男かな？\n\0":
'???',

# Misato Katsuragi 
"拉致された？\n副司令が？\n\0":
'???',

#
# ./USRDIR/event/tev1701.har_EXTRACT/tev1701.evs
#
# Asuka Soryu Langley
"私、勝てなかったんだ。\nエヴァで。▽\nもう私の価値なんてなくなったの。\nどこにも。\n\0":
'???',

# Asuka Soryu Langley
"キライ、だいっきらい。\nみんな嫌いなの。▽\nでも、一番嫌いなのは私。\n\0":
'???',

# Asuka Soryu Langley
"もう、どうでもよくなっちゃった。\n何もかも。\n\0":
'???',

# Hikari Horaki
"私はアスカがどうしたって\nいいと思うし、何も言わないわ。\nアスカはよくやったと思うもの。\n\0":
'???',

# Seele 05
"ロンギヌスの槍、\n何故使用した。\n\0":
'???',

# Seele 09
"最近の君の行動には、\n目に余るものがあるな。\n\0":
'???',

# Gendo Ikari
"冬月、審議中だぞ。▽\n…わかった。▽\n使徒が現在、接近中です。\n続きはまた後程。\n\0":
'???',

# Seele 05
"その時、君の席が残っていたらな。\n\0":
'???',

# Keel Lorenz
"碇、ゼーレを裏切る気か。\n\0":
'???',

#
# ./USRDIR/event/bs107.har_EXTRACT/bs107.evs
#
# [Text Only - No Designated Speaker]
"初号機はΣ機関の能力を得たため、\nアンビリカルケーブルによる\n電源供給が不要となりました。\n\0":
'???',

#
# ./USRDIR/event/tev1705.har_EXTRACT/tev1705.evs
#
# Shigeru Aoba
"目標、零号機と物理的接触！\n\0":
'???',

# Misato Katsuragi 
"零号機のΑΤフィールドは！？\n\0":
'???',

# Maya Ibuki 
"展開中！\nしかし、使徒に侵食されています！\n\0":
'???',

# Ritsuko Akagi 
"使徒が積極的に１次的な接触を\n試みているの？\n零号機と…。\n\0":
'???',

# Maya Ibuki 
"危険です！\n零号機の生体部品が\n侵されています。\n\0":
'???',

# Misato Katsuragi 
"エヴァ弐号機！\nアスカ、レイの救出と援護を！\n\0":
'???',

# Asuka Soryu Langley
"…………ない。\n\0":
'???',

# Asuka Soryu Langley
"動かない…。\n動かないのよ…。\n\0":
'???',

# Maya Ibuki 
"駄目です！\nシンクロ率が二桁を切っています。\n\0":
'???',

# Gendo Ikari
"初号機の凍結を現時刻を持って解除。\n直ちに出撃させろ。\n\0":
'???',

# Asuka Soryu Langley
"…何よ。\n私の時は出さなかったくせに。\n\0":
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
# ./USRDIR/event/tev0304.har_EXTRACT/tev0304.evs
#
# Kensuke Aida
"やったぁ！！\n\0":
'???',

# Toji Suzuhara 
"勝ったぁ！！\n\0":
'???',

# Toji Suzuhara 
"何や…。\n\0":
'???',

# Kensuke Aida
"へへへっ。\nアイツ、ちゃんと守ったよ。\n俺達を。\n\0":
'???',

# Toji Suzuhara 
"……………………。\nわかっとる…。\n\0":
'???',

# Kensuke Aida
"さあ、帰ろうぜ。\n\0":
'???',

#
# ./USRDIR/event/cev0305.har_EXTRACT/cev0305.evs
#
# Rei Ayanami 
"また、私を見てる。\n私が私を見ている。▽\n私は何？\n私は今、どんなモノなの…？ \n\0":
'???',

# Rei Ayanami 
"…。▽\n………。▽\n………………。 \n\0":
'???',

# Gendo Ikari
"アダムも我が手に収まった。\nレイ…、来るべき旅立ちは\nもうすぐだ…。\n\0":
'???',

# Rei Ayanami 
"この人は、私を見ている。\n私…、どの私…？ \n\0":
'???',

# Gendo Ikari
"お前はその時の為にある\n存在なのだから…。\n\0":
'???',

# Rei Ayanami 
"何の為に？\nこの人の為にある私？\nそれは…、本当の私なの…？ \n\0":
'???',

# Gendo Ikari
"アダムは生命の実を食べ、\n使徒に永遠の生命と力を。▽\nリリスは知恵の実を食べ、\n人類に知恵と死を与えた。▽\n我々は、知恵と死と、\n産み増える事しか\n受け取れなかったのだ。▽\n人々が追い求めて止まない\n永遠の命…、だが使徒も同じく\n知恵の実を求めてリリスを目指す。▽\nアダムとリリスの融合は、\n全てを無にもどし\nまた新たな生命の萌芽となる。▽\n知恵と永遠の生命を携えて…、\n新たな生命となる為に。▽\nだが、その生命に宿るものは\n我々人類か使徒かは…わからん。\n\0":
'???',

# Rei Ayanami 
"永遠の命を手にして、\nどうされるのですか？\n\0":
'???',

# Gendo Ikari
"命が永遠である事が\n重要なのではない。▽\n我々全ての魂を一つにする事が\n重要なのだよ。▽\nレイ、お前はその扉となり、\n全ての心を補完する為の\n道標となるのだ。\n\0":
'???',

# Rei Ayanami 
"……………。▽\n私はその為にいるんですか？\n\0":
'???',

# Gendo Ikari
"…………。▽\nお前は、処置なくしては、\n生き長らえる事が出来ない。\n我々よりも…。▽\nお前にも長生きして欲しい。\n\0":
'???',

# Rei Ayanami 
"私の欲しい答えは…、\nいつも闇の中。▽\nこの人は何も、\n答えてはくれないのね。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le128.evs
#
# Shinji Ikari
"僕だって、心を隠したくない。\n自分を知ってもらう事で、\n何かが変われると思うし。\n\0":
'???',

# Shinji's Shadow [Leliel]
"期待通りに行かなかったら？\n今度は何を責めるつもり？\n何に期待を抱くつもり？\n\0":
'???',

#
# ./USRDIR/event/f043.har_EXTRACT/f043.evs
#
# [Text Only - No Designated Speaker]
"校庭には、誰の姿も見当たらない。\n先日、突然開始された集団疎開が\n実行されたためだ。▽\n次に出現する使徒を迎撃するため、\nこの街は放棄される。▽\n出発の時間が近い。\nこの学校の風景を観ることも、\nもうないだろう…。\n\0":
'???',

# Shinji Ikari
"もう、誰もいないんだ…。\n疎開が始まるんだったな。\n\0":
'???',

# Asuka Soryu Langley
"この学校も閉鎖されたのね。\nま、疎開となりゃあ、\nしょーがないわね。\n\0":
'???',

# Rei Ayanami 
"民間人はみな、\n疎開してしまった。▽\nこの学校にも、\nもう誰もいないのね。\n\0":
'???',

# Toji Suzuhara 
"めんどいだけやった、授業も\nもう受けられへんのやな…。▽\nみんな、疎開してしもて、\nもう、学校には誰も来ぇへん。\n\0":
'???',

# Kaworu Nagisa 
"短い間だったけど、楽しかったな。\nもう、この校舎も使われる事は\nないんだな。▽\n疎開していったみんなは、無事に\n平和に過ごす事が出来ればいいな。\n願うのはそればかりだよ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le313.evs
#
# Rei Ayanami 
"エヴァは人類の希望よ。\n滅亡するわけにはいかない。\n\0":
'???',

# Rei's Shadow [Leliel]
"そう吹き込まれて、\n誰かに利用されているのかも…。\nあなたの希望ではないのでしょう？\n\0":
'???',

#
# ./USRDIR/event/f079.har_EXTRACT/f079.evs
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
# ./USRDIR/event/tev1204.har_EXTRACT/tev1204.evs
#
# Misato Katsuragi 
"シンジ君、今日は遅くなるから。\n先に寝ててちょうだいね。\n\0":
'???',

# Shinji Ikari
"お仕事ですか？\n大変ですね。\n\0":
'???',

# Misato Katsuragi 
"ううん、今日は違うの。\n大学の友人の結婚式よ。\n\0":
'???',

# Asuka Soryu Langley
"ふうん。\nじゃあ、加持さんも一緒なワケ？\n\0":
'???',

# Misato Katsuragi 
"ええ、リツコもね。\n\0":
'???',

# Asuka Soryu Langley
"なるべく早く\n帰ってきなさいよっ！\n\0":
'???',

# Shinji Ikari
"何で、そんなに怒るの？\nいつも、ミサトさんの\n帰りなんて気にしないのに。\n\0":
'???',

# Asuka Soryu Langley
"うるさい、バカッ！\n\0":
'???',

# Misato Katsuragi 
"じゃ、私はもう出るから。\n戸締りヨロシクね。\n\0":
'???',

#
# ./USRDIR/event/cev0109.har_EXTRACT/cev0109.evs
#
# Shinji Ikari
"えーっと、あっ…、\nまたお弁当売り切れてる…。\n\0":
'???',

# Makoto Hyuga
"やあ、シンジ君、買い物かい？\n\0":
'???',

# Shinji Ikari
"あ、はい…。\n晩御飯でも…、って思ったけど、\nお弁当売り切れてて…。\n\0":
'???',

# Makoto Hyuga
"ああ、なるほど…。▽\nそうだねぇ、この系列のコンビニは\n大体１便が０時過ぎぐらいに\nなるからね。▽\nちょうど、これぐらいの時間が\n一番品薄なんだ。▽\nだから確実に欲しいなら\n夕方か、深夜０時過ぎじゃないとね。\n\0":
'???',

# Shinji Ikari
"へぇ…、詳しいんですね…。\n\0":
'???',

# Makoto Hyuga
"ああ、学生時代に\nバイトしていたからね…。\n\0":
'???',

# Shinji Ikari
"え？　そうなんですか？\n\0":
'???',

# Makoto Hyuga
"そんなに意外かい？\nまあ、大概の大学生は\nアルバイトしてるもんだよ。▽\nまあ、コンビニは結構楽だし、\n夜中の暇な時間に勉強できたり\nしたから、都合よかったなぁ。\n\0":
'???',

# Shinji Ikari
"仕事中にまで勉強しないと\nいけなかったんですか…。\n大変…ですねぇ。\n\0":
'???',

# Makoto Hyuga
"君だって、パイロットしながら\n学校行ってるじゃないか。\nそっちの方が大変だよ。\n\0":
'???',

# Shinji Ikari
"そんな…事ありません。\n使徒が来なかったら、パイロット\nなんて絶対してませんし…。▽\n勉強だって、仕方なく\nやってる事だし…。\n\0":
'???',

# Makoto Hyuga
"…まぁ、勉強は楽しくないよね。\nでも、僕にはそれしか取り得が\n無かったから。\n\0":
'???',

# Shinji Ikari
"そう…だったんですか？\n\0":
'???',

# Makoto Hyuga
"そうなんだ。\nスポーツは駄目、女の子にも当然\nもてなかったし…。▽\nだから勉強を頑張る以外に\nなかったんだよ。\n\0":
'???',

# Shinji Ikari
"じゃあ、勉強の甲斐ありましたね。\nだって、ネルフで働いて\nいるんですもん。\n\0":
'???',

# Makoto Hyuga
"…どうかな。\n\0":
'???',

# Makoto Hyuga
"ネルフに入れたのは、\n勉強を頑張ったからなんだけどね。▽\nネルフに入るために努力してた\nワケじゃないんだ…。\n\0":
'???',

# Makoto Hyuga
"ただ、勉強でしか認められなかった\nから…、他の人との差を\n見せ付けたかったから…。▽\n…国連職員採用競争試験を受験して\n一発合格したんだ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"日向さんは呟くように言った。\nパイロットでしか僕を表現できない\n僕に似てる…、そう思った。\n\0":
'???',

# Shinji Ikari
"日向さんは…、ホントは\n何になりたかったんですか？\n\0":
'???',

# Makoto Hyuga
"…はは、情けない事に、\nなーんにも考えてなかったんだ。▽\n勉強さえしていれば、\n何とかなると信じてたんだけど。▽\n本当に「なんとかなった」だけ\nだったね…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"寂しそうに微笑む日向さんを見て、\n僕は少し変な顔をしてたのだろう。\n日向さんは慌てて表情を取り繕った。\n\0":
'???',

# Makoto Hyuga
"あはは、まあおかげで世のため\n人のために粉骨砕身しているよ。\nすべては結果論だけどね…。\n\0":
'???',

# Makoto Hyuga
"でもね、シンジ君…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"年長者の声と表情で、\n日向さんは僕の名を\n呼んだ。\n\0":
'???',

# Makoto Hyuga
"勉強を軽視してはいけないよ？\nいずれ使徒のいない平和な\n世の中がやってくる。▽\nいつまでもパイロットやってる\nわけには行かないんだ。▽\nそうなったら…、自分の可能性を\n支えるのは、先を見る目と、目的に\n近づこうとする努力なんだから。\n\0":
'???',

# [Text Only - No Designated Speaker]
"日向さんは僕を見つめていない\nような気がした。▽\nたぶん…、勉強漬けだった過去の\n自分を励ましているんじゃ\nないだろうか。\n\0":
'???',

# Makoto Hyuga
"僕には、先が見えなかった…。\nまあセカンドインパクトを\n経験すれば仕方ないよね…。▽\nとにかく、いい学校に行ければ、\nそれだけ選択肢は増える。\nこの事は憶えておいてね？\n\0":
'???',

# [Text Only - No Designated Speaker]
"日向さんは、柄にもない自分に\n照れているみたいだった。\n\0":
'???',

# Shinji Ikari
"あのっ…。\n\0":
'???',

# Makoto Hyuga, Shinji Ikari, Toji Suzuhara
"…ん？\n\0":
'???',

# Shinji Ikari
"なりたいものなんて、今からでも\n考えられると思います。▽\nその後にでも、なりたいものに\nなればいいんですよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"我ながら生意気な事を言ったと思う。\nそれでも、日向さんは優しく笑った。\n\0":
'???',

# Makoto Hyuga
"そうだね、シンジ君。\nでもやっぱり僕は、\nネルフに居続けると思うよ。▽\n今の仕事も、何だかんだいって\n誇りに思ってる。▽\n君みたいな、出来た弟もいる事だし。\n\0":
'???',

# Shinji Ikari
"弟？\n僕…ですか？\n\0":
'???',

# Makoto Hyuga
"そう。\nだから、さっきのはお兄さん\nとしてのアドバイスさ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"日向さんは、\n僕の頭をくしゃくしゃに撫でて\n微笑んだ。\n\0":
'???',

# Makoto Hyuga
"じゃあね、シンジ君。\nおやすみ。\n\0":
'???',

# Shinji Ikari
"はい…。\nおやすみなさい。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le304.evs
#
# Rei Ayanami 
"ちがう…。\n自分がわからないのは…。\n\0":
'???',

# Rei's Shadow [Leliel]
"空っぽだから。\n何も無いから見えない。\n理解しようがない。▽\nでもそれは…。\nあなたが目を背けているから。▽\n本当は心の奥底に持っている自分を\n見ないようにしているだけ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le118.evs
#
# Shinji Ikari
"いっそ、心が見えればいいと思う。\n少なくとも誤解が無い様に、\n僕の気持ちは伝えられる。\n\0":
'???',

# Shinji's Shadow [Leliel]
"でも、拒否される事もある。\n\0":
'???',

# Shinji Ikari
"何も言えなくなるよりマシだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"まあ、人の顔色をうかがう\n気苦労は無くなるだろうね。\n\0":
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
# ./USRDIR/event/f042.har_EXTRACT/f042.evs
#
# Shinji Ikari
"…僕、一人で…？\n\0":
'???',

# Kaworu Nagisa 
"…あなたは？\n\0":
'???',

# [Text Only - No Designated Speaker]
"あとはエレベーターの中で\n$bの無事を祈った。▽\n怖かった。▽\n出来る事といえば、エヴァに乗って\n戦う事しか出来ない。▽\n最後にもう一度だけ、\nみんなの無事を祈った。\n\0":
'???',

# Asuka Soryu Langley
"………。▽\nねえ、話して。\n何が起こってるの？\n\0":
'???',

# Kozo Fuyutsuki
"エヴァシリーズ…、\n完成していたのか！！\n\0":
'The Eva Series...\n So it\'s been completed!\n\0',

# Shinji Ikari
"…こちら初号機、\n発進準備お願いします。\n\0":
'... Unit-01 here,\n requesting launch preparations.\n\0',

# Asuka Soryu Langley
"…こちら弐号機、\n発進準備お願いします。\n\0":
'... Unit-02 here,\n requesting launch preparations.\n\0',

# Kaworu Nagisa 
"…こちら四号機、\n発進準備お願いします。\n\0":
'... Unit-04 here,\n requesting launch preparations.\n\0',

# Kaworu Nagisa 
"………。▽\nとりあえず、話してくれませんか。\n何があったのかを。\n\0":
'???',

# Gendo Ikari
"やはりここにいたか。\nさあ、行こう、レイ。\n\0":
'???',

# Rei Ayanami 
"いいえ、駄目。\n$cが呼んでいる…。\n\0":
'No, I can\'t.\n $c is calling me...\n\0',

# (Decision Prompt)
"ゲンドウについていく／…私を呼んでいる\0":
'Go along with Gendo／...Someone is calling me\0',

# Misato Katsuragi 
"戦自、約一個師団の投入か。\n占拠は時間の問題のようね。\n\0":
'???',

# [Text Only - No Designated Speaker]
"行ってしまう。\nあの人が行ってしまう。\n多分、ここには戻らないだろう。▽\nこれを最後に、私は見限られる。\nリツコは、静かにゲンドウの\n後を追った。▽\nあの人は、間違いなく\nあの場所へと向かうはずだ。\n\0":
'???',

# Makoto Hyuga
"チッ、とうとうここまで…。\n\0":
'???',

# Kozo Fuyutsuki
"いかん、\nやつらはここのマギが狙いだ。\n\0":
'???',

# Shigeru Aoba
"もう、ここまで来たのか！？\n\0":
'???',

# Male Staff
"くそぅ、来やがった…！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"そこには、レイを連れたゲンドウが\n立っていた。\n\0":
'???',

# JSSDF Staff
"第１発令所に到着。\nこれよりＢＣ兵器を使用する。\n\0":
'???',

# Ritsuko Akagi 
"ごめんなさい。▽\n先ほどマギのプログラムを\n変えさせてもらいました。\n\0":
'???',

# Shigeru Aoba
"マギを無傷で手に\n入れるつもりだな…。\nクソッ…！！\n\0":
'???',

# Makoto Hyuga
"何てやつらだ、このままでは\nマギを奪われてしまう。\nそんな事になったら…。\n\0":
'???',

# Kozo Fuyutsuki
"マギをやつらに渡してはならん。\n\0":
'???',

# Male Staff
"ＢＣ兵器だって…？\nくそ、マギが狙いか…。\n\0":
'???',

# Announcement
"ターミナルドグマ、\n制圧され…　　　　　　　　　　　\n　　　　　　　　\n\0":
'???',

# Kozo Fuyutsuki
"これ以上先に進ませるな！！\n奴らにサードインパクトを\n起こさせるつもりはない。▽\n本部ごと自爆させろ！！\n\0":
'???',

# Misato Katsuragi 
"まずいわ、ヘブンズドアも\n時間の問題よ。▽\nこうなったら、本部ごと自爆よ！\nみんな、覚悟はいい？\n\0":
'???',

# Ritsuko Akagi 
"ヘブンズドアを目指しているのね。▽\nアレが奴らの手に渡れば、\n人為的にサードインパクトを\n引き起こされるわ！！▽\n自爆装置を発動させて、\n今すぐに！！\n\0":
'???',

# Female Staff
"ここを自爆させましょう。\nそれしかありません。\n\0":
'???',

# Kozo Fuyutsuki
"馬鹿な！\n赤木博士にマギの自爆を\n阻止させろ！\n\0":
'???',

# Male Staff
"そ、そんな…。\n赤木博士、マギのカウントを\nリセットして下さい！\n\0":
'???',

# Maya Ibuki 
"わかりました…、うっ…。\nＢＣ兵器が、ここまで…。\n\0":
'???',

# Makoto Hyuga
"了解。▽\n…う、かはぁっ！？\nしまった、ＢＣ兵器が、\n…もうここまで。\n\0":
'???',

# Shigeru Aoba
"わかりました。▽\nう…、ぐあぁっ…。\nＢＣ兵器が…。\n\0":
'???',

# Male Staff
"うー…、ごほっ、ごほ…。\nＢＣ兵器…、い、息が…。\n\0":
'???',

# Announcement
"自爆装置、発動しました。\n爆破予定まで、あと６０秒…。\n\0":
'???',

# Makoto Hyuga
"へっ、へへへ…、\nこっちの…勝ちだ…。▽\nう…、っうー…、ごほっ…。▽\n………………………。\n\0":
'???',

# Shigeru Aoba
"へっ、…渡さねえ、\n…お前達には…、何も…。▽\n…ぐ………、ぐあぁ…ぁ…。▽\n…………………………。\n\0":
'???',

# Maya Ibuki 
"はぁ…、はぁ…、\nここは私達の…、\n誰にも…渡さ…ない。▽\n………ううっ、…うぅー…。▽\n……………………………。\n\0":
'???',

# Male Staff
"ざまあ…みやがれ…、\nふ、ふふふふふ…。▽\nう、げぇっ…、うがぁ…っ。▽\n…………………………。\n\0":
'???',

# Announcement,Local Announcement
"爆発まで１０秒、\n８、７、６、５、４、３、２、１\n\0":
'???',

# Asuka Soryu Langley
"だって、９機って…。\n\0":
'???',

# Ritsuko Akagi 
"作動しない？\nなぜ？\n\0":
'???',

# Maya Ibuki, Female Staff
"ネルフ施設内に多数の侵入者あり、\n通信も各所不通です！\n\0":
'???',

# Gendo Ikari
"………。▽\n赤木リツコ君。\n本当に………\n\0":
'???',

# Ritsuko Akagi 
"嘘つき…。\n\0":
'???',

# Misato Katsuragi 
"クッ、ネルフの対人施設の予算が\n削られていたのは、このためなのね！\n\0":
'???',

# Male Staff
"ネルフの対人施設の予算が\n削られていたのは、このためかっ！\n\0":
'???',

# Misato Katsuragi 
"ある程度ネルフの対人施設は\n機能しているけど…。\n食い止められるかしら…。\n\0":
'???',

# Male Staff
"ある程度ネルフの対人施設は\n機能しているはずだが…。\n食い止められるか…。\n\0":
'???',

# Misato Katsuragi 
"こんな事もあろうかと、\nネルフの対人防御能力を\n高めていて正解だったわ。\n\0":
'???',

# Male Staff
"こんな事もあろうかと、\nネルフの対人防御能力を\n高めておいて正解だったな。\n\0":
'???',

# Misato Katsuragi 
"どんなやつらが侵入しようと、\n心配ないわ！\n\0":
'???',

# Male Staff
"どんなやつらが侵入しようと、\n心配無用さ！\n\0":
'???',

# Shinji Ikari
"何の音…、さっきから一体、\n何が起こってるんだ？\n\0":
'???',

# Asuka Soryu Langley
"敵襲？\nまさか本部に直接…。\n\0":
'???',

# Kaworu Nagisa 
"ゼーレが決断を下したようだ。\nという事は、まず僕は\n消されるだろうな…。\n\0":
'???',

# Kozo Fuyutsuki
"とうとう始まったか…。\n\0":
'???',

# Gendo Ikari
"いよいよその時が来たようだな、\n後は任せましたよ、冬月先生。\n\0":
'???',

# Shinji Ikari
"………。▽\nねえ、本部は今どうなってるの？\n\0":
'???',

# Gendo Ikari
"いよいよこの時が来たか。\n\0":
'???',

# Shinji Ikari
"じゃ、じゃあ、また使徒が…。\n\0":
'???',

# Asuka Soryu Langley
"まさか、使徒なの…？\n\0":
'???',

# Maya Ibuki 
"シンジ君が、\nＢ地区で孤立しています！\n\0":
'???',

# Female Staff
"初号機パイロット、\nＢ地区で孤立しています！\n\0":
'???',

# Kaworu Nagisa 
"９体も…。\nしかも、あのエヴァシリーズか。\n\0":
'???',

# Maya Ibuki 
"アスカが、\nＢ地区で孤立しています！\n\0":
'???',

# Female Staff
"弐号機パイロット、\nＢ地区で孤立しています！\n\0":
'???',

# Maya Ibuki 
"トウジ君が、\nＢ地区で孤立しています！\n\0":
'???',

# Female Staff
"参号機パイロット、\nＢ地区で孤立しています！\n\0":
'???',

# Maya Ibuki 
"カヲル君が、\nＢ地区で孤立しています！\n\0":
'???',

# Female Staff
"四号機パイロット、\nＢ地区で孤立しています！\n\0":
'???',

# Makoto Hyuga
"まずい、\n敵の侵攻ルート上だ！\n\0":
'???',

# Shigeru Aoba
"まずい、\n敵の侵攻ルート上じゃないか！\n\0":
'???',

# Male Staff
"まずい、\n敵の侵攻ルート上ですよ！\n\0":
'???',

# Local Announcement
"マギにより、自爆が\n決議されました。\n\0":
'???',

# Misato Katsuragi 
"私がパイロットの保護に向かいます。\n後は任せたわよ。\n\0":
'???',

# Ritsuko Akagi 
"私が行くわ！\nあなた達はここを！！\n\0":
'???',

# Makoto Hyuga
"僕が行く。\nあの子をここまで連れてこよう。\n\0":
'???',

# Shigeru Aoba
"くそっ、\n俺がパイロットを回収する。\n\0":
'???',

# Maya Ibuki 
"私が行きます。\nあの子は…、私が連れてきます。\n\0":
'???',

# Kozo Fuyutsuki
"葛城君。\n\0":
'???',

# Misato Katsuragi 
"了解しました、\n後の指示、よろしくお願いします。\n\0":
'???',

# Kozo Fuyutsuki
"赤木博士。\n\0":
'???',

# Ritsuko Akagi 
"わかりました、\nあとはお任せします。\n\0":
'???',

# Ritsuko Akagi 
"カスパーが裏切った。\n母さんは娘より\n自分の男を選ぶのね。\n\0":
'???',

# Kozo Fuyutsuki
"日向君。\n\0":
'???',

# Makoto Hyuga
"はい、僕が行きます。\nみなさんもご無事で。\n\0":
'???',

# Kozo Fuyutsuki, Maya Ibuki 
"青葉君。\n\0":
'???',

# Kozo Fuyutsuki
"伊吹君。\n\0":
'???',

# Maya Ibuki 
"…わかりました、\nパイロットを救出してまいります。\n\0":
'???',

# Male Staff
"ネルフ直上に、未確認飛行物体\n計９機を確認。\n\0":
'???',

# Kozo Fuyutsuki
"何ッ！？\n\0":
'???',

# Female Staff
"量産機！？\n飛行物体は、エヴァシリーズです！\n\0":
'???',

# Makoto Hyuga, Shigeru Aoba, Maya Ibuki, Male Staff
"パイロット、\nエヴァへのエントリーを確認！\n\0":
'???',

# Kozo Fuyutsuki
"救出先からの通信は？\n\0":
'???',

# Female Staff
"途絶えました…。\n恐らくは…。\n\0":
'???',

# Kozo Fuyutsuki
"…そうか。▽\nよし、エヴァを発進させろ。\n\0":
'???',

# Male Staff
"パイロット、ケイジに\n到着したそうです。\n\0":
'???',

# Kozo Fuyutsuki
"そうか、他には？\n\0":
'???',

# Male Staff
"これより発令所に\n帰還するとの事です！\n\0":
'???',

# Kozo Fuyutsuki
"わかった。\nよし、エヴァを発進させろ。\n急げ！！\n\0":
'???',

# Misato Katsuragi 
"何ですって！\nリツコは！？\n\0":
'???',

# Ryoji Kaji
"いよいよ最後の時が来たようだな。\n俺はここから人類の未来を\n見物させてもらう…。\n\0":
'???',

# Kozo Fuyutsuki
"……………………………………。\n\0":
'???',

# Kaworu Nagisa 
"始まったね…。\n僕は、ここからリリンの未来を\n見ているよ…。\n\0":
'???',

# JSSDF Staff
"あそこだ！！\n\0":
'???',

# JSSDF Staff
"仕留めたか。\nここはいい、じき爆発予定だ。\n次のブロックへ急げ。\n\0":
'???',

# Misato Katsuragi 
"待て…、クッ…。▽\n………………………あ、▽\n………………………。\n\0":
'???',

# Ritsuko Akagi 
"その先は…、\nその先にはあの子が………。▽\n………………………。\n\0":
'???',

# Makoto Hyuga
"お…あっ…、▽\nその先…には、\nパイ…ロット…が…。▽\n………………………。\n\0":
'???',

# Shigeru Aoba
"何だよ…、\nあと少し…なのによ…。▽\n…かっこ悪ィ…、\nロックな死に方じゃねぇ…。▽\n………………………。\n\0":
'???',

# Maya Ibuki 
"痛…、痛い…。▽\n痛いよぉ…、お母…さん、\nお母さん…、\nお家、帰れそうに…ない…みたい。▽\nお……母さ…………………。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ただ、これから何をするべきかは\nわかった。▽\nやるべきことがある。▽\n戦うこと。▽\nみんなのために戦うことだ。▽\n行こう。\n\0":
'???',

# JSSDF Staff
"あそこだ、逃がすな！！\n\0":
'???',

# Misato Katsuragi 
"悪いわね、こっちゃ死ぬわけには\nいかないのよ。\n\0":
'???',

# Ritsuko Akagi 
"恨まないでね。\nこっちも急ぎなのよ。\n\0":
'???',

# Makoto Hyuga
"………。▽\n急がないと、あの子が危ない…。\n\0":
'???',

# Shigeru Aoba
"さて、急がないとここも\nヤバイな。\n\0":
'???',

# Maya Ibuki 
"………あ、うう。▽\n………………………。▽\n駄目、行かなきゃ、行って\nあの子を助けなきゃ…。\n\0":
'???',

# Misato Katsuragi 
"…！？\nさっきのブロックだわ。\nもうあのルートは使えないわね。\n\0":
'???',

# Ritsuko Akagi 
"…！？\nさっきのフロアね、\n帰りは遠回りになるか…。\n\0":
'???',

# Makoto Hyuga
"…！？▽\nやばい、\nさっきの道はもう使えないな。\n別ルートを確保しないと…。\n\0":
'???',

# Shigeru Aoba
"…！？\nやりやがったな…、\nチッ、帰りは別ルートかよ。\n\0":
'???',

# Maya Ibuki 
"…！？\nどうしよう、さっきのフロアが\n爆破されたんだわ…。\n\0":
'???',

# Misato Katsuragi 
"何ですって？\nまさか、それって…。\n\0":
'???',

# Ritsuko Akagi 
"とうとう来たわね。\n\0":
'???',

# Makoto Hyuga
"何だって…？\n\0":
'???',

# Shigeru Aoba
"こっちもあと少しでパイロットと\n合流する。\nまだ、何かあるのか！？\n\0":
'???',

# Maya Ibuki 
"未確認機…！？\nそれって…。\n\0":
'???',

# Shinji Ikari
"ミサト…さん？\n\0":
'???',

# Asuka Soryu Langley
"ミサト…？\n\0":
'???',

# Toji Suzuhara 
"ミサト…さんやないですか！\n\0":
'???',

# Kaworu Nagisa 
"ミサトさん！！\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley
"リツコ…さん？\n\0":
'???',

# Toji Suzuhara 
"リツコ…さん、リツコさんや\nないですか！？\n\0":
'???',

# Kaworu Nagisa 
"リツコさん！？\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Toji Suzuhara, Kaworu Nagisa
"日向さん！！\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Toji Suzuhara, Kaworu Nagisa
"青葉さん？\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Kaworu Nagisa
"マヤさん…？\n\0":
'???',

# Toji Suzuhara 
"マヤさん、マヤさーん！！？\n\0":
'???',

# Misato Katsuragi 
"あなた…、▽\nよかった、生きててくれて。\n\0":
'???',

# Ritsuko Akagi 
"無事なのね！！\nよかった………。\n\0":
'???',

# Makoto Hyuga
"君か！！\n探したよ、本当によかった…。\n\0":
'???',

# Shigeru Aoba
"バッカヤロウ…、心配したぞ。\nさあ、行こう…。\n\0":
'???',

# Maya Ibuki 
"よかった、\nきっとここにいると思って…。\n勇気を振り絞ってきたの…。\n\0":
'???',

# Shinji Ikari
"急に通路が閉鎖されて…、\nさっきから爆発みたいな音が\nするし…。▽\n一体、何があったんですか？\n\0":
'???',

# Asuka Soryu Langley
"ねえ、何なの！？\n敵襲なの？\nここ、どうなっちゃうのよ…。\n\0":
'???',

# Toji Suzuhara 
"あちこちで、爆発が起こってる\nみたいで、ここまで爆風が…。\n一体、どないなっとるんですか？\n\0":
'???',

# Kaworu Nagisa 
"ゼーレが動き出したんですね。\nこれから、僕はどうすれば\nいいですか…。\n\0":
'???',

# Misato Katsuragi 
"まずはケイジへ急ぎましょう。\n\0":
'???',

# Ritsuko Akagi 
"それより、\n急ぐわよ、ケイジへ。\n\0":
'???',

# Makoto Hyuga
"それより、早くケイジへ。\n\0":
'???',

# Shigeru Aoba
"話は後だ、\nまずはケイジへ行こう。\n\0":
'???',

# Maya Ibuki 
"走って、\nまずはケイジへ急ぐのよ。\n\0":
'???',

# Asuka Soryu Langley
"話が先よ。\nもう、何があったのよ。\n\0":
'???',

# Kaworu Nagisa 
"そうか、エヴァシリーズ。\nゼーレが送り込んできたんですね。\n\0":
'???',

# JSSDF Staff
"エヴァパイロット発見。\nこっちだ、排除しろ！！\n\0":
'???',

# Misato Katsuragi 
"チッ…！！\n\0":
'???',

# Ritsuko Akagi 
"見つかった…。\n\0":
'???',

# Makoto Hyuga
"しまった！！\n\0":
'???',

# Shigeru Aoba
"くそっ！！\n\0":
'???',

# Maya Ibuki 
"させない！！\n\0":
'???',

# Shinji Ikari, Toji Suzuhara, Kaworu Nagisa
"…！？▽\nミサトさんっ！\n\0":
'???',

# Asuka Soryu Langley
"…！？▽\nミサト、アンタ…！！\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Toji Suzuhara, Kaworu Nagisa
"…！？▽\nリツコさんっ！！\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Toji Suzuhara, Kaworu Nagisa
"…！？▽\n日向さん！！\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Toji Suzuhara, Kaworu Nagisa
"…！？▽\n青葉さん！！\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Toji Suzuhara, Kaworu Nagisa
"…！？▽\nマヤさんっ！！\n\0":
'???',

# Rei Ayanami 
"駄目。\n私を呼んでる人がいる…。\n\0":
'???',

# Misato Katsuragi 
"………逃げて、ケイジへ。\nケイジへ行くのよ…。\n\0":
'???',

# Ritsuko Akagi 
"急いで、ケイジへ走るのよ。\n…早く………。\n\0":
'???',

# Makoto Hyuga
"…走れッ…、\n走れったら！！\n\0":
'???',

# Shigeru Aoba
"構うな…行くんだ。\n………行けッ！！\n\0":
'???',

# Maya Ibuki 
"ごめんね、この先は…、\n一人で…走って…。\n\0":
'???',

# JSSDF Staff
"こちら浅井支隊。\nパイロットを発見、排除しました。\n\0":
'???',

# Radio Voice [JSSDF]
"了解。\nそのまま発令所へ向かえ。\n\0":
'???',

# Misato Katsuragi 
"来たわね！！\n\0":
'???',

# Ritsuko Akagi 
"クッ、\nこんなところまで…。\n\0":
'???',

# Makoto Hyuga
"来やがった…！！\n\0":
'???',

# Shigeru Aoba
"野郎…！！\n\0":
'???',

# Maya Ibuki 
"この先は駄目、\n絶対に進ませない！！\n\0":
'???',

# Shinji Ikari, Toji Suzuhara, Kaworu Nagisa
"ミサトさんっ！\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Toji Suzuhara, Kaworu Nagisa
"リツコさんっ！！\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Toji Suzuhara, Kaworu Nagisa
"青葉さん！！\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Toji Suzuhara, Kaworu Nagisa
"マヤさんっ！！\n\0":
'???',

# Misato Katsuragi 
"行くわよ、走って！！\n\0":
'???',

# Ritsuko Akagi 
"ケイジはこの先よ。\n走るわよ！！\n\0":
'???',

# Makoto Hyuga
"走るぞ、あともう少しだ！！\n\0":
'???',

# Shigeru Aoba
"この先を出ると、ケイジはすぐだ。\n走るぞ！！\n\0":
'???',

# Maya Ibuki 
"ケイジまで、あとちょっとよ。\n走りましょう。\n\0":
'???',

# Ritsuko Akagi 
"その時がくれば、ここに来ると\n思っていましたわ。\n\0":
'???',

# Shinji Ikari
"はい！！\n\0":
'???',

# Asuka Soryu Langley
"ＯＫ！！\n\0":
'???',

# Toji Suzuhara 
"は、はい！！\n\0":
'???',

# Misato Katsuragi 
"あんた達にゃ、\nこれでもくれてやるわ！！\n\0":
'???',

# Ritsuko Akagi 
"見てなさい…。\n\0":
'???',

# Makoto Hyuga
"追いつかれる前に、ここを…。\n\0":
'???',

# Shigeru Aoba
"よし、見てろよ…。\n\0":
'???',

# Maya Ibuki 
"そうだ、あれを作動させて\n足止めを…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"素早くフロアに設置された\n爆破装置に手をかけた。▽\n$pがひとたび遠くに行ったのを\n確認して、パスワードを入力する。\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Kaworu Nagisa
"早く！！\n\0":
'Hurry!!\n\0',

# Toji Suzuhara 
"早う！！\n\0":
'???',

# Makoto Hyuga
"このエレベーターでなら、\nケイジまですぐだよ。\n行こう。\n\0":
'???',

# Maya Ibuki 
"このエレベーターを使えば\nケイジまでたどり着けるわ。\n行きましょう。\n\0":
'???',

# Misato Katsuragi 
"今、ネルフ本部は戦略自衛隊に\n侵攻されつつあるのよ。▽\n私達の持つエヴァを\n手に入れるために。▽\nそして、エヴァシリーズ、\n量産機が９体投入されているの。▽\nあなたには、これを全部殲滅して\nもらうわ。\n\0":
'???',

# Ritsuko Akagi 
"今、ネルフ本部は戦略自衛隊の\n手によって侵攻されつつあるの。▽\n私達の持つエヴァを\n奪い取るためにね。▽\nそして、エヴァシリーズ、\n量産機が９体投入されたという\n情報も入ったわ。▽\nあなたには、これを全部殲滅して\nもらいます。\n\0":
'???',

# Makoto Hyuga
"ネルフ本部は戦略自衛隊から攻撃を\n受けている。ここのエヴァを\n回収するつもりなんだ。▽\nそして、エヴァシリーズ、\n量産機が９体投入されたらしい。\n君が今から戦うべき相手だ。\n\0":
'???',

# Shigeru Aoba
"ネルフ本部は戦略自衛隊から\n攻撃を受けている。\nとうとう、政府も腹を括ったようだ。▽\nここのエヴァを回収し、\nネルフをつぶすつもりらしい。▽\nそして、エヴァシリーズ、\n量産機が９体投入された。▽\n君に頼るしかないんだ、エヴァ\nシリーズをすべて殲滅出来るのは\nパイロットである君しかいない。\n\0":
'???',

# Maya Ibuki 
"今、ネルフ本部は戦略自衛隊に\n侵攻されつつあるの。\n私達の持つエヴァを奪うためにね。▽\nそしてたった今、エヴァシリーズ、\n量産機が９体投入されたという\n情報も入ったわ。▽\nあなたがみんなの望みなの。\nお願い、エヴァシリーズをすべて\n殲滅させて、みんなを助けて…。\n\0":
'???',

# Shinji Ikari
"そんな、僕には…。\n\0":
'???',

# Asuka Soryu Langley
"数が多すぎるわよ。\n\0":
'???',

# Toji Suzuhara 
"む、無理ですよ…、\nワシにはそんな…。\n\0":
'???',

# Kaworu Nagisa 
"９機も…。\n僕の力で…。\n\0":
'???',

# Misato Katsuragi 
"全力を尽くすのよ、\nあなたは負けないわ。\n\0":
'???',

# Ritsuko Akagi 
"ここで戦わなかったら、\n後悔するわよ。\n死ぬ間際まで、後悔するのよ。\n\0":
'???',

# Makoto Hyuga
"君なら、出来る。\n僕が保証する…。\n\0":
'???',

# Shigeru Aoba
"みんなを救ってくれ。\n何があっても君を責めたり\nする者はいないよ。\n\0":
'???',

# Maya Ibuki 
"行くのよ…、\nお願い、みんなを助けて…。\n\0":
'???',

# Misato Katsuragi 
"ここから先は、\nあなた一人になるわ。▽\nでも、私は信じてる。\nあなたはきっと勝って\n帰ってくる…、きっとね。\n\0":
'???',

# Ritsuko Akagi 
"乗りなさい。\nそして勝ちなさい。▽\n私も何も思い残す事はないわ。\nあとは、あなたなりにベストを\n尽しなさい。\n\0":
'???',

# Maya Ibuki 
"エヴァに乗って。\nすぐに、発進準備に入るから。▽\n大丈夫、みんなあなたを見守る\n事しか出来ないけど…。▽\nごめんね、ありがとう…。\n\0":
'???',

# Makoto Hyuga
"僕は発令所に戻るよ。\nここから先は、君一人で\n行くんだ。▽\n大丈夫、エヴァの中が\n一番安全なんだ。\n頑張るんだよ…。\n\0":
'???',

# Shigeru Aoba
"あとは、お前の仕事だ。\n勝てよ、必ず…。\n待ってるからな。\n\0":
'???',

# Shinji Ikari
"は、はい…。\n\0":
'???',

# Asuka Soryu Langley
"任せて、\n私が負けるわけないでしょ。\n\0":
'???',

# Toji Suzuhara 
"生きてて下さいよ、\nワシが戻るまで絶対に…。\n\0":
'???',

# Kaworu Nagisa 
"必ず帰ります。\nそれじゃ、行ってきます。\n\0":
'???',

# Maya Ibuki 
"せんぱ…、▽\nセンパイ…、赤木博士がいません。▽\n駄目です、マギの自爆カウント、\n止まりません！\n\0":
'???',

# Misato Katsuragi, Ritsuko Akagi, Maya Ibuki 
"行ってらっしゃい。\n\0":
'???',

# Makoto Hyuga
"待ってるよ。\n\0":
'???',

# Shigeru Aoba
"行ってこい。\n\0":
'???',

# Makoto Hyuga
"赤木博士の所在不明！\nなんてこった、こんな時に！\nマギのカウント、あとわずか！\n\0":
'???',

# [Text Only - No Designated Speaker]
"近くで爆音が聞こえる。\nここも時間の問題のようだ。▽\nパイロットがエヴァにエントリー\nされるのを確認し、発令所までの\n道を急いだ。\n\0":
'???',

# Misato Katsuragi 
"こちら葛城、\nパイロット保護任務終了、\nこれより発令所へ帰還します。\n\0":
'???',

# Ritsuko Akagi 
"私よ、エヴァをすぐに打ち出して。\n私もすぐに戻るわ。\n\0":
'???',

# Maya Ibuki 
"こちら伊吹。\nパイロット、エヴァにエントリー。\nこれより発令所に帰還します。\n\0":
'???',

# Makoto Hyuga
"こちら日向。\nパイロット、エヴァにエントリー。\nこれより発令所に帰還します。\n\0":
'???',

# Shigeru Aoba
"こちら青葉。\nパイロット、エヴァにエントリー。\nこれより発令所に帰還します。\n\0":
'???',

# Kaworu Nagisa 
"ゼーレが決断を下したようだ。\nという事は、まず僕は消される\nだろうな…。\n\0":
'???',

# Shinji Ikari, Asuka Soryu Langley, Rei Ayanami, Hikari Horaki, Toji Suzuhara, Kensuke Aida, Kaworu Nagisa
"………！？\n\0":
'???',

# Male Staff
"これで終わりか…。\n\0":
'???',

# Shinji Ikari
"あ、あれ、生きてる…？\n\0":
'???',

# Asuka Soryu Langley
"痛くない…。\n私、生きてる…？\n\0":
'???',

# [Text Only - No Designated Speaker]
"ポケットからマギの\n操作リモコンを取り出すと\nカスパーは自爆を否定していた。\n\0":
'???',

# Asuka Soryu Langley
"ねえ、何かあったの？\n\0":
'???',

# Shinji Ikari
"９機…？\nそんな数を相手に…。\n\0":
'???',

# Shinji Ikari
"…血が。\n\0":
'???',

# Asuka Soryu Langley
"…血、出てるじゃない！！\n\0":
'???',

# Kaworu Nagisa 
"血が…。\n待って、すぐに発令所まで\n行きますから。\n\0":
'???',

# Shinji Ikari
"置いていくなんて出来ないよ！\n\0":
'???',

# Asuka Soryu Langley
"…このままだと、死んじゃうのよ！\nほら、つかまって！！\n\0":
'???',

# Kaworu Nagisa 
"僕は出来ない、\nあなたを置いていくなんて\n出来ません。\n\0":
'???',

# [Text Only - No Designated Speaker]
"そう言うと$bは、ぐらりと傾き\n糸の切れた操り人形のように\n崩れ落ちた。▽\n床にはおびただしい量の\n血だまりが出来ていた…。\n\0":
'???',

# Shinji Ikari
"必ず、勝つよ…。\n必ず…。\n行ってきます…。\n\0":
'???',

# Asuka Soryu Langley
"勝って来るわよ。\n勝利して、また帰って来るわよ。\n\0":
'???',

# Kaworu Nagisa 
"僕、行きます…。\nそして、必ず勝って見せます。\n\0":
'???',

# Ritsuko Akagi 
"娘からの最後の頼みよ。\n母さん、一緒に死んでちょうだい。\n\0":
'???',

# Female Staff
"赤木博士の所在不明！\nマギの自爆カウント\n止まりません！\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le139.evs
#
# Shinji Ikari
"変わる事が正しいわけじゃない。\n\0":
'???',

# Shinji's Shadow [Leliel]
"変化に期待する事を\nやめればいいんだ。▽\n代償を求めるうちは、\n変化を受け入れられないよ。\n\0":
'???',

# Shinji Ikari
"何の事…？\n\0":
'???',

# Shinji's Shadow [Leliel]
"期待をし、裏切られる。\n変わったのは、\n自分のせいじゃないと言う。▽\n変わる事を選んだのは、\n自分自身なのに。▽\n君は、期待の向こうにある絶望を\n避けようとして、変われないんだ。\n\0":
'???',

#
# ./USRDIR/event/tev0409.har_EXTRACT/tev0409.evs
#
# Shinji Ikari
"ひょっとしたら、\n死んじゃったりするのかな…。\n\0":
'???',

# Rei Ayanami 
"どうしてそんな事を言うの？\n\0":
'???',

# Rei Ayanami 
"あなたは死なないわ。\n\0":
'???',

# Rei Ayanami 
"私が守るもの。\n\0":
'???',

#
# ./USRDIR/event/tev1304.har_EXTRACT/tev1304.evs
#
# Misato Katsuragi 
"参号機、どうするの？\n\0":
'???',

# Ritsuko Akagi 
"ここで引き取る事になったわ。\n米国政府も第１支部までは\n失いたくないみたいね。\n\0":
'???',

# Misato Katsuragi 
"何よそれ。\n参号機と四号機はあっちが建造権を\n主張して強引に造ってたんじゃない。\n\0":
'???',

# Misato Katsuragi 
"今更危ないとこだけ\n押し付けるなんて\nムシのいい話ね。\n\0":
'???',

# Ritsuko Akagi 
"あの惨劇の後じゃ、\n誰だって弱気になるわよ。\n\0":
'???',

# Misato Katsuragi 
"で、起動実験はどうすんの？\n\0":
'???',

# Misato Katsuragi 
"例の「ダミー」を使うのかしら？\n\0":
'???',

# Ritsuko Akagi 
"これから決めるわ。\n\0":
'???',

# Kozo Fuyutsuki
"四号機の事故、\n委員会にどう報告するつもりだ。\n\0":
'???',

# Gendo Ikari
"事実の通り、原因不明さ。\n\0":
'???',

# Kozo Fuyutsuki
"しかし、\nここに来て大きな損失だな。\n\0":
'???',

# Gendo Ikari
"四号機と第２支部はいい。\nΣ機関もサンプルは失っても\nドイツにデータが残っている。\n\0":
'???',

# Gendo Ikari
"ここと初号機が残っていれば、\n充分だ。\n\0":
'???',

# Kozo Fuyutsuki
"しかし、委員会は血相を\n変えていたぞ。\n\0":
'???',

# Gendo Ikari
"予定外の事故だからな。\n\0":
'???',

# Kozo Fuyutsuki
"ゼーレも慌てて行動表を\n修正しているだろうな。\n\0":
'???',

# Gendo Ikari
"死海文書にはない事件も起こる。\n老人にはいい薬だよ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le511.evs
#
# Kaworu Nagisa 
"満足しているさ…。\n現時点ではね。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"欺瞞だよ、そんなの。\n先の事を\n考えてないはずないだろう？\n\0":
'???',

#
# ./USRDIR/event/tev0801.har_EXTRACT/tev0801.evs
#
# Ryoji Kaji
"ほーぉ、修学旅行か。\n行き先は？\n\0":
'???',

# Asuka Soryu Langley
"オキナワよ♪\nスクーバダイビングも\n出来るんだって。▽\nでも、折角なら加持さんと\n二人きりで行きたいわ。▽\nところで、加持さんって\n修学旅行はどこへ行ったの？\n\0":
'???',

# Ryoji Kaji
"ああ…。\n俺達、そんなのなかったんだ。\n\0":
'???',

# Ryoji Kaji
"セカンドインパクトが\nあったからさ。\n\0":
'???',

# Misato Katsuragi 
"あっ、言うの忘れてた。\nゴメン！▽\nあなた達、\n修学旅行は行っちゃ駄目よ。\n\0":
'???',

# Asuka Soryu Langley
"えー、どうしてなのよ！？\n\0":
'???',

# Misato Katsuragi 
"戦闘待機だもの。\nしょうがないでしょ。\n\0":
'???',

# Asuka Soryu Langley
"何よ、シンジ。\nアンタ、居たの？▽\nほらぁ、アンタも何か\n言ってやってよ！\n\0":
'???',

# Shinji Ikari
"えっと…、\n大方予想はついてたから。\n別に言う事なんか…。\n\0":
'???',

# Asuka Soryu Langley
"いっつも、\n待機、待機、待機って、\nそればっか！！▽\nたまには敵の居場所を\n突き止めて、攻めに\n行ったらどうなのよ！\n\0":
'???',

# Misato Katsuragi 
"それが出来たら、\nやってるわよ。▽\nま、これを機会に少しは\n勉強出来るでしょ？▽\nあなた達が\n学校のテストで何点とったかなんて\n筒抜けなんだから。\n\0":
'???',

# Asuka Soryu Langley
"バッカみたい、\n学校の成績が何よ。▽\n旧態依然とした減点式の\nテストなんか、\n何の興味もないわ！\n\0":
'???',

# Misato Katsuragi 
"郷に入っては郷に従え。\n日本の学校にも\nなれてちょうだい。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le129.evs
#
# Shinji Ikari
"僕は、そんな事していない。\n\0":
'???',

# Shinji's Shadow [Leliel]
"いいや、そうだね。\n自分が傷つかない為に、\n必死なんだろう。▽\n相手を不快にさせない為に。\n嫌われないように。▽\nでも結果、その行為が\n他人に嫌な思いをさせてるんだ。▽\n自分がなくなるよ、\nそんな事ばかりしていると。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le403.evs
#
# Toji Suzuhara 
"ホンマの自分…？\nなんや、ソレ…。\nどういうこっちゃ？\n\0":
'???',

# Toji's Shadow [Leliel]
"単純バカの熱血漢。\nそれは弱い自分を守る\n殻みたいなもんや。\n\0":
'???',

#
# ./USRDIR/event/cev0302.har_EXTRACT/cev0302.evs
#
# Rei Ayanami 
"月明かり。\n私の体。\n確かにあるもの。▽\n…心、…魂。\n目に見えないもの。\n確かにあるもの。▽\n続いていくもの…。\n\0":
'???',

# Rei Ayanami 
"空っぽの部分。\nその向こうにある私は…。▽\n私は………。\n私は誰…、私は何…。▽\n何…？\n\0":
'???',

# Rei Ayanami 
"私にあるもの…。▽\n名前。\nこの姿…。▽\nそして、空っぽの部分。▽\n私の中の、\n切り抜かれているものは…。\nどんな姿…、どんな形…？\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le205.evs
#
# Asuka Soryu Langley
"私は選ばれた人間なのよ！\nみんな私を大事にするわ。\n寂しくなんかない。\n\0":
'???',

# Asuka's Shadow [Leliel]
"そうよ。\nみんなが必要としているのは、\nパイロットとしての私。▽\n私そのものには、\n誰も目を向けないわ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le141.evs
#
# Shinji Ikari
"周りは変わってくれないの？\n\0":
'???',

# Shinji's Shadow [Leliel]
"変わるよ。\nそれが君にとって、\nいい事かどうかに関わらずね。\n\0":
'???',

#
# ./USRDIR/event/cev0306.har_EXTRACT/cev0306.evs
#
# Rei Ayanami 
"あなたは、\n知恵の実を持っているの？\n\0":
'???',

# ??? [Lilith]
"知恵の実しか、\n手に入れられなかったの。▽\n白い月が持ち去った後、\n残っていたのは\n知恵の実だけだったのよ。▽\nだから、追ったの。\n白い月を。\n生命の実を手に入れるために。\n\0":
'???',

# Rei Ayanami 
"あなたも生命の実を望むの？\n\0":
'???',

# ??? [Lilith]
"それは、あなたが知っているはず。\nあなたは、私だもの。▽\n私が生み出した生命…。\n人類には生命の実が欠けている。\n不完全な生命体よ。\n\0":
'???',

# Rei Ayanami 
"人々を完全なものにする為に、\n私は必要なの？\n\0":
'???',

# Rei Ayanami 
"私が私を見ている。\n私の中にいる、たくさんの私。\n\0":
'???',

# Rei Ayanami 
"あなたは、何…？\nどこから来たの？\n\0":
'???',

# ??? [Lilith]
"この星ではない、別の宇宙。\nもう、故郷はないわ。▽\n新しい故郷を求めて、\n人の姿を捨てて旅立ったの。\n多くの存在と共に。▽\n私の黒い月、他の月もそう…。\n\0":
'???',

# Rei Ayanami 
"生命の実を手に入れるの？\n\0":
'???',

# Teacher
"えーと、教科書を開いて。\n死の起源神話からだ。▽\n人類の祖先が、\n神、ないし精霊に\n石かバナナかを選ばされ、▽\n人類がバナナを選んだが為に\nバナナの様に短命になった\nという話だ。\n\0":
'???',

# Rei Ayanami 
"生命の実と…、知恵の実。\n\0":
'The Fruit of Life... and the Fruit of Wisdom.\n\0',

# Teacher
"また、神が人間を生成する時に\n石ではなく、やはりバナナや樹木を\n材料にした為、▽\n短命になったのだという神話もある。▽\nまあ、南方系に多く見られる神話だ。▽\n石を選んでいたら、ひょっとしたら\n人間は石のように不死の身体を得て\nいたのかもしれないな。\n\0":
'???',

# Rei Ayanami 
"私は…、▽\n私は………………………。 \n\0":
'???',

# Teacher
"綾波君…？\n大丈夫かね、綾波君…。\n保健室…、いや救急車だ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"…。▽\n………。▽\n………………。\n\0":
'???',

# ??? [Lilith]
"そう…。\n白い月の主から奪い取るの。▽\nだから、私は完全にならないと\nいけない。▽\nさあ、戻りなさい…。\n私へ還りなさい…。▽\nあなたはその姿を保てない。\n本来の姿ではないのだから。\n還るところは他にはないのだから。\n\0":
'???',

# ??? [Lilith]
"戻っておいで…、\n戻ってきなさい…。\n\0":
'Come back...\n Please come back to me...\n\0',

# ??? [Lilith]
"私の子らは、それを望んでいるわ。\n\0":
'???',

# Rei Ayanami 
"あなた、誰？\n\0":
'Who are you?\n\0',

# ??? [Lilith]
"あなたは、私。\n私は、あなた。▽\n人類を生み出したもの。\n人はリリスと呼ぶわ。\n\0":
'You are me.\nI am you.▽\nThe one who birthed humanity.\nPeople call us Lilith.\n\0',

#
# ./USRDIR/event/f052.har_EXTRACT/f052.evs
#
# Female Staff
"ああ、日向さん…。\n\0":
'???',

# Makoto Hyuga
"ああ、郵便物だね。\nわざわざありがとう。\n\0":
'???',

# Female Staff
"それと、これ。\n実家から来てますよ。\n\0":
'???',

# Makoto Hyuga
"実家？\n親父からだ…。\nでかいな、何が入ってるんだろう？\n\0":
'???',

# Makoto Hyuga
"いっ！？\nこれ、お見合い写真じゃ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"お見合い写真とともに\n父からの手紙が同封されている。\n震える手で、手紙を開く。▽\nマコトへ。\n私もそろそろ孫が見たい。\n日取りを決めたいので連絡しなさい。\n\0":
'???',

# Female Staff
"まあ、ふくよかで\nかわいい人じゃないですか…。▽\n日向さん、この人と\nお見合いしちゃうんですか！？\n\0":
'???',

# Makoto Hyuga
"ちょっと待って、\nこれは親父のワナなんだ！！\n\0":
'???',

# Makoto Hyuga
"うぅー、\nとうとう実力行使に出るなんて…。▽\nしかも、こんなもの職場に送って\n既成事実を作るつもりだったんだ…。\n\0":
'???',

# Female Staff
"おめでたい話じゃないですか。▽\nもしかしたら、日向さんの\n扶養家族が増えるかもって、\n総務課の友達に言っておきますね！\n\0":
'???',

# Makoto Hyuga
"待って、待ってくれって………！\n\0":
'Wait! Wait for me!\n\0',

# Female Staff
"タイヘン、タイヘ〜ン！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"気がつくと、見合い写真を\n持っていかれていた。\nもう、終りだ…。▽\n案の定、あっという間に\n見合いの話は広まった。▽\nそれから僕は、\n興奮して親父に電話をかけた。\n\0":
'???',

# Makoto Hyuga
"親父っ！！\nあんなの、職場に送るなって！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"でも、多分懲りずにまた、\n送ってくるんだろうな…。▽\n今までも見合いの話はあったけど、\nきっと今回は本気のようだ。▽\n…親父も孫が欲しい年頃か。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ふと、日向の姿が頭をよぎった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"日向が、\n浮かない顔をして歩いている。\n\0":
'???',

# Shinji Ikari
"日向さん、\nどうしたんですか？\n\0":
'???',

# Asuka Soryu Langley
"あっれー、青ざめた顔して、\nどうしたんですか？\n\0":
'???',

# Maya Ibuki 
"どうかしたんですか？\n\0":
'???',

# Shigeru Aoba
"日向、どうした？\n\0":
'???',

# Toji Suzuhara 
"ぼーっとして\nどないしたんですか？\n\0":
'???',

# [Text Only - No Designated Speaker]
"日向は、ビクリと驚いた様子で\nこちらへ振り向いた。▽\n相当何か焦っていたようで、\n手に持っていた書類を落とした。▽\n手伝って、書類を集めていると、\n手紙らしき物が出てきた。\n\0":
'???',

# Rei Ayanami 
"…手紙だわ。\n\0":
'???',

# Maya Ibuki 
"あら、これ書類じゃないわ。\n\0":
'???',

# Shigeru Aoba
"何だ、こりゃ？\n\0":
'???',

# Toji Suzuhara 
"何やろ、手紙や。\n\0":
'???',

# Kaworu Nagisa 
"手紙だ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"マコトへ。\n私もそろそろ孫が見たい。\n日取りを決めたいので連絡しなさい。▽\n手紙には、こう書かれていた…。\n\0":
'???',

# Makoto Hyuga
"み、見るなよ！！\n\0":
'???',

# Shinji Ikari
"日向さん、結婚するの？\n\0":
'???',

# Asuka Soryu Langley
"ひょっとして、結婚？\n\0":
'???',

# Rei Ayanami 
"結婚、ですか？\n\0":
'???',

# Maya Ibuki 
"ま、孫…！？\n\0":
'???',

# Shigeru Aoba
"日向ぁ…、\nお前一人独身貴族卒業かよ！！\n\0":
'???',

# Toji Suzuhara 
"いぃ〜〜〜！！\nけ、け、け、結婚するんスか？\n\0":
'???',

# Kaworu Nagisa 
"結婚…？\n\0":
'???',

# Makoto Hyuga
"ち、違う！\nこれは、お見合いしろって親父が…。\n\0":
'???',

# Shinji Ikari
"へぇぇ、結婚かぁ。\n\0":
'???',

# Asuka Soryu Langley
"そっか、\n日向さんも適齢期だもんね〜。\n\0":
'???',

# Rei Ayanami, Toji Suzuhara
"おめでとうございます。\n\0":
'???',

# Maya Ibuki 
"いいパパになれるんじゃ\nないんですか？\n\0":
'???',

# Shigeru Aoba
"相手はどんななんだよ。\nカワイーのか？\n\0":
'???',

# Toji Suzuhara 
"そんなん、\n隠さんでもええですよ。\n\0":
'???',

# Kaworu Nagisa 
"それじゃあ、お祝いしなきゃね。\n\0":
'???',

# Makoto Hyuga
"まず話を聞けって！！\n俺は、お見合いなんかしない！\n結婚なんかまだしないんだって！！\n\0":
'???',

# Makoto Hyuga
"あぁぁ、もう！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"日向は、実家に電話をかけ、\nすごい剣幕で見合いを\n一方的に断っていた。▽\n最後には、勘弁してくれと\n半泣きになって電話を切った。▽\nからかってやろうと思ったが、\n本当にまいっていたようなので\n声をかける事が出来なかった。\n\0":
'???',

# [Text Only - No Designated Speaker]
"何気に職員の立ち話に\n耳を立てていると、\n日向の話題を耳にした…。\n\0":
'???',

# Male Staff
"ホラ、作戦局第一課の日向さん、\n昨日、見合いだったらしいよ。\n\0":
'???',

# Misato Katsuragi 
"えっ…！！\n\0":
'???',

# Female Staff
"そうそう、総務部の友達がね、\n日向さんの父親がよく電話かける\nから、取り次いでいたって。▽\nそういう事だったのね。\n\0":
'???',

# Male Staff
"相当、嫌がっていたようだけど\n実際はどうだったのかな。\n気になるよねぇ。\n\0":
'???',

# Female Staff
"そうですね、\n意外とサッサと決めちゃって\n結婚するって事ありますからね。\n\0":
'???',

# Misato Katsuragi 
"ふぅぅぅぅん、お見合いねぇ…。\n\0":
'???',

# Kozo Fuyutsuki
"そうか、彼が見合いか…。\n\0":
'???',

# Ritsuko Akagi 
"ふーん、彼もなかなかやる\nじゃないの。\n\0":
'???',

# Ryoji Kaji
"結婚か…。\nま、親がいるなら結婚が一番の\n親孝行だろうからな…。\n\0":
'???',

# Makoto Hyuga
"もちろん、断りましたよ。\n\0":
'???',

# Misato Katsuragi 
"ア、アラ、日向くん。\nいたの？\n\0":
'???',

# Kozo Fuyutsuki
"あ、ああ、君か。\n\0":
'???',

# Ritsuko Akagi 
"日向くん…。\n\0":
'???',

# Ryoji Kaji
"おぉっと、いたのか？\n\0":
'???',

# Makoto Hyuga
"親の気が済むだろうと思って、\n行っただけです。▽\n結婚なんて、\nまだ興味ありませんよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"とは、言われたものの本当の\nところはどうだったのだろう。▽\n気になって、仕方がない…。\n\0":
'???',

#
# ./USRDIR/event/cev0301.har_EXTRACT/cev0301.evs
#
# Rei Ayanami 
"私が消える。▽\n私が生まれる。▽\n生きるの？\nここで今しばらく生きるの。\n誰が私をそうしたの…？\n\0":
'???',

# Rei Ayanami 
"渦を描いて再び流れる水。\n\0":
'???',

# Rei Ayanami 
"そこにいるのは誰？▽\n私を呼ぶのは誰？▽\n誰？▽\n誰？\n\0":
'???',

# Rei Ayanami 
"目覚めた朝。▽\n初めて見た光。▽\n流れる水。\n滴り落ちる水。\n\0":
'???',

# Rei Ayanami 
"………誰？\n\0":
'???',

# Rei Ayanami 
"ただよう…。▽\nむすぶ…。▽\nひらく…。▽\nしずむ…。▽\nうかぶ…。\n\0":
'???',

# Rei Ayanami 
"…朝？▽\n…そろそろ、行かないと。\n\0":
'???',

#
# ./USRDIR/event/tev0220.har_EXTRACT/tev0220.evs
#
# Misato Katsuragi 
"話しかけるには\n距離が離れているから、\n見る事しか出来ないの。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le414.evs
#
# Toji Suzuhara 
"なんや…、みんなも嘘つきなんか…。\n\0":
'???',

# Toji's Shadow [Leliel]
"皆もそうやからっていうて、\n自分が許されるって事はないで。\nそんな考え方が一番ヘタレや。\n\0":
'???',

#
# ./USRDIR/event/cev1407.har_EXTRACT/cev1407.evs
#
# Toji Suzuhara 
"…………………。▽\n何や、また説教か。\n\0":
'???',

#
# ./USRDIR/event/tev1404.har_EXTRACT/tev1404.evs
#
# Shinji Ikari
"くそ…、くそッ、くそッ！！\n\0":
'???',

# Shinji Ikari
"動け！　動け！　動いてよ！▽\n今動かなきゃ、\nみんな死んじゃうんだ！\nお願いだから動いてよ！！▽\n動け！　動いてよ！\nもう誰も、\n誰も傷つけたくないんだ！\n\0":
'???',

# Maya Ibuki 
"初号機、再起動！！▽\nまさか…、そんな。\nシンクロ率が４００％を\n超えています！\n\0":
'???',

#
# ./USRDIR/event/n007.har_EXTRACT/n007.evs
#
# Misato Katsuragi, Female Staff
"セントラルドグマに突如出現した使徒の正体は、\n\0":
'???',

# Misato Katsuragi 
"目標はエヴァ弐号機を操り、\nターミナルドグマを目指して侵攻しました。\n\0":
'???',

# Female Staff
"目標はエヴァ弐号機を操り、\nターミナルドグマ目指して侵攻しました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"初号機パイロット、碇シンジが目標を追撃。\n\0":
'???',

# Misato Katsuragi, Female Staff
"接触に成功し、目標に対し説得を試みます。\n\0":
'???',

# Misato Katsuragi, Female Staff
"結果、碇シンジによる、目標の説得に成功。\n\0":
'???',

# Misato Katsuragi, Female Staff
"以後「渚・カヲル」は従来通り、\n\0":
'???',

# Misato Katsuragi, Female Staff
"フィフス・チルドレン、\nエヴァパイロットとして存続する\nことになりました。\n\0":
'???',

# Misato Katsuragi, Female Staff
"しかし、目標の説得に失敗し、\n\0":
'???',

# Misato Katsuragi 
"初号機により目標を殲滅…。\n\0":
'???',

# Female Staff
"初号機により目標を殲滅しました。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le101.evs
#
# Shinji Ikari
"怖くなんか無いよ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"嘘だね。\n他人に嫌われていないか、\nいつも他人の中の自分を気にしてる。\n\0":
'???',

#
# ./USRDIR/event/tev0231.har_EXTRACT/tev0231.evs
#
# Misato Katsuragi 
"この食堂での食事は、\n今のように「着席して食事」を\n実行すればいいわ。\n\0":
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
# ./USRDIR/event/tev0411.har_EXTRACT/tev0411.evs
#
# Shinji Ikari
"綾波、綾波！\n大丈夫か！？\n\0":
'???',

# Shinji Ikari
"自分には…、\n自分には、他に何もないなんて\nそんな事言うなよ…。▽\nさよならなんて、\nそんな悲しい事言うなよっ！\n\0":
'???',

# Rei Ayanami 
"何、泣いているの…？\n\0":
'???',

# Rei Ayanami 
"ごめんなさい。▽\nこう言う時、\nどんな顔をすればいいのか\nわからないの。\n\0":
'???',

# Shinji Ikari
"…笑えば…いいと思うよ。\n\0":
'???',

#
# ./USRDIR/event/tev1505.har_EXTRACT/tev1505.evs
#
# Ryoji Kaji
"よぉ、シンジ君。\n\0":
'???',

# Shinji Ikari
"加持さん。\n\0":
'???',

# Ryoji Kaji
"ちょうどよかったよ。\n君と話がしたいと思っていた。\n\0":
'???',

# Shinji Ikari
"ミサトさんがいないんです。\n家に帰らなくって。\n\0":
'???',

# Shinji Ikari
"加持さんと一緒だと\n思ったんですけど。\n\0":
'???',

# Ryoji Kaji
"あいつは戻るよ。\n絶対にね。\n約束する。\n\0":
'???',

# Shinji Ikari
"居場所、知ってるんですか？\n\0":
'???',

# Ryoji Kaji
"いや、予想がついてるだけさ。\n実際は、知らないよ。\n\0":
'???',

# Ryoji Kaji
"さてと…、本題だ。\n君は、お母さんの事を\nどのくらい知ってるんだい？\n\0":
'???',

# Shinji Ikari
"母さん？\n何でそんな事を聞くんですか？\n\0":
'???',

# Ryoji Kaji
"まず、一つ。\nエヴァを造り出したのは\n君のお母さん、碇ユイだ。▽\nそして自ら、\nエヴァの起動実験に臨み\n命を落とした。\n\0":
'???',

# Shinji Ikari
"え………。\n\0":
'???',

# Ryoji Kaji
"二つ目だ。\n君は母親が消えるその瞬間を、\n見ていた。\n\0":
'???',

# Shinji Ikari
"ちょっ、ちょっ…、\nちょっと待ってください！▽\n何でそんな事を僕に！？\n\0":
'???',

# Ryoji Kaji
"母さんが死んだのは、\n父さんの実験によるものだと、\n君は…そう思っているんだろう。▽\n本当は違う。\nそれを君は知っていたはずだ。\n君は…真実を知る義務がある。\n\0":
'???',

# Shinji Ikari
"そんな…。\n僕が知ってるのは…。\n\0":
'???',

# Yui Ikari
"ごめんなさい、冬月先生。\n私が連れてきたんです。\n\0":
'???',

# Kozo Fuyutsuki
"ユイ君、今日は君の実験なんだぞ。\n\0":
'???',

# Yui Ikari
"だからなんです。\nこの子には、明るい未来を\n見せておきたかったんです。\n\0":
'???',

# Shinji Ikari
"僕は…。▽\n僕は、\nエヴァを知っていた…。\n\0":
'???',

# Ryoji Kaji
"君はエヴァを降り、\nそして再び乗った。▽\n俺は、君が真実と向き合う用意が\n出来たのだと判断した。▽\nそして君は、知らなければならない。\n真実を。▽\nお母さんの事も、\n君のお父さんの目的も。\n世界がどうなろうとしているのかを。\n\0":
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
# ./USRDIR/event/f003.har_EXTRACT/f003.evs
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
# ./USRDIR/event/cev0107.har_EXTRACT/cev0107.evs
#
# Shinji Ikari
"ま、待ってください！\nそれは…！？\n\0":
'???',

# Kozo Fuyutsuki
"さあっ！\n\0":
'???',

# Shinji Ikari
"い、嫌だ…。\nた、助けて。▽\n助けてよ、\n父さん、母さーーーーん！！\n\0":
'???',

# Kozo Fuyutsuki
"やあ、シンジ君…。\n\0":
'???',

# Shinji Ikari
"あ、どうも…。\n\0":
'???',

# Kozo Fuyutsuki
"どうだね、私の部屋まで\nちょっと付き合ってくれないかね？\n話があるのだが。\n\0":
'???',

# Shinji Ikari
"話ですか…。\nえ、えぇ…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ほうほうの体で逃げ出した。\n\0":
'???',

# Shinji Ikari
"あの…、話って何ですか？\n\0":
'???',

# Kozo Fuyutsuki
"似ている…。\n\0":
'???',

# Kozo Fuyutsuki
"君は本当によく似ている。\nユイ君に…。\n\0":
'???',

# Shinji Ikari
"母さんに…ですか？\n\0":
'???',

# Kozo Fuyutsuki
"シンジ君、これを着てくれないか？\n\0":
'???',

# [Text Only - No Designated Speaker]
"紙袋を渡された。\n中には、服が入っている。\n\0":
'???',

# Shinji Ikari
"え、何だこれ！？\n\0":
'???',

# Kozo Fuyutsuki
"そうだ、さあ、これを…。\n\0":
'???',

# Kozo Fuyutsuki
"おお、まさに…！！\nユイ君…。▽\n冬月先生と言ってくれないか？\n\0":
'???',

# Shinji Ikari
"…ふ、冬月先生。\n\0":
'???',

# Kozo Fuyutsuki
"さあ、並んで写真でも撮ろう。\n\0":
'???',

# Shinji Ikari
"ちょ、ちょっと…。\n\0":
'???',

# Kozo Fuyutsuki
"次はこれを…。\n\0":
'???',

# Shinji Ikari
"また、着替えるんですか！？\n\0":
'???',

# Shinji Ikari
"あの、僕…。\nこんな服は…。\n\0":
'???',

# Kozo Fuyutsuki
"さあ、このベッドに。\n上目遣いで。\n\0":
'???',

# Shinji Ikari
"わぁぁぁぁぁぁぁぁぁぁぁ！！\n\0":
'???',

# Kozo Fuyutsuki
"きれいだ…、ユイ君。\n\0":
'???',

# Shinji Ikari
"あのー…、副司令。\n\0":
'Ummmm... Deputy Commander...\n\0',

# Kozo Fuyutsuki
"冬月先生と言いたまえ！\n\0":
'???',

# Shinji Ikari
"ふ、冬月先生…、\n僕、いつまでこんな…。\n\0":
'???',

# Kozo Fuyutsuki
"ああ、そうか。\nでは次を急ごう。\n次は、このビキニを…。\n\0":
'???',

#
# ./USRDIR/event/tev0302.har_EXTRACT/tev0302.evs
#
# Toji Suzuhara 
"何ぃ！？\nシェルターの上のドンパチ\n見に行くて…。▽\nお前、正気か？\n\0":
'???',

# Kensuke Aida
"あそこに緊急用のハッチがある。\nなあ、頼むよ。\n\0":
'???',

# Toji Suzuhara 
"ケンスケ、お前な…。\n大概にせーよ。\n外に出たら、死ぬかもわからん。\n\0":
'???',

# Kensuke Aida
"見たいんだよ、あのロボットを！\nどうせここにいたって、\n死ぬ事だってありうるんだ。\n\0":
'???',

# Toji Suzuhara 
"ネルフが守ってくれるはずや。\nここにおったがええって。\n\0":
'???',

# Kensuke Aida
"その、守ってくれるネルフは\nあのロボット…転校生なんだぜ。\nお前が殴った、転校生。▽\nアイツ、乗りたくて\n乗ってるわけじゃないって\n言ってたよな…。▽\nお前のせいで、アイツが\n戦わなかったら…みんな死ぬよ。\n\0":
'???',

# Toji Suzuhara 
"うっ…。\n\0":
'???',

# Kensuke Aida
"トウジの妹は、あの時運悪く\n怪我を負ったけど…。▽\n俺達は…、守ってもらったんだ。\nあの、転校生にね。\n\0":
'???',

# Toji Suzuhara 
"…ほな、ちょっとだけやぞ。\n\0":
'???',

# Kensuke Aida
"そうこなくっちゃ！\nトウジには、アイツの\n戦いを見る義務がある。\n\0":
'???',

# Toji Suzuhara 
"調子のええやっちゃ…。\n\0":
'???',

#
# ./USRDIR/event/bs075.har_EXTRACT/bs075.evs
#
# Misato Katsuragi 
"じゃあ、今日の訓練は終わり。\n今日教えた事は忘れないように\nちゃんと覚えとくのよ。\n\0":
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
# ./USRDIR/event/cev0206.har_EXTRACT/cev0206.evs
#
# Asuka Soryu Langley
"加持センパイ♪\n\0":
'???',

# Ryoji Kaji
"アスカか。\nどうだ、調子は？\n\0":
'???',

# Asuka Soryu Langley
"加持さんの為に絶好調よ。\n\0":
'???',

# Ryoji Kaji
"そうか。\nこの調子で使徒を全滅させて\nもらわないとな。\n\0":
'???',

# Asuka Soryu Langley
"加持さん…。▽\n使徒を倒してしまって、\nエヴァが必要じゃなくなったら、\n私は、どうなるの？\n\0":
'???',

# Ryoji Kaji
"んー、そうなりゃ君は自由だ。\n好きなようにやればいい。\n\0":
'???',

# Asuka Soryu Langley
"加持さんは？\n\0":
'???',

# Ryoji Kaji
"俺もわからんさ。\nその後もネルフがあるのか\nわからんし。▽\n適当に生きていくよ。\n\0":
'???',

# Asuka Soryu Langley
"もう、\n一緒にいられなくなるの？\n\0":
'???',

# Ryoji Kaji
"多分な。\n君には、君の人生がある。\n俺には、俺の人生がある。\n\0":
'???',

# Asuka Soryu Langley
"（私の居場所…、\n　どこにもないんだ。）\n\0":
'???',

# Ryoji Kaji
"ま、将来何になりたいか、\nもう考え始めてもおかしくない\n歳だろ？▽\nアスカなら、何でも出来るさ。\n\0":
'???',

# Asuka Soryu Langley
"…私、加持さんといたい。\nずっと、一生。\nこんなに好きなのに。\n\0":
'???',

# Ryoji Kaji
"君が大人の目を持って\n俺を見たら…印象が変わるさ。\n俺はそんなに立派な人間じゃない。\n\0":
'???',

# Asuka Soryu Langley
"そんな事ない。\n加持さん以外の男は\n考えられないわ。▽\nそれともやっぱり…、\nミサトの事が忘れられないの？\n\0":
'???',

# Ryoji Kaji
"そういうところが子供なんだ。\n表層的な事しか見えていない。\n\0":
'???',

# Asuka Soryu Langley
"私が大人になったら、\n考えてくれる？\n\0":
'???',

# Ryoji Kaji
"その頃には、アスカの価値観が\n変わってるはずさ。▽\nきっと俺には見向きもしないだろう。\n\0":
'???'
}
