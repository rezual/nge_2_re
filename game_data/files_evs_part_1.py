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
'Rei.\n\0',

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
# ./USRDIR/event/tev0102.har_EXTRACT/tev0102.evs
#
# Gendo Ikari
"わかっている。\n人間には時間がないのだ。\n\0":
'I understand.\n Mankind has no time left.\n\0',

# Committeeman A
"使徒再来か。\nあまりに唐突だな。\n\0":
'???',

# Committeeman B
"１５年前と同じだよ。\n災いは何の前触れもなく\n訪れるものだ。\n\0":
'???',

# Committeeman C
"幸いとも言える。\n我々の先行投資が\n無駄にならなかった点においてはな。\n\0":
'???',

# Committeeman D
"そいつはまだわからんよ。\n役に立たなければ無駄と同じだ。\n\0":
'???',

# Committeeman B
"左様。\n今や周知の事実となってしまった\n使徒の処置、情報操作…、▽\nネルフの運用は全て、適切かつ\n迅速に処理してもらわんと困るよ。\n\0":
'???',

# Gendo Ikari
"その件に関しては\n既に対処済みです。\nご安心を。\n\0":
'???',

# Committeeman A
"しかし碇君。\nネルフとエヴァ、\nもう少しうまく使えんのかね。\n\0":
'???',

# Committeeman B
"零号機に引き続き、\n君らが初陣で壊した初号機の修理代。\n国が１つ傾くよ。\n\0":
'???',

# Committeeman C
"聞けば、あのおもちゃは\n君の息子に与えたそうではないか。\n\0":
'???',

# Committeeman D
"人、時間、そして金。\n親子そろっていくら使ったら\n気が済むのかね。\n\0":
'???',

# Committeeman C
"それに君の仕事は\nこれだけではあるまい。▽\n人類補完計画、\nこれこそが君の急務だ。\n\0":
'???',

# Committeeman B
"左様。▽\nその計画こそが、\nこの絶望的状況下における、\n唯一の希望なのだ。▽\n我々のね。\n\0":
'???',

# Keel Lorenz
"いずれにせよ、使徒再来における\n計画スケジュールの遅延は\n認められん。▽\n予算については、一考しよう。\n\0":
'???',

# Committeeman D
"では、あとは委員会の仕事だ。\n\0":
'???',

# Committeeman B
"碇君、ご苦労だったな。\n\0":
'???',

# Keel Lorenz
"碇、後戻りはできんぞ。\n\0":
'???',

#
# ./USRDIR/event/tev0201.har_EXTRACT/tev0201.evs
#
# Shinji Ikari
"ここは…？\n\0":
'???',

# Shinji Ikari
"…知らない天井だ。\n\0":
'???',

# Misato Katsuragi 
"お目覚めかしら？\n\0":
'???',

# Shinji Ikari
"はい…。\nカツラギ、さん…でしたよね？\n\0":
'???',

# Misato Katsuragi 
"ええ、葛城ミサト。\nミサトでいいのよ。▽\nあなたが気が付いたって連絡が\nあったから、迎えに来たの。▽\nで、どう？\n気分は…。\n\0":
'???',

# Shinji Ikari
"ええ、まあ…。\n\0":
'???',

# Misato Katsuragi 
"ん、快調そうね。\n今日はあなたをネルフ本部へ\n案内するわ。\n\0":
'???',

# Shinji Ikari
"父の職場ですか？\n\0":
'???',

# Misato Katsuragi 
"私やあなた、\nシンジ君の仕事の場でもあるのよ？\nさっ、行きましょう。\n\0":
'???',

# Shinji Ikari
"僕の？\n\0":
'???',

# Misato Katsuragi 
"そうよ。\nあなたは、エヴァンゲリオン\n初号機のパイロットなのだから。▽\nだから、\nあなたの仕事場でもあるのよ。\n\0":
'???',

# Shinji Ikari
"（また、アレに乗んなきゃ\n　いけないのか…。）\n\0":
'???',

#
# ./USRDIR/event/tev0202.har_EXTRACT/tev0202.evs
#
# Misato Katsuragi 
"ここが、私達の秘密基地、\nネルフ本部。\n世界再建の要となるところよ。▽\nさて、まずは…\n私の仕事部屋へ行きましょうか。\n\0":
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
# ./USRDIR/event/tev0203.har_EXTRACT/tev0203.evs
#
# Shinji Ikari
"これ…。\n\0":
'???',

# Misato Katsuragi 
"そう、あなたが搭乗した、\nそしてこれからも搭乗する事に\nなるエヴァ初号機よ。▽\nあ、コッチ来て。\n\0":
'???',

# Misato Katsuragi 
"この場所で、エヴァに関する情報を\n確認する事が出来るの。\n\0":
'???',

# Shinji Ikari
"さっき教えてもらった様に、\nこういった場所で%1iボタンを\n押せばいいんですね？\n\0":
'???',

# Misato Katsuragi 
"そ！\nまだまだこういう場所は\nいっぱいあるわ。\n\0":
'???',

# Misato Katsuragi 
"あらら…、大変。\n肝心な事を教えてなかったわね。\n一番重要なパラメーターよ。\n\0":
'???',

# Misato Katsuragi 
"ΑΤが低い時こそ\n出来る行動ってのもあるけど…。▽\n普段から目安として、５０くらい。\n普通の状態を保っておいて\n欲しいわねー。\n\0":
'???',

# Misato Katsuragi 
"そう、これはインパルス。\n衝動力、もしくは動機とでも\n言えばいいかしら。▽\n特殊な行動を実行する為の\n「後押し・きっかけ」を表すの。▽\nインパルスは何かしらの行動により\n蓄積されていくパラメータよ。▽\nインパルスの特徴として、\nΑΤが低い程、辛い体験を行う程\nインパルスは上がりやすくなるの。▽\nインパルスを消費する事で、\n特定の行動や戦闘行動が出来るわ。▽\nまぁ…、溜まったうっぷんを\nここぞという時吐き出して、\n上手く有効利用しなさいって事よ。\n\0":
'???',

#
# ./USRDIR/event/tev0204.har_EXTRACT/tev0204.evs
#
# Misato Katsuragi 
"さぁさ、遠慮なく。\nここでの食事はタダなんだから。\n\0":
'???',

# Misato Katsuragi 
"ごちそうさま。▽\nこうやって、食事をとったり\n水分をとったり、眠ったり…。▽\nきちんと自分の体調を管理するのも\n大事なパイロットの仕事よ。▽\nどう、食事をしたら\n元気になってきたでしょう？\n\0":
'???',

# Misato Katsuragi 
"他も大体同じ。▽\n水分を回復するには、\n飲み物を飲む。▽\n眠気を回復するには、\n部屋で眠る。▽\nＷＣを回復するには、\nトイレで用を足す。▽\n風呂を回復するには、\nお風呂に入る。▽\nそうすれば、\n体調管理はバッチリよ！\n\0":
'???',

#
# ./USRDIR/event/tev0205.har_EXTRACT/tev0205.evs
#
# Misato Katsuragi 
"ここは、自販機コーナーよ。\n水分を回復するには…。\n\0":
'???',

# Shinji Ikari
"あの自販機の前で\n%1iボタン。▽\nジュースを買って\n飲めばいいんですね。\n\0":
'???',

# Misato Katsuragi 
"そうよ。\nあ、チト…トイレ。\n\0":
'???',

# Maya Ibuki 
"あら、あなたシンジ君ね。\n私は、伊吹マヤ。▽\nオペレーターをしてるの。\nよろしく。\n\0":
'???',

# Shinji Ikari
"あ、よろしくお願いします。\n\0":
'???',

# Maya Ibuki 
"一人？\n\0":
'???',

# Shinji Ikari
"いえ、ミサトさんがトイレに。\nここで待っているんです。\n\0":
'???',

# Maya Ibuki 
"何か、わからない事はある？\n\0":
'???',

# Shinji Ikari
"さっきΑΤの事を教わったん\nですけど…まだ、いまいち。▽\nΑΤを普段から５０くらいにして\nおくように言われたんですけど。\nどうすればいいんでしょうか？\n\0":
'???',

# Maya Ibuki 
"そうね…、\nΑΤは、快適な体験によって\n上昇しやすい傾向にあるの。▽\n例えば、人に話し掛けて\n良い反応をしてくれた時なんかね。▽\n逆に、不快な体験をすることで\nΑΤは下降しやすいわ。人から\n冷たい反応を受けた時なんかよ。▽\nこれはあなただけでなく他人も同じ。\nあなたの行動が他人に対して\n影響を与え…。▽\n逆に他人の行動があなたに対し\n影響を与る事になるわ。▽\nΑΤを上げるも下げるも\nコミュニケーション次第。▽\n上手にコミュニケーションを行って、\nお互い良い関係を築く事が\nΑΤを上げる第一歩ね。\n\0":
'???',

# Shinji Ikari
"あんまり、人と付き合った事が\nないから、怒らせる事の方が\n多いかもな…。\n\0":
'???',

# Maya Ibuki 
"相手を怒らせない為には、\n自分がされて嫌な事は\n他人にもしない事。▽\nコミュニケーションにおいて\n基本中の基本よ。▽\n相手のΑΤも、自分のΑΤも\n下がっちゃうなんて\nつまらないでしょ？\n\0":
'???',

# Maya Ibuki 
"人はみんな、それぞれ自分達で\n考えて行動しているの。▽\n今、葛城一尉は、トイレを我慢して\nイライラしない様に、ちゃんと\n考えてトイレに行ったのよ。▽\nあなたと同じ。\nみんな、記憶も感情も\n持って行動しているの。▽\nそして、それぞれがそれぞれの\n人間関係を築いていくの。\n\0":
'???',

# Maya Ibuki 
"この、ステータス画面を\n見てちょうだい。▽\nΑΤやインパルス、体調以外にも、\n技能や、感情に関する情報が\n表示されるの。\n\0":
'???',

# Maya Ibuki 
"体調や感情も、人の行動に大きな\n影響や制限を与える要素よ。\n注意してね。\n\0":
'???',

#
# ./USRDIR/event/tev0207.har_EXTRACT/tev0207.evs
#
# Misato Katsuragi 
"ここは大浴場。\nまあ、職員専用のお風呂ね。\nココも自由に使っていいのよ。▽\nお風呂に入ることも体調管理の\n一環だから覚えておいてね。\n\0":
'???',

# Misato Katsuragi 
"えーっと大体見てまわったから\nリツコに会いに行きましょうか。▽\n多分、研究室にいるはずだわ。\n\0":
'???',

# Shinji Ikari
"…まだあるんですか？\n\0":
'???',

# Misato Katsuragi 
"ホンの一部よ、一部。▽\nでも、シンジ君が立ち入りを\n制限されている場所もあるから\n気をつけてね。▽\nじゃ、行くわよ。\n\0":
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
# ./USRDIR/event/tev0209.har_EXTRACT/tev0209.evs
#
# Misato Katsuragi 
"ここ、ネルフ施設マップでも\nセーブすることができるのよ。\n帰る前にセーブしなくていい？▽\n%4iボタンでシステムメニューを\n表示して「データセーブ」を\n選ぶといいわ。\n\0":
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
# ./USRDIR/event/tev0212.har_EXTRACT/tev0212.evs
#
# Misato Katsuragi 
"さてと、\nそろそろ出かけましょうか。\n\0":
'???',

# Shinji Ikari
"どこへですか？\n\0":
'???',

# Misato Katsuragi 
"ネルフ本部よ。▽\nさ、行きましょ。\n\0":
'???',

# Misato Katsuragi 
"おはよう、シンジ君。\nよく眠れた？\n\0":
'???',

# Shinji Ikari
"まあ、何とか…。\n\0":
'???',

# Misato Katsuragi 
"そうそう、シンジ君。\n時間について教えておくわ。▽\nあなたが活動出来るのは、\n朝の７時から、夜の１時までよ。▽\n夜の１時になったら、\n強制的に一日が終了するの。▽\nそして、次の日の始まりの\n朝７時まで時間が進むわ。\n\0":
'???',

# Misato Katsuragi 
"もう気づいてるでしょうけど、\n時刻はここに表示されているわ。▽\nここでの生活は\n常に時間が流れているから、\n時間を有効に使いなさいね。▽\nあと、特定時刻にならないと\n選択肢に出ない行動もあるわよ。\n\0":
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
# ./USRDIR/event/tev0215.har_EXTRACT/tev0215.evs
#
# Misato Katsuragi 
"改めて、ようこそ第３新東京市へ。\nこの画面は第３新東京市マップ。▽\n第３新東京市の中から、\n移動先を選択出来るの。\nとは言っても、今はネルフだけ。▽\nそのうち、学校も行けるから。\n転入手続きが終わるまで\nもちっと待ってね！\n\0":
'???',

# Misato Katsuragi 
"それから、この画面の時に\nセーブが出来るわ。▽\n%4iボタンでシステムメニューを\n表示して、「データセーブ」を\n選ぶといいわ。\n\0":
'???',

# Misato Katsuragi 
"今セーブをしておいてもいいし、\nこのままネルフへ移動しても\nいいわよ。\n\0":
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
# ./USRDIR/event/tev0217.har_EXTRACT/tev0217.evs
#
# Misato Katsuragi 
"%1iボタンを押すと、\n今のあなたはコレだけの行動を\nとれる事がわかるわ。▽\nこの行動の選択肢は、\nあなたの状態や\n周囲の状況によって変化するの。\n\0":
'???',

# Misato Katsuragi 
"例えば今、「ミサトに話しかける」\nという行動が表示されているでしょ。\n\0":
'???',

#
# ./USRDIR/event/tev0219.har_EXTRACT/tev0219.evs
#
# Misato Katsuragi 
"で、私がこの距離まで\n離れている時に\n%1iボタンを押した時は…。\n\0":
'???',

#
# ./USRDIR/event/tev0220.har_EXTRACT/tev0220.evs
#
# Misato Katsuragi 
"話しかけるには\n距離が離れているから、\n見る事しか出来ないの。\n\0":
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
# ./USRDIR/event/tev0222.har_EXTRACT/tev0222.evs
#
# Misato Katsuragi 
"ここで%1iボタンを押すと、\n\0":
'When you press the %1i button here,\n\0',

#
# ./USRDIR/event/tev0223.har_EXTRACT/tev0223.evs
#
# Misato Katsuragi 
"ホラ、「椅子に座る」という\n行動が出たでしょ？\n\0":
'???',

#
# ./USRDIR/event/tev0224.har_EXTRACT/tev0224.evs
#
# Misato Katsuragi 
"そういった、行動に関わる\n場所や物に近づくと、\nそこで出来る行動が表示されるの。\n\0":
'???',

# Misato Katsuragi 
"こういう場所は、\nマップのあちこちにあるから、\n%1iボタンを押して試してみてね。\n\0":
'???',

# Misato Katsuragi 
"じゃあ、次は\n初号機ケイジへ行きましょうか。\n\0":
'???',

#
# ./USRDIR/event/tev0226.har_EXTRACT/tev0226.evs
#
# Shigeru Aoba
"お疲れ様です、葛城一尉。\nあぁ、彼は初号機の…。\n\0":
'???',

# Misato Katsuragi 
"あら、青葉君。▽\nほら、紹介するわ。\n初号機のパイロット、\n碇シンジ君よ。\n\0":
'???',

# Shigeru Aoba
"よろしく、シンジ君。\n俺は、青葉シゲル。▽\n本部では情報分析担当の\nオペレーターなんだ。▽\nまだまだ、心は若いつもりだから\n仲良くやろうな。\n\0":
'???',

# Shinji Ikari
"あ、よろしく…。\n\0":
'???',

# Misato Katsuragi 
"青葉君、\nなーんか浮かない顔してるわね。\n\0":
'???',

# Shigeru Aoba
"副司令に説教食らって、\nまあ…。\nΑΤ下がりまくりですよ。\n\0":
'???',

# Misato Katsuragi 
"まぁまぁ、副司令はいつも\nあぁだから。\n青葉君は良くやってくれてるわ。▽\n仕事を頑張って、また\n挽回していけばいいじゃない。\n\0":
'???',

# Shigeru Aoba
"そうスね、少し気が晴れました。\nΑΤ持ち直しましたよ。\nそれじゃ…。\n\0":
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
# ./USRDIR/event/tev0230.har_EXTRACT/tev0230.evs
#
# Misato Katsuragi 
"ほら、シンジ君もテーブルへ\nいらっしゃい。▽\nさっき教えたように、\nここで「着席して食事」を\n選択してごらんなさい。\n\0":
'???',

#
# ./USRDIR/event/tev0231.har_EXTRACT/tev0231.evs
#
# Misato Katsuragi 
"この食堂での食事は、\n今のように「着席して食事」を\n実行すればいいわ。\n\0":
'???',

#
# ./USRDIR/event/tev0232.har_EXTRACT/tev0232.evs
#
# Misato Katsuragi 
"ごちそうさま。▽\nこうやって、食事をとったり\n水分をとったり、眠ったり…。▽\nきちんと自分の体調を管理するのも\nパイロットの大事な仕事よ。▽\nどう、食事をしたら\n元気になってきたでしょう？\n\0":
'???',

# Shinji Ikari
"あ、はい…。\n\0":
'???',

#
# ./USRDIR/event/tev0233.har_EXTRACT/tev0233.evs
#
# Misato Katsuragi 
"じゃあ、体調について\n説明をしましょう。▽\n%4iボタンを押してごらんなさい。\nシステムメニューを呼び出せるの。\n\0":
'???',

#
# ./USRDIR/event/tev0234.har_EXTRACT/tev0234.evs
#
# Misato Katsuragi 
"で、この中の\nステータスを選ぶと…。\n\0":
'???',

#
# ./USRDIR/event/tev0235.har_EXTRACT/tev0235.evs
#
# Misato Katsuragi 
"感情、コンディション、\n技能、そして…、▽\n空腹、水分、眠気、ＷＣ、風呂の\n５つの体調の状態を見る事が\n出来るの。▽\nそれぞれの体調メーターは、\n時間の経過と共に減少していくわ。▽\nメーターがカラになると、\nもう限界って状態ね。\n\0":
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
# ./USRDIR/event/tev0237.har_EXTRACT/tev0237.evs
#
# Shinji Ikari
"これらの状態を我慢していたら？\n\0":
'???',

# Misato Katsuragi 
"はい、ここからが重要！\nΑΤは体調の良し悪しにも\n影響を受けるの。▽\n高いΑΤを保つためにも、\n体調管理はしっかりなさいね。\n\0":
'???',

# Shinji Ikari
"わかりました…。\n無理はするなと言う事ですね。\n\0":
'???',

# Misato Katsuragi 
"そゆコト！▽\nあなたと同じ様に、\n他の人にも体調があるのよ。▽\nみんな、自分で低下した\n体調の回復を行っているわ。▽\n他人の行動にも\n注目してみてちょうだい。\n\0":
'???',

# Misato Katsuragi 
"じゃ、案内を続けましょう。\n自販機コーナーに行きましょうか。\n\0":
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
# ./USRDIR/event/tev0241.har_EXTRACT/tev0241.evs
#
# Maya Ibuki 
"そうね…、\nΑΤは、快適な体験によって\n上昇しやすい傾向にあるの。▽\n例えば、人に話しかけて\n良い反応をしてくれた時なんかね。▽\n逆に、不快な体験をすることで\nΑΤは下降しやすいわ。人から\n冷たい反応を受けた時なんかよ。▽\nこれはあなただけでなく他人も同じ。\nあなたの行動が他人に対して\n影響を与え…。▽\n逆に他人の行動があなたに対し\n影響を与る事になるわ。▽\nΑΤを上げるも下げるも\nコミュニケーション次第。▽\n上手にコミュニケーションを行って、\nお互い良い関係を築く事が\nΑΤを上げる第一歩ね。\n\0":
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
# ./USRDIR/event/tev0243.har_EXTRACT/tev0243.evs
#
# Maya Ibuki 
"このステータスで\nあなたの状態だけではなく、\n他の人の状態も確認出来るの。\n\0":
'???',

#
# ./USRDIR/event/tev0245.har_EXTRACT/tev0245.evs
#
# Maya Ibuki 
"相手や自分が喜ぶ事をやれば、\nΑΤを上げる事は\nそう難しい事じゃないわ。\n\0":
'???',

#
# ./USRDIR/event/tev0246.har_EXTRACT/tev0246.evs
#
# Misato Katsuragi 
"ふうー、すっきり…。\n気持ちに余裕が出たわ。▽\nあら、マヤちゃん。\n\0":
'???',

# Maya Ibuki 
"ふふ、ちょっと挨拶をしてました。\n私は、これで失礼します。\nじゃあね、シンジ君。\n\0":
'???',

# Misato Katsuragi 
"ハイ、お疲れさん。\nじゃあ、次。\n射撃場へ行きましょう。\n\0":
'???',

#
# ./USRDIR/event/tev0253.har_EXTRACT/tev0253.evs
#
# Ritsuko Akagi 
"横軸が関心の高さを表すの。\n相手方向に近いほど関心が高い。\n無視出来ない相手というわけね。\n\0":
'???',

#
# ./USRDIR/event/tev0257.har_EXTRACT/tev0257.evs
#
# Ritsuko Akagi 
"次に縦軸、好意についてよ。\n好意は相手への好き嫌いよ。\n\0":
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
# ./USRDIR/event/tev0262.har_EXTRACT/tev0262.evs
#
# Misato Katsuragi 
"じゃあ、私と一緒に…住む？\n\0":
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
# ./USRDIR/event/tev0271.har_EXTRACT/tev0271.evs
#
# Misato Katsuragi 
"じゃあ、\n軽く家の中を案内するわね。\n\0":
'???',

# Misato Katsuragi 
"まずはキッチンから。\n\0":
'???',

#
# ./USRDIR/event/tev0272.har_EXTRACT/tev0272.evs
#
# Misato Katsuragi 
"ここは冷蔵庫。\n私はビール♪\nシンジ君はジュースね。▽\n水分を回復したい時は、\nここでジュースを飲んでネ。\n\0":
'???',

#
# ./USRDIR/event/tev0276.har_EXTRACT/tev0276.evs
#
# Misato Katsuragi 
"ここが、お風呂よ。\n他人が入っていなければ\nいつ使っても構わないわ。\n\0":
'???',

#
# ./USRDIR/event/tev0277.har_EXTRACT/tev0277.evs
#
# Misato Katsuragi 
"チョッチ、散らかってるけど。\n私の部屋よ。▽\nまあ、ほとんど寝る為だけの\n部屋だけどね。\n\0":
'???',

#
# ./USRDIR/event/tev0278.har_EXTRACT/tev0278.evs
#
# Misato Katsuragi 
"ここがあなたの部屋よ。\n荷物もソッコーでこっちに\n回してもらったから。▽\nシンジ君が寝る時は、\nこの部屋を使って。▽\nまあ、こういった特定の場所で\n%1iボタンを押せば、\nその場に応じた行動を実行出来るわ。▽\n色んな所で試してごらんなさい。\n\0":
'???',

#
# ./USRDIR/event/tev0279.har_EXTRACT/tev0279.evs
#
# Misato Katsuragi 
"じゃあ、寝るにはまだ早いから、\nΑΤを高く保つ練習をしましょう。▽\n私やペンペンに話しかけたり、\n色んなアクションを試してみて。\n体調も自己管理でね。▽\nコミュニケーションを取りたいなら、\n話しかけたい相手に近づいて、\n%1iボタンを押すのよ。\n\0":
'???',

#
# ./USRDIR/event/tev0280.har_EXTRACT/tev0280.evs
#
# Misato Katsuragi 
"さてと、今日はこれから\nエヴァでの戦い方を教えます。▽\nこっちもね、\nちょうど先日の戦闘記録の\n分析が終わったとこなのよ。\n\0":
'???',

# Shinji Ikari
"…へぇ、そうですか。\nじゃあ、あの…使徒ってやつに\nついて何かわかったんですか？\n\0":
'???',

# Misato Katsuragi 
"いえ、使徒自身についての情報は\nあまり得られなかったんだけど…ネ。▽\nでも、使徒の行動パターンから、\n戦闘シミュレーションが\n出来るようになったの。\n\0":
'???',

# Shinji Ikari
"それはよかったですね。\n\0":
'???',

# Misato Katsuragi 
"まるで他人事みたいね。\nあなたの為のシミュレーション\nなのよ。\n\0":
'???',

# Shinji Ikari
"…僕の？\n\0":
'???',

# Misato Katsuragi 
"エヴァを動かすという事だけでも\n奇跡的な事なのに、あなたはそれを\n成し遂げ、そして使徒に勝った。\n\0":
'???',

# Shinji Ikari
"…そんな、僕はあの時、\n何もわからずに、ただ…。\n\0":
'???',

# Misato Katsuragi 
"そうね、\nまぐれで勝ったのかもしれない。▽\nでもね、次の使徒は\nいつ攻めてくるか、わからないの。▽\nシンジ君、あなたはもっと訓練を\nして、早く戦闘技術を高めてもらう\n必要があるのよ。\n\0":
'???',

# Shinji Ikari
"そっか、また僕はアレに乗らないと\nいけないんですね…。▽\nその為のシミュレーションか。\n\0":
'???',

# Misato Katsuragi 
"まぐれだとしても、\nあなたは使徒を倒したのよ。\nそれも才能のウチ。▽\n自信を持ちなさい。\nここにいるみんなが\nあなたをサポートするわ。\n\0":
'???',

# Misato Katsuragi 
"じゃ、訓練を始めましょうか。\n\0":
'???',

# Shinji Ikari
"はい…。\nじゃあ、着替えてきます。\n\0":
'???',

#
# ./USRDIR/event/tev0301.har_EXTRACT/tev0301.evs
#
# Misato Katsuragi 
"シンジ君、準備はいい？\n\0":
'???',

# Shinji Ikari
"準備？\nああ、またシミュレーション\nですか？\n\0":
'???',

# Misato Katsuragi 
"何言ってんのよ。\n今日から学校よ。▽\nあなたはエヴァのパイロットでも\nあるけど、中学生なんだし\n勉強が本分でしょ？▽\nじゃ、さっそく登校よ。\n忘れ物ないわね、シンジ君。\n\0":
'???',

# Misato Katsuragi 
"あ、えーっと、クラスはね。\n\0":
'???',

# Shinji Ikari
"２−Ａですよね。\n\0":
'???',

# Misato Katsuragi 
"そう。\nじゃ、オトモダチ\nいっぱい作ってね〜。▽\nオトモダチ、家に連れてきても\nいいわよ。\nおネエさん、歓迎してあげるから♪\n\0":
'???',

# Misato Katsuragi 
"これからは自分で学校に行くのよ。\nんじゃ、私はこれから仕事だから。\n勉強頑張ってね！\n\0":
'???',

# [Text Only - No Designated Speaker]
"授業開始のチャイムが鳴った。\n今朝は自習らしい。\n\0":
'???',

# Shinji Ikari
"あ………………。\n\0":
'???',

# Shinji Ikari
"彼女だ。\n\0":
'It\'s her.\n\0',

# [Text Only - No Designated Speaker]
"突然、パソコンのディスプレイに\nクラスメイトからのメールが表示\nされた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"二列前の女子がこちらを伺っている。\nこのメールは彼女が送信したの\nだろうか。\n\0":
'???',

# [Text Only - No Designated Speaker]
"「ＹＥＳ」\n\0":
'???',

# Toji Suzuhara 
"妹の見舞いや。\n朝からそんな、やいやい言いなや。\n\0":
'???',

# Kensuke Aida
"トウジ、見てアイツ。\n\0":
'???',

# Toji Suzuhara 
"何や、転校生かいな？\n\0":
'???',

# Kensuke Aida
"こないだの、あのロボット。\nアイツがパイロットなんだって。\n\0":
'???',

# Toji Suzuhara 
"何やて…？\n\0":
'???',

# Toji Suzuhara 
"ほな、アイツのせいで…。\nアイツが暴れよったから、\n妹は瓦礫の下敷きに…。\n\0":
'???',

# Kensuke Aida
"おい、トウジ！\n\0":
'???',

# [Text Only - No Designated Speaker]
"トウジが、シンジの元へ歩き、\n襟首を掴む。\n\0":
'???',

# Toji Suzuhara 
"おい、転校生。\n顔、貸せや！\n\0":
'???',

# Toji Suzuhara 
"すぐ戻るわ、委員長。\n\0":
'???',

# Toji Suzuhara 
"ン、のォ…！！\n\0":
'???',

# Kensuke Aida
"おい、トウジ！\nやり過ぎだろ！！\n\0":
'???',

# Toji Suzuhara 
"黙っとれ、ケンスケ。\nワシの妹は、こんな奴のせいで…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"トウジが再びシンジに\n殴りかかろうとしたその時、\n非常召集のサイレンが鳴り響いた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"突然のサイレンに周囲を見渡すと、\nあの少女が立っていた。\n\0":
'???',

# Rei Ayanami 
"非常召集。\n先に行くから…。\n\0":
'???',

# Shinji Ikari
"ま、待って…！\n\0":
'W-wait!\n\0',

# Toji Suzuhara 
"おんどれ！\n話は終わってへんど、転校生！\n\0":
'???',

# Kensuke Aida
"トウジ、シェルターへ行こう。\nきっと、こないだのアレだよ。\n\0":
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
# ./USRDIR/event/tev0303.har_EXTRACT/tev0303.evs
#
# Shinji Ikari
"何でまた乗ってるんだろう。\n人に殴られてまで…。\n\0":
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
# ./USRDIR/event/tev0404.har_EXTRACT/tev0404.evs
#
# [Text Only - No Designated Speaker]
"留守なのだろうか、\nレイの姿はない。▽\n年頃の少女が生活するにしては、\n余りにも殺風景だった。▽\nふと目にしたテーブルの上には、\nレンズにヒビの入った眼鏡がある。\n\0":
'???',

# Shinji Ikari
"眼鏡…？\n綾波の…じゃないよな？\n\0":
'Glasses...?\nThese aren\'t Ayanami\'s, are they?\n\0',

# [Text Only - No Designated Speaker]
"眼鏡を手に取り、かけてみる。\n\0":
'???',

# [Text Only - No Designated Speaker]
"玄関の方で人の気配がした。\n足音がこちらに近づいてくる。\n\0":
'???',

# Rei Ayanami 
"碇君…？\n\0":
'Ikari-kun...?\n\0',

# Shinji Ikari
"あ、綾波…。\n\0":
'A-Ayanami...\n\0',

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
'Commander Ikari.\n\0',

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
'You\'re Commander Ikari\'s son, aren\'t you?\n\0',

# Rei Ayanami 
"信じられないの？\nお父さんの仕事が。\n\0":
'Don\'t you believe\n in your father\'s work?\n\0',

# Shinji Ikari
"当たり前だよ、\nあんな父親。\n\0":
'???',

# [Text Only - No Designated Speaker]
"レイに平手打ちを食わされ、\n呆然とするシンジ。▽\n先程の眼鏡を手に、\nレイは家から出ていった。\n\0":
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
# ./USRDIR/event/tev0503.har_EXTRACT/tev0503.evs
#
# Maya Ibuki 
"あら、シンジ君。\n今、レイのハーモニクステストを\nやってるの。▽\nよかったら、見学していかない？\n\0":
'???',

# Shinji Ikari
"ハーモニクステスト？\n\0":
'???',

# Maya Ibuki 
"そうよ。\nあなたも定期的に行う事に\nなるんだから。▽\n案内するわ。\nついて来てね。\n\0":
'???',

# Maya Ibuki 
"センパイ、シンジ君です。\n\0":
'???',

# Ritsuko Akagi 
"もうすぐ、\nレイのテストが終わるわ。▽\nシンジ君も、近々テストを\n行う予定よ。\n\0":
'???',

# Shinji Ikari
"その、テストって何ですか？\n\0":
'???',

# Ritsuko Akagi 
"ここであなた達は\nテストと訓練が行えるわ。▽\n一つは、ハーモニクステスト。▽\nエヴァとパイロットの\n神経接続における調和を調整し、\nΑΤを高めるテストよ。▽\nもう一つはシンクロ技能訓練。▽\nパイロットとエヴァの\n神経交流を高め、エヴァの\n運動性能を引き出すための訓練よ。▽\nここネルフに来た時に、テストを\nして欲しい時は、私かマヤに\n話し掛けてくれたらいいわ。\n\0":
'???',

# Maya Ibuki 
"学校のテストなんかよりは簡単よ。\nそういえば、学校はどう？\n\0":
'???',

# Shinji Ikari
"まあ、それなりに。▽\n授業では、セカンドインパクトの\n話ばっかりですけど。\nみんな知ってる話なのに…。\n\0":
'???',

# Ritsuko Akagi 
"確かに、公式での話は\nみんな知っているわね。▽\n巨大隕石の落下による大惨事が\nセカンドインパクトだと\n言う事を。\n\0":
'???',

# Shinji Ikari
"えっ…、公式でって…。\n\0":
'???',

# Maya Ibuki 
"本当のセカンドインパクトは\nそんな事が原因ではないのよ。\n\0":
'???',

# Ritsuko Akagi 
"１５年前、\n人類は最初の「使徒」と呼称する\n人型の物体を南極で発見したの。▽\nでも、その調査中に原因不明の\n大爆発を起こしたのよ。▽\nそれが、セカンドインパクトの正体。\n\0":
'???',

# Shinji Ikari
"じゃあ…、\n僕達がエヴァで戦うってのは。\n\0":
'???',

# Ritsuko Akagi 
"予想されるサードインパクトを\n未然に防ぐ事が目的よ。▽\nそのためのネルフと\nエヴァンゲリオンなのだから。\n\0":
'???',

# Shinji Ikari
"……………。\nそうなん…ですか。\n\0":
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
# ./USRDIR/event/tev0505.har_EXTRACT/tev0505.evs
#
# Misato Katsuragi 
"仕事で旧東京まで\n行ってくるわ。\n多分、帰りは遅いから。\n\0":
'???',

# Shinji Ikari
"ああ、出張ですね。\n\0":
'???',

# Misato Katsuragi 
"食事は一人で\n適当に済ませておいてね。\nじゃ、行ってくるわ。\n\0":
'???',

# Ritsuko Akagi 
"遠隔操縦では、\n緊急対処に問題を残します。\n\0":
'???',

# Shiro Tokita
"パイロットに負担をかけ、\n精神汚染を起こすよりは\nより人道的だと思います。\n\0":
'???',

# Ritsuko Akagi 
"その為のパイロットと\nテクノロジーです。\n\0":
'???',

# Shiro Tokita
"まさか、科学と人の心が\nあの化け物を押さえるとでも？\n\0":
'???',

# Ritsuko Akagi 
"ええ、もちろんですわ。\n\0":
'???',

# Shiro Tokita
"人の心などという、曖昧な\nものに頼っているからネルフは\n先のような暴走を許すのですよ。▽\nその結果、国連は莫大な\n追加予算を迫られ、某国では２万の\n餓死者を出そうとしているのです。▽\nよかったですね、\nネルフが超法規にて保護されていて。▽\nあなた方は、その責任を取らずに\n済みますから。\n\0":
'???',

# Ritsuko Akagi 
"ネルフの主力兵器以外、\nあの敵性体は倒せません。\n\0":
'???',

# Shiro Tokita
"ΑΤフィールドですか？\nそれも今では時間の問題に\n過ぎません。▽\nいつまでもネルフの時代では\nありませんよ。\n\0":
'???',

# [Text Only - No Designated Speaker]
"会場が、嘲笑で沸いた。\n\0":
'???',

# Misato Katsuragi 
"何よ、トッチャンボーヤみたいな\n顔しちゃってさぁ！\nムッカツクぅぅぅ！！\n\0":
'???',

# Misato Katsuragi 
"にしても、極秘のはずの\nエヴァの暴走、ΑΤフィールド。\n何であいつが知ってるのよ。▽\n情報、ダダ漏れじゃない。\n諜報部は何やってんのかしら？\n\0":
'???',

# [Text Only - No Designated Speaker]
"会場に、\nどよめきと拍手が沸き上がる。\n\0":
'???',

# Ritsuko Akagi 
"葛城一尉、無駄よ！\n第一、どうやって止める\nつもりなの？\n\0":
'???',

# Misato Katsuragi 
"決まってんでしょ。\n人間の手で直接よ！\n\0":
'???',

# Controller
"制御棒の作動不能、\n炉心融解の危険あり！\n\0":
'???',

# Misato Katsuragi 
"停止手段は？\n\0":
'???',

# Controller
"方法は全て試しました！\n\0":
'???',

# Misato Katsuragi 
"いいえ。\n全てを白紙に戻す、\n最後の手段が残ってるはずよ。▽\nそのパスワードを教えなさい。\n\0":
'???',

# Shiro Tokita
"全プログラムのデリートは\n最高機密、私の管轄外だ。\n口外の権限はない。\n\0":
'???',

# Controller
"ΘΑ、厚木方面に向かい、\n進行中。\n\0":
'???',

# Misato Katsuragi 
"時間がないわ、これより先は\n私の独断で行動します。\nあしからず。\n\0":
'???',

# Misato Katsuragi 
"もしもし、日向君？\nこちら、葛城。▽\n日本重化学工業共同体が開発した\n使徒迎撃用ロボットが、\n披露会場にて暴走。▽\nすぐに初号機をまわして！\n\0":
'???',

# Makoto Hyuga
"了解。\n初号機の許可を申請し、\nすぐに駆けつけます。\n\0":
'???',

# Misato Katsuragi 
"シンジ君、私よ！！\nあれが目標のΘΑ。\n炉心融解の可能性があります。▽\nだから、目標をこれ以上\n人口密集地に近づけるわけには\nいかないの。▽\n目標と併走し、\n私を背後部に取り付けて。▽\n以後は目標の移動を可能な限り\n塞ぎ止めてね！\n\0":
'???',

# Shinji Ikari
"ミサトさんが乗るんですか？\nそんな無茶な！？\n\0":
'???',

# Misato Katsuragi 
"他にベターな方法がないの。\n後悔しないようにしたいじゃない？\nさ、行くわよ！\n\0":
'???',

# Shiro Tokita
"待ってくれ！\nプログラムの消去パスワードだ。▽\n「希望」\nパスワードは「希望」だ。\n…頼みます、ネルフの方々。\n\0":
'???',

#
# ./USRDIR/event/tev0506.har_EXTRACT/tev0506.evs
#
# Shinji Ikari
"ミサトさん、急いで！\n\0":
'Misato-san, hurry!\n\0',

# [Text Only - No Designated Speaker]
"ミサトがΘΑのハッチを開け、\n緊急手動制御室のコンソールに\n手を伸ばした。▽\nパスワードを入力する。\n\0":
'???',

# [Text Only - No Designated Speaker]
"制御棒が、軽々と動き始めた。▽\nΘΑが機能を停止させ、沈黙する。\n\0":
'???',

# Shinji Ikari
"すごいや、ミサトさん！\n僕、見直しちゃいました。\n\0":
'???',

# Shinji Ikari
"ミサトさん…！！\n大丈夫ですか、ミサトさん！？\n\0":
'???',

# Misato Katsuragi 
"ええ、何とかね…。\nビールが恋しいくらいかしら？\n\0":
'???',

# Misato Katsuragi 
"エラー？\nそんな、ばかな！！\n\0":
'???',

# [Text Only - No Designated Speaker]
"再度パスワードを入力する。\nしかし、答えは同じだった。\n\0":
'???',

# Misato Katsuragi 
"間違いない。\nプログラムを変えてあるんだわ。\n\0":
'???',

# Misato Katsuragi 
"でも、時間がない。\nこうなったら、イチかバチか！\n\0":
'???',

# [Text Only - No Designated Speaker]
"騒ぎの顛末を横に、リツコが\nあの男に連絡を取っている。▽\n何もかも事を見通していた、\n落ち着きのある声で…。\n\0":
'???',

# [Text Only - No Designated Speaker]
"ミサトが、\n小型原子炉の制御棒を押し始めた。\nしかし、びくともしない。\n\0":
'???',

# Ritsuko Akagi 
"葛城一尉の行動以外は、\nすべてシナリオ通りです。\n\0":
'???',

# Gendo Ikari
"そうか、ご苦労。\n\0":
'???',

# Misato Katsuragi 
"（ΘΑが止まったのは、\n　私の手ではない…。）▽\n（何者かの手により、\n　仕組まれた可能性が高いと\n　見るべきね…。）\n\0":
'???',

# Controller
"リアクター、\n限界点に達しました！\n\0":
'???',

# [Text Only - No Designated Speaker]
"ΘΑから、冷却水と蒸気が\n噴出した。\n\0":
'???',

# Shinji Ikari
"ミサトさん、逃げて！！\n\0":
'Misato-san, get out!!\n\0',

# Gendo Ikari
"どうだ…？\n\0":
'???',

# Misato Katsuragi 
"動けっ…動けぇぇぇぇぇ！！\n\0":
'???',

#
# ./USRDIR/event/tev0601.har_EXTRACT/tev0601.evs
#
# Misato Katsuragi 
"シンジ君、明日はお出かけよ♪\n\0":
'???',

# Shinji Ikari
"どこか、行くんですか？\n\0":
'???',

# Misato Katsuragi 
"横須賀沖の太平洋上、国連艦隊\nオーバー・ザ・レインボウよ。▽\n明日は早いから、今日は\n早めに休んでね。\n\0":
'???',

# Shinji Ikari
"…？\nはい…。\n\0":
'???',

# Misato Katsuragi 
"シンちゃん、\nちょっと早いけど出かけるわよ。\n\0":
'???',

# Shinji Ikari
"太平洋上の国連艦隊なんて、\nどうやって行くんですか。\n\0":
'???',

# Misato Katsuragi 
"国連軍のヘリを用意してあるわ。\nさ、行きましょ。\n彼女と仲良く出来るといいわね。\n\0":
'???',

# Shinji Ikari
"えっ…。\n何の事なんですか？\n\0":
'???',

# Shinji Ikari
"わぁ…、すごい。\n\0":
'???',

# Misato Katsuragi 
"あれが、国連所属の太平洋艦隊。\n今日はあの船で、太平洋を\nクルージングよ♪\n\0":
'???',

# Ryoji Kaji
"しかし、いきなりの実戦で\n彼のシンクロ率は、\n軽く４０は超えたそうだ。\n\0":
'???',

# Asuka Soryu Langley
"加持さん♪\n\0":
'???',

# Misato Katsuragi 
"げっ…！？\nなっ…なんでアンタが\nこんなところにいるのよ！\n\0":
'???',

# Ryoji Kaji
"よう、相変わらずだな。\n俺は彼女の随伴でね、\nドイツからの出張さ。\n\0":
'???',

# Misato Katsuragi 
"うかつだったわ…。\n十分考えられる事態だったのに。\n\0":
'???',

# Ryoji Kaji
"初めまして、碇シンジ君。▽\n俺は、加持リョウジ。\n特務機関ネルフ、特殊監査部に\n所属している。\n\0":
'???',

# Shinji Ikari
"ミサトさんとは、\nお知り合いなんですか？\n\0":
'???',

# Ryoji Kaji
"あぁ、彼女の事はよく知ってるよ。\n\0":
'???',

# Misato Katsuragi 
"仕事上の付き合いよッ！\n\0":
'???',

# Asuka Soryu Langley
"何、ムキになってるのよ。\n\0":
'???',

# Ryoji Kaji
"あれ、それ以外は…？\nシンジ君、彼女の寝相の悪さとか\n知ってる？\n\0":
'???',

# Misato Katsuragi 
"〜〜〜〜〜〜〜〜〜ッく、\n子供の前でしょーが、アンタねぇ！\n\0":
'???',

# Asuka Soryu Langley
"ちょーっとぉ、ミサトってば！\n私の弐号機、\n見に来たんじゃないの？\n\0":
'???',

# Misato Katsuragi 
"そ…そうそう、弐号機。\nそうだったわ。▽\nえっと、見せてもらえるかしら？\n案内してチョーダイ。\n\0":
'???',

# Asuka Soryu Langley
"私の弐号機は、\n実戦用に造られた、世界初の、\n本物のエヴァンゲリオンなのよ。▽\nアンタの初号機や零号機とは\n格が違うのよ！▽\nほら、サード。\nとっとと、来なさいよ。\n\0":
'???',

# Shinji Ikari
"えぇぇ…？\n\0":
'???',

# Asuka Soryu Langley
"チャ〜ンス！\n早速、私の戦いを見せてあげる。\nほら、サード、来るのよ！\n\0":
'???',

# Shinji Ikari
"そっ、そんな…。\n\0":
'???',

# Shinji Ikari
"わぁぁっ！！\n前、前！！\n\0":
'???',

# Asuka Soryu Langley
"ちょっ、ちょっと！！\nウッソ〜〜〜〜〜〜〜〜！！\n\0":
'???',

#
# ./USRDIR/event/tev0603.har_EXTRACT/tev0603.evs
#
# Ritsuko Akagi 
"あら、ご苦労さん。\n\0":
'???',

# Misato Katsuragi 
"荷物、無事に貰ってきたわよ。\n\0":
'???',

# Ritsuko Akagi 
"意外な荷物にも会ったわ。\n相変わらずね、加持君。\n\0":
'???',

# Misato Katsuragi 
"弐号機の引渡しが終わったんなら、\nさっさと帰りゃいいのよ。\n\0":
'???',

# Ritsuko Akagi 
"ところがね、出向の辞令が出て\nしばらくこっちにいるそうよ。\n\0":
'???',

# Misato Katsuragi 
"ぬわんですってぇ！？\n\0":
'???',

# Ritsuko Akagi 
"元彼に動揺するなんて、\n大人気ないわよ。\n\0":
'???',

# Misato Katsuragi 
"それを言わないでよぅ…。\n人生最大の汚点なんだから。\n\0":
'???',

# Gendo Ikari
"ご苦労だったな。\n\0":
'???',

# Ryoji Kaji
"お久しぶりです。\nいやはや、波乱に満ちた\n船旅でしたよ。▽\nあんなところで使徒襲来とは、\nちょっと話が違いましたね。\n\0":
'???',

# Gendo Ikari
"そのための弐号機だ。\n予備のパイロットも追加してな。\n\0":
'???',

# Ryoji Kaji
"ま、やはり\nコレのせいだったんでしょうが。\n\0":
'???',

# Ryoji Kaji
"既にここまで復元されています。▽\n硬化ベークライトで\n固めてありますが。▽\n生きています。\n間違いなく。▽\n人類補完計画の要ですね。\n\0":
'???',

# Gendo Ikari
"そうだ。\n最初の人間、アダムだよ。\n\0":
'???',

# Asuka Soryu Langley
"ハーイ、シンジ。\n\0":
'???',

# Shinji Ikari
"なっ、\n…何でここにいるんだよ！？\n\0":
'???',

# Asuka Soryu Langley
"私、ここに住む事になったの。▽\nホントは加持さんと一緒が\nいいんだけど、\n世間ってものがあるしね。▽\nじゃ、改めて自己紹介したげる。\n惣流・アスカ・ラングレーよ。\n\0":
'???',

# Shinji Ikari
"えっと、よろしく…。\n僕はシンジ。\n碇…、シンジ。\n\0":
'???',

# Asuka Soryu Langley
"何、湿っぽい声出してるのよ。▽\nこんな美人と一緒に住めるんだから、\nもっと嬉しそうにしなさいよ。\n\0":
'???',

# Shinji Ikari
"…え、えぇぇぇえ！？\n\0":
'???',

# Asuka Soryu Langley
"はン…。\nつまんない男…。\n\0":
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
# ./USRDIR/event/tev0703.har_EXTRACT/tev0703.evs
#
# Shinji Ikari
"はいっ！\n\0":
'Got it!\n\0',

# Asuka Soryu Langley
"オッケー、任せて！！\n\0":
'Okay, leave it to me!\n\0',

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
# ./USRDIR/event/tev1001.har_EXTRACT/tev1001.evs
#
# Toji Suzuhara 
"あーもォ、\n明日はテストかいな。\n\0":
'???',

# Kensuke Aida
"こないだのテストも\n散々だったしな。\n\0":
'???',

# Toji Suzuhara 
"ヤマ勘、外しただけやないか。\n結局勉強してへんかったんは\n同じとちゃうんか。\n\0":
'???',

# Toji Suzuhara 
"シンジ、お前勉強出来るんやろ？\n問題、どこが出そうか見積もって\n教えてくれへんか？\n\0":
'???',

# Shinji Ikari
"僕だって、ここ最近は\n勉強が出来なかったし…。▽\nそれに、勉強が出来る事と\n問題を予想する能力は\n別だと思うよ。\n\0":
'???',

# Toji Suzuhara 
"つれないのう…。\n\0":
'???',

# Kensuke Aida
"こうなったら、ヤマ勘大作戦だ！！\n今からシンジの家で、\n作戦会議をしよう。\n\0":
'???',

# Toji Suzuhara 
"お、サエとるやん。\n三人寄れば文殊の知恵って\n言うしな。\n\0":
'???',

# Shinji Ikari
"ハァ。\n…結局、こうなるのか。\n\0":
'???',

# Toji Suzuhara 
"お邪魔しまーす！\n\0":
'???',

# Misato Katsuragi 
"あら、いらっしゃい。\n\0":
'???',

# Toji Suzuhara 
"あぁぁ…。\nやっぱエエわぁ、ミサトさん。\n\0":
'???',

# Kensuke Aida
"大人の魅力ゥ………ン？\n\0":
'???',

# Kensuke Aida
"ミサトさん。\n昇進されたんですね。\nおめでとうございますっ！\n\0":
'???',

# Shinji Ikari
"えっ、何？\n昇進？\n\0":
'???',

# Kensuke Aida
"君達、ミサトさんの襟章に注目！\n\0":
'???',

# Kensuke Aida
"一尉から三佐に\n昇進されたのだぞ！！\n\0":
'???',

# Shinji Ikari
"あ、そ、そうなんですか。\nおめでとうございます。\n\0":
'???',

# Kensuke Aida
"よーっしゃあ！！\n作戦会議は中止！！▽\n今日はミサトさんの\n昇進を祝って祝賀会だ！！\n\0":
'???',

# Shinji Ikari
"ハァ。\nそして…結局、こうなるのか。\n\0":
'???',

# Toji Suzuhara 
"もうええ。\nワシもテストは諦めた。\n\0":
'???',

# [Text Only - No Designated Speaker]
"日が暮れて、\nミサトの昇進パーティーが\n始まった。\n\0":
'???',

# Ritsuko Akagi 
"折角祝ってもらってるのに、\n今日は静かなのね。\n\0":
'???',

# Misato Katsuragi 
"こいつがいるからよ。\n\0":
'???',

# Ryoji Kaji
"つれないなぁ。\n\0":
'???',

# Ritsuko Akagi 
"ホントに、\nそれが理由かしら？\n\0":
'???',

# Asuka Soryu Langley
"ミサト、暗い！\n\0":
'???',

# Kensuke Aida
"何か…御気に召さないとか。\n\0":
'???',

# Misato Katsuragi 
"ううん、こうして\nお祝いしてくれてる事は\nとっても嬉しいわ。\n\0":
'???',

# Misato Katsuragi 
"そうなるわね。\nでも、それが目的で\nネルフにいるんじゃないから。\n\0":
'???',

# Misato Katsuragi 
"ま、少しは嬉しいんだけど。\n\0":
'???',

# Shinji Ikari
"じゃあ、\nどうしてネルフに入ったんですか？\n\0":
'???',

# Misato Katsuragi 
"さてね。\n昔の事は忘れたわ。\n\0":
'???',

# Toji Suzuhara 
"まぁまぁ、パーッと行きましょう。\n\0":
'???',

# Kensuke Aida
"あ、僕がお酌しますッ！\n\0":
'???',

# Toji Suzuhara 
"ケンスケ、引っ込んどれ！\nワシの役目じゃい！\n\0":
'???',

# Hikari Horaki
"やぁね、男って。\n\0":
'???',

# Toji Suzuhara 
"うっさいわ、アホゥ。\n紳士のたしなみっちゅーやつや。\n\0":
'???',

# Toji Suzuhara 
"お前と違ぅて、ミサトさんは\n淑女なんやからな〜。\n\0":
'???',

# Hikari Horaki
"…………。\n鈴原のバカッ！！\n\0":
'???',

# Shinji Ikari
"もうっ、今日はお祝いなんだよ！\n\0":
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
'Is the pilot of\n Unit-01 there?\n\0',

# Gendo Ikari
"話は聞いた。\nよくやったな、シンジ。\n\0":
'???',

# Shinji Ikari
"え？\n…あ、は、はい。\n\0":
'???',

# Gendo Ikari
"では、葛城三佐。\n後の処理は任せる。\n\0":
'Now then, Major Katsuragi.\nI leave the rest in your hands.\n\0',

# Misato Katsuragi 
"シンジ君。\nこの間、聞いたわよね。▽\n私がどうしてネルフに\n入ったのかを…。\n\0":
'Shinji-kun, you asked me\n something the other day.▽\nAbout why I joined Nerv...\n\0',

# Misato Katsuragi 
"私の父はね、自分の研究、\n夢に生きる人だったわ。▽\nそんな父を許せなかった。\n憎んでさえいたわ。\n\0":
'My father, he was someone who\n lived for his research and his dreams.▽\nI could never forgive him for that.\nI could only hate him.\n\0',

# Shinji Ikari
"……………。\n（僕の父さんと同じだ。）\n\0":
'.........\n(Just like my father.)\n\0',

# Misato Katsuragi 
"母や私、家族の事など\n全く構ってくれなかった。▽\n周りの人達は繊細な人だと\n言っていたわ。\n\0":
'He didn\'t give a damn about\n my mom and me, or the family,\n or anything like that.▽\nPeople always said he was sensitive.\n\0',

# Misato Katsuragi 
"でも、ホントは心の弱い、\n現実から、私達家族という現実から\n逃げてばかりいた人だったのよ。▽\n子供みたいな人だったわ。▽\n母が父と別れた時も、\nすぐに賛成したわ。▽\n母はいつも泣いてばかりだったもの。▽\n父はショックだったみたいだけど、\nその時は自業自得だと笑ったわ。\n\0":
'But in truth he was just a weak\nperson running away from reality\n — the reality of his family.▽\nHe was like a kid. ▽\n母が父と別れた時も、\nすぐに賛成したわ。▽\n母はいつも泣いてばかりだったもの。▽\n父はショックだったみたいだけど、\nその時は自業自得だと笑ったわ。\n\0',

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
# ./USRDIR/event/tev1005.har_EXTRACT/tev1005.evs
#
# Misato Katsuragi 
"…碇司令は？\n\0":
'???',

# Shigeru Aoba
"使徒の放つ、\n強力なジャミングのため、\n連絡出来ません。\n\0":
'???',

# Misato Katsuragi 
"そう。\nじゃあ、全指揮私が\nとらせていただきます。\n\0":
'???',

# Ritsuko Akagi 
"エヴァの初期配置を\n外した時点でアウト。▽\nあなたの勝手な判断で\nエヴァを捨てる気？▽\n勝算は、０．００００１％。\n万に一つもないのよ。\n\0":
'???',

# Misato Katsuragi 
"可能性はゼロ、じゃないのよ。\nエヴァに賭けるだけよ。\n\0":
'???',

# Ritsuko Akagi, Makoto Hyuga
"葛城三佐！\n\0":
'Major Katsuragi!\n\0',

# Misato Katsuragi 
"現、責任者は私です。▽\n…やる事はやっときたいの、\n使徒殲滅は、私の仕事ですもの。\n\0":
'???',

# Ritsuko Akagi 
"仕事？　笑わせるわね。\n自分のためでしょ、\nあなたの使徒への復讐は。\n\0":
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
# ./USRDIR/event/tev1201.har_EXTRACT/tev1201.evs
#
# Asuka Soryu Langley
"あーぁ、つまんない。\n\0":
'???',

# Shinji Ikari
"どうしたの、アスカ？\n\0":
'???',

# Asuka Soryu Langley
"一緒に食事でもしようと\n思ってたのに。\n加持さん、出張なんだって。\n\0":
'???',

# Shinji Ikari
"そりゃ、\n出張くらいあるだろうね。\n\0":
'???',

# Shinji Ikari
"何で怒ってるの？\n\0":
'???',

# Asuka Soryu Langley
"アンタのその態度によっ！！\n\0":
'???',

# Shinji Ikari
"…えぇぇ！？\n\0":
'???',

# [Text Only - No Designated Speaker]
"一方、その頃。\n京都。\n\0":
'???',

# Ryoji Kaji
"１６年前…、\nここで何が始まったんだ？▽\nマルドゥック機関。▽\nエヴァンゲリオン操縦者選出の\nために設けられた、\n人類補完委員会直属の諮問機関。\n\0":
'???',

# Ryoji Kaji
"だが、活動は非公開で、\n組織の実態は未だ不透明。▽\nこのマルドゥック機関に繋がる\n１０８の会社のうち、\n１０６がダミー…。\n\0":
'???',

# Ryoji Kaji
"ここ、京都の外資系のケミカル会社\nシャノン・バイオも例外に漏れず…。\n１０７個目のダミーと言うわけか。\n\0":
'???',

# Ryoji Kaji
"しかし、\nこの会社の登記簿に並ぶ名は…。▽\n碇ゲンドウ、冬月コウゾウ…、\nそしてキール・ローレンツ。▽\nやはり、この組織の実態は…。\n\0":
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
# ./USRDIR/event/tev1302.har_EXTRACT/tev1302.evs
#
# Keel Lorenz
"今回の事件の唯一の当事者であり、\n被験者である初号機パイロットの\n直接尋問を拒否したそうだな。\n\0":
'???',

# Misato Katsuragi 
"はい。\n彼の情緒は大変不安定です。▽\n今ここに立つ事が、\n良策とは思えません。\n\0":
'???',

# Committeeman A
"では、聞こう。\n代理人、葛城三佐。\n\0":
'???',

# Committeeman B
"使徒が我々人類に\nコンタクトを試みたのでは\nないのかね？\n\0":
'???',

# Misato Katsuragi 
"被験者の報告では、\nそれは感じ取れません。▽\nイレギュラーな事件だと\n推定されます。\n\0":
'???',

# Committeeman C
"彼の記憶が正しいとすればな。\n\0":
'???',

# Misato Katsuragi 
"記憶の外的操作は認められません。\n\0":
'???',

# Committeeman C
"エヴァのＡＣレコーダーは\n作動していなかった。\n確認は取れまい。\n\0":
'???',

# Committeeman D
"第１２使徒は人間の精神、\n心に興味を持ったのか？\n\0":
'???',

# Misato Katsuragi 
"その返答は出来かねます。▽\n果たして使徒に「心」の概念が\nあるのか、人間の思考が理解\n出来るのか、全く不明ですから。\n\0":
'???',

# Committeeman A
"今回の事件には使徒がエヴァを\n取り込もうとした、という\n新しい要素がある。▽\nこれが予測され得る第１３使徒\n以降とリンクする可能性は？\n\0":
'???',

# Misato Katsuragi 
"これまでのパターンから、\n使徒同士の組織的な繋がりは、\nほぼ否定されています。\n\0":
'???',

# Committeeman B
"左様。\n単独行動のパターンである事は\n明らかだ、これまではな。\n\0":
'???',

# Misato Katsuragi 
"それは、\nどういう事なのでしょうか？\n\0":
'???',

# Keel Lorenz
"君の質問は許されない。\n\0":
'???',

# Keel Lorenz
"以上だ。\n下がりたまえ。\n\0":
'???',

# Keel Lorenz
"どう思うかね？\n碇君。\n\0":
'What do you think,\n Ikari-kun?\n\0',

# Gendo Ikari
"使徒は知恵をつけ始めています。\n残された時間は…。\n\0":
'The Angel are beginning to cultivate wisdom.\n The time left to us is...\n\0',

# Keel Lorenz
"あとわずか、という事か。\n\0":
'...running short?\n\0',

#
# ./USRDIR/event/tev1303.har_EXTRACT/tev1303.evs
#
# Toji Suzuhara 
"ほな、お先！\n\0":
'???',

# Kensuke Aida
"うん。\nじゃあな、トウジ。\n\0":
'???',

# Shinji Ikari
"…お待たせ。\nあ、トウジ帰っちゃったの？\n\0":
'???',

# Kensuke Aida
"うん。\nあーやって、早く帰る時は\n妹の見舞いに行く時なんだよ。\n\0":
'???',

# Shinji Ikari
"やっぱり、重症なの？\nそんなすぐに退院出来るものじゃ\nないんだ…。\n\0":
'???',

# Kensuke Aida
"まあ、ちょっと症状が\nややこしいらしいけど…。\n\0":
'???',

# Kensuke Aida
"でも、シンジが気にする\n必要はないよ。▽\nだからトウジだって、\n何も言わないんだからさ。\n\0":
'???',

# Shinji Ikari
"でも、僕のせいであんな…。\n\0":
'???',

# Kensuke Aida
"気にするなよ。\nお互い、気を遣う仲じゃないだろ。\nな？\n\0":
'???',

# Asuka Soryu Langley
"ねえ、相談ってさ…。▽\nひょっとして鈴原のコト？\n\0":
'???',

# Hikari Horaki
"うん…。\nわかってたんだ。\n\0":
'???',

# Hikari Horaki
"そう…かな？\n碇君、繊細な感じするし、\nそういうのには敏感なんじゃない？\n\0":
'???',

# Asuka Soryu Langley
"へー………。\n（恋は盲目ってこの事ね…。）\n\0":
'???',

# Asuka Soryu Langley
"ま、いいわ。\nまずは、この現状から\nステップを踏み出さなきゃね。\n\0":
'???',

# Hikari Horaki
"…えぇっ！？\nわ、私…そんな事は…。\n\0":
'???',

# Asuka Soryu Langley
"何よ、行動しないと\n私に相談した意味ないじゃない。\n\0":
'???',

# Asuka Soryu Langley
"ま、私に任せてよ。\n男がコロリとなる責め方…。\nうーん、やっぱり色気？\n\0":
'???',

# Hikari Horaki
"な、何言ってんのよ！！\n駄目、無理よ…。\n\0":
'???',

# Hikari Horaki
"私、ソバカスもあるし…、\nアスカみたいに綺麗な髪も\n素敵なプロポーションも持ってない。\n\0":
'???',

# Asuka Soryu Langley
"そんな悲観的にならなくても。\nうーん、じゃあ…。\n\0":
'???',

# Asuka Soryu Langley
"ヒカリが、\n人より自慢出来るものって？\n\0":
'???',

# Hikari Horaki
"料理…かな。\n\0":
'???',

# Asuka Soryu Langley
"そう、それよそれ！▽\nアイツ、いつもコンビニ弁当\nばっかだし、ここで手作り弁当でも\n渡してノックアウトさせんのよ！\n\0":
'???',

# Hikari Horaki
"食べて…くれるかな？\n\0":
'???',

# Asuka Soryu Langley
"大丈夫！！\n\0":
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
'So we\'ll select a Fourth?\n\0',

# Ritsuko Akagi 
"はい。\n一人速やかに「コア」の準備が\n可能な子供がいます。\n\0":
'Yes. There is one child\n for whom a core can\n be prepared right away.\n\0',

# Gendo Ikari
"任せる。\n\0":
'I\'ll leave it to you.\n\0',

# Gendo Ikari
"上がっていいぞ。\n\0":
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
# ./USRDIR/event/tev1308.har_EXTRACT/tev1308.evs
#
# Toji Suzuhara 
"あのな…、シンジ。\n\0":
'???',

# Shinji Ikari
"なに？\n\0":
'???',

# Toji Suzuhara 
"エヴァに初めて乗った時、\nどうやった？\n\0":
'???',

# Shinji Ikari
"何で、そんな事聞くの？\n\0":
'???',

# Toji Suzuhara 
"いや、何でもあらへん。\nただ…、ワシ…あの時。▽\nお前の気持ち、何も知らんと\nエラそうにお前の事殴ったりして…。\n\0":
'???',

# Shinji Ikari
"トウジ…？\n\0":
'???',

# Misato Katsuragi 
"地下のアダムとマルドゥック機関の\n秘密、知ってるんでしょ？\n\0":
'???',

# Ryoji Kaji
"はて？\n\0":
'???',

# Misato Katsuragi 
"とぼけないで。\n\0":
'???',

# Ryoji Kaji
"他人に頼るとは、\n君らしくないな。\n\0":
'???',

# Misato Katsuragi 
"なりふり構ってらんないの。\n余裕ないのよ、今。▽\n都合よく、フォース・チルドレンが\n見つかる。\nこの裏は何？\n\0":
'???',

# Ryoji Kaji
"一つ教えておくよ。\nマルドゥック機関は存在しない。\n陰で操ってるのはネルフそのものさ。\n\0":
'???',

# Misato Katsuragi 
"ネルフそのもの？\n碇司令が？\n\0":
'???',

# Ryoji Kaji
"コード７０７を調べてみるんだな。\n\0":
'???',

# Misato Katsuragi 
"７０７？\nシンジ君の学校を？\n\0":
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
# ./USRDIR/event/tev1312.har_EXTRACT/tev1312.evs
#
# Maya Ibuki 
"管制システム、切り替え終了。\n全神経、ダミーシステムへ直結完了。▽\n感情素子の３２．８％が不鮮明。\nモニター出来ません。\n\0":
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
# ./USRDIR/event/tev1315.har_EXTRACT/tev1315.evs
#
# Shinji Ikari
"ミサトさん。\n僕は、僕は人を…。\n\0":
'???',

# Misato Katsuragi 
"あの、シンジ君。\nごめん、ごめんね。▽\nあなたがやった事は正しいわ。\nでも、私は…あなたに…。\n\0":
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
# ./USRDIR/event/tev1403.har_EXTRACT/tev1403.evs
#
# Shinji Ikari
"…使徒だ。\n\0":
'... It\'s the Angel.\n\0',

# Kozo Fuyutsuki
"目標は！？\n\0":
'Target\'s status?!\n\0',

# Shigeru Aoba
"すぐ上です。\n防衛線を展開する間もなく、\n侵攻されました。\n\0":
'???',

# Shinji Ikari
"あれか？\n\0":
'???',

# Makoto Hyuga
"第１から１８番装甲まで損壊。\n\0":
'???',

# Misato Katsuragi 
"地上迎撃は間に合わないわ。\n弐号機をジオフロント内に配置！\n本部施設の直援にまわして！\n\0":
'???',

# Shinji Ikari
"僕は…、\nもう乗らないって決めたんだ。\n\0":
'I...\n I decided I wouldn\'t pilot anymore.\n\0',

# Ryoji Kaji
"よォ。\n他は避難したみたいだぞ。\n君はいいのかい？\n\0":
'???',

# Shinji Ikari
"加持さん！？\nな、何でここに？\n僕は戻りませんよ。\n\0":
'???',

# Ryoji Kaji
"そんな事より、外は危険だ。\nシェルターに行こう。\n\0":
'???',

# Shinji Ikari
"加持さんこそ、\nこんなところにいて\nいいんですか？\n\0":
'???',

# Ryoji Kaji
"いや、俺の戦闘配置はないんだ。\nアルバイトが公になってね。\n\0":
'???',

# Shinji Ikari
"…アスカ。\n\0":
'???',

# Ryoji Kaji
"これまで…か。▽\nまあいい、どうやら死ぬ前に\n人類の運命とやらを見れそうだ。\n\0":
'???',

# Shinji Ikari
"死ぬ？\n\0":
'Die?\n\0',

# Ryoji Kaji
"そうだ。▽\n使徒がネルフ本部地下に眠る\nアダムと接触すれば、\n人は全て滅びるといわれる。\n\0":
'That\'s right.▽\nIt\'s said that if an Angel makes contact\n  with Adam, the being asleep beneath H.Q.,\n humanity will be completely wiped out.\n\0',

# Ryoji Kaji
"サードインパクトでね。\n\0":
'The Third Impact.\n\0',

# Ryoji Kaji
"それを阻止出来るのは、\n使徒と同じ力を持つ\nエヴァンゲリオンだけだ。\n\0":
'Only the Evangelions,\n which have power equal to the Angels,\n are capable of stopping it.\n\0',

# Shinji Ikari
"僕は…。\n\0":
'I...\n\0',

# Ryoji Kaji
"君がどう行動しようと\nとがめはしない。\nただ、後悔の無いようにな。\n\0":
'???',

# Shigeru Aoba
"零号機、沈黙！\n使徒、移動を開始しました。\n\0":
'Unit-00 has gone silent!\nThe Angel has commenced movement.\n\0',

# Makoto Hyuga
"最終装甲板、融解！\n\0":
'The final armor plate has melted!\n\0',

# Misato Katsuragi 
"まずい、\nメインシャフトが丸見えだわ！\n\0":
'Not good!\n The main shaft is completely exposed!\n\0',

# Ritsuko Akagi 
"初号機はまだなの？\n\0":
'Any change with Unit-01?\n\0',

# Maya Ibuki 
"駄目です。\nダミープラグを拒否しています。\n\0":
'It\'s not working.\nThe dummy plug is being rejected.\n\0',

# Shinji Ikari
"乗せてください！\n\0":
'Please let me pilot!\n\0',

# Shinji Ikari
"僕を初号機に乗せてください！\n\0":
'Let me pilot Unit-01!\n\0',

# Shinji Ikari
"僕は、\n僕はエヴァンゲリオン初号機の\nパイロット、碇シンジです！▽\n僕をエヴァに乗せてください！\n\0":
'I...\n I\'m the pilot of Evangelion Unit-01, Shinji Ikari!▽\nLet me pilot the Eva, please!\n\0',

# Shinji Ikari
"お願いです！\n僕をエヴァに乗せてください！\n\0":
'I beg you!\n Let me pilot Eva Unit-01!\n\0',

# Gendo Ikari
"パイロットをエヴァに搭乗させる。\nエントリー準備、急げ。\n\0":
'The pilot may board the Eva.\n Prepare for immediate entry.\n\0',

# Misato Katsuragi 
"ハイッ！\n\0":
'Yes, sir!\n\0',

# Gendo Ikari
"乗れ…。\n\0":
'Get in.\n\0',

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
'You sure it\'s okay,\nrestrained in the cage?\n\0',

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
# ./USRDIR/event/tev1406.har_EXTRACT/tev1406.evs
#
# Rei Ayanami 
"碇君、\nどうしてあんな事をしたの？\n\0":
'???',

# Shinji Ikari
"許せなかったんだ。\n父さんが。\n\0":
'???',

# Shinji Ikari
"僕を裏切った父さんが。\n父さんは僕の気持ちなんか\nわかってくれないんだ！！\n\0":
'???',

# Rei Ayanami 
"碇君は、わかろうとしたの？\n\0":
'???',

# Shinji Ikari
"わかろうとした。\nわかろうとしたんだよ！！\n\0":
'???',

# Rei Ayanami 
"そうやって、嫌な事から\n逃げているのね。\n\0":
'???',

# Shinji Ikari
"いいじゃないか！\n嫌な事から逃げ出して、\n何が悪いんだよ！！\n\0":
'???',

#
# ./USRDIR/event/tev1407.har_EXTRACT/tev1407.evs
#
# Hikari Horaki
"鈴原…、学校に来ないの。\n家にも電話かけたけど、\n誰も出ないし…。▽\n相田君も何も言ってくれないし。\n碇君、鈴原から\n何か聞いてない？\n\0":
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
'Asuka...?\n\0',

# Shinji Ikari
"ミサトさん…？\n\0":
'Misato-san...?\n\0',

# Shinji Ikari
"ううん、違う。\nあの時、僕は、\n母さんのにおい…を感じた。\n\0":
'No, not them.\nWhat I sensed, back then...\nIt was the smell of my mother.\n\0',

# Gendo Ikari [Flashback]
"セカンドインパクトの後に\n生きていくのか、この子は…。\nこの地獄に…。\n\0":
'???',

# Gendo Ikari [Flashback]
"そうか、そうだったな。\n\0":
'???',

# Shinji Ikari
"父さん…、\n母さん…。\n\0":
'Father...\nMother...\n\0',

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
'A present.\nThe first one in eight years.▽\nAnd probably the last.\n\0',

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
'Yui-kun, today is your experiment.\n\0',

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
'What about him?\n\0',

# Intelligence Agent
"私は存じません。\n\0":
'???',

# Ryoji Kaji
"よぉ、遅かったじゃないか。\n\0":
'Hey, you\'re late.\n\0',

#
# ./USRDIR/event/tev1507.har_EXTRACT/tev1507.evs
#
# Misato Katsuragi 
"ただいま…。\n\0":
'I\'m home...\n\0',

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
'Idiot.\nYou\'re such an idiot.\n\0',

# Shinji Ikari, Asuka Soryu Langley, Rei Ayanami, Maya Ibuki, Makoto Hyuga, Shigeru Aoba, Toji Suzuhara
"加持さん…。\n\0":
'Kaji-san...\n\0',

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
# ./USRDIR/event/tev1509.har_EXTRACT/tev1509.evs
#
# Ritsuko Akagi 
"ミサト…？\n知らないわよ。▽\n彼女も忙しいから\n家に帰らない時だってあるわよ。\n\0":
'???',

#
# ./USRDIR/event/tev1601.har_EXTRACT/tev1601.evs
#
# Ritsuko Akagi 
"聞こえる、アスカ？\nシンクロ率が低下してるわよ。\nいつも通り、余計な事を考えずに。\n\0":
'???',

# Asuka Soryu Langley
"やってるわよ！！\n\0":
'I\'m doing it!!\n\0',

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
# ./USRDIR/event/tev1603.har_EXTRACT/tev1603.evs
#
# Shigeru Aoba, Male Staff
"未確認物体、衛星軌道上に\n突如出現しました！\n\0":
'???',

# Misato Katsuragi, Female Staff
"衛星軌道上？\n\0":
'???',

# Makoto Hyuga, Male Staff
"パターン青、使徒です！\n\0":
'Pattern blue. It\'s an Angel!\n\0',

# Shigeru Aoba, Female Staff
"使徒、映像、出ます。\n最大望遠です。\n\0":
'???',

# Makoto Hyuga, Female Staff
"衛星軌道から動きませんね。\nここから一定距離を保っています。\n\0":
'???',

# Misato Katsuragi 
"…ってことは、降下接近の機会を\nうかがってるのか、その必要もなく、\nここを破壊できるのか。\n\0":
'???',

# Makoto Hyuga, Male Staff
"こりゃ、うかつに動けませんね。\n\0":
'???',

# Ritsuko Akagi 
"こちらの射程距離内まで\n近づいてくれないと、\nどうしようもないわね。▽\nエヴァには、衛星軌道の敵は\n迎撃できないわ。\n\0":
'???',

# Misato Katsuragi 
"…そうね。\nまずは様子をうかがいましょう。\nレイは？\n\0":
'???',

# Maya Ibuki 
"零号機共に順調。\n行けます。\n\0":
'???',

# Misato Katsuragi 
"了解、零号機発進。\n弐号機アスカは\nバックアップとして、発進準備！\n\0":
'???',

# Asuka Soryu Langley
"バックアップ…！？\n私が…零号機の？▽\n冗談じゃないわよ。\nエヴァ弐号機、発進します！！\n\0":
'???',

# Ritsuko Akagi 
"アスカ、勝手に！！\n\0":
'???',

# Misato Katsuragi 
"いいわ、\n先行してやらせましょう。\n\0":
'???',

# Ritsuko Akagi 
"ここで駄目なら、\nアスカもこれまでという事ね。\n\0":
'???',

# Maya Ibuki 
"ラストチャンス、ですか。\n\0":
'???',

# Ritsuko Akagi 
"弐号機のパイロットの変換、\n考えとくわよ。\n\0":
'???',

# Makoto Hyuga
"あの、\n初号機は出さないんですか？\n\0":
'???',

# Misato Katsuragi 
"凍結なのよ。\n碇司令の絶対命令でね。\n\0":
'???',

#
# ./USRDIR/event/tev1606.har_EXTRACT/tev1606.evs
#
# Shinji Ikari
"リツコさん、アスカは！？\nアスカは、大丈夫なんですか…？\n\0":
'???',

# Ritsuko Akagi 
"命に別状は無いわ。\nただね…。\n\0":
'???',

# Ritsuko Akagi 
"精神に大きなダメージを\n受けたのよ。\nあの使徒との戦いでね…。\n\0":
'???',

# Shinji Ikari
"それって…、\nどういう事なんですか？\n\0":
'???',

# Ritsuko Akagi 
"心を壊されたとでも言えば\nいいかしら…。▽\n万が一回復出来るとしたら、\nそれこそ奇跡ね。\n\0":
'???',

# Shinji Ikari
"そんな…。\n\0":
'???',

# Ritsuko Akagi 
"とにかく長期的に\n様子を見ていくしかないわ。\n\0":
'???',

# Shinji Ikari
"アスカが…、そんな………。\n\0":
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
# ./USRDIR/event/tev1704.har_EXTRACT/tev1704.evs
#
# Asuka Soryu Langley
"はん、\n私が出たって足手まといな\nだけじゃないの？▽\nどうでもいいわよ、もう。\n\0":
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

# ./USRDIR/event/tev1801.har_EXTRACT/tev1801.evs
#
# Seele 06
"ついに、\n第１６の使徒までを倒した。\n\0":
'???',

# Seele 05
"これでゼーレの死海文書に\n記述されている使徒は、\n後一つ。\n\0":
'???',

# Keel Lorenz
"約束の時は近い。\n\0":
'The promised time is near.\n\0',

# Keel Lorenz
"その道程は長く、\n犠牲も大きかったがな。\n\0":
'???',

# Seele 05
"左様。\nロンギヌスの槍に続き、\nエヴァ零号機の損失。\n\0":
'???',

# Seele 09
"碇の解任には十分過ぎる\n理由だな。\n\0":
'???',

# Seele 03
"冬月を無事に返した、\n意味のわからぬ男でもあるまいに。\n\0":
'???',

# Seele 06
"エヴァシリーズ、\n既に８体まで用意されつつある。\n\0":
'???',

# Seele 09
"残るはあと、４体か。\n\0":
'???',

# Keel Lorenz
"第３新東京市の消滅は、\n計画を進めるよき材料になる。\n完成を急がせろ。▽\n約束の時は、その日となる。\n\0":
'???',

# Shinji Ikari
"トウジもケンスケも、\nみんな家を失って\nどこかへ行ってしまった。▽\n友達は…、友達と呼べる人達は\nいなくなってしまった、…誰も。▽\n母さん、アスカ、ミサトさん。\n僕はどうしたら…、\nどうすればいい…？\n\0":
'???',

# Kaworu Nagisa 
"歌はいいね。\n\0":
'???',

# Kaworu Nagisa 
"歌は心を潤してくれる。\nリリンの生み出した文化の極みだよ。▽\nそう、思わないかい？\n碇シンジ君。\n\0":
'???',

# Shinji Ikari
"僕の名を…？\n\0":
'???',

# Kaworu Nagisa 
"知らないものはいないさ。\n失礼だが、君は自分の立場を\n少しは知った方がいいと思うよ。\n\0":
'???',

# Shinji Ikari
"そう、かな？\n………あの、君は？\n\0":
'???',

# Kaworu Nagisa 
"僕はカヲル、渚カヲル。\n君と同じ仕組まれた子供、\nフィフス・チルドレンさ。\n\0":
'???',

# Shinji Ikari
"フィフス・チルドレン？\n君が？\nあの…渚、君。\n\0":
'???',

# Kaworu Nagisa 
"カヲルでいいよ。\n碇君。\n\0":
'???',

# Shinji Ikari
"僕も、あの、\nシ、シンジでいいよ。\n\0":
'???',

# Makoto Hyuga
"現在、フィフス・チルドレンは\nシンジ君と接触中の模様です。\n\0":
'???',

# Misato Katsuragi 
"委員会が直に送ってきた、\nこの少年の資料は何なのよ…？▽\n経歴その他、全てが抹消済み…。\nすべてが謎よ、どういう事かしら。\n\0":
'???',

# Kozo Fuyutsuki
"マルドゥック機関を通さず\n適任者として送り込まれた少年…。\n\0":
'???',

# Gendo Ikari
"ゼーレからの贈り物か…。\n計画の前倒しを\n老人は狙っているようだ…。\n\0":
'???',

#
# ./USRDIR/event/tev1803.har_EXTRACT/tev1803.evs
#
# Gendo Ikari
"我々に与えられた時間は少ない。\nだが、我らの願いを妨げる\nロンギヌスの槍は、既にないのだ。▽\n間もなく最後の使徒が現れるはずだ。\nそれを消せば願いがかなう。\nもうすぐだよ、ユイ。\n\0":
'???',

#
# ./USRDIR/event/tev1804.har_EXTRACT/tev1804.evs
#
# Rei Ayanami 
"私、何故ここにいるの？\n\0":
'???',

# Rei Ayanami 
"私、何故また生きているの？\n\0":
'???',

# Rei Ayanami 
"何のために？\n\0":
'???',

# Rei Ayanami 
"誰のために？\n\0":
'For whom?\n\0',

# Rei Ayanami 
"フィフス・チルドレン。\nあのヒト、私と同じ感じがする。\n…どうして。\n\0":
'???',

# Misato Katsuragi 
"どう？\n彼のデータ、入手出来た？\n\0":
'???',

# Makoto Hyuga
"これです。\n伊吹二尉から、\n無断で借用したものです。\n\0":
'???',

# Misato Katsuragi 
"すまないわね。\nドロボーみたいな事ばかり\nやらせて。▽\nで…。\n何、これ？\n\0":
'???',

# Makoto Hyuga
"マヤちゃんが公表出来ない\nわけですよ。\n理論上はありえない事なんですから。\n\0":
'???',

# Misato Katsuragi 
"そうね、謎は深まるばかりだわ。▽\nエヴァとのシンクロ率を\n自由に設定出来るとはね。\nそれも自分の意志で。▽\nまたも、\nなりふりかまってらんないか。\n\0":
'???',

#
# ./USRDIR/event/tev1805.har_EXTRACT/tev1805.evs
#
# Misato Katsuragi 
"誰もいない！？\nフィフスの少年ではないの？\n\0":
'No one?!\nIt\'s not the Fifth Child?\n\0',

# Makoto Hyuga
"いえ、パターン青。\n間違いありません。\n使徒です。\n\0":
'No, it\'s pattern blue.\nIt\'s definitely\nan Angel.\n\0',

# Kozo Fuyutsuki
"もしや、弐号機との融合を\n果たすつもりなのか？\n\0":
'???',

# Gendo Ikari
"または、破滅を導くためかだ。\n\0":
'???',

# Misato Katsuragi 
"そんな、バカな！！\n…アスカは！？\n\0":
'???',

# Shigeru Aoba
"３０３病室です！\n確認済みです！\n\0":
'???',

# Misato Katsuragi 
"じゃあ、一体誰が。\n\0":
'So then who could it be?\n\0',

# Gendo Ikari
"エヴァ初号機に追撃させる。\n\0":
'Pursue with Unit-01.\n\0',

# Maya Ibuki 
"無人です！\n弐号機にはエントリープラグは\n挿入されていません！\n\0":
'It\'s unmanned!\nUnit-02 has no entry plug\ninserted!\n\0',

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
# ./USRDIR/event/tev1902.har_EXTRACT/tev1902.evs
#
# Misato Katsuragi 
"出来そこないの群体として既に行き\n詰まった人類を完全な単体としての\n生物へと人工進化させる補完計画。▽\nまさに理想の世界ね。\nその為にまだ、\n委員会は使うつもりなんだわ。▽\nアダムやネルフではなく、\nあのエヴァを。\n加持君の予想通りにね。\n\0":
'???',

#
# ./USRDIR/event/tev1903.har_EXTRACT/tev1903.evs
#
# Kozo Fuyutsuki
"やはり人間の敵は、\n同じ人間だったか…。\nゼーレは総力を上げているな。\n\0":
'???',

# Kozo Fuyutsuki
"戦自、約１個師団を投入か。▽\n奴らの目的は、\n本部施設及び、残るエヴァ２体の\n直接占拠だな。\n\0":
'???',

# Gendo Ikari
"ああ。\nリリス、そしてアダムさえ\n我らにある。\n\0":
'Yes.\nAs long as we have Lilith and Adam.\n\0',

# Kozo Fuyutsuki
"老人達が焦るわけだ。\n\0":
'The old men must be getting impatient.\n\0',

# Gendo Ikari
"冬月先生、後を頼みます。\n\0":
'Fuyutsuki-sensei, I leave the rest to you.\n\0',

# Kozo Fuyutsuki
"…わかっている。\nユイ君によろしくな。\n\0":
'... I understand.\n Give my regards to Yui-kun.\n\0',

# Misato Katsuragi 
"サードインパクトを\n起こすつもりなのよ。▽\n使徒ではなく、\nエヴァシリーズを使ってね。▽\n１５年前のセカンドインパクトは\n人間に仕組まれたものだったわ。\n\0":
'They plan on triggering\n the Third Impact.▽\n Using not the Angels,\n but the Eva Series instead.▽\n Second Impact, fifteen years ago,\n was something plotted by humans.\n\0',

# Misato Katsuragi 
"けどそれは他の使徒が覚醒する前に\nアダムを卵へ還元する事で、被害を\n最小限に食い止める為だったのよ。▽\n私達人間もね、アダムと同じ\nリリスと呼ばれる生命体の源から\n生まれた１８番目の使徒なのよ。\n\0":
'But that was to minimize the damage\n by reverting Adam to an egg\n before the other Angels awakened.▽\n We humans are the 18th Angel,\n born from the one called Lilith,\n who is a source of life like Adam.\n\0',

# Misato Katsuragi 
"他の使徒達は別の可能性だったの。\nヒトの形を捨てた人類の…。▽\nただ、お互いを拒絶するしか\nなかった悲しい存在だったけどね。\n同じ人間同士も。▽\nいい、シンジ君。\nエヴァシリーズを全て\n消滅させるのよ。▽\n生き残る手段はそれしかないしかないわ。\n\0":
'The other Angels were an alternate possibility.\n Humanity that had abandoned its human form...▽\n But sadly, all we could\n do was reject one another, \neven though we\'re all human.▽ Okay, Shinji-kun?\n You have to destroy the entire Eva Series.▽\n It\'s the only way we\'ll survive.\n\0',

# Misato Katsuragi 
"いい、シンジ君。\nここから先は、\nもう、あなた一人よ。▽\n全て一人で決めなさい。\n誰の助けもなく。\n\0":
'???',

# Shinji Ikari
"僕は…駄目だ。\n駄目なんですよ。▽\n人を傷つけてまで、殺してまで\nエヴァに乗るなんて、\nそんな資格ないんだ。▽\n僕はエヴァに乗るしかないと\n思ってた。\nでも、そんなの誤魔化しだ。▽\n何もわかってない僕には\nエヴァに乗る価値もない。▽\n僕には、人の為に出来る事なんて\n何もないんだ。▽\n優しさなんか、かけらもない。\nズルくて臆病なだけだ。▽\n僕には人を傷つける事しか\n出来ないんだ。\nだったら、何もしない方がいい！\n\0":
'???',

# Misato Katsuragi 
"自分が嫌いなのね。\nだから、人も傷つける。▽\n自分が傷つくより、\n人を傷つけた方が心が痛い事を\n知っているから。▽\nでも、どんな思いが待っていても、\nそれはあなたが自分一人で\n決めた事だわ。▽\n価値のある事なのよ。\nシンジ君。\nあなた自身の事なのよ。▽\n誤魔化さずに、\n自分に出来る事を考え、\n償いは自分でやりなさい。\n\0":
'???',

# Shinji Ikari
"…ミサトさんだって。\n他人のくせに！\n何もわかってないくせにっ！！\n\0":
'???',

# Misato Katsuragi 
"他人だから、\nどうだってぇのよ！！▽\nあんた、このままやめるつもり！？▽\n今ここで何もしなかったら、\n私、許さないからね！\n一生あんたを許さないからね。\n\0":
'???',

# Misato Katsuragi 
"今の自分が絶対じゃないわ。\n後で間違いに気付き、後悔する。\n私はその繰り返しだった。▽\nヌカ喜びと自己嫌悪を重ねるだけ。\nでも、その度に前に進めた気がする。\n\0":
'???',

# Misato Katsuragi 
"いい、シンジ君。▽\nもう一度エヴァに乗って\nケリをつけなさい。\nエヴァに乗っていた自分に。▽\n何の為にここに来たのか、\n何の為にここにいるのか。\n今の自分の答えを見つけなさい。▽\nそしてケリをつけたら、\n必ず戻ってくるのよ。\n\0":
'???',

# Misato Katsuragi 
"約束よ…。\n\0":
'It\'s a promise...\n\0',

# Misato Katsuragi 
"大人のキスよ。\n帰ったら続きをしましょう。\n\0":
'That\'s a grown-up kiss.\nWe\'ll do the rest when you get back.\n\0',

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
'This is the Sea of L.C.L.\nThe place where life began.\n\0',

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
'What do you desire?\n\0',

# Kozo Fuyutsuki
"アンチΑΤフィールドか。\n\0":
'An Anti-A.T. Field.\n\0',

# Shinji Ikari
"綾波？\nここは？\n\0":
'Ayanami?\nWhere are we?\n\0',

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
'Am I dead?\n\0',

# Kozo Fuyutsuki
"人類の生命の源たるリリスの卵、\n黒き月。▽\n今更、その殻の中へと\n還る事は望まぬ。\nだが、それもリリス次第か。\n\0":
'???',

# Shinji Ikari
"でも、これは違う。\n違うと思う。\n\0":
'But this is wrong.\nIt doesn\'t feel right.\n\0',

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
'...Thank you.\n\0',

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
'I\'m not your doll.▽\nI am not you.\n\0',

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
# ./USRDIR/event/tev1905.har_EXTRACT/tev1905.evs
#
# [Scenario 1: Angel Attack - Best Ending]
#
# Kozo Fuyutsuki
"碇…。\nお前にはまだ、\n違う生き方がある。\n\0":
'???',

# Rei Ayanami 
"自分が何なのか、わからなかった。▽\n私…必要とされていたから\nいただけなの。\n碇司令に。▽\nそれだけだったの。\nそれでよかったの。\nあの人の為に生きていてもよかった。▽\nでも、会いたかった。\n碇君に。▽\n私、ただ…、▽\n会いたかったの。\n\0":
'???',

# Shinji Ikari
"行こう…。\nみんなの所へ。\n\0":
'Let\'s go...\nBack to everybody.\n\0',

# Yui Ikari [Flashback]
"あら、生きて行こうと思えば、\nどこだって天国になるわよ。\n\0":
'???',

# Yui Ikari [Flashback]
"だって、生きているんですもの。\n幸せになるチャンスは\nどこにでもあるわ。\n\0":
'???',

# Shinji Ikari
"ありがとう、母さん…。\n\0":
'Thank you, Mother...\n\0',

# Rei Ayanami 
"…碇君？\n\0":
'...Ikari-kun?\n\0',

# Shinji Ikari
"何の為にここに来て、\n何の為にここに居るのか…。▽\nそれはまだ、はっきりと\nわからないけれど…。▽\nでも、知っていたんだ。\n暖かさを、手を伸ばせば、\n触れられるという事を。▽\nただ、目を逸らしていただけなんだ。▽\n僕は、エヴァに乗らなければ\nずっと目を逸らし続けていたと思う。\n\0":
'???',

# Rei Ayanami 
"…碇君。\n\0":
'...Ikari-kun.\n\0',

# Shinji Ikari
"ありがとう。\n綾波にまた会えて、嬉しい。\n\0":
'???',

# Rei Ayanami 
"…聞こえたの、碇君の声。\n\0":
'...I heard your voice, Ikari-kun.\n\0',

# Shinji Ikari
"呼んだんだ。\n綾波を、みんなを。▽\n会いたかったから。\n\0":
'???',

# Shinji Ikari
"これから何が起こるか\nわからない。▽\nまだ、僕らの考えも及ばない事が\n起こるかもしれない。▽\nだから、会いに行かないと\nいけないって思ったんだ。\n\0":
'???',

# Shinji Ikari
"ありがとう、父さん…。\n\0":
'Thank you, Father...\n\0',

# Kozo Fuyutsuki
"彼女に会う事は、叶わなかったか。▽\n彼女が一人で初号機に残ったのは、\n我々の生きる強さを、\n信じていたからこそではなかったか。\n\0":
'???',

# Kozo Fuyutsuki
"いずれ、会える時が来る。\n我々は、彼女の意志をついで\n生きていかなければならないが。▽\nたとえ、一人になったとしても…。▽\nいや、生きていこうとする\n我々の中に既に彼女はいるのだ。\n\0":
'???',

# Gendo Ikari
"…それを、見失っていたのか。\n今まで…。\n\0":
'???',

#
# ./USRDIR/event/a000.har_EXTRACT/a000.evs
#
# [Angel: Sachiel]
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
# ./USRDIR/event/a002.har_EXTRACT/a002.evs
#
# [Angel: Ramiel]
#
# Shigeru Aoba, Male Staff
"国連艦隊より緊急入電！\n太平洋上にて新型エヴァの部品を\n搬送中、突如使徒が出現。▽\n襲撃を受けた模様です！\n\0":
'???',

# Misato Katsuragi 
"何ですって？\n\0":
'What was that?\n\0',

# Kozo Fuyutsuki, Misato Katsuragi 
"何？\n\0":
'???',

# Female Staff, Asuka Soryu Langley
"！？\n\0":
'?!\n\0',

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
# ./USRDIR/event/a007.har_EXTRACT/a007.evs
#
# [Angel: Tabris]
#
# Kaworu Nagisa 
"さあ、行くよ。\nおいで、アダムの分身、\nそしてリリンのしもべ…。\n\0":
'Come along now. Let us go,\nAdam\'s dark shadow,\nservant of the Lilin...\n\0'

# Makoto Hyuga, Male Staff
"エヴァ弐号機、起動！\n\0":
'Eva Unit-02 is active!\n\0',

# Misato Katsuragi 
"そんな、バカな！！\nまさか、…アスカなの？\n\0":
'But how?!\nIt can\'t be Asuka?\n\0',

# Kozo Fuyutsuki
"何だと…！？\n\0":
'???',

# Female Staff
"えっ？\n弐号機が！？\n\0":
'What?\nUnit-02 is?!\n\0',

# Maya Ibuki, Male Staff
"弐号機にはエントリープラグが\n挿入されていません。\n無人で動いています！\n\0":
'Unit-02 has no\n entry plug inserted.\nIt\'s moving unmanned!\n\0',

# Misato Katsuragi 
"誰もいない？\nどういう事！！\n\0":
'There\'s no one?\nWhat does that mean?!\n\0',

# Kozo Fuyutsuki
"無人…だと…？\n\0":
'Unmanned, you say?\n\0',

# Female Staff
"そんな事って…。\n\0":
'???',

# Makoto Hyuga, Male Staff
"セントラルドグマに、\nΑΤフィールドの発生を確認！\n\0":
'We\'ve confirmed an A.T. Field\nspreading in Central Dogma!\n\0',

# Misato Katsuragi 
"弐号機？\n\0":
'Unit-02?\n\0',

# Kozo Fuyutsuki
"弐号機か？\n\0":
'Is it Unit-02?\n\0',

# Makoto Hyuga, Male Staff
"パターン青。\n間違いありません。\n使徒です。\n\0":
'Pattern blue.\nWithout a doubt,\nit\'s an Angel.\n\0',

# Kozo Fuyutsuki
"何っ！？\n\0":
'What?!\n\0',

# Misato Katsuragi 
"使徒？\nあの少年が？\n\0":
'An Angel?\nThat boy?\n\0',

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
'I leave it to you, Shinji-kun!\n\0',

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
'I leave it to Unit-01!\n\0',

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
'I leave it to Unit-02!\n\0',

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
'I leave it to you, Rei.\n\0',

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
'I leave it to Unit-03!\n\0',

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
'I leave it to Unit-04!\n\0',

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
'Kaworu-kun!!\n\0',

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
'The hell is it this time...?\0',

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
'Shinji-kun,\ncommence firing!\n\0',

# Kozo Fuyutsuki
"初号機パイロット、\n射撃開始！\n\0":
'Pilot of Unit-01,\ncommence firing!\n\0',

# Female Staff
"初号機パイロットは、\n射撃開始！\n\0":
'Pilot of Unit-01,\ncommence firing!\n\0',

# Misato Katsuragi 
"アスカ、射撃開始！\n\0":
'Asuka,\ncommence firing!\n\0',

# Kozo Fuyutsuki
"弐号機パイロット、\n射撃開始！\n\0":
'Pilot of Unit-02,\ncommence firing!\n\0',

# Female Staff
"弐号機パイロットは、\n射撃開始！\n\0":
'Pilot of Unit-02,\ncommence firing!\n\0',

# Misato Katsuragi 
"レイ、射撃開始！\n\0":
'Rei,\ncommence firing!\n\0',

# Kozo Fuyutsuki
"零号機パイロット、\n射撃開始！\n\0":
'Pilot of Unit-00,\ncommence firing!\n\0',

# Female Staff
"零号機パイロットは、\n射撃開始！\n\0":
'Pilot of Unit-00,\ncommence firing!\n\0',

# Misato Katsuragi 
"トウジ君、射撃開始！\n\0":
'Toji-kun,\ncommence firing!\n\0',

# Kozo Fuyutsuki
"参号機パイロット、\n射撃開始！\n\0":
'Pilot of Unit-03,\ncommence firing!\n\0',

# Female Staff
"参号機パイロットは、\n射撃開始！\n\0":
'Pilot of Unit-03,\ncommence firing!\n\0',

# Misato Katsuragi 
"カヲル君、射撃開始！\n\0":
'Kaworu-kun,\ncommence firing!\n\0',

# Kozo Fuyutsuki
"四号機パイロット、\n射撃開始！\n\0":
'Pilot of Unit-04,\ncommence firing!\n\0',

# Female Staff
"四号機パイロットは、\n射撃開始！\n\0":
'Pilot of Unit-04,\ncommence firing!\n\0',

# Misato Katsuragi 
"エヴァ両機、射撃開始！\n\0":
'Both Evas,\ncommence firing!\n\0',

# Kozo Fuyutsuki
"エヴァ両機パイロット、\n射撃開始！\n\0":
'Pilots of both Evas,\ncommence firing!\n\0',

# Female Staff
"エヴァ両機パイロットは\n射撃開始！\n\0":
'Pilots of both Evas,\ncommence firing!\n\0',

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
# ./USRDIR/btl/tabris.har_EXTRACT/bk017.evs
#
# Shinji Ikari
"僕は、君の事を友達だと思ってた。▽\nこんな事にならずに\nずっと友達でいられると思ってた。\n\0":
'???',

# Kaworu Nagisa 
"それは、君の抱いた恐れ。\nそして、希望。▽\n僕は、君達リリンとは\n歩いてはいけないんだ。\n\0":
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
# ./USRDIR/btl/tabris.har_EXTRACT/bk031.evs
#
# Shinji Ikari
"どうして？\nカヲル君が使徒なの？\n\0":
'???',

# Kaworu Nagisa 
"言っただろ、\n僕が仕組まれた子供と言う事を。\n\0":
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
# ./USRDIR/btl/tabris.har_EXTRACT/bk037.evs
#
# Shinji Ikari
"行くなら本気で戦えよ。\n僕を本気で倒してから行けよ！！\n\0":
'???',

# Kaworu Nagisa 
"わかったよ、シンジ君。\n\0":
'I understand, Shinji-kun.\n\0',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk047.evs
#
# Kaworu Nagisa 
"………シンジ君。\n\0":
'...Shinji-kun.\n\0',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk053.evs
#
# Kaworu Nagisa 
"ヒトが…、互いを必要と思うのは\nヒトの中にある何かのためなんだ。\nただそれだけのためなんだ。▽\n…でも、その何かに対して、\nヒトはみな、息を呑むほどに純粋だ。\nとても、哀しいほどに…。\n\0":
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
# ./USRDIR/btl/bevent.har_EXTRACT/ba016.evs
#
# Shigeru Aoba, Male Staff
"$fエリア、国連軍、\n掃滅しました！\n\0":
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
# ./USRDIR/event/bb008.har_EXTRACT/bb008.evs
#
# Kozo Fuyutsuki
"…碇。\n\0":
'...Ikari.\n\0',

# Gendo Ikari
"……………………………。▽\nわかっている、初号機を出せ。\n凍結は解除だ！\n\0":
'???',

# Kozo Fuyutsuki
"一刻を争う。\nすぐに初号機を出せ。\n\0":
'???',

# Male Staff
"はっ…！！\n\0":
'Yessir!!\n\0',

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
# ./USRDIR/event/bs002.har_EXTRACT/bs002.evs
#
# [Text Only - No Designated Speaker]
"$lが退院しました。\n\0":
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
# ./USRDIR/btl/bevent.har_EXTRACT/d011.evs
#
# Toji Suzuhara 
"ぎゃあ！！\n\0":
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
'???',

# Kaworu Nagisa 
"やめろ、僕をどうするつもりだ！\n計画なんか知らない！！\nそんなもの押し付けないでくれ！\n\0":
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
# ./USRDIR/event/bs082.har_EXTRACT/bs082.evs
#
# Kozo Fuyutsuki
"よろしい。\nでは次に、使徒の動きについてだ。▽\n君は常に次の使徒の位置を\n読まなければならない。\nこれが君の重要な仕事だ。▽\n使徒の動きを読み、状況に応じた\n指示を心がけてもらいたい。\n\0":
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
# ./USRDIR/event/cev0111.har_EXTRACT/cev0111.evs
#
# [Scenario 2: Shinji - Scene with Kaji]
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
# ./USRDIR/event/bs012.har_EXTRACT/bs012.evs
#
# Rei Ayanami 
"…っくぅぅぅぅぅ！\n\0":
'???',

#
# ./USRDIR/event/n010.har_EXTRACT/n010.evs
#
# [Post-Battle Report: Sahaquiel, Success and Failure]
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
'Sahaquiel\n\0',

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
# [Psychological: Asuka]
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
'Shut up!!\n\0',

# Shinji Ikari
"そうしないと、自分自身が\n消えてしまうからだろ…。\n\0":
'???',

# Asuka Soryu Langley
"うるさい、うるさい、うるさい！！▽\nみんなキライ、大キライ…。▽\nでも、私…嫌われたくない。\n一人になりたくない…。\n\0":
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
# ./USRDIR/event/f094.har_EXTRACT/f094.evs
#
# [Text Only - No Designated Speaker]
"これからは、\nこの部屋がシンジの部屋です。\n\0":
'From now on, this will be Shinji\'s room.\n\0',

# [Text Only - No Designated Speaker]
"これまでシンジが生活していた\n部屋は、新たな同居人のアスカが\n使用することになりました。\n\0":
'It\'s been decided that new\n housemate Asuka will use the room\n where Shinji stayed previously.\n\0',

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
# ./USRDIR/event/cev0104.har_EXTRACT/cev0104.evs
#
# [Scenario 2: Shinji - Scene with Misato]
#
# Misato Katsuragi 
"シンちゃーん！\nちょっと来てー。\n\0":
'Shin-chan!\nC\'mere a sec.\n\0',

# Shinji Ikari
"はぁい。\n\0":
'Sure.\n\0',

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
}
