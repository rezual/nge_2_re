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
'I mustn\'t run away.\nI mustn\'t run away.\nI mustn\'t run away...!\n\0',

# Shinji Ikari
"やります。\n僕が乗ります！\n\0":
'I\'ll do it.\nI\'ll pilot it!\n\0',

#
# ./USRDIR/event/tev0102.har_EXTRACT/tev0102.evs
#
# Gendo Ikari
"わかっている。\n人間には時間がないのだ。\n\0":
'I understand.\nMankind has no time left.\n\0',

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
'Don\'t you believe\nin your father\'s work?\n\0',

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
'I don\'t want to eat anything.\n\0',

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
'Uh... wait.\n\0',

# Rei Ayanami 
"さよなら…。\n\0":
'Farewell...\n\0',

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
'......\nBecause I\'m connected.\n\0',

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
'It\'s time.\nLet\'s go.\n\0',

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
'Ahhh, great weather.\n\0',

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
'Harmonics test?\n\0',

# Maya Ibuki 
"そうよ。\nあなたも定期的に行う事に\nなるんだから。▽\n案内するわ。\nついて来てね。\n\0":
'???',

# Maya Ibuki 
"センパイ、シンジ君です。\n\0":
'Sempai, this is Shinji-kun.\n\0',

# Ritsuko Akagi 
"もうすぐ、\nレイのテストが終わるわ。▽\nシンジ君も、近々テストを\n行う予定よ。\n\0":
'???',

# Shinji Ikari
"その、テストって何ですか？\n\0":
'What is this test?\n\0',

# Ritsuko Akagi 
"ここであなた達は\nテストと訓練が行えるわ。▽\n一つは、ハーモニクステスト。▽\nエヴァとパイロットの\n神経接続における調和を調整し、\nΑΤを高めるテストよ。▽\nもう一つはシンクロ技能訓練。▽\nパイロットとエヴァの\n神経交流を高め、エヴァの\n運動性能を引き出すための訓練よ。▽\nここネルフに来た時に、テストを\nして欲しい時は、私かマヤに\n話し掛けてくれたらいいわ。\n\0":
'???',

# Maya Ibuki 
"学校のテストなんかよりは簡単よ。\nそういえば、学校はどう？\n\0":
'Much easier than the tests at school.\nSpeaking of, how is school?\n\0',

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
'Yes, of course.\n\0',

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
'Misato-san...!!\nAre you okay, Misato-san?!\n\0',

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
'Is the pilot of\nUnit-01 there?\n\0',

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
'Shinji-kun, you asked me\nsomething the other day.▽\nAbout why I joined Nerv...\n\0',

# Misato Katsuragi 
"私の父はね、自分の研究、\n夢に生きる人だったわ。▽\nそんな父を許せなかった。\n憎んでさえいたわ。\n\0":
'My father, he was someone who\nlived for his research and his dreams.▽\nI could never forgive him for that.\nI could only hate him.\n\0',

# Shinji Ikari
"……………。\n（僕の父さんと同じだ。）\n\0":
'.........\n(Just like my father.)\n\0',

# Misato Katsuragi 
"母や私、家族の事など\n全く構ってくれなかった。▽\n周りの人達は繊細な人だと\n言っていたわ。\n\0":
'He didn\'t give a damn about\nmy mom and me, or the family,\nor anything like that.▽\nPeople always said he was sensitive.\n\0',

# Misato Katsuragi 
"でも、ホントは心の弱い、\n現実から、私達家族という現実から\n逃げてばかりいた人だったのよ。▽\n子供みたいな人だったわ。▽\n母が父と別れた時も、\nすぐに賛成したわ。▽\n母はいつも泣いてばかりだったもの。▽\n父はショックだったみたいだけど、\nその時は自業自得だと笑ったわ。\n\0":
'But in truth he was just a weak\nperson running away from reality\n-- the reality of his family.▽\nHe was like a kid. ▽\n母が父と別れた時も、\nすぐに賛成したわ。▽\n母はいつも泣いてばかりだったもの。▽\n父はショックだったみたいだけど、\nその時は自業自得だと笑ったわ。\n\0',

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
'Understood.\nRei will handle the rest of the operation.\n\0',

# Gendo Ikari
"レイ、後は任せた。\n\0":
'Rei, I leave the rest to you.\n\0',

# Rei Ayanami 
"はい、碇司令。\n\0":
'Understood, Commander Ikari.\n\0',

# Kozo Fuyutsuki
"常に血で濡らされた\nロンギヌスの槍…。\n\0":
'The ever-bloodied\nSpear of Longinus...\n\0',

# Gendo Ikari
"神を殺し、\nまた神を生む力を持った槍…。\n事は我々のシナリオ通りだよ。\n\0":
'A spear with the power\nto both kill and birthe gods...\nThings are going according to our scenario.\n\0',

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
'An Angel has appeared above Tokyo-3!\n\0',

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
'What do you think,\nIkari-kun?\n\0',

# Gendo Ikari
"使徒は知恵をつけ始めています。\n残された時間は…。\n\0":
'The Angel are beginning to cultivate wisdom.\nThe time left to us is...\n\0',

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
'Yes. There is one child\nfor whom a core can\nbe prepared right away.\n\0',

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
'Hey, Shinji...\n\0',

# Shinji Ikari
"なに？\n\0":
'Yeah?\n\0',

# Toji Suzuhara 
"エヴァに初めて乗った時、\nどうやった？\n\0":
'What was it like,\nyour first time in an Eva?\n\0',

# Shinji Ikari
"何で、そんな事聞くの？\n\0":
'Why are you asking me something like that?\n\0',

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
'Nerv itself?\nCommander Ikari does?\n\0',

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
'Well... We\'ll talk when I get back.\n\0',

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
'Hmm, really?\nGood for you.\n\0',

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
'And there it is.\n\0',

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
'Oh no. What do we do?\n\0',

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
'The target...\nWhat you\'re calling an Angel...\nIt\'s an Eva, isn\'t it?!\n\0',

# Gendo Ikari
"あれはもう、\nエヴァ参号機ではない。\n…使徒だ。\n\0":
'That is no longer\nEva Unit-03.\nIt\'s an Angel.\n\0',

# Asuka Soryu Langley
"プラグが見える。\nパイロットはあの中なんだわ。\nまさか使徒に乗っ取られるなんてね。\n\0":
'I can see the plug.\nA pilot\'s on the inside.\nPretty crazy, getting hijacked by an Angel.\n\0',

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
'Eva Unit-02 has gone completely silent.\nTarget is moving toward Unit-00.\n\0',

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
'Unit-03\'s pilot...\nThe Fourth Child is...\n\0',

# Shinji Ikari
"…トウジ？\n\0":
'...Toji?\n\0',

# Misato Katsuragi 
"シンジ君。\n…シンジ君！\n\0":
'Shinji-kun.\nShinji-kun!\n\0',

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
'So you\'re running away again.\n\0',

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
'I...\nI decided I wouldn\'t pilot anymore.\n\0',

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
'That\'s right.▽\nIt\'s said that if an Angel makes contact\nwith Adam, the being asleep beneath H.Q.,\nhumanity will be completely obliterated.\n\0',

# Ryoji Kaji
"サードインパクトでね。\n\0":
'The Third Impact.\n\0',

# Ryoji Kaji
"それを阻止出来るのは、\n使徒と同じ力を持つ\nエヴァンゲリオンだけだ。\n\0":
'Only the Evangelions,\nwhich have power equal to the Angels,\nare capable of stopping it.\n\0',

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
'Not good!\nThe main shaft is completely exposed!\n\0',

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
'I...\nI\'m the pilot of Evangelion Unit-01, Shinji Ikari!▽\nLet me pilot the Eva, please!\n\0',

# Shinji Ikari
"お願いです！\n僕をエヴァに乗せてください！\n\0":
'I beg you!\nLet me pilot Eva Unit-01!\n\0',

# Gendo Ikari
"パイロットをエヴァに搭乗させる。\nエントリー準備、急げ。\n\0":
'The pilot may board the Eva.\nPrepare for immediate entry.\n\0',

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
'Ikari-kun, did you try to understand?\n\0',

# Shinji Ikari
"わかろうとした。\nわかろうとしたんだよ！！\n\0":
'I tried. I really tried!!\n\0',

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
'Ikari, do you plan to betray Seele?\n\0',

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
'What about Unit-00\'s A.T. Field?!\n\0',

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
'......go.\n\0',

# Asuka Soryu Langley
"動かない…。\n動かないのよ…。\n\0":
'Won\'t go...\nIt won\'t go...\n\0',

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
'The A.T. Field\'s inverting!\nIt\'s being eroded all at once!\n\0',

# Ritsuko Akagi 
"使徒を押さえ込むつもり？\n\0":
'She\'s trying to keep the Angel restrained?\n\0',

# Misato Katsuragi 
"レイ、機体は捨てて逃げて！\n\0":
'Rei, abandon the unit and escape!\n\0',

# Rei Ayanami 
"だめ。\n私がいなくなったら\nΑΤフィールドが消えてしまう。▽\nだから、だめ。\n\0":
'I can\'t leave.\nIf I\'m not here,\nthe A.T. Field will completely vanish.▽\nSo, I can\'t.\n\0',

# Misato Katsuragi 
"レイ、死ぬ気？\n\0":
'Rei, you\'re planning to die?\n\0',

#
# ./USRDIR/event/tev1801.har_EXTRACT/tev1801.evs
#
# Seele 06
"ついに、\n第１６の使徒までを倒した。\n\0":
'At last, we\'ve defeated up to the 16th Angel.\n\0',

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
'Aren\'t songs nice?\n\0',

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
'I\'m Kaworu. Kaworu Nagisa.\nA child who\'s part of the plan, like you.\nThe Fifth Child.\n\0',

# Shinji Ikari
"フィフス・チルドレン？\n君が？\nあの…渚、君。\n\0":
'The Fifth Child?\nYou?\n...I mean, Nagisa-kun.\n\0',

# Kaworu Nagisa 
"カヲルでいいよ。\n碇君。\n\0":
'Just call me "Kaworu",\nIkari-kun.\n\0',

# Shinji Ikari
"僕も、あの、\nシ、シンジでいいよ。\n\0":
'Um, me too.\nJust "Shinji" is okay.\n\0',

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
'Why am I here?\n\0',

# Rei Ayanami 
"私、何故また生きているの？\n\0":
'Why am I still alive?\n\0',

# Rei Ayanami 
"何のために？\n\0":
'To what ends?\n\0',

# Rei Ayanami 
"誰のために？\n\0":
'And for whom?\n\0',

# Rei Ayanami 
"フィフス・チルドレン。\nあのヒト、私と同じ感じがする。\n…どうして。\n\0":
'The Fifth Child.\nHe feels like me.\nWhy...?\n\0',

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
'Then who could it be?\n\0',

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
'It is different from Seele\'s scenario, but still.\n\0',

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
'... I understand.\nGive my regards to Yui-kun.\n\0',

# Misato Katsuragi 
"サードインパクトを\n起こすつもりなのよ。▽\n使徒ではなく、\nエヴァシリーズを使ってね。▽\n１５年前のセカンドインパクトは\n人間に仕組まれたものだったわ。\n\0":
'They plan on triggering\nthe Third Impact.▽\nUsing not the Angels,\nbut the Eva Series instead.▽\nSecond Impact, fifteen years ago,\nwas something plotted by humans.\n\0',

# Misato Katsuragi 
"けどそれは他の使徒が覚醒する前に\nアダムを卵へ還元する事で、被害を\n最小限に食い止める為だったのよ。▽\n私達人間もね、アダムと同じ\nリリスと呼ばれる生命体の源から\n生まれた１８番目の使徒なのよ。\n\0":
'But that was to minimize the damage\nby reverting Adam to an egg\nbefore the other Angels awakened.▽\nWe humans are the 18th Angel,\nborn from the one called Lilith,\na source of life like Adam.\n\0',

# Misato Katsuragi 
"他の使徒達は別の可能性だったの。\nヒトの形を捨てた人類の…。▽\nただ、お互いを拒絶するしか\nなかった悲しい存在だったけどね。\n同じ人間同士も。▽\nいい、シンジ君。\nエヴァシリーズを全て\n消滅させるのよ。▽\n生き残る手段はそれしかないしかないわ。\n\0":
'The other Angels were an alternate possibility.\nA humanity that abandoned human form...▽\nBut sadly, we couldn\'t help\nbut reject one another,\neven though we\'re all human.▽\nOkay, Shinji-kun?\nYou have to destroy the entire Eva Series.▽\nIt\'s the only way we\'ll survive.\n\0',

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

# Makoto Hyuga
"次元測定値が反転！\nマイナスを示しています。▽\n観測不能。\n数値化出来ません。\n\0":
'???',

# Kozo Fuyutsuki
"アンチΑΤフィールドか。\n\0":
'An Anti-A.T. Field.\n\0',

# Maya Ibuki 
"全ての現象が、\n１５年前と酷似してる。▽\nじゃあ、これって、\nやっぱりサードインパクトの\n前兆なの？\n\0":
'???',

# Kozo Fuyutsuki
"人類の生命の源たるリリスの卵、\n黒き月。▽\n今更、その殻の中へと\n還る事は望まぬ。\nだが、それもリリス次第か。\n\0":
'???',

# Gendo Ikari
"アダムとリリスの、\n禁じられた融合。\n\0":
'The forbidden fusion\nof Adam and Lilith.\n\0',

# Gendo Ikari
"欠けた心の補完。\n不要な身体を捨て、\n全ての魂を今、ひとつに。\n\0":
'???',

# Gendo Ikari
"そして、ユイのもとへ行こう。\n\0":
'And then, we\'ll go where Yui is.\n\0',

# Gendo Ikari
"始めよう、レイ。\nΑΤフィールドを、\n心の壁を解き放つのだ…。\n\0":
'Let\'s begin, Rei.\nRelease the wall of your heart,\nyour A.T. Field...\n\0',

# Gendo Ikari
"どうした、レイ。\n\0":
'What it is, Rei?\n\0',

# Rei Ayanami 
"私はあなたの人形じゃない。▽\n私はあなたじゃないもの。\n\0":
'I\'m not your doll.▽\nI am not you.\n\0',

# Gendo Ikari
"頼む！\n待ってくれレイ！！\n\0":
'Please!\nWait for me, Rei!!\n\0',

# Rei Ayanami 
"だめ。\n碇君が呼んでる。\n\0":
'I can\'t.\nIkari-kun is calling.\n\0',

# Rei Ayanami 
"闇の入り口、\nそして、闇の終り。\nそこは、私が帰る場所。▽\n…ただいま。\n\0":
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

# Keel Lorenz
"エヴァンゲリオン初号機\nパイロットの欠けた自我を持って\n人々の補完を。▽\n三度の報いの時が、今…。\n\0":
'???',

# Kozo Fuyutsuki
"使徒の持つ生命の実と、\nヒトの持つ知恵の実。\nその両方を手に入れた。▽\nそして今や、命の胎芽たる\n生命の樹へと還元している。\n\0":
'???',

# Kozo Fuyutsuki
"この先に、サードインパクトの\n無からヒトを救う箱舟となるか、\nヒトを滅ぼす悪魔となるのか。▽\n未来は碇の息子に委ねられたな。\n\0":
'???',

# Shigeru Aoba
"エヴァシリーズの\nΑΤフィールドが共鳴！\n\0":
'???',

# Makoto Hyuga
"更に、増幅しています！！\n\0":
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
"何を願うの？\n\0":
'What do you desire?\n\0',

# Shinji Ikari
"綾波？\nここは？\n\0":
'Ayanami?\nWhere are we?\n\0',

# Rei Ayanami 
"ここはＬＣＬの海。\n生命の源の海の中。\n\0":
'This is the Sea of L.C.L.\nThe place where life began.\n\0',

# Rei Ayanami 
"ΑΤフィールドを失った、\n自分の形を失った世界。▽\nどこまでが自分で、\nどこからが他人なのかわからない、\n曖昧な世界。\n\0":
'???',

# Rei Ayanami 
"どこまでも自分で、\nどこにも自分が居なくなってる\n脆弱な世界。\n\0":
'???',

# Shinji Ikari
"僕は死んだの？\n\0":
'Am I dead?\n\0',

# Rei Ayanami 
"いいえ、\n全てが一つになっているだけ。▽\nこれがあなたの望んだ世界、\nそのものよ。\n\0":
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

# Shinji Ikari, Misato Katsuragi 
"…ありがとう。\n\0":
'...Thank you.\n\0',

# Shinji Ikari
"あそこではイヤな事しか\nなかった気がする。▽\nだから、\nきっと逃げ出してもよかったんだ。\n\0":
'???',

# Shinji Ikari
"でも、逃げたところにも\nいい事はなかった。▽\nだって僕が居ないもの。\n誰も居ないのと同じだもの。\n\0":
'???',

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

# Kaworu Nagisa 
"現実は知らないところに。\n夢は現実の中に。\n\0":
'???',

# Rei Ayanami 
"そして、真実は心の中にある。\n\0":
'???',

# Kaworu Nagisa 
"ヒトの心が自分自身の形を\n造り出しているからね。\n\0":
'???',

# Rei Ayanami 
"そして、新たなイメージが\nそのヒトの心も形も変えていくわ。▽\nイメージが、想像する力が、\n自分達の未来を、\n時の流れを造り出しているもの。\n\0":
'???',

# Kaworu Nagisa 
"ただ、ヒトは自分自身の意思で\n動かなければ、何も変わらない。\n\0":
'???',

# Rei Ayanami 
"だから、見失った自分は、\n自分の力で取り戻すのよ。▽\n例え、自分の言葉を失っても。\n他人の言葉に取り込まれても。▽\n自らの心で\n自分自身をイメージ出来れば\n誰もがヒトの形に戻れるわ。\n\0":
'???',

# Yui Ikari
"心配ないわよ。▽\n全ての生命には\n復元しようとする力がある。\n生きていこうとする心がある。▽\n生きていこうとさえ思えば…、\nどこだって天国になるわ。\n\0":
'???',

# Yui Ikari
"だって、生きているんですもの。\n幸せになるチャンスは、\nどこにでもあるわ。▽\n太陽と、月と、地球がある限り、\n大丈夫…。\n\0":
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

# Shinji Ikari
"うん、母さん…。▽\nさよなら…、母さん…。\n\0":
'???',

# Asuka Soryu Langley
"…ぐ…ぐぐぅ…ぅ\n\0":
'???',

# Shinji Ikari
"う…、ううぅ、ううううぅ。\n\0":
'???',

# Asuka Soryu Langley
"気持ち悪い。\n\0":
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
'The $d Angel has appeared in the\nvicinity of Tokyo-3\'s $f area.\n\0',

# Shigeru Aoba, Male Staff
"目標を映像で確認。\n出ます！\n\0":
'Target has been visually verified.\nOn-screen!\n\0',

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
'Its particle cannon and A.T. Field are powerful.\nIn terms of offense and defense, it\'s the perfect floating fortress.\n\0',

# Kozo Fuyutsuki
"強力な加粒子砲とΑΤフィールド。\nまさに完璧な空中要塞だな。\n\0":
'Its particle cannon and A.T. Field are potent.\nTruly a consummate floating fortress.\n\0',

# Female Staff
"強力な加粒子砲とΑΤフィールド。\nまさに完璧な空中要塞ですね。\n\0":
'Its particle cannon and A.T. Field are powerful.\nIt certainly is a perfect floating fortress.\n\0',

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
# ./USRDIR/event/a003.har_EXTRACT/a003.evs
#
# [Angel: Israfel]
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
# ./USRDIR/event/a007.har_EXTRACT/a007.evs
#
# [Angel: Tabris]
#
# Kaworu Nagisa 
"さあ、行くよ。\nおいで、アダムの分身、\nそしてリリンのしもべ…。\n\0":
'Come along now. Let us go,\nAdam\'s dark shadow,\nservant of the Lilin...\n\0',

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
'Unit-02 has no\nentry plug inserted.\nIt\'s moving unmanned!\n\0',

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
'That\'s the Fifth Child...\n\0',

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
# ./USRDIR/event/n002.har_EXTRACT/n002.evs
#
# Misato Katsuragi, Female Staff
"ラミエル\n\0":
'Ramiel\n\0',

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
'The units that participated in this operation were...\n\0',

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
# ./USRDIR/event/n007.har_EXTRACT/n007.evs
#
# Misato Katsuragi, Female Staff
"セントラルドグマに突如出現した使徒の正体は、\n\0":
'An Angel that appeared suddenly in Central Dogma\n\0',

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
'Sandalphon\n\0',

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
# ./USRDIR/event/n011.har_EXTRACT/n011.evs
#
# Misato Katsuragi, Female Staff
"レリエル\n\0":
'Leliel\n\0',

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
'Unit-01 disappears.\n\0',

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
# ./USRDIR/event/n012.har_EXTRACT/n012.evs
#
# Misato Katsuragi, Female Staff
"これより戦闘結果報告を行います。\n\0":
'I will now provide the battle outcome report.\n\0',

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
'Arael\n\0',

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
# ./USRDIR/event/n013.har_EXTRACT/n013.evs
#
# Misato Katsuragi 
"全プログラムを消去する作戦を実行します。\n\0":
'???',

# Misato Katsuragi 
"しかし、ΘΑは自動停止しました\n\0":
'However, J.A. automatically shut down.\n\0',

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
'A shadow...?!\nThis is...!\n\0',

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
'Uhhh...\nI\'m sinking, all the way...\nI can\'t get loose.....\n\0',

# Rei Ayanami 
"影が…！？\n\0":
'A shadow...?!\n\0',

# Male Staff
"影から離れてください！\n危険です！\n\0":
'???',

# Misato Katsuragi 
"影から離れて！！\n逃げてッ！！\n\0":
'Get away from the shadow!\nRun!!\n\0',

# Makoto Hyuga, Female Staff
"パターン青！\n初号機の真下ですっ！\n\0":
'Pattern blue!\nDirectly under Unit-01!\n\0',

# Makoto Hyuga, Female Staff
"パターン青！\n弐号機の真下ですっ！\n\0":
'Pattern blue!\nDirectly under Unit-02!\n\0',

# Shinji Ikari
"か…、影が？\n何だよこれ！？\nおかしいよ…！\n\0":
'A sh-shadow?\nWhat is this?!\nIt\'s weird!\n\0',

# Makoto Hyuga, Female Staff
"パターン青！\n零号機の真下ですっ！\n\0":
'Pattern blue!\nDirectly under Unit-00!\n\0',

# Makoto Hyuga, Female Staff
"パターン青！\n参号機の真下ですっ！\n\0":
'Pattern blue!\nDirectly under Unit-03!\n\0',

# Asuka Soryu Langley
"やだ…！！\n沈む、沈んじゃう！！\n誰か！　どうにか出来ないの…。\n\0":
'???',

# Makoto Hyuga, Female Staff
"パターン青！\n四号機の真下ですっ！\n\0":
'Pattern blue!\nDirectly under Unit-04!\n\0',

# Kaworu Nagisa 
"くっ…、しまった。\n捕らえられたか………。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le003.evs
#
# Shinji Ikari
"ここは、どこなんだろう。▽\n外は真っ白だし。\nレーダー電波やソナーは\n返ってこない。▽\n空間が広すぎるんだ。\n\0":
'???',

# Shinji Ikari
"システムを\n生命維持モードに切り替えてから、\nもう１２時間。▽\n僕の命も、あと４、５時間か。\n\0":
'???',

# Asuka Soryu Langley
"どうなってるの？▽\n一体何をされたって言うの！？\nレーダー電波もソナーも\n役に立ちゃあしない。\n\0":
'???',

# Asuka Soryu Langley
"…このまま救助が来なかったら。\n生命維持モードにしても、\n限界はあと４、５時間の命…。\n\0":
'???',

# Asuka Soryu Langley
"ヤダ…。\nこんな終わり方って\n絶対にヤダ！！\n\0":
'???',

# Rei Ayanami 
"レーダー電波もソナーも\n反応がない。\n\0":
'No response from\nradar waves or sonar.\n\0',

# Rei Ayanami 
"生命維持モードは、\nあと４、５時間は持ちそう。\n\0":
'Life support mode will last about\nfour or five more hours.\n\0',

# Rei Ayanami 
"静かだわ。\n静か過ぎて耳が痛いくらい…。\n\0":
'It\'s quiet.\nSo quiet it hurts my ears...\n\0',

# Toji Suzuhara 
"出せコラー！！\nワレ、出さんかい！！\nこン野郎〜…！！▽\nどうなっとんねん、\nどこやねんここ？▽\n外は何の反応もないし…。\nワシ、一人なんか！？\n\0":
'Gimme a picture, come on!!\nWhy won\'t you show me anything?!\nPiece of shit...!!▽\nWhat\'s going on?\nWhere am I?▽\nI\'m not getting any kind of readings from outside...\nThat means... I\'m all alone?!\n\0',

# Toji Suzuhara 
"…どんだけ、時間過ぎてんねやろ。\nここで、死ぬんか…ワシ。\n\0":
'...Man. How long\'ve I been here?\nAm I gonna die here?\n\0',

# Toji Suzuhara 
"……………チッ。▽\n今日、ナイターあるんやった。\n\0":
'......Crap.▽\nI\'ve got a game tonight.\n\0',

# Kaworu Nagisa 
"恐らくここは、負のエネルギー空間。\nレーダー電波もソナーも\nここじゃ役に立たないな。\n\0":
'???',

# Kaworu Nagisa 
"生命維持モードは、\nよくて５時間…。\n\0":
'???',

# Kaworu Nagisa 
"計画の狂いは、\nここまで及ぶ…か。\n\0":
'???',

# Misato Katsuragi 
"じゃあ、あの影の部分が\n使徒の本体なわけ？\n\0":
'???',

# Makoto Hyuga
"では、あの影の部分が\n使徒の本体だと…？\n\0":
'So, that shadow section is\nthe Angel\'s real body?\n\0',

# Male Staff
"あの影の部分が…使徒ですか？\n\0":
'That shadow section... is the Angel?\n\0',

# Ritsuko Akagi 
"直径６８０メートル、\n厚さ約３ナノメートルのね。▽\nその極薄の空間を、内向きの\nΑΤフィールドで支え、内部は\nディラックの海と呼ばれる虚数空間。▽\n…多分、別の宇宙に\n繋がっているんじゃないかしら？\n\0":
'???',

# Maya Ibuki, Female Staff
"直径６８０メートル、\n厚さ約３ナノメートル。▽\nその極薄の空間を、内向きの\nΑΤフィールドで支え、内部は\nディラックの海と呼ばれる虚数空間。▽\n…恐らく、別の宇宙に\n繋がっているものと思われます。\n\0":
'???',

# Misato Katsuragi, Makoto Hyuga
"あの球体みたいなものは？\n\0":
'???',

# Male Staff
"質問です。\nあの球体みたいなものは？\n\0":
'???',

# Ritsuko Akagi 
"本体の虚数回路が閉じれば\n消えてしまう。\n上空の物体こそ影にすぎないわ。\n\0":
'???',

# Maya Ibuki, Female Staff
"本体の虚数回路が閉じれば\n消えてしまいます。▽\n上空の物体が、\n影という事になりますね。\n\0":
'???',

# Misato Katsuragi, Makoto Hyuga, Male Staff
"エヴァを取り込んだ、\n黒い影が目標か。\n\0":
'So the black shadow that absorbed\nthe Eva is our target.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le004.evs
#
# Shinji's Shadow [Leliel]
"気分はどう？\n\0":
'How do you feel?\n\0',

# Shinji Ikari, Rei Ayanami
"…誰？\n\0":
'...Who\'s there?\n\0',

# Shinji's Shadow [Leliel], Kozo Fuyutsuki
"碇シンジ。\n\0":
'Shinji Ikari.\n\0',

# Shinji Ikari
"それは、僕だ。\n\0":
'That\'s me.\n\0',

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
'That\'s right.\nIt\'s also you.\nAsuka Soryu Langley.▽\nThe Asuka in you.\nThe Asuka in everyone.\nThat\'s me.▽\nDeep down inside, you\'re always crying.\n\0',

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
'Yes. Something others call Rei Ayanami.\nAn object with a fabricated body and a false soul,\nmerely pretending to be human.\n\0',

# Rei Ayanami 
"それが私…。\nあなたは本当の私…。\nいつも私を見つめている私？\n\0":
'That is me...\nYou are the real me...\nThe me that always gazes upon myself?\n\0',

# Rei's Shadow [Leliel]
"あなたの暗くて見えない心を\n私は知りたい…。▽\nあなたは、一体\n何のために生きているの？\n\0":
'You wish to know your own heart,\nhidden in darkness...▽\nFor what possible reason\ndo you exist?\n\0',

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
'Hahah...\n\0',

# Kaworu Nagisa 
"これは…？\n\0":
'Is that...?\n\0',

# Kaworu's Shadow [Leliel]
"僕がわかるかい？\n\0":
'Do you know me?\n\0',

# Kaworu Nagisa 
"…己の内面。\n弱い部分と向き合うなんて、\n未熟なリリンどもの風習だね…。\n\0":
'My inner self.\nConfronting one\'s own weakness,\n\'tis a custom of the fledgeling Lilin...\n\0',

# Kaworu's Shadow [Leliel]
# Second sentence's translation too liberal, fix. -Reichu
"その未熟なリリンの物真似が\n上手になったね。\n内面の弱さまで再現してるんだから。\n\0":
'Oh, but you\'ve grown adept at mimicking those fledgeling Lilin.\nThus, parts of yourself as deeply buried as your inner weakness are returning.\n\0',

# Kaworu Nagisa 
"………。\n一体、何しに現れたの？\n\0":
'......\nWhat could you possibly have shown up to do?\n\0',

# Kaworu's Shadow [Leliel]
"フフ…。\n確認だよ。\n本来の目的を忘れてはいないかい？\n\0":
'Haha...\nSo it\'s true.\nYou haven\'t totally forgotten your original purpose, have you?\n\0',

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
'...So, ultimately,\nwhy do you exist?\n\0',

# Toji's Shadow [Leliel]
"なあやっぱり、\n自分を演じていくのんって\nしんどいやろ？\n\0":
'???',

# Kaworu's Shadow [Leliel]
"繰り返すよ。\n本来の目的を忘れてはいないかい？\n\0":
'I\'ll say it again.\nHave you completely forgotten your original purpose?\n\0',

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
# ./USRDIR/event/levent.har_EXTRACT/le009.evs
#
# Shinji Ikari
"ミサトさん？\nミサトさん！？\nミサトさ………………。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le102.evs
#
# Shinji Ikari
"嫌われるのは嫌だよ。\n誰だってそうじゃないか。\n君だって、嫌われたくは無いだろ！？\n\0":
'???',

# Shinji's Shadow [Leliel]
"嫌われる原因と結果は、\n君が生み出すんだよ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le104.evs
#
# Shinji Ikari
"僕ばっかりが悪くは無い。\n悪くなくても、\n嫌われる時はあるんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"そうやって、\n他人と距離をおこうとしている。\n楽だからね、傷つかなくていいから。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le106.evs
#
# Shinji Ikari
"誰だってそうだ。\n楽しい思い出を大事にして\n生きてるはずだよ。▽\nそれさえあれば、\n生きていけるんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"でも、思い出はそこで終わり。\n同じ思い出ばかりを繋いで、\n何も変われない生き方を歩むのか？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le107.evs
#
# Shinji Ikari
"ムリに足掻こうとするから\n苦しいんだ。▽\n諦めれば、楽になる。\n諦めは…、\n人が生きていくのに必要な事だよ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"でも、君の中に抱えている\n後悔は隠せないよ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le109.evs
#
# Shinji Ikari
"それは、違う。▽\n嫌われるのは怖いけど、\nだからといって、\n一人になるのは違うと思う。\n\0":
'???',

# Shinji's Shadow [Leliel]
"そうやって、ほのかな期待を\n積み上げて生きていくんだ。\n\0":
'???',

# Shinji Ikari
"いつかはきっと、\n楽しい時が来るかもしれないから。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le111.evs
#
# Shinji Ikari
"いい事なんか無いよ。\nこれ以上嫌われない為に\n何もしない方がいいんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"嫌われないかわりに、\n皆から忘れ去られても？\n自分の存在がなくなっても？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le112.evs
#
# Shinji Ikari
"変化なんて要らない。▽\nせっかく居心地がいい\n場所を見つけても、\n変化がそれを奪うんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"その後にやってくる\n新しい世界を知るには、\n痛みを伴うものなんだよ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le113.evs
#
# Shinji Ikari
"変化は望まなくてもやってくる。\nエヴァに乗る事だってそうだ。\n僕が望んだ変化じゃない。▽\nでも、悪くは無い変化もあった…。▽\n思い出が尽きる事は無いよ。\nもちろん、\nいい事ばかりじゃないけど。\n\0":
'???',

# Shinji's Shadow [Leliel]
"惰性だね。\n痛みを知る覚悟が無いだけなんだ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le115.evs
#
# Shinji Ikari
"そんな事、思い出させないでよ！\n何で僕を傷つけるんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"今まで君が押し込めていた\n痛み苦しみ、それが僕さ。▽\nでも、僕は君と会う必要が\nあったんだ。\n\0":
'???',

# Shinji Ikari
"どうして…、そんな…？\n\0":
'???',

# Shinji's Shadow [Leliel]
"僕と向き合う準備を\nしないといけない。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le117.evs
#
# Shinji Ikari
"そんな…、嫌だよ！\n心を覗かれるなんて。\n\0":
'???',

# Shinji's Shadow [Leliel]
"心の中を知られると、\n嫌われるかもしれない。\nそういう思いが君の中にあるわけだ。▽\n他人が自分を傷つけるとばかり\n思ってるけど、どうかな？▽\n自分もまた、他人を傷つける事に\nなるかもしれないんだ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le119.evs
#
# Shinji Ikari
"僕は誰も傷つけてない。\n何も言っていない。\n\0":
'???',

# Shinji's Shadow [Leliel]
"そうやって、\n他人と距離をおこうとしてる。▽\nまず、それで誰かを傷つけている。\n自分自身もね。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le121.evs
#
# Shinji Ikari
"みんな心を隠しすぎるんだ。\nお互いを理解したくないんだよ。▽\n心を隠しているうちは、\n打ち解けるわけが無いんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"自分自身が心を隠しておきながら、\nどうしてそんな事が言えるんだ？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le122.evs
#
# Shinji Ikari
"付け入る隙を狙ってるんだ。\nみんな、優しくするふりをして、\n傷つけようと構えてるんだ。▽\nそんな事なら、お互いの心の中が\n見えていた方がいい。\n\0":
'???',

# Shinji's Shadow [Leliel]
"傷つけるのは\n他人ばかりじゃないよ。▽\n他人の顔色をうかがって、\n隙を見つけようとしてるのは\n君の方だ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le123.evs
#
# Shinji Ikari
"僕が傷つくのは、\n自分自身のせいなのか…。\n\0":
'???',

# Shinji's Shadow [Leliel]
"痛みを感じる自由も\nあるという事だ。\n\0":
'???',

# Shinji Ikari
"よくわからない。\n痛みなんて、要らないのに。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le124.evs
#
# Shinji Ikari
"違う。\n僕が傷つくのは他人のせいだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"じゃあ、幸せになる事も全て\n他人任せにするのかい？\n\0":
'???',

# Shinji Ikari
"僕は…、\nそんなに自由じゃないんだ。\n色んなしがらみが多すぎるんだ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le125.evs
#
# Shinji Ikari
"でも、他人が怖くても、\n人に嫌われるのが怖くても、\n人を好きにはなりたいんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"幻想の中にいては、\n祈りも願いも意味のないものだよ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le126.evs
#
# Shinji Ikari
"だから、他人といるのが怖いんだ▽\n嫌われるかもしれないって、\nそればかりに怯えないと\nいけないから。\n\0":
'???',

# Shinji's Shadow [Leliel]
"孤独でいるのが居心地がいい？\nそのくせ、他人の事ばかり\n気にしてる。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le127.evs
#
# Shinji Ikari
"だから、きっかけを待ってる。\nお互い、理解しあえる瞬間を。\n\0":
'???',

# Shinji's Shadow [Leliel]
"自分からは何もしない。\nそれは、理解するという事を\n既に放棄してるよ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le129.evs
#
# Shinji Ikari
"僕は、そんな事していない。\n\0":
'???',

# Shinji's Shadow [Leliel]
"いいや、そうだね。\n自分が傷つかない為に、\n必死なんだろう。▽\n相手を不快にさせない為に。\n嫌われないように。▽\nでも結果、その行為が\n他人に嫌な思いをさせてるんだ。▽\n自分がなくなるよ、\nそんな事ばかりしていると。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le131.evs
#
# Shinji Ikari
"他人の事なんか、\nどうだっていいよ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"傷つく事を避けたいからだろ？\n他人に興味ないフリを\nしているだけさ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le133.evs
#
# Shinji Ikari
"自分の事だけで精一杯なんだ。\n他人の事まで考えている\n余裕なんかないよ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"他人は、自分を映し出す\n鏡だからね。▽\n少なからず、他人を意識せずには\nいられないものだよ。▽\nだから、君は僕を無視する事は\n出来ない。\n\0":
'???',

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
# ./USRDIR/event/levent.har_EXTRACT/le135.evs
#
# Shinji Ikari
"僕は変われるの？\n\0":
'???',

# Shinji's Shadow [Leliel]
"人は変わろうと思った瞬間から、\n変わり始める。\n良い方にも、悪い方にも。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le137.evs
#
# Shinji Ikari
"君は僕自身なんだろう？\nどうして思ってもない事を言うのさ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"僕が言うのは、\nいつも君が思っている事。▽\n君は、僕を、自分自身を\n信頼出来ないから、\nあえて欠如させたんだ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le140.evs
#
# Shinji Ikari
"僕は、変わりたいと思う。\nでも…。\n\0":
'???',

# Shinji's Shadow [Leliel]
"自分がどんな存在でいたいのかが\nわからないだけなんだ。\n\0":
'???',

# Shinji Ikari
"変わった先の自分は、\nみんなに好かれる自分かどうか、\nわからないから。\n\0":
'???',

# Shinji's Shadow [Leliel]
"周りが期待している自分になる\n必要はない。▽\nそれは変化じゃない。\n服従、依存だよ。▽\n居場所を確保しようと\nしているだけだ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le142.evs
#
# Shinji Ikari
"じゃあ、何で僕を傷つけるんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"僕は君にとっての真実だ。▽\n君は自分に正直でないから、\n否定的に捉えてるだけだよ。\n他人の中の僕も、君の中の僕も。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le144.evs
#
# Shinji Ikari
"君なんて必要ない。\n必要ないから、忘れられたんだ。\n\0":
'???',

# Shinji's Shadow [Leliel]
"でも、今こうして君と\n向かい合ってる。\n君が必要としたからだよ。\n\0":
'???',

# Shinji Ikari
"僕が…？\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le201.evs
#
# Asuka Soryu Langley
"私は、一人で生きるの。\nずっとそう決めてきたの。\nそんな弱音は吐かないわ。\n\0":
'???',

# Asuka's Shadow [Leliel]
"でも、誰かを思わずには\nいられない。▽\nママにしか呼びかけられない事を、\n寂しく思ってるんでしょう。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le203.evs
#
# Asuka Soryu Langley
"ママ以外、誰も要らない。\n\0":
'???',

# Asuka's Shadow [Leliel]
"ママだけを拠り所に一生、\n生きていくの？▽\nあなたを人形にしたママを？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le204.evs
#
# Asuka Soryu Langley
"逃げてなんかないわよ！\n\0":
'???',

# Asuka's Shadow [Leliel]
"その逃げた先から、\nいつか、自分のすごさをわかって\nくれると、人から求めてもらおうと。▽\n振り返りながら、\n誰かを待ってるのよ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le206.evs
#
# Asuka Soryu Langley
"私は人形じゃない！\n\0":
'???',

# Asuka's Shadow [Leliel]
"人形としての生き方を\n選ばなかった代わりに、\n孤独を選んだのね。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le208.evs
#
# Asuka Soryu Langley
"一人でいるのが怖いの。\n認められる為に、\nエリートになったのに。\n\0":
'???',

# Asuka's Shadow [Leliel]
"ますます虚勢を張るだけしか\n出来なくなったのよね。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le209.evs
#
# Asuka Soryu Langley
"寂しいのは\n私のせいだっていうの…？\n\0":
'You\'re saying it\'s my\nfault I\'m lonely...?\n\0',

# Asuka's Shadow [Leliel]
"あなたは\n人を遠ざけるために努力した。\n大学を出た、エヴァに乗った…。▽\nそう、\nすべてあなたの努力の成果なのよ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le211.evs
#
# Asuka Soryu Langley
"私は認められたかっただけ…。\nこんなの望んでいなかった…。\n\0":
'???',

# Asuka's Shadow [Leliel]
"あなたが認めさせたかった相手は\nもういないのよ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le214.evs
#
# Asuka Soryu Langley
"イヤよ…、一人で苦しむのは嫌…。\nどうすれば\n他人に気が付いてもらえるの？\n\0":
'???',

# Asuka's Shadow [Leliel]
"すべてを捨ててしまえば、\n哀れんでもらえる…。▽\nでもあなたは\n何も手放したくないのでしょ？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le215.evs
#
# Asuka Soryu Langley
"誰も…、\n私を守ってくれないの？\n\0":
'There\'s no one\nprotecting me?\n\0',

# Asuka's Shadow [Leliel]
"遠ざけるから。\n自分も、他人も。\nだから、本音は誰にも届かない。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le217.evs
#
# Asuka Soryu Langley
"こんなに苦しんでいるのに…。\n他人って冷たいのね…。\n\0":
'???',

# Asuka's Shadow [Leliel]
"みんなその冷たさに耐えているのよ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le219.evs
#
# Asuka Soryu Langley
"私が苦しんでいるみたいに、\n他の人も苦しんでいるの？\nそんなハズはないわ。\n\0":
'???',

# Asuka's Shadow [Leliel]
"他人の苦しみを知りたくないから\n距離を取ったのでしょう？▽\n知ってしまえば優しくしてしまう。\n偉そうにできなくなってしまう…。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le221.evs
#
# Asuka Soryu Langley
"私は違うわ…。\nだって私は他の人と違うんだもの…。\n\0":
'???',

# Asuka's Shadow [Leliel]
"孤独に凍えているあなたを知ったら、\n誰もそうは思わないでしょうね。\nやはり誰も近づけない方がいいわ。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le301.evs
#
# Rei Ayanami 
"わからない…。\n心は自分で見えないから。\n\0":
'I don\'t know...\nMy heart is hidden to me.\n\0',

# Rei's Shadow [Leliel]
"あなたは利用されているだけ。\n本当は誰にも必要とされていない。\n\0":
'You are only being used.\nThe truth is, nobody needs you.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le302.evs
#
# Rei Ayanami 
"私、自分がわからない。\n\0":
'I don\'t know myself.\n\0',

# Rei's Shadow [Leliel]
"自分という存在に興味が無いのね。\n生きる事を放棄している。\n\0":
'You\'re not interested in your own existence.\nYou\'ve given up on the act of living.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le303.evs
#
# Rei Ayanami 
"私には、果たすべき役割がある。\n\0":
'I have duties that I must carry out.\n\0',

# Rei's Shadow [Leliel]
"果たし終わったら、残るものは何？\n\0":
'And when you\'ve finished them, what will you have left?\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le304.evs
#
# Rei Ayanami 
"ちがう…。\n自分がわからないのは…。\n\0":
'No...\nIt\'s not that I don\'t understand myself...\n\0',

# Rei's Shadow [Leliel]
"空っぽだから。\n何も無いから見えない。\n理解しようがない。▽\nでもそれは…。\nあなたが目を背けているから。▽\n本当は心の奥底に持っている自分を\n見ないようにしているだけ。\n\0":
'It\'s because you\'re empty.\nThere\'s nothing inside -to- see.\nNo point in understanding it.▽\nBut there\'s a reason...\nYou\'re averting your eyes.▽\nIn truth, you\'re doing it solely so you don\'t see\nthe you that\'s in the depths of your heart.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le305.evs
#
# Rei's Shadow [Leliel]
"自分が無価値である事に\n気が付きたくないだけ…。\n\0":
'You just don\'t want to realize\nthat you\'re worthless...\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le306.evs
#
# Rei Ayanami 
"また次の役目があるわ。\n私にしかできない事が…。\n\0":
'There are still the duties to come.\nThings that only I can do. But...\n\0',

# Rei's Shadow [Leliel]
"そんな形でしか、\nあなたは他人に関われないのね…。\n\0":
'It\'s only with a form like that\nthat you can be affected by others...\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le307.evs
#
# Rei Ayanami 
"果たした役割はデータとして残る。\n\0":
'I will leave behind the duties I\'ve performed as data.\n\0',

# Rei's Shadow [Leliel]
# Reference to spreadsheets added to make translation less stiff. Too unintentionally funny? -Reichu
"ただの数値の羅列が残るだけ。\n人の想いに関わる事はできない。\n\0":
'Mere numbers in a spreadsheet.\nYou won\'t linger in anyone\'s thoughts.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le308.evs
#
# Rei Ayanami 
"目的なんて無くても\n生きていけるわ。\n\0":
'I\'m capable of living without\nsomething like a purpose.\n\0',

# Rei's Shadow [Leliel]
"それでは生きているとは言えない。\n存在しないと同じ。\n\0":
'If so, you can\'t really call that living.\nYou may as well not exist.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le309.evs
#
# Rei Ayanami 
"それでいい、それで構わない。\n私が生き、ここにいる。\n\0":
'That\'s fine. I see no problem with that.\nI am here, living.\n\0',

# Rei's Shadow [Leliel]
"ただ生きていたいだけなら、\n危険なパイロットを\n辞めなければならない。\n\0":
'If being alive is really all you want,\nyou should stop piloting.\nIt\'s dangerous.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le310.evs
#
# Rei Ayanami 
"でも変わると思う。\nそのために私は戦っている。\nエヴァに乗っている。\n\0":
'But I think I will change.\nThat\'s why I\'m fighting.\nWhy I pilot the Eva.\n\0',

# Rei's Shadow [Leliel]
"使徒をすべて倒した後の事を\n言っているのね。\nそんな事、あなたにできると思う？\n\0":
'You\'re talking about after\nall the Angels are defeated.\nYou think you\'re capable of something like that?\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le311.evs
#
# Rei Ayanami 
"それは私の役目。\n\0":
'It\'s my duty.\n\0',

# Rei's Shadow [Leliel]
"報われない仕事ね…。\nこれまで誰もあなたの辛さを\n理解しなかった。\n\0":
'Work without reward, is it...?\nSo far nobody\'s appreciated your hardships.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le312.evs
#
# Rei Ayanami 
"私はエヴァに乗る。\n\0":
'I pilot the Eva.\n\0',

# Rei's Shadow [Leliel]
"あなたの存在意義は\nそこにしかないもの。\n依存しているのね。\n\0":
'That\'s the only thing that gives meaning to your existence.\nYou depend on it.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le313.evs
#
# Rei Ayanami 
"エヴァは人類の希望よ。\n滅亡するわけにはいかない。\n\0":
'Evas are the hope of humanity.\nWe can\'t let ourselves be wiped out.\n\0',

# Rei's Shadow [Leliel]
# [NOTE] First sentence is certainly wrong. -Reichu
"そう吹き込まれて、\n誰かに利用されているのかも…。\nあなたの希望ではないのでしょう？\n\0":
'Spouting propaganda like that,\ncould be someone is using you...\nYou don\'t have any hope of your own, am I right?\n\0'

#
# ./USRDIR/event/levent.har_EXTRACT/le314.evs
#
# Rei Ayanami 
"私一人の力じゃ無理…。\n\0":
'It\'s beyond the power of me alone...\n\0',

# Rei's Shadow [Leliel]
"自分一人では、\n変化も期待できないのね。\n\0":
'You alone lack\nthe potential to change.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le315.evs
#
# Rei Ayanami 
"私は、私だけの体じゃない…。\n私は絆によってこの形になったの。\n\0":
'My body isn\'t mine alone...\nI assumed this form through the bonds I share.\n\0',

# Rei's Shadow [Leliel]
# [NOTE] Not sure about this. -Reichu
"でも中身までは作られなかった。\n\0":
'But you\'ve created none with any substance.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le316.evs
#
# Rei Ayanami 
"それでも私はエヴァに乗っている。▽\n絆のために、\n人と人の結びつきのために、\n私は戦っている。\n\0":
'Even so, I pilot the Eva.▽\nFor the bonds I share,\nfor the connections between people --\nthat\'s why I fight.\n\0 ',

# Rei's Shadow [Leliel]
"エヴァで得たものは\nいずれ消え失せるわ。\n絆も消え失せる。\n\0":
'What you\'ve gained with the Eva\nwill vanish sooner or later.\nThat includes your bonds.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le317.evs
#
# Rei Ayanami 
"あるわ。\n私はここにいる。\n想いもここにあるもの。\n\0":
'They exist.\nI\'m here.\nBecause my feelings, too, exist here.\n\0',

# Rei's Shadow [Leliel]
# [NOTE] Come back to trouble sentence later. -Reichu
"想いは移ろいやすいものよ。\nそんなものを根拠にするの？\n相手の気持ちも変わっていく。\n\0":
'Feelings tend to fade with time.\nそんなものを根拠にするの？\nYour companions\' feelings are changing too.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le318.evs
#
# Rei Ayanami 
"私がいた、という記憶は残る。\nみんな、私を忘れない。\n\0":
'Memories of my existence will remain with them.\nThe others won\'t forget me.\n\0',

# Rei's Shadow [Leliel]
"思い上がりね。\nあなたは誰の記憶にも留まらない。\nただいなくなるだけ。\n\0":
'You\'re too sure of yourself.\nYou won\'t linger in anyone\'s memory.\nMerely fade away, nothing more.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le319.evs
#
# Rei Ayanami 
"消えたりしない。\n永遠に結びつく。\n\0":
'I won\'t disappear or anything.\nI\'m forever connected.\n\0',

# Rei's Shadow [Leliel]
"一つになりたいのね。\nその人と結びつくのが\nあなたの本当の目的なの？\n\0":
'So you want to become as one.\nBeing joined with these people\nis your true goal, isn\'t it?\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le320.evs
#
# Rei Ayanami 
"結ばれた絆は変わらない。\n\0":
'The ties that bind me won\'t change.\n\0',

# Rei's Shadow [Leliel]
"変わらない…。\nあなたはそう思い込みたいだけ。\n\0":
'"Won\'t change"...\nYou just WANT to believe that.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le321.evs
#
# Rei Ayanami 
"それでもいい…。それでも…。\n\0":
'That is still fine... And yet...\n\0',

# Rei's Shadow [Leliel]
"想いは流れていく。\n記憶は薄れていく。▽\nそのすべてにあなたは抗わない。\nそれでは人の心に残れない。\n\0":
'Feelings wash away.\nMemories grow dimmer.▽\nYou can\'t fight all of that.\nThat\'s why you won\'t last within people\'s hearts.\n\0',

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
# ./USRDIR/event/levent.har_EXTRACT/le402.evs
#
# Toji Suzuhara 
"アホか！\n素じゃ！\n素中の素やっちゅうねん。\n\0":
'???',

# Toji's Shadow [Leliel]
"大声出さんでええって。\n\0":
'???',

# Toji Suzuhara 
"素じゃ…。\n素中の素やっちゅうねん…。\n\0":
'???',

# Toji's Shadow [Leliel]
"二回言わんでええねん！\n大声出さんと全然説得力無いやんか。\nそんなん虚勢張ってる証拠や。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le404.evs
#
# Toji Suzuhara 
"イキって何が悪いねん。\n虚勢張るんのどこがアカンねんな！\n\0":
'???',

# Toji's Shadow [Leliel]
"ほな、\nイキってたんは認めんねんな？▽\n自分が、\n小さい弱い人間やっちゅうのも\n認めたんや。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le405.evs
#
# Toji Suzuhara 
"ちゃうわ！\nワシがそんなんいちいち考えながら\n人と接してるワケないやろ！\n\0":
'???',

# Toji's Shadow [Leliel]
"強情やのぉ。\nまあ、そういう演出なんやろ？\n名演技や、ホンマ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le407.evs
#
# Toji Suzuhara 
"ちゃうわい！\nワシはそんな見栄っぱりやない。\n\0":
'???',

# Toji's Shadow [Leliel]
"せやけど、\nオマエそないに運動得意ちゃうやん。▽\nせやのにジャージ着こんでからに…。\nそれがハッタリやっちゅうとうねん。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le409.evs
#
# Toji Suzuhara 
"それがどないしてん？\nなんか文句あるんか？\n\0":
'???',

# Toji's Shadow [Leliel]
"嘘の自分で接してるって事は、や。\nその人を騙してるんと同じ事やな。\n…なんも思わへんの？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le410.evs
#
# Toji Suzuhara 
"ア、アカンかな？\n悪い事…かもしれん…。\n\0":
'???',

# Toji's Shadow [Leliel]
"まあ、そんなん誰でもしてる事や。\nオマエも同じように\n嘘の他人と接してんねんて。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le411.evs
#
# Toji Suzuhara 
"な〜んとも思わへんわ。\n悪い事してるワケやないしな。\n\0":
'???',

# Toji's Shadow [Leliel]
"そりゃそうや。\n演じてるんは皆一緒や。▽\nせやからオマエの嘘なんか\nだ〜れも気にせぇへんねんて。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le413.evs
#
# Toji Suzuhara 
"ワシは…、嘘つきなんかもしれん…。\n\0":
'???',

# Toji's Shadow [Leliel]
"自分の弱さを認めてんな？\nけど、今さら作ったイメージは\n脱がれへん。▽\nオマエは、そのジャージをずっと\n着続けんといかんねや。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le415.evs
#
# Toji Suzuhara 
"そうやなぁ、\nちょっとしんどい時もあるなぁ。\n\0":
'???',

# Toji's Shadow [Leliel]
"せやろ？\nもう止めてもええんちゃうか？\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le417.evs
#
# Toji Suzuhara 
"はぁ…。\nせやなぁ、もうかったるいわ。\n\0":
'???',

# Toji's Shadow [Leliel]
"せっかく着込んだ\n今までのイメージ捨てんとあかんな。▽\nけど今さら、\nそのジャージ脱げるんか？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le418.evs
#
# Toji Suzuhara 
"ワシはワシや。▽\nジャージ着ようが、\nレオタード来ようが、\nワシは何も変わらへん。\n\0":
'???',

# Toji's Shadow [Leliel]
"周りはドギモ抜かれるやろな…。▽\nいや、案外周りに影響力無くて、\n全然無視される可能性もあるな…。\nなんか寒いでぇ、それ…。\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le419.evs
#
# Toji Suzuhara 
"そんなん知らんわ。\n大体評判っちゅうんは\n他人が決めるもんや。\n\0":
'???',

# Toji's Shadow [Leliel]
"他人に判断をおもねるんは\n楽やもんな。\nでもそれってただの責任逃れやで？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le420.evs
#
# Toji Suzuhara 
"脱ぐわ…。\nワシ、ジャージしか着てへん\nイメージしかないし…。\n\0":
'???',

# Toji's Shadow [Leliel]
"で？　次は何着んの？\nま、それも別の偽りの自分自身を\n作るだけの事やけどね。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le501.evs
#
# Kaworu Nagisa 
# [NOTE] This is quite liberal, but hopefully nothing of importance is lost. -Reichu
"フフフ、決まってるだろう？\n彷徨った魂が、本来の肉体に宿る…。\nつまりアダムに還る事さ。\n\0":
'Heh heh heh, isn\'t it obvious?\nSo that a lost soul might inhabit its true flesh...\nReturning to Adam is my purpose.\n\0',

# Kaworu's Shadow [Leliel]
"構わないのかい？\n君が交じるリリン達の多くを、\n裏切る結果になってしまうだろう。\n\0":
'Don\'t you care?\nWhen all is said and done,\nyou\'ll have betrayed the many Lilin you\'ve met.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le502.evs
#
# Kaworu Nagisa 
"構わないよ。\nそのために僕は\nゼーレの計画に乗ったんだから。\n\0":
'No, I don\'t.\nThat\'s the very reason I\ngot on board with Seele\'s plan.\n\0',

# Kaworu's Shadow [Leliel]
"ネルフに来て得たもの、知ったもの、\n感じたもの、触れたもの…。\nすべて失う事になっても？\n\0":
'Coming to Nerv, learning,\nfeeling, experiencing...\nYou\'re okay with losing all of that?\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le503.evs
#
# Kaworu Nagisa 
"大袈裟だよ。\n彼らもわかってくれるさ。\n\0":
'You exaggerate.\nEven they understand me.\n\0',

# Kaworu's Shadow [Leliel]
"わかってくれる？\nリリンとアダムは相容れないものさ。\nその事を理解しているくせに…。\n\0":
'Understand you?\nLilin and Adam are incompatible.\nYou know it, too, and yet...\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le504.evs
#
# Kaworu Nagisa 
"覚悟の上さ。\nアダムの肉体を取り戻す事以上に\n大切なものって他に何かあるかい？\n\0":
'I\'m ready, besides.\nIs there anything more important\nthan taking back Adam\'s flesh?\n\0',

# Kaworu's Shadow [Leliel]
"フフフ…。\n嘘をついているね。\nずいぶん躊躇しているはずだよ。\n\0":
'Hehehe...\nYou\'re lying, you know.\nYou should be hesitating a great deal.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le505.evs
#
# Kaworu Nagisa 
"だが、まだ時期尚早さ。\n物事には順序があるからね。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"失うものの大きさに、\n怖気付いているんだね。▽\nやはり\nリリンに毒されているようだ…。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le507.evs
#
# Kaworu Nagisa 
"そうだね。\nでも僕は上手くやっているだろ？\n\0":
'???',

# Kaworu's Shadow [Leliel]
"思い上がりだよ。\n上手くやっているのは、\n壊したくないものがあるから。▽\nそれは弱さの証明さ。\n君はリリンから弱さを学んだだけだ。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le509.evs
#
# Kaworu Nagisa 
"仕方ないさ。\n当面の間はね。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"リリンの予定調和に\n組み込まれている事へ不満を\n感じているだろ？\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le511.evs
#
# Kaworu Nagisa 
"満足しているさ…。\n現時点ではね。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"欺瞞だよ、そんなの。\n先の事を\n考えてないはずないだろう？\n\0":
'???',

#
# ./USRDIR/event/levent.har_EXTRACT/le512.evs
#
# Kaworu Nagisa 
"くっ…、\n言うなっ！\n\0":
'Ngh...\nHold your tongue!\n\0',

# Kaworu's Shadow [Leliel]
"フフ…、見て見ぬふりかい？\n自分の事なのに…。▽\nともかく、\n今後君はどうするつもりなのかな？\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le514.evs
#
# Kaworu Nagisa 
"大丈夫さ。\n僕は生を諦めるつもりはないよ。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"それは\nリリンを全滅させるって意味だね。▽\nその後、\n君の生の意味を知るものはいるの？\n君一人で生き永らえてどうするの？\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le516.evs
#
# Kaworu Nagisa 
"当然だよ。\nフフ、わかってはいるんだけどね…。\n\0":
'???',

# Kaworu's Shadow [Leliel]
"ずいぶん曖昧な態度だね。\nリリンに感化されすぎたかな。\n\0":
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
# ./USRDIR/event/levent.har_EXTRACT/le518.evs
#
# Kaworu Nagisa 
# [Note] Not 100% on 種 referring to 生命の種 here. -Reichu
"いや、僕はアダムだ。\n種の役割を果たすつもりさ。\n\0":
'No, I am Adam.\nI intend to fulfill my Seedly duty.',

# Kaworu's Shadow [Leliel]
"フフ、本心の言葉じゃないね。\n…いや、自分を言い聞かせようと\nしているのか。\n\0":
'Heh-heh, but you don\'t voice your true feelings.\nNo... You are trying\nto persuade yourself.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le519.evs
#
# Kaworu Nagisa 
"そう…かもしれない…な。\n\0":
'It... could well be so.\n\0',

# Kaworu's Shadow [Leliel]
"フフ…、でも敵は敵だよ？\n彼らも最終的には絶対に\n君を受け入れないだろうね。\n\0":
'Heh-heh... But an enemy is an enemy, yes?\nIn the end, they won\'t accept\nyou unconditionally, will they?\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le520.evs
#
# Kaworu Nagisa 
"純粋な興味さ。\nヒトを知らないと、\nヒトに交われないからね。\n\0":
'It\'s genuine curiosity.\nIf I don\'t know anyone,\nI cannot interact with them.\n\0',

# Kaworu's Shadow [Leliel]
"悪影響を受けているようにしか\n見えない…、いや、他人に\n交わりつつ自分を変える…。▽\nそれは、リリンならではの行為だよ。\n\0":
'Looks to me like you\'re suffering ill effect...\nNo, rather, you yourself change\nas you mingle with others...▽\nThat is characteristic Lilin behavior.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le521.evs
#
# Kaworu Nagisa 
"そうじゃない！\n僕はヒトを知るために、\nヒトと接していただけだ。\n\0":
'That\'s not true!\nI only came in contact with humans\nso that I could know them.\n\0',

# Kaworu's Shadow [Leliel]
"フフ、そうは見えないよ。▽\nリリンの中は暖かくて、\n気持ちよかったんだろ？\nもう、すべてを忘れてしまうほどに。\n\0":
'Heh heh, that\'s not what I see.▽\nDon\'t you feel nice and warm\namong the Lilin?\nSo much that you\'ve already forgotten everything.\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le007.evs
#
# Kaworu Nagisa 
"もう、生命維持も限界か。▽\n…………………。\n\0":
'???',

# Kaworu Nagisa 
"僕の魂は僕のものだ。\n身体が滅びても、\nヒトとして生きた事を忘れても。▽\n僕はアダムの運命はもう、\n歩まない…。\n\0":
'My soul is everything I am.\nEven if my body perishes,\neven if I forget living as a human.▽\nI no longer follow\nAdam\'s fate...\n',

# Kaworu Nagisa 
"僕は、ヒトとして生きた。\n死ぬ時もヒトとして死のう。▽\nさよなら…、みんな…。\n\0":
'I lived as a human.\nShould I ever die, let it also be as a human.▽\nFarewell, everyone...\n\0',

# Shinji Ikari
"………………………。\nもう、保温も酸素の循環も\n切れてる。\n\0":
'???',

# Shinji Ikari
"寒い…。\n\0":
'???',

# Shinji Ikari
"駄目だ、スーツも限界か。\n\0":
'No good. Even the suit\'s giving out.\n\0',

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
'Asuka...\nAsuka-chan...\n\0',

# Asuka Soryu Langley
"ママ？\n\0":
'Mama?\n\0',

# Kyoko Soryu Zeppelin 
"アスカちゃん…。\n\0":
'Asuka-chan...\n\0',

# Asuka Soryu Langley
"ママ…、ママぁ…。\nどこに行ってたの、ママ。▽\nもう行かないで、そばにいて！\nママ…。\n\0":
'Mama... Mama!\nWhere have you been, Mama?▽\nDon\'t go away again, stay with me!\nMama...\n\0',

# Kyoko Soryu Zeppelin 
"一緒よ、ずっと…。\nでも、それでいいのね？\n\0":
'I\'m with you, always...\nBut is that alright?\n\0',

# Asuka Soryu Langley
"うん、いいの。\nママのところがいいの。\nずっとずっと、一緒にいる。\n\0":
'Yes, it\'s fine.\nI\'m okay being with Mama.\nTogether, forever and ever.\n\0',

# Kyoko Soryu Zeppelin 
"そう…、いいのよ。\nママはずっと一緒にいるわ。▽\nアスカちゃん…。\n\0":
'I see... That\'s good.\nMama is always with you,▽\nAsuka-chan...\n\0',

# Rei Ayanami 
"もう、何も見えない。\n何も聞こえない…。▽\n思い出すのは、ただ暗闇の中。\n\0":
'I can no longer see anything.\nNor hear anything...▽\nBeing shrouded in darkness, it\'s all I remember.\n\0',

# Rei Ayanami 
# [NOTE] Note sure if -te moraeru is being rendered correctly. -Reichu
"もう、帰してもらえるかしら。\n無へと…帰してもらえるのかしら。\n\0":
'Will I be able to return soon?\nWill they let me return to nothing?\n\0',

# Rei Ayanami 
"この身体も、もう終わり…。▽\n時間ね…。\n\0":
'It\'s already over for this body, too...▽\nAny time now...\n\0',

# Toji Suzuhara 
"寒ぅ…。\nもう、プラグの機能も\n限界なんやな…。\n\0":
'???',

# Toji Suzuhara 
"……………………。▽\n妹、無事なんかな…。▽\nごめんな。\n兄ちゃん、戻られへんわ。\n\0":
'.........▽\nSis,無事なんかな…。▽\nI\'m sorry.\nYour big brother won\'t be coming back.\n\0',

# Toji Suzuhara 
"おかん…。\nもう、ワシ…。\n\0":
'Mom...\nSo I\'m already...\n\0',

# Toji's Mother
"しんどかったなぁ、もうええねんで。\n\0":
'???',

# Toji Suzuhara 
"おかん…。\n何か、寒くて眠いんや…。\n\0":
'???',

# Toji's Mother
"さあ眠り…、お母ちゃんが\n温めてあげるわ…。\n\0":
'Go on, sleep... And\nMommy will keep you warm...\n\0',

#
# ./USRDIR/event/levent.har_EXTRACT/le008.evs
#
# Shinji Ikari
"会いたい。▽\nもう、一度。\n\0":
'I want to see them again.▽\nJust one more time.\n\0',

# Kyoko Soryu Zeppelin 
"あなたを待っている人がいるわ。\n\0":
'There are people waiting for you.\n\0',

# Kyoko Soryu Zeppelin 
"あなたはまだ、生きるのよ。\nアスカ。\nさあ、行きましょう。\n\0":
'You are still alive.\nAsuka.\nCome along now.\n\0',

# ??? [Lilith]
"そうはいかないわ。\n\0":
'That\'s not happening.\n\0',

# Rei Ayanami, Shinji Ikari
"誰…？\n\0":
'Who is it...?\n\0',

# ??? [Lilith]
"生命の実をこの手に…。\nアダムの民から奪い返すまでは。\n\0":
'Take the Fruit of Life in hand...\nDon\'t stop until you wrest it back from Adam\'s people.\n\0',

# Toji's Mother
"泣いたらアカンよ…。\nさあ、帰るで…。\n\0":
'???',

# Kaworu Nagisa 
"だが、この一度だけ。\n僕はアダムになろう…。\nヒトであり続けるために！\n\0":
'But I will become Adam,\njust one more time...\nSo I may continue being human!\n\0',

# Makoto Hyuga, Female Staff
"爆雷投下、６０秒前。\n\0":
'Dropping depth charges in 60 seconds.\n\0',

# Ritsuko Akagi, Female Staff
# [NOTE] Second sentence probably wrong is some subtle way. Third sounds utterly inane, not sure how to fix. -Reichu
"エヴァの機能は既に\n停止していたはず。\nなぜ、エヴァにあんな力が…！▽\n人の息の届かぬところに…、\nエヴァに心があるというの！？\n\0":
'The Eva\'s functions should\nhave suspended already.\nHow does the Eva have such power?!▽\nIs there a mind beyond the reach\nof people\'s breath... inside the Eva?!\n\0',

# Shigeru Aoba, Male Staff
"目標、殲滅を確認しました。\nパイロット、無事です！\n\0":
'Target has been destroyed.\nPilot is secure!\n\0',

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
# ./USRDIR/btl/tabris.har_EXTRACT/bk001.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk002.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk003.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk004.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk005.evs
# 
# Shinji Ikari
"君も…、\n僕を助けてくれないの？\n\0":
'???',

# Kaworu Nagisa 
"僕は君を、君は僕を救えない。\nいや、みんなそうさ。▽\n救われるかどうかは、\n自分で決めるしかない。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk006.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk007.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk008.evs
# 
# Shinji Ikari
"ごまかさないでよ、\nそうやって僕の気持ちを\nごまかさないでよ！！\n\0":
'???',

# Kaworu Nagisa 
"リリンは、絶望と向き合う事が\n出来ないからね。\n\0":
'???',

# Shinji Ikari
"そうやって、心を閉ざさないでよ！\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk009.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk010.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk011.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk012.evs
# 
# Shinji Ikari
"…そうなんだ。\n僕が嫌いなんだね。\n\0":
'???',

# Kaworu Nagisa 
"いいや、\n恐怖と絶望は、リリン達にも\n不要だという事さ。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk013.evs
# 
# Shinji Ikari
"何で、君まで僕を…、\n僕を傷つけるの…？\n\0":
'???',

# Kaworu Nagisa 
"君が僕という存在を知っただけ。\n傷つけたつもりはないよ。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk014.evs
# 
# Shinji Ikari
"でも、そうじゃないか。\n\0":
'???',

# Kaworu Nagisa 
"拒絶。\nそうやって自分の心を守るしか\nないのかい。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk015.evs
# 
# Shinji Ikari
"どうすればいいの？\n出会った時のように２人が\nなれるには、どうしたらいいの？\n\0":
'???',

# Kaworu Nagisa 
"………。▽\nすべてはリリンの流れのままに。▽\n………………。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk016.evs
# 
# Shinji Ikari
"嘘だよね。\nカヲル君が使徒だったなんて、\n嘘だよね…。\n\0":
'???',

# Kaworu Nagisa 
"僕は使徒としての価値を\n与えられた。▽\nそれが今、僕の存在している\n理由なんだ。\n\0":
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
# ./USRDIR/btl/tabris.har_EXTRACT/bk019.evs
#
# Kaworu Nagisa 
"嫌いじゃないよ。\nでも、嫌われると僕に恐怖心を\n抱いている。▽\nヒトを信じられないからだね。\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk018.evs
# 
# Shinji Ikari
"…関係ないよ。\nねえ、カヲル君は僕の事\nどう思ってるの…。\n\0":
'???',

# Kaworu Nagisa 
"…好きだよ、シンジ君。\n君の事が。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk019.evs
# 
# Shinji Ikari
"君に嫌われたくないよ。\n\0":
'???',

# Kaworu Nagisa 
"嫌いじゃないよ。\nでも、嫌われると僕に恐怖心を\n抱いている。▽\nヒトを信じられないからだね。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk020.evs
# 
# Shinji Ikari
"僕は、君に出会えた事が\n嬉しかったんだ。▽\n僕が探していたのは\n君だったんだって、嬉しかったんだ。\n\0":
'???',

# Kaworu Nagisa 
"僕も君に出会えて嬉しかったよ。\n同時に、悲しみもあった。\n\0":
'???',

# Kaworu Nagisa 
"でも、どんなに悲しくても\n君の事を忘れる事なんて出来ない。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk021.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk022.evs
# 
# Shinji Ikari
"カヲル君は、\n生きる事が楽しいの？\n\0":
'???',

# Kaworu Nagisa ,Teruo Kato, Misato Katsuragi, Rei Ayanami, Gendo Ikari, Ryoji Kaji, Shinji Ikari, Hikari Horaki, Maya Ibuki 
"……………。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk023.evs
# 
# Shinji Ikari
"カヲル君、\nもしかして死ぬつもりなの？\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk024.evs
# 
# Shinji Ikari
"わからないよ。\n君の意志じゃないのに\n使徒になったなんて。\n\0":
'???',

# Kaworu Nagisa 
"でも、僕が使徒なのは事実さ。\n君の友達という事も。▽\nどうする事も出来ないんだ、\n流れには逆らえない。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk025.evs
# 
# Shinji Ikari
"僕とやり直せるよ。\n違う生き方があるよ、\n僕も、君も。▽\n一緒にやり直そうよ、\nカヲル君…。\n\0":
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
# ./USRDIR/btl/tabris.har_EXTRACT/bk027.evs
# 
# Shinji Ikari
"カヲル君は僕にとって\n必要な人間なんだ。▽\n人類が居なくなるより、\n君が居なくなる方が嫌だよ！！\n\0":
'???',

# Kaworu Nagisa 
"………。▽\nでも、それじゃ、\n僕が寂しいままなんだ。▽\n一人で…。\nずっと一人で…。\n\0":
'???',

# Shinji Ikari
"だから！！\n僕がいるよ、ずっと側にいる！！\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk028.evs
# 
# Shinji Ikari
"僕もそうやって逃げてきた。\nでも、いい事なんてなかった。▽\n流れに任せて生きるなんて、\n死んでるのと同じじゃないか。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk029.evs
# 
# Shinji Ikari
"ねえ、僕ともう一度\n友達になってよ。▽\nそして全部…、何もかも\n二人でやりなおそうよ。\n\0":
'???',

# Kaworu Nagisa 
"友達に…？\nもう一度…？\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk030.evs
# 
# Shinji Ikari
"卑怯だよ。\n散々、僕に知った風な事を言って…。\n\0":
'???',

# Kaworu Nagisa 
"そうだね、そうかもしれない。\nその事は君に謝らなくちゃ\nいけなかったね…。\n\0":
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
# ./USRDIR/btl/tabris.har_EXTRACT/bk033.evs
# 
# Shinji Ikari
"そんなの信用出来ないよ！！\n\0":
'???',

# Kaworu Nagisa 
"僕が使徒だから…？\n僕は君を友達と思っているよ。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk034.evs
# 
# Shinji Ikari
"行くなら、いっそ僕を殺してよ…。\n\0":
'???',

# Kaworu Nagisa 
"………。▽\nそれが、君の答えだね。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk035.evs
# 
# Shinji Ikari
"君と戦うなら、死んだ方がいい。\n死んだ方がいいよ！！\n\0":
'???',

# Kaworu Nagisa 
"戦いを放棄するのかい？\nこの先に、君達の未来が\nかかっているとしても…？\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk036.evs
# 
# Shinji Ikari
"嘘だ！\n全部、それも僕を騙すためだ！\n\0":
'???',

# Kaworu Nagisa 
"…。▽\n僕が嫌いかい？\nそれが君の意志なら、\nしょうがない。\n\0":
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
# ./USRDIR/btl/tabris.har_EXTRACT/bk038.evs
# 
# Shinji Ikari
"行かないで…、\nカヲル君、行かないでよ！！▽\nそしたら、僕も君も\n一人じゃなくなるんだ！！\n\0":
'???',

# Kaworu Nagisa 
"…一人じゃ、なくなる…。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk039.evs
# 
# Shinji Ikari
"カヲル君、\n君とは戦いたくないよ。\n\0":
'???',

# Kaworu Nagisa 
"なぜ？\nじゃあなぜ僕を止めようとするの？\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk040.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk041.evs
# 
# Shinji Ikari
"死ぬのは怖いよ。\nでも、それより君を傷つける方が\n怖いよ。\n\0":
'???',

# Kaworu Nagisa 
"…なぜ、そこまで\n僕と戦いたくないんだい？\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk042.evs
# 
# Shinji Ikari
"行かないって言ってよ！！\nお願いだよ！\nこのままじゃ、君と戦うことになる。\n\0":
'???',

# Kaworu Nagisa 
"だったら、しょうがないんじゃ\nないかな。▽\n僕も、君と戦うのは\nいい気分じゃないけれど…。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk043.evs
# 
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

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk044.evs
# 
# Shinji Ikari
"行かないで…！！\n\0":
'???',

# Kaworu Nagisa 
"…それは君の意思かい？\nそれとも…。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk045.evs
# 
# Shinji Ikari
"僕は、僕はね…、\n君と生きたいんだ…。▽\n君が使徒だとかそんな事は\n関係ない。▽\n他の何でも関係なく、\n君と生きたいんだ。\n\0":
'???',

# Kaworu Nagisa 
"僕と…？\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk046.evs
# 
# Kaworu Nagisa 
"…シンジ君にはわからないよ。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk047.evs
#
# Kaworu Nagisa 
"………シンジ君。\n\0":
'...Shinji-kun.\n\0',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk048.evs
# 
# Kaworu Nagisa 
"僕にあったのは、\n…希望という絶望。▽\n人類がたどるべきだった道は\n絶望という希望…。▽\nシンジ君、僕も君が好きだったよ、\n君と希望を見つめたかった…。\nそうする事が出来れば…。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk049.evs
# 
# Kaworu Nagisa 
"………。▽\n僕も未来が見たい。\n君達、人と…、シンジ君の未来を\n見てみたいと思う。▽\n………。▽\nシンジ君…、僕も君と生きよう。\n僕も一緒に戦うよ…。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk050.evs
# 
# Kaworu Nagisa 
"これが………アダム………。\n…いや、…これは、リリス！？\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk052.evs
# 
# Kaworu Nagisa 
"僕の還る場所は一つしかない。\nここでは、生きていけない事は無い。\n…でも、…でも僕は。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk053.evs
#
# Kaworu Nagisa 
"ヒトが…、互いを必要と思うのは\nヒトの中にある何かのためなんだ。\nただそれだけのためなんだ。▽\n…でも、その何かに対して、\nヒトはみな、息を呑むほどに純粋だ。\nとても、哀しいほどに…。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk054.evs
# 
# Shinji Ikari
"カヲル君、\nみんなカヲル君が好きなんだ。\n僕も…。▽\nもっと話し合おうよ。\n僕ら、きっとわかりあえるよ。\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk055.evs
# 
# Shinji Ikari
"わかりあえないの？\nどうしても…？\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk056.evs
# 
# Shinji Ikari
"やっぱり、戦うしかないの…？\n\0":
'???',

#
# ./USRDIR/btl/tabris.har_EXTRACT/bk057.evs
# 
# Makoto Hyuga, Male Staff
"目標、反応消えました。\n使徒………殲滅しました。\n\0":
'???',

# Makoto Hyuga
"目標、反応消えました。\n使徒………消失しました。\n\0":
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
# ./USRDIR/event/bs007.har_EXTRACT/bs007.evs
#
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

#
# ./USRDIR/event/bs109.har_EXTRACT/bs109.evs
#
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

#
# ./USRDIR/event/bs008.har_EXTRACT/bs008.evs
#
# Kozo Fuyutsuki
"…勝ったな。\n\0":
'???',

#
# ./USRDIR/event/bs009.har_EXTRACT/bs009.evs
#
# Gendo Ikari
"そろそろだな…。\n\0":
'???',

#
# ./USRDIR/event/bs011.har_EXTRACT/bs011.evs
#
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

#
# ./USRDIR/event/bs012.har_EXTRACT/bs012.evs
#
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

#
# ./USRDIR/event/bs012.har_EXTRACT/bs013.evs
#
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

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba000.evs
#
# Shigeru Aoba, Male Staff
"エヴァ初号機、\nΑΤフィールド中和開始！\n\0":
'Eva Unit-01, commencing\nA.T. Field neutralization!\n\0',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\n初号機、残留ΑΤフィールド$h。\n\0":
'Angel\'s remaining A.T. Field at $g.\nUnit-01, remaining A.T. Field at $h.\n\0',

# Shigeru Aoba, Male Staff
"エヴァ弐号機、\nΑΤフィールド中和開始！\n\0":
'Eva Unit-02, commencing\nA.T. Field neutralization!\n\0',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\n弐号機、残留ΑΤフィールド$h。\n\0":
'Angel\'s remaining A.T. Field at $g.\nUnit-02, remaining A.T. Field at $h.\n\0',

# Shigeru Aoba, Male Staff
"エヴァ零号機、\nΑΤフィールド中和開始！\n\0":
'Eva Unit-00, commencing\nA.T. Field neutralization!\n\0',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\n零号機、残留ΑΤフィールド$h。\n\0":
'Angel\'s remaining A.T. Field at $g.\nUnit-00, remaining A.T. Field at $h.\n\0',

# Shigeru Aoba, Male Staff
"エヴァ参号機、\nΑΤフィールド中和開始！\n\0":
'Eva Unit-03, commencing\nA.T. Field neutralization!\n\0',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\n参号機、残留ΑΤフィールド$h。\n\0":
'Angel\'s remaining A.T. Field at $g.\nUnit-03, remaining A.T. Field at $h.\n\0',

# Shigeru Aoba, Male Staff
"エヴァ四号機、\nΑΤフィールド中和開始！\n\0":
'Eva Unit-04, commencing\nA.T. Field neutralization!\n\0',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\n四号機、残留ΑΤフィールド$h。\n\0":
'Angel\'s remaining A.T. Field at $g.\nUnit-04, remaining A.T. Field at $h.\n\0',

# Shigeru Aoba, Male Staff
"エヴァ両機、\nΑΤフィールド中和開始！\n\0":
'Both Eva units, commencing\nA.T. Field neutralization!\n\0',

# Shigeru Aoba, Male Staff
"使徒、残留ΑΤフィールド$g。\nエヴァ、残留ΑΤフィールド$h。\n\0":
'Angel\'s remaining A.T. Field at $g.\nEvas\' remaining A.T. Field at $h.\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba001.evs
#
# Shigeru Aoba, Male Staff
"目標のΑΤフィールド、\n消滅しました！\n\0":
'Target\'s A.T. Field\nhas gone down!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba002.evs
#
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

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba003.evs
#
# Misato Katsuragi 
"シンジ君は退避して！\n\0":
'Shinji-kun, take refuge!\n\0',

# Kozo Fuyutsuki
"初号機パイロットはただちに退避！\n\0":
'???',

# Female Staff
"初号機パイロットは\n退避して下さい！\n\0":
'???',

# Misato Katsuragi 
"アスカは退避して！\n\0":
'Asuka, take refuge!\n\0',

# Kozo Fuyutsuki
"弐号機パイロットは退避しろ。\n\0":
'???',

# Female Staff
"弐号機パイロットは\n退避して下さい！\n\0":
'???',

# Misato Katsuragi 
"レイは退避して！\n\0":
'Rei, take refuge!\n\0',

# Kozo Fuyutsuki
"零号機パイロットは退避しろ！\n\0":
'???',

# Female Staff
"零号機パイロットは\n退避して下さい！\n\0":
'???',

# Misato Katsuragi 
"トウジ君は退避して！\n\0":
'Toji-kun, take refuge!\n\0',

# Kozo Fuyutsuki
"参号機パイロットは退避だ！\n\0":
'???',

# Female Staff
"参号機パイロットは\n退避して下さい！\n\0":
'???',

# Misato Katsuragi 
"カヲル君は退避して！\n\0":
'Kaworu-kun, take refuge!\n\0',

# Kozo Fuyutsuki
"四号機パイロットは退避しろ！\n\0":
'???',

# Female Staff
"四号機パイロットは\n退避して下さい！\n\0":
'???',

# Misato Katsuragi 
"エヴァ両機は退避して！\n\0":
'Both Eva units, take refuge!\n\0',

# Kozo Fuyutsuki
"エヴァ両機パイロットは\nただちに退避！\n\0":
'???',

# Female Staff
"エヴァ両機パイロットは\n退避して下さい！\n\0":
'???',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba004.evs
#
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
# ./USRDIR/btl/bevent.har_EXTRACT/ba006.evs
#
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

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba007.evs
#
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

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba008.evs
#
# Misato Katsuragi 
"初号機、\n$fエリアに移動して！\n\0":
'Unit-01,\nmove to Area $f!\n\0',

# Kozo Fuyutsuki
"初号機、\n$fエリアに移動！\n\0":
'Unit-01,\nmove to Area $f!\n\0',

# Female Staff
"初号機、$fエリアに\n移動して下さい！\n\0":
'Unit-01, please\nmove to Area $f!\n\0',

# Misato Katsuragi 
"弐号機、\n$fエリアに移動して！\n\0":
'Unit-02,\nmove to Area $f!\n\0',

# Kozo Fuyutsuki
"弐号機、\n$fエリアに移動！\n\0":
'Unit-02,\nmove to Area $f!\n\0',

# Female Staff
"弐号機、$fエリアに\n移動して下さい！\n\0":
'Unit-02, please\nmove to Area $f!\n\0',

# Misato Katsuragi 
"零号機、\n$fエリアに移動して！\n\0":
'Unit-00,\nmove to Area $f!\n\0',

# Kozo Fuyutsuki
"零号機、\n$fエリアに移動！\n\0":
'Unit-00,\nmove to Area $f!\n\0',

# Female Staff
"零号機、$fエリアに\n移動して下さい！\n\0":
'Unit-00, please\nmove to Area $f!\n\0',

# Misato Katsuragi 
"参号機、\n$fエリアに移動して！\n\0":
'Unit-03,\nmove to Area $f!\n\0',

# Kozo Fuyutsuki
"参号機、\n$fエリアに移動！\n\0":
'Unit-03,\nmove to Area $f!\n\0',

# Female Staff
"参号機、$fエリアに\n移動して下さい！\n\0":
'Unit-03, please\nmove to Area $f!\n\0',

# Misato Katsuragi 
"四号機、\n$fエリアに移動して！\n\0":
'Unit-04,\nmove to Area $f!\n\0',

# Kozo Fuyutsuki
"四号機、\n$fエリアに移動！\n\0":
'Unit-04,\nmove to Area $f!\n\0',

# Female Staff
"四号機、$fエリアに\n移動して下さい！\n\0":
'Unit-04, please\nmove to Area $f!\n\0',

# Misato Katsuragi 
"エヴァ両機、\n$fエリアに移動して！\n\0":
'Both Evas,\nmove to Area $f!\n\0',

# Kozo Fuyutsuki
"エヴァ両機、\n$fエリアに移動！\n\0":
'Both Evas,\nmove to Area $f!',

# Female Staff
"エヴァ両機、$fエリアに\n移動して下さい！\n\0":
'Both Evas, please\nmove to Area $f!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba009.evs
#
# Makoto Hyuga, Male Staff
"エヴァ初号機の攻撃、\n使徒に$jのダメージ！\n\0":
'Eva Unit-01\'s attack did\n$j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ弐号機の攻撃、\n使徒に$jのダメージ！\n\0":
'Eva Unit-02\'s attack did\n$j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ零号機の攻撃、\n使徒に$jのダメージ！\n\0":
'Eva Unit-00\'s attack did\n$j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ参号機の攻撃、\n使徒に$jのダメージ！\n\0":
'Eva Unit-03\'s attack did\n$j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ四号機の攻撃、\n使徒に$jのダメージ！\n\0":
'Eva Unit-04\'s attack did\n$j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"エヴァ両機の攻撃、\n使徒に$jのダメージ！\n\0":
'Both Evas\' attacks did\n$j damage to the Angel!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、初号機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n$j damage to the Unit-01!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、弐号機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n$j damage to the Unit-02!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、零号機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n$j damage to the Unit-00!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、参号機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n$j damage to the Unit-03!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、四号機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n$j damage to the Unit-04!\n\0',

# Makoto Hyuga, Male Staff
"使徒の攻撃、エヴァ両機に\n$jのダメージ！\n\0":
'The Angel\'s attack did\n$j damage to both Evas!\n\0',

# Makoto Hyuga, Male Staff
"ΑΤフィールドとシンクロ率、\n共に低下！\n\0":
'A.T. Field and synch ratio\nare both down!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba011.evs
#
# Shigeru Aoba, Male Staff
"$fエリア、兵装ビル、攻撃！\n使徒に$jのダメージ！\n\0":
'???',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba012.evs
#
# Shigeru Aoba, Male Staff
"$fエリア電源ビル、\n使徒の攻撃により、$jのダメージ！\n\0":
'The power building in Area $f\nreceived $j damage from the Angel!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア武器庫ビル、\n使徒の攻撃により、$jのダメージ！\n\0":
'The armory building in Area $f\nreceived $j damage from the Angel!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア兵装ビル、\n使徒の攻撃により、$jのダメージ！\n\0":
'The armament building in Area $f\nreceived $j damage from the Angel!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア防御施設、\n使徒の攻撃により、$jのダメージ！\n\0":
'The defense facility in Area $f\nreceived $j damage from the Angel!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba013.evs
#
# Shigeru Aoba, Male Staff
"$fエリア、国連軍、攻撃！\n使徒、$jのダメージ！\n\0":
'Attack by U.N. forces in Area $f!\n$j damage to the Angel!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア、国連軍、\n使徒の攻撃により、$jのダメージ！\n\0":
'U.N. forces in Area $f\nreceived $j damage from the Angel!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba015.evs
#
# Shigeru Aoba, Male Staff
"$fエリア電源ビル、\n破壊されました！\n\0":
'The power building in Area $f\nhas been destroyed!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア武器庫ビル、\n破壊されました！\n\0":
'The armory building in Area $f\nhas been destroyed!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア兵装ビル、\n破壊されました！\n\0":
'The armament building in Area $f\nhas been destroyed!\n\0',

# Shigeru Aoba, Male Staff
"$fエリア防御施設、\n破壊されました！\n\0":
'The defense facility in Area $f\nhas been destroyed!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba016.evs
#
# Shigeru Aoba, Male Staff
"$fエリア、国連軍、\n掃滅しました！\n\0":
'???',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba017.evs
#
# Maya Ibuki, Female Staff
"エヴァ初号機のアンビリカルケーブル、\n切断しました！\n\0":
'Eva Unit-01\'s umbilical cable\nis disconnected!\n\0',

# Maya Ibuki, Female Staff
"エヴァ弐号機のアンビリカルケーブル、\n切断しました！\n\0":
'Eva Unit-02\'s umbilical cable\nis disconnected!\n\0',

# Maya Ibuki, Female Staff
"エヴァ零号機のアンビリカルケーブル、\n切断しました！\n\0":
'Eva Unit-00\'s umbilical cable\nis disconnected!\n\0',

# Maya Ibuki, Female Staff
"エヴァ参号機のアンビリカルケーブル、\n切断しました！\n\0":
'Eva Unit-03\'s umbilical cable\nis disconnected!\n\0',

# Maya Ibuki, Female Staff
"エヴァ四号機のアンビリカルケーブル、\n切断しました！\n\0":
'Eva Unit-04\'s umbilical cable\nis disconnected!\n\0',

# Maya Ibuki, Female Staff
"エヴァ両機のアンビリカルケーブル、\n切断しました！\n\0":
'Both Evas\' umbilical cables\nare disconnected!\n\0',

# Maya Ibuki, Female Staff
"エヴァ初号機、\nアンビリカルケーブル接続。\n\0":
'Eva Unit-01,\numbilical cable connected.\n\0',

# Maya Ibuki, Female Staff
"エヴァ弐号機、\nアンビリカルケーブル接続。\n\0":
'Eva Unit-02,\numbilical cable connected.\n\0',

# Maya Ibuki, Female Staff
"エヴァ零号機、\nアンビリカルケーブル接続。\n\0":
'Eva Unit-00,\numbilical cable connected.\n\0',

# Maya Ibuki, Female Staff
"エヴァ参号機、\nアンビリカルケーブル接続。\n\0":
'Eva Unit-03,\numbilical cable connected.\n\0',

# Maya Ibuki, Female Staff
"エヴァ四号機、\nアンビリカルケーブル接続。\n\0":
'Eva Unit-04,\numbilical cable connected.\n\0',

# Maya Ibuki, Female Staff
"エヴァ両機、\nアンビリカルケーブル接続。\n\0":
'Both Evas,\numbilical cables connected.\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba021.evs
# 
# Toji Suzuhara 
"ほな、いっちょ\nパチキかましたらぁ！！\n\0":
'???',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba022.evs
# 
# Maya Ibuki 
"エヴァ初号機、\nポジトロンスナイパーライフル発射！\n\0":
'Eva Unit-01 has discharged\nthe positron sniper rifle!\n\0',

# Male Staff
"エヴァ初号機、ポジトロンスナイパー\nライフルの発射に成功しました！\n\0":
'Eva Unit-01 successfully discharged\nthe positron sniper rifle!\n\0',

# Maya Ibuki 
"エヴァ弐号機、\nポジトロンスナイパーライフル発射！\n\0":
'Eva Unit-02 has discharged\nthe positron sniper rifle!\n\0',

# Male Staff
"エヴァ弐号機、ポジトロンスナイパー\nライフルの発射に成功しました！\n\0":
'Eva Unit-02 successfully discharged\nthe positron sniper rifle!\n\0',

# Maya Ibuki 
"エヴァ零号機、\nポジトロンスナイパーライフル発射！\n\0":
'Eva Unit-00 has discharged\nthe positron sniper rifle!\n\0',

# Male Staff
"エヴァ零号機、ポジトロンスナイパー\nライフルの発射に成功しました！\n\0":
'Eva Unit-00 successfully discharged\nthe positron sniper rifle!\n\0',

# Maya Ibuki 
"エヴァ参号機、\nポジトロンスナイパーライフル発射！\n\0":
'Eva Unit-03 has discharged\nthe positron sniper rifle!\n\0',

# Male Staff
"エヴァ参号機、ポジトロンスナイパー\nライフルの発射に成功しました！\n\0":
'Eva Unit-03 successfully discharged\nthe positron sniper rifle!\n\0',

# Maya Ibuki 
"エヴァ四号機、\nポジトロンスナイパーライフル発射！\n\0":
'Eva Unit-04 has discharged\nthe positron sniper rifle!\n\0',

# Male Staff
"エヴァ四号機、ポジトロンスナイパー\nライフルの発射に成功しました！\n\0":
'Eva Unit-04 successfully discharged\nthe positron sniper rifle!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba030.evs
# 
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

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba032.evs
# 
# Shigeru Aoba, Male Staff
"兵装ビル、攻撃！\n$jのダメージ！\n\0":
'Armory building has attacked!\nIt did $j damage!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba034.evs
# 
# Shigeru Aoba, Male Staff
"電源ビル、エヴァシリーズの\n攻撃により、破壊されました！\n\0":
'Power building has been\ndestroyed by the Eva Series!\n\0',

# Shigeru Aoba, Male Staff
"武器庫ビル、エヴァシリーズの\n攻撃により、破壊されました！\n\0":
'Armory building has been\ndestroyed by the Eva Series!\n\0',

# Shigeru Aoba, Male Staff
"兵装ビル、エヴァシリーズの\n攻撃により、破壊されました！\n\0":
'Armament building has been\ndestroyed by the Eva Series!\n\0',

# Shigeru Aoba, Male Staff
"防御施設、エヴァシリーズの\n攻撃により、破壊されました！\n\0":
'Defense facility has been\ndestroyed by the Eva Series!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba035.evs
# 
# Makoto Hyuga, Male Staff
"ΘΑ改、攻撃！\n$jのダメージ！\n\0":
'ΘΑ2 has attacked!\nIt did $j damage!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba036.evs
# 
# Makoto Hyuga, Male Staff
"エヴァシリーズの攻撃、\nΘΑ改に$jのダメージ！\n\0":
'Attack by Eva Series unit\ndid $j damage to ΘΑ2!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba037.evs
# 
# Shigeru Aoba, Male Staff
"兵装ビル、攻撃！\n使徒に$jのダメージ！\n\0":
'Armament building attacked!\n$j damage to the Angel!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba038.evs
# 
# Shigeru Aoba, Male Staff
"電源ビル、\n$jのダメージ！\n\0":
'Power building has\ntaken $j damage!\n\0',

# Shigeru Aoba, Male Staff
"武器庫ビル、\n$jのダメージ！\n\0":
'Armory building has\ntaken $j damage!\n\0',

# Shigeru Aoba, Male Staff
"兵装ビル、\n$jのダメージ！\n\0":
'Armament building has\ntaken $j damage!\n\0',

# Shigeru Aoba, Male Staff
"防御施設、\n$jのダメージ！\n\0":
'Defense facility has\ntaken $j damage!\n\0',

# Shigeru Aoba, Male Staff
"ネルフ本部、\n$jのダメージ！\n\0":
'Nerv H.Q. has\ntaken $j damage!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba039.evs
# 
# Shigeru Aoba, Male Staff
"国連軍、攻撃！\n使徒、$jのダメージ！\n\0":
'Attack by U.N. forces!\n$j damage to the Angel!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba040.evs
# 
# Shigeru Aoba, Male Staff
"国連軍、\n$jのダメージ！\n\0":
'U.N. forces have\ntaken $j damage!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba041.evs
# 
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

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba042.evs
# 
# Shigeru Aoba, Male Staff
"国連軍、\n掃滅しました！\n\0":
'U.N. forces have\nbeen annihilated!\n\0',

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
# ./USRDIR/btl/bevent.har_EXTRACT/ba045.evs
# 
# Maya Ibuki, Female Staff
"エヴァ初号機、神経再接続完了！\n\0":
'Eva Unit-01, neural reconnection completed!\n\0',

# Maya Ibuki, Female Staff
"エヴァ弐号機、神経再接続完了！\n\0":
'Eva Unit-02, neural reconnection completed!\n\0',

# Maya Ibuki, Female Staff
"エヴァ零号機、神経再接続完了！\n\0":
'Eva Unit-00, neural reconnection completed!\n\0',

# Maya Ibuki, Female Staff
"エヴァ参号機、神経再接続完了！\n\0":
'Eva Unit-03, neural reconnection completed!\n\0',

# Maya Ibuki, Female Staff
"エヴァ四号機、神経再接続完了！\n\0":
'Eva Unit-04, neural reconnection completed!\n\0',

# Maya Ibuki, Female Staff
"エヴァ両機、神経再接続完了！\n\0":
'Both Eva units, neural reconnection completed!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/ba046.evs
# 
# Shigeru Aoba, Male Staff
"量産機、残留ΑΤフィールド$g。\n初号機、残留ΑΤフィールド$h。\n\0":
'Mass production unit, remaining A.T. Field at $g.\nUnit-01, remaining A.T. Field at $h.\n\0',

# Shigeru Aoba, Male Staff
"量産機、残留ΑΤフィールド$g。\n弐号機、残留ΑΤフィールド$h。\n\0":
'Mass production unit, remaining A.T. Field at $g.\nUnit-02, remaining A.T. Field at $h.\n\0',

# Shigeru Aoba, Male Staff
"量産機、残留ΑΤフィールド$g。\n零号機、残留ΑΤフィールド$h。\n\0":
'Mass production unit, remaining A.T. Field at $g.\nUnit-00, remaining A.T. Field at $h.\n\0',

# Shigeru Aoba, Male Staff
"量産機、残留ΑΤフィールド$g。\n参号機、残留ΑΤフィールド$h。\n\0":
'Mass production unit, remaining A.T. Field at $g.\nUnit-03, remaining A.T. Field at $h.\n\0',

# Shigeru Aoba, Male Staff
"量産機、残留ΑΤフィールド$g。\n四号機、残留ΑΤフィールド$h。\n\0":
'Mass production unit, remaining A.T. Field at $g.\nUnit-04, remaining A.T. Field at $h.\n\0',

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
# ./USRDIR/btl/bevent.har_EXTRACT/ba048.evs
# 
# Misato Katsuragi 
"初号機、移動して！\n\0":
'Unit-01, relocate!\n\0',

# Kozo Fuyutsuki
"初号機、移動！\n\0":
'Unit-01, relocate!\n\0',

# Female Staff
"初号機、移動して下さい！\n\0":
'Unit-01, please relocate!\n\0',

# Misato Katsuragi 
"弐号機、移動して！\n\0":
'Unit-02, relocate!\n\0',

# Kozo Fuyutsuki
"弐号機、移動！\n\0":
'Unit-02, relocate!\n\0',

# Female Staff
"弐号機、移動して下さい！\n\0":
'Unit-02, please relocate!\n\0',

# Misato Katsuragi 
"零号機、移動して！\n\0":
'Unit-00, relocate!\n\0',

# Kozo Fuyutsuki
"零号機、移動！\n\0":
'Unit-00, relocate!\n\0',

# Female Staff
"零号機、移動して下さい！\n\0":
'Unit-00, please relocate!\n\0',

# Misato Katsuragi 
"参号機、移動して！\n\0":
'Unit-03, relocate!\n\0',

# Kozo Fuyutsuki
"参号機、移動！\n\0":
'Unit-03, relocate!\n\0',

# Female Staff
"参号機、移動して下さい！\n\0":
'Unit-03, please relocate!\n\0',

# Misato Katsuragi 
"四号機、移動して！\n\0":
'Unit-04, relocate!\n\0',

# Kozo Fuyutsuki
"四号機、移動！\n\0":
'Unit-04, relocate!\n\0',

# Female Staff
"四号機、移動して下さい！\n\0":
'Unit-04, please relocate!\n\0',

# Misato Katsuragi 
"エヴァ両機、移動して！\n\0":
'Both Eva units, relocate!\n\0',

# Kozo Fuyutsuki
"エヴァ両機、移動！\n\0":
'Both Eva units, relocate!\n\0',

# Female Staff
"エヴァ両機、移動して下さい！\n\0":
'Both Eva units, please relocate!\n\0',

#
# ./USRDIR/btl/bevent.har_EXTRACT/d011.evs
#
# Toji Suzuhara 
"ぎゃあ！！\n\0":
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
}
