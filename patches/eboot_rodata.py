#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Note:
# This file contains section-specific untranslated strings
# Put the translations in the ???
# \n is a linebreak
# \' is a single quote
# The string terminator is implied (and already included in size)

from game_app.support import *

section_rodata = AppSection('.rodata', 0x001B0640, 0x0002A3A0, AppSectionFlag.Allocated,
{
    # PreRelocationAddress: Data(Type, Size, Value, Comment)
    0x001B1540: Data(DataType.String, 16, "Yes No", "は　い　いいえ"),
    0x001B1880: Data(DataType.String, 72, "Follows the events of the show.\nIncludes a tutorial and\nideal for first-time players.", "原作どおりに展開する。\nチュートリアルを含み、\n初めてのプレイに最適。"),
    0x001B18C8: Data(DataType.String, 76, "Before you are loved by another, you\nshould love all people in full.\nIt will surely change the world.", "人に愛される前に、\n全ての人を充分に愛して下さい。\n世界は必ず変わります。"),
    0x001B1914: Data(DataType.String, 72, "Rei Ayanami's gaze is fixed upon her\nformer self -- and upon her future.\nWhat is Rei's soul planning...?", "綾波レイとなる以前の自分、\nそして未来を見つめる。\nレイの魂の目的は…？"),
    0x001B195C: Data(DataType.String, 80, "Asuka fights, keeping her fragility hidden.\nCan the curse on her heart\nbe lifted at Instrumentality's end?", "己の脆さを隠し、戦うアスカ。\n補完の果てに、心の呪縛を\n解き放つ事が出来るのか。"),
    0x001B19AC: Data(DataType.String, 64, "Seeking revenge on all the things\nthat took her father from her,\na woman chases after the truth.", "父を奪った全てのものに\n復讐する為に、\n女は真実を追い求める。"),
    0x001B19EC: Data(DataType.String, 76, "There is but one hope: the Way to God.\nSo that all hearts can be made one,\na man waits for that time...", "望みは唯一つ、神への道。\n全ての心を一つにする為に、\n男はその時を待つ…。"),
    0x001B1A38: Data(DataType.String, 80, "Drifting within a dream,\nchasing the scent and shadow of an old loved one...\nAnd as for his reunion with her...", "かつての想い人の香りと影を\n追って、夢の中に舞う…。\nそして想い人との再会は…。"),
    0x001B1A88: Data(DataType.String, 76, "The pride of a woman who's been toyed with.\nMen being inflamed by a female inferno. The one who'll be kneeling in the end is HIM.", "弄ばれた女の意地。\n女の炎にただれていく男達。\n最後にひざまずくのはあの男。"),
    0x001B1AD4: Data(DataType.String, 92, "Maya rejects the world from a desire to not be sullied,\nputting on a brave face as she seeks the place she belongs.\nThe day she will find her peace is coming...", "汚れたくない思いで世界を拒み、\n居場所を求め虚勢を張るマヤ。\n彼女が安らぎを得られる日は…。"),
    0x001B1B30: Data(DataType.String, 80, "Hyuga pursues the truth as a pretext to\nmeet with Misato. And so follow the sweet,\nreckless relations between man and woman.", "ミサトに会う口実の為に真実を\n追う日向。そして、甘く、\nだらしなく交わる男と女。"),
    0x001B1B80: Data(DataType.String, 88, "Aoba gave up a career as a musician\nwhen he joined Nerv. But if he\nhadn't abandoned his old dream...", "ミュージシャンとしての道を\n諦めて、ネルフに入った青葉。\nあの時の夢を諦めなければ…。"),
    0x001B1BD8: Data(DataType.String, 48, "In search of the truth behind Seele\nand Nerv, he'll fight alone.", "ゼーレとネルフを相手に\n真実を求めて孤独に戦う。"),
    0x001B1C08: Data(DataType.String, 76, "For the sake of his hospitalized sister, doing\nthe things he can do... What\nwill Toji's reality be like in the end...?", "入院する妹の為に、自分が\n出来る事…。全てを尽くして\n得られた現実とは…？"),
    0x001B1C54: Data(DataType.String, 88, "Dreaming of becoming an Eva pilot until\nthe end, what tragedy awaits after\nawaking from this dream...?", "エヴァのパイロットに憧れ、\t\nその果てに知った絶え難い現実。\n夢から覚めた後の悲劇とは…。"),
    0x001B1CAC: Data(DataType.String, 80, "The meek Hikari, her thoughts of Toji\ngrowing deeper. The love of two who\npass each other by.", "募りゆくトウジへの想い。\n素直になれないヒカリ。\nすれ違う２人の恋の行方は…。"),
    0x001B1CFC: Data(DataType.String, 84, "Born as an Angel, where is Kaworu's\nsoul headed? Upon releasing his\npower as an Angel, he...", "使徒として生まれたカヲルの\n魂の向かう先…。使徒として\n力を解放した時、カヲルは…。"),
    0x001B1D50: Data(DataType.String, 76, "Seeking happiness, Pen Pen's sweepstakes\nlife begins. Collect all the\ncoupon stickers you can!", "幸せになりたいペンペンの\n懸賞生活が始まる。\nクーポンシールを集めまくれ！"),
    0x001B1D9C: Data(DataType.String, 52, "Highest difficulty.\nSnatch humanity's victory from the\njaws of defeat!", "難易度最高。\n絶望的な状況から、\n人類の勝利を掴め！"),
    0x001B1E98: Data(DataType.String, 12, "Angel Attack", "使徒襲来"),
    0x001B1EAC: Data(DataType.String, 24, "But I Like This World", "でも、この世界が好き"),
    0x001B1ECC: Data(DataType.String, 20, "Rei: Beyond Her Heart", "レイ、心の向こうに"),
    0x001B1EE8: Data(DataType.String, 24, "To Kiss in a Fragile Place", "脆いところへくちづけを"),
    0x001B1F08: Data(DataType.String, 12, "A Woman's Fight", "女の戦い"),
    0x001B1F1C: Data(DataType.String, 16, "Human Instrumentality Project", "人類補完計画"),
    0x001B1F34: Data(DataType.String, 16, "Impossible Daydream", "見果てぬ白昼夢"),
    0x001B1F4C: Data(DataType.String, 8, "Female Inferno", "女は炎"),
    0x001B1F5C: Data(DataType.String, 12, "Green Grass Days", "若草の頃"),
    0x001B1F70: Data(DataType.String, 12, "Hazy Skies", "曖昧な空"),
    0x001B1F84: Data(DataType.String, 16, "Cobalt Sky", "コバルトスカイ"),
    0x001B1F9C: Data(DataType.String, 16, "Vs. Seele", "ＶＳ．ゼーレ"),
    0x001B1FB4: Data(DataType.String, 20, "I Give You My Everything", "心のありったけを"),
    0x001B1FD0: Data(DataType.String, 16, "If You Wake From the Dream", "夢から覚めれば"),
    0x001B1FE8: Data(DataType.String, 16, "Those Who Saw Spring", "春を見たヒト"),
    0x001B2000: Data(DataType.String, 12, "Broken Wings", "折れた翼"),
    0x001B2014: Data(DataType.String, 28, "What Human Hands Can't Yet Touch", "ニンゲンの手がまだ触れない"),
    0x001B2038: Data(DataType.String, 28, "Shibamuratic Balance", "シバムラティックバランス"),
    0x001B205C: Data(DataType.String, 16, "Emotional Complementation Viewing", "心の補完観察"),
    0x001B236C: Data(DataType.String, 12, "Living Room", "リビング"),
    0x001B2378: Data(DataType.String, 20, "Dining Room and Kitchen", "ダイニングキッチン"),
    0x001B238C: Data(DataType.String, 16, "Shinji's Room (Old)", "旧シンジの部屋"),
    0x001B239C: Data(DataType.String, 16, "Shinji's Room (New)", "新シンジの部屋"),
    0x001B23AC: Data(DataType.String, 16, "Asuka's Room", "アスカの部屋"),
    0x001B23BC: Data(DataType.String, 16, "Misato's Room", "ミサトの部屋"),
    0x001B23CC: Data(DataType.String, 16, "Misato's House: Bathroom", "ミサト家洗面所"),
    0x001B23DC: Data(DataType.String, 16, "Commander's Office", "総司令公務室"),
    0x001B23EC: Data(DataType.String, 8, "Command Center", "発令所"),
    0x001B23F4: Data(DataType.String, 16, "Misato's Office", "ミサトの執務室"),
    0x001B2404: Data(DataType.String, 12, "Nerv Cafeteria", "ネルフ食堂"),
    0x001B2410: Data(DataType.String, 16, "Ritsuko's Laboratory", "リツコの研究室"),
    0x001B2420: Data(DataType.String, 12, "Kaji's Private Room", "加持の個室"),
    0x001B242C: Data(DataType.String, 20, "Vending Machine Corner A", "自販機コーナーＡ"),
    0x001B2440: Data(DataType.String, 20, "Vending Machine Corner B", "自販機コーナーＢ"),
    0x001B2454: Data(DataType.String, 16, "Kaworu's Quarters", "カヲルの宿舎"),
    0x001B2464: Data(DataType.String, 16, "Nerv Public Bath", "ネルフ大浴場"),
    0x001B2474: Data(DataType.String, 20, "Central Dogma", "セントラルドグマ"),
    0x001B2488: Data(DataType.String, 12, "Rei's Room", "レイの部屋"),
    0x001B2494: Data(DataType.String, 16, "Rei's House: Bathroom", "レイ家洗面所"),
    0x001B24A4: Data(DataType.String, 12, "Classroom 2-A", "２−Ａ教室"),
    0x001B24B0: Data(DataType.String, 12, "School Hallway", "学校廊下"),
    0x001B24BC: Data(DataType.String, 12, "Convenience Store", "コンビニ"),
    0x001B24C8: Data(DataType.String, 8, "Ruins", "廃墟"),
    0x001B24D0: Data(DataType.String, 12, "Labyrinth of the Heart", "心の迷宮"),
    0x001B24DC: Data(DataType.String, 12, "Backup (1)", "予備（１）"),
    0x001B24E8: Data(DataType.String, 12, "Backup (2)", "予備（２）"),
    0x001B24F4: Data(DataType.String, 12, "Backup (3)", "予備（３）"),
    0x001B2500: Data(DataType.String, 12, "Backup (4)", "予備（４）"),
    0x001B250C: Data(DataType.String, 12, "Backup (5)", "予備（５）"),
    0x001B2518: Data(DataType.String, 12, "Full Map", "全体マップ"),
    0x001B2524: Data(DataType.String, 20, "Nerv Facilities Map", "ネルフ施設マップ"),
    0x001B2538: Data(DataType.String, 8, "Your House", "自宅"),
    0x001B2540: Data(DataType.String, 8, "Your Room", "自室"),
    0x001B2548: Data(DataType.String, 20, "Game Backup (1)", "ゲーム用予備（１）"),
    0x001B255C: Data(DataType.String, 20, "Game Backup (2)", "ゲーム用予備（２）"),
    0x001B2570: Data(DataType.String, 20, "Game Backup (3)", "ゲーム用予備（３）"),
    0x001B2584: Data(DataType.String, 20, "Game Backup (4)", "ゲーム用予備（４）"),
    0x001B2598: Data(DataType.String, 20, "Game Backup (5)", "ゲーム用予備（５）"),
    0x001B2B84: Data(DataType.String, 16, "Easily triumphed in battle", "戦闘に快勝した"),
    0x001B2B94: Data(DataType.String, 16, "Victorious in battle", "戦闘に勝利した"),
    0x001B2BA4: Data(DataType.String, 16, "Narrowly won the battle", "戦闘に辛勝した"),
    0x001B2BB4: Data(DataType.String, 24, "Defeated Bardiel", "バルディエルを倒した"),
    0x001B2BCC: Data(DataType.String, 20, "Compromise reached with Kaworu", "カヲルと和解した"),
    0x001B2BE0: Data(DataType.String, 16, "Defeated Kaworu", "カヲルを殺した"),
    0x001B2BF0: Data(DataType.String, 20, "J.A. was stopped", "ＪＡを停止させた"),
    0x001B2C04: Data(DataType.String, 24, "Triumphed against Leliel", "レリエル戦に勝利した"),
    0x001B2C1C: Data(DataType.String, 24, "Damaged the enemy", "敵にダメージを与えた"),
    0x001B2C34: Data(DataType.String, 24, "Damaged by enemy", "敵にダメージを受けた"),
    0x001B2C4C: Data(DataType.String, 20, "Finished off the enemy", "敵に止めを刺した"),
    0x001B2C60: Data(DataType.String, 20, "Finished off by the enemy", "敵に止めを刺された"),
    0x001B2C74: Data(DataType.String, 20, "Instructions were rejected", "指示を拒否された"),
    0x001B2C88: Data(DataType.String, 20, "Unit-01 went berserk", "初号機が暴走した"),
    0x001B2C9C: Data(DataType.String, 20, "Unit-01 awakened", "初号機が覚醒した"),
    0x001B2CB0: Data(DataType.String, 28, "Utilized the Spear of Longinus", "ロンギヌスの槍を使用した"),
    0x001B2CCC: Data(DataType.String, 24, "Utilized the Dummy Plug", "ダミープラグを使用した"),
    0x001B2CE4: Data(DataType.String, 28, "Piloting impossible due to sync ratio decrease", "シンクロ率低下で操縦不能"),
    0x001B2D00: Data(DataType.String, 20, "Internal power fully depleted", "体内電源0になった"),
    0x001B2D14: Data(DataType.String, 16, "Comrades incapable of combat", "仲間が戦闘不能"),
    0x001B2D24: Data(DataType.String, 24, "Nearly strangled to death", "絞め殺されそうになった"),
    0x001B2D3C: Data(DataType.String, 20, "Intimidated with Evas", "エヴァで恫喝した"),
    0x001B2D50: Data(DataType.String, 24, "Suicide bombed the Angel", "使徒を道ずれに自爆した"),
    0x001B2D68: Data(DataType.String, 28, "Angel breached the Geofront", "ジオフロンに使徒が侵入した"),
    0x001B2D84: Data(DataType.String, 24, "Comrade took damage", "相手にダメージを与えた"),
    0x001B2D9C: Data(DataType.String, 20, "Comrade went down", "相手に止めを刺した"),
    0x001B2DB0: Data(DataType.String, 16, "Evaded attack", "攻撃をかわした"),
    0x001B2DC0: Data(DataType.String, 24, "Chose not to fight", "戦いに選抜されなかった"),
    0x001B2DD8: Data(DataType.String, 24, "Freeze on Unit-01 rescinded", "初号機の凍結解除した"),
    0x001B2DF0: Data(DataType.String, 28, "Dispatch was ordered during hospitalization", "入院時に出動を命じられた"),
    0x001B2E0C: Data(DataType.String, 24, "Raised objections against strategic details", "作戦内容に異を唱えた"),
    0x001B2E24: Data(DataType.String, 40, "Pilots selected to fight Israfel", "イスラフェル戦でパイロットに選抜された"),
    0x001B2E4C: Data(DataType.String, 32, "Pilot died via unplayable battle", "非プレイ戦闘でパイロット死亡"),
    0x001B2E6C: Data(DataType.String, 24, "Put through the wringer by Angel", "使徒に痛い目にあった"),
    0x001B2E84: Data(DataType.String, 24, "Angel lightly injured", "使徒に軽傷を負わされた"),
    0x001B2E9C: Data(DataType.String, 24, "Angel injured", "使徒に怪我を負わされた"),
    0x001B2EB4: Data(DataType.String, 28, "Angel gravely injured", "使徒に大怪我を負わされた"),
    0x001B2ED0: Data(DataType.String, 24, "Mind peeked at by Angel", "使徒に心をのぞかれた"),
    0x001B2EE8: Data(DataType.String, 28, "Mind trampled by Angel", "使徒に心を踏みにじられた"),
    0x001B2F04: Data(DataType.String, 28, "Mind toyed with by Angel", "使徒に心をもてあそばれた"),
    0x001B2F20: Data(DataType.String, 20, "Mind defiled by Angel", "使徒に心を汚された"),
    0x001B2F34: Data(DataType.String, 16, "Rejected the instructions", "指示を拒否した"),
    0x001B2F60: Data(DataType.String, 12, "grateful", "感謝した"),
    0x001B2F6C: Data(DataType.String, 16, "have a good impression", "好感を持った"),
    0x001B2F7C: Data(DataType.String, 16, "refreshed", "すっきりした"),
    0x001B2F8C: Data(DataType.String, 12, "good vibes", "いい感じ"),
    0x001B2F98: Data(DataType.String, 12, "happy", "嬉しかった"),
    0x001B2FA4: Data(DataType.String, 16, "excited", "ドキドキした"),
    0x001B2FB4: Data(DataType.String, 16, "turned on", "ムラムラした"),
    0x001B2FC4: Data(DataType.String, 16, "very skilled", "美味しかった"),
    0x001B2FD4: Data(DataType.String, 12, "satisfied", "満足した"),
    0x001B2FE0: Data(DataType.String, 12, "had fun", "楽しかった"),
    0x001B2FEC: Data(DataType.String, 16, "feel good", "気持ち良かった"),
    0x001B2FFC: Data(DataType.String, 16, "embarassed", "恥ずかしかった"),
    0x001B300C: Data(DataType.String, 12, "admire", "感心した"),
    0x001B3018: Data(DataType.String, 8, "like", "好きだ"),
    0x001B3020: Data(DataType.String, 12, "love", "愛していた"),
    0x001B302C: Data(DataType.String, 16, "want to value", "大切にしたい"),
    0x001B303C: Data(DataType.String, 12, "relieved", "安心した"),
    0x001B3048: Data(DataType.String, 12, "incredible", "信じられた"),
    0x001B3054: Data(DataType.String, 12, "honored", "尊敬した"),
    0x001B3060: Data(DataType.String, 12, "hopeful", "期待した"),
    0x001B306C: Data(DataType.String, 16, "got a sense of mastery", "優越感を得た"),
    0x001B307C: Data(DataType.String, 8, "normal", "普通"),
    0x001B3084: Data(DataType.String, 8, "surprised", "驚いた"),
    0x001B308C: Data(DataType.String, 8, "troubled", "困った"),
    0x001B3094: Data(DataType.String, 8, "hesitant", "迷った"),
    0x001B309C: Data(DataType.String, 12, "tense", "緊張した"),
    0x001B30A8: Data(DataType.String, 12, "worried", "心配した"),
    0x001B30B4: Data(DataType.String, 12, "serves them right", "いい気味だ"),
    0x001B30C0: Data(DataType.String, 16, "pathetic", "かわいそうだ"),
    0x001B30D0: Data(DataType.String, 16, "awkward", "ぎこちなかった"),
    0x001B30E0: Data(DataType.String, 20, "indifferent", "どうでもよかった"),
    0x001B30F4: Data(DataType.String, 20, "wonder what's wrong", "どうしたんだろう"),
    0x001B3108: Data(DataType.String, 20, "don't really get it", "よく分からなかった"),
    0x001B311C: Data(DataType.String, 8, "angry", "怒った"),
    0x001B3124: Data(DataType.String, 8, "offensive", "不快だ"),
    0x001B312C: Data(DataType.String, 8, "exhausted", "疲れた"),
    0x001B3134: Data(DataType.String, 12, "huffy", "ムッとした"),
    0x001B3140: Data(DataType.String, 12, "sad", "哀しかった"),
    0x001B314C: Data(DataType.String, 12, "obscene", "いやらしい"),
    0x001B3158: Data(DataType.String, 12, "disgusting", "ヘドがでる"),
    0x001B3164: Data(DataType.String, 12, "unpleasant", "まずかった"),
    0x001B3170: Data(DataType.String, 12, "discontent", "不満だった"),
    0x001B317C: Data(DataType.String, 16, "boring", "つまらなかった"),
    0x001B318C: Data(DataType.String, 16, "disgusted", "気持ち悪かった"),
    0x001B319C: Data(DataType.String, 16, "want to die", "死にたくなった"),
    0x001B31AC: Data(DataType.String, 12, "stunned", "あきれた"),
    0x001B31B8: Data(DataType.String, 8, "Dislike", "嫌いだ"),
    0x001B31C0: Data(DataType.String, 12, "Hateful", "憎かった"),
    0x001B31CC: Data(DataType.String, 20, "Ready to give up", "捨ててしまいたい"),
    0x001B31E0: Data(DataType.String, 16, "Uneasy", "不安を感じた"),
    0x001B31F0: Data(DataType.String, 20, "Incredible", "信じられなかった"),
    0x001B3204: Data(DataType.String, 12, "Contemptuous", "軽蔑した"),
    0x001B3210: Data(DataType.String, 16, "Dejected", "がっかりした"),
    0x001B3220: Data(DataType.String, 12, "Frustrated", "悔しかった"),
    0x001B322C: Data(DataType.String, 16, "Refreshed", "スカっとした"),
    0x001B323C: Data(DataType.String, 12, "In pain", "痛かった"),
    0x001B3248: Data(DataType.String, 12, "Scared", "恐かった"),
    0x001B3254: Data(DataType.String, 12, "Debug+", "デバッグ＋"),
    0x001B3260: Data(DataType.String, 12, "Debug-", "デバッグ−"),
    0x001B326C: Data(DataType.String, 20, "sparked my fighting spirit", "闘争心に火が付いた"),
    0x001B328C: Data(DataType.String, 8, "Shinji", "シンジ"),
    0x001B3294: Data(DataType.String, 8, "Asuka", "アスカ"),
    0x001B329C: Data(DataType.String, 8, "Rei", "レイ"),
    0x001B32A4: Data(DataType.String, 8, "Misato", "ミサト"),
    0x001B32AC: Data(DataType.String, 12, "Gendo", "ゲンドウ"),
    0x001B32B8: Data(DataType.String, 8, "Fuyutsuki", "冬月"),
    0x001B32C0: Data(DataType.String, 8, "Ritsuko", "リツコ"),
    0x001B32C8: Data(DataType.String, 8, "Maya", "マヤ"),
    0x001B32D0: Data(DataType.String, 8, "Hyuga", "日向"),
    0x001B32D8: Data(DataType.String, 8, "Aoba", "青葉"),
    0x001B32E0: Data(DataType.String, 8, "Kaji", "加持"),
    0x001B32E8: Data(DataType.String, 8, "Hikari", "ヒカリ"),
    0x001B32F0: Data(DataType.String, 8, "Toji", "トウジ"),
    0x001B32F8: Data(DataType.String, 12, "Kensuke", "ケンスケ"),
    0x001B3304: Data(DataType.String, 8, "Kaworu", "カヲル"),
    0x001B330C: Data(DataType.String, 12, "Pen Pen", "ペンペン"),
    0x001B3318: Data(DataType.String, 4, "+", "＋"),
    0x001B331C: Data(DataType.String, 4, "-", "−"),
    0x001B334C: Data(DataType.String, 8, "Unit-00", "零号機"),
    0x001B3354: Data(DataType.String, 8, "Unit-01", "初号機"),
    0x001B335C: Data(DataType.String, 8, "Unit-02", "弐号機"),
    0x001B3364: Data(DataType.String, 8, "Unit-03", "参号機"),
    0x001B336C: Data(DataType.String, 8, "Unit-04", "四号機"),
    0x001B3374: Data(DataType.String, 12, "Sachiel", "サキエル"),
    0x001B3380: Data(DataType.String, 16, "Shamshel", "シャムシエル"),
    0x001B3390: Data(DataType.String, 12, "Ramiel", "ラミエル"),
    0x001B339C: Data(DataType.String, 16, "Israfel", "イスラフェル"),
    0x001B33AC: Data(DataType.String, 12, "Matarael", "マトリエル"),
    0x001B33B8: Data(DataType.String, 16, "Bardiel", "バルディエル"),
    0x001B33C8: Data(DataType.String, 12, "Zeruel", "ゼルエル"),
    0x001B33D4: Data(DataType.String, 16, "Armisael", "アルミサエル"),
    0x001B33E4: Data(DataType.String, 12, "Enemy Eva", "敵エヴァ"),
    0x001B33F0: Data(DataType.String, 8, "M.P. Eva", "量産機"),
    0x001B33F8: Data(DataType.String, 8, "J.A. 2", "ＪＡ２"),
    0x001B3400: Data(DataType.String, 8, "U.N. Forces", "国連軍"),
    0x001B3408: Data(DataType.String, 8, "Nerv", "ネルフ"),
    0x001B3410: Data(DataType.String, 12, "Armament Building", "兵装ビル"),
    0x001B341C: Data(DataType.String, 12, "Defense Facility", "防御施設"),
    0x001B3428: Data(DataType.String, 12, "Power Building", "電源ビル"),
    0x001B3434: Data(DataType.String, 12, "Armory Building", "武器庫ビル"),
    0x001B3440: Data(DataType.String, 12, "Gaghiel", "ガギエル"),
    0x001B344C: Data(DataType.String, 16, "Sandalphon", "サンダルフォン"),
    0x001B345C: Data(DataType.String, 16, "Sahaquiel", "サハクィエル"),
    0x001B346C: Data(DataType.String, 12, "Ireul", "イロウル"),
    0x001B3478: Data(DataType.String, 12, "Leliel", "レリエル"),
    0x001B3484: Data(DataType.String, 12, "Arael", "アラエル"),
    0x001B3490: Data(DataType.String, 12, "Tabris", "ダブリス"),
    0x001B349C: Data(DataType.String, 8, "J.A.", "ＪＡ"),
    0x001B34A4: Data(DataType.String, 16, "Tokyo-3", "第３新東京市"),
    0x001B34B4: Data(DataType.String, 12, "Cursor", "カーソル"),
    0x001B34C0: Data(DataType.String, 16, "Israfel A&B", "イスラフェルＷ"),
    0x001B34D0: Data(DataType.String, 8, "Both Evas", "両機"),
    0x001B34D8: Data(DataType.String, 12, "New Unit-00", "新零号機"),
    0x001B34E4: Data(DataType.String, 12, "New Unit-01", "新初号機"),
    0x001B34F0: Data(DataType.String, 12, "New Unit-02", "新弐号機"),
    0x001B34FC: Data(DataType.String, 16, "Sachiel (Scenario 1)", "サキエル(ｼﾅﾘｵ1)"),
    0x001B350C: Data(DataType.String, 20, "Sachiel (Scenario 3)", "サキエル(ｼﾐｭﾚｰｼｮﾝ)"),
    0x001B3520: Data(DataType.String, 20, "Shamshel (Scenario 1)", "シャムシェル(ｼﾅﾘｵ1)"),
    0x001B3534: Data(DataType.String, 16, "Sachiel (Scenario 5)", "サキエル(ｼﾅﾘｵ5)"),
    0x001B3544: Data(DataType.String, 16, "M.P. Eva (Post-Revival)", "量産機(復活後)"),
    0x001B3698: Data(DataType.String, 8, "???", "？？？"),
    0x001B3750: Data(DataType.String, 8, "......", "………"),
    0x001B3810: Data(DataType.String, 12, "Shinji Ikari", "碇シンジ"),
    0x001B381C: Data(DataType.String, 28, "Asuka Soryu Langley", "惣流・アスカ・ラングレー"),
    0x001B3838: Data(DataType.String, 12, "Rei Ayanami", "綾波レイ"),
    0x001B3844: Data(DataType.String, 12, "Misato Katsuragi", "葛城ミサト"),
    0x001B3850: Data(DataType.String, 12, "Gendo Ikari", "碇ゲンドウ"),
    0x001B385C: Data(DataType.String, 16, "Kozo Fuyutsuki", "冬月コウゾウ"),
    0x001B386C: Data(DataType.String, 12, "Ritsuko Akagi", "赤木リツコ"),
    0x001B3878: Data(DataType.String, 12, "Maya Ibuki", "伊吹マヤ"),
    0x001B3884: Data(DataType.String, 12, "Makoto Hyuga", "日向マコト"),
    0x001B3890: Data(DataType.String, 12, "Shigeru Aoba", "青葉シゲル"),
    0x001B389C: Data(DataType.String, 16, "Ryoji Kaji", "加持リョウジ"),
    0x001B38AC: Data(DataType.String, 12, "Hikari Horaki", "洞木ヒカリ"),
    0x001B38B8: Data(DataType.String, 12, "Toji Suzuhara", "鈴原トウジ"),
    0x001B38C4: Data(DataType.String, 16, "Kensuke Aida", "相田ケンスケ"),
    0x001B38D4: Data(DataType.String, 12, "Kaworu Nagisa", "渚カヲル"),
    0x001B38E0: Data(DataType.String, 12, "Pen Pen", "ペンペン"),
    0x001B38EC: Data(DataType.String, 16, "Male Staff", "男性スタッフ"),
    0x001B38FC: Data(DataType.String, 16, "Female Staff", "女性スタッフ"),
    0x001B390C: Data(DataType.String, 8, "Clerk", "店員"),
    0x001B391C: Data(DataType.String, 16, "Shinji Ikari", "　　　碇シンジ"),
    0x001B392C: Data(DataType.String, 28, "Asuka Soryu\nLangley", "惣流・アスカ\n　・ラングレー"),
    0x001B3948: Data(DataType.String, 16, "Rei Ayanami", "　　　綾波レイ"),
    0x001B3958: Data(DataType.String, 16, "Misato Katsuragi", "　　葛城ミサト"),
    0x001B3968: Data(DataType.String, 16, "Gendo Ikari", "　　碇ゲンドウ"),
    0x001B3978: Data(DataType.String, 16, "Kozo Fuyutsuki", "　冬月コウゾウ"),
    0x001B3988: Data(DataType.String, 16, "Ritsuko Akagi", "　　赤木リツコ"),
    0x001B3998: Data(DataType.String, 16, "Maya Ibuki", "　　　伊吹マヤ"),
    0x001B39A8: Data(DataType.String, 16, "Makoto Hyuga", "　　日向マコト"),
    0x001B39B8: Data(DataType.String, 16, "Shigeru Aoba", "　　青葉シゲル"),
    0x001B39C8: Data(DataType.String, 16, "Ryoji Kaji", "　加持リョウジ"),
    0x001B39D8: Data(DataType.String, 16, "Hikari Horaki", "　　洞木ヒカリ"),
    0x001B39E8: Data(DataType.String, 16, "Toji Suzuhara", "　　鈴原トウジ"),
    0x001B39F8: Data(DataType.String, 16, "Kensuke Aida", "　相田ケンスケ"),
    0x001B3A08: Data(DataType.String, 16, "Kaworu Nagisa", "　　　渚カヲル"),
    0x001B3A18: Data(DataType.String, 16, "Pen Pen", "　　　ペンペン"),
    0x001B3A28: Data(DataType.String, 16, "Male Staff", "　男性スタッフ"),
    0x001B3A38: Data(DataType.String, 16, "Female Staff", "　女性スタッフ"),
    0x001B3A48: Data(DataType.String, 16, "Clerk", "　　　　　店員"),
    0x001B3A58: Data(DataType.String, 24, "Keel Lorenz", "キール\n　・ローレンツ"),
    0x001B3A70: Data(DataType.String, 16, "Shiro Tokita", "　　時田シロウ"),
    0x001B3A80: Data(DataType.String, 16, "Yui Ikari", "　　　　碇ユイ"),
    0x001B3A90: Data(DataType.String, 16, "Female Announcer", "　　　女子アナ"),
    0x001B3AA0: Data(DataType.String, 16, "T.V. Talent", "テレビタレント"),
    0x001B3AB0: Data(DataType.String, 16, "Kensuke's Father", "　ケンスケの父"),
    0x001B3AC0: Data(DataType.String, 16, "Toji's Sister", "　　トウジの妹"),
    0x001B3AD0: Data(DataType.String, 16, "Nursing Staff", "　介護スタッフ"),
    0x001B3AE0: Data(DataType.String, 16, "Psychiatrist", "　　　精神科医"),
    0x001B3AF0: Data(DataType.String, 16, "Baby's Mother", "　　　幼子の母"),
    0x001B3B00: Data(DataType.String, 16, "Naoko Akagi", "　　赤木ナオコ"),
    0x001B3B10: Data(DataType.String, 16, "Female Classmate", "　クラスの女子"),
    0x001B3B20: Data(DataType.String, 16, "Announcement", "　　アナウンス"),
    0x001B3B30: Data(DataType.String, 16, "Teruo Kato", "　　加藤テルオ"),
    0x001B3B40: Data(DataType.String, 16, "Committeeman A", "　　　委員会Ａ"),
    0x001B3B50: Data(DataType.String, 16, "Committeeman B", "　　　委員会Ｂ"),
    0x001B3B60: Data(DataType.String, 16, "Committeeman C", "　　　委員会Ｃ"),
    0x001B3B70: Data(DataType.String, 16, "Committeeman D", "　　　委員会Ｄ"),
    0x001B3B80: Data(DataType.String, 16, "Seele 02", "　　　［０２］"),
    0x001B3B90: Data(DataType.String, 16, "Seele 03", "　　　［０３］"),
    0x001B3BA0: Data(DataType.String, 16, "Seele 04", "　　　［０４］"),
    0x001B3BB0: Data(DataType.String, 16, "Seele 05", "　　　［０５］"),
    0x001B3BC0: Data(DataType.String, 16, "Seele 06", "　　　［０６］"),
    0x001B3BD0: Data(DataType.String, 16, "Seele 09", "　　　［０９］"),
    0x001B3BE0: Data(DataType.String, 16, "JSSDF Staff", "　　　戦自隊員"),
    0x001B3BF0: Data(DataType.String, 16, "Radio Voice", "　　　無線音声"),
    0x001B3C00: Data(DataType.String, 16, "Local Announcement", "館内アナウンス"),
    0x001B3C10: Data(DataType.String, 16, "Girlfriends", "　　　　女友達"),
    0x001B3C20: Data(DataType.String, 16, "Matsushiro Staff", "　　　松代職員"),
    0x001B3C30: Data(DataType.String, 16, "Seele 01", "　　　［０１］"),
    0x001B3C40: Data(DataType.String, 16, "Shinji's Shadow", "　　シンジの影"),
    0x001B3C50: Data(DataType.String, 16, "Asuka's Shadow", "　　アスカの影"),
    0x001B3C60: Data(DataType.String, 16, "Rei's Shadow", "　　　レイの影"),
    0x001B3C70: Data(DataType.String, 16, "Toji's Shadow", "　　トウジの影"),
    0x001B3C80: Data(DataType.String, 16, "Kaworu's Shadow", "　　カヲルの影"),
    0x001B3C90: Data(DataType.String, 16, "        ???", "　　　　？？？"),
    0x001B3CA0: Data(DataType.String, 16, "Evacuation Announcement", "避難アナウンス"),
    0x001B3CB0: Data(DataType.String, 16, "Street Announcement", "街頭アナウンス"),
    0x001B3CC0: Data(DataType.String, 16, "Host", "　　　　司会者"),
    0x001B3CD0: Data(DataType.String, 16, "Teacher", "　　　　　教師"),
    0x001B3CE0: Data(DataType.String, 16, "School Broadcast", "　　　校内放送"),
    0x001B3CF0: Data(DataType.String, 16, "Receptionist", "　　　　受付人"),
    0x001B3D00: Data(DataType.String, 16, "Nurse", "　　　　看護師"),
    0x001B3D10: Data(DataType.String, 16, "Girl", "　　　　　少女"),
    0x001B3D20: Data(DataType.String, 16, "T.V. Commercial", "　　テレビＣＭ"),
    0x001B3D30: Data(DataType.String, 16, "Delivery Man", "　　　　宅配人"),
    0x001B3D40: Data(DataType.String, 16, "Controller", "　　　　管制員"),
    0x001B3D50: Data(DataType.String, 16, "Naval Officer", "　　　海軍士官"),
    0x001B3D60: Data(DataType.String, 16, "Intelligence Agent", "　　　諜報部員"),
    0x001B3D70: Data(DataType.String, 24, "Answering Machine\nAnnouncement", "　留守電\n　　アナウンス"),
    0x001B3D88: Data(DataType.String, 16, "Kazuki Anami", "　　阿南カズキ"),
    0x001B3D98: Data(DataType.String, 16, "Tadamitsu Otsubo", "　大坪タダミツ"),
    0x001B3DA8: Data(DataType.String, 16, "Mikio Shimaki", "　　島木ミキオ"),
    0x001B3DB8: Data(DataType.String, 16, "Yoji Uozumi", "　　魚住ヨウジ"),
    0x001B3DC8: Data(DataType.String, 16, "Lordi", "　　　ローディ"),
    0x001B3DD8: Data(DataType.String, 32, "Kyoko Soryu\nZeppelin", "惣流・キョウコ\n・ツェッペリン"),
    0x001B3DF8: Data(DataType.String, 16, "Everyone", "　　　　　全員"),
    0x001B3E08: Data(DataType.String, 28, "Emergency Phone\nAnnouncement", "　非常電話\n　　アナウンス"),
    0x001B3E24: Data(DataType.String, 16, "Street T.V.", "　　街頭テレビ"),
    0x001B3E34: Data(DataType.String, 12, "Toji's Mother", "トウジの母"),
    0x001B3E40: Data(DataType.String, 16, "Gendo Rokubungi", "六分儀ゲンドウ"),
    0x001B3E7C: Data(DataType.String, 8, "Yes", "は　い"),
    0x001B3E84: Data(DataType.String, 8, "No", "いいえ"),
    0x001B421C: Data(DataType.String, 16, "Snack Food", "スナック菓子"),
    0x001B422C: Data(DataType.String, 44, "Scantly restores hunger stat when used.", "使うと、体調の空腹をわずかに回復できます。"),
    0x001B4258: Data(DataType.String, 40, "Salt-free, low-calorie snack. Reduces hunger.", "カロリー控えめ減塩スナック。空腹を回復"),
    0x001B4280: Data(DataType.String, 24, "A little less hungry!", "空腹が少し回復した！"),
    0x001B4298: Data(DataType.String, 16, "Easy Bento Box", "コンビニ弁当"),
    0x001B42A8: Data(DataType.String, 36, "Restores hunger stat when used.", "使うと、体調の空腹を回復できます。"),
    0x001B42CC: Data(DataType.String, 40, "Super-typical pre-made bento box. Reduces hunger.", "ごくありふれたコンビニ弁当。空腹を回復"),
    0x001B42F4: Data(DataType.String, 24, "Much less hungry!", "空腹がかなり回復した！"),
    0x001B430C: Data(DataType.String, 12, "Pastry", "菓子パン"),
    0x001B4318: Data(DataType.String, 40, "Slightly restores hunger stat when used.", "使うと、体調の空腹を少し回復できます。"),
    0x001B4340: Data(DataType.String, 40, "Chocolate-covered croissant. Reduces hunger.", "チョコを塗ったクロワッサン。空腹を回復"),
    0x001B4368: Data(DataType.String, 20, "Recovered from hunger!", "空腹が回復した！"),
    0x001B437C: Data(DataType.String, 16, "Sandwich", "サンドイッチ"),
    0x001B438C: Data(DataType.String, 40, "A ham and lettuce sandwich. Reduces hunger.", "ハムとレタスのサンドイッチ。空腹を回復"),
    0x001B43B4: Data(DataType.String, 24, "Instant Ramen", "インスタントラーメン"),
    0x001B43CC: Data(DataType.String, 40, "Crudely packaged instant noodles. Reduces hunger.", "下品なパッケージの即席麺。空腹を回復"),
    0x001B43F4: Data(DataType.String, 16, "Shortcake", "ショートケーキ"),
    0x001B4404: Data(DataType.String, 40, "A plain shortcake. Reduces hunger.", "飾り気の無いショートケーキ。空腹を回復"),
    0x001B442C: Data(DataType.String, 8, "Custard Pudding", "プリン"),
    0x001B4434: Data(DataType.String, 40, "Custard pudding that used plenty of eggs. Reduces hunger.", "卵をたっぷり使ったプリン。空腹を回復"),
    0x001B445C: Data(DataType.String, 24, "Restored a little stamina!", "体力が少し回復した！"),
    0x001B4474: Data(DataType.String, 12, "Juice", "ジュース"),
    0x001B4480: Data(DataType.String, 36, "Restores thirst stat when used.", "使うと、体調の水分を回復できます。"),
    0x001B44A4: Data(DataType.String, 40, "Popular commodity advertised recently on TV. Reduces thirst.", "最近テレビＣＭが盛んな商品。水分を回復"),
    0x001B44CC: Data(DataType.String, 16, "Quenched your thirst!", "喉が潤った！"),
    0x001B44DC: Data(DataType.String, 12, "Coffee", "コーヒー"),
    0x001B44E8: Data(DataType.String, 36, "Low-sugar canned coffee. Reduces thirst.", "砂糖控えめの缶コーヒー。水分を回復"),
    0x001B450C: Data(DataType.String, 8, "Green Tea", "緑茶"),
    0x001B4514: Data(DataType.String, 40, "Canned tea that has difficult kanji in its name. Reduces thirst.", "難しい漢字タイトルの缶茶。水分を回復"),
    0x001B453C: Data(DataType.String, 8, "Beer", "ビール"),
    0x001B4544: Data(DataType.String, 40, "BOA Beer that goes down real smooth. Reduces thirst.", "喉ごしごっくりＢＯＡビール。水分を回復"),
    0x001B456C: Data(DataType.String, 8, "Watermelon", "スイカ"),
    0x001B4574: Data(DataType.String, 48, "Restores hunger and thirst stats a little when used.", "使うと、体調の空腹と水分を少し回復できます。"),
    0x001B45A4: Data(DataType.String, 40, "Watermelon from the produce department. Reduces hunger.", "生鮮食料品コーナーのスイカ。空腹を回復"),
    0x001B45CC: Data(DataType.String, 8, "Newspaper", "新聞"),
    0x001B45D4: Data(DataType.String, 44, "When in one's possession, raises clerical skill by 1.", "所持していると、事務技能が＋１されます。"),
    0x001B4600: Data(DataType.String, 32, "Daily METI newspaper, covering political science and economics.", "政治経済充実の、日日経産新聞"),
    0x001B4620: Data(DataType.String, 36, "This item can't be used here.", "このアイテムは、ここでは使えない。"),
    0x001B4644: Data(DataType.String, 8, "Magazine", "週刊誌"),
    0x001B464C: Data(DataType.String, 44, "When in one's possession, raises information skill by 1.", "所持していると、情報技能が＋１されます。"),
    0x001B4678: Data(DataType.String, 16, "Weekly general information magazine.", "週刊総合情報誌"),
    0x001B4688: Data(DataType.String, 8, "Manga", "マンガ"),
    0x001B4690: Data(DataType.String, 84, "If owned by a non-player character,\nmakes it easier for hesitant thoughts to be chosen.", "プレイヤー以外のキャラが所持すると、\n何もしたくない思考が選択されやすくなります。"),
    0x001B46E4: Data(DataType.String, 24, "A crisply illustrated manga magazine.", "絵が小綺麗な漫画雑誌"),
    0x001B46FC: Data(DataType.String, 24, "Travel Guidebook", "トラベルガイドブック"),
    0x001B4714: Data(DataType.String, 84, "If owned by a non-player character,\nmakes it easier for thoughts valuing friendship to be chosen.", "プレイヤー以外のキャラが所持すると、\n友情を大切にする思考が選択されやすくなります。"),
    0x001B4768: Data(DataType.String, 40, "An extensive introductory travel guidebook,\nproviding both local and overseas coverage.", "近場から海外まで、手広い紹介の旅行本"),
    0x001B4790: Data(DataType.String, 12, "Necklace", "ネックレス"),
    0x001B479C: Data(DataType.String, 76, "If owned by a non-player character,\nmakes it easier for romantic thoughts to be chosen.", "プレイヤー以外のキャラが所持すると、\n恋愛の思考が選択されやすくなります。"),
    0x001B47E8: Data(DataType.String, 24, "A fashion accessory.", "おしゃれ用アクセサリー"),
    0x001B4800: Data(DataType.String, 12, "Handkerchief", "ハンカチ"),
    0x001B480C: Data(DataType.String, 40, "Restores bathing stat a little when used.", "使うと、体調の風呂を少し回復できます。"),
    0x001B4834: Data(DataType.String, 16, "An etiquette item.", "エチケット用品"),
    0x001B4844: Data(DataType.String, 24, "Wiped hands with handkerchief!", "ハンカチで手を拭いた！"),
    0x001B485C: Data(DataType.String, 20, "Pocket Tissues", "ポケットティッシュ"),
    0x001B4870: Data(DataType.String, 44, "Makes you feel a little refreshed when used.", "使うと、ちょっぴり爽快な気分になります。"),
    0x001B489C: Data(DataType.String, 20, "For use on the go.", "携帯用ティッシュ"),
    0x001B48B0: Data(DataType.String, 16, "Blew your nose.", "ハナをかんだ。"),
    0x001B48C0: Data(DataType.String, 8, "Eye Drops", "目薬"),
    0x001B48C8: Data(DataType.String, 40, "Restores sleepiness stat a little when used.", "使うと、体調の眠気を少し回復できます。"),
    0x001B48F0: Data(DataType.String, 16, "A stimulating eyewash.", "刺激的な目薬"),
    0x001B4900: Data(DataType.String, 20, "Perked up a little!", "少し目が覚めた！"),
    0x001B4914: Data(DataType.String, 8, "Perfume Bag", "香水袋"),
    0x001B491C: Data(DataType.String, 8, "Hand Mirror", "手鏡"),
    0x001B4924: Data(DataType.String, 88, "If owned by a non-player character,\nmakes them more inclined to want everyone's admiration.", "プレイヤー以外のキャラが所持すると、\nみんなに好かれたい思考が選択されやすくなります。"),
    0x001B497C: Data(DataType.String, 24, "Puts one's grooming in order.", "身だしなみを整えます"),
    0x001B4994: Data(DataType.String, 12, "Cooling Band", "冷却バンド"),
    0x001B49A0: Data(DataType.String, 36, "Restores sleepiness stat when used.", "使うと、体調の眠気を回復できます。"),
    0x001B49C4: Data(DataType.String, 20, "Drives your drowsiness away.", "眠気が吹き飛びます"),
    0x001B49D8: Data(DataType.String, 16, "Perked right up!", "目が覚めた！"),
    0x001B49E8: Data(DataType.String, 20, "Body Spray", "エチケットスプレー"),
    0x001B49FC: Data(DataType.String, 36, "Restores bathing stat when used.", "使うと、体調の風呂を回復できます。"),
    0x001B4A20: Data(DataType.String, 24, "Eliminates bothersome body odor.", "気になる体臭を消します"),
    0x001B4A38: Data(DataType.String, 16, "Suppressed your body odor!", "体臭を抑えた！"),
    0x001B4A48: Data(DataType.String, 16, "Aromatherapy Oil", "アロマオイル"),
    0x001B4A58: Data(DataType.String, 28, "Relieves tension when used.", "使うと、緊張が和らぎます。"),
    0x001B4A74: Data(DataType.String, 44, "Lavender-scented aromatherapy oil.", "ラベンダーの香りのアロマテラピー用オイル"),
    0x001B4AA0: Data(DataType.String, 56, "The smell of lavender permeates... It seems to have a calming effect.\n", "ラベンダーの香りが広がる…。\n気持ちが落ち着くようだ。"),
    0x001B4AD8: Data(DataType.String, 8, "Bathing Powder", "入浴剤"),
    0x001B4AE0: Data(DataType.String, 68, "When in one's possession, slightly boosts how much\none's bathing stat recovers when taking a bath.", "所持していると、体調の風呂の回復効率が、\n入浴時に少しアップします。"),
    0x001B4B24: Data(DataType.String, 28, "Take a bath that feels great.", "気持ち良くお風呂に入れます"),
    0x001B4B40: Data(DataType.String, 12, "Sunglasses", "サングラス"),
    0x001B4B4C: Data(DataType.String, 88, "If owned by a non-player character,\nmakes them more inclined to seek out confidential information.", "プレイヤー以外のキャラが所持すると、\n機密情報を入手する思考が選択されやすくなります。"),
    0x001B4BA4: Data(DataType.String, 8, "Earrings", "ピアス"),
    0x001B4BAC: Data(DataType.String, 88, "If owned by a non-player character,\nmakes them more inclined toward obtaining items.", "プレイヤー以外のキャラが所持すると、\nアイテムを入手する思考が選択されやすくなります。"),
    0x001B4C04: Data(DataType.String, 8, "Ring", "指輪"),
    0x001B4C0C: Data(DataType.String, 8, "Porn Mag", "Ｈな本"),
    0x001B4C14: Data(DataType.String, 72, "If owned by a non-player character,\nmakes dirty thoughts happen more easily.", "プレイヤー以外のキャラが所持すると、\nＨな思考が選択されやすくなります。"),
    0x001B4C5C: Data(DataType.String, 24, "An entertainment magazine with extreme content.", "過激な内容の娯楽雑誌"),
    0x001B4C74: Data(DataType.String, 8, "Reference Book", "参考書"),
    0x001B4C7C: Data(DataType.String, 44, "When in one's possession, raises clerical skill by 10.", "所持していると、事務技能が＋１０されます。"),
    0x001B4CA8: Data(DataType.String, 28, "Full of useful information.", "なかなか便利な知識が満載"),
    0x001B4CC4: Data(DataType.String, 8, "Charm", "お守り"),
    0x001B4CCC: Data(DataType.String, 92, "If owned by a non-player character,\nmakes them more inclined to distance themselves from disliked characters.", "プレイヤー以外のキャラが所持すると、\n嫌いなキャラから離れる思考が選択されやすくなります。"),
    0x001B4D28: Data(DataType.String, 20, "A charm that keeps calamity in check.", "災厄防止のお守り"),
    0x001B4D3C: Data(DataType.String, 12, "SDAT", "ＳＤＡＴ"),
    0x001B4D48: Data(DataType.String, 28, "Cutting-edge audio tape.", "最新型のオーディオテープ"),
    0x001B4D64: Data(DataType.String, 8, "PDA", "ＰＤＡ"),
    0x001B4D6C: Data(DataType.String, 44, "When in one's possession, raises information skill by 10.", "所持していると、情報技能が＋１０されます。"),
    0x001B4D98: Data(DataType.String, 20, "Portable digital assistant.", "携帯情報端末機器"),
    0x001B4DAC: Data(DataType.String, 20, "Teddy Bear", "クマのぬいぐるみ"),
    0x001B4DC0: Data(DataType.String, 28, "An adorable bear plushie.", "かわいいクマのぬいぐるみ"),
    0x001B4DDC: Data(DataType.String, 12, "Mug", "マグカップ"),
    0x001B4DE8: Data(DataType.String, 88, "If owned by a non-player character,\nlets them restore their thirst stat more easily.", "プレイヤー以外のキャラが所持すると、\n体調の水分を回復する思考が選択されやすくなります。"),
    0x001B4E40: Data(DataType.String, 40, "Adorable mug imprinted with a cat logo.", "ネコマークがついた、かわいいグカップ"),
    0x001B4E68: Data(DataType.String, 8, "Camouflage", "迷彩服"),
    0x001B4E70: Data(DataType.String, 84, "If owned by a non-player character,\nmakes them more inclined toward achieving justice. ", "プレイヤー以外のキャラが所持すると、\n正義をなしたい思考が選択されやすくなります。"),
    0x001B4EC4: Data(DataType.String, 16, "Genuine camouflage garb.", "本格的な迷彩服"),
    0x001B4ED4: Data(DataType.String, 12, "Mobile Phone", "携帯電話"),
    0x001B4EE0: Data(DataType.String, 68, "When in one's possession,\ngives access to a command that allows a specific character's location to be confirmed.\n", "所持していると、\n特定キャラの居場所を確認できる行動が起動できます。"),
    0x001B4F24: Data(DataType.String, 32, "You can confirm the whereabouts of a particular individual.", "特定の人の居場所を確認出来ます"),
    0x001B4F44: Data(DataType.String, 12, "Fancy Wallet", "高級財布"),
    0x001B4F50: Data(DataType.String, 84, "If owned by a non-player character,\ninclines them toward enhancing their reputation.", "プレイヤー以外のキャラが所持すると、\n名声を高めたい思考が選択されやすくなります。"),
    0x001B4FA4: Data(DataType.String, 44, "Made from rare leather and imbued with craftsmanship.", "希少な本皮と、職人技術が注ぎ込まれた一品"),
    0x001B4FD0: Data(DataType.String, 12, "Ergonomic Pillow", "安眠マクラ"),
    0x001B4FDC: Data(DataType.String, 68, "When in one's possession, slightly boosts how much\none's sleepiness stat recovers at bedtime.", "所持していると、体調の眠気の回復効率が\n就寝時に少しアップします。"),
    0x001B5020: Data(DataType.String, 16, "Bedding that promotes restive sleep.", "安眠促進寝具"),
    0x001B5030: Data(DataType.String, 20, "Ultimate Black Mamushi Drink", "絶倫黒マムシ飲料"),
    0x001B5044: Data(DataType.String, 52, "Restores hunger stat and increases feelings of perversion when used.", "使うと、体調の空腹を回復し、Ｈな気分が上昇します。"),
    0x001B5078: Data(DataType.String, 20, "An energizing drink.", "元気になる飲み物"),
    0x001B508C: Data(DataType.String, 20, "Started to fret.", "悶々としてきた。"),
    0x001B50A0: Data(DataType.String, 20, "Max Water", "マックスウォーター"),
    0x001B50B4: Data(DataType.String, 76, "Completely restores thirst stat when used,\nbut steadily increases bathroom stat.", "使うと、体調の水分は全回復しますが、\n徐々に体調のＷＣが増加していきます。"),
    0x001B5100: Data(DataType.String, 16, "Hydrating beverage.", "水分補完飲料"),
    0x001B5110: Data(DataType.String, 44, "Slaked your thirst,\nbut now you need to use the bathroom!", "喉は潤ったけど、\nトイレに行きたくなった！"),
    0x001B513C: Data(DataType.String, 12, "Cozy Z", "快適ゼット"),
    0x001B5148: Data(DataType.String, 52, "Reduces sleepiness stat and leaves you feeling refreshed when used.", "使うと、体調の空腹と眠気を回復し、爽快になります。"),
    0x001B517C: Data(DataType.String, 16, "A revitalizing beverage.", "疲労回復飲料"),
    0x001B518C: Data(DataType.String, 44, "Stamina and sleepiness restored --\nyou're feeling good!", "体力と眠気が回復し、\n快適な気分になった！"),
    0x001B51B8: Data(DataType.String, 20, "Sports Drink", "スポーツドリンク"),
    0x001B51CC: Data(DataType.String, 56, "Restores hunger and thirst stats and\nstabilizes mood when used.", "使うと、体調の空腹と水分を回復し、\n気分は落ち着きます。"),
    0x001B5204: Data(DataType.String, 24, "A soothing drink.", "気持ちが落ち着く飲み物"),
    0x001B521C: Data(DataType.String, 44, "Restored a little stamina and put you at ease!", "体力が少し回復して、\n気持ちも落ち着いた！"),
    0x001B5248: Data(DataType.String, 16, "Cry Drink", "クライドリンク"),
    0x001B5258: Data(DataType.String, 60, "Restores thirst stat but puts one\nin a crappy mood when used.", "使うと、体調の水分は回復しますが、\n不快な気分になります。"),
    0x001B5294: Data(DataType.String, 28, "A drink that makes one's mood unpleasant.", "不快な気分になれる飲み物"),
    0x001B52B0: Data(DataType.String, 24, "You feel a bit down...", "ちょっとヘコんだ…。"),
    0x001B52C8: Data(DataType.String, 20, "Vulcan Juice", "ヴァルカンジュース"),
    0x001B52DC: Data(DataType.String, 64, "Reduces thirst but leaves one feeling\nirritated when used.", "使うと、体調の水分は回復しますが、\n腹立たしい気分になります。"),
    0x001B531C: Data(DataType.String, 32, "A drink that causes aggravated mood.", "腹立たしい気分になれる飲み物"),
    0x001B533C: Data(DataType.String, 24, "Rage started building inside you!", "怒りが込み上げてきた！"),
    0x001B5354: Data(DataType.String, 20, "Hedgehog X", "ハリネズミエキス"),
    0x001B5368: Data(DataType.String, 60, "Restores thirst stat but puts one in\na negative mood when used.", "使うと、体調の水分は回復しますが、\n消極的な気分になります。"),
    0x001B53A4: Data(DataType.String, 28, "A drink that brings on passivity and pessimism.", "消極的な気分になれる飲み物"),
    0x001B53C0: Data(DataType.String, 24, "You got a bad feeling...", "嫌な気分になった…。"),
    0x001B53D8: Data(DataType.String, 16, "Horror Drink", "ホラードリンク"),
    0x001B53E8: Data(DataType.String, 60, "Restores thirst stat but induces a sense of caution when used.", "使うと、体調の水分は回復しますが、\n警戒的な気分になります。"),
    0x001B5424: Data(DataType.String, 20, "A drink that heightens wariness.", "警戒感が増す飲み物"),
    0x001B5438: Data(DataType.String, 24, "Started tensing up for some reason.", "なんか緊張してきた。"),
    0x001B5450: Data(DataType.String, 16, "Uncensored Report", "未検閲の報告書"),
    0x001B5460: Data(DataType.String, 68, "When used, one can obtain general\nor, rarely, non-public info.", "使うと、一般情報か、\nまれに非公開情報を入手することが出来る書類。"),
    0x001B54A4: Data(DataType.String, 8, "Nothing", "なし"),
    0x001B54AC: Data(DataType.String, 32, "Didn't learn anything useful.", "有益な情報は得られなかった。"),
    0x001B54CC: Data(DataType.String, 12, "Top Secret Report", "極秘報告書"),
    0x001B54D8: Data(DataType.String, 76, "When used, one can obtain general,\nnon-public, or, rarely,\nin-depth info.", "使うと、一般情報か非公開情報、\nまれに最深度情報を入手することが出来る書類。"),
    0x001B5524: Data(DataType.String, 12, "Confidential Report", "機密報告書"),
    0x001B5530: Data(DataType.String, 60, "When used, one can obtain\nnon-public or in-depth info.", "使うと、非公開情報か\n最深度情報を入手することが出来る書類。"),
    0x001B556C: Data(DataType.String, 20, "Nerv Staff I.D.", "ネルフスタッフＩＤ"),
    0x001B5580: Data(DataType.String, 28, "A Nerv staff I.D. card.", "ネルフ職員のＩＤカード。"),
    0x001B559C: Data(DataType.String, 20, "Senior Nerv Staff I.D.", "上級ネルフ職員ＩＤ"),
    0x001B55B0: Data(DataType.String, 32, "A senior Nerv staff I.D. card.", "上級ネルフ職員のＩＤカード。"),
    0x001B55D0: Data(DataType.String, 16, "Special Forged I.D.", "特殊偽造ＩＤ"),
    0x001B55E0: Data(DataType.String, 24, "An I.D. card that was forged.", "偽造されたＩＤカード。"),
    0x001B55F8: Data(DataType.String, 12, "Seele I.D.", "ゼーレＩＤ"),
    0x001B5604: Data(DataType.String, 28, "A Seele-exclusive I.D. card.", "ゼーレ専用のＩＤカード。"),
    0x001B5620: Data(DataType.String, 16, "Kyoto Business Trip Manifest", "京都出張計画書"),
    0x001B5630: Data(DataType.String, 76, "Business trip plans were forged to obtain\n non-public information\nregarding Marduk Institute.", "マルドゥック機関に関する最深度情報を\n入手するために偽造された出張計画書。"),
    0x001B567C: Data(DataType.String, 64, "Head to Nerv while you have this\nitem.", "このアイテムを所持した状態で、\nネルフ施設に移動してください。"),
    0x001B56BC: Data(DataType.String, 20, "2nd Branch Inspection Manifest", "第２支部視察計画書"),
    0x001B56D0: Data(DataType.String, 64, "Business trip plans were forged to obtain\n non-public information\nregarding Σ Engine.", "Σ機関に関する非公開情報を\n入手するために偽造された出張計画書。"),
    0x001B5710: Data(DataType.String, 16, "Antarctic Inspection Manifest", "南極視察計画書"),
    0x001B5720: Data(DataType.String, 72, "Business trip plans were forged to obtain\n non-public information\nregarding Spear of Longinus.", "ロンギヌスの槍に関する非公開情報を\n入手するために偽造された出張計画書。"),
    0x001B5768: Data(DataType.String, 20, "Ogasawara Business Trip Manifest", "小笠原出張計画書"),
    0x001B577C: Data(DataType.String, 72, "Business trip plans were forged to obtain\n non-public information\nregarding First Ancestral Race.", "第１始祖民族に関する非公開情報を\n入手するために偽造された出張計画書。"),
    0x001B57C4: Data(DataType.String, 20, "Germany Business Trip Manifest", "ドイツ出張計画書"),
    0x001B57D8: Data(DataType.String, 80, "Business trip plans were forged to obtain\n non-public information\nregarding The Second Child.", "セカンド・チルドレンに関する最深度情報を\n入手するために偽造された出張計画書。"),
    0x001B5828: Data(DataType.String, 24, "Special Specs Plugsuit", "特別仕様プラグスーツ"),
    0x001B5840: Data(DataType.String, 24, "Improves battle ability.", "戦闘能力が向上します。"),
    0x001B5858: Data(DataType.String, 16, "Deformed Glasses", "変形した眼鏡"),
    0x001B5868: Data(DataType.String, 80, "If owned by a non-player character,\nlets them select thoughts that raise love\nmore easily.", "プレイヤー以外のキャラが所持すると、\n親愛を上げる思考が選択されやすくなります。"),
    0x001B58B8: Data(DataType.String, 32, "Grasped the Deformed Glasses...", "変形した眼鏡を握り締めた…。"),
    0x001B58D8: Data(DataType.String, 20, "Handmade Miracle Bento Box", "奇跡の手作り弁当"),
    0x001B58EC: Data(DataType.String, 48, "Restores hunger, thirst, and\nsleepiness when used.", "使うと、体調の空腹、水分、眠気を回復できます。"),
    0x001B591C: Data(DataType.String, 36, "Hunger, thirst, drowsiness\nrecovered greatly!", "空腹、水分、眠気が\nかなり回復した！"),
    0x001B5940: Data(DataType.String, 20, "Yummy-Looking Bento Box", "おいしそうなお弁当"),
    0x001B5954: Data(DataType.String, 44, "Restores hunger and thirst\nwhen used.", "使うと、体調の空腹、水分を回復できます。"),
    0x001B5980: Data(DataType.String, 32, "Hunger and thirst\nrecovered greatly!", "空腹、水分がかなり回復した！"),
    0x001B59A0: Data(DataType.String, 20, "Sandwich", "サンドイッチ盛り"),
    0x001B59B4: Data(DataType.String, 12, "Normal Bento Box", "普通の弁当"),
    0x001B59C0: Data(DataType.String, 16, "Leftover Bento Box", "残りもの弁当"),
    0x001B59D0: Data(DataType.String, 16, "Gross-Looking Bento Box", "まずそうな弁当"),
    0x001B59E0: Data(DataType.String, 60, "Restores hunger, but makes\nyou disagreeable when used.", "使うと、体調の空腹を少し回復できますが、\n不快になります。"),
    0x001B5A1C: Data(DataType.String, 44, "Hunger recovered a little\nbut you feel disagreeable!", "空腹が少し回復したが、\n不快な気分になった！"),
    0x001B5A48: Data(DataType.String, 16, "Nightmare Leftovers Bento", "悪夢の残飯弁当"),
    0x001B5A58: Data(DataType.String, 72, "Restores hunger a little\nbut makes you frustrated when used.", "使うと、体調の空腹を少し回復できますが、\nとても悔しい気分になります。"),
    0x001B5AA0: Data(DataType.String, 44, "Hunger recovered a bit,\nbut you feel frustrated!", "空腹が少し回復したが、\n悔しい気分になった！"),
    0x001B5ACC: Data(DataType.String, 20, "Comedy Program Video", "お笑い番組ビデオ"),
    0x001B5AE0: Data(DataType.String, 32, "Funny video, can be\nviewed via TV.", "お笑いビデオ。テレビで観れます"),
    0x001B5B00: Data(DataType.String, 44, "Have to use it somewhere\nwith a video player...", "ビデオデッキのあるところで使わないと…。"),
    0x001B5B2C: Data(DataType.String, 20, "Documentary Video", "ドキュメントビデオ"),
    0x001B5B40: Data(DataType.String, 44, "Documentary video. Can be viewed via TV.", "ドキュメンタリービデオ。テレビで観れます"),
    0x001B5B6C: Data(DataType.String, 20, "Masterpiece Anime Video", "名作アニメビデオ"),
    0x001B5B80: Data(DataType.String, 32, "Anime video.\nCan be viewed via TV.", "アニメビデオ。テレビで観れます"),
    0x001B5BA0: Data(DataType.String, 16, "Period Drama Video", "時代劇ビデオ"),
    0x001B5BB0: Data(DataType.String, 32, "Pereiod drama video.\nCan be viewed via TV.", "時代劇ビデオ。テレビで観れます"),
    0x001B5BD0: Data(DataType.String, 20, "Slightly Pervy Video", "ちょっとＨなビデオ"),
    0x001B5BE4: Data(DataType.String, 40, "A slightly perverted video. Can be viewed via TV.", "ちょっとＨなビデオ。テレビで観れます"),
    0x001B5C0C: Data(DataType.String, 16, "Prize Entry Sticker", "懸賞応募シール"),
    0x001B5C1C: Data(DataType.String, 80, "Collect five to get Mocha-chan!\nC prize is a strap of popular\ncomedian \"Namazume\"!", "５枚集めてモカちゃんをゲット！\nＣ賞は人気お笑い芸人「生爪」の特製ストラップ！！"),
    0x001B5C6C: Data(DataType.String, 36, "Let's stick it in\nthe seal book!", "冷蔵庫のシール台帳に\n貼り付けよう！"),
    0x001B5C90: Data(DataType.String, 20, "Kyoto University Business Trip Manifest", "京都大学出張計画書"),
    0x001B5CA4: Data(DataType.String, 28, "Plan of business trip\nto Kyoto University.", "京都大学への出張計画書。"),
    0x001B5CC0: Data(DataType.String, 20, "Locker 01 Key", "０１番ロッカーの鍵"),
    0x001B5CD4: Data(DataType.String, 36, "Key for a locker at New Hakone-Yumoto Station.", "新箱根湯本駅のロッカーの鍵です。"),
    0x001B5CF8: Data(DataType.String, 20, "Locker 02 Key", "０２番ロッカーの鍵"),
    0x001B5D0C: Data(DataType.String, 20, "Locker 03 Key", "０３番ロッカーの鍵"),
    0x001B5D20: Data(DataType.String, 20, "Locker 04 Key", "０４番ロッカーの鍵"),
    0x001B5D34: Data(DataType.String, 20, "Locker 05 Key", "０５番ロッカーの鍵"),
    0x001B5D48: Data(DataType.String, 20, "Locker 06 Key", "０６番ロッカーの鍵"),
    0x001B5D5C: Data(DataType.String, 20, "Locker 07 Key", "０７番ロッカーの鍵"),
    0x001B5D70: Data(DataType.String, 20, "Locker 08 Key", "０８番ロッカーの鍵"),
    0x001B5D84: Data(DataType.String, 20, "Locker 09 Key", "０９番ロッカーの鍵"),
    0x001B5D98: Data(DataType.String, 20, "Locker 10 Key", "１０番ロッカーの鍵"),
    0x001B5DAC: Data(DataType.String, 20, "Locker 11 Key", "１１番ロッカーの鍵"),
    0x001B5DC0: Data(DataType.String, 20, "Locker 12 Key", "１２番ロッカーの鍵"),
    0x001B5DD4: Data(DataType.String, 20, "Locker 13 Key", "１３番ロッカーの鍵"),
    0x001B5DE8: Data(DataType.String, 20, "Locker 14 Key", "１４番ロッカーの鍵"),
    0x001B5DFC: Data(DataType.String, 20, "Locker 15 Key", "１５番ロッカーの鍵"),
    0x001B5E10: Data(DataType.String, 20, "Locker 16 Key", "１６番ロッカーの鍵"),
    0x001B5E24: Data(DataType.String, 20, "Locker 17 Key", "１７番ロッカーの鍵"),
    0x001B5E38: Data(DataType.String, 20, "Locker 18 Key", "１８番ロッカーの鍵"),
    0x001B5E4C: Data(DataType.String, 20, "Locker 19 Key", "１９番ロッカーの鍵"),
    0x001B5E60: Data(DataType.String, 20, "Locker 20 Key", "２０番ロッカーの鍵"),
    0x001B5E74: Data(DataType.String, 20, "Locker 21 Key", "２１番ロッカーの鍵"),
    0x001B5E88: Data(DataType.String, 20, "Locker 22 Key", "２２番ロッカーの鍵"),
    0x001B5E9C: Data(DataType.String, 20, "Locker 23 Key", "２３番ロッカーの鍵"),
    0x001B5EB0: Data(DataType.String, 20, "Locker 24 Key", "２４番ロッカーの鍵"),
    0x001B5EC4: Data(DataType.String, 20, "Locker 25 Key", "２５番ロッカーの鍵"),
    0x001B5ED8: Data(DataType.String, 20, "Locker 26 Key", "２６番ロッカーの鍵"),
    0x001B5EEC: Data(DataType.String, 20, "Locker 27 Key", "２７番ロッカーの鍵"),
    0x001B5F00: Data(DataType.String, 20, "Locker 28 Key", "２８番ロッカーの鍵"),
    0x001B5F14: Data(DataType.String, 20, "Locker 29 Key", "２９番ロッカーの鍵"),
    0x001B5F28: Data(DataType.String, 20, "Locker 30 Key", "３０番ロッカーの鍵"),
    0x001B5F3C: Data(DataType.String, 20, "Locker 31 Key", "３１番ロッカーの鍵"),
    0x001B5F50: Data(DataType.String, 20, "Locker 32 Key", "３２番ロッカーの鍵"),
    0x001B5F64: Data(DataType.String, 16, "Sage's Gift", "賢者の贈り物"),
    0x001B5F74: Data(DataType.String, 28, "A.T. increases when used.", "使うと、ΑΤが増加します。"),
    0x001B5F90: Data(DataType.String, 28, "It's a mysterious item for some reason.", "なにやら、不思議な商品だ"),
    0x001B5FAC: Data(DataType.String, 20, "A.T. went up!", "ΑΤが増加した！"),
    0x001B5FC0: Data(DataType.String, 12, "Sympathetic Soul", "理解の精神"),
    0x001B5FCC: Data(DataType.String, 12, "Passionate Soul", "情熱の精神"),
    0x001B5FD8: Data(DataType.String, 16, "Indomitable Heart", "くじけない心"),
    0x001B5FE8: Data(DataType.String, 36, "Restores Impulse when used.", "使うと、インパルスが回復します。"),
    0x001B600C: Data(DataType.String, 24, "Impulse was restored!", "インパルスが回復した！"),
    0x001B6024: Data(DataType.String, 12, "Dazzling Spirit", "絢爛の精神"),
    0x001B6030: Data(DataType.String, 12, "The Fool's Slate", "愚者の石板"),
    0x001B603C: Data(DataType.String, 28, "A.T. decreases when used.", "使うと、ΑΤが減少します。"),
    0x001B6058: Data(DataType.String, 20, "A.T. went down!", "ΑΤが減少した！"),
    0x001B606C: Data(DataType.String, 12, "Unearthly Technique", "仙人の技法"),
    0x001B6078: Data(DataType.String, 44, "If you have it, you will not feel sick.", "所持していると、体調が低下しなくなります。"), # MACHINE_TRANSLATED
    0x001B60A4: Data(DataType.String, 12, "Timid Spirit", "小心の精神"),
    0x001B60B0: Data(DataType.String, 12, "Expert Technique", "達人の技法"),
    0x001B60BC: Data(DataType.String, 40, "When used, all skills reach their maximum value.", "使うと、全ての技能が最大値になります。"), # MACHINE_TRANSLATED
    0x001B60E4: Data(DataType.String, 32, "All skills have reached their maximum value!", "全ての技能が最高値になった！"), # MACHINE_TRANSLATED
    0x001B6104: Data(DataType.String, 12, "Alchemical Technique", "錬金の技法"),
    0x001B6110: Data(DataType.String, 36, "If you use it, your money will increase by 100,000 yen.", "使うと、所持金が１０万円増えます。"), # MACHINE_TRANSLATED
    0x001B6134: Data(DataType.String, 28, "Money in hand increased by 100,000 yen!", "所持金が１０万円増えた！"), # MACHINE_TRANSLATED
    0x001B6150: Data(DataType.String, 12, "Mere Words", "許しの言葉"),
    0x001B615C: Data(DataType.String, 32, "If used, everyone's interest will increase.", "使うと、全員の関心が高くなる。"), # MACHINE_TRANSLATED
    0x001B617C: Data(DataType.String, 28, "Everyone's interest increased!", "みんなの関心が高くなった！"), # MACHINE_TRANSLATED
    0x001B6198: Data(DataType.String, 12, "Sickness Unto Death", "死に至る病"),
    0x001B61A4: Data(DataType.String, 36, "When used, everyone's ΑΤ will decrease.", "使うと、全員のΑΤが減少します。"), # MACHINE_TRANSLATED
    0x001B61C8: Data(DataType.String, 24, "Everyone's ΑΤ has decreased!", "全員のΑΤが減少した！"), # MACHINE_TRANSLATED
    0x001B61E0: Data(DataType.String, 12, "Words of Solace", "癒しの言葉"),
    0x001B61EC: Data(DataType.String, 32, "When used, everyone's favor will be high.", "使うと、全員の好意が高くなる。"), # MACHINE_TRANSLATED
    0x001B620C: Data(DataType.String, 28, "Everyone's favor increased!", "みんなの好意が高くなった！"), # MACHINE_TRANSLATED
    0x001B6228: Data(DataType.String, 16, "Complemented Heart", "補完された心"),
    0x001B6238: Data(DataType.String, 36, "If used, everyone's ΑΤ will increase.", "使うと、全員のΑΤが増加します。"), # MACHINE_TRANSLATED
    0x001B625C: Data(DataType.String, 24, "Everyone's A.T. went up!", "全員のΑΤが増加した！"),
    0x001B6274: Data(DataType.String, 20, "Soft nail special strap", "生爪特製ストラップ"), # MACHINE_TRANSLATED
    0x001B6288: Data(DataType.String, 48, "If you have a lot,\nThere may be something good.", "たくさん持っていると、\n何かいいことあるかも。"), # MACHINE_TRANSLATED
    0x001B64C8: Data(DataType.String, 8, "......", "……。"),
    0x001B64D0: Data(DataType.String, 32, "(There is no message.)", "（メッセージがありません。）"),
    0x001B64F0: Data(DataType.String, 8, "Shinji", "シンジ"),
    0x001B64F8: Data(DataType.String, 8, "Asuka", "アスカ"),
    0x001B6500: Data(DataType.String, 8, "Rei", "レイ"),
    0x001B6508: Data(DataType.String, 8, "Misato", "ミサト"),
    0x001B6510: Data(DataType.String, 12, "Gendo", "ゲンドウ"),
    0x001B651C: Data(DataType.String, 8, "Fuyutsuki", "冬月"),
    0x001B6524: Data(DataType.String, 8, "Ritsuko", "リツコ"),
    0x001B652C: Data(DataType.String, 8, "Maya", "マヤ"),
    0x001B6534: Data(DataType.String, 8, "Hyuga", "日向"),
    0x001B653C: Data(DataType.String, 8, "Aoba", "青葉"),
    0x001B6544: Data(DataType.String, 8, "Kaji", "加持"),
    0x001B654C: Data(DataType.String, 8, "Hikari", "ヒカリ"),
    0x001B6554: Data(DataType.String, 8, "Toji", "トウジ"),
    0x001B655C: Data(DataType.String, 12, "Kensuke", "ケンスケ"),
    0x001B6568: Data(DataType.String, 8, "Kaworu", "カヲル"),
    0x001B6570: Data(DataType.String, 12, "Pen Pen", "ペンペン"),
    0x001B657C: Data(DataType.String, 8, "Nerv", "ネルフ"),
    0x001B6584: Data(DataType.String, 8, "Eva-00", "零号機"),
    0x001B658C: Data(DataType.String, 8, "Eva-01", "初号機"),
    0x001B6594: Data(DataType.String, 8, "Eva-02", "弐号機"),
    0x001B659C: Data(DataType.String, 8, "Eva-03", "参号機"),
    0x001B65A4: Data(DataType.String, 8, "Eva-04", "四号機"),
    0x001B65AC: Data(DataType.String, 12, "Sachiel", "サキエル"),
    0x001B65B8: Data(DataType.String, 16, "Shamshel", "シャムシェル"),
    0x001B65C8: Data(DataType.String, 12, "Ramiel", "ラミエル"),
    0x001B65D4: Data(DataType.String, 12, "Gaghiel", "ガギエル"),
    0x001B65E0: Data(DataType.String, 16, "Israfel", "イスラフェル"),
    0x001B65F0: Data(DataType.String, 16, "Sandalphon", "サンダルフォン"),
    0x001B6600: Data(DataType.String, 12, "Matarael", "マトリエル"),
    0x001B660C: Data(DataType.String, 16, "Sahaquiel", "サハクィエル"),
    0x001B661C: Data(DataType.String, 12, "Ireul", "イロウル"),
    0x001B6628: Data(DataType.String, 12, "Leliel", "レリエル"),
    0x001B6634: Data(DataType.String, 16, "Bardiel", "バルディエル"),
    0x001B6644: Data(DataType.String, 12, "Zeruel", "ゼルエル"),
    0x001B6650: Data(DataType.String, 12, "Arael", "アラエル"),
    0x001B665C: Data(DataType.String, 16, "Armisael", "アノミサエル"),
    0x001B666C: Data(DataType.String, 12, "Tabris", "ダブリス"),
    0x001B6678: Data(DataType.String, 16, "Eva Mass Production Model", "ＥＶＡ量産機"),
    0x001B6688: Data(DataType.String, 8, "ΘΑ", "ΘΑ"),
    0x001B6690: Data(DataType.String, 4, "I", "僕"),
    0x001B6694: Data(DataType.String, 8, "Ayanami", "綾波"),
    0x001B669C: Data(DataType.String, 12, "Misato-san", "ミサトさん"),
    0x001B66A8: Data(DataType.String, 8, "Father", "父さん"),
    0x001B66B0: Data(DataType.String, 12, "Fuyutsuki-san", "冬月さん"),
    0x001B66BC: Data(DataType.String, 12, "Ritsuko-san", "リツコさん"),
    0x001B66C8: Data(DataType.String, 12, "Maya-san", "マヤさん"),
    0x001B66D4: Data(DataType.String, 12, "Hyuga-san", "日向さん"),
    0x001B66E0: Data(DataType.String, 12, "Aoba-san", "青葉さん"),
    0x001B66EC: Data(DataType.String, 12, "Kaji-san", "加持さん"),
    0x001B66F8: Data(DataType.String, 8, "Chairman", "委員長"),
    0x001B6700: Data(DataType.String, 12, "Kaworu-kun", "カヲルくん"),
    0x001B670C: Data(DataType.String, 20, "The Angel that shoots spears from its arms", "腕から槍が出る使徒"),
    0x001B6720: Data(DataType.String, 24, "The Angel shaped like an alien", "宇宙人の形をした使徒"),
    0x001B6738: Data(DataType.String, 12, "The box-shaped Angel", "四角い使徒"),
    0x001B6744: Data(DataType.String, 12, "The water Angel", "水中の使徒"),
    0x001B6750: Data(DataType.String, 16, "The splitting Angel", "分裂する使徒"),
    0x001B6760: Data(DataType.String, 16, "The lava Angel", "溶岩の中の使徒"),
    0x001B6770: Data(DataType.String, 20, "The spider-like Angel", "クモみたいな使徒"),
    0x001B6784: Data(DataType.String, 20, "The big eyeball Angel", "巨大な目玉の使徒"),
    0x001B6798: Data(DataType.String, 16, "The virus Angel", "ウィルスの使徒"),
    0x001B67A8: Data(DataType.String, 12, "The shadow Angel", "影の使徒"),
    0x001B67B4: Data(DataType.String, 12, "The black Eva", "黒いエヴァ"),
    0x001B67C0: Data(DataType.String, 20, "The angel with glowy wing-things", "光る羽みたいな使徒"),
    0x001B67D4: Data(DataType.String, 12, "The shellfish Angel", "ひもの使徒"),
    0x001B67E0: Data(DataType.String, 16, "Eva mass production model", "エヴァの量産機"),
    0x001B67F0: Data(DataType.String, 20, "The bipedal robot", "二本足のロボット"),
    0x001B6804: Data(DataType.String, 4, "I", "私"),
    0x001B6808: Data(DataType.String, 12, "First", "ファースト"),
    0x001B6814: Data(DataType.String, 8, "Commander", "司令"),
    0x001B681C: Data(DataType.String, 8, "Deputy Commander", "副司令"),
    0x001B6824: Data(DataType.String, 8, "Suzuhara", "鈴原"),
    0x001B682C: Data(DataType.String, 8, "Aida", "相田"),
    0x001B6834: Data(DataType.String, 12, "Fifth", "フィフス"),
    0x001B6840: Data(DataType.String, 20, "The Eva imposter", "エヴァのニセモノ"),
    0x001B6854: Data(DataType.String, 8, "Ikari-kun", "碇くん"),
    0x001B685C: Data(DataType.String, 12, "Second", "セカンド"),
    0x001B6868: Data(DataType.String, 8, "Commander Ikari", "碇司令"),
    0x001B6870: Data(DataType.String, 12, "Dr. Akagi", "赤木博士"),
    0x001B687C: Data(DataType.String, 12, "Lt. Ibuki", "伊吹二尉"),
    0x001B6888: Data(DataType.String, 12, "Lt. Hyuga", "日向二尉"),
    0x001B6894: Data(DataType.String, 12, "Lt. Aoba", "青葉二尉"),
    0x001B68A0: Data(DataType.String, 12, "Horaki-san", "洞木さん"),
    0x001B68AC: Data(DataType.String, 12, "Suzuhara-kun", "鈴原くん"),
    0x001B68B8: Data(DataType.String, 12, "Aida-kun", "相田くん"),
    0x001B68C4: Data(DataType.String, 16, "Armisael", "アルミサエル"),
    0x001B68D4: Data(DataType.String, 16, "Eva Mass Production Model", "エヴァ量産機"),
    0x001B68E4: Data(DataType.String, 12, "Maya-chan", "マヤちゃん"),
    0x001B68F0: Data(DataType.String, 8, "Hyuga-kun", "日向君"),
    0x001B68F8: Data(DataType.String, 8, "Aoba-kun", "青葉君"),
    0x001B6900: Data(DataType.String, 8, "Kaji-kun", "加持君"),
    0x001B6908: Data(DataType.String, 8, "Nagisa-kun", "渚くん"),
    0x001B6910: Data(DataType.String, 12, "Shinji-kun", "シンジくん"),
    0x001B691C: Data(DataType.String, 4, "Ikari", "碇"),
    0x001B6920: Data(DataType.String, 8, "Ibuki-kun", "伊吹君"),
    0x001B6928: Data(DataType.String, 12, "Sempai", "センパイ"),
    0x001B6934: Data(DataType.String, 4, "I", "俺"),
    0x001B6938: Data(DataType.String, 8, "Katsuragi", "葛城"),
    0x001B6940: Data(DataType.String, 8, "Akagi", "赤木"),
    0x001B6948: Data(DataType.String, 12, "Ayanami-san", "綾波さん"),
    0x001B6954: Data(DataType.String, 20, "Ikari-kun's father", "碇くんのお父さん"),
    0x001B6968: Data(DataType.String, 20, "Ayanami's Eva", "綾波さんのエヴァ"),
    0x001B697C: Data(DataType.String, 16, "Ikari's Eva", "碇くんのエヴァ"),
    0x001B698C: Data(DataType.String, 16, "Asuka's Eva", "アスカのエヴァ"),
    0x001B699C: Data(DataType.String, 16, "Suzuhara's Eva", "鈴原のエヴァ"),
    0x001B69AC: Data(DataType.String, 16, "Nagisa's Eva", "渚くんのエヴァ"),
    0x001B69BC: Data(DataType.String, 8, "Angel", "使徒"),
    0x001B69C4: Data(DataType.String, 12, "The white Eva", "白いエヴァ"),
    0x001B69D0: Data(DataType.String, 8, "Soryu", "惣流"),
    0x001B69D8: Data(DataType.String, 16, "Shinji's dad", "シンジのおとん"),
    0x001B69E8: Data(DataType.String, 8, "I", "ワシ"),
    0x001B69F0: Data(DataType.String, 16, "Ayanami's Eva", "綾波のエヴァ"),
    0x001B6A00: Data(DataType.String, 16, "Shinji's Eva", "シンジのエヴァ"),
    0x001B6A10: Data(DataType.String, 16, "My Eva", "ワイのエヴァ"),
    0x001B6A20: Data(DataType.String, 16, "Kaworu's Eva", "カヲルのエヴァ"),
    0x001B6A30: Data(DataType.String, 20, "Knockoff Eva", "エヴァのパチモン"),
    0x001B6A44: Data(DataType.String, 20, "Shinji's father", "シンジのお父さん"),
    0x001B6A58: Data(DataType.String, 12, "Ikari's Eva", "碇のエヴァ"),
    0x001B6A64: Data(DataType.String, 16, "Toji's Eva", "トウジのエヴァ"),
    0x001B6A74: Data(DataType.String, 12, "Shinji-kun", "シンジ君"),
    0x001B6A84: Data(DataType.String, 12, "Toji-kun", "トウジくん"),
    0x001B6A90: Data(DataType.String, 8, "Akagi-kun", "赤木君"),
    0x001B6A98: Data(DataType.String, 12, "Major Katsuragi", "葛城三佐"),
    0x001B6AA4: Data(DataType.String, 12, "Captain Katsuragi", "葛城一尉"),
    0x001B6AB0: Data(DataType.String, 12, "Shin-chan", "シンちゃん"),
    0x001B6ABC: Data(DataType.String, 16, "Damage: intermediate", "被害は中規模"),
    0x001B6ACC: Data(DataType.String, 12, "Damage: severe", "被害は甚大"),
    0x001B6AD8: Data(DataType.String, 12, "Damage: insignificant", "被害は軽微"),
    0x001B6AE4: Data(DataType.String, 12, "Damage: ???", "被害は？？"),
    0x001B6AF0: Data(DataType.String, 16, "Damage: catastrophic", "被害は壊滅的"),
    0x001B6B00: Data(DataType.String, 8, "? ? ?", "？？？"), # MACHINE_TRANSLATED
    0x001B6B08: Data(DataType.String, 12, "Debut Pending", "登場待ち"),
    0x001B6B14: Data(DataType.String, 8, "Debuted", "登場"),
    0x001B6B1C: Data(DataType.String, 8, "Hospitalized", "入院"),
    0x001B6B24: Data(DataType.String, 8, "Invalid", "無効"),
    0x001B6B2C: Data(DataType.String, 12, "Rested for 1 Day", "１日休み"),
    0x001B6B38: Data(DataType.String, 16, "Suspended (%s)", "出場停止(%s)"),
    0x001B6B48: Data(DataType.String, 8, "Evacuated", "疎開"),
    0x001B6B50: Data(DataType.String, 8, "Resigned", "辞職"),
    0x001B6B58: Data(DataType.String, 8, "Ran Away", "家出"),
    0x001B6B60: Data(DataType.String, 12, "Exeunt (%s)", "退場(%s)"),
    0x001B6B6C: Data(DataType.String, 8, "K.I.A.", "戦死"),
    0x001B6B74: Data(DataType.String, 8, "Assassinated", "暗殺"),
    0x001B6B7C: Data(DataType.String, 12, "Passed Away (%s)", "死亡(%s)"),
    0x001B6BA0: Data(DataType.String, 16, "Eva Mechanics", "エヴァの構造"),
    0x001B6BB0: Data(DataType.String, 16, "Eva Unit-01", "エヴァ初号機"),
    0x001B6BC0: Data(DataType.String, 24, "The Second Child", "セカンド・チルドレン"),
    0x001B6BD8: Data(DataType.String, 8, "Yui Ikari", "碇ユイ"),
    0x001B6BE0: Data(DataType.String, 12, "Gendo Ikari", "碇ゲンドウ"),
    0x001B6BEC: Data(DataType.String, 16, "Special Agency Nerv", "特務機関ネルフ"),
    0x001B6BFC: Data(DataType.String, 20, "Marduk Institute", "マルドゥック機関"),
    0x001B6C10: Data(DataType.String, 16, "Gendo's Ambitions", "ゲンドウの野望"),
    0x001B6C20: Data(DataType.String, 16, "History of Nerv", "ネルフの歴史"),
    0x001B6C30: Data(DataType.String, 20, "Human Instrumentality Project in Detail", "人類補完計画の内容"),
    0x001B6C44: Data(DataType.String, 12, "Gehirn", "ゲヒルン"),
    0x001B6C50: Data(DataType.String, 8, "Seele", "ゼーレ"),
    0x001B6C58: Data(DataType.String, 16, "A.T. Field", "ΑΤフィールド"),
    0x001B6C68: Data(DataType.String, 8, "Σ Engine", "Σ機関"),
    0x001B6C70: Data(DataType.String, 8, "Angels", "使徒"),
    0x001B6C78: Data(DataType.String, 8, "Adam", "アダム"),
    0x001B6C80: Data(DataType.String, 12, "Dead Sea Scrolls", "死海文書"),
    0x001B6C8C: Data(DataType.String, 16, "First Ancestral Race", "第一始祖民族"),
    0x001B6C9C: Data(DataType.String, 12, "The Second Angel", "第二使徒"),
    0x001B6CA8: Data(DataType.String, 20, "Second Impact", "セカンドインパクト"),
    0x001B6CBC: Data(DataType.String, 20, "Third Impact", "サードインパクト"),
    0x001B6CD0: Data(DataType.String, 16, "Spear of Longinus", "ロンギヌスの槍"),
    0x001B6CE0: Data(DataType.String, 16, "Dummy Plug", "ダミープラグ"),
    0x001B6CF0: Data(DataType.String, 16, "GeoFront", "ジオフロント"),
    0x001B6D00: Data(DataType.String, 16, "Public Information", "広報公開情報"),
    0x001B6D10: Data(DataType.String, 12, "General Information", "一般情報"),
    0x001B6D1C: Data(DataType.String, 12, "Non-Public Information", "非公開情報"),
    0x001B6D28: Data(DataType.String, 12, "Top Secret Information", "最深度情報"),
    0x001B6DA8: Data(DataType.String, 4, "A", "Ａ"),
    0x001B6DAC: Data(DataType.String, 8, "%s−%s", "%s−%s"),
    0x001B6F90: Data(DataType.String, 28, "%4iBack\n%3iRedo\n%1iNext\n%2iFinish\n", "%4i前\n%3i再\n%1i次\n%2i終了\n"),
    0x001B77A4: Data(DataType.String, 40, "Loc.　%3D\nNar.Base No.　%7D\nNar.No.　%7D", "場所　%3D\nナレ元番　%7D\nナレ番号　%7D"),
    0x001B8CEC: Data(DataType.String, 28, "%s(%d)Index Error\n", "%s(%d)インデックスエラー\n"),
    0x001B8DBC: Data(DataType.String, 16, "Evaluation Pulse", "効果判定パルス"),
    0x001B8DCC: Data(DataType.String, 8, "Constant", "定数"),
    0x001B8DD4: Data(DataType.String, 12, "A.Y.P. Performance", "ＡＹＰ性能"),
    0x001B8DE0: Data(DataType.String, 28, "Execution of Self-Destruction Accelerant Program", "自滅促進プログラムの実行"),
    0x001B8DFC: Data(DataType.String, 32, "You find courage enough to keep Suzuhara in check", "勇気を出して、鈴原を引き止める"),
    0x001B8E1C: Data(DataType.String, 28, "You find courage enough to hand over the bento box", "勇気を出して、お弁当を渡す"),
    0x001B8FA0: Data(DataType.String, 16, "Game Pace", "ゲーム進行速度"),
    0x001B8FB0: Data(DataType.String, 8, "Normal", "普通"),
    0x001B8FB8: Data(DataType.String, 8, "Fast", "速い"),
    0x001B8FC0: Data(DataType.String, 8, "Slow", "遅い"),
    0x001B8FC8: Data(DataType.String, 24, "Character Graphics", "キャラグラフィックス"),
    0x001B8FE0: Data(DataType.String, 12, "Faces On", "顔グラ有"),
    0x001B8FEC: Data(DataType.String, 12, "Faces Off", "顔グラ無"),
    0x001B8FF8: Data(DataType.String, 16, "Character Voices", "キャラボイス"),
    0x001B9008: Data(DataType.String, 12, "Voices On", "ボイス有"),
    0x001B9014: Data(DataType.String, 12, "Voices Off", "ボイス無"),
    0x001B9020: Data(DataType.String, 16, "Directional Button Behavior", "方向キー挙動"),
    0x001B9030: Data(DataType.String, 8, "Movement", "移動"),
    0x001B9038: Data(DataType.String, 24, "%%1i%%2i%%3i%%4i", "%%1i%%2i%%3i%%4i対応"),
    0x001B9050: Data(DataType.String, 16, "Exit Options", "オプション終了"),
    0x001B9060: Data(DataType.String, 28, "Save changes", "現在の設定に更新して終了"),
    0x001B907C: Data(DataType.String, 24, "Cancel", "最初の設定に戻して終了"),
    0x001B9554: Data(DataType.String, 8, "Invalid", "無効"),
    0x001B955C: Data(DataType.String, 8, "Motivated", "やる気"),
    0x001B9564: Data(DataType.String, 8, "Happy", "喜び"),
    0x001B956C: Data(DataType.String, 8, "Optimistic", "楽観"),
    0x001B9574: Data(DataType.String, 8, "Earnest", "真剣"),
    0x001B957C: Data(DataType.String, 8, "Positive", "積極"),
    0x001B9584: Data(DataType.String, 8, "Apprehensive", "静観"),
    0x001B958C: Data(DataType.String, 8, "Seething", "殺気"),
    0x001B9594: Data(DataType.String, 8, "Mad", "怒り"),
    0x001B959C: Data(DataType.String, 8, "Hopeless", "絶望"),
    0x001B95A4: Data(DataType.String, 8, "Hopeful", "期待"),
    0x001B95AC: Data(DataType.String, 8, "Refreshed", "爽快"),
    0x001B95B4: Data(DataType.String, 8, "Straightforward", "開放"),
    0x001B95BC: Data(DataType.String, 8, "Tense", "緊張"),
    0x001B95C4: Data(DataType.String, 8, "Serene", "平穏"),
    0x001B95CC: Data(DataType.String, 8, "Relaxed", "弛緩"),
    0x001B95D4: Data(DataType.String, 8, "Cautious", "警戒"),
    0x001B95DC: Data(DataType.String, 8, "Disagreeable", "不快"),
    0x001B95E4: Data(DataType.String, 8, "Frustrated", "悔しい"),
    0x001B95EC: Data(DataType.String, 8, "Prudent", "慎重"),
    0x001B95F4: Data(DataType.String, 8, "Relieved", "安堵"),
    0x001B95FC: Data(DataType.String, 8, "Exhausted", "脱力"),
    0x001B9604: Data(DataType.String, 8, "Anxious", "不安"),
    0x001B960C: Data(DataType.String, 8, "Passive", "消極"),
    0x001B9614: Data(DataType.String, 8, "Apathetic", "無気力"),
    0x001B961C: Data(DataType.String, 8, "Afraid", "恐怖"),
    0x001B9624: Data(DataType.String, 8, "Sad", "悲しみ"),
    0x001B962C: Data(DataType.String, 8, "Regretful", "後悔"),
    0x001B9634: Data(DataType.String, 8, "Impassioned", "欲情"),
    0x001B963C: Data(DataType.String, 12, "Bashful", "恥じらい"),
    0x001B9648: Data(DataType.String, 8, "Ashamed", "羞恥"),
    0x001B9728: Data(DataType.String, 20, "Smash Hawk", "スマッシュホーク"),
    0x001B9748: Data(DataType.String, 20, "Sonic Glaive", "ソニックグレイブ"),
    0x001B975C: Data(DataType.String, 12, "M.P.E. Sword", "量産機の剣"),
    0x001B9768: Data(DataType.String, 20, "Pallet Rifle", "パレットライフル"),
    0x001B977C: Data(DataType.String, 36, "Wide firing range\nbut low power.", "広い射角を持つ射撃\n攻撃、威力は低め"),
    0x001B97A0: Data(DataType.String, 12, "Handgun", "ハンドガン"),
    0x001B97AC: Data(DataType.String, 12, "Bazooka", "バズーカ"),
    0x001B97B8: Data(DataType.String, 12, "Rifle", "ライフル"),
    0x001B97C4: Data(DataType.String, 56, "Long but narrow\nfiring range.", "真正面に対して行う\n射撃攻撃、射角は\n狭いが射程は長め"),
    0x001B97FC: Data(DataType.String, 20, "Positron Rifle", "ポジトロンライフル"),
    0x001B9810: Data(DataType.String, 40, "Strong, long range fire,\nbut slows you down.", "強力な長距離射程\n攻撃、移動速度が\n低下"),
    0x001B9838: Data(DataType.String, 16, "Positron Sniper Rifle", "ボジトロン・Ｓ"),
    0x001B9848: Data(DataType.String, 48, "Extremely long range\nbut slows you extremely.", "超長距離狙撃の必殺\n攻撃、移動速度は\n極端に低下"),
    0x001B9878: Data(DataType.String, 12, "Shield", "シールド"),
    0x001B9884: Data(DataType.String, 28, "Defensive weapon,\nadds durability.", "耐久度が追加される\n防御兵器"),
    0x001B98A0: Data(DataType.String, 16, "Dura-Shield", "強化シールド"),
    0x001B98B0: Data(DataType.String, 56, "Defensive weapon,\nadds more durability\nthan regular Shield.", "耐久度が追加される\n防御兵器、シールド\nより耐久度が高い"),
    0x001B98E8: Data(DataType.String, 12, "Mastema", "マステマ"),
    0x001B98F4: Data(DataType.String, 52, "Weapon with melee,\nranged, and N2\nMissile-firing ability.", "近接／射撃／\nΝミサイルの３種類\nの攻撃方法がある"),
    0x001B9928: Data(DataType.String, 16, "Dual Saw", "デュアルソー"),
    0x001B9938: Data(DataType.String, 52, "Powerful melee attack to front of target.\nStuns enemy briefly.", "真正面へ強力な近接\n攻撃、しばらくの間\n敵が移動不能"),
    0x001B996C: Data(DataType.String, 16, "Magoroku Sword", "マゴロクソード"),
    0x001B997C: Data(DataType.String, 36, "Weapon twice as powerful\nas a prog knife.", "プログナイフの２倍\nの威力を持つ武器"),
    0x001B99A8: Data(DataType.String, 20, "Eva: Kick A", "ＥＶＡのキックＡ"),
    0x001B99BC: Data(DataType.String, 16, "Middle Kick", "ミドルキック"),
    0x001B99CC: Data(DataType.String, 20, "Sideways melee attack.", "側面用の近接攻撃"),
    0x001B99E4: Data(DataType.String, 28, "Eva: Prog Knife Stab", "ＥＶＡのプログナイフ・突く"),
    0x001B9A00: Data(DataType.String, 20, "Prog Knife Stab", "プログナイフ・突く"),
    0x001B9A14: Data(DataType.String, 24, "Powerful melee attack\n to front of target.", "真正面へ強力な近接\n攻撃"),
    0x001B9A2C: Data(DataType.String, 16, "Prog Knife", "プログナイフ"),
    0x001B9A3C: Data(DataType.String, 28, "Eva: Smash Hawk", "ＥＶＡのスマッシュホーク"),
    0x001B9A58: Data(DataType.String, 24, "Eva: Punch A/B", "ＥＶＡのパンチＡ／Ｂ"),
    0x001B9A70: Data(DataType.String, 12, "Chop", "チョップ"),
    0x001B9A7C: Data(DataType.String, 32, "Melee attack covering\noblique forward angles.", "斜め前方をカバー\nする近接攻撃"),
    0x001B9A9C: Data(DataType.String, 28, "Eva: Prog Knife Cutting", "ＥＶＡのプログナイフ・切る"),
    0x001B9AB8: Data(DataType.String, 20, "Prog Knife Cutting", "プログナイフ・切る"),
    0x001B9ACC: Data(DataType.String, 28, "Eva: Sonic Glaive", "ＥＶＡのソニックグレイブ"),
    0x001B9AE8: Data(DataType.String, 16, "Front Kick", "フロントキック"),
    0x001B9AF8: Data(DataType.String, 20, "Eva: Kick B", "ＥＶＡのキックＢ"),
    0x001B9B0C: Data(DataType.String, 48, "Melee attack to front of target./nStuns enemy momentarily.", "真正面への近接攻撃\n一瞬、敵が移動不能\nになる"),
    0x001B9B3C: Data(DataType.String, 24, "Eva: Needle Gun", "ＥＶＡのニードルガン"),
    0x001B9B54: Data(DataType.String, 28, "Eva: Eva Mass Production Model Sword", "ＥＶＡのＥＶＡ量産機の剣"),
    0x001B9B70: Data(DataType.String, 20, "Eva Mass Production Model Sword", "ＥＶＡ量産機の剣"),
    0x001B9B84: Data(DataType.String, 44, "Powerful melee attack\nwith wide forward range.", "前方の広い範囲を\nカバーする強力な\n近接攻撃"),
    0x001B9BB0: Data(DataType.String, 12, "Mass Production Model's Sword", "量産機の剣"),
    0x001B9BBC: Data(DataType.String, 32, "Eva: A.T. Field Attack", "ＥＶＡのＡＴフィールドアタック"),
    0x001B9BDC: Data(DataType.String, 16, "A.T. Field Attack", "ＡＴＦアタック"),
    0x001B9BEC: Data(DataType.String, 44, "Powerful melee attack\ncovering all but your rear.", "後方を除く周囲を\nカバーする強力な\n近接攻撃"),
    0x001B9C18: Data(DataType.String, 28, "Eva: Two Platoon Kick", "ＥＶＡのツープラトンキック"),
    0x001B9C34: Data(DataType.String, 20, "Two Platoon Kick", "ツープラトンキック"),
    0x001B9C48: Data(DataType.String, 52, "Super powerful simultaneous\nattack covering a wide\nforward range.", "前方の広い範囲を\nカバーする超強力な\n同時荷重攻撃"),
    0x001B9C7C: Data(DataType.String, 28, "Eva: Pallet Rifle", "ＥＶＡのパレットライフル"),
    0x001B9C98: Data(DataType.String, 20, "Pallet Rifle", "パレットライフル"),
    0x001B9CAC: Data(DataType.String, 44, "Wide-ranged firing attack\nthat easily hits enemies.", "広範囲の射角を持つ\n射撃攻撃\n敵を捉え易い"),
    0x001B9CD8: Data(DataType.String, 20, "Eva: Handgun", "ＥＶＡのハンドガン"),
    0x001B9CEC: Data(DataType.String, 20, "Eva: Bazooka", "ＥＶＡのバズーカ"),
    0x001B9D00: Data(DataType.String, 20, "Eva: Rifle", "ＥＶＡのライフル"),
    0x001B9D14: Data(DataType.String, 12, "Rifle", "ライフル"),
    0x001B9D20: Data(DataType.String, 56, "Firing attack that\nbriefly stuns enemies.", "真正面に対して行う\n射撃攻撃、一瞬、\n敵が移動不能になる"),
    0x001B9D58: Data(DataType.String, 28, "Eva: Positron Rifle", "ＥＶＡのポジトロンライフル"),
    0x001B9D74: Data(DataType.String, 20, "Positron Rifle", "ポジトロンライフル"),
    0x001B9D88: Data(DataType.String, 36, "Strong firing attack\nwith long, but\nnarrow, range.", "強力な長距離射程\n攻撃、射角は狭い"),
    0x001B9DAC: Data(DataType.String, 32, "Eva: Positron Rifle", "ＥＶＡのスナイパーポジトロン"),
    0x001B9DCC: Data(DataType.String, 16, "Positron Sniper Rifle", "ポジトロン・Ｓ"),
    0x001B9DDC: Data(DataType.String, 48, "Extremely long range attack\nbut slows you extremely.", "超長距離狙撃の必殺\n攻撃、移動速度は\n極端に低下"),
    0x001B9E0C: Data(DataType.String, 28, "Sachiel: Face Grab, Spear of Light", "サキエルのつかむ頭−光の槍"),
    0x001B9E28: Data(DataType.String, 24, "Sachiel: Ocular Light Beam", "サキエルの目から怪光線"),
    0x001B9E40: Data(DataType.String, 20, "Sachiel: Punch", "サキエルのパンチ"),
    0x001B9E54: Data(DataType.String, 24, "Shamshel: Whip Strike", "シャムシェルのムチ突き"),
    0x001B9E6C: Data(DataType.String, 24, "Shamshel: Whip Pierce", "シャムシェルのムチ貫き"),
    0x001B9E84: Data(DataType.String, 32, "Shamshel: Whip Fling", "シャムシェルのムチ弾き飛ばし"),
    0x001B9EA4: Data(DataType.String, 24, "Ramiel: Beam Attack", "ラミエルのビーム発射"),
    0x001B9EBC: Data(DataType.String, 28, "Israfel: Ocular Light Beam", "イスラフェルの目から怪光線"),
    0x001B9ED8: Data(DataType.String, 36, "Israfel: Mongolian Chop", "イスラフェルのモンゴリアンチョップ"),
    0x001B9EFC: Data(DataType.String, 28, "Matarael: Acid", "マトリエルの溶解液を飛ばす"),
    0x001B9F18: Data(DataType.String, 24, "Bardiel: Neck Throttle", "バルディエルの首絞め"),
    0x001B9F30: Data(DataType.String, 28, "Bardiel: Punch A/B", "バルディエルのパンチＡ／Ｂ"),
    0x001B9F4C: Data(DataType.String, 28, "Bardiel: Kick A/B", "バルディエルのキックＡ／Ｂ"),
    0x001B9F68: Data(DataType.String, 24, "Zeruel: Ocular Light Beam", "ゼルエルの目から怪光線"),
    0x001B9F80: Data(DataType.String, 24, "Zeruel: Arm Cutter", "ゼルエルの腕カッター"),
    0x001B9F98: Data(DataType.String, 24, "Armisael: Penetrative Attack", "アルミサエルの貫き攻撃"),
    0x001B9FB0: Data(DataType.String, 36, "Armisael: Merging Attack (Hijack)", "アルミサエルの合体攻撃（乗っ取り）"),
    0x001B9FD4: Data(DataType.String, 44, "Enemy Eva (Tabris): Prog Knife Stab", "敵ＥＶＡ（ダブリス）のプログナイフ・突く"),
    0x001BA000: Data(DataType.String, 44, "Enemy Eva (Tabris): Punch A (No B)", "敵ＥＶＡ（ダブリス）のパンチＡ（Ｂは無し）"),
    0x001BA02C: Data(DataType.String, 44, "Enemy Eva (Tabris): Prog Knife Cutting", "敵ＥＶＡ（ダブリス）のプログナイフ・切る"),
    0x001BA058: Data(DataType.String, 20, "M.P. Eva: Attack with Sword", "量産機の剣で攻撃"),
    0x001BA06C: Data(DataType.String, 32, "M.P. Eva: Attack with Spear of Longinus", "量産機のロンギヌスの槍で攻撃"),
    0x001BA08C: Data(DataType.String, 32, "Armament Building: Rocket Launcher", "兵装ビルのロケットランチャー"),
    0x001BA0AC: Data(DataType.String, 16, "U.N. Forces: Attack", "国連軍の攻撃"),
    0x001BA0BC: Data(DataType.String, 24, "Eva: Firing with Mastema", "ＥＶＡのマステマで射撃"),
    0x001BA0D4: Data(DataType.String, 16, "Mastema Firing", "マステマ・射撃"),
    0x001BA0E4: Data(DataType.String, 32, "Powerful, long-range\nfiring attack.", "真正面へ強力な\n長距離射程攻撃"),
    0x001BA104: Data(DataType.String, 16, "Mastema (Firing)", "マステマ(射撃)"),
    0x001BA114: Data(DataType.String, 24, "Eva: Cutting with Mastema", "ＥＶＡのマステマで切る"),
    0x001BA12C: Data(DataType.String, 16, "Mastema Cutting", "マステマ・切る"),
    0x001BA13C: Data(DataType.String, 16, "Mastema(Strike)", "マステマ(打撃)"),
    0x001BA14C: Data(DataType.String, 28, "Eva: N2 Missile Attack", "ＥＶＡのＮ２ミサイル攻撃"),
    0x001BA168: Data(DataType.String, 12, "Ν Missile", "Νミサイル"),
    0x001BA174: Data(DataType.String, 48, "Ultra-powerful firing\nattack, but destroys\nsurrounding buildings.", "超強力な射撃攻撃\nだが、周囲の建物\nも同時に破壊"),
    0x001BA1A4: Data(DataType.String, 28, "Eva: Attack with Dual Saw", "ＥＶＡのデュアルソーで攻撃"),
    0x001BA1C0: Data(DataType.String, 16, "Dual Saw", "デュアルソー"),
    0x001BA1D0: Data(DataType.String, 52, "Powerful melee attack\nthat briefly stuns the target.", "真正面へ強力な近接\n攻撃、しばらくの間\n敵が移動不能"),
    0x001BA204: Data(DataType.String, 32, "New Unit-01: Stab with Prog Dagger", "新初号機のプログダガーで突く"),
    0x001BA224: Data(DataType.String, 20, "Prog Dagger Stabbing", "プログダガー・突く"),
    0x001BA238: Data(DataType.String, 48, "Powerful melee attack\nwith enhanced prog\nknife.", "真正面へ強力な近接\n攻撃、プログナイフ\n強化版"),
    0x001BA268: Data(DataType.String, 16, "Prog Dagger", "プログダガー"),
    0x001BA278: Data(DataType.String, 32, "New Unit-01: Cut with Prog Dagger", "新初号機のプログダガーで切る"),
    0x001BA298: Data(DataType.String, 20, "Prog Dagger Cutting", "プログダガー・切る"),
    0x001BA2AC: Data(DataType.String, 56, "Powerful melee attack\ncovering oblique forward angles\nwith enhanced prog knife.", "斜め前方をカバー\nする強力な近接攻撃\nプログナイフ強化版"),
    0x001BA2E4: Data(DataType.String, 28, "New Unit-01: Impact Bolt", "新初号機のインパクトボルト"),
    0x001BA300: Data(DataType.String, 20, "Impact Bolt", "インパクトボルト"),
    0x001BA314: Data(DataType.String, 48, "Powerful melee attack\nthat stuns the enemy\nfor a while.", "真正面へ強力な\n近接攻撃、しばらく\n敵が移動不能"),
    0x001BA344: Data(DataType.String, 28, "New Unit-01: Hyper Chop", "新初号機のハイパーチョップ"),
    0x001BA360: Data(DataType.String, 20, "Hyper Chop", "ハイパーチョップ"),
    0x001BA374: Data(DataType.String, 48, "Melee attack that covers\nsides, more powerful\than middle kick.", "側面用の近接攻撃\nミドルキックより\n威力が高い"),
    0x001BA3A4: Data(DataType.String, 20, "J.A. 2 Hammer", "ＪＡ２のハンマー"),
    0x001BA3B8: Data(DataType.String, 16, "J.A. 2 Electric Shock", "ＪＡ２の電撃"),
    0x001BA3C8: Data(DataType.String, 20, "Arael: Mental Attack", "アラエルの精神攻撃"),
    0x001BA3DC: Data(DataType.String, 28, "Eva: Slice with Magoroku Sword", "EVAのマゴロクソードで斬る"),
    0x001BA3F8: Data(DataType.String, 20, "Slice with Magoroku Sword", "マゴロクソード斬る"),
    0x001BA40C: Data(DataType.String, 24, "Quick melee attack\ndirectly in front.", "真正面へ素早い\n近接攻撃"),
    0x001BA424: Data(DataType.String, 16, "Magoroku Sword", "マゴロクソード"),
    0x001BA434: Data(DataType.String, 28, "Eva: Stab with Magoroku Sword", "EVAのマゴロクソードで突く"),
    0x001BA450: Data(DataType.String, 20, "Stab with Magoroku Sword", "マゴロクソード突く"),
    0x001BA464: Data(DataType.String, 16, "Ready stance", "姿勢を構える"),
    0x001BA474: Data(DataType.String, 16, "Ready knife", "ナイフを構える"),
    0x001BA484: Data(DataType.String, 16, "Ready sword", "ソードを構える"),
    0x001BA494: Data(DataType.String, 16, "Take aim", "狙いをつける"),
    0x001BA4A4: Data(DataType.String, 12, "Snipe", "長距離狙撃"),
    0x001BA4B0: Data(DataType.String, 12, "Support", "支援攻撃"),
    0x001BA4BC: Data(DataType.String, 20, "Melee", "使徒を正面に捉える"),
    0x001BA4D0: Data(DataType.String, 16, "Close the gap", "間合いを詰める"),
    0x001BA4E0: Data(DataType.String, 8, "Rush", "突進"),
    0x001BA4E8: Data(DataType.String, 16, "Jump right", "右に飛びのく"),
    0x001BA4F8: Data(DataType.String, 16, "Jump left", "左に飛びのく"),
    0x001BA508: Data(DataType.String, 16, "Jump back", "バックジャンプ"),
    0x001BA518: Data(DataType.String, 12, "Turn right", "右ターン"),
    0x001BA524: Data(DataType.String, 12, "Turn left", "左ターン"),
    0x001BA530: Data(DataType.String, 12, "Change course", "方向転換"),
    0x001BA53C: Data(DataType.String, 20, "Release A.T. Field", "ΑΤフィールド全開"),
    0x001BA550: Data(DataType.String, 16, "Get heated", "闘志を燃やす"),
    0x001BA560: Data(DataType.String, 16, "Get motivated", "気合を入れる"),
    0x001BA570: Data(DataType.String, 16, "Feel better", "気を持ち直す"),
    0x001BA580: Data(DataType.String, 12, "Go carefully", "慎重に行く"),
    0x001BA58C: Data(DataType.String, 8, "Lose temper", "キレる"),
    0x001BA594: Data(DataType.String, 12, "Be afraid", "怖気づく"),
    0x001BA5A0: Data(DataType.String, 8, "Move!", "動け！"),
    0x001BA5A8: Data(DataType.String, 16, "Move! Move!", "動け！動け！"),
    0x001BA5B8: Data(DataType.String, 20, "Move! Move! Move it!", "動け！動け！動け！"),
    0x001BA5CC: Data(DataType.String, 16, "I don't want to die...", "死ぬのはイヤ…"),
    0x001BA5DC: Data(DataType.String, 20, "I don't want to die!", "死ぬのはイヤッ！"),
    0x001BA5F0: Data(DataType.String, 24, "I don't want to diiiiiie!", "死ぬのはイヤーーッ！"),
    0x001BA608: Data(DataType.String, 20, "Synch with Eva", "エヴァとシンクロ"),
    0x001BA61C: Data(DataType.String, 16, "Cheer Shinji on", "シンジを励ます"),
    0x001BA62C: Data(DataType.String, 16, "Cheer Asuka on", "アスカを励ます"),
    0x001BA63C: Data(DataType.String, 16, "Cheer Rei on", "レイを励ます"),
    0x001BA64C: Data(DataType.String, 16, "Cheer Toji on", "トウジを励ます"),
    0x001BA65C: Data(DataType.String, 16, "Cheer Kaworu on", "カヲルを励ます"),
    0x001BA66C: Data(DataType.String, 20, "Increase viewing range", "視界レンジを広げる"),
    0x001BA680: Data(DataType.String, 16, "Request support0", "サポートを要求"),
    0x001BA690: Data(DataType.String, 20, "Keep distance", "距離を空けさせる"),
    0x001BA6A4: Data(DataType.String, 20, "Walk (Small speed inc.)", "加速(速度増・小)"),
    0x001BA6B8: Data(DataType.String, 20, "Run (Med. speed inc.)", "増速(速度増・中)"),
    0x001BA6CC: Data(DataType.String, 24, "Dash (Large speed inc.)", "ダッシュ(速度増・大)"),
    0x001BA6E4: Data(DataType.String, 8, "Hop", "ホップ"),
    0x001BA6EC: Data(DataType.String, 12, "Step", "ステップ"),
    0x001BA6F8: Data(DataType.String, 12, "Jump", "ジャンプ"),
    0x001BA704: Data(DataType.String, 8, "--", "−−"),
    0x001BA70C: Data(DataType.String, 8, "More than %d", "%d以上"),
    0x001BA714: Data(DataType.String, 8, "%3d consumption", "%3d消費"),
    0x001BA71C: Data(DataType.String, 8, "%d~%d", "%d〜%d"),
    0x001BA724: Data(DataType.String, 8, "Less than %d", "%d以下"),
    0x001BB6B8: Data(DataType.String, 76, "Data receieved.\nFilesize: %d bytes\nPress any key.", "データを受信しました。\nファイルサイズ：%d bytes\n何かキーを押して下さい。\n"),
    0x001BB720: Data(DataType.String, 8, "Shinji", "シンジ"),
    0x001BB728: Data(DataType.String, 8, "Asuka", "アスカ"),
    0x001BB730: Data(DataType.String, 8, "Rei", "レイ"),
    0x001BB738: Data(DataType.String, 8, "Misato", "ミサト"),
    0x001BB740: Data(DataType.String, 12, "Gendo", "ゲンドウ"),
    0x001BB74C: Data(DataType.String, 8, "Fuyutsuki", "冬月"),
    0x001BB754: Data(DataType.String, 8, "Ritsuko", "リツコ"),
    0x001BB75C: Data(DataType.String, 8, "Maya", "マヤ"),
    0x001BB764: Data(DataType.String, 8, "Hyuga", "日向"),
    0x001BB76C: Data(DataType.String, 8, "Aoba", "青葉"),
    0x001BB774: Data(DataType.String, 8, "Kaji", "加持"),
    0x001BB77C: Data(DataType.String, 8, "Hikari", "ヒカリ"),
    0x001BB784: Data(DataType.String, 8, "Toji", "トウジ"),
    0x001BB78C: Data(DataType.String, 12, "Kensuke", "ケンスケ"),
    0x001BB798: Data(DataType.String, 8, "Kaworu", "カヲル"),
    0x001BB7A0: Data(DataType.String, 12, "Pen Pen", "ペンペン"),
    0x001BB7AC: Data(DataType.String, 16, "%s's transformation(%d)\n", "%sの変身(%d)\n"),
    0x001BB7BC: Data(DataType.String, 20, "Cannot transform %d\n", "変身できません %d\n"),
    0x001BB7D0: Data(DataType.String, 28, "Will be replaced.%d\n", "入れ替えを行ないます。%d\n"),
    0x001BB7EC: Data(DataType.String, 20, "Invalid data.", "無効なデータです。"),
    0x001BBC18: Data(DataType.String, 28, "[view]Character Init.", "[view ] キャラ初期化(事前)"),
    0x001BBC34: Data(DataType.String, 28, "[debug]Debug System", "[debug] デバッグシステム"),
    0x001BBC50: Data(DataType.String, 16, "[ctrl]BGM", "[ctrl ] ＢＧＭ"),
    0x001BBC60: Data(DataType.String, 20, "[anno]Anno Init.", "[anno ] 庵野初期化"),
    0x001BBC74: Data(DataType.String, 20, "[view]Attribute Data", "[view ] 属性データ"),
    0x001BBC88: Data(DataType.String, 28, "[Ctrl]Event Entry", "[Ctrl ] イベントエントリー"),
    0x001BBCA4: Data(DataType.String, 28, "[ctrl]Player Start Choice", "[ctrl ] プレイヤー起点選択"),
    0x001BBCC0: Data(DataType.String, 24, "[shell]Game Data", "[shell] ゲームデータ"),
    0x001BBCD8: Data(DataType.String, 24, "[view]Effect (Disp. Layer)", "[view ] Effect(表示層)"),
    0x001BBCF0: Data(DataType.String, 24, "[view]Map (Disp. Layer)", "[view ] マップ(表示層)"),
    0x001BBD08: Data(DataType.String, 28, "[view]Gimmick (Disp. Layer)", "[view ] ギミック(表示層)"),
    0x001BBD24: Data(DataType.String, 24, "[view]Character (Disp. Layer)", "[view ] キャラ(表示層)"),
    0x001BBD3C: Data(DataType.String, 24, "[view]2D Display Relation", "[view ] ２Ｄ表示関係"),
    0x001BBD54: Data(DataType.String, 24, "[model]2D Map Relation", "[model] ２Ｄマップ関係"),
    0x001BBD6C: Data(DataType.String, 24, "[model]Map (Logic Layer)", "[model] マップ(論理層)"),
    0x001BBD84: Data(DataType.String, 24, "[model]Character (Logic Layer)", "[model] キャラ(論理層)"),
    0x001BBD9C: Data(DataType.String, 28, "[model]Chara. Mvmt (Logic Layer)", "[model] キャラ移動(論理層)"),
    0x001BBDB8: Data(DataType.String, 28, "[model]Gimmick (Logic Layer)", "[model] ギミック(論理層)"),
    0x001BBDD4: Data(DataType.String, 20, "[model]Update Processing", "[model] 更新処理"),
    0x001BBDE8: Data(DataType.String, 28, "[model]Map Switch Proc.", "[model] マップスイッチ処理"),
    0x001BBE04: Data(DataType.String, 24, "[model]Movement Parameter", "[model] 移動パラメータ"),
    0x001BBE34: Data(DataType.String, 24, "[Ctrl]Angel Entry", "[Ctrl ] 使徒エントリー"),
    0x001BBE4C: Data(DataType.String, 20, "[Ctrl]Time Management", "[Ctrl ] 時間管理"),
    0x001BBE60: Data(DataType.String, 20, "[Ctrl]Start Point Select", "[Ctrl ] 起点選択"),
    0x001BBE74: Data(DataType.String, 20, "[Ctrl]Start Pt. Select PSP", "[Ctrl ] 起点選択PSP"),
    0x001BBE88: Data(DataType.String, 20, "[Ctrl]NPC Processing", "[Ctrl ] ＮＰＣ処理"),
    0x001BBE9C: Data(DataType.String, 24, "[Ctrl]IM Flow Processing", "[Ctrl ] ＩＭフロー処理"),
    0x001BBEB4: Data(DataType.String, 28, "[Ctrl]AI Controller", "[Ctrl ] ＡＩコントローラ"),
    0x001BBED0: Data(DataType.String, 28, "[Ctrl]Warning Processing", "[Ctrl ] もうだめぽ警告処理"),
    0x001BBEEC: Data(DataType.String, 24, "[Ctrl]Ireul Battle Proc.", "[Ctrl ] イロウル戦処理"),
    0x001BBF24: Data(DataType.String, 20, "[Ctrl]Shopping Basket", "[Ctrl ] 買い物籠"),
    0x001BBF38: Data(DataType.String, 20, "[Ctrl]NPC A.T. Bar", "[Ctrl ] NPCATバー"),
    0x001BC098: Data(DataType.String, 24, "Move trap stop\n", "トラップにより移動停止\n"),
    0x001BC278: Data(DataType.String, 28, "Move interrupt stop\n", "インタラプトにより移動停止\n"),
    0x001BC5AC: Data(DataType.String, 16, "Reserve start pt. %04d", "予約起点-%04d"),
    0x001BC5BC: Data(DataType.String, 24, "Desired start pt. %04d Want %s(%d)", "欲望起点-%04d 欲-%s(%d)"),
    0x001BC5D4: Data(DataType.String, 16, "Record desire %s\n", "欲望を記録 %s\n"), # MACHINE_TRANSLATED
    0x001BC5E8: Data(DataType.String, 12, " Field-%d.%d", " 場-%d.%d"), # MACHINE_TRANSLATED
    0x001BC5F4: Data(DataType.String, 8, " Pro-%d", " 予-%d"), # MACHINE_TRANSLATED
    0x001BC5FC: Data(DataType.String, 28, "Action return Normal move %d.%d\n", "行動復帰 通常移動 %d.%d\n"), # MACHINE_TRANSLATED
    0x001BC618: Data(DataType.String, 44, "Reservation IM discard by activation try counter IM-%04d\n", "起動トライカウンタにより予約IM破棄 IM-%04d\n"), # MACHINE_TRANSLATED
    0x001BC664: Data(DataType.String, 40, "Reserved start failure-%04d Hold due to passing\n", "予約起動失敗-%04d すれ違いにつき保留\n"), # MACHINE_TRANSLATED
    0x001BC68C: Data(DataType.String, 52, "Reservation start failure-%04d Map difference-%d Current-%d try=%d\n", "予約起動失敗-%04d マップ違い 目-%d 現-%d try=%d\n"), # MACHINE_TRANSLATED
    0x001BC6C0: Data(DataType.String, 52, "Reservation start failure-%04d Point difference (%d) Continue moving try=%d\n", "予約起動失敗-%04d ポイント違い(%d) 移動継続 try=%d\n"), # MACHINE_TRANSLATED
    0x001BC6F4: Data(DataType.String, 48, "Reserved start failure-%04d Start condition check failure try=%d\n", "予約起動失敗-%04d 起動条件チェック失敗 try=%d\n"), # MACHINE_TRANSLATED
    0x001BC724: Data(DataType.String, 16, "%dth thought", "%d回目の思考"), # MACHINE_TRANSLATED
    0x001BC734: Data(DataType.String, 20, "No IM to launch\n", "起動するIMがない\n"), # MACHINE_TRANSLATED
    0x001BC76C: Data(DataType.String, 8, "Progress:", "進×"),
    0x001BC774: Data(DataType.String, 8, "Story:", "条×"),
    0x001BC77C: Data(DataType.String, 8, "Re-election ×", "再選×"), # MACHINE_TRANSLATED
    0x001BC784: Data(DataType.String, 8, "Population:", "人口×"),
    0x001BC78C: Data(DataType.String, 8, "Straddle ×", "跨×"), # MACHINE_TRANSLATED
    0x001BC794: Data(DataType.String, 8, "Ma ×", "マ×"), # MACHINE_TRANSLATED
    0x001BC79C: Data(DataType.String, 8, "Transfer only", "移のみ"), # MACHINE_TRANSLATED
    0x001BC7A4: Data(DataType.String, 44, "Cancel starting point ignore=%d, IM-%04d %d\n", "起点選択キャンセル ignore=%d, IM-%04d %d\n"), # MACHINE_TRANSLATED
    0x001BC7F4: Data(DataType.String, 64, "Designates a map that cannot be entered in NPC mode. Cancel destination translation map=%d\n", "NPCモード時進入不可マップを指定。目的地翻訳をキャンセル map=%d\n"), # MACHINE_TRANSLATED
    0x001BC8B0: Data(DataType.String, 32, "Became object of thought correction.\n", "思考矯正の対象になりました。\n"),
    0x001BC90C: Data(DataType.String, 8, "Strength", "体力"),
    0x001BC914: Data(DataType.String, 8, "Thirst", "喉渇"),
    0x001BC91C: Data(DataType.String, 8, "Sleep", "睡眠"),
    0x001BC924: Data(DataType.String, 8, "Unpleasant", "嫌遠"),
    0x001BC92C: Data(DataType.String, 8, "Lust", "色欲"),
    0x001BC934: Data(DataType.String, 8, "Greed", "物欲"),
    0x001BC93C: Data(DataType.String, 8, "Avarice", "金欲"),
    0x001BC944: Data(DataType.String, 8, "Honor", "名誉"),
    0x001BC94C: Data(DataType.String, 8, "Lust for power", "力欲"),
    0x001BC954: Data(DataType.String, 8, "Self-love", "み好"),
    0x001BC95C: Data(DataType.String, 8, "Justice", "正義"),
    0x001BC964: Data(DataType.String, 8, "Love life", "恋生"),
    0x001BC96C: Data(DataType.String, 8, "Nothing", "何も"),
    0x001BC974: Data(DataType.String, 8, "Bathroom", "ＷＣ"),
    0x001BC97C: Data(DataType.String, 8, "Friendship", "友情"),
    0x001BC984: Data(DataType.String, 8, "Attachment", "親愛"),
    0x001BC9D0: Data(DataType.String, 20, "Next map calculation %d\n", "隣のマップ算出 %d\n"), # MACHINE_TRANSLATED
    0x001BC9E4: Data(DataType.String, 20, "Calculate my room %d\n", "自分の部屋算出 %d\n"), # MACHINE_TRANSLATED
    0x001BC9F8: Data(DataType.String, 24, "Current map calculation %d\n", "現在のマップ算出 %d\n"), # MACHINE_TRANSLATED
    0x001BCA10: Data(DataType.String, 32, "Mysterious maximum character map calculation failure\n", "謎最大キャラマップ算出 失敗\n"), # MACHINE_TRANSLATED
    0x001BCA30: Data(DataType.String, 32, "Maximum mystery character map calculation %d (%s)\n", "謎最大キャラマップ算出 %d (%s)\n"), # MACHINE_TRANSLATED
    0x001BCA50: Data(DataType.String, 28, "Someone's map calculation failed\n", "誰か居るマップ算出 失敗\n"), # MACHINE_TRANSLATED
    0x001BCA6C: Data(DataType.String, 24, "Calculate the map where someone is %d\n", "誰か居るマップ算出 %d\n"), # MACHINE_TRANSLATED
    0x001BCA84: Data(DataType.String, 36, "Map calculation of favored opposite sex %d (%s)\n", "好意が高い異性のマップ算出 %d (%s)\n"), # MACHINE_TRANSLATED
    0x001BCAA8: Data(DataType.String, 36, "Highly favored opposite sex map failure\n", "好意が高い異性のマップ算出 失敗\n"), # MACHINE_TRANSLATED
    0x001BCACC: Data(DataType.String, 36, "Comparing same favored maps %d (%s)\n", "好意が高い同性のマップ算出 %d (%s)\n"), # MACHINE_TRANSLATED
    0x001BCAF0: Data(DataType.String, 36, "Highly favored same-sex map failure\n", "好意が高い同性のマップ算出 失敗\n"), # MACHINE_TRANSLATED
    0x001BCB14: Data(DataType.String, 40, "Map calculation of characters with high interest %d (%s)\n", "関心が高いキャラのマップ算出 %d (%s)\n"), # MACHINE_TRANSLATED
    0x001BCB3C: Data(DataType.String, 36, "Failed map calculation for characters with high interest\n", "関心が高いキャラのマップ算出 失敗\n"), # MACHINE_TRANSLATED
    0x001BCC54: Data(DataType.String, 24, "%s was discharged from the hospital.", "%sが退院できました。"),
    0x001BCD08: Data(DataType.String, 32, "IM execution memory input IM-%04d map=%d\n", "IM実行記憶投入 IM-%04d map=%d\n"), # MACHINE_TRANSLATED
    0x001BCD28: Data(DataType.String, 36, "IM execution (without memory) IM-%04d map=%d\n", "IM実行(記憶なし) IM-%04d map=%d\n"), # MACHINE_TRANSLATED
    0x001BCD7C: Data(DataType.String, 40, "It will be a random move Destmap=%d.\n", "ランダム移動になります Destmap=%d。\n"), # MACHINE_TRANSLATED
    0x001BCDA4: Data(DataType.String, 24, "Do not enter map %d\n", "マップ %d には進入禁止\n"), # MACHINE_TRANSLATED
    0x001BCDBC: Data(DataType.String, 28, "Inability to select map points.\n", "マップポイントの選択不能。\n"), # MACHINE_TRANSLATED
    0x001BCDD8: Data(DataType.String, 52, "Map changes to one to which the selected point belongs %d->%d\n", "マップは選んだポイントが属するものに変更 %d->%d\n"), # MACHINE_TRANSLATED
    0x001BCE0C: Data(DataType.String, 28, "It's too close, so movement is restricted.\n", "近距離すぎるので移動制限。\n"), # MACHINE_TRANSLATED
    0x001BCE28: Data(DataType.String, 40, "Calculate destination from IM %d (%d.%02d, %d,%02d)\n", "IMより移動先算出 %d (%d.%02d, %d,%02d)\n"), # MACHINE_TRANSLATED
    0x001BCE50: Data(DataType.String, 64, "It failed in pulling the IM point by normal processing. chr=%d, im=%d\n", "通常処理でＩＭポイントをひっぱって来るのに失敗。chr=%d, im=%d\n"), # MACHINE_TRANSLATED
    0x001BCE90: Data(DataType.String, 56, "Found %d IM-%d map points from map %d\n", "マップ%dよりIM-%dのマップポイントを%d個発見しました\n"), # MACHINE_TRANSLATED
    0x001BCEC8: Data(DataType.String, 68, "Map point (%d) cannot be found in the map (%d) specified in the origin selection.\n", "起点選択で指定したマップ(%d)にマップポイント(%d)が見つかりません。\n"), # MACHINE_TRANSLATED
    0x001BCF0C: Data(DataType.String, 48, "Destination map is prohibited by the master sys Transfer destination transfer %d to %d\n", "目的マップが主人シスで禁止 移動先振替 %d to %d\n"), # MACHINE_TRANSLATED
    0x001BCF3C: Data(DataType.String, 44, "Current map is forced to exit due to master syst %d to %d\n", "現在マップが主人シスで退出を強制 %d to %d\n"), # MACHINE_TRANSLATED
    0x001BCF98: Data(DataType.String, 40, "Trap for %s failed.\n", "%s に対してのトラップが失敗しました。\n"), # MACHINE_TRANSLATED
    0x001BCFE0: Data(DataType.String, 48, "Transferred to random due to overcrowding (Dstmap=%d)\n", "人口過密によりランダム移動に振替(Dstmap=%d)\n"), # MACHINE_TRANSLATED
    0x001BD010: Data(DataType.String, 36, "There is a problem in specifying the destination map. (%d)\n", "行き先マップの指定に問題が。(%d)\n"), # MACHINE_TRANSLATED
    0x001BD034: Data(DataType.String, 36, "Transfer to random movement (Dstmap=%d/%d)\n", "ランダム移動に振替(Dstmap=%d/%d)\n"), # MACHINE_TRANSLATED
    0x001BD0AC: Data(DataType.String, 12, "Default Selection", "起点選択"),
    0x001BD0BC: Data(DataType.String, 12, "Walking Movement", "歩いて移動"),
    0x001BD0C8: Data(DataType.String, 12, "Raise a topic", "話題をふる"),
    0x001BD0D4: Data(DataType.String, 12, "(Missing Number)", "（欠番）"),
    0x001BD0E0: Data(DataType.String, 12, "Ignore", "無視する"),
    0x001BD0EC: Data(DataType.String, 16, "Approach PsvChr", "受動者に近づく"),
    0x001BD0FC: Data(DataType.String, 16, "Dismissive response", "そっけない返事"),
    0x001BD10C: Data(DataType.String, 24, "Chew out PsvChr for being weak", "ふがいない受動者を叱る"),
    0x001BD124: Data(DataType.String, 20, "End conversation", "会話を切り上げる"),
    0x001BD138: Data(DataType.String, 12, "Silently ignore", "黙って無視"),
    0x001BD144: Data(DataType.String, 16, "Regret distance", "つれなさを嘆く"),
    0x001BD154: Data(DataType.String, 8, "Yield in defeat", "ヘコむ"),
    0x001BD15C: Data(DataType.String, 12, "Stand your ground", "動じない"),
    0x001BD168: Data(DataType.String, 8, "Feel awkward", "照れる"),
    0x001BD170: Data(DataType.String, 16, "Avert gaze", "視線を逸らす"),
    0x001BD180: Data(DataType.String, 12, "Smile", "笑いかける"),
    0x001BD18C: Data(DataType.String, 16, "Enter the labyrinth of the heart", "心の迷宮に入る"),
    0x001BD19C: Data(DataType.String, 20, "Prize out confidential information", "機密情報を聞き出す"),
    0x001BD1B0: Data(DataType.String, 20, "Leave Commander's office", "総司令公務室を出る"),
    0x001BD1C4: Data(DataType.String, 20, "I don't get it", "わからないと言う"),
    0x001BD1D8: Data(DataType.String, 12, "Warn", "警告する"),
    0x001BD1E4: Data(DataType.String, 16, "End the conversation", "話を切り上げる"),
    0x001BD1F4: Data(DataType.String, 20, "Share confidential info", "機密情報を教える"),
    0x001BD208: Data(DataType.String, 16, "Get angry", "怒ってみせる"),
    0x001BD218: Data(DataType.String, 12, "Let go of", "身を離す"),
    0x001BD224: Data(DataType.String, 12, "Kiss", "キスする"),
    0x001BD230: Data(DataType.String, 12, "Hug", "抱きしめる"),
    0x001BD23C: Data(DataType.String, 12, "Hold hand", "手を握る"),
    0x001BD248: Data(DataType.String, 12, "Whisper", "ささやく"),
    0x001BD254: Data(DataType.String, 16, "Hug tightly", "強く抱きしめる"),
    0x001BD264: Data(DataType.String, 16, "Wrap finger", "指をからめる"),
    0x001BD274: Data(DataType.String, 12, "Reject", "拒絶する"),
    0x001BD280: Data(DataType.String, 20, "Ask what happened", "どうしたと尋ねる"),
    0x001BD294: Data(DataType.String, 20, "Be embarrassed over nothing", "何でもないと照れる"),
    0x001BD2A8: Data(DataType.String, 24, "Ask for personal favor", "自分への好意を尋ねる"),
    0x001BD2C0: Data(DataType.String, 24, "Ask why they avoid you", "自分を避ける理由を聞く"),
    0x001BD2D8: Data(DataType.String, 16, "Don't answer", "何も答えない"),
    0x001BD2E8: Data(DataType.String, 20, "Say it's no good now", "今はダメだと言う"),
    0x001BD2FC: Data(DataType.String, 16, "Answer favorably", "好意的に答える"),
    0x001BD30C: Data(DataType.String, 16, "Voice hate", "嫌いだと言う"),
    0x001BD31C: Data(DataType.String, 16, "Voice happiness", "嬉しいと言う"),
    0x001BD32C: Data(DataType.String, 20, "Accuse of lying", "うそつきだと言う"),
    0x001BD340: Data(DataType.String, 20, "Voice Dislike", "自分も嫌いだと言う"),
    0x001BD354: Data(DataType.String, 20, "Embrace PsvChr", "受動者に抱きつく"),
    0x001BD368: Data(DataType.String, 16, "Look happy", "喜んでみせる"),
    0x001BD378: Data(DataType.String, 12, "Chastise them", "たしなめる"),
    0x001BD384: Data(DataType.String, 16, "Chat mirthfully", "気分良く話す"),
    0x001BD394: Data(DataType.String, 28, "Treat in an over-familiar manner", "なれなれしい態度で接する"),
    0x001BD3B0: Data(DataType.String, 24, "Give a dismissive response", "そっけない返事をする"),
    0x001BD3C8: Data(DataType.String, 20, "Give an icy response", "冷たい返事をする"),
    0x001BD3DC: Data(DataType.String, 16, "Cock your head", "首をかしげる"),
    0x001BD3EC: Data(DataType.String, 20, "Worry over PsvChr", "受動者を心配する"),
    0x001BD400: Data(DataType.String, 24, "Study PsvChr's condition", "受動者の様子を観察する"),
    0x001BD418: Data(DataType.String, 20, "Apologize for returning", "我に返ってあやまる"),
    0x001BD42C: Data(DataType.String, 20, "Space out", "ぼーっとしている"),
    0x001BD440: Data(DataType.String, 20, "Look tearful", "泣きそうな顔をする"),
    0x001BD454: Data(DataType.String, 20, "It's nothing", "何でもないと言う"),
    0x001BD468: Data(DataType.String, 24, "Talk in dark tone", "暗い調子で話しかける"),
    0x001BD480: Data(DataType.String, 28, "Say you're not in the mood", "そんな気分じゃないと言う"),
    0x001BD49C: Data(DataType.String, 24, "Take offense at their attitude", "相手の態度に腹を立てる"),
    0x001BD4B4: Data(DataType.String, 16, "Be in good mood", "上機嫌になる"),
    0x001BD4C4: Data(DataType.String, 20, "Feign ignorance", "知らんふりをする"),
    0x001BD4D8: Data(DataType.String, 24, "Talk over", "なぐさめの声をかける"),
    0x001BD4F0: Data(DataType.String, 8, "Cheer them on", "励ます"),
    0x001BD4F8: Data(DataType.String, 24, "You don't have to say anything", "言わなくていいと言う"),
    0x001BD510: Data(DataType.String, 12, "Say nothing", "黙っている"),
    0x001BD51C: Data(DataType.String, 28, "It's nothing after all", "やっぱり何でもないと言う"),
    0x001BD538: Data(DataType.String, 12, "Worry", "心配する"),
    0x001BD544: Data(DataType.String, 16, "Think they're weird", "変な奴と思う"),
    0x001BD554: Data(DataType.String, 12, "Warn them", "注意する"),
    0x001BD560: Data(DataType.String, 16, "Sigh", "ため息をつく"),
    0x001BD570: Data(DataType.String, 12, "Bluntly refuse", "突き放す"),
    0x001BD57C: Data(DataType.String, 20, "Tell them not to worry", "気にするなと言う"),
    0x001BD590: Data(DataType.String, 12, "Acknowledge", "了解する"),
    0x001BD59C: Data(DataType.String, 12, "Touch their shoulder", "肩を叩く"),
    0x001BD5A8: Data(DataType.String, 8, "What?", "なに？"),
    0x001BD5B0: Data(DataType.String, 20, "Casually disengage", "それとなく離れる"),
    0x001BD5C4: Data(DataType.String, 12, "Take a bath", "入浴する"),
    0x001BD5D0: Data(DataType.String, 12, "Sitting down", "座っている"),
    0x001BD5DC: Data(DataType.String, 20, "Disrupt their studies", "勉強の邪魔をする"),
    0x001BD5F0: Data(DataType.String, 12, "Complain", "文句を言う"),
    0x001BD5FC: Data(DataType.String, 16, "Study quietly", "黙って勉強する"),
    0x001BD60C: Data(DataType.String, 16, "Rise from chair", "椅子から立つ"),
    0x001BD61C: Data(DataType.String, 12, "Keep company", "相手をする"),
    0x001BD628: Data(DataType.String, 24, "Reject opponent", "相手は出来ないと拒む"),
    0x001BD640: Data(DataType.String, 12, "Give up", "あきらめる"),
    0x001BD64C: Data(DataType.String, 20, "Let's go fishing", "一緒に釣りに行こう"),
    0x001BD660: Data(DataType.String, 24, "System: School Studies", "システム：学校のお勉強"),
    0x001BD678: Data(DataType.String, 12, "Relax", "くつろぐ"),
    0x001BD684: Data(DataType.String, 20, "Watch T.V. together", "一緒にテレビを観る"),
    0x001BD698: Data(DataType.String, 20, "Change the channel", "チャンネルを変える"),
    0x001BD6AC: Data(DataType.String, 20, "Complain about what's on", "番組の文句を語る"),
    0x001BD6C0: Data(DataType.String, 24, "Complain about change of channel", "チャンネル変更に文句"),
    0x001BD6D8: Data(DataType.String, 20, "Watch T.V. in silence", "黙ってテレビを観る"),
    0x001BD6EC: Data(DataType.String, 16, "Show interest in conversation", "話に興味を示す"),
    0x001BD6FC: Data(DataType.String, 16, "Join conversation", "自分も雑談する"),
    0x001BD70C: Data(DataType.String, 24, "Check location with mobile phone", "携帯電話で所在を確認"),
    0x001BD724: Data(DataType.String, 12, "Sit in chair", "椅子に座る"),
    0x001BD730: Data(DataType.String, 20, "Seated in chair", "椅子に座っている"),
    0x001BD744: Data(DataType.String, 20, "Ask about school grades", "学校の成績を尋ねる"),
    0x001BD758: Data(DataType.String, 20, "They're pretty good", "かなりいいと答える"),
    0x001BD76C: Data(DataType.String, 20, "They're okay", "まあまあと答える"),
    0x001BD780: Data(DataType.String, 16, "They're bad", "悪いと答える"),
    0x001BD790: Data(DataType.String, 16, "They're awful", "最悪だと答える"),
    0x001BD7A0: Data(DataType.String, 20, "Debug: Labyrinth of the Heart", "デバック：心の迷宮"),
    0x001BD7B4: Data(DataType.String, 20, "System: Angel Advent", "システム：使徒出現"),
    0x001BD7C8: Data(DataType.String, 12, "I'm home.", "ただいま"),
    0x001BD7D4: Data(DataType.String, 28, "Care about others' opinions", "他人からの評価を気にする"),
    0x001BD7F0: Data(DataType.String, 16, "Open fusuma", "ふすまを開ける"),
    0x001BD800: Data(DataType.String, 16, "Open sliding door", "引き戸を開ける"),
    0x001BD810: Data(DataType.String, 20, "Open the curtain", "カーテンを開ける"),
    0x001BD824: Data(DataType.String, 12, "Sleep-talk", "寝言を言う"),
    0x001BD830: Data(DataType.String, 8, "Forced smile", "苦笑い"),
    0x001BD838: Data(DataType.String, 20, "Discuss present status with PsvChr", "受動者と現状会話"),
    0x001BD84C: Data(DataType.String, 12, "Thank you", "ありがとう"),
    0x001BD858: Data(DataType.String, 20, "Request your allowance", "小遣いを要求する"),
    0x001BD86C: Data(DataType.String, 16, "Hand over allowance", "小遣いを渡す"),
    0x001BD87C: Data(DataType.String, 24, "No money to give", "お金が無くて渡せない"),
    0x001BD894: Data(DataType.String, 24, "Assure that it's okay", "大丈夫だと安心させる"),
    0x001BD8AC: Data(DataType.String, 24, "Become quiet", "気まずそうに沈黙する"),
    0x001BD8C4: Data(DataType.String, 24, "Ask PsvChr to collect information", "受動者に情報収集依頼"),
    0x001BD8DC: Data(DataType.String, 12, "Thank them", "礼を言う"),
    0x001BD8E8: Data(DataType.String, 16, "Turn on the lights", "照明をつける"),
    0x001BD8F8: Data(DataType.String, 8, "Decline", "断る"),
    0x001BD900: Data(DataType.String, 12, "Turn off the lights", "照明を消す"),
    0x001BD90C: Data(DataType.String, 24, "Whisper into Gendo's ear", "ゲンドウに耳打ちする"),
    0x001BD924: Data(DataType.String, 12, "Quite right", "そうだな"),
    0x001BD930: Data(DataType.String, 24, "Don't worry, things are going as planned", "心配ない、計画通りだ"),
    0x001BD948: Data(DataType.String, 16, "Got a question?", "何か質問は？"),
    0x001BD958: Data(DataType.String, 12, "State your opinion", "意見を言う"),
    0x001BD964: Data(DataType.String, 16, "Voice objections", "異議を唱える"),
    0x001BD974: Data(DataType.String, 20, "Announce tactical decisions", "作戦決定を通告する"),
    0x001BD988: Data(DataType.String, 12, "Retort", "言い返す"),
    0x001BD994: Data(DataType.String, 16, "Reluctantly obey", "しぶしぶ従う"),
    0x001BD9A4: Data(DataType.String, 16, "Revise strategy", "作戦を変更する"),
    0x001BD9B4: Data(DataType.String, 28, "System: Post-Harmonics", "システム：ハーモニクス後"),
    0x001BD9D0: Data(DataType.String, 20, "Sit down and eat", "着席して食事をする"),
    0x001BD9E4: Data(DataType.String, 28, "Ask if you can eat next to them", "横で食事する許可を求める"),
    0x001BDA00: Data(DataType.String, 12, "Agree", "了承する"),
    0x001BDA0C: Data(DataType.String, 20, "Sit next to them and eat", "横に座って食事する"),
    0x001BDA20: Data(DataType.String, 16, "Keep eating", "食事を続ける"),
    0x001BDA30: Data(DataType.String, 20, "Quit piloting", "パイロットやめます"),
    0x001BDA44: Data(DataType.String, 12, "Consent", "承諾する"),
    0x001BDA50: Data(DataType.String, 20, "Question their decision", "決意を問いただす"),
    0x001BDA64: Data(DataType.String, 24, "System: Leaving and Returning Processing", "システム：退場復帰処理"),
    0x001BDA7C: Data(DataType.String, 24, "I won't change my mind", "決意は変わらないと言う"),
    0x001BDA94: Data(DataType.String, 20, "It's not actually true", "本当はウソだと言う"),
    0x001BDAA8: Data(DataType.String, 8, "Get mad", "怒る"),
    0x001BDAB0: Data(DataType.String, 16, "Vent to PsvChr", "受動者に愚痴る"),
    0x001BDAC0: Data(DataType.String, 12, "Agree", "同意する"),
    0x001BDACC: Data(DataType.String, 12, "Feel doubtful", "疑問に思う"),
    0x001BDAD8: Data(DataType.String, 16, "Keep venting", "愚痴を続ける"),
    0x001BDAE8: Data(DataType.String, 20, "Also say nothing", "自分も黙っている"),
    0x001BDAFC: Data(DataType.String, 20, "Want to know the truth?", "真実を知りたいか？"),
    0x001BDB10: Data(DataType.String, 8, "Yes", "はい"),
    0x001BDB18: Data(DataType.String, 8, "No", "いいえ"),
    0x001BDB20: Data(DataType.String, 24, "Ask if they really want to know", "本当に知りたいか尋ねる"),
    0x001BDB38: Data(DataType.String, 16, "Implicitly refuse", "それとなく断る"),
    0x001BDB48: Data(DataType.String, 20, "Just have to know", "どうしても知りたい"),
    0x001BDB5C: Data(DataType.String, 24, "Give opinion brief to PsvChr", "受動者に意見書を渡す"),
    0x001BDB74: Data(DataType.String, 20, "Accept opinion brief", "意見書を受け取る"),
    0x001BDB88: Data(DataType.String, 20, "Tear up opinion brief", "意見書を破り捨てる"),
    0x001BDB9C: Data(DataType.String, 24, "Don't accept opinion brief", "意見書を受け取らない"),
    0x001BDBB4: Data(DataType.String, 16, "Entrust them with opinion brief", "意見書を任せる"),
    0x001BDBC4: Data(DataType.String, 20, "Thank politely", "よろしくお願いする"),
    0x001BDBD8: Data(DataType.String, 20, "Tentatively accept", "とりあえず受け取る"),
    0x001BDBEC: Data(DataType.String, 16, "Reject opinion brief", "意見書を拒む"),
    0x001BDBFC: Data(DataType.String, 12, "Apologize", "あやまる"),
    0x001BDC08: Data(DataType.String, 12, "Lash out", "逆ギレする"),
    0x001BDC14: Data(DataType.String, 8, "Shut up", "黙る"),
    0x001BDC1C: Data(DataType.String, 20, "Review opinion brief", "意見書を審査する"),
    0x001BDC30: Data(DataType.String, 20, "Ignore because it's annoying", "ウザイので無視する"),
    0x001BDC44: Data(DataType.String, 16, "Ask if they're working", "仕事中か尋ねる"),
    0x001BDC54: Data(DataType.String, 12, "Reply", "返事を返す"),
    0x001BDC60: Data(DataType.String, 16, "Get mad about nuisance", "邪魔だと怒る"),
    0x001BDC70: Data(DataType.String, 16, "Keep working", "仕事を再開する"),
    0x001BDC80: Data(DataType.String, 20, "Study with PsvChr", "受動者と一緒に勉強"),
    0x001BDC94: Data(DataType.String, 20, "Study together", "一緒に勉強をする"),
    0x001BDCA8: Data(DataType.String, 24, "Offer to review lessons", "授業の復習を持ちかける"),
    0x001BDCC0: Data(DataType.String, 24, "Review lessons together", "一緒に授業の復習をする"),
    0x001BDCD8: Data(DataType.String, 24, "Offer to do combat training", "戦闘訓練を持ちかける"),
    0x001BDCF0: Data(DataType.String, 24, "Do combat training together", "一緒に戦闘訓練をする"),
    0x001BDD08: Data(DataType.String, 20, "Ask to do research together", "調査の協力を求める"),
    0x001BDD1C: Data(DataType.String, 24, "Look into confidential info", "一緒に機密情報の調査"),
    0x001BDD34: Data(DataType.String, 24, "System: Go to school", "システム：学校へ行く"),
    0x001BDD4C: Data(DataType.String, 28, "System: NPC goes to school", "システム：ＮＰＣ学校へ行く"),
    0x001BDD68: Data(DataType.String, 20, "Flatter PsvChr", "受動者をおだてる"),
    0x001BDD7C: Data(DataType.String, 16, "Let it go to your head", "いい気になる"),
    0x001BDD8C: Data(DataType.String, 20, "React negatively", "ネガティブな反応"),
    0x001BDDA0: Data(DataType.String, 20, "Watch who's sleeping", "寝ているのを見る"),
    0x001BDDB4: Data(DataType.String, 12, "Sleeping", "寝ている"),
    0x001BDDC0: Data(DataType.String, 20, "Take care of business", "トイレで用を足す"),
    0x001BDDD4: Data(DataType.String, 16, "Ring the doorbell", "呼び鈴を押す"),
    0x001BDDE4: Data(DataType.String, 16, "Force strategy", "作戦を強行する"),
    0x001BDDF4: Data(DataType.String, 16, "Borrow toilet", "トイレを借りる"),
    0x001BDE04: Data(DataType.String, 20, "Suit partner", "テキトーに相手する"),
    0x001BDE18: Data(DataType.String, 16, "Watch T.V.", "テレビを観る"),
    0x001BDE28: Data(DataType.String, 16, "Open the fridge", "冷蔵庫を開ける"),
    0x001BDE38: Data(DataType.String, 16, "Vent on the wall", "壁に八つ当たり"),
    0x001BDE48: Data(DataType.String, 24, "Eat at the table", "テーブルで食事をする"),
    0x001BDE60: Data(DataType.String, 16, "Share meal", "食事にあやかる"),
    0x001BDE70: Data(DataType.String, 12, "Thought", "考えごと"),
    0x001BDE7C: Data(DataType.String, 8, "Sleep", "寝る"),
    0x001BDE84: Data(DataType.String, 12, "Take a bath", "風呂に入る"),
    0x001BDE90: Data(DataType.String, 12, "Study", "勉強する"),
    0x001BDE9C: Data(DataType.String, 12, "Run away from home", "家出する"),
    0x001BDEA8: Data(DataType.String, 8, "Sleeping", "睡眠中"),
    0x001BDEB0: Data(DataType.String, 24, "Be mindful of others' circumstances", "他人の様子を心にとめる"),
    0x001BDEC8: Data(DataType.String, 24, "Keep pretending to be out", "さらに居留守を決め込む"),
    0x001BDEE0: Data(DataType.String, 12, "Invite them in", "招き入れる"),
    0x001BDEEC: Data(DataType.String, 20, "Pretend to be out", "居留守を決め込む"),
    0x001BDF00: Data(DataType.String, 20, "Beg them off", "理由をつけて断る"),
    0x001BDF14: Data(DataType.String, 12, "Leave", "立ち去る"),
    0x001BDF20: Data(DataType.String, 16, "Knock again", "繰り返し叩く"),
    0x001BDF30: Data(DataType.String, 12, "Keep after them", "食い下がる"),
    0x001BDF3C: Data(DataType.String, 20, "Return downtrodden", "ヘコみながら帰る"),
    0x001BDF50: Data(DataType.String, 12, "Disturb", "お邪魔する"),
    0x001BDF5C: Data(DataType.String, 16, "Reluctantly open", "しぶしぶ開ける"),
    0x001BDF6C: Data(DataType.String, 16, "Absolutely refuse", "断固拒否する"),
    0x001BDF7C: Data(DataType.String, 12, "Item", "アイテム"),
    0x001BDF88: Data(DataType.String, 20, "Present an item", "アイテムを差し出す"),
    0x001BDF9C: Data(DataType.String, 24, "What's it for?", "それがどうしたと言う"),
    0x001BDFB4: Data(DataType.String, 20, "It's a present\"", "プレゼントだと言う"),
    0x001BDFC8: Data(DataType.String, 20, "I'm just showing it", "見せただけと言う"),
    0x001BDFDC: Data(DataType.String, 16, "Gladly accept", "喜んで受け取る"),
    0x001BDFEC: Data(DataType.String, 16, "Don't need it", "いらないと言う"),
    0x001BDFFC: Data(DataType.String, 24, "Please take it", "受け取って欲しいと言う"),
    0x001BE014: Data(DataType.String, 24, "Accept without complaint", "しょうがなく受け取る"),
    0x001BE02C: Data(DataType.String, 16, "Keep your cool", "平然としている"),
    0x001BE03C: Data(DataType.String, 24, "It actually is a present", "本当はプレゼントと言う"),
    0x001BE054: Data(DataType.String, 16, "Feel disappointed", "拍子抜けする"),
    0x001BE064: Data(DataType.String, 16, "Accept with pleasant surprise", "呆れて受け取る"),
    0x001BE074: Data(DataType.String, 24, "Feel nervous about the Angels' appearance", "使徒の出現に緊張する"),
    0x001BE08C: Data(DataType.String, 16, "Head to headquarters", "本部に向かう"),
    0x001BE09C: Data(DataType.String, 20, "Hear out", "何しに来たかを聞く"),
    0x001BE0B0: Data(DataType.String, 12, "Request sortie", "出撃要請"),
    0x001BE0BC: Data(DataType.String, 16, "Don't call", "呼び出しはない"),
    0x001BE0CC: Data(DataType.String, 24, "I want to go", "行かせて欲しいと頼む"),
    0x001BE0E4: Data(DataType.String, 24, "I am useful", "自分は役に立つと言う"),
    0x001BE0FC: Data(DataType.String, 24, "I can do more than support", "援護ぐらい出来ると言う"),
    0x001BE114: Data(DataType.String, 16, "Authorize sortie", "出撃を許可する"),
    0x001BE124: Data(DataType.String, 16, "Go reluctantly", "しぶしぶ行く"),
    0x001BE134: Data(DataType.String, 12, "Don't go", "行かない"),
    0x001BE140: Data(DataType.String, 20, "Report hospital discharge to PsvChr", "退院を受動者に報告"),
    0x001BE154: Data(DataType.String, 24, "Worry about PsvChr's hospital discharge", "退院した受動者を気遣う"),
    0x001BE16C: Data(DataType.String, 16, "Ask about the situation", "状況を尋ねる"),
    0x001BE17C: Data(DataType.String, 20, "Say it's fine", "大丈夫だと答える"),
    0x001BE190: Data(DataType.String, 20, "Ask if the going's been tough", "大変だったか尋ねる"),
    0x001BE1A4: Data(DataType.String, 20, "Because I'm the ○th one", "私、○人目だから"),
    0x001BE1B8: Data(DataType.String, 24, "Things aren't too good", "あまりよくないと答える"),
    0x001BE1D0: Data(DataType.String, 8, "Smile", "微笑む"),
    0x001BE1D8: Data(DataType.String, 20, "Take care", "気をつけてと言う"),
    0x001BE1EC: Data(DataType.String, 28, "Say that caring isn't enough", "気遣うほどでもないと言う"),
    0x001BE208: Data(DataType.String, 28, "It's been difficult in its way", "それなりに辛かったと言う"),
    0x001BE224: Data(DataType.String, 20, "Be shocked by Rei's words", "レイの言葉に驚く"),
    0x001BE238: Data(DataType.String, 12, "Be completely stunned", "愕然となる"),
    0x001BE244: Data(DataType.String, 16, "Nod silently", "黙ってうなずく"),
    0x001BE254: Data(DataType.String, 24, "No need to worry", "心配の必要は無いと言う"),
    0x001BE26C: Data(DataType.String, 20, "Awkward silence", "気まずそうに黙る"),
    0x001BE280: Data(DataType.String, 20, "Ask what they're getting", "何を食べるか尋ねる"),
    0x001BE294: Data(DataType.String, 20, "Decide what to do", "何にするか決める"),
    0x001BE2A8: Data(DataType.String, 16, "I'm at a loss", "何がいいか迷う"),
    0x001BE2B8: Data(DataType.String, 24, "Ask if it's delicious", "美味しいものかと尋ねる"),
    0x001BE2D0: Data(DataType.String, 16, "Speak highly", "なかなかと言う"),
    0x001BE2E0: Data(DataType.String, 24, "I wouldn't recommend it...", "おすすめはしないと言う"),
    0x001BE2F8: Data(DataType.String, 16, "Sit at table", "テーブルに着く"),
    0x001BE308: Data(DataType.String, 20, "Rise from table", "テーブルから立つ"),
    0x001BE31C: Data(DataType.String, 16, "Excuse yourself", "おいとまする"),
    0x001BE32C: Data(DataType.String, 24, "Greet PsvChr casually", "受動者に軽く挨拶する"),
    0x001BE344: Data(DataType.String, 12, "Reply", "返事をする"),
    0x001BE350: Data(DataType.String, 24, "Give PsvChr their allowance", "受動者に小遣いを渡す"),
    0x001BE368: Data(DataType.String, 16, "Shop", "買い物をする"),
    0x001BE378: Data(DataType.String, 20, "Talk to the clerk", "店員に話しかける"),
    0x001BE38C: Data(DataType.String, 12, "Check out", "清算する"),
    0x001BE398: Data(DataType.String, 20, "Finish overtime work at home", "家で残業を片付ける"),
    0x001BE3AC: Data(DataType.String, 20, "Deal with written apologies", "始末書を処理する"),
    0x001BE3C0: Data(DataType.String, 24, "Claim Eva maintenance budget", "エヴァの補修予算請求"),
    0x001BE3D8: Data(DataType.String, 28, "Claim Tokyo-3 repairs budget", "第３新東京市復興予算請求"),
    0x001BE3F4: Data(DataType.String, 20, "Dummy Plug Research", "ダミープラグの研究"),
    0x001BE408: Data(DataType.String, 20, "Operational Time Extension Research", "稼動時間の延長研究"),
    0x001BE41C: Data(DataType.String, 24, "A.T. Field Morphing Test", "ΑΤフィールド変形試験"),
    0x001BE434: Data(DataType.String, 24, "A.T. Field Amplification Test", "ΑΤフィールド増幅試験"),
    0x001BE44C: Data(DataType.String, 20, "Operator Duties", "オペレーター業務"),
    0x001BE460: Data(DataType.String, 12, "Commander Duties", "司令業務"),
    0x001BE46C: Data(DataType.String, 12, "Deputy Commander Duties", "副司令業務"),
    0x001BE478: Data(DataType.String, 24, "Create forged document or card", "偽造書類、カードを作る"),
    0x001BE490: Data(DataType.String, 16, "Hack", "ハッキングする"),
    0x001BE4A0: Data(DataType.String, 16, "Buy juice", "ジュースを買う"),
    0x001BE4B0: Data(DataType.String, 24, "Try doting on Pen Pen", "ペンペンにかまってみる"),
    0x001BE4C8: Data(DataType.String, 20, "Wonder", "不思議そうにする"),
    0x001BE4DC: Data(DataType.String, 16, "Ignore and disengage", "無視して離れる"),
    0x001BE4EC: Data(DataType.String, 24, "Stroke head", "よしよしと頭をなでる"),
    0x001BE504: Data(DataType.String, 12, "Be cynical", "皮肉を言う"),
    0x001BE510: Data(DataType.String, 20, "Feel a little empty", "ちょっとさびしい"),
    0x001BE524: Data(DataType.String, 24, "Leave Pen Pen as is", "ペンペンの事はほっとく"),
    0x001BE53C: Data(DataType.String, 20, "Pull PsvChr close", "受動者にすりよる"),
    0x001BE550: Data(DataType.String, 16, "What's wrong?", "どうしたの？"), # MACHINE_TRANSLATED
    0x001BE560: Data(DataType.String, 12, "Cry", "グエと鳴く"), # MACHINE_TRANSLATED
    0x001BE56C: Data(DataType.String, 24, "Make a cute gesture", "かわいいしぐさをする"), # MACHINE_TRANSLATED
    0x001BE584: Data(DataType.String, 16, "Say cute", "かわいいと言う"), # MACHINE_TRANSLATED
    0x001BE594: Data(DataType.String, 12, "do not know", "わからない"), # MACHINE_TRANSLATED
    0x001BE5A0: Data(DataType.String, 12, "Hand over materials", "資料を渡す"), # MACHINE_TRANSLATED
    0x001BE5AC: Data(DataType.String, 12, "Speak information", "情報を話す"), # MACHINE_TRANSLATED
    0x001BE5B8: Data(DataType.String, 12, "Ask for a talk", "話をせがむ"), # MACHINE_TRANSLATED
    0x001BE5C4: Data(DataType.String, 20, "Change your mind with conversation", "会話で気分転換する"), # MACHINE_TRANSLATED
    0x001BE5D8: Data(DataType.String, 12, "do not talk", "話さない"), # MACHINE_TRANSLATED
    0x001BE5E4: Data(DataType.String, 12, "Feels good", "気持ちいい"), # MACHINE_TRANSLATED
    0x001BE5F0: Data(DataType.String, 16, "Draw up opinion brief", "意見書の作成"),
    0x001BE600: Data(DataType.String, 28, "Hack into MAGI terminal", "マギ端末にハッキングする"),
    0x001BE61C: Data(DataType.String, 28, "Information Skill Practice (6/20 ROM Use)", "情報技能の訓練(6/20ROM専用)"),
    0x001BE638: Data(DataType.String, 20, "Ask how work is going", "仕事の調子を尋ねる"),
    0x001BE64C: Data(DataType.String, 16, "It's going smoothly", "順調だと答える"),
    0x001BE65C: Data(DataType.String, 20, "It could be better", "芳しくないと答える"),
    0x001BE670: Data(DataType.String, 12, "Be appreciative", "ねぎらう"),
    0x001BE67C: Data(DataType.String, 16, "Respond spontaneously", "適当に相手する"),
    0x001BE68C: Data(DataType.String, 12, "Be modest", "謙遜する"),
    0x001BE698: Data(DataType.String, 24, "Sorry to interrupt", "邪魔した事をあやまる"),
    0x001BE6B0: Data(DataType.String, 20, "It sounds rough", "大変そうだと言う"),
    0x001BE6C4: Data(DataType.String, 20, "Talk about the anxiety of the situation", "状況の不安さを語る"), # MACHINE_TRANSLATED
    0x001BE6D8: Data(DataType.String, 20, "Talk to PsvChr", "受動者に話しかける"),
    0x001BE6EC: Data(DataType.String, 20, "Take a shower", "シャワーを浴びる"),
    0x001BE700: Data(DataType.String, 16, "Interrupt the conversation", "会話に割り込む"),
    0x001BE710: Data(DataType.String, 16, "Impede their liaison", "情事を邪魔する"),
    0x001BE720: Data(DataType.String, 24, "Interrupt hostile conversation", "険悪な会話に割り込む"),
    0x001BE738: Data(DataType.String, 24, "Interrupt serious conversation", "深刻な会話を邪魔する"),
    0x001BE750: Data(DataType.String, 20, "Interrupt work-related conversation", "業務会話に割り込む"),
    0x001BE764: Data(DataType.String, 8, "Restroom", "トイレ"),
    0x001BE76C: Data(DataType.String, 8, "Sleeping", "睡眠"),
    0x001BE774: Data(DataType.String, 12, "Hydrating", "水分補給"),
    0x001BE780: Data(DataType.String, 8, "Bathing", "入浴"),
    0x001BE788: Data(DataType.String, 8, "Eating", "食事"),
    0x001BE790: Data(DataType.String, 20, "01: Eva Mechanics", "０１：ＥＶＡの構造"),
    0x001BE7A4: Data(DataType.String, 20, "02: Eva Unit-01", "０２：ＥＶＡ初号機"),
    0x001BE7B8: Data(DataType.String, 28, "03: Second Child", "０３：セカンドチルドレン"),
    0x001BE7D4: Data(DataType.String, 16, "04: Yui Ikari", "０４：碇ユイ"),
    0x001BE7E4: Data(DataType.String, 20, "05: Gendo Ikari", "０５：碇ゲンドウ"),
    0x001BE7F8: Data(DataType.String, 24, "06: Special Agency Nerv", "０６：特務機関ネルフ"),
    0x001BE810: Data(DataType.String, 24, "07: Marduk Institute", "０７：マルドゥック機関"),
    0x001BE828: Data(DataType.String, 24, "08: Gendo's Ambitions", "０８：ゲンドウの野望"),
    0x001BE840: Data(DataType.String, 20, "09: History of Nerv", "０９：ネルフの歴史"),
    0x001BE854: Data(DataType.String, 28, "10: Human Instrumentality Project in Detail", "１０：人類補完計画の内容"),
    0x001BE870: Data(DataType.String, 16, "11: Gehirn", "１１：ゲヒルン"),
    0x001BE880: Data(DataType.String, 16, "12: Seele", "１２：ゼーレ"),
    0x001BE890: Data(DataType.String, 24, "13: A.T. Field", "１３：ΑΤフィールド"),
    0x001BE8A8: Data(DataType.String, 16, "14: S2 Engine", "１４：Ｓ２機関"),
    0x001BE8B8: Data(DataType.String, 12, "15: Angels", "１５：使徒"),
    0x001BE8C4: Data(DataType.String, 16, "16: Adam", "１６：アダム"),
    0x001BE8D4: Data(DataType.String, 16, "17: Dead Sea Scrolls", "１７：死海文書"),
    0x001BE8E4: Data(DataType.String, 20, "18: First Ancestral Race", "１８：第１始祖民族"),
    0x001BE8F8: Data(DataType.String, 16, "19: The Second Angel", "１９：第２使徒"),
    0x001BE908: Data(DataType.String, 28, "20: Second Impact", "２０：セカンドインパクト"),
    0x001BE924: Data(DataType.String, 24, "21: Third Impact", "２１：サードインパクト"),
    0x001BE93C: Data(DataType.String, 24, "22: Spear of Longinus", "２２：ロンギヌスの槍"),
    0x001BE954: Data(DataType.String, 20, "23: Dummy Plug", "２３：ダミープラグ"),
    0x001BE968: Data(DataType.String, 20, "24: GeoFront", "２４：ジオフロント"),
    0x001BE97C: Data(DataType.String, 24, "(Running Away: Memory, has men in black)", "（家出の　黒服用記憶）"),
    0x001BE994: Data(DataType.String, 12, "＜Close＞", "＜終了＞"),
    0x001BE9A0: Data(DataType.String, 24, "Talk about the previous battle", "前回の戦闘について話す"),
    0x001BE9B8: Data(DataType.String, 20, "Express words of praise", "賞賛の言葉を述べる"),
    0x001BE9CC: Data(DataType.String, 16, "Praise how well they fought", "善戦をたたえる"),
    0x001BE9DC: Data(DataType.String, 24, "Tell them to stay the present course", "今の調子でいけと言う"),
    0x001BE9F4: Data(DataType.String, 24, "Suggest they be on their guard", "油断は禁物と助言する"),
    0x001BEA0C: Data(DataType.String, 24, "Advise to tighten", "気を引き締めるよう忠告"), # MACHINE_TRANSLATED
    0x001BEA24: Data(DataType.String, 24, "Get rid of the darkness of the future", "先行きの暗さをもらす"), # MACHINE_TRANSLATED
    0x001BEA3C: Data(DataType.String, 24, "Blame you to do something", "なんとかするよう責める"), # MACHINE_TRANSLATED
    0x001BEA54: Data(DataType.String, 24, "Hitting despair", "絶望の気持ちをぶつける"), # MACHINE_TRANSLATED
    0x001BEA6C: Data(DataType.String, 20, "Say it was an easy victory", "楽勝であったと言う"), # MACHINE_TRANSLATED
    0x001BEA80: Data(DataType.String, 24, "Say you won without any effort", "苦労せず勝てたと言う"), # MACHINE_TRANSLATED
    0x001BEA98: Data(DataType.String, 24, "Say because I did my best", "がんばったからと言う"), # MACHINE_TRANSLATED
    0x001BEAB0: Data(DataType.String, 24, "Say hardship was forced", "苦戦は強いられたと言う"), # MACHINE_TRANSLATED
    0x001BEAC8: Data(DataType.String, 24, "I did my best, but...", "がんばったけど…と言う"), # MACHINE_TRANSLATED
    0x001BEAE0: Data(DataType.String, 24, "Say i was killed", "だいぶやられたと言う"), # MACHINE_TRANSLATED
    0x001BEAF8: Data(DataType.String, 24, "Say I don't want to fight anymore", "もう戦いたくないと言う"), # MACHINE_TRANSLATED
    0x001BEB10: Data(DataType.String, 20, "Show a bearish attitude", "弱気な態度を見せる"), # MACHINE_TRANSLATED
    0x001BEB24: Data(DataType.String, 28, "Tokyo-3 is peaceful", "第３新東京市は安泰と言う"),
    0x001BEB40: Data(DataType.String, 24, "Intercept status is operational", "迎撃状態は機能している"),
    0x001BEB58: Data(DataType.String, 24, "Talk about the incidence of damage", "被害の発生を話題にする"),
    0x001BEB70: Data(DataType.String, 24, "Mention the evacuation's progress", "疎開の進捗を口にする"),
    0x001BEB88: Data(DataType.String, 24, "Intercept function is unlikely", "迎撃機能は期待できない"),
    0x001BEBA0: Data(DataType.String, 28, "Mention Tokyo-3's destruction", "第３新東京市の破棄の話題"),
    0x001BEBBC: Data(DataType.String, 24, "Secure, even though an Angel is always coming", "いつ使徒がきても安心"),
    0x001BEBD4: Data(DataType.String, 20, "The rest is up to the Evas", "あとはエヴァ次第"),
    0x001BEBE8: Data(DataType.String, 20, "It'll be okay for a while", "しばらくは大丈夫"),
    0x001BEBFC: Data(DataType.String, 24, "The battle's odds are 50-50", "戦いの行方は五分五分"),
    0x001BEC14: Data(DataType.String, 20, "We're expecting a close fight", "苦戦が予想される"),
    0x001BEC28: Data(DataType.String, 24, "I feel more lonely", "もっと寂しくなりそう"), # MACHINE_TRANSLATED
    0x001BEC40: Data(DataType.String, 28, "It's too much to take until the next Angel", "次の使徒まで耐え切れない"),
    0x001BEC5C: Data(DataType.String, 28, "We'll be saying goodbye to this city soon, too", "もう、この街ともお別れだ"),
    0x001BEC78: Data(DataType.String, 24, "Concerning Shinji's hospitalization", "シンジの入院について"),
    0x001BECC0: Data(DataType.String, 20, "Perk up at once", "すぐに元気になる"),
    0x001BECD4: Data(DataType.String, 28, "It'll take a little more time", "ちょっと時間がかかりそう"),
    0x001BECF0: Data(DataType.String, 20, "It'd be nice to lighten up, huh?", "元気になるといいね"),
    0x001BED04: Data(DataType.String, 28, "It looked like a horrible injury...", "ひどい怪我だったようだ…"),
    0x001BED20: Data(DataType.String, 16, "They seem to be critical...", "重体のようだ…"),
    0x001BED30: Data(DataType.String, 16, "They're in serious condition.", "容態は深刻だ"),
    0x001BED40: Data(DataType.String, 24, "Mention Shinji's death", "シンジの死を口にする"),
    0x001BED58: Data(DataType.String, 24, "Mention Asuka's death", "アスカの死を口にする"),
    0x001BED70: Data(DataType.String, 24, "Mention Toji's death", "トウジの死を口にする"),
    0x001BED88: Data(DataType.String, 24, "Mention Kaworu's death", "カヲルの死を口にする"),
    0x001BEDA0: Data(DataType.String, 12, "Cry", "泣き崩れる"), # MACHINE_TRANSLATED
    0x001BEDAC: Data(DataType.String, 16, "Stuck in words", "言葉に詰まる"), # MACHINE_TRANSLATED
    0x001BEDBC: Data(DataType.String, 16, "Dying face", "死にそうな顔"), # MACHINE_TRANSLATED
    0x001BEDCC: Data(DataType.String, 24, "I don't want to hear that story", "そんな話聞きたくない"), # MACHINE_TRANSLATED
    0x001BEDE4: Data(DataType.String, 12, "Vigor", "カラ元気"), # MACHINE_TRANSLATED
    0x001BEDF0: Data(DataType.String, 24, "The topic of increase in evacuated students", "疎開する生徒増加の話題"), # MACHINE_TRANSLATED
    0x001BEE08: Data(DataType.String, 24, "The topic of student sharp decline due to evacuation", "疎開で生徒激減の話題"), # MACHINE_TRANSLATED
    0x001BEE20: Data(DataType.String, 24, "Topic of convenience store assortment", "コンビニの品揃えの話題"), # MACHINE_TRANSLATED
    0x001BEE38: Data(DataType.String, 28, "There are no products at convenience stores", "コンビニに商品が無い話題"), # MACHINE_TRANSLATED
    0x001BEE54: Data(DataType.String, 24, "Talk about wishful observation", "希望的観測を口にする"), # MACHINE_TRANSLATED
    0x001BEE6C: Data(DataType.String, 28, "The topic that Hikari sisters died", "ヒカリの姉妹が死んだ話題"), # MACHINE_TRANSLATED
    0x001BEE88: Data(DataType.String, 24, "Topic that Touji evacuated", "トウジが疎開した話題"), # MACHINE_TRANSLATED
    0x001BEEA0: Data(DataType.String, 24, "The topic that Kensuke evacuated", "ケンスケが疎開した話題"), # MACHINE_TRANSLATED
    0x001BEEB8: Data(DataType.String, 24, "The topic that Hikari evacuated", "ヒカリが疎開した話題"), # MACHINE_TRANSLATED
    0x001BEED0: Data(DataType.String, 28, "Rei's apartment collapse topic", "レイのアパート倒壊の話題"), # MACHINE_TRANSLATED
    0x001BEEEC: Data(DataType.String, 12, "Swear", "絶句する"), # MACHINE_TRANSLATED
    0x001BEEF8: Data(DataType.String, 20, "Sadly share", "悲しく相づちをうつ"), # MACHINE_TRANSLATED
    0x001BEF0C: Data(DataType.String, 24, "Say you'll be lonely", "寂しくなるね、と言う"), # MACHINE_TRANSLATED
    0x001BEF24: Data(DataType.String, 12, "Bring up the weather", "天気の話題"),
    0x001BEF30: Data(DataType.String, 12, "Sympathize", "共感する"), # MACHINE_TRANSLATED
    0x001BEF3C: Data(DataType.String, 12, "Opposition", "反対の意見"), # MACHINE_TRANSLATED
    0x001BEF48: Data(DataType.String, 24, "Ask if they did the homework", "宿題してきたか尋ねる"),
    0x001BEF60: Data(DataType.String, 16, "Say you did", "してきたと言う"),
    0x001BEF70: Data(DataType.String, 20, "Say you haven't", "やっていないと言う"),
    0x001BEF84: Data(DataType.String, 20, "Surprised by the existence of homework", "宿題の存在に驚く"), # MACHINE_TRANSLATED
    0x001BEF98: Data(DataType.String, 28, "Ask Toji how his sister's doing", "トウジに妹の様子を尋ねる"),
    0x001BEFB4: Data(DataType.String, 20, "Answer that you are in good shape", "調子がいいと答える"), # MACHINE_TRANSLATED
    0x001BEFC8: Data(DataType.String, 20, "Answer", "ぼちぼちだと答える"), # MACHINE_TRANSLATED
    0x001BEFDC: Data(DataType.String, 12, "Silence", "押し黙る"), # MACHINE_TRANSLATED
    0x001BEFE8: Data(DataType.String, 20, "Ask about Misato", "ミサトについて聞く"),
    0x001BEFFC: Data(DataType.String, 16, "Praise Misato", "ミサトを誉める"), # MACHINE_TRANSLATED
    0x001BF00C: Data(DataType.String, 24, "Say Misato is a good person", "ミサトはいい人だと言う"), # MACHINE_TRANSLATED
    0x001BF024: Data(DataType.String, 24, "Nothing to say", "とくに言うことはない"), # MACHINE_TRANSLATED
    0x001BF03C: Data(DataType.String, 20, "Beat Misato lightly", "ミサトを軽くけなす"), # MACHINE_TRANSLATED
    0x001BF050: Data(DataType.String, 24, "Representing dissatisfaction with Misato", "ミサトへの不満を表す"), # MACHINE_TRANSLATED
    0x001BF068: Data(DataType.String, 16, "Depress", "相づちをうつ"), # MACHINE_TRANSLATED
    0x001BF078: Data(DataType.String, 24, "Speak fondly of Kaji", "加持についてのろける"),
    0x001BF090: Data(DataType.String, 28, "Be all ears for Asuka", "アスカの言葉に耳を傾ける"),
    0x001BF0AC: Data(DataType.String, 12, "Am not interested", "興味ない"), # MACHINE_TRANSLATED
    0x001BF0B8: Data(DataType.String, 16, "Curtail", "加持をけなす"), # MACHINE_TRANSLATED
    0x001BF0C8: Data(DataType.String, 24, "Makatsuku is defeated", "加持をけなされムカツク"), # MACHINE_TRANSLATED
    0x001BF0E0: Data(DataType.String, 20, "Surprised to be kicked", "加持をけなされ驚く"), # MACHINE_TRANSLATED
    0x001BF0F4: Data(DataType.String, 28, "Explode dissatisfaction with holding", "加持への不満を爆発させる"), # MACHINE_TRANSLATED
    0x001BF110: Data(DataType.String, 20, "I agree with Asuka", "アスカに同意する"), # MACHINE_TRANSLATED
    0x001BF124: Data(DataType.String, 24, "Worry about how Asuka is doing", "アスカの様子を心配する"),
    0x001BF13C: Data(DataType.String, 20, "Ask about A.T. status", "ΑΤの調子を尋ねる"),
    0x001BF150: Data(DataType.String, 20, "Say good", "好調であると答える"), # MACHINE_TRANSLATED
    0x001BF164: Data(DataType.String, 20, "Answer normal", "普通であると答える"), # MACHINE_TRANSLATED
    0x001BF178: Data(DataType.String, 20, "Answer that you're out of tune", "調子が悪いと答える"), # MACHINE_TRANSLATED
    0x001BF18C: Data(DataType.String, 20, "Ask how things are at school", "学校の様子を尋ねる"),
    0x001BF1A0: Data(DataType.String, 16, "Say fun", "楽しいと答える"), # MACHINE_TRANSLATED
    0x001BF1B0: Data(DataType.String, 20, "Answer not having fun", "楽しくないと答える"), # MACHINE_TRANSLATED
    0x001BF1C4: Data(DataType.String, 16, "Blast", "発破をかける"), # MACHINE_TRANSLATED
    0x001BF1D4: Data(DataType.String, 16, "Say comfort", "気休めを言う"), # MACHINE_TRANSLATED
    0x001BF1E4: Data(DataType.String, 24, "Ask how busy work is", "仕事の忙しさを尋ねる"),
    0x001BF1FC: Data(DataType.String, 24, "I'm doing my job easily", "仕事は楽にこなしている"), # MACHINE_TRANSLATED
    0x001BF214: Data(DataType.String, 24, "You can do it without overtime", "残業なしでやれている"), # MACHINE_TRANSLATED
    0x001BF22C: Data(DataType.String, 16, "There is no particular problem", "特に問題は無い"), # MACHINE_TRANSLATED
    0x001BF23C: Data(DataType.String, 20, "Overtime is increasing", "残業が増えている"), # MACHINE_TRANSLATED
    0x001BF250: Data(DataType.String, 12, "Busy and hard", "多忙で大変"), # MACHINE_TRANSLATED
    0x001BF25C: Data(DataType.String, 20, "Ask about Nerv", "ネルフについて質問"),
    0x001BF270: Data(DataType.String, 20, "Reply about Nerv", "ネルフについて返答"), # MACHINE_TRANSLATED
    0x001BF284: Data(DataType.String, 20, "Ask about Evas", "エヴァについて質問"),
    0x001BF298: Data(DataType.String, 20, "Tell them about Evas", "エヴァについて返答"),
    0x001BF2AC: Data(DataType.String, 20, "Ask about Angels", "使徒について質問"),
    0x001BF2C0: Data(DataType.String, 20, "Tell them about Angels", "使徒について返答"),
    0x001BF2D4: Data(DataType.String, 20, "Stagger the answer", "答えをはぐらかす"), # MACHINE_TRANSLATED
    0x001BF2E8: Data(DataType.String, 28, "Ask about Human Instrumentality Project", "人類補完計画について質問"),
    0x001BF304: Data(DataType.String, 28, "Reply about human complementation plan", "人類補完計画について返答"), # MACHINE_TRANSLATED
    0x001BF320: Data(DataType.String, 24, "Ask about Gendo", "ゲンドウについて尋ねる"),
    0x001BF338: Data(DataType.String, 20, "Teach that you are a good person", "立派な人だと教える"), # MACHINE_TRANSLATED
    0x001BF34C: Data(DataType.String, 20, "Teach that you are a busy person", "忙しい人だと教える"), # MACHINE_TRANSLATED
    0x001BF360: Data(DataType.String, 24, "Teach you to be the lowest boss", "最低の上司だと教える"), # MACHINE_TRANSLATED
    0x001BF378: Data(DataType.String, 24, "Teach if you don't understand", "よくわからないと教える"), # MACHINE_TRANSLATED
    0x001BF390: Data(DataType.String, 20, "Based on my father's evaluation", "父の評価に相づち"), # MACHINE_TRANSLATED
    0x001BF3A4: Data(DataType.String, 24, "Stick to Shinji's attitude", "シンジの態度につっこむ"), # MACHINE_TRANSLATED
    0x001BF3BC: Data(DataType.String, 20, "Become muddy", "しどろもどろになる"), # MACHINE_TRANSLATED
    0x001BF3D0: Data(DataType.String, 24, "Hear how pilots are doing", "パイロットの様子を聞く"),
    0x001BF3E8: Data(DataType.String, 16, "Smooth sailing", "順風満帆である"), # MACHINE_TRANSLATED
    0x001BF3F8: Data(DataType.String, 12, "Is in good order", "順調である"), # MACHINE_TRANSLATED
    0x001BF404: Data(DataType.String, 24, "No good, no bad", "可も無く、不可も無く"), # MACHINE_TRANSLATED
    0x001BF41C: Data(DataType.String, 24, "Not without problems", "問題が無いわけではない"), # MACHINE_TRANSLATED
    0x001BF434: Data(DataType.String, 20, "It's a difficult situation", "困難な事態である"), # MACHINE_TRANSLATED
    0x001BF448: Data(DataType.String, 20, "Ask about Eva status", "エヴァの調子を聞く"),
    0x001BF45C: Data(DataType.String, 20, "They're in peak condition", "最高の状態である"),
    0x001BF470: Data(DataType.String, 24, "Maintaining favorable status", "いい状態を保っている"),
    0x001BF488: Data(DataType.String, 20, "Problems are developing", "問題が発生している"),
    0x001BF49C: Data(DataType.String, 16, "There's tough times ahead", "前途多難である"),
    0x001BF4AC: Data(DataType.String, 20, "Curb undercover activity", "諜報活動を牽制する"),
    0x001BF4C0: Data(DataType.String, 12, "Play dumb", "とぼける"),
    0x001BF4CC: Data(DataType.String, 12, "Dodge the question", "誤魔化す"),
    0x001BF4D8: Data(DataType.String, 20, "We should talk sometime", "そのうち話をしよう"),
    0x001BF4EC: Data(DataType.String, 24, "Approaching the core", "核心に近づきつつある"), # MACHINE_TRANSLATED
    0x001BF504: Data(DataType.String, 20, "Tweet your own danger", "身の危険をつぶやく"), # MACHINE_TRANSLATED
    0x001BF518: Data(DataType.String, 28, "Request printed report", "プリントの届けを依頼する"),
    0x001BF534: Data(DataType.String, 16, "Entrust the print", "プリントを託す"), # MACHINE_TRANSLATED
    0x001BF544: Data(DataType.String, 16, "Decline evasively", "あいまいに断る"),
    0x001BF554: Data(DataType.String, 16, "Lose heart", "がっかりする"),
    0x001BF564: Data(DataType.String, 12, "Decline bluntly", "むげに断る"),
    0x001BF570: Data(DataType.String, 16, "Get irritated", "カチンとくる"),
    0x001BF580: Data(DataType.String, 16, "Deliver print-out", "プリントを渡す"),
    0x001BF590: Data(DataType.String, 20, "Thank them and accept", "感謝して受け取る"),
    0x001BF5A4: Data(DataType.String, 12, "Accept", "受け取る"),
    0x001BF5B0: Data(DataType.String, 24, "Accept gruffly", "ぶっきらぼうに受け取る"),
    0x001BF5C8: Data(DataType.String, 20, "Rejoice for the discharge of a passive person", "受動者の退院を喜ぶ"), # MACHINE_TRANSLATED
    0x001BF5DC: Data(DataType.String, 28, "Reply to look good", "調子が良さそうに返事する"), # MACHINE_TRANSLATED
    0x001BF5F8: Data(DataType.String, 16, "Reply normally", "普通に返事する"), # MACHINE_TRANSLATED
    0x001BF608: Data(DataType.String, 24, "Replying to be unwell", "調子が悪そうに返事する"), # MACHINE_TRANSLATED
    0x001BF620: Data(DataType.String, 20, "Respond gently", "気さくに応答する"), # MACHINE_TRANSLATED
    0x001BF634: Data(DataType.String, 16, "Respond normally", "普通に応答する"), # MACHINE_TRANSLATED
    0x001BF644: Data(DataType.String, 24, "Respond to Bukkake", "ぶっきらぼうに応答する"), # MACHINE_TRANSLATED
    0x001BF65C: Data(DataType.String, 20, "Mention how cheerful they look", "楽しげな様子を指摘"),
    0x001BF670: Data(DataType.String, 28, "Mention how vibrant they look", "活気にあふれる様子を指摘"),
    0x001BF68C: Data(DataType.String, 20, "Mention how earnest they look", "真剣な様子を指摘"),
    0x001BF6A0: Data(DataType.String, 24, "Point out that you are nervous", "緊張している様子を指摘"), # MACHINE_TRANSLATED
    0x001BF6B8: Data(DataType.String, 24, "Point out that you are at ease", "安心している様子を指摘"), # MACHINE_TRANSLATED
    0x001BF6D0: Data(DataType.String, 20, "Point out anxiety", "不安な様子を指摘"), # MACHINE_TRANSLATED
    0x001BF6E4: Data(DataType.String, 24, "Pointed out how sad", "悲しんでいる様子を指摘"), # MACHINE_TRANSLATED
    0x001BF6FC: Data(DataType.String, 28, "Pointed out how relaxed", "気が緩んでいる様子を指摘"), # MACHINE_TRANSLATED
    0x001BF718: Data(DataType.String, 24, "Pointed out how disappointed", "落胆している様子を指摘"), # MACHINE_TRANSLATED
    0x001BF730: Data(DataType.String, 20, "Pointed out the unpleasant appearance", "不愉快な様子を指摘"), # MACHINE_TRANSLATED
    0x001BF744: Data(DataType.String, 24, "Point out angry", "怒っている様子を指摘"), # MACHINE_TRANSLATED
    0x001BF75C: Data(DataType.String, 20, "Mention their flushed face", "顔のほてりを指摘"),
    0x001BF770: Data(DataType.String, 24, "Pointed out ashamed", "恥らっている様子を指摘"), # MACHINE_TRANSLATED
    0x001BF788: Data(DataType.String, 16, "Brightly affirm", "明るく肯定する"), # MACHINE_TRANSLATED
    0x001BF798: Data(DataType.String, 16, "Cheat bright", "明るくごまかす"), # MACHINE_TRANSLATED
    0x001BF7A8: Data(DataType.String, 16, "Brightly deny", "明るく否定する"), # MACHINE_TRANSLATED
    0x001BF7B8: Data(DataType.String, 12, "Affirm", "肯定する"),
    0x001BF7C4: Data(DataType.String, 12, "Cheat", "ごまかす"), # MACHINE_TRANSLATED
    0x001BF7D0: Data(DataType.String, 12, "Deny", "否定する"), # MACHINE_TRANSLATED
    0x001BF7DC: Data(DataType.String, 20, "Awkwardly affirm", "気まずく肯定する"), # MACHINE_TRANSLATED
    0x001BF7F0: Data(DataType.String, 20, "Awkward cheat", "気まずくごまかす"), # MACHINE_TRANSLATED
    0x001BF804: Data(DataType.String, 20, "Awkwardly deny", "気まずく否定する"), # MACHINE_TRANSLATED
    0x001BF818: Data(DataType.String, 24, "Affirm when sunken", "沈んだ様子で肯定する"), # MACHINE_TRANSLATED
    0x001BF830: Data(DataType.String, 24, "Cheat in the sunken state", "沈んだ様子でごまかす"), # MACHINE_TRANSLATED
    0x001BF848: Data(DataType.String, 24, "Deny it as it sank", "沈んだ様子で否定する"), # MACHINE_TRANSLATED
    0x001BF860: Data(DataType.String, 24, "Stop saying that", "そんな言い方やめてよ"), # MACHINE_TRANSLATED
    0x001BF878: Data(DataType.String, 16, "S-say what?", "そ、そんな…"),
    0x001BF888: Data(DataType.String, 24, "Be ashamed to deny", "恥じらいながら否定する"), # MACHINE_TRANSLATED
    0x001BF8A0: Data(DataType.String, 24, "Round up casually", "さりげなく切り上げる"), # MACHINE_TRANSLATED
    0x001BF8B8: Data(DataType.String, 20, "Awkwardly round up", "気まずく切り上げる"), # MACHINE_TRANSLATED
    0x001BF8CC: Data(DataType.String, 28, "Talk to classmate", "クラスメイトに話しかける"),
    0x001BF8E8: Data(DataType.String, 16, "Engage in regular conversation", "普通に会話する"),
    0x001BF8F8: Data(DataType.String, 16, "Put in a good word", "いい評判を流す"),
    0x001BF908: Data(DataType.String, 16, "Spread gossip", "悪い噂を流す"),
    0x001BF918: Data(DataType.String, 24, "Talk to Nerv personnel", "ネルフ職員に話しかける"),
    0x001BF930: Data(DataType.String, 12, "Start of lesson", "授業開始"),
    0x001BF93C: Data(DataType.String, 16, "Take it as usual", "普通に受ける"),
    0x001BF94C: Data(DataType.String, 16, "Take it seriously", "マジメに受ける"),
    0x001BF95C: Data(DataType.String, 12, "Do something on the side", "内職を行う"),
    0x001BF968: Data(DataType.String, 16, "Look away", "よそ見をする"),
    0x001BF978: Data(DataType.String, 8, "Nod off", "居眠り"),
    0x001BF980: Data(DataType.String, 12, "Invite to school", "学校に誘う"),
    0x001BF98C: Data(DataType.String, 16, "Go to school with them", "一緒に登校する"),
    0x001BF99C: Data(DataType.String, 16, "Invite to Nerv", "ネルフに誘う"),
    0x001BF9AC: Data(DataType.String, 16, "Go to work with them", "一緒に登庁する"),
    0x001BF9BC: Data(DataType.String, 24, "Propose an item exchange", "アイテムの交換を提案"),
    0x001BF9D4: Data(DataType.String, 28, "No items to exchange", "アイテムは所有していない"),
    0x001BF9F0: Data(DataType.String, 12, "Decline exchange", "交換を断る"),
    0x001BF9FC: Data(DataType.String, 16, "Accept exchange", "交換を了承する"),
    0x001BFA0C: Data(DataType.String, 24, "Pass on the exchange", "やっぱり交換をやめる"),
    0x001BFA24: Data(DataType.String, 28, "Have them pick an item", "相手にアイテムを選ばせる"),
    0x001BFA40: Data(DataType.String, 28, "Select desired item", "欲しいアイテムを指定する"),
    0x001BFA5C: Data(DataType.String, 20, "Item exchange completed", "アイテムの交換成立"),
    0x001BFA70: Data(DataType.String, 20, "Sit on bed", "ベッドに腰掛ける"),
    0x001BFA84: Data(DataType.String, 24, "Rise from bed", "ベッドから立ち上がる"),
    0x001BFA9C: Data(DataType.String, 16, "Stare at the ceiling", "天井を見つめる"),
    0x001BFAAC: Data(DataType.String, 20, "Reminisce about someone", "誰かの事を思い出す"),
    0x001BFAC0: Data(DataType.String, 24, "Think back on fun times", "楽しい出来事を反芻する"),
    0x001BFAD8: Data(DataType.String, 24, "Recall a painful experience", "辛い出来事を思い出す"),
    0x001BFAF0: Data(DataType.String, 12, "Listen to music", "音楽を聴く"),
    0x001BFAFC: Data(DataType.String, 16, "Drink beer", "ビールを飲む"),
    0x001BFB0C: Data(DataType.String, 24, "Talk to person in bed", "ベッドの人に話しかける"),
    0x001BFB24: Data(DataType.String, 20, "Respond and stand up", "応答して立ち上がる"), # MACHINE_TRANSLATED
    0x001BFB38: Data(DataType.String, 12, "Drive away", "追い払う"), # MACHINE_TRANSLATED
    0x001BFB44: Data(DataType.String, 16, "Sit on bench", "ベンチに座る"),
    0x001BFB54: Data(DataType.String, 24, "Rise from bench", "ベンチから立ち上がる"),
    0x001BFB6C: Data(DataType.String, 28, "Vaguely relax on the bench", "ベンチでぼんやりくつろぐ"), # MACHINE_TRANSLATED
    0x001BFB88: Data(DataType.String, 16, "Drink juice", "ジュースを飲む"),
    0x001BFB98: Data(DataType.String, 20, "Talk to person next to you", "隣の人に話しかける"),
    0x001BFBAC: Data(DataType.String, 24, "Talk to person on bench", "ベンチの人に話しかける"),
    0x001BFBC4: Data(DataType.String, 20, "Relax at table", "テーブルでくつろぐ"),
    0x001BFBD8: Data(DataType.String, 28, "Request harmonics test", "ハーモニクステストの依頼"),
    0x001BFBF4: Data(DataType.String, 28, "Decline harmonics test", "ハーモニクステストを断る"),
    0x001BFC10: Data(DataType.String, 28, "Begin harmonics test", "ハーモニクステストを開始"),
    0x001BFC2C: Data(DataType.String, 20, "Focus on testing", "テストに集中する"), # MACHINE_TRANSLATED
    0x001BFC40: Data(DataType.String, 12, "Keep heartless", "無心を保つ"), # MACHINE_TRANSLATED
    0x001BFC4C: Data(DataType.String, 24, "Focus on Eva", "エヴァに意識を向ける"), # MACHINE_TRANSLATED
    0x001BFC64: Data(DataType.String, 16, "Face in nature", "自然体で臨む"), # MACHINE_TRANSLATED
    0x001BFC74: Data(DataType.String, 16, "Relax", "リラックスする"),
    0x001BFC84: Data(DataType.String, 16, "Restless", "落ち着かない"), # MACHINE_TRANSLATED
    0x001BFC94: Data(DataType.String, 16, "Not motivated", "やる気が出ない"), # MACHINE_TRANSLATED
    0x001BFCA4: Data(DataType.String, 24, "Satisfied with the test results", "テストの結果に満足する"), # MACHINE_TRANSLATED
    0x001BFCBC: Data(DataType.String, 28, "Tell me that your grades are mediocre", "平凡な成績であると伝える"), # MACHINE_TRANSLATED
    0x001BFCD8: Data(DataType.String, 20, "Scold the test results", "テストの結果を叱る"), # MACHINE_TRANSLATED
    0x001BFCEC: Data(DataType.String, 24, "Request Synch Skill Training", "シンクロ技能訓練の依頼"),
    0x001BFD04: Data(DataType.String, 16, "Staff skills training", "参謀技能の訓練"), # MACHINE_TRANSLATED
    0x001BFD14: Data(DataType.String, 16, "Development skills training", "開発技能の訓練"), # MACHINE_TRANSLATED
    0x001BFD24: Data(DataType.String, 24, "Operator Skill Training", "オペレート技能の訓練"),
    0x001BFD3C: Data(DataType.String, 16, "Espionage Skill Training", "諜報技能の訓練"),
    0x001BFD4C: Data(DataType.String, 16, "Clerical Skill Training", "事務技能の訓練"),
    0x001BFD5C: Data(DataType.String, 16, "Information Skill Training", "情報技能の訓練"),
    0x001BFD6C: Data(DataType.String, 16, "Self-defense skill training", "白兵技能の訓練"),
    0x001BFD7C: Data(DataType.String, 12, "Make bento box", "弁当を作る"),
    0x001BFD88: Data(DataType.String, 20, "Drink water from fountain", "冷水機で水を飲む"),
    0x001BFD9C: Data(DataType.String, 20, "Drink park tap-water", "公園の水道水を飲む"),
    0x001BFDB0: Data(DataType.String, 16, "Run away from town", "街から逃げ出す"),
    0x001BFDC0: Data(DataType.String, 16, "Space out", "ぼんやりする"),
    0x001BFDD0: Data(DataType.String, 20, "Inspire yourself via self-help", "自己啓発で奮起する"),
    0x001BFDE4: Data(DataType.String, 20, "Depressed by self-loathing", "自己嫌悪で落ち込む"), # MACHINE_TRANSLATED
    0x001BFDF8: Data(DataType.String, 16, "Look at Unit-00", "零号機を見る"),
    0x001BFE08: Data(DataType.String, 16, "Look at Unit-01", "初号機を見る"),
    0x001BFE18: Data(DataType.String, 16, "Look at Unit-02", "弐号機を見る"),
    0x001BFE28: Data(DataType.String, 16, "Look at Unit-03", "参号機を見る"),
    0x001BFE38: Data(DataType.String, 16, "Look at Unit-04", "四号機を見る"),
    0x001BFE48: Data(DataType.String, 24, "See the current state of Nerv force", "ネルフ戦力の現状を見る"), # MACHINE_TRANSLATED
    0x001BFE60: Data(DataType.String, 24, "View Nerv General Information", "ネルフ総合情報を見る"),
    0x001BFE78: Data(DataType.String, 20, "Request an item", "アイテムをねだる"),
    0x001BFE8C: Data(DataType.String, 24, "Which item would you like?", "どのアイテムがいいの"),
    0x001BFEA4: Data(DataType.String, 8, "No can do", "いやだ"),
    0x001BFEAC: Data(DataType.String, 24, "I'd like this one", "このアイテムが欲しい"),
    0x001BFEC4: Data(DataType.String, 20, "I'm good, actually", "やっぱりいらない"),
    0x001BFED8: Data(DataType.String, 16, "No problem", "ああ、いいよ"),
    0x001BFEE8: Data(DataType.String, 16, "Not that one", "これは駄目だよ"),
    0x001BFEF8: Data(DataType.String, 20, "Atmosphere Action starting point IM", "雰囲気行動起点IM"), # MACHINE_TRANSLATED
    0x001BFF0C: Data(DataType.String, 16, "Fidget", "もじもじする"),
    0x001BFF1C: Data(DataType.String, 16, "Yawn", "あくびをする"), # MACHINE_TRANSLATED
    0x001BFF2C: Data(DataType.String, 16, "I'm hungry", "お腹がすいた"), # MACHINE_TRANSLATED
    0x001BFF3C: Data(DataType.String, 12, "Itchy", "頭がかゆい"), # MACHINE_TRANSLATED
    0x001BFF48: Data(DataType.String, 16, "I'm feeling good", "気合入れてる"), # MACHINE_TRANSLATED
    0x001BFF58: Data(DataType.String, 16, "Good mood", "ご機嫌な様子"), # MACHINE_TRANSLATED
    0x001BFF68: Data(DataType.String, 16, "Face grins", "顔がニヤつく"), # MACHINE_TRANSLATED
    0x001BFF78: Data(DataType.String, 16, "Something serious", "なにやら真剣"), # MACHINE_TRANSLATED
    0x001BFF88: Data(DataType.String, 16, "Clench your fist", "拳を握り締め"), # MACHINE_TRANSLATED
    0x001BFF98: Data(DataType.String, 16, "Discouraged", "落胆している"), # MACHINE_TRANSLATED
    0x001BFFA8: Data(DataType.String, 16, "get annoyed", "イライラする"), # MACHINE_TRANSLATED
    0x001BFFB8: Data(DataType.String, 16, "I'm faint", "気が抜けてる"), # MACHINE_TRANSLATED
    0x001BFFC8: Data(DataType.String, 16, "Be frightened", "おどおどする"), # MACHINE_TRANSLATED
    0x001BFFD8: Data(DataType.String, 16, "Wipe forehead sweat", "額の汗を拭く"), # MACHINE_TRANSLATED
    0x001BFFE8: Data(DataType.String, 16, "Gaze at the setting sun", "夕日を眺める"),
    0x001BFFF8: Data(DataType.String, 16, "Sneeze", "くしゃみする"), # MACHINE_TRANSLATED
    0x001C0008: Data(DataType.String, 16, "Check in wallet", "財布の中を確認"), # MACHINE_TRANSLATED
    0x001C0018: Data(DataType.String, 16, "Pick up the product", "商品を手に取る"), # MACHINE_TRANSLATED
    0x001C0028: Data(DataType.String, 16, "to call", "電話をかける"), # MACHINE_TRANSLATED
    0x001C0038: Data(DataType.String, 16, "Operate the mobile phone", "携帯電話を操作"), # MACHINE_TRANSLATED
    0x001C0048: Data(DataType.String, 24, "Character-specific action", "キャラ固有アクション"), # MACHINE_TRANSLATED
    0x001C0060: Data(DataType.String, 20, "Stop and think", "立ち止まって考え事"), # MACHINE_TRANSLATED
    0x001C0074: Data(DataType.String, 24, "Decline synch skill training", "シンクロ技能訓練を断る"),
    0x001C008C: Data(DataType.String, 24, "Start synch skill training", "シンクロ技能訓練を開始"),
    0x001C00A4: Data(DataType.String, 16, "Concentrate on training", "訓練に集中する"), # MACHINE_TRANSLATED
    0x001C00B4: Data(DataType.String, 24, "Satisfied with the results of the training", "訓練の結果に満足する"), # MACHINE_TRANSLATED
    0x001C00CC: Data(DataType.String, 20, "Scold the results of the training", "訓練の結果を叱る"), # MACHINE_TRANSLATED
    0x001C00E0: Data(DataType.String, 28, "Mob IM, pretending to be talking", "モブIM、会話しているフリ"), # MACHINE_TRANSLATED
    0x001C00FC: Data(DataType.String, 32, "Mob IM, pretending to enter school toilet", "モブIM、学校トイレに入るフリ"), # MACHINE_TRANSLATED
    0x001C011C: Data(DataType.String, 24, "Mob IM, pretending to be in a hurry", "モブIM、急いでいるフリ"), # MACHINE_TRANSLATED
    0x001C0134: Data(DataType.String, 32, "Mob IM, pretending to enter NERV toilet", "モブIM、ネルフトイレに入るフリ"), # MACHINE_TRANSLATED
    0x001C0154: Data(DataType.String, 20, "Talk about recent events", "最近の出来事を話す"), # MACHINE_TRANSLATED
    0x001C0168: Data(DataType.String, 20, "Talk about the events of others", "他人の出来事を話す"), # MACHINE_TRANSLATED
    0x001C017C: Data(DataType.String, 20, "Speak recent complaints", "最近の愚痴を話す"), # MACHINE_TRANSLATED
    0x001C0190: Data(DataType.String, 20, "Talk about previous events", "以前の出来事を話す"), # MACHINE_TRANSLATED
    0x001C01A4: Data(DataType.String, 24, "Add something in the park toilet", "公園トイレで用を足す"), # MACHINE_TRANSLATED
    0x001C01BC: Data(DataType.String, 20, "Add to the station toilet", "駅トイレで用を足す"), # MACHINE_TRANSLATED
    0x001C01D0: Data(DataType.String, 24, "Ask about recent happenings", "最近の出来事を尋ねる"),
    0x001C01E8: Data(DataType.String, 24, "Tell them about recent happenings", "最近の出来事を教える"),
    0x001C0200: Data(DataType.String, 20, "Ask for their impressions of ○○", "○○の印象を尋ねる"),
    0x001C0214: Data(DataType.String, 16, "Share impressions", "印象を答える"),
    0x001C0224: Data(DataType.String, 20, "Ask about current health", "今の体調を尋ねる"),
    0x001C0238: Data(DataType.String, 20, "Tell them about current health", "今の体調を教える"),
    0x001C024C: Data(DataType.String, 20, "Ask how things've been lately", "最近の調子を尋ねる"),
    0x001C0260: Data(DataType.String, 20, "Tell them how things've been lately", "最近の調子を教える"),
    0x001C0274: Data(DataType.String, 16, "Ask for money", "お金をねだる"),
    0x001C0284: Data(DataType.String, 16, "Lend them money", "お金を融通する"),
    0x001C0294: Data(DataType.String, 20, "There's none on me", "持ち合わせがない"),
    0x001C02A8: Data(DataType.String, 24, "Request they cheer up someone", "○○を励ますよう頼む"),
    0x001C02C0: Data(DataType.String, 24, "Understand to encourage", "励ますことを了解する"), # MACHINE_TRANSLATED
    0x001C02D8: Data(DataType.String, 20, "Evasively play dumb", "あいまいにごまかす"),
    0x001C02EC: Data(DataType.String, 12, "Deny", "拒否する"),
    0x001C02F8: Data(DataType.String, 28, "Request they befriend someone", "○○と仲良くするよう頼む"),
    0x001C0314: Data(DataType.String, 28, "Agree to befriend them", "仲良くすることを了解する"),
    0x001C0330: Data(DataType.String, 24, "Speak highly of ○○", "○○のいい評判を流す"),
    0x001C0348: Data(DataType.String, 20, "Nod to it", "いい評判にうなずく"),
    0x001C035C: Data(DataType.String, 24, "Question it", "いい評判に疑問をもつ"),
    0x001C0374: Data(DataType.String, 20, "Deny it", "いい評判を否定する"),
    0x001C0388: Data(DataType.String, 24, "Disseminate a bad reputation of ○○", "○○の悪い評判を流す"), # MACHINE_TRANSLATED
    0x001C03A0: Data(DataType.String, 20, "Nod to a bad reputation", "悪い評判にうなずく"), # MACHINE_TRANSLATED
    0x001C03B4: Data(DataType.String, 24, "Question bad reputation", "悪い評判に疑問をもつ"), # MACHINE_TRANSLATED
    0x001C03CC: Data(DataType.String, 20, "Deny a bad reputation", "悪い評判を否定する"), # MACHINE_TRANSLATED
    0x001C03E0: Data(DataType.String, 16, "Complain", "不満をぶつける"), # MACHINE_TRANSLATED
    0x001C03F0: Data(DataType.String, 20, "Listening silently", "黙って聞いている"), # MACHINE_TRANSLATED
    0x001C0404: Data(DataType.String, 16, "Complain", "文句を言い返す"), # MACHINE_TRANSLATED
    0x001C0414: Data(DataType.String, 16, "Don't", "相手にしない"), # MACHINE_TRANSLATED
    0x001C0424: Data(DataType.String, 24, "The attitude that makes the other person stupid", "相手をバカにした態度"), # MACHINE_TRANSLATED
    0x001C043C: Data(DataType.String, 24, "Laugh like a fool", "馬鹿にするように笑う"), # MACHINE_TRANSLATED
    0x001C0454: Data(DataType.String, 20, "Scold ΑΤ undertone", "ΑΤの低調を叱る"), # MACHINE_TRANSLATED
    0x001C0468: Data(DataType.String, 16, "Apologize without power", "力なくあやまる"), # MACHINE_TRANSLATED
    0x001C0478: Data(DataType.String, 20, "Show good will to other person", "相手への好意を表す"),
    0x001C048C: Data(DataType.String, 16, "Friendly response", "好意的な反応"),
    0x001C049C: Data(DataType.String, 12, "Normal response", "普通の反応"),
    0x001C04A8: Data(DataType.String, 12, "Cruel response", "邪険な反応"),
    0x001C04B4: Data(DataType.String, 20, "Talk amiably", "気さくに話しかける"),
    0x001C04C8: Data(DataType.String, 24, "Admire their high A.T.", "ΑΤの高さを感心する"),
    0x001C04E0: Data(DataType.String, 16, "Look at PsvChr", "受動者を見る"),
    0x001C04F0: Data(DataType.String, 20, "Look at them fondly", "好意的な目で見る"),
    0x001C0504: Data(DataType.String, 16, "Lightly return greetings", "軽く挨拶を返す"), # MACHINE_TRANSLATED
    0x001C0514: Data(DataType.String, 16, "Look at them casually", "何気なく見る"),
    0x001C0524: Data(DataType.String, 20, "Feel awkward", "気まずい思いをする"), # MACHINE_TRANSLATED
    0x001C0538: Data(DataType.String, 20, "Look maliciously", "悪意を込めて見る"), # MACHINE_TRANSLATED
    0x001C054C: Data(DataType.String, 12, "Stare back", "睨み返す"), # MACHINE_TRANSLATED
    0x001C0558: Data(DataType.String, 12, "Look away", "目を逸らす"), # MACHINE_TRANSLATED
    0x001C0564: Data(DataType.String, 28, "Complain to the other person's eyes", "相手の目つきに文句を言う"), # MACHINE_TRANSLATED
    0x001C0580: Data(DataType.String, 16, "Respond agreeably", "相づちを打つ"),
    0x001C0590: Data(DataType.String, 16, "Respond indifferently", "気のない返事"),
    0x001C05A0: Data(DataType.String, 12, "Wow sky", "うわのそら"), # MACHINE_TRANSLATED
    0x001C05AC: Data(DataType.String, 12, "Take offense", "ムっとする"),
    0x001C05B8: Data(DataType.String, 12, "Be a killjoy", "しらける"),
    0x001C05C4: Data(DataType.String, 12, "Let your shoulders droop", "肩を落とす"),
    0x001C05D0: Data(DataType.String, 12, "Hang your head", "うなだれる"),
    0x001C05DC: Data(DataType.String, 12, "Be humble", "はにかむ"),
    0x001C05E8: Data(DataType.String, 16, "Worry about the other person", "相手を心配する"), # MACHINE_TRANSLATED
    0x001C05F8: Data(DataType.String, 20, "Feel poorly toward companion", "相手に不快感を持つ"),
    0x001C060C: Data(DataType.String, 20, "Feel fondly toward companion", "相手に好意を感じる"),
    0x001C0620: Data(DataType.String, 8, "Falter", "ひるむ"),
    0x001C0628: Data(DataType.String, 28, "Creating a self-destruction promotion program", "自滅促進プログラムの作成"), # MACHINE_TRANSLATED
    0x001C0644: Data(DataType.String, 28, "Execution of self-destruction promotion program", "自滅促進プログラムの実行"), # MACHINE_TRANSLATED
    0x001C0660: Data(DataType.String, 20, "Unison training decision", "ユニゾン訓練判定"), # MACHINE_TRANSLATED
    0x001C0674: Data(DataType.String, 20, "Small around start", "小アラウンド開始"), # MACHINE_TRANSLATED
    0x001C0688: Data(DataType.String, 20, "Free turn resume", "フリーターン再開"), # MACHINE_TRANSLATED
    0x001C069C: Data(DataType.String, 16, "Peel off the seal", "シールをはがす"), # MACHINE_TRANSLATED
    0x001C06AC: Data(DataType.String, 24, "Check the seal sheet", "シールのシートを確認"), # MACHINE_TRANSLATED
    0x001C06C4: Data(DataType.String, 24, "Talk to Pen Pen", "ペンペンに話しかける"),
    0x001C06DC: Data(DataType.String, 20, "Request a sweepstakes application", "懸賞の応募を頼む"), # MACHINE_TRANSLATED
    0x001C06F0: Data(DataType.String, 28, "Create Kyoto University travel plan", "京都大学出張計画書を作成"), # MACHINE_TRANSLATED
    0x001C070C: Data(DataType.String, 20, "Call Aoba on the phone", "青葉に電話をかける"),
    0x001C0720: Data(DataType.String, 20, "Ask Aoba on a date", "青葉をデートに誘う"),
    0x001C0734: Data(DataType.String, 20, "Question Kaji", "加持を問いただす"),
    0x001C0748: Data(DataType.String, 16, "Invite Misato", "ミサトを誘う"), # MACHINE_TRANSLATED
    0x001C0758: Data(DataType.String, 24, "Unleash the power of Tabris", "タブリスの力を解放する"),
    0x001C0770: Data(DataType.String, 16, "Worry about Fuyutsuki", "冬月を心配する"),
    0x001C0780: Data(DataType.String, 20, "I want to apologize to Touji", "トウジに謝りたい"), # MACHINE_TRANSLATED
    0x001C0794: Data(DataType.String, 20, "Listen to Touji's condition", "トウジの容態を聞く"), # MACHINE_TRANSLATED
    0x001C07A8: Data(DataType.String, 20, "Rei's hospitalization", "レイの入院について"), # MACHINE_TRANSLATED
    0x001C07BC: Data(DataType.String, 24, "About Asuka hospitalization", "アスカの入院について"), # MACHINE_TRANSLATED
    0x001C07D4: Data(DataType.String, 24, "About hospitalization of Touji", "トウジの入院について"), # MACHINE_TRANSLATED
    0x001C07EC: Data(DataType.String, 24, "Regarding Kaworu's hospitalization", "カヲルの入院について"),
    0x001C0804: Data(DataType.String, 24, "Eva repair efficiency increased", "エヴァの修理効率上昇"), # MACHINE_TRANSLATED
    0x001C081C: Data(DataType.String, 24, "Boosting repair efficiency of support facilities", "支援施設の修復効率上昇"),
    0x001C0834: Data(DataType.String, 28, "Strengthen Nerv personnel defense facilities", "ネルフ対人防衛施設の増強"),
    0x001C0850: Data(DataType.String, 20, "Switch vending machine suppliers", "自販機業者の変更"),
    0x001C0864: Data(DataType.String, 20, "Leave Nerv public bath", "ネルフ大浴場を出る"),
    0x001C0878: Data(DataType.String, 20, "Leave firearms training center", "射撃訓練所を出る"),
    0x001C088C: Data(DataType.String, 16, "Jogging Movement", "小走りで移動"),
    0x001C089C: Data(DataType.String, 16, "Check print-out", "プリント確認"),
    0x001C08AC: Data(DataType.String, 20, "Create Seele I.D.", "ゼーレＩＤの作成"),
    0x001C08C0: Data(DataType.String, 20, "Create Special Forged I.D.", "特殊偽造ＩＤの作成"),
    0x001C08D4: Data(DataType.String, 28, "Create Senior Nerv Staff I.D.", "上級ネルフ職員ＩＤの作成"),
    0x001C08F0: Data(DataType.String, 28, "Create Nerv Staff I.D.", "ネルフスタッフＩＤの作成"),
    0x001C090C: Data(DataType.String, 24, "Forge Kyoto Business Trip Manifest", "京都出張計画書の偽造"),
    0x001C0924: Data(DataType.String, 28, "Forge 2nd Branch Inspection Manifest", "第２支部視察計画書の偽造"),
    0x001C0940: Data(DataType.String, 24, "Forge Germany Business Trip Manifest", "ドイツ出張計画書の偽造"),
    0x001C0958: Data(DataType.String, 24, "Forge Antarctic Inspection Manifest", "南極視察計画書の偽造"),
    0x001C0970: Data(DataType.String, 24, "Forge Ogasawara Business Trip Manifest", "小笠原出張計画書の偽造"),
    0x001C0988: Data(DataType.String, 16, "Quit after all", "やっぱりやめる"), # MACHINE_TRANSLATED
    0x001C0998: Data(DataType.String, 20, "Get permission to visit", "面会許可をもらう"), # MACHINE_TRANSLATED
    0x001C09AC: Data(DataType.String, 16, "Pass time at your home", "自宅で過ごす"),
    0x001C09BC: Data(DataType.String, 8, "Reserve", "予備"),
    0x001C09C4: Data(DataType.String, 20, "Dummy IM For Events", "イベント用ダミーIM"),
    0x001C09D8: Data(DataType.String, 20, "Cannot use 12-character title", "12文字ﾀｲﾄﾙ使用不可"), # MACHINE_TRANSLATED
    0x001C09EC: Data(DataType.String, 8, "○○", "○○"),
    0x001C09F4: Data(DataType.String, 8, "Shinji", "シンジ"),
    0x001C09FC: Data(DataType.String, 8, "Asuka", "アスカ"),
    0x001C0A04: Data(DataType.String, 8, "Rei", "レイ"),
    0x001C0A0C: Data(DataType.String, 8, "Misato", "ミサト"),
    0x001C0A14: Data(DataType.String, 12, "Gendo", "ゲンドウ"),
    0x001C0A20: Data(DataType.String, 8, "Fuyutsuki", "冬月"),
    0x001C0A28: Data(DataType.String, 8, "Ritsuko", "リツコ"),
    0x001C0A30: Data(DataType.String, 8, "Maya", "マヤ"), # MACHINE_TRANSLATED
    0x001C0A38: Data(DataType.String, 8, "Hinata", "日向"), # MACHINE_TRANSLATED
    0x001C0A40: Data(DataType.String, 8, "Green leaves", "青葉"), # MACHINE_TRANSLATED
    0x001C0A48: Data(DataType.String, 8, "Holding", "加持"), # MACHINE_TRANSLATED
    0x001C0A50: Data(DataType.String, 8, "Hikari", "ヒカリ"), # MACHINE_TRANSLATED
    0x001C0A58: Data(DataType.String, 8, "Touji", "トウジ"), # MACHINE_TRANSLATED
    0x001C0A60: Data(DataType.String, 12, "Kensuke", "ケンスケ"), # MACHINE_TRANSLATED
    0x001C0A6C: Data(DataType.String, 8, "Kaworu", "カヲル"), # MACHINE_TRANSLATED
    0x001C0A74: Data(DataType.String, 12, "Pen pen", "ペンペン"), # MACHINE_TRANSLATED
    0x001C0A88: Data(DataType.String, 8, "ActChr", "能動者"),
    0x001C0A94: Data(DataType.String, 8, "PsvChr", "受動者"),
    0x001C3884: Data(DataType.String, 36, "Interrupted due to map change due to event\n", "イベントによるマップチェンジで中断\n"), # MACHINE_TRANSLATED
    0x001C3A88: Data(DataType.String, 20, "Misato's Apartment", "ミサトのマンション"),
    0x001C3A9C: Data(DataType.String, 16, "Commander's Office", "総司令公務室"),
    0x001C3AAC: Data(DataType.String, 12, "Command Center 1", "第１発令所"),
    0x001C3AB8: Data(DataType.String, 16, "Misato's Office", "ミサトの執務室"),
    0x001C3AC8: Data(DataType.String, 12, "Nerv Cafeteria", "ネルフ食堂"),
    0x001C3AD4: Data(DataType.String, 16, "Ritsuko's Laboratory", "リツコの研究室"),
    0x001C3AE4: Data(DataType.String, 12, "Kaji's Private Room", "加持の個室"),
    0x001C3AF0: Data(DataType.String, 20, "Vending Machine Corner A", "自販機コーナーＡ"),
    0x001C3B04: Data(DataType.String, 20, "Vending Machine Corner B", "自販機コーナーＢ"),
    0x001C3B18: Data(DataType.String, 16, "Kaworu's Quarters", "カヲルの宿舎"),
    0x001C3B28: Data(DataType.String, 16, "Nerv Public Bath", "ネルフ大浴場"),
    0x001C3B38: Data(DataType.String, 20, "Central Dogma", "セントラルドグマ"),
    0x001C3B4C: Data(DataType.String, 12, "Rei's Room", "レイの部屋"),
    0x001C3B58: Data(DataType.String, 12, "Classroom 2-A", "２−Ａ教室"),
    0x001C3B64: Data(DataType.String, 12, "Convenience Store", "コンビニ"),
    0x001C3B70: Data(DataType.String, 8, "Ruins", "廃墟"),
    0x001C3B78: Data(DataType.String, 20, "%8s：%04d %s：%s\n", "%8s：%04d %s：%s\n"),
    0x001C3B8C: Data(DataType.String, 4, "×", "×"),
    0x001C3B90: Data(DataType.String, 4, "○", "○"),
    0x001C3B94: Data(DataType.String, 12, "%8s：%s\n", "%8s：%s\n"),
    0x001C3BA0: Data(DataType.String, 12, "Invalid ID", "無効ＩＤ"), # MACHINE_TRANSLATED
    0x001C3BAC: Data(DataType.String, 12, "Romantic Comedy", "ラブコメ"),
    0x001C3BB8: Data(DataType.String, 16, "Mysterious", "ミステリアス"),
    0x001C3BC8: Data(DataType.String, 12, "Adult", "アダルト"),
    0x001C3BD4: Data(DataType.String, 8, "School", "学園"),
    0x001C3BDC: Data(DataType.String, 8, "Father and Son", "親子鷹"),
    0x001C3BE4: Data(DataType.String, 12, "Depression", "落ち込み"), # MACHINE_TRANSLATED
    0x001C3BF0: Data(DataType.String, 20, "Character dug up", "キャラ掘り起こし"), # MACHINE_TRANSLATED
    0x001C3C04: Data(DataType.String, 12, "Heap up", "盛り上げる"), # MACHINE_TRANSLATED
    0x001C3C10: Data(DataType.String, 12, "Psychological Portrait", "心理描写"),
    0x001C3C1C: Data(DataType.String, 12, "End brute force", "強引終らせ"), # MACHINE_TRANSLATED
    0x001C3C28: Data(DataType.String, 20, "IM manual selection", "ＩＭ手動選択　　"), # MACHINE_TRANSLATED
    0x001C3C3C: Data(DataType.String, 20, "Repeat conversation", "会話リピート　　"),
    0x001C3C50: Data(DataType.String, 20, "Autoplay", "オートプレイ　　"),
    0x001C3C64: Data(DataType.String, 20, "Automatic conversation progress", "自動会話進行　　"), # MACHINE_TRANSLATED
    0x001C3C78: Data(DataType.String, 20, "Special IM addition", "特殊ＩＭ追加　　"), # MACHINE_TRANSLATED
    0x001C3C8C: Data(DataType.String, 8, "Shinji", "シンジ"),
    0x001C3C94: Data(DataType.String, 8, "Asuka", "アスカ"),
    0x001C3C9C: Data(DataType.String, 8, "Rei", "レイ"),
    0x001C3CA4: Data(DataType.String, 8, "Misato", "ミサト"),
    0x001C3CAC: Data(DataType.String, 12, "Gendo", "ゲンドウ"),
    0x001C3CB8: Data(DataType.String, 8, "Fuyutsuki", "冬月"),
    0x001C3CC0: Data(DataType.String, 8, "Ritsuko", "リツコ"),
    0x001C3CC8: Data(DataType.String, 8, "Maya", "マヤ"),
    0x001C3CD0: Data(DataType.String, 8, "Hyuga", "日向"),
    0x001C3CD8: Data(DataType.String, 8, "Aoba", "青葉"),
    0x001C3CE0: Data(DataType.String, 8, "Kaji", "加持"),
    0x001C3CE8: Data(DataType.String, 8, "Hikari", "ヒカリ"),
    0x001C3CF0: Data(DataType.String, 8, "Toji", "トウジ"),
    0x001C3CF8: Data(DataType.String, 12, "Kensuke", "ケンスケ"),
    0x001C3D04: Data(DataType.String, 8, "Kaworu", "カヲル"),
    0x001C3D0C: Data(DataType.String, 12, "Pen Pen", "ペンペン"),
    0x001C3D18: Data(DataType.String, 32, "Produced Opinion Brief x 1. ", "意見書を１枚、作成しました。"),
    0x001C3D38: Data(DataType.String, 32, "Accepted Opinion Brief x 1.", "意見書を１枚、受理しました。"),
    0x001C3D58: Data(DataType.String, 8, "Standby", "待機"),
    0x001C3D60: Data(DataType.String, 8, "Entrance", "登場"),
    0x001C3D68: Data(DataType.String, 8, "Rest", "休止"),
    0x001C3D70: Data(DataType.String, 8, "Exit", "退場"),
    0x001C3D78: Data(DataType.String, 8, "Passed Away", "死亡"),
    0x001C3D94: Data(DataType.String, 60, "Initiates Do-Nothing Play.\nYou can't go back; sorry about that.", "放置プレイを開始します。\n後戻りはできません、あしからず。"),
    0x001C3DD0: Data(DataType.String, 16, "Daily Special Debug", "日替りデバッグ"),
    0x001C3DE0: Data(DataType.String, 12, "Angel Advent", "使徒出現"),
    0x001C3DEC: Data(DataType.String, 12, "Debut Status", "登場状態"),
    0x001C3DF8: Data(DataType.String, 12, "Hospitalization Status", "入院状態"),
    0x001C3E04: Data(DataType.String, 20, "Character Information", "キャラクター情報"),
    0x001C3E18: Data(DataType.String, 16, "Item Creation", "アイテム作成"),
    0x001C3E28: Data(DataType.String, 20, "Narration Test", "ナレーションテスト"),
    0x001C3E3C: Data(DataType.String, 12, "Written Apology Additions", "始末書追加"),
    0x001C3E48: Data(DataType.String, 12, "Opinion Brief Creation", "意見書作成"),
    0x001C3E54: Data(DataType.String, 12, "Opinion Brief Acceptance", "意見書受理"),
    0x001C3E60: Data(DataType.String, 20, "Eva Repair Work", "エヴァの修復作業"),
    0x001C3E74: Data(DataType.String, 16, "Doors Anywhere", "どこでもドア"),
    0x001C3E84: Data(DataType.String, 16, "Armageddon", "ハルマゲドン"),
    0x001C3E94: Data(DataType.String, 20, "Vending Machines: New Machine Swap-out", "自販機の新台入替"),
    0x001C3EA8: Data(DataType.String, 16, "Business Trip Automatic Vending Machine", "出張自動販売機"),
    0x001C3EB8: Data(DataType.String, 20, "Do-Nothing Play Mode", "放置プレイモード"),
    0x001C3ECC: Data(DataType.String, 20, "Impulse: Situational Output", "ＩＭ使用状況出力"),
    0x001C3EE0: Data(DataType.String, 20, "Impulse: Situational Check", "ＩＭ使用状況確認"),
    0x001C3EF4: Data(DataType.String, 20, "Sufficiency Level: Attenuation Value Interval", "充足度：減衰値間隔"),
    0x001C3F08: Data(DataType.String, 20, "Sufficiency Level: Current Settings", "充足度：現在値設定"),
    0x001C3F1C: Data(DataType.String, 20, "Sufficiency Level: Protagonist Recovery", "充足度：主人公回復"),
    0x001C3F30: Data(DataType.String, 20, "Game Mode Change", "ゲームモード変更"),
    0x001C3F44: Data(DataType.String, 20, "Game Mode Confirmation", "ゲームモード確認"),
    0x001C3F58: Data(DataType.String, 20, "Debug Function Configuration", "デバッグ機能設定"),
    0x001C3F6C: Data(DataType.String, 12, "Confidential Information", "機密情報"),
    0x001C3F78: Data(DataType.String, 12, "Varied Information", "各種情報"),
    0x001C3F84: Data(DataType.String, 12, "Conversation Test", "会話テスト"),
    0x001C3F90: Data(DataType.String, 16, "Fade Off", "フェードＯＦＦ"),
    0x001C3FA0: Data(DataType.String, 16, "Hug Test", "抱き付きテスト"),
    0x001C3FB0: Data(DataType.String, 12, "Emotional Map", "心の地図"),
    0x001C3FBC: Data(DataType.String, 24, "Satisfaction has been restored.", "充足度が回復しました。"), # MACHINE_TRANSLATED
    0x001C3FD4: Data(DataType.String, 32, "Added 10 disclaimers.", "始末書を１０枚追加しました。"), # MACHINE_TRANSLATED
    0x001C3FF4: Data(DataType.String, 20, "Got %s.", "%sを取得しました。"), # MACHINE_TRANSLATED
    0x001C4008: Data(DataType.String, 24, "I have a lot of belongings.", "持ち物がいっぱいです。"), # MACHINE_TRANSLATED
    0x001C4020: Data(DataType.String, 24, "%s%-8s: %s %s%-8s: %s", "%s%-8s：%s　%s%-8s：%s"), # MACHINE_TRANSLATED
    0x001C403C: Data(DataType.String, 12, "%-8s：%DDays\n", "%-8s：%D日\n"),
    0x001C4048: Data(DataType.String, 16, "＜%sMode＞\n", "＜%sモード＞\n"),
    0x001C4058: Data(DataType.String, 28, "Mode Name     [Total Points]\n", "モード名　　　　　[ 得点 ]\n"),
    0x001C4074: Data(DataType.String, 16, "%-16s　[%6d]\n", "%-16s　[%6d]\n"),
    0x001C4084: Data(DataType.String, 28, "−−−−−−−−−−−−−\n", "−−−−−−−−−−−−−\n"),
    0x001C40A0: Data(DataType.String, 28, "Event Programing [%3d,%3d,%3d]\n", "イベント予約 [%3d,%3d,%3d]\n"),
    0x001C40BC: Data(DataType.String, 12, "%s OFF", "%s　ＯＦＦ"),
    0x001C40C8: Data(DataType.String, 12, "%s ON", "%s　ＯＮ"),
    0x001C40D4: Data(DataType.String, 12, "%-20s：%12s", "%-20s：%12s"),
    0x001C40E0: Data(DataType.String, 80, "■ Third Shin-Tokyo City\nTotal damage: %-5D 100 million yen\nReconstruction budget: %-5D 100 million yen\nNumber of restoration: %-5D%/book\n", "■　第三新東京市\n被害総額：%-5D億円\n復興予算：%-5D億円\n復旧本数：%-5D％／本\n"), # MACHINE_TRANSLATED
    0x001C4130: Data(DataType.String, 168, "■ Evangelions\n Total Damage: %-5D hundred million yen\n Repair Budget: %-5D hundred million yen\n Efficiency of Repairs: %-5D ／ HP\n Unit-00: %3D ／ %3D\nUnit-01: %3D／%3D\nUnit-02: %3D／%3D\nUnit-03: %3D／%3D\nUnit-04: %3D／%3D\n", "■ Evangelion\n Total Damage: %-5D hundred million yen\n Repair Budget: %-5D hundred million yen\n Efficiency of Repairs: %-5D ／ HP\n Unit-00: %3D ／ %3D\nUnit-01: %3D／%3D\nUnit-02: %3D／%3D\nUnit-03: %3D／%3D\nUnit-04: %3D／%3D\n"),
    0x001C41D8: Data(DataType.String, 28, "All you can hug.", "抱き付き放題になりました。"), # MACHINE_TRANSLATED
    0x001C41F4: Data(DataType.String, 16, "To whom?", "誰に対する？"), # MACHINE_TRANSLATED
    0x001C4204: Data(DataType.String, 24, "Who's your heart?", "誰の心に入りますか？"), # MACHINE_TRANSLATED
    0x001C421C: Data(DataType.String, 56, "%s\n\nPC active person: %6d\nPC passives: %6d\nBetween NPCs: %6d\n", "%s\n\nＰＣ能動者：%6d\nＰＣ受動者：%6d\nＮＰＣ同士：%6d\n"), # MACHINE_TRANSLATED
    0x001C45A8: Data(DataType.String, 64, "As a result of Dr. Akagi's research,\nthe dummy plug was successfully developed.", "赤木博士の研究成果により、\nダミープラグの開発に成功しました。"),
    0x001C45E8: Data(DataType.String, 68, "As a result of Dr. Akagi's research,\nthe Evas' operation time was\nsuccessfully extended.", "赤木博士の研究成果により、\nエヴァ稼動時間の延長に\n成功しました。"),
    0x001C462C: Data(DataType.String, 68, "As a result of Dr. Akagi's research,\nA.T. Field morphing was\nsuccessfully tested.", "赤木博士の研究成果により、\nΑΤフィールド変形試験に\n成功しました。"),
    0x001C4670: Data(DataType.String, 68, "As a result of Dr. Akagi's research,\nA.T. Field amplification was\nsuccessfully tested.", "赤木博士の研究成果により、\nΑΤフィールド増幅試験に\n成功しました。"),
    0x001C46B4: Data(DataType.String, 16, "(Unknown Map)", "（不明マップ）"),
    0x001C46C4: Data(DataType.String, 12, "First Middle School", "第壱中学校"),
    0x001C46D0: Data(DataType.String, 20, "Misato's Apartment", "ミサトのマンション"),
    0x001C46E4: Data(DataType.String, 16, "Shinji's Room (Old)", "旧シンジの部屋"),
    0x001C46F4: Data(DataType.String, 16, "Shinji's Room (New)", "新シンジの部屋"),
    0x001C4704: Data(DataType.String, 16, "Asuka's Room", "アスカの部屋"),
    0x001C4714: Data(DataType.String, 16, "Misato's Room", "ミサトの部屋"),
    0x001C4724: Data(DataType.String, 16, "Misato's House Bathroom", "ミサト家洗面所"),
    0x001C4734: Data(DataType.String, 16, "Commander's Office", "総司令公務室"),
    0x001C4744: Data(DataType.String, 12, "Command Center 1", "第１発令所"),
    0x001C4750: Data(DataType.String, 8, "Cafeteria", "食堂"),
    0x001C4758: Data(DataType.String, 16, "Ritsuko's Laboratory", "リツコの研究室"),
    0x001C4768: Data(DataType.String, 12, "Kaji's Private Room", "加持の個室"),
    0x001C4774: Data(DataType.String, 16, "Vending Machine Corner", "自販機コーナー"),
    0x001C4784: Data(DataType.String, 16, "Nerv Public Bath", "ネルフ大浴場"),
    0x001C4794: Data(DataType.String, 20, "Central Dogma", "セントラルドグマ"),
    0x001C47A8: Data(DataType.String, 20, "Rei's Apartment", "レイのマンション"),
    0x001C47BC: Data(DataType.String, 12, "Convenience Store", "コンビニ"),
    0x001C47C8: Data(DataType.String, 12, "Surface Ruins", "地上の廃墟"),
    0x001C47D4: Data(DataType.String, 16, "Unit-01's Cage", "初号機ケイジ"),
    0x001C47E4: Data(DataType.String, 16, "Misato's Office", "ミサトの執務室"),
    0x001C47F4: Data(DataType.String, 24, "Tokyo-3             Δ", "第３新東京市　　　　Δ"),
    0x001C480C: Data(DataType.String, 24, "Nerv Facilities     Δ", "ネルフ施設　　　　　Δ"),
    0x001C4824: Data(DataType.String, 8, "Your Home", "自宅"),
    0x001C482C: Data(DataType.String, 8, "Your Room", "自室"),
    0x001C4834: Data(DataType.String, 12, "Highland Park", "高台の公園"),
    0x001C4840: Data(DataType.String, 16, "New Hakone-Yumoto Station", "新箱根湯本駅"),
    0x001C4850: Data(DataType.String, 16, "Unit-00's Cage", "零号機ケイジ"),
    0x001C4860: Data(DataType.String, 16, "Unit-02's Cage", "弐号機ケイジ"),
    0x001C4870: Data(DataType.String, 16, "Unit-03's Cage", "参号機ケイジ"),
    0x001C4880: Data(DataType.String, 16, "Unit-04's Cage", "四号機ケイジ"),
    0x001C4890: Data(DataType.String, 16, "Kaworu's Quarters", "カヲルの宿舎"),
    0x001C48A0: Data(DataType.String, 12, "Kaji's Quarters", "加持の宿舎"),
    0x001C48AC: Data(DataType.String, 16, "Shinji's Quarters", "シンジの宿舎"),
    0x001C48BC: Data(DataType.String, 12, "Rei's Quarters", "レイの宿舎"),
    0x001C48C8: Data(DataType.String, 16, "Asuka's Quarters", "アスカの宿舎"),
    0x001C48D8: Data(DataType.String, 16, "Misato's Quarters", "ミサトの宿舎"),
    0x001C48E8: Data(DataType.String, 16, "Ritsuko's Quarters", "リツコの宿舎"),
    0x001C48F8: Data(DataType.String, 16, "Toji's Quarters", "トウジの宿舎"),
    0x001C4908: Data(DataType.String, 12, "Hyuga's Quarters", "日向の宿舎"),
    0x001C4914: Data(DataType.String, 12, "Aoba's Quarters", "青葉の宿舎"),
    0x001C4920: Data(DataType.String, 12, "Maya's Quarters", "マヤの宿舎"),
    0x001C492C: Data(DataType.String, 12, "Fuyutsuki's Quarters", "冬月の宿舎"),
    0x001C4938: Data(DataType.String, 16, "Gendo's Quarters", "ゲンドウの宿舎"),
    0x001C4948: Data(DataType.String, 12, "Firearms Training Center", "射撃訓練所"),
    0x001C4954: Data(DataType.String, 12, "Executive Staff Quarters", "幹部宿舎"),
    0x001C4960: Data(DataType.String, 12, "Personnel Quarters", "職員宿舎"),
    0x001C496C: Data(DataType.String, 16, "Pilot Quarters", "パイロット宿舎"),
    0x001C4D68: Data(DataType.String, 12, "Go outside", "外に出る"),
    0x001C4E18: Data(DataType.String, 28, "Anyway, I arrived at the end", "とりあえず終端につきました"), # MACHINE_TRANSLATED
    0x001C52CC: Data(DataType.String, 24, "Arrived at destination nowmap=%d\n", "目的地に到着 nowmap=%d\n"), # MACHINE_TRANSLATED
    0x001C5894: Data(DataType.String, 12, "Leave %s", "%sを出る"),
    0x001C58A0: Data(DataType.String, 8, "Don't leave", "出ない"),
    #0x001C58A8: Data(DataType.String, 84, "I still have uncleared products.\nWhether to complete the liquidation of the product\nPlease return the product to the product shelf.", "未清算の商品を持ったままです。\n商品の清算を済ませるか\n商品を商品棚に戻して下さい。"), # MACHINE_TRANSLATED
    0x001C58A8: Data(DataType.String, 84, "DEBUG FIX SHORTER TEXT\nYou have not paid for your items", "未清算の商品を持ったままです。\n商品の清算を済ませるか\n商品を商品棚に戻して下さい。"), # MACHINE_TRANSLATED
    0x001C590C: Data(DataType.String, 48, "Shinji,\nIt's already late today,\nDon't go out.", "シンジ君、\n今日はもう遅いから、\n外出はダメよ。"), # MACHINE_TRANSLATED
    0x001C593C: Data(DataType.String, 12, "Don't go out", "出かけない"), # MACHINE_TRANSLATED
    0x001C5948: Data(DataType.String, 16, "Go out", "外に出かける"), # MACHINE_TRANSLATED
    0x001C5958: Data(DataType.String, 12, "Enter the school building", "校舎に入る"), # MACHINE_TRANSLATED
    0x001C5964: Data(DataType.String, 12, "Don't go in", "入らない"),
    0x001C5970: Data(DataType.String, 12, "Go out on the roof", "屋上に出る"), # MACHINE_TRANSLATED
    0x001C5AEC: Data(DataType.String, 24, "Movement interruption due to passing\n", "すれ違いによる移動中断\n"), # MACHINE_TRANSLATED
    0x001C5B04: Data(DataType.String, 40, "Like looping the same place all the time\n", "ずっと同じ場所をループしているような\n"), # MACHINE_TRANSLATED
    0x001C5E7C: Data(DataType.String, 20, "Coordinate guide ON", "座標ガイド　　ＯＮ"), # MACHINE_TRANSLATED
    0x001C5E90: Data(DataType.String, 24, "Coordinate guide OFF", "座標ガイド　　ＯＦＦ"), # MACHINE_TRANSLATED
    0x001C5EA8: Data(DataType.String, 20, "Resident icon ON", "常駐アイコン　ＯＮ"), # MACHINE_TRANSLATED
    0x001C5EBC: Data(DataType.String, 24, "Resident icon OFF", "常駐アイコン　ＯＦＦ"), # MACHINE_TRANSLATED
    0x001C5ED4: Data(DataType.String, 20, "Character transparency ON", "キャラの透過　ＯＮ"), # MACHINE_TRANSLATED
    0x001C5EE8: Data(DataType.String, 24, "Character transparency OFF", "キャラの透過　ＯＦＦ"), # MACHINE_TRANSLATED
    0x001C5F00: Data(DataType.String, 20, "Automatic wall eraser ON", "自動壁消し　　ＯＮ"), # MACHINE_TRANSLATED
    0x001C5F14: Data(DataType.String, 24, "Automatic wall eraser OFF", "自動壁消し　　ＯＦＦ"), # MACHINE_TRANSLATED
    0x001C5F2C: Data(DataType.String, 20, "Snapshot", "スナップショット"),
    0x001C6BDC: Data(DataType.String, 12, "Range setting", "範囲の設定"), # MACHINE_TRANSLATED
    0x001C6BE8: Data(DataType.String, 16, "Camera Settings", "カメラの設定"),
    0x001C6BF8: Data(DataType.String, 16, "Free Camera", "フリーカメラ"),
    0x001C6C08: Data(DataType.String, 28, "(Corrupted data)", "（壊れているデータです）"), # MACHINE_TRANSLATED
    0x001C6C80: Data(DataType.String, 20, "Use a dedicated camera", "専用カメラを使う"), # MACHINE_TRANSLATED
    0x001C6C94: Data(DataType.String, 24, "Do not use a dedicated camera", "専用カメラを使わない"), # MACHINE_TRANSLATED
    0x001C6D60: Data(DataType.String, 32, "%s has recovered from the shock.", "%sは、ショックから立ち直った。"), # MACHINE_TRANSLATED
    0x001C6D90: Data(DataType.String, 32, "The feelings of %s have subsided.", "%sの浮かれた気持ちは治まった。"), # MACHINE_TRANSLATED
    0x001C6DB0: Data(DataType.String, 12, "Health %3d\n", "体力 %3d\n"), # MACHINE_TRANSLATED
    0x001C6DBC: Data(DataType.String, 12, "Moisture %3d\n", "水分 %3d\n"), # MACHINE_TRANSLATED
    0x001C6DC8: Data(DataType.String, 12, "Sleep %3d\n", "睡眠 %3d\n"), # MACHINE_TRANSLATED
    0x001C6DD4: Data(DataType.String, 12, "Menstruation %3d\n", "生理 %3d\n"), # MACHINE_TRANSLATED
    0x001C6DE0: Data(DataType.String, 12, "Clean %3d\n", "清潔 %3d\n"), # MACHINE_TRANSLATED
    0x001C6E18: Data(DataType.String, 12, "(missing number)", "（欠番）"),
    0x001C6E2C: Data(DataType.String, 16, "Stand up", "　立ちあがる"),
    0x001C6E40: Data(DataType.String, 12, "Living Room", "リビング"),
    0x001C6E4C: Data(DataType.String, 12, "Kitchen", "キッチン"),
    0x001C6E58: Data(DataType.String, 16, "Shinji's Room", "シンジの部屋"),
    0x001C6E68: Data(DataType.String, 8, "Bathroom", "洗面所"),
    0x001C6E70: Data(DataType.String, 16, "Tokyo-3", "第３新東京市"),
    0x001C6E80: Data(DataType.String, 12, "Nerv Facilities", "ネルフ施設"),
    0x001C6E8C: Data(DataType.String, 16, "Executive Staff Quarters Entrance", "幹部宿舎通路"),
    0x001C6E9C: Data(DataType.String, 16, "Personnel Quarters Entrance", "職員宿舎通路"),
    0x001C6EAC: Data(DataType.String, 20, "Pilot Quarters Entrance", "パイロット宿舎通路"),
    0x001C70F8: Data(DataType.String, 28, "We are heading for the visitor", "来客の対応に向かっている"), # MACHINE_TRANSLATED
    0x001C7414: Data(DataType.String, 12, "Synch", "　シンクロ"),
    0x001C7420: Data(DataType.String, 12, "Staff", "　　　参謀"),
    0x001C742C: Data(DataType.String, 12, "Development", "　　　開発"),
    0x001C7438: Data(DataType.String, 12, "Operator", "オペレート"),
    0x001C7444: Data(DataType.String, 12, "Espionage", "　　　諜報"),
    0x001C7488: Data(DataType.String, 16, "     Normal", "　　　　　通常"),
    0x001C7498: Data(DataType.String, 16, "%3d Days Until Hospital Discharge", " 退院まで%3d日"),
    0x001C74B4: Data(DataType.String, 4, "Ten thousand", "万"), # MACHINE_TRANSLATED
    0x001C74CC: Data(DataType.String, 20, "No Items Carried", "所持アイテムなし"),
    0x001C7608: Data(DataType.String, 12, "Introduction", "はじめに"),
    0x001C7614: Data(DataType.String, 12, "Daily Life Section", "生活パート"),
    0x001C7620: Data(DataType.String, 12, "Battle Section", "戦闘パート"),
    0x001C7664: Data(DataType.String, 44, "Information about %s\nFrom %s to %s\nI got up.", "%sに関する情報が\n%sから%sに\nあがりました。"), # MACHINE_TRANSLATED
    0x001C7690: Data(DataType.String, 52, "Underage is prohibited.\nDrinking since I was 20 years old.", "未成年は飲酒禁止です。\nお酒は二十歳になってから。"), # MACHINE_TRANSLATED
    0x001C76C4: Data(DataType.String, 32, "I felt it was very important.", "なんだか大切なものと感じた。"), # MACHINE_TRANSLATED
    0x001C76E4: Data(DataType.String, 20, "Discarded %s.", "%sを捨てました。"),
    0x001C771C: Data(DataType.String, 24, "There is no item.", "アイテムがありません。"),
    0x001C7734: Data(DataType.String, 16, "Use item", "アイテムを使う"),
    0x001C7744: Data(DataType.String, 20, "Discard item", "アイテムを捨てる"),
    0x001C7758: Data(DataType.String, 32, "You are discarding %s.\nIs that okay?\n", "%sを捨てます。\nよろしいですか？"),
    0x001C7778: Data(DataType.String, 20, "Use %s?", "%sを使いますか？"),
    0x001C7790: Data(DataType.String, 12, "Status", "ステータス"),
    0x001C779C: Data(DataType.String, 12, "Relationships", "人間関係"),
    0x001C77A8: Data(DataType.String, 12, "Confidential Information", "機密情報"),
    0x001C77B4: Data(DataType.String, 16, "Tutorial", "チュートリアル"),
    0x001C77C4: Data(DataType.String, 12, "Options", "オプション"),
    0x001C77D0: Data(DataType.String, 16, "Title Screen", "タイトル画面へ"),
    0x001C77E0: Data(DataType.String, 16, "Save Data", "データセーブ"),
    0x001C77F0: Data(DataType.String, 16, "Continue game", "ゲームを続ける"),
    0x001C7800: Data(DataType.String, 16, "Return to title", "タイトルに戻る"),
    0x001C782C: Data(DataType.String, 12, "Unimplemented Functions", "未実装機能"),
    0x001C785C: Data(DataType.String, 60, "Database inoperable due to engagement\nin Angel (including Ireul) battle.", "使徒、イロウルとの戦闘中のため、\nデータセーブは行えません。"),
    0x001C7898: Data(DataType.String, 68, "Database inoperable in Pen Pen's scenario\nexcept after a battle's completion.", "データセーブは、\nペンペンのシナリオでは\n戦闘終了後にのみ行えます。"),
    0x001C78DC: Data(DataType.String, 68, "Database inoperable at maps of\nTokyo-3 and Nerv Facilities.", "データセーブは、\n第３新東京市マップか\nネルフ施設マップで行えます。"),
    0x001C79E8: Data(DataType.String, 28, " I spent a while at home", " しばらく、自宅で過ごした　"), # MACHINE_TRANSLATED
    0x001C7A04: Data(DataType.String, 28, " I spent a while in my room", " しばらく、自室で過ごした　"), # MACHINE_TRANSLATED
    0x001C7A20: Data(DataType.String, 32, " Spent somewhere for a while", " しばらく、どこかで過ごした　"), # MACHINE_TRANSLATED
    0x001C7A64: Data(DataType.String, 32, "EVA%s operating status... Lost\n", "ＥＶＡ%sの稼動状況　…　ロスト\n"), # MACHINE_TRANSLATED
    0x001C7A84: Data(DataType.String, 8, "Medium scale", "中規模"), # MACHINE_TRANSLATED
    0x001C7A8C: Data(DataType.String, 8, "Minor", "軽微"), # MACHINE_TRANSLATED
    0x001C7A94: Data(DataType.String, 8, "Enormous", "甚大"), # MACHINE_TRANSLATED
    0x001C7A9C: Data(DataType.String, 8, "Catastrophic", "壊滅的"), # MACHINE_TRANSLATED
    0x001C7AA4: Data(DataType.String, 8, "undefined", "未定義"), # MACHINE_TRANSLATED
    0x001C7AAC: Data(DataType.String, 36, "Damage to Tokyo-3 ...   %6s\n", "第３新東京市の被害　…　　　　%6s\n"),
    0x001C7AD0: Data(DataType.String, 36, "Operating status of support facilities...%3D%\n", "支援施設の稼動状況　…　　　%3D％\n"), # MACHINE_TRANSLATED
    0x001C7AF4: Data(DataType.String, 32, "EVA%s operating status...%3D%\n", "ＥＶＡ%sの稼動状況　…　%3D％\n"), # MACHINE_TRANSLATED
    0x001C7B44: Data(DataType.String, 28, "%04d:There is no title", "%04d：タイトルがありません"),
    0x001C811C: Data(DataType.String, 16, "Primary person", "主要人物の選択"),
    0x001C812C: Data(DataType.String, 16, "Target person", "対象人物の選択"),
    0x001C8160: Data(DataType.String, 8, "indifferent", "無関心"),
    0x001C8168: Data(DataType.String, 12, "no common ground", "接点が無い"),
    0x001C8174: Data(DataType.String, 8, "I dislike them", "苦手"),
    0x001C817C: Data(DataType.String, 8, "they're an eyesore", "目障り"),
    0x001C8184: Data(DataType.String, 8, "they're hateful", "憎い"),
    0x001C818C: Data(DataType.String, 16, "they're inconsequential", "どうでもいい"),
    0x001C819C: Data(DataType.String, 12, "Ordinary relationship", "普通の関係"), # MACHINE_TRANSLATED
    0x001C81A8: Data(DataType.String, 12, "concern", "気になる"), # MACHINE_TRANSLATED
    0x001C81B4: Data(DataType.String, 12, "Care", "気にかかる"), # MACHINE_TRANSLATED
    0x001C81C0: Data(DataType.String, 12, "Sometimes conversation", "たまに会話"), # MACHINE_TRANSLATED
    0x001C81CC: Data(DataType.String, 16, "Familiar", "馴染みがある"), # MACHINE_TRANSLATED
    0x001C81DC: Data(DataType.String, 8, "Benevolent", "仁慈"), # MACHINE_TRANSLATED
    0x001C81E4: Data(DataType.String, 8, "Longing", "思慕"), # MACHINE_TRANSLATED
    0x001C81EC: Data(DataType.String, 8, "Ugly", "ウザい"), # MACHINE_TRANSLATED
    0x001C81F4: Data(DataType.String, 8, "Dislike", "嫌悪"), # MACHINE_TRANSLATED
    0x001C81FC: Data(DataType.String, 8, "Evasion", "忌避"), # MACHINE_TRANSLATED
    0x001C8204: Data(DataType.String, 12, "Dear", "いとおしい"), # MACHINE_TRANSLATED
    0x001C8210: Data(DataType.String, 8, "Enthusiasm", "熱愛"), # MACHINE_TRANSLATED
    0x001C8218: Data(DataType.String, 8, "friend", "友人"), # MACHINE_TRANSLATED
    0x001C8220: Data(DataType.String, 8, "Close friend", "親友"), # MACHINE_TRANSLATED
    0x001C8228: Data(DataType.String, 8, "Friendship", "心友"), # MACHINE_TRANSLATED
    0x001C8230: Data(DataType.String, 8, "friend", "友達"), # MACHINE_TRANSLATED
    0x001C8238: Data(DataType.String, 8, "I miss", "恋しい"), # MACHINE_TRANSLATED
    0x001C8240: Data(DataType.String, 8, "Dear", "愛しい"), # MACHINE_TRANSLATED
    0x001C8248: Data(DataType.String, 8, "Kindness and Affection", "恩愛"),
    0x001C8304: Data(DataType.String, 8, "--", "−−"),
    0x001C8314: Data(DataType.String, 24, "\n\n━━━━━━━━━━", "\n\n━━━━━━━━━━"),
    0x001C832C: Data(DataType.String, 8, "%9D　", "%9D　"),
    0x001C8338: Data(DataType.String, 20, "　　　　%2D／%2D", "　　　　%2D／%2D"),
    0x001C8364: Data(DataType.String, 12, "Shinji", "シンジ　"),
    0x001C8370: Data(DataType.String, 12, "Asuka", "アスカ　"),
    0x001C837C: Data(DataType.String, 12, "Rei", "レイ　　"),
    0x001C8388: Data(DataType.String, 12, "Misato", "ミサト　"),
    0x001C8394: Data(DataType.String, 12, "Gendo", "ゲンドウ"),
    0x001C83A0: Data(DataType.String, 12, "Fuyutsuki", "冬月　　"),
    0x001C83AC: Data(DataType.String, 12, "Ritsuko", "リツコ　"),
    0x001C83B8: Data(DataType.String, 12, "Maya", "マヤ　　"),
    0x001C83C4: Data(DataType.String, 12, "Hyuga", "日向　　"),
    0x001C83D0: Data(DataType.String, 12, "Aoba", "青葉　　"),
    0x001C83DC: Data(DataType.String, 12, "Kaji", "加持　　"),
    0x001C83E8: Data(DataType.String, 12, "Hikari", "ヒカリ　"),
    0x001C83F4: Data(DataType.String, 12, "Toji", "トウジ　"),
    0x001C8400: Data(DataType.String, 12, "Kensuke", "ケンスケ"),
    0x001C840C: Data(DataType.String, 12, "Kaworu", "カヲル　"),
    0x001C8418: Data(DataType.String, 12, "Pen Pen", "ペンペン"),
    0x001C8424: Data(DataType.String, 12, "Nerv Man", "ネルフ男"),
    0x001C8430: Data(DataType.String, 12, "Nerv Woman", "ネルフ女"),
    0x001C843C: Data(DataType.String, 12, "Convenience Store", "コンビニ"),
    0x001C8448: Data(DataType.String, 12, "(Normal)", "（通常）"),
    0x001C8454: Data(DataType.String, 12, "(Angry)", "（怒り）"),
    0x001C8460: Data(DataType.String, 12, "(Sad)", "（悲しみ）"),
    0x001C846C: Data(DataType.String, 12, "(Happy)", "（笑い）"),
    0x001C8478: Data(DataType.String, 12, "(Serious)", "（真剣）"),
    0x001C8484: Data(DataType.String, 12, "(Amorous)", "（発情）"),
    0x001C8490: Data(DataType.String, 12, "(Perplexed)", "（困惑）"),
    0x001C849C: Data(DataType.String, 12, "(Surprised)", "（驚き）"),
    0x001C84A8: Data(DataType.String, 12, "(Sullen)", "（不機嫌）"),
    0x001C84B4: Data(DataType.String, 12, "(Special A)", "（特殊Ａ）"),
    0x001C84C0: Data(DataType.String, 12, "(Special B)", "（特殊Ｂ）"),
    0x001C84CC: Data(DataType.String, 12, "(Special C)", "（特殊Ｃ）"),
    0x001C84D8: Data(DataType.String, 12, "(Special D)", "（特殊Ｄ）"),
    0x001C84E4: Data(DataType.String, 12, "(Special E)", "（特殊Ｅ）"),
    0x001C84F0: Data(DataType.String, 12, "(Special F)", "（特殊Ｆ）"),
    0x001C84FC: Data(DataType.String, 12, "(Special G)", "（特殊Ｇ）"),
    0x001C8508: Data(DataType.String, 12, "(Special H)", "（特殊Ｈ）"),
    0x001C8514: Data(DataType.String, 12, "(Special I)", "（特殊Ｉ）"),
    0x001C8528: Data(DataType.String, 20, "IM-%04d 〜 IM-%04d", "IM-%04d 〜 IM-%04d"),
    0x001C853C: Data(DataType.String, 12, "IntChr:%s", "乱入者：%s"),
    0x001C8548: Data(DataType.String, 12, "PsvChr:%s", "受動者：%s"),
    0x001C8554: Data(DataType.String, 12, "ActChr:%s", "能動者：%s"),
    0x001C8568: Data(DataType.String, 20, " = Execute = ", "　＝　実行　＝　"),
    0x001C857C: Data(DataType.String, 12, "Not applicable", "該当なし"),
    0x001C85AC: Data(DataType.String, 8, "IntChr", "能動者"),
    0x001C85B4: Data(DataType.String, 8, "PsvChr", "受動者"),
    0x001C85BC: Data(DataType.String, 8, "ActChr", "乱入者"),
    0x001C8640: Data(DataType.String, 24, "Clerical skill went up by %D!", "事務技能が%D上がった！"),
    0x001C8778: Data(DataType.String, 12, "%-18s %3dyen", "%-18s %3d円"),
    0x001C8784: Data(DataType.String, 20, "After all I do not buy", "やっぱり買わない"), # MACHINE_TRANSLATED
    0x001C879C: Data(DataType.String, 28, "Interest%-4D\nFavor%-4D\nRating: %s", "関心%-4D\n好意%-4D\n評価：%s"), # MACHINE_TRANSLATED
    0x001C87B8: Data(DataType.String, 24, "%s addressed to you.", "%sが話し掛けてきた。"),
    0x001C87D0: Data(DataType.String, 36, "Next to sleeping %s\n%s is standing.", "寝ている%sの横に\n%sが佇んでいる。"), # MACHINE_TRANSLATED
    0x001C87F4: Data(DataType.String, 24, "%s is hugging.", "%sが抱きついてきた。"), # MACHINE_TRANSLATED
    0x001C880C: Data(DataType.String, 28, "%s is checking in on %s.", "%sの様子を%sが見ている。"),
    0x001C8828: Data(DataType.String, 32, "It seems someone has stopped by to visit.", "誰か訪ねてきた、来客のようだ。"),
    0x001C8848: Data(DataType.String, 24, "%s is approaching your side.", "%sが側に近づいてきた。"), # MACHINE_TRANSLATED
    0x001C8860: Data(DataType.String, 20, "Clear greetings and resumes", "挨拶と再開のクリア"), # MACHINE_TRANSLATED
    0x001C8874: Data(DataType.String, 16, "Set greeting only", "挨拶のみ設定"), # MACHINE_TRANSLATED
    0x001C8884: Data(DataType.String, 20, "Greetings and resume settings", "挨拶と再開の設定"), # MACHINE_TRANSLATED
    0x001C8898: Data(DataType.String, 8, "Normal", "通常"),
    0x001C88A0: Data(DataType.String, 8, "Destruction", "破壊"), # MACHINE_TRANSLATED
    0x001C88A8: Data(DataType.String, 8, "Medium destruction", "中破壊"), # MACHINE_TRANSLATED
    0x001C88B0: Data(DataType.String, 8, "Great destruction", "大破壊"), # MACHINE_TRANSLATED
    0x001C88B8: Data(DataType.String, 12, "Housework skills", "家事技能"), # MACHINE_TRANSLATED
    0x001C88C4: Data(DataType.String, 12, "Clerical Skill", "事務技能"),
    0x001C88D0: Data(DataType.String, 12, "Information Skill", "情報技能"),
    0x001C88DC: Data(DataType.String, 12, "Battle Skill", "戦闘技能"),
    0x001C88E8: Data(DataType.String, 12, "A.T. Increase", "ＡＴアップ"),
    0x001C88F4: Data(DataType.String, 12, "A.T. Decrease", "ＡＴダウン"),
    0x001C8900: Data(DataType.String, 16, "A.T. Large Increase", "ＡＴ大アップ"),
    0x001C8910: Data(DataType.String, 16, "A.T. Large Decrease", "ＡＴ大ダウン"),
    0x001C8920: Data(DataType.String, 16, "AT divisor change", "ＡＴ除数変更"), # MACHINE_TRANSLATED
    0x001C8930: Data(DataType.String, 12, "Baldly", "はげまして"), # MACHINE_TRANSLATED
    0x001C893C: Data(DataType.String, 16, "Tell me that you like", "好きだと伝えて"), # MACHINE_TRANSLATED
    0x001C894C: Data(DataType.String, 20, "Tell me that you care", "気になると伝えて"), # MACHINE_TRANSLATED
    0x001C8960: Data(DataType.String, 20, "Tell me that you are not interested", "興味がないと伝えて"), # MACHINE_TRANSLATED
    0x001C8974: Data(DataType.String, 20, "Tell me it's an eyesore", "目障りだと伝えて"), # MACHINE_TRANSLATED
    0x001C8988: Data(DataType.String, 16, "Tell me I hate", "嫌いと伝えて"), # MACHINE_TRANSLATED
    0x001C8998: Data(DataType.String, 12, "Be careful", "気をつけて"), # MACHINE_TRANSLATED
    0x001C89DC: Data(DataType.String, 8, "What kind", "どんな"), # MACHINE_TRANSLATED
    0x001C89E4: Data(DataType.String, 12, "School Arrival", "学校出現"),
    0x001C89F0: Data(DataType.String, 12, "Nerv Arrival", "ネルフ出現"),
    0x001C89FC: Data(DataType.String, 20, "Rei's Apartment", "レイのマンション"),
    0x001C8A10: Data(DataType.String, 12, "All Angels Defeated", "使徒全滅"),
    0x001C8A1C: Data(DataType.String, 20, "Shinji's Allowance 1st Time", "シンジ小遣い初回"),
    0x001C8A30: Data(DataType.String, 20, "Asuka's Allowance 1st Time", "アスカ小遣い初回"),
    0x001C8A44: Data(DataType.String, 16, "Shinji's Allowance", "シンジ小遣い"),
    0x001C8A54: Data(DataType.String, 16, "Asuka's Allowance", "アスカ小遣い"),
    0x001C8A64: Data(DataType.String, 16, "During Ireul Battle", "イロウル戦中"),
    0x001C8A74: Data(DataType.String, 20, "Announcer: Dummy Plug", "アナ：ダミープラグ"),
    0x001C8A88: Data(DataType.String, 24, "Announcer: Operational Time Extension", "アナ：稼動時間の延長"),
    0x001C8AA0: Data(DataType.String, 20, "Announcer: A.T. Field Morphing", "アナ：ＡＴＦ変形"),
    0x001C8AB4: Data(DataType.String, 20, "Announcer: A.T. Field Amplification", "アナ：ＡＴＦ増幅"),
    0x001C8AC8: Data(DataType.String, 20, "Development: Dummy Plug", "開発：ダミープラグ"),
    0x001C8ADC: Data(DataType.String, 24, "Development: Operational Time Extension", "開発：稼動時間の延長"),
    0x001C8AF4: Data(DataType.String, 20, "Development: A.T. Field Morphing", "開発：ＡＴＦ変形"),
    0x001C8B08: Data(DataType.String, 20, "Development: A.T. Field Amplification", "開発：ＡＴＦ増幅"),
    0x001C8B1C: Data(DataType.String, 12, "First greeting", "初回挨拶"), # MACHINE_TRANSLATED
    0x001C8B28: Data(DataType.String, 8, "message", "伝言"), # MACHINE_TRANSLATED
    0x001C8B30: Data(DataType.String, 12, "Greetings and resumption", "挨拶と再開"), # MACHINE_TRANSLATED
    0x001C8B3C: Data(DataType.String, 16, "Labyrinth of the Heart 35", "心の迷宮３５"),
    0x001C8B4C: Data(DataType.String, 16, "School preparation 223", "学校準備２２３"), # MACHINE_TRANSLATED
    0x001C8B5C: Data(DataType.String, 16, "Mobile phone 238", "携帯電話２３８"), # MACHINE_TRANSLATED
    0x001C8B6C: Data(DataType.String, 28, "Nerv Cafeteria 341-345", "ネルフ食堂３４１−３４５"),
    0x001C8B88: Data(DataType.String, 36, "Pilot leaving home 358-364", "パイロット辞め家出３５８−３６４"), # MACHINE_TRANSLATED
    0x001C8BAC: Data(DataType.String, 12, "Runaway 598", "家出５９８"),
    0x001C8BB8: Data(DataType.String, 16, "Related to Command Center Chairs", "発令所椅子関係"),
    0x001C8BC8: Data(DataType.String, 16, "Toilet syndrome", "トイレ症候群"), # MACHINE_TRANSLATED
    0x001C8BD8: Data(DataType.String, 8, "Opinion Brief", "意見書"),
    0x001C8C40: Data(DataType.String, 12, "Full opening", "学園全開"), # MACHINE_TRANSLATED
    0x001C8C4C: Data(DataType.String, 12, "School Entrance", "学校登場"),
    0x001C8C58: Data(DataType.String, 12, "Kaworu Enters", "カヲル登場"),
    0x001C8C64: Data(DataType.String, 12, "Asuka Arrives", "アスカ来日"),
    0x001C8C70: Data(DataType.String, 12, "Rei Enters", "レイ登場"),
    0x001C8C7C: Data(DataType.String, 20, "Kaworu Piloting", "カヲルパイロット"),
    0x001C8C90: Data(DataType.String, 20, "Toji Piloting", "トウジパイロット"),
    0x001C8CDC: Data(DataType.String, 20, "Kyoto Trip (2 days and 1 night)", "京都１泊２日の旅"),
    0x001C8CF0: Data(DataType.String, 16, "America Trip", "アメリカ旅行"),
    0x001C8D00: Data(DataType.String, 16, "Aurora Watching", "オーロラ見物"),
    0x001C8D10: Data(DataType.String, 12, "Ogasaware Business Trip", "小笠原出張"),
    0x001C8D1C: Data(DataType.String, 20, "Want to go to Germany?", "ドイツに行きたいか"),
    0x001C8D58: Data(DataType.String, 12, "Impulse Setup", "ＩＭ準備"),
    0x001C8D64: Data(DataType.String, 16, "TV Ending Setup", "ＴＶ−ＥＤ準備"),
    0x001C8D74: Data(DataType.String, 12, "Daddy Love", "パパらぶ"),
    0x001C8D80: Data(DataType.String, 12, "Dogma Arrival", "ドグマ出現"),
    0x001C8D8C: Data(DataType.String, 12, "Character Operations", "人物操作"),
    0x001C8D98: Data(DataType.String, 12, "A.T. Operations", "ＡＴ操作"),
    0x001C8DA4: Data(DataType.String, 12, "Rei Replacement", "レイ交換"),
    0x001C8DB0: Data(DataType.String, 12, "Technique Up", "技能アップ"),
    0x001C8DBC: Data(DataType.String, 12, "Flag Operations", "フラグ操作"),
    0x001C8DC8: Data(DataType.String, 12, "Extent of City's Destruction", "街破壊度"),
    0x001C8DD4: Data(DataType.String, 12, "Seele's Ire", "ゼーレ怒る"),
    0x001C8DE0: Data(DataType.String, 8, "Business Trip", "出張"),
    0x001C8DE8: Data(DataType.String, 16, "Damage Processing", "ダメージ処理"),
    0x001C8E60: Data(DataType.String, 20, "%s was obtained.", "%sを入手しました。"),
    0x001C8E74: Data(DataType.String, 20, "Impulse Debug Function", "ＩＭデバッグ機能"),
    0x001C8E88: Data(DataType.String, 8, "to whom", "誰に"),
    0x001C8E90: Data(DataType.String, 12, "from whom", "誰からの"),
    0x001C8E9C: Data(DataType.String, 8, "Extent of destruction", "破壊度"),
    0x001C8EA4: Data(DataType.String, 20, "Rei was replaced", "レイが交換された"),
    0x001C8EB8: Data(DataType.String, 12, "Technique Selection", "技能選択"),
    0x001C8EC4: Data(DataType.String, 12, "%-20s　%s", "%-20s　%s"),
    0x001C8ED0: Data(DataType.String, 4, "○", "○"),
    0x001C8ED4: Data(DataType.String, 4, "×", "×"),
    0x001C8ED8: Data(DataType.String, 12, "Full school", "学校全開"), # MACHINE_TRANSLATED
    0x001C8EE4: Data(DataType.String, 32, "Kaworu became a pilot", "カヲルがパイロットになりました"),
    0x001C8F04: Data(DataType.String, 32, "Toji became a pilot", "トウジがパイロットになりました"),
    0x001C8F24: Data(DataType.String, 24, "I made the first greeting", "初回挨拶済みにしました"), # MACHINE_TRANSLATED
    0x001C8F3C: Data(DataType.String, 16, "Anger + 20", "怒り＋２０個"),
    0x001C8F4C: Data(DataType.String, 16, "%s is hungry.", "%sは腹へった。"),
    0x001C8F5C: Data(DataType.String, 28, "Bump off Nerv staff member", "ネルフスタッフを消します"),
    0x001C8F78: Data(DataType.String, 16, "%s is dead.", "%sは死んだ。"),
    0x001C8F88: Data(DataType.String, 24, "Tempted to run away from home.", "家出したくなります。"),
    0x001C8FA0: Data(DataType.String, 32, "Pilot is tempted to quit.", "パイロット辞めたくなります。"),
    0x001C8FC0: Data(DataType.String, 32, "Everyone gets the urge to pee.", "皆トイレに行きたくなります。"),
    0x001C8FE0: Data(DataType.String, 16, "Summoned %s.", "%sを召喚した。"),
    0x001C8FF0: Data(DataType.String, 24, "Made it 8:00AM", "ＡＭ８：００にしました"),
    0x001C9008: Data(DataType.String, 24, "Received opinion brief", "意見書を受け取りました"),
    0x001C9020: Data(DataType.String, 20, "A.T=%3d  Divisor=%5d", "ＡＴ＝%3d 除数＝%5d"),
    0x001C9048: Data(DataType.String, 24, "Central Dogma appeared.", "セントラルドグマ出現。"),
    0x001C9060: Data(DataType.String, 28, "On good terms with %s.", "%sと、なかよくなります。"),
    0x001C907C: Data(DataType.String, 44, "Branch off into TV ending via labyrinth of the heart.", "心の迷宮でＴＶエンディングに分岐します。"),
    0x001C90A8: Data(DataType.String, 28, "Set assassination conditions", "暗殺系の条件を設定します"), # MACHINE_TRANSLATED
    0x001C90C4: Data(DataType.String, 28, "Take a lot of damage", "いろいろダメージを受けます"), # MACHINE_TRANSLATED
    0x001C90E0: Data(DataType.String, 24, "%s received damage.", "%sはダメージを受けた。"),
    0x001C90F8: Data(DataType.String, 24, "%s came closer.", "%sが、近づいてきた。"),
    0x001C920C: Data(DataType.String, 8, "Asuka", "アスカ"),
    0x001C9214: Data(DataType.String, 4, "My", "私"),
    0x001C9218: Data(DataType.String, 12, "Second", "セカンド"),
    0x001C9224: Data(DataType.String, 8, "Wark", "グエッ"),
    0x001C922C: Data(DataType.String, 8, "Mother", "母さん"),
    0x001C9234: Data(DataType.String, 16, "Shinji's mom", "シンジのママ"),
    0x001C9244: Data(DataType.String, 16, "Ikari-kun's mother", "碇君のお母さん"),
    0x001C9254: Data(DataType.String, 20, "Shinji-kun's mother", "シンジ君のお母さん"),
    0x001C9268: Data(DataType.String, 8, "Yui", "ユイ"),
    0x001C9270: Data(DataType.String, 8, "Yui-kun", "ユイ君"),
    0x001C9278: Data(DataType.String, 16, "Shinji's mom", "シンジのおかん"),
    0x001C9288: Data(DataType.String, 20, "Shinji's mother", "シンジのお母さん"),
    0x001C929C: Data(DataType.String, 8, "Father", "父さん"),
    0x001C92A4: Data(DataType.String, 8, "Commander Ikari", "碇司令"),
    0x001C92AC: Data(DataType.String, 4, "Ikari", "碇"),
    0x001C92B0: Data(DataType.String, 16, "Ikari's father", "碇君のお父さん"),
    0x001C92C0: Data(DataType.String, 16, "Shinji's dad", "シンジのおとん"),
    0x001C92D0: Data(DataType.String, 16, "Father's objective", "父さんの目的"),
    0x001C92E0: Data(DataType.String, 20, "Commander Ikari's plan", "碇司令のたくらみ"),
    0x001C92F4: Data(DataType.String, 16, "Commander Ikari's objective", "碇司令の目的"),
    0x001C9304: Data(DataType.String, 12, "My objective", "私の目的"),
    0x001C9310: Data(DataType.String, 12, "Ikari's objective", "碇の目的"),
    0x001C931C: Data(DataType.String, 24, "Shinji's father's objective", "碇君のお父さんの目的"),
    0x001C9334: Data(DataType.String, 24, "Shinji's dad's objective", "シンジのおとんの目的"),
    0x001C9350: Data(DataType.String, 24, "Second Child", "セカンド・チルドレン"),
    0x001C936C: Data(DataType.String, 12, "1000", "１０００"),
    0x001C9378: Data(DataType.String, 12, "2000", "２０００"),
    0x001C9384: Data(DataType.String, 12, "4000", "４０００"),
    0x001C9390: Data(DataType.String, 12, "50000", "５００００"),
    0x001C939C: Data(DataType.String, 12, "40000", "４００００"),
    0x001C93A8: Data(DataType.String, 12, "30000", "３００００"),
    0x001C93B4: Data(DataType.String, 12, "20000", "２００００"),
    0x001C93C0: Data(DataType.String, 8, "700", "７００"),
    0x001C93C8: Data(DataType.String, 8, "100", "１００"),
    0x001C93D0: Data(DataType.String, 20, "No self-confidence", "自分に自信がない"),
    0x001C93E4: Data(DataType.String, 12, "Romantic advice", "恋愛相談"),
    0x001C93F0: Data(DataType.String, 16, "Relationship advice", "人間関係の相談"),
    0x001C9400: Data(DataType.String, 16, "About the future", "今後について"),
    0x001C943C: Data(DataType.String, 28, "Please select an\nitem to give", "渡すアイテムを\n選んで下さい"),
    0x001C94DC: Data(DataType.String, 36, "More importantly,\nI'm so hungry I could faint...", "そんな事より、\n空腹で倒れそうだ…。"),
    0x001C9500: Data(DataType.String, 40, "More importantly,\nI'm so thirsty I could die...", "そんな事より、\n喉が渇いて死にそうだ…。"),
    0x001C9528: Data(DataType.String, 44, "More importantly,\nI\\m so tired I can't think...", "そんな事より、\n眠くて何も考えられない…。"),
    0x001C9554: Data(DataType.String, 48, "More importantly, a toilet\nis all I can think about...", "そんな事より、\nトイレの事しか考えられない…。"),
    0x001C9584: Data(DataType.String, 56, "More importantly, even a\nshower wouldn't get me clean...", "そんな事より、シャワーでも浴びて\n清潔にならないと…。"),
    0x001C95BC: Data(DataType.String, 44, "Than that\nI'm hungry and motivated...", "そんな事より、\n空腹でやる気が起きない…。"), # MACHINE_TRANSLATED
    0x001C95E8: Data(DataType.String, 44, "Than that\nI'm thirsty and I can't turn my head...", "そんな事より、\n喉が渇いて、頭が回らない…。"), # MACHINE_TRANSLATED
    0x001C9614: Data(DataType.String, 40, "Than that\nI'm sleepy and unmotivated...", "そんな事より、\n眠くて意欲が湧かない…。"), # MACHINE_TRANSLATED
    0x001C963C: Data(DataType.String, 40, "Than that\nI have to go to the toilet...", "そんな事より、\nトイレに行かないと…。"), # MACHINE_TRANSLATED
    0x001C9664: Data(DataType.String, 40, "Than that\nDirty and restless...", "そんな事より、\n不潔で落ちつかない…。"), # MACHINE_TRANSLATED
    0x001C96C4: Data(DataType.String, 44, "Went through the daily grind of school\nand was then dismissed.", "学校で学校生活を行い\nそして放課後になった。"),
    0x001C9764: Data(DataType.String, 32, "The phone doesn't seem to connect now.", "今は電話が繋がらないようだ。"), # MACHINE_TRANSLATED
    0x001C9784: Data(DataType.String, 20, "The Third Child", "サード・チルドレン"),
    0x001C9798: Data(DataType.String, 8, "Mystery Person", "謎の人"),
    0x001C97A0: Data(DataType.String, 24, "The Second Child", "セカンド・チルドレン"),
    0x001C97B8: Data(DataType.String, 24, "The First Child", "ファースト・チルドレン"),
    0x001C97D0: Data(DataType.String, 12, "Major Katsuragi", "葛城三佐"),
    0x001C97DC: Data(DataType.String, 12, "Captain Katsuragi", "葛城一尉"),
    0x001C97E8: Data(DataType.String, 12, "Commander-in-Chief- Ikari", "碇総司令"),
    0x001C97F4: Data(DataType.String, 12, "Deputy Commander Fuyutsuki", "冬月副司令"),
    0x001C9800: Data(DataType.String, 12, "Dr. Akagi", "赤木博士"),
    0x001C980C: Data(DataType.String, 12, "2nd Lt. Ibuki", "伊吹二尉"),
    0x001C9818: Data(DataType.String, 12, "2nd Lt. Hyuga", "日向二尉"),
    0x001C9824: Data(DataType.String, 12, "2nd Lt. Aoba", "青葉二尉"),
    0x001C9830: Data(DataType.String, 28, "Special Audit Department, Ryoji Kamochi", "特殊監査部、加持リョウジ"), # MACHINE_TRANSLATED
    0x001C984C: Data(DataType.String, 12, "Hikari Horaki", "洞木ヒカリ"),
    0x001C9858: Data(DataType.String, 24, "Fourth Child", "フォース・チルドレン"),
    0x001C9870: Data(DataType.String, 12, "Toji Suzuhara", "鈴原トウジ"),
    0x001C987C: Data(DataType.String, 16, "Kensuke Aida", "相田ケンスケ"),
    0x001C988C: Data(DataType.String, 24, "The Fifth Child", "フィフス・チルドレン"),
    0x001C98E8: Data(DataType.String, 20, "Hospitalized in Central Hospital", "中央病院に入院中"), # MACHINE_TRANSLATED
    0x001C9974: Data(DataType.String, 12, "Command Center 1", "第１発令所"),
    0x001C9980: Data(DataType.String, 16, "Katsuragi Misa's home", "葛城三佐の自宅"), # MACHINE_TRANSLATED
    0x001C9990: Data(DataType.String, 16, "Katsuragi's home", "葛城一尉の自宅"), # MACHINE_TRANSLATED
    0x001C99A0: Data(DataType.String, 16, "Commander's Office", "総司令公務室"),
    0x001C99B0: Data(DataType.String, 20, "Major Katsuragi's Office", "葛城三佐の執務室"),
    0x001C99C4: Data(DataType.String, 20, "Captain Katsuragi's Office", "葛城一尉の執務室"),
    0x001C99D8: Data(DataType.String, 16, "Nerv Cafeteria", "ネルフ内食堂"),
    0x001C99E8: Data(DataType.String, 20, "Dr. Akagi's Laboratory", "赤木博士の研究室"),
    0x001C99FC: Data(DataType.String, 20, "Inspector Kaji's Private Room", "加持監察官の執務室"),
    0x001C9A10: Data(DataType.String, 20, "vending machine corner", "自動販売機コーナー"),
    0x001C9A24: Data(DataType.String, 16, "Nerv Public Bath", "ネルフ大浴場"),
    0x001C9A34: Data(DataType.String, 12, "First Middle School", "第壱中学校"),
    0x001C9A40: Data(DataType.String, 24, "going to Tokyo-3", "第３新東京市を移動中"),
    0x001C9A58: Data(DataType.String, 16, "inside the convenience store", "市内のコンビニ"),
    0x001C9A68: Data(DataType.String, 20, "Tokyo-3 Ruins", "第３新東京市廃墟"),
    0x001C9A7C: Data(DataType.String, 16, "Unit-01's Cage", "初号機ケイジ"),
    0x001C9A8C: Data(DataType.String, 24, "Moving in the nerf facility", "ネルフ施設内を移動中"), # MACHINE_TRANSLATED
    0x001C9AA4: Data(DataType.String, 8, "home", "自宅"), # MACHINE_TRANSLATED
    0x001C9AAC: Data(DataType.String, 24, "on standby at their quarters in Nerv", "ネルフ内宿舎で待機中"),
    0x001C9AC4: Data(DataType.String, 28, "the First Child's home", "ファースト・チルドレン宅"),
    0x001C9AE0: Data(DataType.String, 8, "somewhere", "どこか"),
    0x001C9AE8: Data(DataType.String, 16, "the roof of the First Middle School", "第壱中学校屋上"),
    0x001C9AF8: Data(DataType.String, 12, "the city park", "市内公園"),
    0x001C9B04: Data(DataType.String, 16, "New Hakone-Yumoto Station", "新箱根湯本駅"),
    0x001C9B14: Data(DataType.String, 16, "Unit-00's Cage", "零号機ケイジ"),
    0x001C9B24: Data(DataType.String, 16, "Unit-02's Cage", "弐号機ケイジ"),
    0x001C9B34: Data(DataType.String, 16, "Unit-03's Cage", "参号機ケイジ"),
    0x001C9B44: Data(DataType.String, 16, "Unit-04's Cage", "四号機ケイジ"),
    0x001C9B54: Data(DataType.String, 16, "Near Nerv H.Q.", "ネルフ本部脇"),
    0x001C9B64: Data(DataType.String, 16, "Pilot Quarters", "パイロット宿舎"),
    0x001C9B74: Data(DataType.String, 16, "Nerv Personnel Quarters", "ネルフ職員宿舎"),
    0x001C9B84: Data(DataType.String, 12, "Executive Staff Quarters", "幹部宿舎"),
    0x001C9B90: Data(DataType.String, 16, "School road to school", "学校への通学路"), # MACHINE_TRANSLATED
    0x001C9BA0: Data(DataType.String, 24, "Nerv Escalator", "ネルフエスカレーター"),
    0x001C9BB8: Data(DataType.String, 12, "Test Site 7", "第７実験場"),
    0x001C9BC4: Data(DataType.String, 8, "Test Site", "実験場"),
    0x001C9BCC: Data(DataType.String, 12, "Firearms Training Center", "射撃訓練所"),
    0x001C9BD8: Data(DataType.String, 16, "Executive Staff Quarters Corridor", "幹部宿舎廊下"),
    0x001C9BE8: Data(DataType.String, 20, "Nerv Personnel Quarters Corridor", "ネルフ職員宿舎廊下"),
    0x001C9BFC: Data(DataType.String, 20, "Pilot Quarters Corridor", "パイロット宿舎廊下"),
    0x001CA3E8: Data(DataType.String, 20, "Didn't find anything.", "何も見つからない。"),
    0x001CA3FC: Data(DataType.String, 16, "Found %s.", "%sを見つけた。"),
    0x001CA40C: Data(DataType.String, 48, "Cannot keep item because inventory is full.", "アイテムがいっぱいなので持つことができない。"),
    0x001CA43C: Data(DataType.String, 20, "%s is\nPassed %s.", "%sは、\n%sを渡した。"), # MACHINE_TRANSLATED
    0x001CA468: Data(DataType.String, 12, "Toothpicks", "つまようじ"),
    0x001CA474: Data(DataType.String, 8, "Cleaning cloth", "台布巾"),
    0x001CA47C: Data(DataType.String, 8, "Toilet paper", "ちり紙"),
    0x001CA484: Data(DataType.String, 12, "Nail clippers", "つめ切り"),
    0x001CA490: Data(DataType.String, 20, "T.V. Remote", "テレビのリモコン"),
    0x001CA4A8: Data(DataType.String, 32, "There are no people to evaluate.", "評価できる相手が存在しません。"), # MACHINE_TRANSLATED
    0x001CA4E4: Data(DataType.String, 28, "%s's person rating for %s", "%sの、%sに対する人物評価"), # MACHINE_TRANSLATED
    0x001CA580: Data(DataType.String, 16, "Nerv Deluxe Special", "ネルフ豪華定食"),
    0x001CA590: Data(DataType.String, 16, "Nerv [A] Special", "ネルフＡ定食"),
    0x001CA5A0: Data(DataType.String, 16, "Fried Egg Special", "目玉焼き定食"),
    0x001CA5B0: Data(DataType.String, 12, "Seaweed Special", "のり定食"),
    0x001CA5BC: Data(DataType.String, 12, "Suudon", "すうどん"),
    0x001CA658: Data(DataType.String, 72, "%s left the city...\nAnd then back to Nerve again\nI never came...", "%sは、街を出た…。\nそして、二度とネルフに戻って\n来ることはなかった…。"), # MACHINE_TRANSLATED
    0x001CA6B4: Data(DataType.String, 20, "%s \n handed over %s.", "%sは、\n%sを渡した。"),
    0x001CA6C8: Data(DataType.String, 20, "%s \n handed over %s.", "%sは、\n%sを渡した。"),
    0x001CA840: Data(DataType.String, 8, "Go in", "入る"),
    0x001CA848: Data(DataType.String, 12, "Don't go in", "入らない"),
    0x001CA854: Data(DataType.String, 16, "Drink beer", "ビールを飲む"),
    0x001CA864: Data(DataType.String, 16, "Close the fridge", "冷蔵庫を閉める"),
    0x001CA874: Data(DataType.String, 16, "Drink juice", "ジュースを飲む"),
    0x001CA938: Data(DataType.String, 12, "Return home", "家に戻る"),
    0x001CA944: Data(DataType.String, 20, "Wander aimlessly", "あてもなくさまよう"),
    0x001CA9A8: Data(DataType.String, 8, "Wake up", "起きる"),
    0x001CA9B0: Data(DataType.String, 12, "Keep sleeping", "眠り続ける"),
    0x001CAA9C: Data(DataType.String, 16, "Used %s.", "%sを使った。"),
    0x001CAC38: Data(DataType.String, 28, "Placed %s in shopping basket.", "%sを\n買い物カゴに入れた。"),
    0x001CAC54: Data(DataType.String, 8, "Pay", "支払う"),
    0x001CAC5C: Data(DataType.String, 12, "Don't pay", "支払わない"),
    0x001CAC70: Data(DataType.String, 32, "There appears to be crowding in front of the cashier.", "レジの前は混雑しているようだ。"),
    0x001CACD0: Data(DataType.String, 24, "Your inventory is full.", "持ち物がいっぱいです。"),
    0x001CAD04: Data(DataType.String, 56, "Because your inventory is full, you cannot hack at the MAGI terminal.", "アイテムが一杯のため、\nマギ端末にハッキングできません。"),
    0x001CAD48: Data(DataType.String, 24, "Incredible! Information skill +%d", "大成功！　情報技能+%d"),
    0x001CAD60: Data(DataType.String, 20, "Very nice! Information skill +%d", "成功！　情報技能+%d"),
    0x001CAD74: Data(DataType.String, 24, "Did okay. Information skill +%d", "まあまあ　情報技能+%d"),
    0x001CAD8C: Data(DataType.String, 20, "Nothing special. Information skill +%d", "普通　情報技能+%d"),
    0x001CADA0: Data(DataType.String, 24, "Didn't do well. Information skill +%d", "調子悪い　情報技能+%d"),
    0x001CADB8: Data(DataType.String, 20, "Failed. Information skill +%d", "失敗　情報技能+%d"),
    0x001CADCC: Data(DataType.String, 36, "Completely failed. Information skill didn't go up.", "大失敗　情報技能は上がらなかった"),
    0x001CAE08: Data(DataType.String, 28, "No interrupting dialogue found", "割込セリフが見つからない"),
    0x001CAE24: Data(DataType.String, 28, "No interrupting dialogue found", "割込セリフが見つからない"),
    0x001CAE40: Data(DataType.String, 28, "No interrupting dialogue found", "割込セリフが見つからない"),
    0x001CAE5C: Data(DataType.String, 28, "No interrupting dialogue found", "割込セリフが見つからない"),
    0x001CAE78: Data(DataType.String, 28, "No interrupting dialogue found", "割込セリフが見つからない"),
    0x001CAE98: Data(DataType.String, 16, "handout of %s", "%sのプリント"),
    0x001CAEA8: Data(DataType.String, 16, "handout to %s", "%sへのプリント\n"),
    0x001CAEB8: Data(DataType.String, 28, "List of handouts in your custody\n", "預かっているプリント一覧\n"),
    0x001CAF98: Data(DataType.String, 104, "Entrusted with handouts for a student who missed lessons.$nPlease supply handouts that are requested directly or by other students. ", "授業を欠席した生徒のプリントを\n任されました。$n直接、あるいは他の生徒に頼って\nプリントを渡しましょう。"),
    0x001CB0C8: Data(DataType.String, 12, "remembered", "思い出した"),
    0x001CB11C: Data(DataType.String, 28, "Impulse, Synch Skill", "インパルス　シンクロ技能"),
    0x001CB138: Data(DataType.String, 60, "Eva%s   Combat Behavior List\n\nCombat Behavior Name           A.T. Requirements\n", "ＥＶＡ%s　戦闘行動リスト\n\n戦闘行動名称　　　　　　ΑΤ条件\n"),
    0x001CB174: Data(DataType.String, 8, "--", "−−"),
    0x001CB184: Data(DataType.String, 32, "%-24s　%-6s　　%s%-7s 　%s%s\n", "%-24s　%-6s　　%s%-7s 　%s%s\n"),
    0x001CB1D0: Data(DataType.String, 12, "Rei Ayanami", "綾波レイ"),
    0x001CB1DC: Data(DataType.String, 12, "Shinji Ikari", "碇シンジ"),
    0x001CB1E8: Data(DataType.String, 12, "Asuka Soryu", "惣流アスカ"),
    0x001CB1F4: Data(DataType.String, 12, "Toji Suzuhara", "鈴原トウジ"),
    0x001CB200: Data(DataType.String, 12, "Kaworu Nagisa", "渚カヲル"),
    0x001CB234: Data(DataType.String, 72, "Eva & Pilot Data\n\nEva  Stamina  Pilot  A.T.  Impulse", "エヴァとパイロット情報\n\nエヴァ　耐久力　パイロット　　ΑΤ　インパルス"),
    0x001CB27C: Data(DataType.String, 32, "%-6s　%3D　%-10s　%3D　　%3D\n", "%-6s　%3D　%-10s　%3D　　%3D\n"),
    0x001CB29C: Data(DataType.String, 64, "Information on Deployed Weapon\n\n Name of Weapon      Range Limit  Attack Power", "配備武器情報\n\n武器名称　　　　　　　　　　　射程限界　攻撃力\n"),
    0x001CB2DC: Data(DataType.String, 20, "%-28s　%4D　%3D\n", "%-28s　%4D　%3D\n"),
    0x001CB328: Data(DataType.String, 160, "Nerv General Information\n\nTokyo-3 Operational Status　%s%\nTokyo-3 Reconstruction Budget　%s00,000,000 yen\nRepair Efficiency of Support Facilities　　　%s%\n\nEva Maintenance Budget　　　　%s00,000,000 yen\nEva Maintenance Efficiency　　　　%s%\n", "ネルフ総合情報\n\n第３新東京市稼働状態　%s％\n第３新東京市復興予算　%s億円\n支援施設修復効率　　　%s％\n\nエヴァ補修予算　　　　%s億円\nエヴァ補修効率　　　　%s％\n"),
    0x001CB3C8: Data(DataType.String, 120, "Nerv General Information\n\nMaya's Work Performance     %s\nHyuga's Work Performance     %s\nAoba's Work Performance     %s\n\nNerv Personnel Defensive Capacity  %s%\n", "ネルフ総合情報\n\nマヤ仕事性能　　　　　%s\n日向仕事性能　　　　　%s\n青葉仕事性能　　　　　%s\n\nネルフ対人防衛能力　　%s％\n"),
    0x001CB47C: Data(DataType.String, 8, "told", "話した"),
    0x001CB484: Data(DataType.String, 12, "complained", "愚痴った"),
    0x001CB4F8: Data(DataType.String, 16, "After receiving their allowance,\n", "小遣いを貰い、\n"),
    0x001CB508: Data(DataType.String, 20, "After being paid their salary,\n", "給料が振り込まれ、\n"),
    0x001CB560: Data(DataType.String, 28, "%s has %D yen total.\n", "%s所持金が%D円増えました。\n"),
    0x001CB57C: Data(DataType.String, 56, "Max impulse increased by %D.\n Max Impulse  %D→%D\n", "インパルス上限が%D増えました。\nインパルス上限　%D→%D\n"),
    0x001CB5B4: Data(DataType.String, 20, "You made %s.", "%sを作りました。"),
    0x001CB758: Data(DataType.String, 20, "Please press", "押してください。"),
    0x001CB76C: Data(DataType.String, 16, "%s the %1i button.", "%1iボタンを%s"),
    0x001CB77C: Data(DataType.String, 16, "%s the %4i button.", "%4iボタンを%s"),
    0x001CBB40: Data(DataType.String, 20, "Review opinion brief", "意見書を審査する"),
    0x001CBB54: Data(DataType.String, 20, "Study together", "一緒に勉強をする"),
    0x001CBB68: Data(DataType.String, 24, "Review lessons together", "一緒に授業の復習をする"),
    0x001CBB80: Data(DataType.String, 24, "Do combat training together", "一緒に戦闘訓練をする"),
    0x001CBB98: Data(DataType.String, 24, "Investigate confidential information together", "一緒に機密情報の調査"),
    0x001CBBB0: Data(DataType.String, 12, "Study", "勉強する"),
    0x001CBBBC: Data(DataType.String, 20, "Finish overtime work at home", "家で残業を片付ける"),
    0x001CBBD0: Data(DataType.String, 20, "Handle the disposition", "始末書を処理する"), # MACHINE_TRANSLATED
    0x001CBBE4: Data(DataType.String, 24, "Eva repair budget request", "エヴァの補修予算請求"), # MACHINE_TRANSLATED
    0x001CBBFC: Data(DataType.String, 28, "Request for 3rd New Tokyo City Reconstruction Budget", "第３新東京市復興予算請求"), # MACHINE_TRANSLATED
    0x001CBC18: Data(DataType.String, 20, "Dummy Plug Research", "ダミープラグの研究"),
    0x001CBC2C: Data(DataType.String, 20, "Operational Time Extension Research", "稼動時間の延長研究"),
    0x001CBC40: Data(DataType.String, 24, "A.T. Field Morphing Test", "ΑΤフィールド変形試験"),
    0x001CBC58: Data(DataType.String, 24, "A.T. Field Amplification Test", "ΑΤフィールド増幅試験"),
    0x001CBC70: Data(DataType.String, 20, "Operator Duties", "オペレーター業務"),
    0x001CBC84: Data(DataType.String, 12, "Commander Duties", "司令業務"),
    0x001CBC90: Data(DataType.String, 12, "Deputy Commander Duties", "副司令業務"),
    0x001CBC9C: Data(DataType.String, 24, "Make forged document or card", "偽造書類、カードを作る"),
    0x001CBCB4: Data(DataType.String, 16, "Hack", "ハッキングする"),
    0x001CBCC4: Data(DataType.String, 28, "Hack MAGI terminal", "マギ端末にハッキングする"),
    0x001CBCE0: Data(DataType.String, 24, "Information skill training(Debug)", "情報技能の訓練(Debug)"),
    0x001CBCF8: Data(DataType.String, 16, "Receive earnestly", "マジメに受ける"),
    0x001CBD08: Data(DataType.String, 12, "Do some moonlighting", "内職を行う"),
    0x001CBD14: Data(DataType.String, 20, "Concentrate on the test", "テストに集中する"),
    0x001CBD28: Data(DataType.String, 12, "Clear your mind", "無心を保つ"),
    0x001CBD34: Data(DataType.String, 24, "Direct your awareness toward the Eva", "エヴァに意識を向ける"),
    0x001CBD4C: Data(DataType.String, 16, "Approach with an open mind", "自然体で臨む"),
    0x001CBD5C: Data(DataType.String, 16, "Relax", "リラックスする"),
    0x001CBD6C: Data(DataType.String, 16, "Restless", "落ち着かない"), # MACHINE_TRANSLATED
    0x001CBD7C: Data(DataType.String, 16, "Not motivated", "やる気が出ない"), # MACHINE_TRANSLATED
    0x001CBD8C: Data(DataType.String, 16, "Staff skill training", "参謀技能訓練"), # MACHINE_TRANSLATED
    0x001CBD9C: Data(DataType.String, 16, "Development skill training", "開発技能訓練"), # MACHINE_TRANSLATED
    0x001CBDAC: Data(DataType.String, 20, "Operator Skill Training", "オペレート技能訓練"),
    0x001CBDC0: Data(DataType.String, 16, "Espionage Skill Training", "諜報技能訓練"),
    0x001CBDD0: Data(DataType.String, 16, "Clerical Skill Training", "事務技能訓練"),
    0x001CBDE0: Data(DataType.String, 16, "Information Skill Training", "情報技能訓練"),
    0x001CBDF0: Data(DataType.String, 16, "Self-Defense Skill Training", "白兵技能訓練"),
    0x001CBE00: Data(DataType.String, 12, "Make bento box", "弁当を作る"),
    0x001CBE0C: Data(DataType.String, 16, "Concentrate on training", "訓練に集中する"), # MACHINE_TRANSLATED
    0x001CBE1C: Data(DataType.String, 28, "Creating a self-destruction promotion program", "自滅促進プログラムの作成"), # MACHINE_TRANSLATED
    0x001CBE38: Data(DataType.String, 28, "Execution of self-destruction promotion program", "自滅促進プログラムの実行"), # MACHINE_TRANSLATED
    0x001CBE54: Data(DataType.String, 16, "Unison Training", "ユニゾン訓練"),
    0x001CBE64: Data(DataType.String, 16, "Peel off the seal", "シールをはがす"), # MACHINE_TRANSLATED
    0x001CBE74: Data(DataType.String, 28, "Create Kyoto University travel plan", "京都大学出張計画書を作成"), # MACHINE_TRANSLATED
    0x001CBE90: Data(DataType.String, 28, "New Opinion Brief: Eva Repair Efficiency", "意見書作成、エヴァ修理効率"),
    0x001CBEAC: Data(DataType.String, 32, "New Opinion Brief: Repair Efficiency of Support Facilities", "意見書作成、支援施設の修復効率"),
    0x001CBECC: Data(DataType.String, 32, "New Opinion Brief: Nerv Personnel Defense Facilities", "意見書作成、ネルフ対人防衛施設"),
    0x001CBEEC: Data(DataType.String, 32, "New Opinion Brief: Change Vending Machine Suppliers", "意見書作成、自販機業者の変更"),
    0x001CBF0C: Data(DataType.String, 32, "New Opinion Brief: Repair Efficiency of Support Facilities", "意見書作成、援施設の修復効率"),
    0x001CBF2C: Data(DataType.String, 20, "Create Seele I.D.", "ゼーレＩＤの作成"),
    0x001CBF40: Data(DataType.String, 20, "Create Special Forged I.D.", "特殊偽造ＩＤの作成"),
    0x001CBF54: Data(DataType.String, 28, "Create Senior Nerv Staff I.D.", "上級ネルフ職員ＩＤの作成"),
    0x001CBF70: Data(DataType.String, 28, "Create Nerv Staff I.D.", "ネルフスタッフＩＤの作成"),
    0x001CBF8C: Data(DataType.String, 24, "Forge Kyoto Business Trip Manifest", "京都出張計画書の偽造"),
    0x001CBFA4: Data(DataType.String, 28, "Forge 2nd Branch Inspection Manifest", "第２支部視察計画書の偽造"),
    0x001CBFC0: Data(DataType.String, 24, "Forge Germany Business Trip Manifest", "ドイツ出張計画書の偽造"),
    0x001CBFD8: Data(DataType.String, 24, "Forge Antarctic Inspection Manifest", "南極視察計画書の偽造"),
    0x001CBFF0: Data(DataType.String, 24, "Forge Ogasawara Business Trip Manifest", "小笠原出張計画書の偽造"),
    0x001CC008: Data(DataType.String, 8, "Constant", "定数"),
    0x001CC010: Data(DataType.String, 12, "Information Skill", "情報技能"),
    0x001CC01C: Data(DataType.String, 12, "Clerical Skill", "事務技能"),
    0x001CC028: Data(DataType.String, 12, "Staff Skill", "参謀技能"),
    0x001CC034: Data(DataType.String, 12, "Development Skill", "開発技能"),
    0x001CC040: Data(DataType.String, 12, "Operator Skill", "ＯＰ技能"),
    0x001CC04C: Data(DataType.String, 12, "Espionage Skill", "諜報技能"),
    0x001CC058: Data(DataType.String, 12, "Self-Defense Skill", "白兵技能"),
    0x001CC064: Data(DataType.String, 12, "Synchro", "シンクロ"),
    0x001CC070: Data(DataType.String, 12, "AYP performance", "ＡＹＰ性能"), # MACHINE_TRANSLATED
    0x001CC07C: Data(DataType.String, 12, "Opponent AT", "相手Ａ.Ｔ."), # MACHINE_TRANSLATED
    0x001CC088: Data(DataType.String, 8, "Restroom", "トイレ"),
    0x001CC090: Data(DataType.String, 12, "Total grades", "成績合計"), # MACHINE_TRANSLATED
    0x001CC09C: Data(DataType.String, 12, "Total favor", "好意合計"), # MACHINE_TRANSLATED
    0x001CC0A8: Data(DataType.String, 12, "Information total", "情報合計"), # MACHINE_TRANSLATED
    0x001CC0B4: Data(DataType.String, 12, "Intelligence + office work", "諜報＋事務"), # MACHINE_TRANSLATED
    0x001CC0C0: Data(DataType.String, 12, "Intelligence + information", "諜報＋情報"), # MACHINE_TRANSLATED
    0x001CC12C: Data(DataType.String, 20, "I was talking about", "に話題を振ったこと"), # MACHINE_TRANSLATED
    0x001CC140: Data(DataType.String, 16, "ignoring", "を無視したこと"),
    0x001CC150: Data(DataType.String, 16, "approaching", "に近づいたこと"),
    0x001CC160: Data(DataType.String, 24, "And an innocent reply", "に、そっけない返事を"), # MACHINE_TRANSLATED
    0x001CC178: Data(DataType.String, 12, "What you did", "したこと"), # MACHINE_TRANSLATED
    0x001CC184: Data(DataType.String, 20, "Stubborn attitude", "のふがいない態度を"), # MACHINE_TRANSLATED
    0x001CC198: Data(DataType.String, 12, "Scolded", "叱ったこと"), # MACHINE_TRANSLATED
    0x001CC1A4: Data(DataType.String, 12, "conversation with", "との会話を"),
    0x001CC1B0: Data(DataType.String, 16, "Rounded up", "切り上げたこと"), # MACHINE_TRANSLATED
    0x001CC1C0: Data(DataType.String, 20, "An uncomfortable attitude", "のつれない態度を"), # MACHINE_TRANSLATED
    0x001CC1D4: Data(DataType.String, 12, "Lamenting", "嘆いたこと"), # MACHINE_TRANSLATED
    0x001CC1E0: Data(DataType.String, 24, "Be sick of the attitude", "の態度にヘコんだこと"), # MACHINE_TRANSLATED
    0x001CC1F8: Data(DataType.String, 12, "To the attitude of", "の態度に"), # MACHINE_TRANSLATED
    0x001CC204: Data(DataType.String, 20, "What did not move", "動じなかったこと"), # MACHINE_TRANSLATED
    0x001CC218: Data(DataType.String, 16, "Being shined by", "に照れたこと"), # MACHINE_TRANSLATED
    0x001CC228: Data(DataType.String, 24, "Diversion of eyes to", "への視線を逸らしたこと"), # MACHINE_TRANSLATED
    0x001CC240: Data(DataType.String, 20, "Laughing at", "に笑いかけたこと"), # MACHINE_TRANSLATED
    0x001CC254: Data(DataType.String, 16, "Approached to", "に近寄ったこと"), # MACHINE_TRANSLATED
    0x001CC264: Data(DataType.String, 20, "Troubled alone", "一人で悩んだこと"), # MACHINE_TRANSLATED
    0x001CC278: Data(DataType.String, 16, "Sensitive information to", "に機密情報を"), # MACHINE_TRANSLATED
    0x001CC288: Data(DataType.String, 16, "What I heard", "聞き出したこと"), # MACHINE_TRANSLATED
    0x001CC298: Data(DataType.String, 16, "To the question from", "からの問いに"), # MACHINE_TRANSLATED
    0x001CC2A8: Data(DataType.String, 24, "I don't understand", "わからないと答えたこと"), # MACHINE_TRANSLATED
    0x001CC2C0: Data(DataType.String, 16, "To warn", "に警告したこと"), # MACHINE_TRANSLATED
    0x001CC2D0: Data(DataType.String, 12, "Talk with", "との話を"), # MACHINE_TRANSLATED
    0x001CC2DC: Data(DataType.String, 24, "Telling us sensitive information", "に機密情報を教えたこと"), # MACHINE_TRANSLATED
    0x001CC2F4: Data(DataType.String, 20, "Was angry with", "に怒ってみせたこと"), # MACHINE_TRANSLATED
    0x001CC308: Data(DataType.String, 20, "Away from", "から身を離したこと"), # MACHINE_TRANSLATED
    0x001CC31C: Data(DataType.String, 16, "Kissed by", "にキスしたこと"), # MACHINE_TRANSLATED
    0x001CC32C: Data(DataType.String, 20, "Hugging", "を抱きしめたこと"), # MACHINE_TRANSLATED
    0x001CC340: Data(DataType.String, 20, "Holding the hand of", "の手を握ったこと"), # MACHINE_TRANSLATED
    0x001CC354: Data(DataType.String, 20, "What I whispered", "にささやいたこと"), # MACHINE_TRANSLATED
    0x001CC368: Data(DataType.String, 24, "Hugging", "を強く抱きしめたこと"), # MACHINE_TRANSLATED
    0x001CC380: Data(DataType.String, 24, "And entwined my fingers", "と指を絡めあったこと"), # MACHINE_TRANSLATED
    0x001CC398: Data(DataType.String, 16, "An invitation from", "からの誘いを"), # MACHINE_TRANSLATED
    0x001CC3A8: Data(DataType.String, 16, "That I refused", "拒絶したこと"), # MACHINE_TRANSLATED
    0x001CC3B8: Data(DataType.String, 20, "With a dull attitude", "に、つれない態度の"), # MACHINE_TRANSLATED
    0x001CC3CC: Data(DataType.String, 20, "I heard the reason", "理由を聞いたこと"), # MACHINE_TRANSLATED
    0x001CC3E0: Data(DataType.String, 20, "And nothing", "に、何でもないと"), # MACHINE_TRANSLATED
    0x001CC3F4: Data(DataType.String, 12, "Be shy", "照れたこと"), # MACHINE_TRANSLATED
    0x001CC400: Data(DataType.String, 20, "To favor $a", "に、$aへの好意を"), # MACHINE_TRANSLATED
    0x001CC414: Data(DataType.String, 12, "What I asked", "尋ねたこと"), # MACHINE_TRANSLATED
    0x001CC420: Data(DataType.String, 24, "And why to avoid $a", "に、$aを避ける理由を"), # MACHINE_TRANSLATED
    0x001CC438: Data(DataType.String, 12, "What i heard", "聞いたこと"), # MACHINE_TRANSLATED
    0x001CC444: Data(DataType.String, 16, "To the question from", "からの質問に"), # MACHINE_TRANSLATED
    0x001CC454: Data(DataType.String, 24, "I didn't answer anything", "何も答えなかったこと"), # MACHINE_TRANSLATED
    0x001CC46C: Data(DataType.String, 24, "To say that now", "に、今はダメだと言って"), # MACHINE_TRANSLATED
    0x001CC484: Data(DataType.String, 24, "To something", "に、思わせぶりなことを"), # MACHINE_TRANSLATED
    0x001CC49C: Data(DataType.String, 12, "talking", "言ったこと"),
    0x001CC4A8: Data(DataType.String, 24, "I said that I hate", "に、嫌いだと言ったこと"), # MACHINE_TRANSLATED
    0x001CC4C0: Data(DataType.String, 24, "Said that he was happy", "に、嬉しいと言ったこと"), # MACHINE_TRANSLATED
    0x001CC4D8: Data(DataType.String, 20, "To be a liar", "に、うそつきだと"), # MACHINE_TRANSLATED
    0x001CC4EC: Data(DataType.String, 12, "I hate", "を嫌いだ"), # MACHINE_TRANSLATED
    0x001CC4F8: Data(DataType.String, 16, "saying", "と言ったこと"),
    0x001CC508: Data(DataType.String, 20, "Hugging in", "に抱きついたこと"), # MACHINE_TRANSLATED
    0x001CC51C: Data(DataType.String, 20, "Hugged from", "から抱きつかれて"), # MACHINE_TRANSLATED
    0x001CC530: Data(DataType.String, 20, "What made me happy", "喜んでみせたこと"), # MACHINE_TRANSLATED
    0x001CC544: Data(DataType.String, 16, "What I tanned", "たしなめたこと"), # MACHINE_TRANSLATED
    0x001CC554: Data(DataType.String, 20, "I was hugged by", "から抱きつかれたが"), # MACHINE_TRANSLATED
    0x001CC568: Data(DataType.String, 16, "ignoring", "無視したこと"),
    0x001CC578: Data(DataType.String, 12, "Against", "に対して、"), # MACHINE_TRANSLATED
    0x001CC584: Data(DataType.String, 20, "What I said in good mood", "上機嫌で話したこと"), # MACHINE_TRANSLATED
    0x001CC598: Data(DataType.String, 20, "Be nice to me", "に、なれなれしく"), # MACHINE_TRANSLATED
    0x001CC5AC: Data(DataType.String, 12, "Contact", "接したこと"), # MACHINE_TRANSLATED
    0x001CC5B8: Data(DataType.String, 24, "In a friendly attitude", "のなれなれしい態度に"), # MACHINE_TRANSLATED
    0x001CC5D0: Data(DataType.String, 24, "I responded quietly", "そっけなく応対したこと"), # MACHINE_TRANSLATED
    0x001CC5E8: Data(DataType.String, 24, "A friendly attitude", "のなれなれしい態度を"), # MACHINE_TRANSLATED
    0x001CC600: Data(DataType.String, 24, "Cold treatment", "冷たくあしらったこと"), # MACHINE_TRANSLATED
    0x001CC618: Data(DataType.String, 20, "Swearing", "首をかしげたこと"), # MACHINE_TRANSLATED
    0x001CC62C: Data(DataType.String, 16, "Worried about", "を心配したこと"), # MACHINE_TRANSLATED
    0x001CC63C: Data(DataType.String, 24, "I observed the situation of", "の様子を観察したこと"), # MACHINE_TRANSLATED
    0x001CC654: Data(DataType.String, 8, "To", "に、"), # MACHINE_TRANSLATED
    0x001CC65C: Data(DataType.String, 28, "What happened back to me", "我に返ってあやまったこと"), # MACHINE_TRANSLATED
    0x001CC678: Data(DataType.String, 12, "In front of", "を前にして"), # MACHINE_TRANSLATED
    0x001CC684: Data(DataType.String, 24, "I was vacant", "ぼーっとしていたこと"), # MACHINE_TRANSLATED
    0x001CC69C: Data(DataType.String, 24, "Having a crying face", "泣きそうな顔をしたこと"), # MACHINE_TRANSLATED
    0x001CC6B4: Data(DataType.String, 16, "And nothing", "に、何でもない"), # MACHINE_TRANSLATED
    0x001CC6C4: Data(DataType.String, 16, "In a dark tone", "に、暗い調子で"), # MACHINE_TRANSLATED
    0x001CC6D4: Data(DataType.String, 16, "What you talked to", "話しかけたこと"), # MACHINE_TRANSLATED
    0x001CC6E4: Data(DataType.String, 24, "I don't feel like that", "に、そんな気分じゃない"), # MACHINE_TRANSLATED
    0x001CC6FC: Data(DataType.String, 16, "Getting angry", "腹を立てたこと"), # MACHINE_TRANSLATED
    0x001CC70C: Data(DataType.String, 12, "With the attitude of", "の態度で"), # MACHINE_TRANSLATED
    0x001CC718: Data(DataType.String, 20, "Being in a good mood", "上機嫌になったこと"), # MACHINE_TRANSLATED
    0x001CC72C: Data(DataType.String, 28, "Nodding in no time", "間をあけてうなずいたこと"), # MACHINE_TRANSLATED
    0x001CC748: Data(DataType.String, 24, "Even if you look at her crying face", "の泣きそうな顔を見ても"), # MACHINE_TRANSLATED
    0x001CC760: Data(DataType.String, 20, "What I knew", "知らんぷりしたこと"), # MACHINE_TRANSLATED
    0x001CC774: Data(DataType.String, 24, "Look at the crying face", "の泣きそうな顔を見て"), # MACHINE_TRANSLATED
    0x001CC78C: Data(DataType.String, 28, "I called out to Nagusame", "なぐさめの声をかけたこと"), # MACHINE_TRANSLATED
    0x001CC7A8: Data(DataType.String, 16, "Encouragement", "励ましたこと"), # MACHINE_TRANSLATED
    0x001CC7B8: Data(DataType.String, 24, "You don't have to say anything", "に、何も言わなくていい"), # MACHINE_TRANSLATED
    0x001CC7D0: Data(DataType.String, 16, "I was silent", "黙っていたこと"), # MACHINE_TRANSLATED
    0x001CC7E0: Data(DataType.String, 24, "After all, nothing", "に、やっぱり何でもない"), # MACHINE_TRANSLATED
    0x001CC7F8: Data(DataType.String, 12, "About", "のことを、"), # MACHINE_TRANSLATED
    0x001CC804: Data(DataType.String, 24, "What I thought was a weird guy", "変な奴だと思ったこと"), # MACHINE_TRANSLATED
    0x001CC81C: Data(DataType.String, 16, "Be careful of", "に注意したこと"), # MACHINE_TRANSLATED
    0x001CC82C: Data(DataType.String, 24, "When being observed by", "に観察されているとき"), # MACHINE_TRANSLATED
    0x001CC844: Data(DataType.String, 20, "sighing", "ため息をついたこと"),
    0x001CC858: Data(DataType.String, 20, "That was released", "を突き放したこと"), # MACHINE_TRANSLATED
    0x001CC86C: Data(DataType.String, 16, "Don't worry", "に、気にするな"), # MACHINE_TRANSLATED
    0x001CC87C: Data(DataType.String, 24, "I understood the reply from", "の返事に了解したこと"), # MACHINE_TRANSLATED
    0x001CC894: Data(DataType.String, 20, "Hitting the shoulders of", "の肩を叩いたこと"), # MACHINE_TRANSLATED
    0x001CC8A8: Data(DataType.String, 24, "Asked,", "に、何かと尋ねたこと"), # MACHINE_TRANSLATED
    0x001CC8C0: Data(DataType.String, 16, "And this story", "に、こんな話は"), # MACHINE_TRANSLATED
    0x001CC8D0: Data(DataType.String, 28, "I said I was bored", "退屈そうだね、と言ったこと"), # MACHINE_TRANSLATED
    0x001CC8EC: Data(DataType.String, 8, "From", "から、"), # MACHINE_TRANSLATED
    0x001CC8F4: Data(DataType.String, 24, "Being separated", "それとなく離れたこと"), # MACHINE_TRANSLATED
    0x001CC90C: Data(DataType.String, 16, "taking a bath", "入浴したこと"),
    0x001CC91C: Data(DataType.String, 12, "Studying", "の勉強を"), # MACHINE_TRANSLATED
    0x001CC928: Data(DataType.String, 16, "What disturbed me", "邪魔したこと"), # MACHINE_TRANSLATED
    0x001CC938: Data(DataType.String, 28, "I was disturbed by my study", "に勉強の邪魔をされたので"), # MACHINE_TRANSLATED
    0x001CC954: Data(DataType.String, 20, "Complained", "文句を言ったこと"), # MACHINE_TRANSLATED
    0x001CC968: Data(DataType.String, 24, "I was disturbed by my study", "に勉強の邪魔をされたが"), # MACHINE_TRANSLATED
    0x001CC980: Data(DataType.String, 24, "ignoring and studying", "無視して勉強したこと"),
    0x001CC998: Data(DataType.String, 20, "Sitting in a chair", "椅子に座ったこと"), # MACHINE_TRANSLATED
    0x001CC9AC: Data(DataType.String, 24, "Was complained to,", "に文句を言われたので、"), # MACHINE_TRANSLATED
    0x001CC9C4: Data(DataType.String, 20, "The other person", "の相手をしたこと"), # MACHINE_TRANSLATED
    0x001CC9D8: Data(DataType.String, 20, "Can't do", "の相手は出来ない"), # MACHINE_TRANSLATED
    0x001CC9EC: Data(DataType.String, 16, "And refused", "と拒んだこと"), # MACHINE_TRANSLATED
    0x001CC9FC: Data(DataType.String, 16, "To eat", "にかまうのを"), # MACHINE_TRANSLATED
    0x001CCA0C: Data(DataType.String, 16, "Giving up", "あきらめたこと"), # MACHINE_TRANSLATED
    0x001CCA1C: Data(DataType.String, 20, "Invited to fishing", "を釣りに誘ったこと"), # MACHINE_TRANSLATED
    0x001CCA30: Data(DataType.String, 16, "(Memory conversation)", "（記憶会話）"), # MACHINE_TRANSLATED
    0x001CCA40: Data(DataType.String, 12, "together with", "と一緒に"),
    0x001CCA4C: Data(DataType.String, 20, "watching T.V.", "テレビを観たこと"),
    0x001CCA60: Data(DataType.String, 28, "And when watching TV", "とテレビを観ているときに"), # MACHINE_TRANSLATED
    0x001CCA7C: Data(DataType.String, 24, "changing the channel", "チャンネルを変えたこと"),
    0x001CCA94: Data(DataType.String, 24, "What the program complained about", "番組の文句を言ったこと"), # MACHINE_TRANSLATED
    0x001CCAAC: Data(DataType.String, 20, "To change the channel", "のチャンネル変更に"), # MACHINE_TRANSLATED
    0x001CCAC0: Data(DataType.String, 12, "Regardless of", "にかまわず"), # MACHINE_TRANSLATED
    0x001CCACC: Data(DataType.String, 24, "I watched TV silently", "黙ってテレビを観たこと"), # MACHINE_TRANSLATED
    0x001CCAE4: Data(DataType.String, 24, "I was interested in the story", "の話に興味を持ったこと"), # MACHINE_TRANSLATED
    0x001CCAFC: Data(DataType.String, 20, "Chatting with", "と雑談をしたこと"), # MACHINE_TRANSLATED
    0x001CCB10: Data(DataType.String, 12, "(Delete)", "（削除）"), # MACHINE_TRANSLATED
    0x001CCB1C: Data(DataType.String, 20, "The school grades", "に、学校の成績を"), # MACHINE_TRANSLATED
    0x001CCB30: Data(DataType.String, 20, "And the school grade", "に、学校の成績は"), # MACHINE_TRANSLATED
    0x001CCB44: Data(DataType.String, 28, "That it is pretty good", "かなり良い、と答えたこと"), # MACHINE_TRANSLATED
    0x001CCB60: Data(DataType.String, 28, "That's ok", "まあまあだ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CCB7C: Data(DataType.String, 24, "And the school grades are bad", "に、学校の成績は悪い"), # MACHINE_TRANSLATED
    0x001CCB94: Data(DataType.String, 16, "I answered", "と答えたこと"), # MACHINE_TRANSLATED
    0x001CCBA4: Data(DataType.String, 24, "And the school record is the worst", "に、学校の成績は最悪だ"), # MACHINE_TRANSLATED
    0x001CCBBC: Data(DataType.String, 12, "Against", "に対して"), # MACHINE_TRANSLATED
    0x001CCBC8: Data(DataType.String, 20, "What was fooled", "ふてくされたこと"), # MACHINE_TRANSLATED
    0x001CCBDC: Data(DataType.String, 24, "I laughed at my sleep", "の寝言に苦笑いしたこと"), # MACHINE_TRANSLATED
    0x001CCBF4: Data(DataType.String, 16, "For the time being", "を、とりあえず"), # MACHINE_TRANSLATED
    0x001CCC04: Data(DataType.String, 16, "Hugging", "抱きしめたこと"), # MACHINE_TRANSLATED
    0x001CCC14: Data(DataType.String, 16, "For the time being,", "に、とりあえず"), # MACHINE_TRANSLATED
    0x001CCC24: Data(DataType.String, 16, "I hugged", "抱き返したこと"), # MACHINE_TRANSLATED
    0x001CCC34: Data(DataType.String, 20, "From the beginning", "から、とりあえず"), # MACHINE_TRANSLATED
    0x001CCC48: Data(DataType.String, 12, "Separated", "離れたこと"), # MACHINE_TRANSLATED
    0x001CCC54: Data(DataType.String, 24, "And the self-destruction promotion program", "と、自滅促進プログラム"), # MACHINE_TRANSLATED
    0x001CCC6C: Data(DataType.String, 24, "Talked about", "について、話をしたこと"), # MACHINE_TRANSLATED
    0x001CCC84: Data(DataType.String, 28, "I got some pocket money from", "からお小遣いを貰ったので"), # MACHINE_TRANSLATED
    0x001CCCA0: Data(DataType.String, 16, "thanking", "礼を言ったこと"),
    0x001CCCB0: Data(DataType.String, 24, "Want some pocket money", "に、お小遣いが欲しい"), # MACHINE_TRANSLATED
    0x001CCCC8: Data(DataType.String, 16, "To spend money", "に、お小遣いを"), # MACHINE_TRANSLATED
    0x001CCCD8: Data(DataType.String, 12, "Passed", "渡したこと"), # MACHINE_TRANSLATED
    0x001CCCE4: Data(DataType.String, 24, "What could not be raised", "上げられなかったこと"), # MACHINE_TRANSLATED
    0x001CCCFC: Data(DataType.String, 24, "I can't get my pocket money", "からお小遣いを貰えず"), # MACHINE_TRANSLATED
    0x001CCD14: Data(DataType.String, 24, "What complained about $b", "$bに文句を言ったこと"), # MACHINE_TRANSLATED
    0x001CCD2C: Data(DataType.String, 20, "And Ritsuko's ΑΤ", "と、リツコのΑΤを"), # MACHINE_TRANSLATED
    0x001CCD40: Data(DataType.String, 16, "Worried", "心配したこと"), # MACHINE_TRANSLATED
    0x001CCD50: Data(DataType.String, 24, "If Ritsuko is fine", "に、リツコなら大丈夫"), # MACHINE_TRANSLATED
    0x001CCD68: Data(DataType.String, 24, "And relieved me", "と伝え、安心させたこと"), # MACHINE_TRANSLATED
    0x001CCD80: Data(DataType.String, 24, "Awkward against", "に対して気まずくなり、"), # MACHINE_TRANSLATED
    0x001CCD98: Data(DataType.String, 20, "I have shut up", "黙ってしまったこと"), # MACHINE_TRANSLATED
    0x001CCDAC: Data(DataType.String, 16, "To collect information", "に、情報収集を"), # MACHINE_TRANSLATED
    0x001CCDBC: Data(DataType.String, 12, "What I asked for", "頼んだこと"), # MACHINE_TRANSLATED
    0x001CCDC8: Data(DataType.String, 24, "To collect information from", "からの情報収集依頼に"), # MACHINE_TRANSLATED
    0x001CCDE0: Data(DataType.String, 16, "I understand", "了解したこと"), # MACHINE_TRANSLATED
    0x001CCDF0: Data(DataType.String, 20, "Information collection cooperation", "の情報収集協力に"), # MACHINE_TRANSLATED
    0x001CCE04: Data(DataType.String, 24, "Request to collect information from", "からの情報収集依頼を"), # MACHINE_TRANSLATED
    0x001CCE1C: Data(DataType.String, 12, "What I refused", "断ったこと"), # MACHINE_TRANSLATED
    0x001CCE28: Data(DataType.String, 20, "What I heard", "に耳打ちしたこと"), # MACHINE_TRANSLATED
    0x001CCE3C: Data(DataType.String, 24, "That I had a relationship with", "に相づちをうったこと"), # MACHINE_TRANSLATED
    0x001CCE54: Data(DataType.String, 16, "Don't worry", "に、心配するな"), # MACHINE_TRANSLATED
    0x001CCE64: Data(DataType.String, 20, "At a strategy meeting with", "との作戦会議で、"), # MACHINE_TRANSLATED
    0x001CCE78: Data(DataType.String, 28, "Confirmed the presence of questions", "質問の有無を確認したこと"), # MACHINE_TRANSLATED
    0x001CCE94: Data(DataType.String, 24, "To the content of the strategy presented by", "の提示した作戦内容に"), # MACHINE_TRANSLATED
    0x001CCEAC: Data(DataType.String, 24, "What I said", "対して、意見したこと"), # MACHINE_TRANSLATED
    0x001CCEC4: Data(DataType.String, 16, "To the content of the strategy", "の作戦内容に"), # MACHINE_TRANSLATED
    0x001CCED4: Data(DataType.String, 12, "That I obeyed", "従ったこと"), # MACHINE_TRANSLATED
    0x001CCEE0: Data(DataType.String, 28, "Dissatisfied with the operation content of", "の作戦内容に対する不満に"), # MACHINE_TRANSLATED
    0x001CCEFC: Data(DataType.String, 16, "What I argued", "異論したこと"), # MACHINE_TRANSLATED
    0x001CCF0C: Data(DataType.String, 16, "In a strategy meeting with", "との作戦会議で"), # MACHINE_TRANSLATED
    0x001CCF1C: Data(DataType.String, 32, "Deciding on a strategy and challenging the apostles", "作戦を決定し、使徒に挑んだこと"), # MACHINE_TRANSLATED
    0x001CCF3C: Data(DataType.String, 16, "Against the objection of", "の異論に対して"), # MACHINE_TRANSLATED
    0x001CCF4C: Data(DataType.String, 16, "What I said back", "言い返したこと"), # MACHINE_TRANSLATED
    0x001CCF5C: Data(DataType.String, 20, "Responding reluctantly", "しぶしぶ従ったこと"), # MACHINE_TRANSLATED
    0x001CCF70: Data(DataType.String, 20, "To share a meal", "に、食事の相席を"), # MACHINE_TRANSLATED
    0x001CCF84: Data(DataType.String, 12, "What I asked for", "求めたこと"), # MACHINE_TRANSLATED
    0x001CCF90: Data(DataType.String, 24, "Requested and approved", "求められ、了承したこと"), # MACHINE_TRANSLATED
    0x001CCFA8: Data(DataType.String, 16, "Sitting next to", "の横に座って"), # MACHINE_TRANSLATED
    0x001CCFB8: Data(DataType.String, 16, "Having a meal", "食事をしたこと"), # MACHINE_TRANSLATED
    0x001CCFC8: Data(DataType.String, 28, "I was asked but refused", "求められたが、断ったこと"), # MACHINE_TRANSLATED
    0x001CCFE4: Data(DataType.String, 24, "What I refused and dented", "断られて、ヘコんだこと"), # MACHINE_TRANSLATED
    0x001CCFFC: Data(DataType.String, 28, "To the Eva pilot", "に、エヴァのパイロットを"), # MACHINE_TRANSLATED
    0x001CD018: Data(DataType.String, 24, "I said to quit", "辞める、と言ったこと"), # MACHINE_TRANSLATED
    0x001CD030: Data(DataType.String, 24, "To leave the pilot", "に、パイロットを辞める"), # MACHINE_TRANSLATED
    0x001CD048: Data(DataType.String, 28, "Was accepted and accepted", "と言われ、受け入れたこと"), # MACHINE_TRANSLATED
    0x001CD064: Data(DataType.String, 24, "Asking for determination", "決意を問いただしたこと"), # MACHINE_TRANSLATED
    0x001CD07C: Data(DataType.String, 32, "Saying that my determination will not change", "決意は変わらないと言ったこと"), # MACHINE_TRANSLATED
    0x001CD09C: Data(DataType.String, 24, "To the resignation of the pilot", "に、パイロット辞任は"), # MACHINE_TRANSLATED
    0x001CD0B4: Data(DataType.String, 20, "What I said was a lie", "ウソだと言ったこと"), # MACHINE_TRANSLATED
    0x001CD0C8: Data(DataType.String, 28, "I was angry when I was told to be a lie", "ウソだと言われ、怒ったこと"), # MACHINE_TRANSLATED
    0x001CD0E4: Data(DataType.String, 16, "To complain to", "に愚痴ったこと"), # MACHINE_TRANSLATED
    0x001CD0F4: Data(DataType.String, 12, "The complaints of", "の愚痴を"), # MACHINE_TRANSLATED
    0x001CD100: Data(DataType.String, 20, "What I heard silently", "黙って聞いたこと"), # MACHINE_TRANSLATED
    0x001CD114: Data(DataType.String, 24, "Agreeing to the complaints of", "の愚痴に同意したこと"), # MACHINE_TRANSLATED
    0x001CD12C: Data(DataType.String, 16, "Against the complaints of", "の愚痴に対して"), # MACHINE_TRANSLATED
    0x001CD13C: Data(DataType.String, 20, "Wondering", "疑問に思ったこと"), # MACHINE_TRANSLATED
    0x001CD150: Data(DataType.String, 24, "And continued to complain", "に、愚痴り続けたこと"), # MACHINE_TRANSLATED
    0x001CD168: Data(DataType.String, 24, "Touching the silence of", "の黙り込んだ様子に触れ"), # MACHINE_TRANSLATED
    0x001CD180: Data(DataType.String, 16, "$a also shut up", "$aも黙ったこと"), # MACHINE_TRANSLATED
    0x001CD190: Data(DataType.String, 20, "Be amazed at how he complains", "の愚痴る様子に呆れ"), # MACHINE_TRANSLATED
    0x001CD1A4: Data(DataType.String, 16, "That I pushed", "突き放したこと"), # MACHINE_TRANSLATED
    0x001CD1B4: Data(DataType.String, 16, "The following complaints", "の続く愚痴を"), # MACHINE_TRANSLATED
    0x001CD1C4: Data(DataType.String, 20, "Do you want to know the truth", "に真実を知りたいか"), # MACHINE_TRANSLATED
    0x001CD1D8: Data(DataType.String, 32, "I answered yes", "と聞かれ、はい、と答えたこと"), # MACHINE_TRANSLATED
    0x001CD1F8: Data(DataType.String, 32, "Asked, no", "と聞かれ、いいえ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CD218: Data(DataType.String, 28, "Do you really want to know the truth", "に本当に真実を知りたいか"), # MACHINE_TRANSLATED
    0x001CD234: Data(DataType.String, 20, "Asked further", "と、更に尋ねたこと"), # MACHINE_TRANSLATED
    0x001CD248: Data(DataType.String, 20, "After all, the truth is", "に、やっぱり真実は"), # MACHINE_TRANSLATED
    0x001CD25C: Data(DataType.String, 32, "That you don't need to know", "知らなくていい、と答えたこと"), # MACHINE_TRANSLATED
    0x001CD27C: Data(DataType.String, 16, "By all means", "に、どうしても"), # MACHINE_TRANSLATED
    0x001CD28C: Data(DataType.String, 32, "I want to know the truth", "真実を知りたい、と答えたこと"), # MACHINE_TRANSLATED
    0x001CD2AC: Data(DataType.String, 28, "To Central Dogma", "に、セントラルドグマへの"), # MACHINE_TRANSLATED
    0x001CD2C8: Data(DataType.String, 24, "Teaching how to infiltrate", "潜入方法を教えたこと"), # MACHINE_TRANSLATED
    0x001CD2E0: Data(DataType.String, 16, "an opinion brief from", "からの意見書を"),
    0x001CD2F0: Data(DataType.String, 16, "Received", "受け取ったこと"), # MACHINE_TRANSLATED
    0x001CD300: Data(DataType.String, 12, "opinion brief", "の意見書を"),
    0x001CD30C: Data(DataType.String, 16, "Tossed away", "破り捨てたこと"), # MACHINE_TRANSLATED
    0x001CD31C: Data(DataType.String, 16, "What I refused", "拒否したこと"), # MACHINE_TRANSLATED
    0x001CD32C: Data(DataType.String, 24, "giving an opinion brief to", "に、意見書を渡したこと"),
    0x001CD344: Data(DataType.String, 16, "Accept your opinion", "に意見書受理を"), # MACHINE_TRANSLATED
    0x001CD354: Data(DataType.String, 28, "Rejected and eaten down", "拒否され、食い下がったこと"), # MACHINE_TRANSLATED
    0x001CD370: Data(DataType.String, 24, "I have no choice but to accept", "仕方なく受理したこと"), # MACHINE_TRANSLATED
    0x001CD388: Data(DataType.String, 16, "Strongly refused", "強く拒んだこと"), # MACHINE_TRANSLATED
    0x001CD398: Data(DataType.String, 16, "Apologize to", "に謝ったこと"), # MACHINE_TRANSLATED
    0x001CD3A8: Data(DataType.String, 20, "Reverse", "に逆ギレしたこと"), # MACHINE_TRANSLATED
    0x001CD3BC: Data(DataType.String, 12, "Scolded by", "に叱られ"), # MACHINE_TRANSLATED
    0x001CD3C8: Data(DataType.String, 24, "examining an opinion brief", "意見書を審査したこと"),
    0x001CD3E0: Data(DataType.String, 16, "Feeling annoyed", "をウザく感じて"), # MACHINE_TRANSLATED
    0x001CD3F0: Data(DataType.String, 16, "being ignored by", "に無視されて"),
    0x001CD400: Data(DataType.String, 16, "Dented", "ヘコんだこと"), # MACHINE_TRANSLATED
    0x001CD410: Data(DataType.String, 20, "Is it at work", "に、仕事中なのか"), # MACHINE_TRANSLATED
    0x001CD424: Data(DataType.String, 16, "When you are at work", "に、仕事中だと"), # MACHINE_TRANSLATED
    0x001CD434: Data(DataType.String, 12, "What I answered", "答えたこと"), # MACHINE_TRANSLATED
    0x001CD440: Data(DataType.String, 20, "Because I'm at work", "に、仕事中だから"), # MACHINE_TRANSLATED
    0x001CD454: Data(DataType.String, 24, "What I said was an obstacle", "邪魔だ、と言ったこと"), # MACHINE_TRANSLATED
    0x001CD46C: Data(DataType.String, 24, "Let's study together", "に、一緒に勉強しよう"), # MACHINE_TRANSLATED
    0x001CD484: Data(DataType.String, 20, "I said that", "と持ちかけたこと"), # MACHINE_TRANSLATED
    0x001CD498: Data(DataType.String, 24, "What I studied with", "と一緒に勉強したこと"), # MACHINE_TRANSLATED
    0x001CD4B0: Data(DataType.String, 20, "An invitation to study from", "からの勉強の誘いを"), # MACHINE_TRANSLATED
    0x001CD4C4: Data(DataType.String, 24, "Let's review the lesson", "に、授業の復習をしよう"), # MACHINE_TRANSLATED
    0x001CD4DC: Data(DataType.String, 12, "together,", "と一緒に、"),
    0x001CD4E8: Data(DataType.String, 24, "reviewing class work", "授業の復習をしたこと"),
    0x001CD500: Data(DataType.String, 28, "Invitation to review the lesson", "からの授業の復習の誘いを"), # MACHINE_TRANSLATED
    0x001CD51C: Data(DataType.String, 24, "Together, fight training together", "に、一緒に戦闘訓練を"), # MACHINE_TRANSLATED
    0x001CD534: Data(DataType.String, 28, "I tried to try", "しよう、と持ちかけたこと"), # MACHINE_TRANSLATED
    0x001CD550: Data(DataType.String, 20, "doing combat training", "戦闘訓練をしたこと"),
    0x001CD564: Data(DataType.String, 24, "an invitation to do combat training with", "からの戦闘訓練の誘いを"),
    0x001CD57C: Data(DataType.String, 20, "To cooperate in the survey", "に、調査の協力を"), # MACHINE_TRANSLATED
    0x001CD590: Data(DataType.String, 16, "What you asked for", "お願いしたこと"), # MACHINE_TRANSLATED
    0x001CD5A0: Data(DataType.String, 24, "Request for survey cooperation from", "からの調査協力の依頼を"), # MACHINE_TRANSLATED
    0x001CD5B8: Data(DataType.String, 16, "Consent", "承諾したこと"), # MACHINE_TRANSLATED
    0x001CD5C8: Data(DataType.String, 16, "What was offered", "をおだてたこと"), # MACHINE_TRANSLATED
    0x001CD5D8: Data(DataType.String, 16, "Struck by", "におだてられて"), # MACHINE_TRANSLATED
    0x001CD5E8: Data(DataType.String, 24, "I feel good", "良い気分になったこと"), # MACHINE_TRANSLATED
    0x001CD600: Data(DataType.String, 20, "I was invited to", "におだてられたが、"), # MACHINE_TRANSLATED
    0x001CD614: Data(DataType.String, 24, "I felt confused", "いぶかしく感じたこと"), # MACHINE_TRANSLATED
    0x001CD62C: Data(DataType.String, 12, "Sleeping", "の寝姿を"), # MACHINE_TRANSLATED
    0x001CD638: Data(DataType.String, 16, "What I looked into", "覗き込んだこと"), # MACHINE_TRANSLATED
    0x001CD648: Data(DataType.String, 28, "Disputed, but forced", "異論が出たが、強行したこと"), # MACHINE_TRANSLATED
    0x001CD664: Data(DataType.String, 32, "going to the convenience store's bathroom", "コンビニのトイレに行ったこと"),
    0x001CD684: Data(DataType.String, 12, "The opponent of", "の相手を"), # MACHINE_TRANSLATED
    0x001CD690: Data(DataType.String, 20, "What I did text", "テキトーにしたこと"), # MACHINE_TRANSLATED
    0x001CD6A4: Data(DataType.String, 24, "Eight hits on the wall", "壁に八つ当たりしたこと"), # MACHINE_TRANSLATED
    0x001CD6BC: Data(DataType.String, 24, "Was bad for my meal", "の食事にあやかったこと"), # MACHINE_TRANSLATED
    0x001CD6D4: Data(DataType.String, 20, "being absorbed in thought", "考え事をしたこと"),
    0x001CD6E8: Data(DataType.String, 12, "sleeping", "寝たこと"),
    0x001CD6F4: Data(DataType.String, 20, "taking a bath", "お風呂に入ったこと"),
    0x001CD708: Data(DataType.String, 16, "studying", "勉強したこと"),
    0x001CD718: Data(DataType.String, 16, "Leaving home", "家出したこと"), # MACHINE_TRANSLATED
    0x001CD728: Data(DataType.String, 28, "being mindful of others' circumstances", "他人の様子を心に留めたこと"),
    0x001CD744: Data(DataType.String, 24, "Showed the item to", "にアイテムを見せたこと"), # MACHINE_TRANSLATED
    0x001CD75C: Data(DataType.String, 24, "Show me the item", "にアイテムを見せられて"), # MACHINE_TRANSLATED
    0x001CD774: Data(DataType.String, 16, "Confused", "困惑したこと"), # MACHINE_TRANSLATED
    0x001CD784: Data(DataType.String, 20, "The item shown to", "に見せたアイテムを"), # MACHINE_TRANSLATED
    0x001CD798: Data(DataType.String, 28, "What I said to present", "プレゼントすると言ったこと"), # MACHINE_TRANSLATED
    0x001CD7B4: Data(DataType.String, 20, "an item shown to", "に見せたアイテムは"),
    0x001CD7C8: Data(DataType.String, 28, "What I said I just showed you", "見せただけだと言ったこと"), # MACHINE_TRANSLATED
    0x001CD7E4: Data(DataType.String, 20, "a present from", "からのプレゼントを"),
    0x001CD7F8: Data(DataType.String, 24, "joyously receiving", "喜んで受け取ったこと"),
    0x001CD810: Data(DataType.String, 24, "rejecting for lack of want", "いらないと断ったこと"),
    0x001CD828: Data(DataType.String, 28, "I want to give you a present", "にプレゼントを渡したくて"), # MACHINE_TRANSLATED
    0x001CD844: Data(DataType.String, 20, "That I was eating down", "食い下がったこと"), # MACHINE_TRANSLATED
    0x001CD858: Data(DataType.String, 24, "Reluctantly received", "しぶしぶ受け取ったこと"), # MACHINE_TRANSLATED
    0x001CD870: Data(DataType.String, 28, "Refused the present to", "へのプレゼントを断られて"), # MACHINE_TRANSLATED
    0x001CD88C: Data(DataType.String, 28, "I just showed you the item", "に、アイテムを見せただけ"), # MACHINE_TRANSLATED
    0x001CD8A8: Data(DataType.String, 32, "It was said that it was calm", "と言われたが、平然としたこと"), # MACHINE_TRANSLATED
    0x001CD8C8: Data(DataType.String, 24, "that it's really a present", "に、本当はプレゼントだ"),
    0x001CD8E0: Data(DataType.String, 20, "To the calm attitude of", "の平然とした態度に"), # MACHINE_TRANSLATED
    0x001CD8F4: Data(DataType.String, 20, "Missing time", "拍子抜けしたこと"), # MACHINE_TRANSLATED
    0x001CD908: Data(DataType.String, 28, "What I received while amazed", "呆れながら受け取ったこと"), # MACHINE_TRANSLATED
    0x001CD924: Data(DataType.String, 20, "What did you come to", "に、何しに来たのか"), # MACHINE_TRANSLATED
    0x001CD938: Data(DataType.String, 20, "Was hospitalized,", "は入院中だったが、"), # MACHINE_TRANSLATED
    0x001CD94C: Data(DataType.String, 20, "Requesting a sortie", "出撃要請をしたこと"), # MACHINE_TRANSLATED
    0x001CD960: Data(DataType.String, 24, "Was hospitalized, so", "は入院中だったので、"), # MACHINE_TRANSLATED
    0x001CD978: Data(DataType.String, 24, "What I didn't call", "呼び出さなかったこと"), # MACHINE_TRANSLATED
    0x001CD990: Data(DataType.String, 24, "I want you to sort out", "に、出撃させてほしい"), # MACHINE_TRANSLATED
    0x001CD9A8: Data(DataType.String, 16, "I asked", "と頼んだこと"), # MACHINE_TRANSLATED
    0x001CD9B8: Data(DataType.String, 20, "To be useful", "に、役にたつから"), # MACHINE_TRANSLATED
    0x001CD9CC: Data(DataType.String, 28, "What I told you to sortie", "出撃させろ、と言ったこと"), # MACHINE_TRANSLATED
    0x001CD9E8: Data(DataType.String, 28, "You can do as much as support", "に、援護くらいなら出来る"), # MACHINE_TRANSLATED
    0x001CDA04: Data(DataType.String, 24, "Allowed to sortie", "の出撃を許可したこと"), # MACHINE_TRANSLATED
    0x001CDA1C: Data(DataType.String, 20, "To the sortie request from", "からの出撃要請に"), # MACHINE_TRANSLATED
    0x001CDA30: Data(DataType.String, 20, "Request for a sortie from", "からの出撃要請を"), # MACHINE_TRANSLATED
    0x001CDA44: Data(DataType.String, 12, "What I refused", "拒んだこと"), # MACHINE_TRANSLATED
    0x001CDA50: Data(DataType.String, 24, "Reported to be discharged", "に、退院を報告したこと"), # MACHINE_TRANSLATED
    0x001CDA68: Data(DataType.String, 24, "Receiving a discharge report from", "からの退院報告を受けて"), # MACHINE_TRANSLATED
    0x001CDA80: Data(DataType.String, 20, "worrying about $b", "$bを気遣ったこと"),
    0x001CDA94: Data(DataType.String, 16, "To the current situation", "に、今の状況を"), # MACHINE_TRANSLATED
    0x001CDAA4: Data(DataType.String, 24, "To be caring for", "の気遣いに、大丈夫だと"), # MACHINE_TRANSLATED
    0x001CDABC: Data(DataType.String, 20, "I don't have $a", "に、$aが居なくて"), # MACHINE_TRANSLATED
    0x001CDAD0: Data(DataType.String, 24, "Asked if it was hard", "大変だったか尋ねたこと"), # MACHINE_TRANSLATED
    0x001CDAE8: Data(DataType.String, 16, "And the current situation is", "に、今の状況は"), # MACHINE_TRANSLATED
    0x001CDAF8: Data(DataType.String, 32, "I said that it was not so good", "あまり良くない、と答えたこと"), # MACHINE_TRANSLATED
    0x001CDB18: Data(DataType.String, 20, "What is the current situation", "に、今の状況なんて"), # MACHINE_TRANSLATED
    0x001CDB2C: Data(DataType.String, 28, "Don't worry", "気にするな、と言ったこと"), # MACHINE_TRANSLATED
    0x001CDB48: Data(DataType.String, 20, "And smiled", "に、微笑んだこと"), # MACHINE_TRANSLATED
    0x001CDB5C: Data(DataType.String, 16, "Be careful", "に、気をつけて"), # MACHINE_TRANSLATED
    0x001CDB6C: Data(DataType.String, 28, "It wasn't particularly difficult", "に、別に大変じゃなかった"), # MACHINE_TRANSLATED
    0x001CDB88: Data(DataType.String, 24, "It was hard as it was", "に、それなりに辛かった"), # MACHINE_TRANSLATED
    0x001CDBA0: Data(DataType.String, 20, "Surprised by the words", "の言葉に驚いたこと"), # MACHINE_TRANSLATED
    0x001CDBB4: Data(DataType.String, 24, "Stunned by the words", "の言葉に愕然としたこと"), # MACHINE_TRANSLATED
    0x001CDBCC: Data(DataType.String, 16, "And the current situation", "と現状について"), # MACHINE_TRANSLATED
    0x001CDBDC: Data(DataType.String, 12, "talking", "話したこと"),
    0x001CDBE8: Data(DataType.String, 28, "To talk about the current situation", "からの現状についての話に"), # MACHINE_TRANSLATED
    0x001CDC04: Data(DataType.String, 24, "What I silently nodded", "黙ってうなずいたこと"), # MACHINE_TRANSLATED
    0x001CDC1C: Data(DataType.String, 24, "To talk about the current situation of", "の現状についての話に、"), # MACHINE_TRANSLATED
    0x001CDC34: Data(DataType.String, 24, "I answered that I have no worries", "心配は無いと答えたこと"), # MACHINE_TRANSLATED
    0x001CDC4C: Data(DataType.String, 28, "About the current situation from", "からの現状についての話で"), # MACHINE_TRANSLATED
    0x001CDC68: Data(DataType.String, 20, "I feel awkward", "気まずくなったこと"), # MACHINE_TRANSLATED
    0x001CDC7C: Data(DataType.String, 12, "In a conversation with", "との会話で"), # MACHINE_TRANSLATED
    0x001CDC88: Data(DataType.String, 20, "Having shared", "相づちをうったこと"), # MACHINE_TRANSLATED
    0x001CDC9C: Data(DataType.String, 20, "What to eat", "に、何を食べるのか"), # MACHINE_TRANSLATED
    0x001CDCB0: Data(DataType.String, 24, "To eat", "に、食べるメニューを"), # MACHINE_TRANSLATED
    0x001CDCC8: Data(DataType.String, 12, "telling", "伝えたこと"),
    0x001CDCD4: Data(DataType.String, 28, "Asked me what to eat", "に何を食べるか聞かれたが"), # MACHINE_TRANSLATED
    0x001CDCF0: Data(DataType.String, 24, "Asked me what to eat", "に何を食べるか聞かれて"), # MACHINE_TRANSLATED
    0x001CDD08: Data(DataType.String, 28, "I was wondering", "迷っている、と答えたこと"), # MACHINE_TRANSLATED
    0x001CDD24: Data(DataType.String, 20, "The menu decided by", "の決めたメニューは"), # MACHINE_TRANSLATED
    0x001CDD38: Data(DataType.String, 24, "I asked if it was delicious", "美味しいのか尋ねたこと"), # MACHINE_TRANSLATED
    0x001CDD50: Data(DataType.String, 24, "The menu I told", "に、伝えたメニューは"), # MACHINE_TRANSLATED
    0x001CDD68: Data(DataType.String, 32, "It was said that it was delicious", "なかなか美味しい、と答えたこと"), # MACHINE_TRANSLATED
    0x001CDD88: Data(DataType.String, 32, "I replied that I would not recommend", "オススメはしない、と答えたこと"), # MACHINE_TRANSLATED
    0x001CDDA8: Data(DataType.String, 24, "casually greeting", "に、軽く挨拶したこと"),
    0x001CDDC0: Data(DataType.String, 16, "Greeting from", "からの挨拶に"), # MACHINE_TRANSLATED
    0x001CDDD0: Data(DataType.String, 16, "Reply", "返事をしたこと"), # MACHINE_TRANSLATED
    0x001CDDE0: Data(DataType.String, 24, "I gave my pocket money", "に、小遣いを渡したこと"), # MACHINE_TRANSLATED
    0x001CDDF8: Data(DataType.String, 28, "Selecting a product at a convenience store", "コンビニで商品を選んだこと"), # MACHINE_TRANSLATED
    0x001CDE14: Data(DataType.String, 28, "Shopping at a convenience store", "コンビニで買い物をしたこと"), # MACHINE_TRANSLATED
    0x001CDE30: Data(DataType.String, 28, "Worked overtime at home", "自宅で残務処理をしたこと"), # MACHINE_TRANSLATED
    0x001CDE4C: Data(DataType.String, 24, "Processing the disposition book", "始末書の処理をしたこと"), # MACHINE_TRANSLATED
    0x001CDE64: Data(DataType.String, 24, "the Eva maintenance budget", "エヴァの補修予算請求を"),
    0x001CDE7C: Data(DataType.String, 28, "Request for repair budget for support facility", "支援施設の修復予算請求を"), # MACHINE_TRANSLATED
    0x001CDE98: Data(DataType.String, 24, "dummy plug research", "ダミープラグの研究を"),
    0x001CDEB0: Data(DataType.String, 24, "Eva operational time extension", "エヴァの稼動時間延長の"),
    0x001CDEC8: Data(DataType.String, 16, "researching", "研究をしたこと"),
    0x001CDED8: Data(DataType.String, 28, "the A.T. Field morphing test", "ΑΤフィールド変形試験を"),
    0x001CDEF4: Data(DataType.String, 12, "going", "行ったこと"),
    0x001CDF00: Data(DataType.String, 28, "ΑΤ field amplification test", "ΑΤフィールド増幅試験を"), # MACHINE_TRANSLATED
    0x001CDF1C: Data(DataType.String, 20, "Operator work", "オペレーター業務を"), # MACHINE_TRANSLATED
    0x001CDF30: Data(DataType.String, 24, "Performed command operations", "司令業務を行ったこと"), # MACHINE_TRANSLATED
    0x001CDF48: Data(DataType.String, 24, "carrying out deputy commander duties", "副司令業務を行ったこと"),
    0x001CDF60: Data(DataType.String, 20, "What I was bitten by", "にかまってみたこと"), # MACHINE_TRANSLATED
    0x001CDF74: Data(DataType.String, 16, "Be bitten by", "にかまわれて"), # MACHINE_TRANSLATED
    0x001CDF84: Data(DataType.String, 20, "Wondering", "不思議に思ったこと"), # MACHINE_TRANSLATED
    0x001CDF98: Data(DataType.String, 24, "ignoring and disengaging", "を無視して離れたこと"),
    0x001CDFB0: Data(DataType.String, 20, "Stroking the head of", "の頭をなでたこと"), # MACHINE_TRANSLATED
    0x001CDFC4: Data(DataType.String, 20, "Was ironic to", "に皮肉を言ったこと"), # MACHINE_TRANSLATED
    0x001CDFD8: Data(DataType.String, 16, "Separated by", "に離れられて、"), # MACHINE_TRANSLATED
    0x001CDFE8: Data(DataType.String, 24, "A little lonely", "ちょっと寂しかったこと"), # MACHINE_TRANSLATED
    0x001CE000: Data(DataType.String, 8, "about", "の事は"),
    0x001CE008: Data(DataType.String, 20, "Left alone", "放っておいたこと"), # MACHINE_TRANSLATED
    0x001CE01C: Data(DataType.String, 20, "To be close to", "に、すり寄ったこと"), # MACHINE_TRANSLATED
    0x001CE030: Data(DataType.String, 24, "Because I was snuggled up to", "に、すり寄られたので"), # MACHINE_TRANSLATED
    0x001CE048: Data(DataType.String, 24, "What did you ask", "どうしたと尋ねたこと"), # MACHINE_TRANSLATED
    0x001CE060: Data(DataType.String, 20, "To tell something to", "に何かを伝えるべく"), # MACHINE_TRANSLATED
    0x001CE074: Data(DataType.String, 20, "Crying", "グエと鳴いたこと"), # MACHINE_TRANSLATED
    0x001CE088: Data(DataType.String, 12, "toward", "に向かって"),
    0x001CE094: Data(DataType.String, 28, "Having a cute gesture", "かわいいしぐさをしたこと"), # MACHINE_TRANSLATED
    0x001CE0B0: Data(DataType.String, 16, "Very cute", "に、かわいい"), # MACHINE_TRANSLATED
    0x001CE0C0: Data(DataType.String, 24, "I was told something", "に、何かを言われたが"), # MACHINE_TRANSLATED
    0x001CE0D8: Data(DataType.String, 20, "I didn't understand", "わからなかったこと"), # MACHINE_TRANSLATED
    0x001CE0EC: Data(DataType.String, 24, "I handed the material to", "に、資料を渡したこと"), # MACHINE_TRANSLATED
    0x001CE104: Data(DataType.String, 20, "Receive materials from", "から資料を受け取り"), # MACHINE_TRANSLATED
    0x001CE118: Data(DataType.String, 20, "To the information", "に、入手した情報を"), # MACHINE_TRANSLATED
    0x001CE12C: Data(DataType.String, 16, "What I heard", "耳打ちしたこと"), # MACHINE_TRANSLATED
    0x001CE13C: Data(DataType.String, 24, "To tell me the information from", "から情報を伝えてもらい"), # MACHINE_TRANSLATED
    0x001CE154: Data(DataType.String, 16, "Tell me something", "に、何か話して"), # MACHINE_TRANSLATED
    0x001CE164: Data(DataType.String, 16, "Blame", "とせがんだこと"), # MACHINE_TRANSLATED
    0x001CE174: Data(DataType.String, 20, "Having a change", "気分転換をしたこと"), # MACHINE_TRANSLATED
    0x001CE188: Data(DataType.String, 16, "Stroked", "になでられて"), # MACHINE_TRANSLATED
    0x001CE198: Data(DataType.String, 20, "It was pleasant", "気持ち良かったこと"), # MACHINE_TRANSLATED
    0x001CE1AC: Data(DataType.String, 24, "writing an opinion brief", "意見書を作成したこと"),
    0x001CE1C4: Data(DataType.String, 28, "doing information skill training", "情報技能の訓練をしたこと"),
    0x001CE1E0: Data(DataType.String, 20, "To work", "に、仕事の調子を"), # MACHINE_TRANSLATED
    0x001CE1F4: Data(DataType.String, 24, "Asked about your work", "に仕事の調子を尋ねられ"), # MACHINE_TRANSLATED
    0x001CE20C: Data(DataType.String, 20, "I answered that it was okay", "順調だと答えたこと"), # MACHINE_TRANSLATED
    0x001CE220: Data(DataType.String, 24, "I answered that it was not good", "芳しくないと答えたこと"), # MACHINE_TRANSLATED
    0x001CE238: Data(DataType.String, 12, "'s work", "の作業を"),
    0x001CE244: Data(DataType.String, 16, "What I did", "ねぎらったこと"), # MACHINE_TRANSLATED
    0x001CE254: Data(DataType.String, 24, "To the words of the onions from", "からのねぎらいの言葉に"), # MACHINE_TRANSLATED
    0x001CE26C: Data(DataType.String, 16, "Reply", "返答したこと"), # MACHINE_TRANSLATED
    0x001CE27C: Data(DataType.String, 20, "What I showed humbly", "謙遜してみせたこと"), # MACHINE_TRANSLATED
    0x001CE290: Data(DataType.String, 24, "I hindered my work", "に、仕事の邪魔をした"), # MACHINE_TRANSLATED
    0x001CE2A8: Data(DataType.String, 16, "I apologized", "と謝ったこと"), # MACHINE_TRANSLATED
    0x001CE2B8: Data(DataType.String, 20, "Job seems to be difficult", "の仕事が大変そうだ"), # MACHINE_TRANSLATED
    0x001CE2CC: Data(DataType.String, 16, "To worry about the situation", "に状況の不安を"), # MACHINE_TRANSLATED
    0x001CE2DC: Data(DataType.String, 12, "What I told", "語ったこと"), # MACHINE_TRANSLATED
    0x001CE2E8: Data(DataType.String, 24, "a silly story to", "に、たわいもない話を"),
    0x001CE300: Data(DataType.String, 12, "The discharge of", "の退院を"), # MACHINE_TRANSLATED
    0x001CE30C: Data(DataType.String, 16, "worrying", "気遣ったこと"),
    0x001CE31C: Data(DataType.String, 24, "Having taken a shower", "シャワーを浴びたこと"), # MACHINE_TRANSLATED
    0x001CE334: Data(DataType.String, 24, "about the previous battle to", "に、前回の戦闘について"),
    0x001CE34C: Data(DataType.String, 28, "In the last battle", "の、前回の戦闘での活躍を"), # MACHINE_TRANSLATED
    0x001CE368: Data(DataType.String, 16, "Praise", "賞賛したこと"), # MACHINE_TRANSLATED
    0x001CE378: Data(DataType.String, 28, "Of the good fight in the last battle", "の、前回の戦闘での善戦を"), # MACHINE_TRANSLATED
    0x001CE394: Data(DataType.String, 16, "praising", "たたえたこと"),
    0x001CE3A4: Data(DataType.String, 20, "I'm in good shape", "に、今の調子でいけ"), # MACHINE_TRANSLATED
    0x001CE3B8: Data(DataType.String, 20, "\"Be more careful!\"", "に、もっと注意しろ"),
    0x001CE3CC: Data(DataType.String, 12, "And more", "に、もっと"), # MACHINE_TRANSLATED
    0x001CE3D8: Data(DataType.String, 32, "What I told you to be careful", "気を引き締めろ、と言ったこと"), # MACHINE_TRANSLATED
    0x001CE3F8: Data(DataType.String, 20, "that the future is uncertain", "に、先行き不安だ"),
    0x001CE40C: Data(DataType.String, 16, "\"Do something!\"", "を、何とかしろ"),
    0x001CE41C: Data(DataType.String, 16, "reproaching", "と責めたこと"),
    0x001CE42C: Data(DataType.String, 28, "Can't be a pilot", "には、パイロットは無理だ"), # MACHINE_TRANSLATED
    0x001CE448: Data(DataType.String, 16, "that it was an easy win", "に、楽勝だった"),
    0x001CE458: Data(DataType.String, 20, "To win without effort", "に、労せず勝てた"), # MACHINE_TRANSLATED
    0x001CE46C: Data(DataType.String, 20, "that it's the fruit of their labors", "に、努力の成果だ"),
    0x001CE480: Data(DataType.String, 20, "that the fight was a little tough", "に、少し苦戦した"),
    0x001CE494: Data(DataType.String, 24, "It wasn't in good shape", "に、本調子じゃなかった"), # MACHINE_TRANSLATED
    0x001CE4AC: Data(DataType.String, 20, "considerably damaged", "に、かなりやられた"),
    0x001CE4C0: Data(DataType.String, 24, "piloting a.s.a.p.", "に、もうパイロットを"),
    0x001CE4D8: Data(DataType.String, 24, "saying they wanted to quit", "辞めたい、と言ったこと"),
    0x001CE4F0: Data(DataType.String, 20, "A bearish attitude", "に、弱気な態度を"), # MACHINE_TRANSLATED
    0x001CE504: Data(DataType.String, 12, "showing", "見せたこと"),
    0x001CE510: Data(DataType.String, 28, "the status of Tokyo-3 to", "に、第３新東京市の状況は"),
    0x001CE52C: Data(DataType.String, 28, "saying they're at peace", "安泰している、と言ったこと"),
    0x001CE548: Data(DataType.String, 20, "of Tokyo-3 to", "に、第３新東京市の"),
    0x001CE55C: Data(DataType.String, 32, "I said that the intercept function was in place", "迎撃機能は整った、と言ったこと"), # MACHINE_TRANSLATED
    0x001CE57C: Data(DataType.String, 28, "saying there are notable amounts of damage", "被害が目立つ、と言ったこと"),
    0x001CE598: Data(DataType.String, 28, "Tokyo's citizens to", "に、第３新東京市の住民は"),
    0x001CE5B4: Data(DataType.String, 28, "I said that I was almost evacuated", "ほぼ疎開した、と言ったこと"), # MACHINE_TRANSLATED
    0x001CE5D0: Data(DataType.String, 24, "To intercept the 3rd New Tokyo City", "に、第３新東京市の迎撃"), # MACHINE_TRANSLATED
    0x001CE5E8: Data(DataType.String, 32, "I said that the function is not expected", "機能は期待薄だ、と言ったこと"), # MACHINE_TRANSLATED
    0x001CE608: Data(DataType.String, 28, "And the destruction of the 3rd New Tokyo City", "に、第３新東京市の破棄が"), # MACHINE_TRANSLATED
    0x001CE624: Data(DataType.String, 24, "I said I decided", "決定した、と言ったこと"), # MACHINE_TRANSLATED
    0x001CE63C: Data(DataType.String, 28, "In addition, the apostle interception function is perfect", "に、使徒迎撃機能が万全で"), # MACHINE_TRANSLATED
    0x001CE658: Data(DataType.String, 24, "That you feel safe", "安心だ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CE670: Data(DataType.String, 20, "And the city function is perfect", "に、都市機能は万全"), # MACHINE_TRANSLATED
    0x001CE684: Data(DataType.String, 32, "After that, it was up to Eva", "あとはエヴァ次第、と答えたこと"), # MACHINE_TRANSLATED
    0x001CE6A4: Data(DataType.String, 16, "And the city function is", "に、都市機能は"), # MACHINE_TRANSLATED
    0x001CE6B4: Data(DataType.String, 32, "I answered that it was okay for a while", "しばらくは大丈夫、と答えたこと"), # MACHINE_TRANSLATED
    0x001CE6D4: Data(DataType.String, 28, "And I'm worried about city functions", "に、都市機能に不安があり"), # MACHINE_TRANSLATED
    0x001CE6F0: Data(DataType.String, 32, "That the battle is fifty-fifth", "戦いは五分五分だ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CE710: Data(DataType.String, 24, "Because of urban dysfunction", "に、都市機能不全のため"), # MACHINE_TRANSLATED
    0x001CE728: Data(DataType.String, 32, "I said that I would struggle", "苦戦するだろう、と答えたこと"), # MACHINE_TRANSLATED
    0x001CE748: Data(DataType.String, 24, "In addition, the evacuation of residents has progressed", "に、住民の疎開が進んで"), # MACHINE_TRANSLATED
    0x001CE760: Data(DataType.String, 32, "I answered that I would be lonelier", "もっと寂しくなる、と答えたこと"), # MACHINE_TRANSLATED
    0x001CE780: Data(DataType.String, 24, "In addition, the interception function of the city", "に、都市の迎撃機能には"), # MACHINE_TRANSLATED
    0x001CE798: Data(DataType.String, 28, "That you can't expect", "期待出来ない、と答えたこと"), # MACHINE_TRANSLATED
    0x001CE7B4: Data(DataType.String, 24, "And with the 3rd New Tokyo City", "に、第３新東京市とも"), # MACHINE_TRANSLATED
    0x001CE7CC: Data(DataType.String, 24, "Saying goodbye", "お別れだ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CE7E4: Data(DataType.String, 24, ", But Shinji was hospitalized", "に、シンジが入院したが"), # MACHINE_TRANSLATED
    0x001CE7FC: Data(DataType.String, 32, "I said that it was not a big deal", "大した事では無い、と言ったこと"), # MACHINE_TRANSLATED
    0x001CE81C: Data(DataType.String, 32, "What I said to leave the hospital soon", "すぐに退院する、と言ったこと"), # MACHINE_TRANSLATED
    0x001CE83C: Data(DataType.String, 24, "Then, Shinji was hospitalized", "に、シンジが入院して"), # MACHINE_TRANSLATED
    0x001CE854: Data(DataType.String, 28, "I was a little worried", "少し心配だ、と言ったこと"), # MACHINE_TRANSLATED
    0x001CE870: Data(DataType.String, 28, "Saying that it looks like a serious injury", "重傷のようだ、と言ったこと"), # MACHINE_TRANSLATED
    0x001CE88C: Data(DataType.String, 32, "I said, \"Is it okay?\"", "大丈夫だろうか、と言ったこと"), # MACHINE_TRANSLATED
    0x001CE8AC: Data(DataType.String, 28, "You said you wouldn't die", "死なないよね、と言ったこと"), # MACHINE_TRANSLATED
    0x001CE8C8: Data(DataType.String, 28, "To the dead Shinji", "に、死んだシンジのことを"), # MACHINE_TRANSLATED
    0x001CE8E4: Data(DataType.String, 28, "And about the dead Asuka", "に、死んだアスカのことを"), # MACHINE_TRANSLATED
    0x001CE900: Data(DataType.String, 28, "To the dead Touji", "に、死んだトウジのことを"), # MACHINE_TRANSLATED
    0x001CE91C: Data(DataType.String, 28, "To the dead Kaworu", "に、死んだカヲルのことを"), # MACHINE_TRANSLATED
    0x001CE938: Data(DataType.String, 24, "And evacuation is progressing", "と、疎開が進んでいる"), # MACHINE_TRANSLATED
    0x001CE950: Data(DataType.String, 24, "Talking about things", "事について話したこと"), # MACHINE_TRANSLATED
    0x001CE968: Data(DataType.String, 24, "And the number of students decreased due to evacuation", "と、疎開で生徒が減った"), # MACHINE_TRANSLATED
    0x001CE980: Data(DataType.String, 24, "And assortment of convenience stores", "と、コンビニの品揃えの"), # MACHINE_TRANSLATED
    0x001CE998: Data(DataType.String, 24, "What we talked about", "悪さについて話したこと"), # MACHINE_TRANSLATED
    0x001CE9B0: Data(DataType.String, 24, "And the product from the convenience store", "と、コンビニから商品が"), # MACHINE_TRANSLATED
    0x001CE9C8: Data(DataType.String, 32, "What I said was almost gone", "ほとんど消えていると話したこと"), # MACHINE_TRANSLATED
    0x001CE9E8: Data(DataType.String, 20, "Agreeing to the story", "の話に同意したこと"), # MACHINE_TRANSLATED
    0x001CE9FC: Data(DataType.String, 20, "Is okay to talk about", "の話に、大丈夫だ"), # MACHINE_TRANSLATED
    0x001CEA10: Data(DataType.String, 28, "And wishful observation", "と希望的観測を述べたこと"), # MACHINE_TRANSLATED
    0x001CEA2C: Data(DataType.String, 20, "Of the Hikari family", "と、ヒカリの家族の"), # MACHINE_TRANSLATED
    0x001CEA40: Data(DataType.String, 24, "Talking about death", "死について話したこと"), # MACHINE_TRANSLATED
    0x001CEA58: Data(DataType.String, 28, "And about the evacuation of Touji", "と、トウジの疎開について"), # MACHINE_TRANSLATED
    0x001CEA74: Data(DataType.String, 28, "And about Kensuke evacuation", "と、ケンスケ疎開について"), # MACHINE_TRANSLATED
    0x001CEA90: Data(DataType.String, 28, "And about the escape of Hikari", "と、ヒカリの疎開について"), # MACHINE_TRANSLATED
    0x001CEAAC: Data(DataType.String, 20, "And Rei’s house", "と、レイの住まいが"), # MACHINE_TRANSLATED
    0x001CEAC0: Data(DataType.String, 32, "Talking about the collapse", "倒壊した事について話したこと"), # MACHINE_TRANSLATED
    0x001CEAE0: Data(DataType.String, 12, "Listen to", "の話を聞き"), # MACHINE_TRANSLATED
    0x001CEAEC: Data(DataType.String, 16, "What I said", "絶句したこと"), # MACHINE_TRANSLATED
    0x001CEAFC: Data(DataType.String, 16, "I hurt my chest", "胸を痛めたこと"), # MACHINE_TRANSLATED
    0x001CEB0C: Data(DataType.String, 16, "I missed you", "寂しがったこと"), # MACHINE_TRANSLATED
    0x001CEB1C: Data(DataType.String, 16, "And today is hot", "に、今日は暑い"), # MACHINE_TRANSLATED
    0x001CEB2C: Data(DataType.String, 16, "That", "と話したこと"), # MACHINE_TRANSLATED
    0x001CEB3C: Data(DataType.String, 20, "Because today is hot", "から、今日は暑いと"), # MACHINE_TRANSLATED
    0x001CEB50: Data(DataType.String, 24, "What was said and agreed", "言われ、同意したこと"), # MACHINE_TRANSLATED
    0x001CEB68: Data(DataType.String, 28, "What I was told but denied", "言われたが、否定したこと"), # MACHINE_TRANSLATED
    0x001CEB98: Data(DataType.String, 28, "I did my homework with Chan", "に、宿題はチャンとやった"), # MACHINE_TRANSLATED
    0x001CEBB4: Data(DataType.String, 24, "I'm not doing my homework", "に、宿題はやっていない"), # MACHINE_TRANSLATED
    0x001CEBCC: Data(DataType.String, 20, "I was told about my homework", "から宿題の話をされ"), # MACHINE_TRANSLATED
    0x001CEBE0: Data(DataType.String, 12, "Surprised", "驚いたこと"), # MACHINE_TRANSLATED
    0x001CEBEC: Data(DataType.String, 16, "To the condition of my sister", "に、妹の容態を"), # MACHINE_TRANSLATED
    0x001CEBFC: Data(DataType.String, 20, "And my sister's condition is good", "に、妹の調子は良い"), # MACHINE_TRANSLATED
    0x001CEC10: Data(DataType.String, 28, "My sister's tone is", "に、妹の調子はボチボチだ"), # MACHINE_TRANSLATED
    0x001CEC2C: Data(DataType.String, 28, "Asked me about my sister’s condition", "から妹の容態を聞かれたが"), # MACHINE_TRANSLATED
    0x001CEC48: Data(DataType.String, 20, "About Misato", "に、ミサトについて"), # MACHINE_TRANSLATED
    0x001CEC5C: Data(DataType.String, 28, "Asked about Misato,", "からミサトの事を尋ねられ、"), # MACHINE_TRANSLATED
    0x001CEC78: Data(DataType.String, 20, "Praising Misato", "ミサトを誉めたこと"), # MACHINE_TRANSLATED
    0x001CEC8C: Data(DataType.String, 24, "That I'm a good person", "良い人だ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CECA4: Data(DataType.String, 28, "I answered that there is nothing in particular", "特に何も無い、と答えたこと"), # MACHINE_TRANSLATED
    0x001CECC0: Data(DataType.String, 28, "What Misato lightly broke", "ミサトを軽くけなしたこと"), # MACHINE_TRANSLATED
    0x001CECDC: Data(DataType.String, 28, "What I returned because of my dissatisfaction with Misato", "ミサトへの不満で返したこと"), # MACHINE_TRANSLATED
    0x001CECF8: Data(DataType.String, 28, "Can answer about Misato,", "からミサトの事を答えられ、"), # MACHINE_TRANSLATED
    0x001CED14: Data(DataType.String, 24, "Having a light relationship", "軽く相づちをうったこと"), # MACHINE_TRANSLATED
    0x001CED2C: Data(DataType.String, 24, "In addition, there is no location to support", "に、加持へのノロケを"), # MACHINE_TRANSLATED
    0x001CED44: Data(DataType.String, 24, "Norosuke talk to the support of", "の加持へのノロケ話に"), # MACHINE_TRANSLATED
    0x001CED5C: Data(DataType.String, 16, "Having listened", "耳を傾けたこと"), # MACHINE_TRANSLATED
    0x001CED6C: Data(DataType.String, 24, "Norooke story to the support of", "の加持へのノロケ話を"), # MACHINE_TRANSLATED
    0x001CED84: Data(DataType.String, 20, "What I shed without interest", "興味なく流したこと"), # MACHINE_TRANSLATED
    0x001CED98: Data(DataType.String, 24, "And distrust of support", "に、加持への不信感を"), # MACHINE_TRANSLATED
    0x001CEDB0: Data(DataType.String, 20, "Be defeated by", "に加持をけなされ"), # MACHINE_TRANSLATED
    0x001CEDC4: Data(DataType.String, 16, "What was ridiculous", "ムカついたこと"), # MACHINE_TRANSLATED
    0x001CEDD4: Data(DataType.String, 20, "To dissatisfaction with", "に、加持への不満を"), # MACHINE_TRANSLATED
    0x001CEDE8: Data(DataType.String, 16, "What exploded", "爆発させたこと"), # MACHINE_TRANSLATED
    0x001CEDF8: Data(DataType.String, 24, "Was told by Kaji", "から加持の話を聞かされ"), # MACHINE_TRANSLATED
    0x001CEE10: Data(DataType.String, 24, "Agree with Tekito", "テキトーに同意したこと"), # MACHINE_TRANSLATED
    0x001CEE28: Data(DataType.String, 28, "To see how resentful he was", "の加持に憤慨する様子を見て"), # MACHINE_TRANSLATED
    0x001CEE44: Data(DataType.String, 20, "Soothing $b", "$bをなだめたこと"), # MACHINE_TRANSLATED
    0x001CEE58: Data(DataType.String, 20, "The tone of ΑΤ", "に、ΑΤの調子を"), # MACHINE_TRANSLATED
    0x001CEE6C: Data(DataType.String, 24, "Asked the tone of ΑΤ", "にΑΤの調子を聞かれ"), # MACHINE_TRANSLATED
    0x001CEE84: Data(DataType.String, 24, "That you are doing well", "好調だ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CEE9C: Data(DataType.String, 24, "That it is normal", "普通だ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CEEB4: Data(DataType.String, 24, "That you feel unwell", "調子悪い、と答えたこと"), # MACHINE_TRANSLATED
    0x001CEECC: Data(DataType.String, 20, "To see what happened at school", "に、学校での様子を"), # MACHINE_TRANSLATED
    0x001CEEE0: Data(DataType.String, 24, "Asked me what they were doing at school", "に学校での様子を聞かれ"), # MACHINE_TRANSLATED
    0x001CEEF8: Data(DataType.String, 24, "That it was fun", "楽しい、と答えたこと"), # MACHINE_TRANSLATED
    0x001CEF10: Data(DataType.String, 32, "Having answered that there is nothing fun", "楽しい事は無い、と答えたこと"), # MACHINE_TRANSLATED
    0x001CEF30: Data(DataType.String, 16, "To school life", "の学校生活に"), # MACHINE_TRANSLATED
    0x001CEF40: Data(DataType.String, 20, "Blasting", "発破をかけたこと"), # MACHINE_TRANSLATED
    0x001CEF54: Data(DataType.String, 20, "What you said", "気休めを言ったこと"), # MACHINE_TRANSLATED
    0x001CEF68: Data(DataType.String, 24, "Is your work busy?", "に、仕事が忙しいのか"), # MACHINE_TRANSLATED
    0x001CEF80: Data(DataType.String, 16, "And work is easy", "に、仕事は楽に"), # MACHINE_TRANSLATED
    0x001CEF90: Data(DataType.String, 28, "I answered that I am doing well", "こなせている、と答えたこと"), # MACHINE_TRANSLATED
    0x001CEFAC: Data(DataType.String, 24, "To work without overtime", "に、仕事は残業無しで"), # MACHINE_TRANSLATED
    0x001CEFC4: Data(DataType.String, 20, "And work is fine", "に、仕事は問題無く"), # MACHINE_TRANSLATED
    0x001CEFD8: Data(DataType.String, 28, "And overtime is increasing recently", "に、最近残業が増えている"), # MACHINE_TRANSLATED
    0x001CEFF4: Data(DataType.String, 24, "And work is the busiest now", "に、仕事は今一番忙しい"), # MACHINE_TRANSLATED
    0x001CF00C: Data(DataType.String, 28, "What kind of organization is Nerv", "に、ネルフはどんな組織か"), # MACHINE_TRANSLATED
    0x001CF028: Data(DataType.String, 20, "About Nerv", "に、ネルフについて"), # MACHINE_TRANSLATED
    0x001CF03C: Data(DataType.String, 28, "I was asked, so I answered", "聞かれたので、答えたこと"), # MACHINE_TRANSLATED
    0x001CF058: Data(DataType.String, 20, "About Eva", "に、エヴァについて"), # MACHINE_TRANSLATED
    0x001CF06C: Data(DataType.String, 20, "About the apostle", "に、使徒について"), # MACHINE_TRANSLATED
    0x001CF080: Data(DataType.String, 28, "Asked about the apostle", "に、使徒について聞かれたが"), # MACHINE_TRANSLATED
    0x001CF09C: Data(DataType.String, 24, "I strayed the answer", "答えをはぐらかしたこと"), # MACHINE_TRANSLATED
    0x001CF0B4: Data(DataType.String, 28, "About the human complementation plan", "に、人類補完計画について"), # MACHINE_TRANSLATED
    0x001CF0D0: Data(DataType.String, 28, "Asked, but stopped", "聞かれたが、制止したこと"), # MACHINE_TRANSLATED
    0x001CF0EC: Data(DataType.String, 24, "Heard and taught lightly", "聞かれ、軽く教えたこと"), # MACHINE_TRANSLATED
    0x001CF104: Data(DataType.String, 24, "Heard and deeply taught", "聞かれ、深く教えたこと"), # MACHINE_TRANSLATED
    0x001CF11C: Data(DataType.String, 16, "About my father", "に、父について"), # MACHINE_TRANSLATED
    0x001CF12C: Data(DataType.String, 28, "Asked about Gendou", "に、ゲンドウについて聞かれ"), # MACHINE_TRANSLATED
    0x001CF148: Data(DataType.String, 28, "I answered that he was a good person", "立派な人だ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF164: Data(DataType.String, 28, "That you are a busy person", "忙しい人だ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF180: Data(DataType.String, 28, "That you are the lowest boss", "最低の上司だ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF19C: Data(DataType.String, 32, "I don't understand", "よくわからない、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF1BC: Data(DataType.String, 24, "And to evaluate Gendou", "に、ゲンドウへの評価を"), # MACHINE_TRANSLATED
    0x001CF1D4: Data(DataType.String, 24, "Thank you for telling me", "教えて貰い、礼を言った"), # MACHINE_TRANSLATED
    0x001CF1EC: Data(DataType.String, 28, "Asking about Gendou", "のゲンドウを尋ねる様子に"), # MACHINE_TRANSLATED
    0x001CF208: Data(DataType.String, 24, "I rushed in unexpectedly", "思わず突っ込んだこと"), # MACHINE_TRANSLATED
    0x001CF220: Data(DataType.String, 16, "Plunged into", "に突っ込まれて"), # MACHINE_TRANSLATED
    0x001CF230: Data(DataType.String, 28, "What became sloppy", "しどろもどろになったこと"), # MACHINE_TRANSLATED
    0x001CF24C: Data(DataType.String, 20, "To see the state of the child", "に、子供の様子を"), # MACHINE_TRANSLATED
    0x001CF260: Data(DataType.String, 24, "Asked about the child", "に、子供の様子を聞かれ"), # MACHINE_TRANSLATED
    0x001CF278: Data(DataType.String, 32, "I answered that I have no worries", "何の心配も無い、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF298: Data(DataType.String, 28, "I answered that it feels good", "イイ感じだ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF2B4: Data(DataType.String, 28, "Well, that's average", "まあ平均的だ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF2D0: Data(DataType.String, 32, "I answered that I have trouble with unevenness", "ムラが有って困る、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF2F0: Data(DataType.String, 28, "That you feel unwell", "調子が悪い、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF30C: Data(DataType.String, 20, "And the tone of Eva", "に、エヴァの調子を"), # MACHINE_TRANSLATED
    0x001CF320: Data(DataType.String, 28, "Asked the tone of Eva", "に、エヴァの調子を聞かれ"), # MACHINE_TRANSLATED
    0x001CF33C: Data(DataType.String, 28, "That you are in the best condition", "最高の状態だ、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF358: Data(DataType.String, 24, "I answered that there is no problem", "問題無い、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF370: Data(DataType.String, 32, "That there was a problem", "問題が発生した、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF390: Data(DataType.String, 28, "I answered that it was not good", "芳しくない、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF3AC: Data(DataType.String, 24, "Restrained the intelligence activity of", "の諜報活動を牽制した"), # MACHINE_TRANSLATED
    0x001CF3C4: Data(DataType.String, 28, "Was asked about intelligence activities", "に、諜報活動の事を聞かれ"), # MACHINE_TRANSLATED
    0x001CF3E0: Data(DataType.String, 16, "Blurry", "とぼけたこと"), # MACHINE_TRANSLATED
    0x001CF3F0: Data(DataType.String, 16, "Deceived", "誤魔化したこと"), # MACHINE_TRANSLATED
    0x001CF400: Data(DataType.String, 28, "I told you to speak", "そのうち話す、と答えたこと"), # MACHINE_TRANSLATED
    0x001CF41C: Data(DataType.String, 32, "I told you to pretend", "見ぬフリをしてくれと返したこと"), # MACHINE_TRANSLATED
    0x001CF43C: Data(DataType.String, 28, "Muttering personal danger", "身の危険をつぶやいたこと"), # MACHINE_TRANSLATED
    0x001CF458: Data(DataType.String, 16, "To print", "に、プリントを"), # MACHINE_TRANSLATED
    0x001CF468: Data(DataType.String, 12, "What I entrusted", "託したこと"), # MACHINE_TRANSLATED
    0x001CF474: Data(DataType.String, 20, "To print", "から、プリントを"), # MACHINE_TRANSLATED
    0x001CF488: Data(DataType.String, 24, "I was happy to be handed over", "渡され、嬉しかったこと"), # MACHINE_TRANSLATED
    0x001CF4A0: Data(DataType.String, 28, "Passed and disappointed", "渡され、がっかりしたこと"), # MACHINE_TRANSLATED
    0x001CF4BC: Data(DataType.String, 20, "Happy to be discharged from the hospital", "の退院を喜んだこと"), # MACHINE_TRANSLATED
    0x001CF4D0: Data(DataType.String, 16, "Celebrated to be discharged", "に退院を祝われ"), # MACHINE_TRANSLATED
    0x001CF4E0: Data(DataType.String, 16, "I was happy", "嬉しかったこと"), # MACHINE_TRANSLATED
    0x001CF4F0: Data(DataType.String, 24, "Was celebrated by the hospital", "に退院を祝われたこと"), # MACHINE_TRANSLATED
    0x001CF508: Data(DataType.String, 20, "Was celebrated by the hospital", "に退院を祝われたが"), # MACHINE_TRANSLATED
    0x001CF51C: Data(DataType.String, 32, "I answered that I was not in good shape yet", "まだ本調子じゃないと答えたこと"), # MACHINE_TRANSLATED
    0x001CF53C: Data(DataType.String, 20, "Sincerely pleased", "心から喜んだこと"), # MACHINE_TRANSLATED
    0x001CF550: Data(DataType.String, 16, "To the discharge greeting of", "の退院挨拶に"), # MACHINE_TRANSLATED
    0x001CF560: Data(DataType.String, 20, "I returned normally", "普通に返したこと"), # MACHINE_TRANSLATED
    0x001CF574: Data(DataType.String, 16, "The discharge greeting of", "の退院挨拶を"), # MACHINE_TRANSLATED
    0x001CF584: Data(DataType.String, 20, "Returning to nothing", "無下に返したこと"), # MACHINE_TRANSLATED
    0x001CF598: Data(DataType.String, 20, "The fun-looking state of", "の楽しそうな様子を"), # MACHINE_TRANSLATED
    0x001CF5AC: Data(DataType.String, 16, "What I pointed out", "指摘したこと"), # MACHINE_TRANSLATED
    0x001CF5BC: Data(DataType.String, 24, "A motivated appearance", "のやる気に満ちた様子を"), # MACHINE_TRANSLATED
    0x001CF5D4: Data(DataType.String, 16, "The serious expression of", "の真剣な表情を"), # MACHINE_TRANSLATED
    0x001CF5E4: Data(DataType.String, 20, "The tense appearance of", "の緊張した様子を"), # MACHINE_TRANSLATED
    0x001CF5F8: Data(DataType.String, 20, "The relieved state of", "のホッとした様子を"), # MACHINE_TRANSLATED
    0x001CF60C: Data(DataType.String, 20, "The uneasy appearance of", "の不安めいた様子を"), # MACHINE_TRANSLATED
    0x001CF620: Data(DataType.String, 24, "The sadness of", "の悲しんでいる様子を"), # MACHINE_TRANSLATED
    0x001CF638: Data(DataType.String, 24, "The state of being relaxed", "の気が緩んでいる様子を"), # MACHINE_TRANSLATED
    0x001CF650: Data(DataType.String, 24, "How discouraged", "の落胆している様子を"), # MACHINE_TRANSLATED
    0x001CF668: Data(DataType.String, 20, "The moody state of", "の不機嫌な様子を"), # MACHINE_TRANSLATED
    0x001CF67C: Data(DataType.String, 20, "The angry appearance of", "の怒っている様子を"), # MACHINE_TRANSLATED
    0x001CF690: Data(DataType.String, 20, "Because his face was red", "の顔が赤かったので"), # MACHINE_TRANSLATED
    0x001CF6A4: Data(DataType.String, 24, "How embarrassed", "の恥らっている様子を"), # MACHINE_TRANSLATED
    0x001CF6BC: Data(DataType.String, 20, "Asked the situation", "に様子を尋ねられ"), # MACHINE_TRANSLATED
    0x001CF6D0: Data(DataType.String, 20, "Bright and positive", "明るく肯定したこと"), # MACHINE_TRANSLATED
    0x001CF6E4: Data(DataType.String, 24, "Bright and misleading", "明るく誤魔化したこと"), # MACHINE_TRANSLATED
    0x001CF6FC: Data(DataType.String, 20, "Brightly denied", "明るく否定したこと"), # MACHINE_TRANSLATED
    0x001CF710: Data(DataType.String, 20, "Seriously affirmed", "真剣に肯定したこと"), # MACHINE_TRANSLATED
    0x001CF724: Data(DataType.String, 16, "Denied", "否定したこと"), # MACHINE_TRANSLATED
    0x001CF734: Data(DataType.String, 24, "Awkward affirmation", "気まずく肯定したこと"), # MACHINE_TRANSLATED
    0x001CF74C: Data(DataType.String, 24, "Awkwardly misleading", "気まずく誤魔化したこと"), # MACHINE_TRANSLATED
    0x001CF764: Data(DataType.String, 24, "Awkwardly denied", "気まずく否定したこと"), # MACHINE_TRANSLATED
    0x001CF77C: Data(DataType.String, 24, "Positive things that tend to sink", "沈みがちに肯定したこと"), # MACHINE_TRANSLATED
    0x001CF794: Data(DataType.String, 28, "What was fooled by the tendency to sink", "沈みがちに誤魔化したこと"), # MACHINE_TRANSLATED
    0x001CF7B0: Data(DataType.String, 24, "Denial that tends to sink", "沈みがちに否定したこと"), # MACHINE_TRANSLATED
    0x001CF7C8: Data(DataType.String, 24, "bashfully repressing", "照れながら制止したこと"),
    0x001CF7E0: Data(DataType.String, 28, "bashfully dodging", "照れながら誤魔化したこと"),
    0x001CF7FC: Data(DataType.String, 24, "bashfully denying", "照れながら否定したこと"),
    0x001CF814: Data(DataType.String, 24, "Asked about the situation,", "に様子を尋ねられたが、"), # MACHINE_TRANSLATED
    0x001CF82C: Data(DataType.String, 28, "casually finishing", "さり気なく切り上げたこと"),
    0x001CF848: Data(DataType.String, 24, "forcibly stopping", "無理やり打ち切ったこと"),
    0x001CF860: Data(DataType.String, 8, "the lesson", "授業を"),
    0x001CF868: Data(DataType.String, 20, "typically taking on", "普通に受けたこと"),
    0x001CF87C: Data(DataType.String, 20, "seriously taking on", "マジメに受けたこと"),
    0x001CF890: Data(DataType.String, 12, "mid-lesson", "授業中、"),
    0x001CF89C: Data(DataType.String, 24, "secretly moonlighting", "コッソリ内職したこと"),
    0x001CF8B4: Data(DataType.String, 28, "vacantly gazing outside", "ぼんやりと外を眺めたこと"),
    0x001CF8D0: Data(DataType.String, 20, "nodding off", "居眠りをしたこと"),
    0x001CF8E4: Data(DataType.String, 16, "During class", "を、授業中に"), # MACHINE_TRANSLATED
    0x001CF8F4: Data(DataType.String, 20, "glancing now and again", "チラチラ見たこと"),
    0x001CF908: Data(DataType.String, 12, "And in class", "と、授業中"), # MACHINE_TRANSLATED
    0x001CF914: Data(DataType.String, 28, "sharing secrets through the mail", "メールで内緒話をしたこと"),
    0x001CF930: Data(DataType.String, 24, "Let's go to school together", "に、一緒に登校しよう"), # MACHINE_TRANSLATED
    0x001CF948: Data(DataType.String, 24, "going to school with", "と一緒に登校したこと"),
    0x001CF960: Data(DataType.String, 20, "an invitation to go to school from", "からの登校の誘いを"),
    0x001CF974: Data(DataType.String, 24, "evasively turning down", "あいまいに断ったこと"),
    0x001CF98C: Data(DataType.String, 20, "hurrying to school with", "と学校に急いだこと"),
    0x001CF9B8: Data(DataType.String, 28, "I was about to go", "行こう、と持ちかけたこと"), # MACHINE_TRANSLATED
    0x001CF9D4: Data(DataType.String, 28, "Heading to Nerv Headquarters", "ネルフ本部へ向かったこと"), # MACHINE_TRANSLATED
    0x001CF9F0: Data(DataType.String, 28, "Inviting Nerv from Tokyo", "からのネルフ登庁の誘いを"), # MACHINE_TRANSLATED
    0x001CFA0C: Data(DataType.String, 16, "To Nerv Headquarters", "とネルフ本部へ"), # MACHINE_TRANSLATED
    0x001CFA1C: Data(DataType.String, 12, "Hurry up", "急いだこと"), # MACHINE_TRANSLATED
    0x001CFA28: Data(DataType.String, 24, "To exchange items", "に、アイテムの交換を"), # MACHINE_TRANSLATED
    0x001CFA40: Data(DataType.String, 16, "What I brought", "持ちかけたこと"), # MACHINE_TRANSLATED
    0x001CFA50: Data(DataType.String, 28, "And the items that can be exchanged are", "に、交換出来るアイテムは"), # MACHINE_TRANSLATED
    0x001CFA6C: Data(DataType.String, 28, "I told you I don't have", "持っていない、と伝えたこと"), # MACHINE_TRANSLATED
    0x001CFA88: Data(DataType.String, 24, "Of item exchange from", "からのアイテム交換の"), # MACHINE_TRANSLATED
    0x001CFAA0: Data(DataType.String, 20, "I refused the invitation", "誘いを、断ったこと"), # MACHINE_TRANSLATED
    0x001CFAB4: Data(DataType.String, 20, "I was invited", "誘いに乗ったこと"), # MACHINE_TRANSLATED
    0x001CFAC8: Data(DataType.String, 20, "Exchange items with", "とのアイテム交換を"), # MACHINE_TRANSLATED
    0x001CFADC: Data(DataType.String, 28, "After all, I refused", "やっぱりいい、と断ったこと"), # MACHINE_TRANSLATED
    0x001CFAF8: Data(DataType.String, 20, "By exchanging items with", "とのアイテム交換で"), # MACHINE_TRANSLATED
    0x001CFB0C: Data(DataType.String, 24, "Choosing what you want", "欲しい物を選んだこと"), # MACHINE_TRANSLATED
    0x001CFB24: Data(DataType.String, 24, "Refusing the chosen one", "選ばれた物を断ったこと"), # MACHINE_TRANSLATED
    0x001CFB3C: Data(DataType.String, 20, "That the negotiation was concluded", "交渉成立したこと"), # MACHINE_TRANSLATED
    0x001CFB50: Data(DataType.String, 20, "staring at the ceiling", "天井を見つめたこと"),
    0x001CFB64: Data(DataType.String, 20, "spacing out", "ぼんやりしたこと"),
    0x001CFB78: Data(DataType.String, 20, "listening to music", "音楽を聴いたこと"),
    0x001CFB8C: Data(DataType.String, 20, "Reading a magazine", "雑誌を読んだこと"), # MACHINE_TRANSLATED
    0x001CFBA0: Data(DataType.String, 20, "Gendo's glasses", "ゲンドウのメガネを"),
    0x001CFBB4: Data(DataType.String, 16, "looking at", "見つめたこと"),
    0x001CFBC4: Data(DataType.String, 20, "drinking beer", "ビールを飲んだこと"),
    0x001CFBD8: Data(DataType.String, 20, "To talk to", "に話しかけたこと"), # MACHINE_TRANSLATED
    0x001CFBEC: Data(DataType.String, 28, "Talked to me from the bed", "から話しかけられ、ベッド"), # MACHINE_TRANSLATED
    0x001CFC08: Data(DataType.String, 28, "I got up and responded", "から立ち上がり応対したこと"), # MACHINE_TRANSLATED
    0x001CFC24: Data(DataType.String, 24, "I was told by", "から話しかけられたが"), # MACHINE_TRANSLATED
    0x001CFC3C: Data(DataType.String, 16, "What I got rid of", "追い払ったこと"), # MACHINE_TRANSLATED
    0x001CFC4C: Data(DataType.String, 28, "Vaguely relaxing", "ぼんやりとくつろいだこと"), # MACHINE_TRANSLATED
    0x001CFC68: Data(DataType.String, 24, "drinking juice", "ジュースを飲んだこと"),
    0x001CFC80: Data(DataType.String, 28, "From the bench", "から話しかけられ、ベンチ"), # MACHINE_TRANSLATED
    0x001CFC9C: Data(DataType.String, 28, "And a harmonics test", "に、ハーモニクステストを"), # MACHINE_TRANSLATED
    0x001CFCB8: Data(DataType.String, 16, "What I requested", "依頼したこと"), # MACHINE_TRANSLATED
    0x001CFCC8: Data(DataType.String, 28, "From the harmonics test", "からハーモニクステストを"), # MACHINE_TRANSLATED
    0x001CFCE4: Data(DataType.String, 28, "Requested but refused", "依頼されたが、断ったこと"), # MACHINE_TRANSLATED
    0x001CFD00: Data(DataType.String, 24, "The harmonics test", "のハーモニクステストを"), # MACHINE_TRANSLATED
    0x001CFD18: Data(DataType.String, 24, "Of the harmonics test", "のハーモニクステストの"), # MACHINE_TRANSLATED
    0x001CFD30: Data(DataType.String, 24, "I was satisfied with the result", "結果に、満足したこと"), # MACHINE_TRANSLATED
    0x001CFD48: Data(DataType.String, 24, "The result was reassuring", "結果に、安心したこと"), # MACHINE_TRANSLATED
    0x001CFD60: Data(DataType.String, 24, "I was disappointed in the result", "結果に、落胆したこと"), # MACHINE_TRANSLATED
    0x001CFD78: Data(DataType.String, 20, "Invited to the rooftop", "を屋上に誘ったこと"), # MACHINE_TRANSLATED
    0x001CFD8C: Data(DataType.String, 24, "To invite to the roof from", "からの屋上への誘いに"), # MACHINE_TRANSLATED
    0x001CFDA4: Data(DataType.String, 12, "Riding", "乗ったこと"), # MACHINE_TRANSLATED
    0x001CFDB0: Data(DataType.String, 16, "from the roof with", "と、屋上から"),
    0x001CFDC0: Data(DataType.String, 20, "Going back downstairs", "階下に戻ったこと"), # MACHINE_TRANSLATED
    0x001CFDD4: Data(DataType.String, 20, "To the outdoors of Nerv", "をネルフの屋外へ"), # MACHINE_TRANSLATED
    0x001CFDE8: Data(DataType.String, 12, "What I invited", "誘ったこと"), # MACHINE_TRANSLATED
    0x001CFDF4: Data(DataType.String, 24, "From nerv outdoors", "からのネルフ屋外への"), # MACHINE_TRANSLATED
    0x001CFE0C: Data(DataType.String, 32, "Ambiguous decline of invitation", "誘いを、あいまいに断ったこと"), # MACHINE_TRANSLATED
    0x001CFE2C: Data(DataType.String, 20, "From the nerf outdoors", "と、ネルフ屋外から"), # MACHINE_TRANSLATED
    0x001CFE40: Data(DataType.String, 20, "Returning to the headquarters", "本部内へ戻ったこと"), # MACHINE_TRANSLATED
    0x001CFE54: Data(DataType.String, 24, "In addition, synchro skill training", "に、シンクロ技能訓練を"), # MACHINE_TRANSLATED
    0x001CFE6C: Data(DataType.String, 12, "Staff skills", "参謀技能の"), # MACHINE_TRANSLATED
    0x001CFE78: Data(DataType.String, 16, "Having trained", "訓練をしたこと"), # MACHINE_TRANSLATED
    0x001CFE88: Data(DataType.String, 12, "Development skills", "開発技能の"), # MACHINE_TRANSLATED
    0x001CFE94: Data(DataType.String, 20, "operator skill", "オペレート技能の"),
    0x001CFEA8: Data(DataType.String, 12, "espionage skill", "諜報技能の"),
    0x001CFEB4: Data(DataType.String, 12, "clerical skill", "事務技能の"),
    0x001CFEC0: Data(DataType.String, 12, "information skill", "情報技能の"),
    0x001CFECC: Data(DataType.String, 12, "self-defense skill", "白兵技能の"),
    0x001CFED8: Data(DataType.String, 20, "making a bento box", "お弁当を作ったこと"),
    0x001CFEEC: Data(DataType.String, 24, "Escape from the city", "街から逃げ出したこと"), # MACHINE_TRANSLATED
    0x001CFF04: Data(DataType.String, 16, "Washing my face", "顔を洗ったこと"), # MACHINE_TRANSLATED
    0x001CFF14: Data(DataType.String, 28, "What inspired me to develop myself", "自己啓発して奮起したこと"), # MACHINE_TRANSLATED
    0x001CFF30: Data(DataType.String, 28, "Being self-loathing and depressed", "自己嫌悪して落ち込んだこと"), # MACHINE_TRANSLATED
    0x001CFF4C: Data(DataType.String, 20, "looking at Unit-00", "零号機を見たこと"),
    0x001CFF60: Data(DataType.String, 20, "looking at Unit-01", "初号機を見たこと"),
    0x001CFF74: Data(DataType.String, 20, "looking at Unit-02", "弐号機を見たこと"),
    0x001CFF88: Data(DataType.String, 20, "looking at Unit-03", "参号機を見たこと"),
    0x001CFF9C: Data(DataType.String, 20, "looking at Unit-04", "四号機を見たこと"),
    0x001CFFB0: Data(DataType.String, 24, "the current state of Nerv's fighting power", "ネルフの戦力の現状を"),
    0x001CFFC8: Data(DataType.String, 16, "verifying", "確認したこと"),
    0x001CFFD8: Data(DataType.String, 28, "viewing Nerv General Information", "ネルフ総合情報を見たこと"),
    0x001CFFF4: Data(DataType.String, 24, "soliciting an item", "アイテムをねだったこと"),
    0x001D000C: Data(DataType.String, 24, "Having chosen an item", "アイテムを選ばせたこと"), # MACHINE_TRANSLATED
    0x001D0024: Data(DataType.String, 16, "Items from", "からアイテムを"), # MACHINE_TRANSLATED
    0x001D0034: Data(DataType.String, 28, "Begged, but refused", "ねだられたが、断ったこと"), # MACHINE_TRANSLATED
    0x001D0050: Data(DataType.String, 24, "To the item you want", "に、欲しいアイテムを"), # MACHINE_TRANSLATED
    0x001D0068: Data(DataType.String, 28, "I don't have the item I want", "に、欲しいアイテムが無く"), # MACHINE_TRANSLATED
    0x001D0084: Data(DataType.String, 28, "After all it was said that it was good", "やっぱりいい、と言ったこと"), # MACHINE_TRANSLATED
    0x001D00A0: Data(DataType.String, 24, "The item you wanted", "の欲しがったアイテムを"), # MACHINE_TRANSLATED
    0x001D00B8: Data(DataType.String, 16, "giving to $b", "$bにあげたこと"),
    0x001D00C8: Data(DataType.String, 24, "The item I wanted", "の欲しがったアイテムは"), # MACHINE_TRANSLATED
    0x001D00E0: Data(DataType.String, 24, "I refused to pass it", "渡せない、と断ったこと"), # MACHINE_TRANSLATED
    0x001D00F8: Data(DataType.String, 20, "Get items from", "からアイテムを貰い"), # MACHINE_TRANSLATED
    0x001D010C: Data(DataType.String, 20, "For physical recovery", "に、体力回復用の"), # MACHINE_TRANSLATED
    0x001D0120: Data(DataType.String, 20, "To quench your thirst", "に、喉の渇きを癒す"), # MACHINE_TRANSLATED
    0x001D0134: Data(DataType.String, 20, "To wake up", "に、目を覚まさせる"), # MACHINE_TRANSLATED
    0x001D0148: Data(DataType.String, 12, "I hate", "に、嫌いな"), # MACHINE_TRANSLATED
    0x001D0154: Data(DataType.String, 20, "To meet the lust", "に、色欲を満たす"), # MACHINE_TRANSLATED
    0x001D0168: Data(DataType.String, 20, "To meet the desire", "に、物欲を満たす"), # MACHINE_TRANSLATED
    0x001D017C: Data(DataType.String, 12, "In gold", "に、金目の"), # MACHINE_TRANSLATED
    0x001D0188: Data(DataType.String, 20, "To meet the desire for honor", "に、名誉欲を満たす"), # MACHINE_TRANSLATED
    0x001D019C: Data(DataType.String, 20, "To meet the greed", "に、力欲を満たす"), # MACHINE_TRANSLATED
    0x001D01B0: Data(DataType.String, 28, "For when you want to be liked by everyone", "に、皆に好かれたい時用の"), # MACHINE_TRANSLATED
    0x001D01CC: Data(DataType.String, 28, "For when you want to do justice", "に、正義をなしたい時用の"), # MACHINE_TRANSLATED
    0x001D01E8: Data(DataType.String, 24, "For when you want to live in love", "に、恋に生きたい時用の"), # MACHINE_TRANSLATED
    0x001D0200: Data(DataType.String, 28, "For when you don't want to do anything", "に、何もしたくない時用の"), # MACHINE_TRANSLATED
    0x001D021C: Data(DataType.String, 28, "When you want to go to the bathroom", "に、トイレに行きたい時の"), # MACHINE_TRANSLATED
    0x001D0238: Data(DataType.String, 28, "For when you want to live in friendship", "に、友情に生きたい時用の"), # MACHINE_TRANSLATED
    0x001D0254: Data(DataType.String, 28, "For when you want to live dearly", "に、親愛に生きたい時用の"), # MACHINE_TRANSLATED
    0x001D0270: Data(DataType.String, 28, "presenting an item", "アイテムを差し出したこと"),
    0x001D028C: Data(DataType.String, 24, "Synchro skill training", "のシンクロ技能訓練を"), # MACHINE_TRANSLATED
    0x001D02A4: Data(DataType.String, 24, "Of synchronized skill training", "のシンクロ技能訓練の"), # MACHINE_TRANSLATED
    0x001D02BC: Data(DataType.String, 20, "To recent events", "に、最近の出来事を"), # MACHINE_TRANSLATED
    0x001D02D0: Data(DataType.String, 20, "The events of others", "に、他人の出来事を"), # MACHINE_TRANSLATED
    0x001D02E4: Data(DataType.String, 20, "To the recent complaints", "に、最近の愚痴を"), # MACHINE_TRANSLATED
    0x001D02F8: Data(DataType.String, 20, "To the previous events", "に、以前の出来事を"), # MACHINE_TRANSLATED
    0x001D030C: Data(DataType.String, 20, "I saw an ornamental plant", "観葉植物を見たこと"), # MACHINE_TRANSLATED
    0x001D0320: Data(DataType.String, 28, "looking at the cafeteria menu", "食堂のメニューを見たこと"),
    0x001D033C: Data(DataType.String, 12, "to locker", "ロッカーに"),
    0x001D0348: Data(DataType.String, 20, "I checked in my luggage", "荷物を預けたこと"), # MACHINE_TRANSLATED
    0x001D035C: Data(DataType.String, 16, "from locker", "ロッカーから"),
    0x001D036C: Data(DataType.String, 24, "I took out my luggage", "荷物を取り出したこと"), # MACHINE_TRANSLATED
    0x001D0384: Data(DataType.String, 20, "watching videos", "ビデオを観たこと"),
    0x001D0398: Data(DataType.String, 20, "going to the bathroom", "トイレに行ったこと"),
    0x001D03AC: Data(DataType.String, 12, "To the story of", "の話に、"), # MACHINE_TRANSLATED
    0x001D03B8: Data(DataType.String, 32, "Having shared with Tekito", "テキトーに相づちをうったこと"), # MACHINE_TRANSLATED
    0x001D03D8: Data(DataType.String, 20, "I got on the story of", "の話に乗ったこと"), # MACHINE_TRANSLATED
    0x001D03EC: Data(DataType.String, 28, "That's it", "それだけか、と言ったこと"), # MACHINE_TRANSLATED
    0x001D0408: Data(DataType.String, 16, "And recent things", "に、最近の事を"), # MACHINE_TRANSLATED
    0x001D0418: Data(DataType.String, 12, "thinking", "教えたこと"),
    0x001D0424: Data(DataType.String, 16, "To the current physical condition", "に、今の体調を"), # MACHINE_TRANSLATED
    0x001D0434: Data(DataType.String, 20, "And the recent tone", "に、最近の調子を"), # MACHINE_TRANSLATED
    0x001D0448: Data(DataType.String, 24, "I was asked for money", "に、お金をねだったこと"), # MACHINE_TRANSLATED
    0x001D0460: Data(DataType.String, 24, "Passed money to", "に、お金を渡したこと"), # MACHINE_TRANSLATED
    0x001D0478: Data(DataType.String, 20, "Innocent of money from", "からのお金の無心に"), # MACHINE_TRANSLATED
    0x001D048C: Data(DataType.String, 32, "I refused that I had no money", "持ち合わせが無い、と断ったこと"), # MACHINE_TRANSLATED
    0x001D04AC: Data(DataType.String, 20, "Heartless money from", "からのお金の無心を"), # MACHINE_TRANSLATED
    0x001D04C0: Data(DataType.String, 24, "I was dissatisfied with", "に、不満をぶつけたこと"), # MACHINE_TRANSLATED
    0x001D04D8: Data(DataType.String, 24, "Dissatisfaction hit by", "からぶつけられた不満を"), # MACHINE_TRANSLATED
    0x001D04F0: Data(DataType.String, 24, "listening quietly", "黙って聞いていたこと"),
    0x001D0508: Data(DataType.String, 24, "To the frustration that was hit", "からぶつけられた不満に"), # MACHINE_TRANSLATED
    0x001D0520: Data(DataType.String, 24, "What I complained about", "文句を言い返したこと"), # MACHINE_TRANSLATED
    0x001D0538: Data(DataType.String, 28, "I was dissatisfied by", "から不満をぶつけられたが"), # MACHINE_TRANSLATED
    0x001D0554: Data(DataType.String, 24, "What you didn't do", "相手にしなかったこと"), # MACHINE_TRANSLATED
    0x001D056C: Data(DataType.String, 20, "The lines that provoke", "を挑発するセリフを"), # MACHINE_TRANSLATED
    0x001D0580: Data(DataType.String, 12, "Spit", "吐いたこと"), # MACHINE_TRANSLATED
    0x001D058C: Data(DataType.String, 20, "Was provoked by", "から挑発されたが"), # MACHINE_TRANSLATED
    0x001D05A0: Data(DataType.String, 16, "Provoked by", "から挑発され"), # MACHINE_TRANSLATED
    0x001D05B0: Data(DataType.String, 28, "I laughed like a fool", "馬鹿にするように笑ったこと"), # MACHINE_TRANSLATED
    0x001D05CC: Data(DataType.String, 16, "The undertone of ΑΤ", "のΑΤの低調を"), # MACHINE_TRANSLATED
    0x001D05DC: Data(DataType.String, 24, "Was scolded by ΑΤ undertone", "からΑΤ低調を叱られ"), # MACHINE_TRANSLATED
    0x001D05F4: Data(DataType.String, 20, "Apologize without power", "力なく謝ったこと"), # MACHINE_TRANSLATED
    0x001D0608: Data(DataType.String, 24, "To show a favor for", "への好意を表したこと"), # MACHINE_TRANSLATED
    0x001D0620: Data(DataType.String, 24, "Treated with friendship from", "から友好的に接せられ"), # MACHINE_TRANSLATED
    0x001D0638: Data(DataType.String, 24, "Responding positively", "好意的に応対したこと"), # MACHINE_TRANSLATED
    0x001D0650: Data(DataType.String, 28, "Responding with an evil attitude", "邪険な態度で応対したこと"), # MACHINE_TRANSLATED
    0x001D066C: Data(DataType.String, 16, "In a friendly way", "に、気さくに"), # MACHINE_TRANSLATED
    0x001D067C: Data(DataType.String, 28, "Talked to me kindly", "から気さくに話しかけられ"), # MACHINE_TRANSLATED
    0x001D0698: Data(DataType.String, 16, "The height of ΑΤ", "のΑΤの高さを"), # MACHINE_TRANSLATED
    0x001D06A8: Data(DataType.String, 20, "What I was impressed with", "感心してみせたこと"), # MACHINE_TRANSLATED
    0x001D06BC: Data(DataType.String, 28, "Was impressed by the height of ΑΤ", "からΑΤの高さを感心され"), # MACHINE_TRANSLATED
    0x001D06D8: Data(DataType.String, 12, "looking at", "を見たこと"),
    0x001D06E4: Data(DataType.String, 24, "Seeing with a positive eye", "を好意的な目で見たこと"), # MACHINE_TRANSLATED
    0x001D06FC: Data(DataType.String, 28, "Seen from a friendly eye", "から好意的な目で見られて"), # MACHINE_TRANSLATED
    0x001D0718: Data(DataType.String, 24, "What I returned with a light greeting", "軽い挨拶で返したこと"), # MACHINE_TRANSLATED
    0x001D0730: Data(DataType.String, 20, "With a friendly eye", "から好意的な目で"), # MACHINE_TRANSLATED
    0x001D0744: Data(DataType.String, 28, "ignoring the stares", "見られたが、無視したこと"),
    0x001D0760: Data(DataType.String, 20, "Casually saw", "を何気なく見たこと"), # MACHINE_TRANSLATED
    0x001D0774: Data(DataType.String, 24, "Casually seen from", "から何気なく見られて"), # MACHINE_TRANSLATED
    0x001D078C: Data(DataType.String, 24, "Awkward thoughts", "気まずい思いをしたこと"), # MACHINE_TRANSLATED
    0x001D07A4: Data(DataType.String, 24, "I was casually seen from", "から何気なく見られたが"), # MACHINE_TRANSLATED
    0x001D07BC: Data(DataType.String, 24, "To look maliciously", "を悪意を込めて見たこと"), # MACHINE_TRANSLATED
    0x001D07D4: Data(DataType.String, 28, "Because I felt bad intentions at the line of sight of", "の視線に悪意を感じたので"), # MACHINE_TRANSLATED
    0x001D07F0: Data(DataType.String, 16, "glaring back", "睨み返したこと"),
    0x001D0800: Data(DataType.String, 20, "averting their eyes", "目を逸らしたこと"),
    0x001D0814: Data(DataType.String, 24, "I felt malicious in the eyes of", "の視線に悪意を感じたが"), # MACHINE_TRANSLATED
    0x001D082C: Data(DataType.String, 20, "flaring up at", "食って掛かったこと"),
    0x001D0840: Data(DataType.String, 24, "Smiling at", "に対して微笑んだこと"), # MACHINE_TRANSLATED
    0x001D0858: Data(DataType.String, 24, "Consent to", "に対して同意したこと"), # MACHINE_TRANSLATED
    0x001D0870: Data(DataType.String, 20, "nodding along", "相づちを打ったこと"),
    0x001D0884: Data(DataType.String, 24, "responding indifferently", "気の無い返事をしたこと"),
    0x001D089C: Data(DataType.String, 24, "Vaguely against", "に対して、あいまいに"), # MACHINE_TRANSLATED
    0x001D08B4: Data(DataType.String, 24, "Having a deceptive attitude", "誤魔化す態度をしたこと"), # MACHINE_TRANSLATED
    0x001D08CC: Data(DataType.String, 24, "averting their eyes from", "から目を逸らしたこと"),
    0x001D08E4: Data(DataType.String, 16, "It's empty", "に、うわの空な"), # MACHINE_TRANSLATED
    0x001D08F4: Data(DataType.String, 16, "Having an attitude", "態度をしたこと"), # MACHINE_TRANSLATED
    0x001D0904: Data(DataType.String, 16, "being huffy", "ムッとしたこと"),
    0x001D0914: Data(DataType.String, 20, "Against", "に対して、しらけた"), # MACHINE_TRANSLATED
    0x001D0928: Data(DataType.String, 20, "sagging with disappointment", "肩を落としたこと"),
    0x001D093C: Data(DataType.String, 16, "hanging their head", "うなだれたこと"),
    0x001D094C: Data(DataType.String, 20, "feeling let down", "がっかりしたこと"),
    0x001D0960: Data(DataType.String, 16, "being bashful", "はにかんだこと"),
    0x001D0970: Data(DataType.String, 20, "Worried about", "の心配をしたこと"), # MACHINE_TRANSLATED
    0x001D0984: Data(DataType.String, 20, "feeling unsettled", "不快感を持ったこと"),
    0x001D0998: Data(DataType.String, 20, "Kindly", "の事を、好意的に"), # MACHINE_TRANSLATED
    0x001D09AC: Data(DataType.String, 12, "sensing", "感じたこと"),
    0x001D09B8: Data(DataType.String, 16, "Be flirting", "ひるんだこと"), # MACHINE_TRANSLATED
    0x001D09C8: Data(DataType.String, 24, "Self-destruction promotion program", "自滅促進プログラムの"), # MACHINE_TRANSLATED
    0x001D09E0: Data(DataType.String, 20, "What was created", "作成を行ったこと"), # MACHINE_TRANSLATED
    0x001D09F4: Data(DataType.String, 24, "Self-destruction promotion program", "自滅促進プログラムを"), # MACHINE_TRANSLATED
    0x001D0A0C: Data(DataType.String, 16, "What you did", "実行したこと"), # MACHINE_TRANSLATED
    0x001D0A1C: Data(DataType.String, 20, "unison training with", "と、ユニゾン訓練を"),
    0x001D0A30: Data(DataType.String, 16, "To peel off the seal", "シールはがしに"), # MACHINE_TRANSLATED
    0x001D0A40: Data(DataType.String, 20, "challenging", "チャレンジしたこと"),
    0x001D0A54: Data(DataType.String, 20, "a sheet of stickers", "シールのシートを"),
    0x001D0A68: Data(DataType.String, 20, "To apply for the prize", "に、懸賞の応募を"), # MACHINE_TRANSLATED
    0x001D0A7C: Data(DataType.String, 24, "Of a business trip plan to Kyoto", "京都への出張計画書の"), # MACHINE_TRANSLATED
    0x001D0A94: Data(DataType.String, 24, "Having called Aoba", "青葉に電話をかけたこと"), # MACHINE_TRANSLATED
    0x001D0AAC: Data(DataType.String, 24, "Invited to date", "をデートに誘ったこと"), # MACHINE_TRANSLATED
    0x001D0AC4: Data(DataType.String, 20, "Questions", "を問いただしたこと"), # MACHINE_TRANSLATED
    0x001D0AD8: Data(DataType.String, 16, "Have invited", "を誘ったこと"), # MACHINE_TRANSLATED
    0x001D0AE8: Data(DataType.String, 20, "Releasing power", "力を解放したこと"), # MACHINE_TRANSLATED
    0x001D0AFC: Data(DataType.String, 20, "Heard the condition of", "の容態を聞いたこと"), # MACHINE_TRANSLATED
    0x001D0B10: Data(DataType.String, 24, "In, Ray was hospitalized", "に、レイが入院したが"), # MACHINE_TRANSLATED
    0x001D0B28: Data(DataType.String, 20, "Rei is hospitalized", "に、レイが入院して"),
    0x001D0B3C: Data(DataType.String, 24, "Asuka was hospitalized", "に、アスカが入院したが"), # MACHINE_TRANSLATED
    0x001D0B54: Data(DataType.String, 24, "Asuka is hospitalized", "に、アスカが入院して"),
    0x001D0B6C: Data(DataType.String, 24, "Touji was hospitalized", "に、トウジが入院したが"), # MACHINE_TRANSLATED
    0x001D0B84: Data(DataType.String, 24, "Toji is hospitalized", "に、トウジが入院して"),
    0x001D0B9C: Data(DataType.String, 24, "Then, Kaworu was hospitalized", "に、カヲルが入院したが"), # MACHINE_TRANSLATED
    0x001D0BB4: Data(DataType.String, 24, "Kaworu is hospitalized", "に、カヲルが入院して"),
    0x001D0BCC: Data(DataType.String, 24, "Eva repair efficiency review", "エヴァ修理効率見直しの"),
    0x001D0BE4: Data(DataType.String, 24, "drawing up a new opinion brief", "意見書作成を行ったこと"),
    0x001D0BFC: Data(DataType.String, 32, "Eva support facility restoration efficiency review", "エヴァ支援施設修復効率見直しの"), # MACHINE_TRANSLATED
    0x001D0C1C: Data(DataType.String, 28, "Nerv personnel defense facility strengthening", "ネルフ対人防衛施設増強の"),
    0x001D0C38: Data(DataType.String, 20, "Change of vending machine supplier", "自販機業者変更の"),
    0x001D0C4C: Data(DataType.String, 20, "Illegal Map Name", "イリーガルマップ名"),
    0x001D0C60: Data(DataType.String, 24, "in the apartment's living room", "マンションのリビングで"),
    0x001D0C78: Data(DataType.String, 24, "in the kitchen", "ダイニングキッチンで"),
    0x001D0C90: Data(DataType.String, 16, "in Shinji's room", "シンジの部屋で"),
    0x001D0CA0: Data(DataType.String, 16, "in Asuka's room", "アスカの部屋で"),
    0x001D0CB0: Data(DataType.String, 16, "in Misato's room", "ミサトの部屋で"),
    0x001D0CC0: Data(DataType.String, 24, "in the apartment's bathroom", "マンションの洗面所で"),
    0x001D0CD8: Data(DataType.String, 16, "in the Commander's office", "総司令公務室で"),
    0x001D0CE8: Data(DataType.String, 20, "in the Nerv Command Center", "ネルフの発令所で"),
    0x001D0CFC: Data(DataType.String, 20, "in Misato's office", "ミサトの執務室で"),
    0x001D0D10: Data(DataType.String, 16, "at the Nerv cafeteria", "ネルフの食堂で"),
    0x001D0D20: Data(DataType.String, 20, "in Ritsuko's laboratory", "リツコの研究室で"),
    0x001D0D34: Data(DataType.String, 16, "in Kaji's private room", "加持の個室で"),
    0x001D0D44: Data(DataType.String, 24, "at the Nerv vending machine corner", "ネルフ自販機コーナーで"),
    0x001D0D5C: Data(DataType.String, 24, "at (unnamed map: backup 1)", "（呼称未定義予備１）で"),
    0x001D0D74: Data(DataType.String, 20, "in the Nerv public bath", "ネルフの大浴場で"),
    0x001D0D88: Data(DataType.String, 20, "in Central Dogma", "セントラルドグマで"),
    0x001D0D9C: Data(DataType.String, 20, "at Rei's apartment", "レイのマンションで"),
    0x001D0DB0: Data(DataType.String, 16, "in the school classroom", "学校の教室で"),
    0x001D0DC0: Data(DataType.String, 16, "in the school hallway", "学校の廊下で"),
    0x001D0DD0: Data(DataType.String, 12, "at the convenience store", "コンビニで"),
    0x001D0DDC: Data(DataType.String, 16, "at the ruins on the surface", "地上の廃墟で"),
    0x001D0DEC: Data(DataType.String, 12, "in the labyrinth of the heart", "心の迷宮で"),
    0x001D0DF8: Data(DataType.String, 20, "at Unit-01's Cage", "初号機のケイジで"),
    0x001D0E0C: Data(DataType.String, 36, "at (unnamed map: Eva cage)", "（呼称未定義マップＥＶＡケイジ）で"),
    0x001D0E30: Data(DataType.String, 32, "at (unnamed map: backup quarters)", "（呼称未定義マップ予備宿舎）で"),
    0x001D0E50: Data(DataType.String, 32, "at (unnamed map: backup 5)", "（呼称未定義マップ予備５）で"),
    0x001D0E70: Data(DataType.String, 16, "at Tokyo-3", "第３新東京市で"),
    0x001D0E80: Data(DataType.String, 16, "at Nerv Headquarters", "ネルフ本部で"),
    0x001D0E90: Data(DataType.String, 8, "at their own house", "自宅で"),
    0x001D0E98: Data(DataType.String, 28, "at (unnamed map: their own room)", "（呼称未定義マップ自室）で"),
    0x001D0EB4: Data(DataType.String, 12, "on the veranda", "ベランダで"),
    0x001D0EC0: Data(DataType.String, 20, "outside the apartment", "マンションの外で"),
    0x001D0ED4: Data(DataType.String, 12, "somewhere", "どこかで"),
    0x001D0EE0: Data(DataType.String, 32, "at (unnamed map: backup 6)", "（呼称未定義マップ予備６）で"),
    0x001D0F00: Data(DataType.String, 24, "at Misato's apartment", "ミサトのマンションで"),
    0x001D0F18: Data(DataType.String, 16, "outside the convenience store", "コンビニの外で"),
    0x001D0F28: Data(DataType.String, 16, "on the roof of the school", "学校の屋上で"),
    0x001D0F38: Data(DataType.String, 16, "at the highland park", "高台の公園で"),
    0x001D0F48: Data(DataType.String, 16, "at New Hakone-Yumoto Station", "新箱根湯本駅で"),
    0x001D0F58: Data(DataType.String, 20, "at Unit-00's Cage", "零号機のケイジで"),
    0x001D0F6C: Data(DataType.String, 20, "at Unit-02's Cage", "弐号機のケイジで"),
    0x001D0F80: Data(DataType.String, 20, "at Unit-03's Cage", "参号機のケイジで"),
    0x001D0F94: Data(DataType.String, 20, "at Unit-04's Cage", "四号機のケイジで"),
    0x001D0FA8: Data(DataType.String, 20, "nearby Nerv H.Q.", "ネルフの本部脇で"),
    0x001D0FBC: Data(DataType.String, 16, "at Kaworu's quarters", "カヲルの宿舎で"),
    0x001D0FCC: Data(DataType.String, 16, "at Kaji's quarters", "加持の宿舎で"),
    0x001D0FDC: Data(DataType.String, 16, "at Shinji's quarters", "シンジの宿舎で"),
    0x001D0FEC: Data(DataType.String, 16, "at Rei's quarters", "レイの宿舎で"),
    0x001D0FFC: Data(DataType.String, 16, "at Asuka's quarters", "アスカの宿舎で"),
    0x001D100C: Data(DataType.String, 16, "at Misato's quarters", "ミサトの宿舎で"),
    0x001D101C: Data(DataType.String, 16, "at Ritsuko's quarters", "リツコの宿舎で"),
    0x001D102C: Data(DataType.String, 16, "at Toji's quarters", "トウジの宿舎で"),
    0x001D103C: Data(DataType.String, 16, "at Aoba's quarters", "青葉の宿舎で"),
    0x001D104C: Data(DataType.String, 16, "at Hyuga's quarters", "日向の宿舎で"),
    0x001D105C: Data(DataType.String, 16, "at Maya's quarters", "マヤの宿舎で"),
    0x001D106C: Data(DataType.String, 16, "at Fuyutsuki's quarters", "冬月の宿舎で"),
    0x001D107C: Data(DataType.String, 20, "at Gendo's quarters", "ゲンドウの宿舎で"),
    0x001D1090: Data(DataType.String, 20, "on the way to school", "学校への通学路で"),
    0x001D10A4: Data(DataType.String, 24, "in an escalator at H.Q.", "本部のエスカレーターで"),
    0x001D10BC: Data(DataType.String, 16, "at Test Site 7", "第７実験場で"),
    0x001D10CC: Data(DataType.String, 12, "at the test site", "実験場で"),
    0x001D10D8: Data(DataType.String, 16, "at the firearms training center", "射撃訓練所で"),
    0x001D10E8: Data(DataType.String, 20, "at the entrance of the executive staff quarters", "幹部宿舎前の通路で"),
    0x001D10FC: Data(DataType.String, 20, "at the entrance of the personnel quarters", "職員宿舎前の通路で"),
    0x001D1110: Data(DataType.String, 24, "at the entrance of the pilot quarters", "パイロット宿舎前廊下で"),
    0x001D1128: Data(DataType.String, 32, "at (unnamed map background: ruins)", "（呼称未定義マップ遠景廃墟）で"),
    0x001D1148: Data(DataType.String, 32, "at (unnamed map background: rooftop)", "（呼称未定義マップ遠景屋上）で"),
    0x001D1168: Data(DataType.String, 32, "at (unnamed map background: park)", "（呼称未定義マップ遠景公園）で"),
    0x001D1188: Data(DataType.String, 32, "at (unnamed map background: station)", "（呼称未定義マップ遠景駅）で"),
    0x001D11A8: Data(DataType.String, 12, "a moment ago", "たった今"),
    0x001D11B4: Data(DataType.String, 12, "a little earlier", "ちょっと前"),
    0x001D11C0: Data(DataType.String, 12, "one hour ago", "１時間前"),
    0x001D11CC: Data(DataType.String, 12, "two hours ago", "２時間前"),
    0x001D11D8: Data(DataType.String, 8, "yesterday", "昨日"),
    0x001D11E0: Data(DataType.String, 12, "the day before yesterday", "おととい"),
    0x001D11EC: Data(DataType.String, 12, "about three days ago", "３日程前"),
    0x001D11F8: Data(DataType.String, 12, "about a week ago", "１週間程前"),
    0x001D1204: Data(DataType.String, 12, "about two weeks ago", "２週間程前"),
    0x001D1210: Data(DataType.String, 12, "about a month ago", "ひと月程前"),
    0x001D121C: Data(DataType.String, 12, "about two months ago", "ふた月程前"),
    0x001D1228: Data(DataType.String, 8, "half a year ago", "半年前"),
    0x001D1230: Data(DataType.String, 8, "one year ago", "１年前"),
    0x001D1238: Data(DataType.String, 12, "a very long time ago", "ずいぶん昔"),
    0x001D1244: Data(DataType.String, 8, "the middle of the night", "夜中"),
    0x001D124C: Data(DataType.String, 8, "early morning", "早朝"),
    0x001D1254: Data(DataType.String, 8, "this morning", "今朝"),
    0x001D125C: Data(DataType.String, 8, "daytime", "昼間"),
    0x001D1264: Data(DataType.String, 8, "evening", "夕方"),
    0x001D126C: Data(DataType.String, 8, "tonight", "今夜"),
    0x001D1274: Data(DataType.String, 8, "earlier", "以前"),
    0x001D127C: Data(DataType.String, 16, "Remember well", "よく思い出す"),
    0x001D128C: Data(DataType.String, 20, "remember really well", "よくよく思い出す"),
    0x001D12A0: Data(DataType.String, 24, "Remember really, really well", "よくよくよく思い出す"),
    0x001D12B8: Data(DataType.String, 16, "Remember in earnest", "真剣に思い出す"),
    0x001D12C8: Data(DataType.String, 20, "Rethink this from the top", "もう一度考え直す"),
    0x001D12DC: Data(DataType.String, 24, "$a %s something that happened long ago.", "$aは、昔の出来事を%s。"),
    0x001D12F4: Data(DataType.String, 36, "But %s\nI didn't understand well.", "しかし%sは\nよく理解できなかった。"), # MACHINE_TRANSLATED
    0x001D1318: Data(DataType.String, 36, "But %s\nI didn't hear well.", "しかし%sは\nうまく聞き取れなかった。"), # MACHINE_TRANSLATED
    0x001D133C: Data(DataType.String, 32, "But %s didn't understand it well.", "しかし%sは\nよくわからなかった。"),
    0x001D135C: Data(DataType.String, 8, [36, 98, 130, 201, 0, 0, 0, 0], "$bに"),
    0x001D1364: Data(DataType.String, 4, [130, 170, 0, 0], "が"),
    0x001D1368: Data(DataType.String, 44, "$a is %s,\n%s happening in %s. $n%s%s%s\n%s%s.", "$aは%s、\n%sの出来事を%s。$n%s%s%s\n%s%sを。"), # MACHINE_TRANSLATED
    0x001D13A4: Data(DataType.String, 4, "...", "…"),
    0x001D13A8: Data(DataType.String, 8, "and company", "たち"),
    0x001D13B0: Data(DataType.String, 8, "myself", "自分"),
    0x001D13B8: Data(DataType.String, 8, "right here", "ここで"),
    0x001D1438: Data(DataType.String, 20, "● Battle Play Start", "●戦闘プレイ開始"),
    0x001D144C: Data(DataType.String, 20, "● Battle Demo Test", "●戦闘デモテスト"),
    0x001D1460: Data(DataType.String, 16, "● Adjusted Play", "●調整プレイ"),
    0x001D1470: Data(DataType.String, 16, "● Demo Check", "●デモチェック"),
    0x001D1480: Data(DataType.String, 20, "● Debug Switch", "●デバッグスイッチ"),
    0x001D1494: Data(DataType.String, 20, "● Game Flag Settings", "●ゲームフラグ設定"),
    0x001D14A8: Data(DataType.String, 24, "● Hideaki Anno Mode Settings", "●庵野監督モード設定"),
    0x001D14C0: Data(DataType.String, 24, "● Display Test Menu", "●表示テストメニュー"),
    0x001D14D8: Data(DataType.String, 28, "● Event Test Menu", "●イベントテストメニュー"),
    0x001D14F4: Data(DataType.String, 24, "● Screen Test Menu", "●画面テストメニュー"),
    0x001D150C: Data(DataType.String, 24, "● Misc. Test Menu", "●その他テストメニュー"),
    0x001D1524: Data(DataType.String, 20, "● Misato 1 Day Vacation", "●ミサト１日やすみ"),
    0x001D1538: Data(DataType.String, 16, "● Option", "●オプション"),
    0x001D1548: Data(DataType.String, 12, "● Test", "●テスト"),
    0x001D1554: Data(DataType.String, 8, "○%s", "○%s"),
    0x001D155C: Data(DataType.String, 8, "○%sDays", "○%s日"),
    0x001D1574: Data(DataType.String, 20, "● Narrow Window", "●狭いウインドウ"),
    0x001D1588: Data(DataType.String, 16, "● Window Frame", "●ウインドウ枠"),
    0x001D1598: Data(DataType.String, 20, "● Unit Plate", "●ユニットプレート"),
    0x001D15AC: Data(DataType.String, 24, "● Status Display Test", "●ステータス表示テスト"),
    0x001D15C4: Data(DataType.String, 24, "● Internal Power Display Test", "●体内電源表示テスト"),
    0x001D15DC: Data(DataType.String, 24, "● Unit Name Display Test", "●ユニット名表示テスト"),
    0x001D15F4: Data(DataType.String, 24, "● Unit obj Display Test", "●ユニットobj表示テスト"),
    0x001D160C: Data(DataType.String, 24, "● Demo Screen Test", "●デモスクリーンテスト"),
    0x001D1624: Data(DataType.String, 16, "● Guide Test", "●ガイドテスト"),
    0x001D1634: Data(DataType.String, 12, "● FAN Test", "●FANテスト"),
    0x001D1640: Data(DataType.String, 16, "● WING Test", "●WINGテスト"),
    0x001D1650: Data(DataType.String, 24, "● Assist Display Test", "●アシスト表示テスト"),
    0x001D1668: Data(DataType.String, 20, "● Event 1 Test", "●イベント１テスト"),
    0x001D167C: Data(DataType.String, 20, "● Event 2 Test", "●イベント２テスト"),
    0x001D1690: Data(DataType.String, 20, "● Kaworu Dialogue Test", "●カヲル問答テスト"),
    0x001D16A4: Data(DataType.String, 24, "● Leliel Dialogue Test", "●レリエル問答テスト"),
    0x001D16BC: Data(DataType.String, 28, "● Non-playable Battle Demo Test", "●非プレイ戦闘デモテスト"),
    0x001D16D8: Data(DataType.String, 24, "● Angel Advent Demo Test", "●使徒出現デモテスト"),
    0x001D16F0: Data(DataType.String, 16, "● tevent Test", "●teventテスト"),
    0x001D1700: Data(DataType.String, 16, "● cevent Test", "●ceventテスト"),
    0x001D1710: Data(DataType.String, 20, "● bt2 Event Test", "●bt2イベントテスト"),
    0x001D1724: Data(DataType.String, 20, "● Report Test", "●レポートテスト"),
    0x001D1738: Data(DataType.String, 20, "● Information Screen Test", "●情報画面テスト"),
    0x001D174C: Data(DataType.String, 20, "● Results Screen Test", "●結果画面テスト"),
    0x001D1760: Data(DataType.String, 24, "● Battle Transmissions Screen Test", "●作戦伝達画面テスト"),
    0x001D1778: Data(DataType.String, 24, "● Battle Settings Screen Test", "●作戦設定画面テスト"),
    0x001D1790: Data(DataType.String, 16, "● IM319 Testト", "●IM319テスト"),
    0x001D17A0: Data(DataType.String, 16, "● IM660 Test", "●IM660テスト"),
    0x001D17B0: Data(DataType.String, 16, "● IM003 Test", "●IM003テスト"),
    0x001D17C0: Data(DataType.String, 20, "● Player Standby Screen", "●プレーヤ待機画面"),
    0x001D17D4: Data(DataType.String, 16, "● Eyecatch", "●アイキャッチ"),
    0x001D17E4: Data(DataType.String, 12, "● Studying", "●お勉強"),
    0x001D17F0: Data(DataType.String, 16, "● Equipment Information Screen", "●装備情報画面"),
    0x001D1800: Data(DataType.String, 20, "● \"_ Days Later\" Screen", "●「○日後」画面"),
    0x001D1814: Data(DataType.String, 20, "● Impulse Text Test", "●IMテキストテスト"),
    0x001D1828: Data(DataType.String, 16, "● Memory Test", "●記憶テスト"),
    0x001D1838: Data(DataType.String, 20, "● Automated Deployment Test", "●自動配置テスト"),
    0x001D184C: Data(DataType.String, 16, "● Character String Test", "●文字列テスト"),
    0x001D185C: Data(DataType.String, 20, "● Launch Demo Test", "●出撃デモテスト"),
    0x001D1870: Data(DataType.String, 24, "● View Unit Data", "●ユニットデータを見る"),
    0x001D1888: Data(DataType.String, 24, "● View Angel Para-Calculation", "●使徒パラ計算を見る"),
    0x001D18A0: Data(DataType.String, 20, "● Weapon Deployment Test", "●武器配備テスト"),
    0x001D18B4: Data(DataType.String, 20, "● Equipment List Test", "●装備リストテスト"),
    0x001D18C8: Data(DataType.String, 24, "● Battle Impulse List Test", "●戦闘IMリストテスト"),
    0x001D18E0: Data(DataType.String, 20, "● btCityPageOfArea", "●btCityPageOfArea"),
    0x001D1920: Data(DataType.String, 24, "Sachiel (Scenario 1)", "サキエル(シナリオ１)"),
    0x001D1938: Data(DataType.String, 28, "Simulation Battle (1st Time)", "シミュレーション戦(１回目)"),
    0x001D1954: Data(DataType.String, 28, "Simulation Battle (2nd Time)", "シミュレーション戦(２回目)"),
    0x001D1970: Data(DataType.String, 28, "Shamshel (Scenario 1)", "シャムシエル(シナリオ１)"),
    0x001D198C: Data(DataType.String, 24, "Sachiel (Playing As Misato)", "サキエル(ミサトプレイ)"),
    0x001D19A4: Data(DataType.String, 12, "Sachiel", "サキエル"),
    0x001D19B0: Data(DataType.String, 16, "Shamshel", "シャムシエル"),
    0x001D19C0: Data(DataType.String, 12, "Ramiel", "ラミエル"),
    0x001D19CC: Data(DataType.String, 12, "Gaghiel", "ガギエル"),
    0x001D19D8: Data(DataType.String, 16, "Israfel", "イスラフェル"),
    0x001D19E8: Data(DataType.String, 16, "Sandalphon", "サンダルフォン"),
    0x001D19F8: Data(DataType.String, 12, "Matariel", "マトリエル"),
    0x001D1A04: Data(DataType.String, 16, "Sahaquiel", "サハクイエル"),
    0x001D1A14: Data(DataType.String, 12, "Leliel", "レリエル"),
    0x001D1A20: Data(DataType.String, 20, "Bardiel (Matsushiro)", "バルディエル(松代)"),
    0x001D1A34: Data(DataType.String, 24, "Bardiel (Nerv)", "バルディエル(ネルフ)"),
    0x001D1A4C: Data(DataType.String, 12, "Zeruel", "ゼルエル"),
    0x001D1A58: Data(DataType.String, 12, "Arael", "アラエル"),
    0x001D1A64: Data(DataType.String, 16, "Armisael", "アルミサエル"),
    0x001D1A74: Data(DataType.String, 12, "Tabris", "ダブリス"),
    0x001D1A80: Data(DataType.String, 8, "Mass Production Unit", "量産機"),
    0x001D1A88: Data(DataType.String, 8, "J.A.", "ＪＡ"),
    0x001D1A90: Data(DataType.String, 20, "Sachiel Fight (Misato)", "サキエル戦(ミサト)"),
    0x001D1AA4: Data(DataType.String, 20, "○ Debug Switch", "○デバッグスイッチ"),
    0x001D1AB8: Data(DataType.String, 20, "○ Hideaki Anno Mode:%s", "○庵野監督モード:%s"),
    0x001D1ACC: Data(DataType.String, 20, "○ Game Flag Settings", "○ゲームフラグ設定"),
    0x001D1AE0: Data(DataType.String, 16, "○ Background Type:%s", "○背景タイプ:%s"),
    0x001D1AF0: Data(DataType.String, 20, "○ Player Selection:%s", "○プレーヤ選択:%s"),
    0x001D1B04: Data(DataType.String, 16, "● Begin Playing", "●プレイ開始"),
    0x001D1B14: Data(DataType.String, 12, "○ Angel:%s", "○使徒:%s"),
    0x001D1B20: Data(DataType.String, 16, "○ Number of stories: %d…%s", "○話数:%d…%s"), # MACHINE_TRANSLATED
    0x001D1B30: Data(DataType.String, 12, "○ Sortie: %s", "○出撃:%s"), # MACHINE_TRANSLATED
    0x001D1B3C: Data(DataType.String, 32, "○ Tokyo-3 Facility Operating Rate", "○第３新東京市の施設稼動率:%d％"),
    0x001D1B5C: Data(DataType.String, 32, "○ Geofront facility utilization rate: %d%", "○ジオフロントの施設稼動率:%d％"), # MACHINE_TRANSLATED
    0x001D1BB4: Data(DataType.String, 12, "AT change", "　ＡＴ変更"), # MACHINE_TRANSLATED
    0x001D1BD8: Data(DataType.String, 32, "Endurance %d, Synchro %d, Speed %d M/sec", "耐久%d,シンクロ%d,速度%dM/秒"), # MACHINE_TRANSLATED
    0x001D1C00: Data(DataType.String, 16, "AT + intensity correction", "ＡＴ＋強度補正"), # MACHINE_TRANSLATED
    0x001D1C10: Data(DataType.String, 16, "AT-strength correction", "ＡＴ−強度補正"), # MACHINE_TRANSLATED
    0x001D1C20: Data(DataType.String, 32, "Whose parameters do you want to change?", "誰のパラメータを変更しますか？"), # MACHINE_TRANSLATED
    0x001D1C40: Data(DataType.String, 32, "Which parameter do you want to change?", "どのパラメータを変更しますか？"), # MACHINE_TRANSLATED
    0x001D1C64: Data(DataType.String, 28, "Who are you going to do?", "誰に対して行ないますか？"), # MACHINE_TRANSLATED
    0x001D1C80: Data(DataType.String, 36, "Please specify the memory strength ratio in%", "記憶強度倍率を％で指定して下さい"), # MACHINE_TRANSLATED
    0x001D1CB8: Data(DataType.String, 8, "Shinji", "シンジ"),
    0x001D1CC0: Data(DataType.String, 8, "Asuka", "アスカ"),
    0x001D1CC8: Data(DataType.String, 8, "Rei", "レイ"),
    0x001D1CD0: Data(DataType.String, 8, "Misato", "ミサト"),
    0x001D1CD8: Data(DataType.String, 12, "Gendo", "ゲンドウ"),
    0x001D1CE4: Data(DataType.String, 8, "Fuyutsuki", "冬月"),
    0x001D1CEC: Data(DataType.String, 8, "Ritsuko", "リツコ"),
    0x001D1CF4: Data(DataType.String, 8, "Maya", "マヤ"),
    0x001D1CFC: Data(DataType.String, 8, "Hyuga", "日向"),
    0x001D1D04: Data(DataType.String, 8, "Aoba", "青葉"),
    0x001D1D0C: Data(DataType.String, 8, "Kaji", "加持"),
    0x001D1D14: Data(DataType.String, 8, "Hikari", "ヒカリ"),
    0x001D1D1C: Data(DataType.String, 8, "Toji", "トウジ"),
    0x001D1D24: Data(DataType.String, 12, "Kensuke", "ケンスケ"),
    0x001D1D30: Data(DataType.String, 8, "Kaworu", "カヲル"),
    0x001D1D38: Data(DataType.String, 12, "Pen Pen", "ペンペン"),
    0x001D1D54: Data(DataType.String, 8, "A.T.", "ＡＴ"),
    0x001D1D5C: Data(DataType.String, 56, "Friendship to %-8s %6d\nLove for %-8s %6d\nDear love for %-8s %6d\n", "%-8sへの友情　%6d\n%-8sへの性愛　%6d\n%-8sへの親愛　%6d\n"), # MACHINE_TRANSLATED
    0x001D1DF8: Data(DataType.String, 28, "All Clear Ending", "オールクリア・エンディング"),
    0x001D1E14: Data(DataType.String, 32, "Pilot Quit Ending", "パイロット辞めたエンディング"),
    0x001D1E34: Data(DataType.String, 32, "Game Over Ending", "ゲームオーバー・エンディング"),
    0x001D1ED4: Data(DataType.String, 8, "%l%s％", "%l%s％"),
    0x001D1F00: Data(DataType.String, 20, "%1iGo Back　%2iGo Back", "%1i戻る　%2i戻る"),
    0x001D1F58: Data(DataType.String, 24, "%1iDecide　%2iCancel", "%1i決定　%2iキャンセル"),
    0x001D1FA4: Data(DataType.String, 8, "To Va", "ヴァへ"), # MACHINE_TRANSLATED
    0x001D1FB8: Data(DataType.String, 8, "Battle planning", "戦立案"), # MACHINE_TRANSLATED
    0x001D1FE4: Data(DataType.String, 8, "%1i selection", "%1i選択"), # MACHINE_TRANSLATED
    0x001D2038: Data(DataType.String, 16, "Eva Unit-00", "EVA-00　零号機"),
    0x001D2048: Data(DataType.String, 16, "Eva Unit-01", "EVA-01　初号機"),
    0x001D2058: Data(DataType.String, 16, "Eva Unit-02", "EVA-02　弐号機"),
    0x001D2068: Data(DataType.String, 16, "Eva Unit-03", "EVA-03　参号機"),
    0x001D2078: Data(DataType.String, 16, "Eva Unit-04", "EVA-04　四号機"),
    0x001D2088: Data(DataType.String, 12, "Impossible", "ありえない"), # MACHINE_TRANSLATED
    0x001D2120: Data(DataType.String, 16, "Operation transmission screen", "作戦伝達画面"), # MACHINE_TRANSLATED
    0x001D2160: Data(DataType.String, 20, "%1i Eva placement confirmation", "%1iエヴァ配置確認へ"), # MACHINE_TRANSLATED
    0x001D21E4: Data(DataType.String, 32, "In hospital\n%s is\nIt was summoned.", "入院中の\n%sは\n召喚されました。"), # MACHINE_TRANSLATED
    0x001D2250: Data(DataType.String, 16, "Sortie members", "出撃メンバー"), # MACHINE_TRANSLATED
    0x001D2264: Data(DataType.String, 12, "Damage", "ダメージ"),
    0x001D2278: Data(DataType.String, 12, "\nUnited Nations Army: %d", "\n国連軍:%d"), # MACHINE_TRANSLATED
    0x001D2284: Data(DataType.String, 20, "\nTokyo-3:%d", "\n第３新東京市:%d"),
    0x001D23A4: Data(DataType.String, 16, "Automatic operation settings", "自動作戦設定"), # MACHINE_TRANSLATED
    0x001D23EC: Data(DataType.String, 8, "To Va", "ヴァへ"), # MACHINE_TRANSLATED
    0x001D23FC: Data(DataType.String, 8, "○ %s", "○%s"),
    0x001D2404: Data(DataType.String, 16, "○ Eva%s、", "○エヴァ%s、"),
    0x001D2414: Data(DataType.String, 12, "○ Hospitalization: %s", "○入院:%s"), # MACHINE_TRANSLATED
    0x001D2420: Data(DataType.String, 16, "● View screen", "●画面を見る"),
    0x001D255C: Data(DataType.String, 40, "The battle is not over! I have a bug", "戦闘は終了していません！バグ入ってます"), # MACHINE_TRANSLATED
    0x001D2584: Data(DataType.String, 24, "Reconciled with Kaworu", "カヲルと和解しました"), # MACHINE_TRANSLATED
    0x001D259C: Data(DataType.String, 20, "Defeated in battle", "戦闘に敗北しました"), # MACHINE_TRANSLATED
    0x001D25B0: Data(DataType.String, 24, "Killed Kaworu", "カヲルを殺害しました"), # MACHINE_TRANSLATED
    0x001D26CC: Data(DataType.String, 8, "Remaining Ammo %s", "残弾%s"),
    0x001D2790: Data(DataType.String, 20, "\nEndurance: %3d", "\n耐久力　　　:%3d"), # MACHINE_TRANSLATED
    0x001D27A4: Data(DataType.String, 20, "\nHayflick:%3d%", "\nヘイフリック:%3d％"),
    0x001D27B8: Data(DataType.String, 20, "\nSynch Ratio :%3d", "\nシンクロ率　:%3d％"),
    0x001D27CC: Data(DataType.String, 20, "\nA.T.F.   :%3d", "\nＡＴＦ　　　:%3d"),
    0x001D27E0: Data(DataType.String, 20, "\nNeutralization range: %3d", "\n中和レンジ　:%3d"), # MACHINE_TRANSLATED
    0x001D27F4: Data(DataType.String, 20, "\nMovement speed: %3d", "\n移動速度　　:%3d"), # MACHINE_TRANSLATED
    0x001D2808: Data(DataType.String, 20, "\nTurning speed: %3d", "\n旋回速度　　:%3d"), # MACHINE_TRANSLATED
    0x001D281C: Data(DataType.String, 20, "\nStrength: %3d", "\n戦力　　　　:%3d"), # MACHINE_TRANSLATED
    0x001D2830: Data(DataType.String, 20, "\nDamage distribution: %3d", "\nダメージ配分:%3d"), # MACHINE_TRANSLATED
    0x001D2844: Data(DataType.String, 28, "How to calculate the apostle's durability\n%S", "使徒の耐久力の計算方法\n　%s"), # MACHINE_TRANSLATED
    0x001D2860: Data(DataType.String, 32, "\nHow to calculate the apostle's movement speed\n%S", "\n使徒の移動速度の計算方法\n　%s"), # MACHINE_TRANSLATED
    0x001D2880: Data(DataType.String, 36, "\nHow to calculate the apostle's sync rate\n%S", "\n使徒のシンクロ率の計算方法\n　%s"), # MACHINE_TRANSLATED
    0x001D28A4: Data(DataType.String, 28, "\nHow to calculate the strength of the Apostles\n%S", "\n使徒の戦力の計算方法\n　%s"), # MACHINE_TRANSLATED
    0x001D28C8: Data(DataType.String, 8, "Unimplemented", "未実装"), # MACHINE_TRANSLATED
    0x001D2910: Data(DataType.String, 12, "Without equipment", "装備なし"), # MACHINE_TRANSLATED
    0x001D2920: Data(DataType.String, 8, "Remaining Ammo%s", "残弾%s"),
    0x001D2C28: Data(DataType.String, 24, "eva: Pallet Rifle", "eva:パレットライフル"),
    0x001D2C40: Data(DataType.String, 12, "eva: Punch A", "eva:パンチA"),
    0x001D2C4C: Data(DataType.String, 12, "eva: Punch B", "eva:パンチB"),
    0x001D2C58: Data(DataType.String, 12, "eva: Kick A", "eva:キックA"),
    0x001D2C64: Data(DataType.String, 12, "eva: Kick B", "eva:キックB"),
    0x001D2C70: Data(DataType.String, 28, "Israfel: Chop (Isolated)", "Israfel:チョップ（分離）"),
    0x001D2C8C: Data(DataType.String, 16, "eva: 2P Kick", "eva"),
    0x001D2C9C: Data(DataType.String, 24, "eva: Prog Knife Cutting", "eva:プログナイフ切る"),
    0x001D2CB4: Data(DataType.String, 24, "eva: Prog Knife Stabbing", "eva:プログナイフ突く"),
    0x001D2CCC: Data(DataType.String, 16, "Sachiel: Spear of Light", "Sachiel:光の槍"),
    0x001D2CDC: Data(DataType.String, 16, "Bardiel: Neck Throttle", "Bardiel:首絞め"),
    0x001D2CEC: Data(DataType.String, 20, "eva: Internal Power Suspended", "eva:内蔵電源停止"),
    0x001D2D00: Data(DataType.String, 16, "eva: Activity Suspended", "eva:活動停止"),
    0x001D2D10: Data(DataType.String, 24, "eva: Positron Rifle", "eva:ボジトロンライフル"),
    0x001D2D28: Data(DataType.String, 16, "Sachiel: Debut", "Sachiel:登場"),
    0x001D2D38: Data(DataType.String, 16, "Sachiel: Light Beam", "Sachiel:怪光線"),
    0x001D2D48: Data(DataType.String, 16, "Sachiel: Punch", "Sachiel:パンチ"),
    0x001D2D58: Data(DataType.String, 20, "Bardiel: Dropkick", "Bardiel:飛び蹴り"),
    0x001D2D6C: Data(DataType.String, 24, "eva: Sniper Rifle", "eva:スナイパーライフル"),
    0x001D2D84: Data(DataType.String, 12, "eva: Launch", "eva:出撃"),
    0x001D2D90: Data(DataType.String, 20, "Bardiel: Tackle", "Bardiel:タックル"),
    0x001D2DA4: Data(DataType.String, 20, "Bardiel: Bear Claw", "Bardiel:ベアクロー"),
    0x001D2DB8: Data(DataType.String, 16, "Bardiel: Kick", "Bardiel:キック"),
    0x001D2DC8: Data(DataType.String, 20, "Shamshel: Whip Pierce", "Shamshel:ムチ貫き"),
    0x001D2DDC: Data(DataType.String, 20, "Shamshel: Whip Strike", "Shamshel:ムチ叩き"),
    0x001D2DF0: Data(DataType.String, 24, "Israfel: Light Beam (Isolated)", "Israfel:怪光線(分離)"),
    0x001D2E08: Data(DataType.String, 24, "eva: Berserk/DP Kick A", "eva:暴走／ＤＰキックA"),
    0x001D2E20: Data(DataType.String, 24, "eva: Berserk/DP Kick Tackle", "eva:暴走／ＤＰタックル"),
    0x001D2E38: Data(DataType.String, 28, "eva: Berserk/DP Bear Claw", "eva:暴走／ＤＰベアクロー"),
    0x001D2E54: Data(DataType.String, 24, "eva: Berserk/DP Roundhouse Kick", "eva:暴走／ＤＰ回し蹴り"),
    0x001D2E6C: Data(DataType.String, 36, "eva: Positron Sniper Rifle", "eva:ポジトロンスナイパーライフル"),
    0x001D2E90: Data(DataType.String, 36, "eva: Unit-01 Berserk  Eyes Glowing, Roaring", "eva:初号機暴走　目が光り咆哮する"),
    0x001D2EB4: Data(DataType.String, 20, "eva: Unit-01 True Berserk??", "eva:初号機真・暴走"),
    0x001D2EC8: Data(DataType.String, 28, "eva: Unit-01 True Berserk  Movement", "eva:初号機真・暴走　移動"),
    0x001D2EE4: Data(DataType.String, 20, "Zeruel: Arm Cutter", "Zeruel:腕カッター"),
    0x001D2EF8: Data(DataType.String, 16, "Zeruel: Light Beam", "Zeruel:怪光線"),
    0x001D2F08: Data(DataType.String, 20, "Armisael: Stab", "Armisael:突き刺し"),
    0x001D2F1C: Data(DataType.String, 16, "Matriel: Lytic Fluid", "Matriel:溶解液"),
    0x001D2F2C: Data(DataType.String, 16, "Ramiel: Beam", "Ramiel:ビーム"),
    0x001D2F3C: Data(DataType.String, 16, "Shamshel:Entrance", "Shamshel:登場"),
    0x001D2F4C: Data(DataType.String, 12, "Tabris: Persuasion", "Tabris:説得"),
    0x001D2F58: Data(DataType.String, 24, "Tabris: Unit-01 Punch Attack", "Tabris:初号機パンチ攻撃"),
    0x001D2F70: Data(DataType.String, 24, "Tabris: Unit-02 Punch Attack", "Tabris:弐号機パンチ攻撃"),
    0x001D2F88: Data(DataType.String, 24, "Tabris: Unit-01 Knife Attack", "Tabris:初号機ナイフ攻撃"),
    0x001D2FA0: Data(DataType.String, 24, "Tabris: Unit-02 Knife Attack", "Tabris:弐号機ナイフ攻撃"),
    0x001D2FB8: Data(DataType.String, 24, "Tabris: Kaworu Crush", "Tabris:カオル握りつぶす"),
    0x001D2FD0: Data(DataType.String, 16, "Armisael: Entrance", "Armisael:登場"),
    0x001D2FE0: Data(DataType.String, 12, "Zeruel: Entrance", "Zeruel:登場"),
    0x001D2FEC: Data(DataType.String, 16, "Bardiel: Entrance", "Bardiel:登場"),
    0x001D2FFC: Data(DataType.String, 12, "Ramiel: Entrance", "Ramiel:登場"),
    0x001D3008: Data(DataType.String, 16, "Israfel: Entrance", "Israfel:登場"),
    0x001D3018: Data(DataType.String, 16, "Matriel:Entrance", "Matriel:登場"),
    0x001D3028: Data(DataType.String, 28, "eva: Throwing Spear of Longinus", "eva:ロンギヌスの槍を投げる"),
    0x001D3044: Data(DataType.String, 24, "eva: A.T. Field Neutralization", "eva:ＡＴフィールド中和"),
    0x001D305C: Data(DataType.String, 16, "neweva: Scratch", "neweva:引っ掻き"),
    0x001D306C: Data(DataType.String, 28, "neweva: Prog Dagger Ripper", "neweva:プログダガー切り裂き"), # MACHINE_TRANSLATED
    0x001D3088: Data(DataType.String, 28, "neweva: Prod Dagger Stab", "neweva:プログダガー突き刺し"), # MACHINE_TRANSLATED
    0x001D30A4: Data(DataType.String, 24, "neweva: Impact bolt", "neweva:インパクトボルト"), # MACHINE_TRANSLATED
    0x001D30BC: Data(DataType.String, 20, "eva: ATF attack", "eva:ＡＴＦアタック"), # MACHINE_TRANSLATED
    0x001D30D0: Data(DataType.String, 24, "eva: Mastema slash", "eva:マステマ斬り付け"), # MACHINE_TRANSLATED
    0x001D30E8: Data(DataType.String, 20, "eva: Mastema shooting", "eva:マステマ射撃"), # MACHINE_TRANSLATED
    0x001D30FC: Data(DataType.String, 16, "eva5: Mass Production Model Entrance", "eva5:量産機登場"),
    0x001D310C: Data(DataType.String, 12, "JA2: Entrance", "JA2:登場"),
    0x001D3118: Data(DataType.String, 20, "Eva: N2 Missile", "Eva:Ｎ２ミサイル"),
    0x001D312C: Data(DataType.String, 20, "Eva: Dual Saw", "Eva:デュアルソー"),
    0x001D3140: Data(DataType.String, 16, "JA2: Electric Shock Discharge", "JA2:電撃放電"),
    0x001D3150: Data(DataType.String, 20, "JA2: Hammer Attack", "JA2:ハンマー攻撃"),
    0x001D3164: Data(DataType.String, 24, "eva5: Cutting with Mass Production Model Sword", "eva5:量産機剣で切り裂き"),
    0x001D317C: Data(DataType.String, 20, "eva: Cutting with Sword", "eva:剣で切り裂き"),
    0x001D3190: Data(DataType.String, 24, "eva: True runaway ATF attack", "eva:真暴走用ATFアタック"), # MACHINE_TRANSLATED
    0x001D31A8: Data(DataType.String, 24, "eva5: Longinus Stab", "eva5:ロンギヌス突き刺し"), # MACHINE_TRANSLATED
    0x001D31C0: Data(DataType.String, 24, "eva: Magolo sword slash", "eva:マゴロクソード斬り"), # MACHINE_TRANSLATED
    0x001D31D8: Data(DataType.String, 24, "eva: Magolo sword butt", "eva:マゴロクソード突き"), # MACHINE_TRANSLATED
    0x001D31F0: Data(DataType.String, 12, "gagiel: Appeared", "gagiel:登場"), # MACHINE_TRANSLATED
    0x001D31FC: Data(DataType.String, 16, "gagiel: body hit", "gagiel:体当たり"), # MACHINE_TRANSLATED
    0x001D320C: Data(DataType.String, 16, "gagiel: bite", "gagiel:噛み付き"), # MACHINE_TRANSLATED
    0x001D321C: Data(DataType.String, 32, "eva02: Against Gaguiel Prog Knife", "eva02:対ガギエルプログナイフ"), # MACHINE_TRANSLATED
    0x001D323C: Data(DataType.String, 16, "sandalphon: appeared", "sandalphon:登場"), # MACHINE_TRANSLATED
    0x001D324C: Data(DataType.String, 20, "sandalphon: hitting", "sandalphon:体当たり"), # MACHINE_TRANSLATED
    0x001D3260: Data(DataType.String, 20, "sandalphon: hugging", "sandalphon:抱きつき"), # MACHINE_TRANSLATED
    0x001D3274: Data(DataType.String, 32, "eva_d: vs sandalphon prog knife", "eva_d:対sandalphonプログナイフ"), # MACHINE_TRANSLATED
    0x001D3294: Data(DataType.String, 12, "leliel: Appeared", "leliel:登場"), # MACHINE_TRANSLATED
    0x001D32A0: Data(DataType.String, 16, "leliel: Shadow rise", "leliel:影上昇"), # MACHINE_TRANSLATED
    0x001D32B0: Data(DataType.String, 28, "arael: Mental attack (large damage)", "arael:精神攻撃(ダメージ大)"), # MACHINE_TRANSLATED
    0x001D32CC: Data(DataType.String, 28, "arael: Mental attack (small damage)", "arael:精神攻撃(ダメージ小)"), # MACHINE_TRANSLATED
    0x001D32E8: Data(DataType.String, 8, "Downtown", "ビル街"),
    0x001D32F0: Data(DataType.String, 8, "City Outskirts", "郊外"),
    0x001D32F8: Data(DataType.String, 16, "GeoFront", "ジオフロント"),
    0x001D3308: Data(DataType.String, 8, "Underwater", "海中"),
    0x001D3310: Data(DataType.String, 8, "Magma", "マグマ"),
    0x001D3318: Data(DataType.String, 8, "Daytime", "日中"),
    0x001D3320: Data(DataType.String, 8, "Evening", "夕方"),
    0x001D3330: Data(DataType.String, 16, "Automatic execution of all demos", "全デモ自動実行"), # MACHINE_TRANSLATED
    0x001D3340: Data(DataType.String, 20, "All demo simple automatic execution", "全デモ簡易自動実行"), # MACHINE_TRANSLATED
    0x001D3354: Data(DataType.String, 20, "All demo road tests", "全デモロードテスト"), # MACHINE_TRANSLATED
    0x001D3368: Data(DataType.String, 32, "Processing drop test (development machine only)", "処理落ちテスト（開発機専用）"), # MACHINE_TRANSLATED
    0x001D3388: Data(DataType.String, 20, "Time zone: %s", "　時間帯  　　:%s"), # MACHINE_TRANSLATED
    0x001D339C: Data(DataType.String, 20, "Dummy Plug: %s", "　ダミープラグ:%s"),
    0x001D33B0: Data(DataType.String, 20, "Cable: %s", "　ケーブル　　:%s"),
    0x001D33C4: Data(DataType.String, 20, "Face Window Dialogue  :%s", "　顔窓セリフ  :%s"),
    0x001D33D8: Data(DataType.String, 8, "●%s", "●%s"),
    0x001D33E0: Data(DataType.String, 4, "R", "Ｒ"),
    0x001D33E4: Data(DataType.String, 20, "Left or right: %s", "　左又は右　　:%s"), # MACHINE_TRANSLATED
    0x001D33F8: Data(DataType.String, 4, "L", "Ｌ"),
    0x001D33FC: Data(DataType.String, 20, "　Angle　　:%d", "　アングル　　:%d"),
    0x001D3410: Data(DataType.String, 20, "　Eva 2　　:%s", "　エヴァ２　　:%s"),
    0x001D3424: Data(DataType.String, 20, "　Eva 1　　:%s", "　エヴァ１　　:%s"),
    0x001D3438: Data(DataType.String, 20, "　Angel    　　:%s", "　使徒    　　:%s"),
    0x001D344C: Data(DataType.String, 20, "Background:%s", "　背景    　　:%s"),
    0x001D349C: Data(DataType.String, 32, "Berserk attacks against Israfel A+B not allowed", "イスラフェルWに暴走攻撃は不可"),
    0x001D34BC: Data(DataType.String, 36, "For Isla Fel W, 2 vs Eva is required", "対イスラフェルWでは2対エヴァが必要"), # MACHINE_TRANSLATED
    0x001D34E0: Data(DataType.String, 20, "No two same evas", "同じエヴァ2体は不可"), # MACHINE_TRANSLATED
    0x001D34F4: Data(DataType.String, 40, "Merging of Unit-03 and Bardiel is ×", "参号機とバルディエルの組み合わせは×"),
    0x001D351C: Data(DataType.String, 12, "−−−−−", "−−−−−"),
    0x001D35A0: Data(DataType.String, 20, "Pallet Rifle", "パレットライフル"),
    0x001D35B4: Data(DataType.String, 8, "Punch A", "パンチA"),
    0x001D35BC: Data(DataType.String, 8, "Punch B", "パンチB"),
    0x001D35C4: Data(DataType.String, 8, "Kick A", "キックA"),
    0x001D35CC: Data(DataType.String, 8, "Kick B", "キックB"),
    0x001D35D4: Data(DataType.String, 12, "2P Kick", "２Ｐキック"),
    0x001D35E0: Data(DataType.String, 20, "Prog Knife Cutting", "プログナイフ切る"),
    0x001D35F4: Data(DataType.String, 20, "Prog Knife Stabbing", "プログナイフ突く"),
    0x001D3608: Data(DataType.String, 16, "Internal Power Suspended", "内蔵電源停止"),
    0x001D3618: Data(DataType.String, 12, "Activity Suspended", "活動停止"),
    0x001D3624: Data(DataType.String, 20, "Positron Rifle", "ボジトロンライフル"),
    0x001D3638: Data(DataType.String, 20, "Sniper Rifle", "スナイパーライフル"),
    0x001D364C: Data(DataType.String, 24, "Positron Sniper Rifle", "ポジトロンスナイパー"),
    0x001D3664: Data(DataType.String, 24, "Throwing Spear of Longinus", "ロンギヌスの槍を投げる"),
    0x001D367C: Data(DataType.String, 20, "A.T. Field Neutralization", "ＡＴフィールド中和"),
    0x001D3690: Data(DataType.String, 16, "A.T.F. Attack", "ＡＴＦアタック"),
    0x001D36A0: Data(DataType.String, 20, "Mastema Slash", "マステマ斬り付け"),
    0x001D36B4: Data(DataType.String, 16, "Mastema Firing", "マステマ射撃"),
    0x001D36C4: Data(DataType.String, 16, "N2 Missile", "Ｎ２ミサイル"),
    0x001D36D4: Data(DataType.String, 16, "Dual Saw", "デュアルソー"),
    0x001D36E4: Data(DataType.String, 16, "Cutting with Sword", "剣で切り裂き"),
    0x001D36F4: Data(DataType.String, 12, "Scratch", "引っ掻き"),
    0x001D3700: Data(DataType.String, 24, "Prog Dagger Cut", "プログダガー切り裂き"),
    0x001D3718: Data(DataType.String, 24, "Prog Dagger Stab", "プログダガー突き刺し"),
    0x001D3730: Data(DataType.String, 20, "Impact Bolt", "インパクトボルト"),
    0x001D3744: Data(DataType.String, 20, "Eva Berserk Kick A", "エヴァ暴走キックA"),
    0x001D3758: Data(DataType.String, 20, "Eva Berserk Tackle", "エヴァ暴走タックル"),
    0x001D376C: Data(DataType.String, 24, "Eva Berserk Bear Claw", "エヴァ暴走ベアクロー"),
    0x001D3784: Data(DataType.String, 20, "Eva Berserk Roundhouse Kick", "エヴァ暴走回し蹴り"),
    0x001D3798: Data(DataType.String, 24, "Unit-01 Berserk Roaring", "初号機暴走　咆哮する"),
    0x001D37B0: Data(DataType.String, 16, "Unit-01 True Berserk", "初号機真・暴走"),
    0x001D37C0: Data(DataType.String, 24, "Unit-01 True Berserk  Movement", "初号機真・暴走　移動"),
    0x001D37D8: Data(DataType.String, 8, "Entrance", "登場"),
    0x001D37E0: Data(DataType.String, 12, "Electric Shock Discharge", "電撃放電"),
    0x001D37EC: Data(DataType.String, 16, "Hammer Attack", "ハンマー攻撃"),
    0x001D37FC: Data(DataType.String, 8, "Light Beam", "怪光線"),
    0x001D3804: Data(DataType.String, 8, "Punch", "パンチ"),
    0x001D380C: Data(DataType.String, 8, "Spear of Light", "光の槍"),
    0x001D3814: Data(DataType.String, 12, "Whip Pierce", "ムチ貫き"),
    0x001D3820: Data(DataType.String, 12, "Whip Strike", "ムチ叩き"),
    0x001D382C: Data(DataType.String, 8, "Beam", "ビーム"),
    0x001D3834: Data(DataType.String, 20, "Chop", "チョップ（分離）"),
    0x001D3848: Data(DataType.String, 16, "Light Beam (Isolated)", "怪光線(分離)"),
    0x001D3858: Data(DataType.String, 8, "Lytic Fluid", "溶解液"),
    0x001D3860: Data(DataType.String, 8, "Neck Throttle", "首絞め"),
    0x001D3868: Data(DataType.String, 12, "Dropkick", "飛び蹴り"),
    0x001D3874: Data(DataType.String, 12, "Tackle", "タックル"),
    0x001D3880: Data(DataType.String, 12, "Bear Claw", "ベアクロー"),
    0x001D388C: Data(DataType.String, 8, "Kick", "キック"),
    0x001D3894: Data(DataType.String, 12, "Arm Cutters", "腕カッター"),
    0x001D38A0: Data(DataType.String, 12, "Stab", "突き刺し"),
    0x001D38AC: Data(DataType.String, 8, "Persuasion", "説得"),
    0x001D38B4: Data(DataType.String, 20, "Unit-01 Punch Attack", "初号機パンチ攻撃"),
    0x001D38C8: Data(DataType.String, 20, "Unit-02 Punch Attack", "弐号機パンチ攻撃"),
    0x001D38DC: Data(DataType.String, 20, "Unit-01 Knife Attack", "初号機ナイフ攻撃"),
    0x001D38F0: Data(DataType.String, 20, "Unit-02 Knife Attack", "弐号機ナイフ攻撃"),
    0x001D3904: Data(DataType.String, 20, "Kaworu Crush", "カオル握りつぶす"),
    0x001D3918: Data(DataType.String, 12, "Mass Production Model Entrance", "量産機登場"),
    0x001D3924: Data(DataType.String, 20, "Cutting with Mass Production Model Sword", "量産機剣で切り裂き"),
    0x001D3938: Data(DataType.String, 8, "All", "全部"),
    0x001D3940: Data(DataType.String, 8, "Unit-00", "零号機"),
    0x001D3948: Data(DataType.String, 8, "Unit-01", "初号機"),
    0x001D3950: Data(DataType.String, 8, "Unit-02", "弐号機"),
    0x001D3958: Data(DataType.String, 8, "Unit-03", "参号機"),
    0x001D3960: Data(DataType.String, 8, "Unit-04", "四号機"),
    0x001D3968: Data(DataType.String, 12, "New Unit-01", "新初号機"),
    0x001D3974: Data(DataType.String, 8, "J.A. 2", "ＪＡ２"),
    0x001D397C: Data(DataType.String, 12, "Sachiel", "サキエル"),
    0x001D3988: Data(DataType.String, 16, "Shamshel", "シャムシエル"),
    0x001D3998: Data(DataType.String, 12, "Ramiel", "ラミエル"),
    0x001D39A4: Data(DataType.String, 16, "Israfel", "イスラフェル"),
    0x001D39B4: Data(DataType.String, 12, "Matarael", "マトリエル"),
    0x001D39C0: Data(DataType.String, 16, "Bardiel", "バルディエル"),
    0x001D39D0: Data(DataType.String, 12, "Zeruel", "ゼルエル"),
    0x001D39DC: Data(DataType.String, 16, "Armisael", "アルミサエル"),
    0x001D39EC: Data(DataType.String, 12, "Tabris", "ダブリス"),
    0x001D39F8: Data(DataType.String, 8, "M.P. Eva", "量産機"),
    0x001D3A04: Data(DataType.String, 8, "ON", "ＯＮ"),
    0x001D3A0C: Data(DataType.String, 8, "off", "ｏｆｆ"),
    0x001D3A14: Data(DataType.String, 168, "[%3d/%3d](%3d/%3d)\nScene name: %s(%d)\nCamera: %s (%d)\nEva1: %s\nEva2: %s\nApostle: %s\nCable: %s\nDummy plug: %s\nOther: %2d %2d %2d\n", "[%3d/%3d](%3d/%3d)\nシーン名　　：%s(%d)\nカメラ　　　：%s (%d)\nＥｖａ１　　：%s\nＥｖａ２　　：%s\n使徒　　　　：%s\nケーブル　　：%s\nダミープラグ：%s\nその他：%2d %2d %2d\n"), # MACHINE_TRANSLATED
    0x001D3ACC: Data(DataType.String, 20, "Stop playing", "再生を止めています"), # MACHINE_TRANSLATED
    0x001D3AE0: Data(DataType.String, 32, "Select the display start demo.", "表示開始デモを選んでください。"), # MACHINE_TRANSLATED
    0x001D3B00: Data(DataType.String, 36, "Select the EVA to display.", "表示するエヴァを選んでください。"), # MACHINE_TRANSLATED
    0x001D3B24: Data(DataType.String, 12, "Random", "ランダム"),
    0x001D3D74: Data(DataType.String, 28, "Demo data is new (btdemo)", "デモデータは新規(btdemo)"), # MACHINE_TRANSLATED
    0x001D3D90: Data(DataType.String, 28, "Demo data is conventional (btldemo)", "デモデータは従来(btldemo)"), # MACHINE_TRANSLATED
    0x001D3DAC: Data(DataType.String, 32, "New demo is not possible with conventional data", "新規デモは従来データでは不可"), # MACHINE_TRANSLATED
    0x001D41A4: Data(DataType.String, 16, "You betrayed me!", "裏切ったな！"),
    0x001D41B4: Data(DataType.String, 28, "Trampled my feelings", "僕の気持ちを踏みにじった"), # MACHINE_TRANSLATED
    0x001D41D0: Data(DataType.String, 20, "But you hurt me", "でも僕は傷ついた"),
    0x001D41E4: Data(DataType.String, 20, "I don't want to hurt you", "君を傷つけたくない"),
    0x001D41F8: Data(DataType.String, 24, "You won't help me either", "君も助けてくれないんだ"), # MACHINE_TRANSLATED
    0x001D4210: Data(DataType.String, 16, "It's too convenient!", "勝手過ぎるよ！"),
    0x001D4220: Data(DataType.String, 28, "Why can you say that?", "なぜそんな事が言えるの？"), # MACHINE_TRANSLATED
    0x001D423C: Data(DataType.String, 16, "Don't gloss over things!", "ごまかさないで"),
    0x001D424C: Data(DataType.String, 20, "Even you're the same as Father.", "君も父さんと同じだ"),
    0x001D4260: Data(DataType.String, 20, "I liked it too", "僕も好きだったのに"), # MACHINE_TRANSLATED
    0x001D4274: Data(DataType.String, 8, "No!", "違う！"),
    0x001D427C: Data(DataType.String, 12, "...I guess you're right.", "…そうかい"),
    0x001D4288: Data(DataType.String, 20, "Why do you hurt me", "なぜ僕を傷つけるの"), # MACHINE_TRANSLATED
    0x001D429C: Data(DataType.String, 24, "Isn't it so", "だってそうじゃないか"), # MACHINE_TRANSLATED
    0x001D42B4: Data(DataType.String, 20, "What should I do?", "どうすればいいの"),
    0x001D42C8: Data(DataType.String, 20, "This is a lie", "こんなの嘘だよね"), # MACHINE_TRANSLATED
    0x001D42DC: Data(DataType.String, 24, "Wasn't he a friend?", "友達じゃなかったの？"), # MACHINE_TRANSLATED
    0x001D42F4: Data(DataType.String, 20, "It doesn't matter", "そんなの関係ないよ"), # MACHINE_TRANSLATED
    0x001D4308: Data(DataType.String, 24, "I don't want to be hated by you", "君には嫌われたくない"), # MACHINE_TRANSLATED
    0x001D4320: Data(DataType.String, 24, "I was happy to meet you", "出会って嬉しかったのに"), # MACHINE_TRANSLATED
    0x001D4338: Data(DataType.String, 16, "But still, why?", "なのに、何故"),
    0x001D4348: Data(DataType.String, 24, "Do you want to keep living?", "生きていて嬉しいの？"),
    0x001D4360: Data(DataType.String, 20, "Why do you want to die?", "どうして死にたいの"),
    0x001D4374: Data(DataType.String, 16, "I don't get it", "わからないよ"),
    0x001D4384: Data(DataType.String, 24, "Just try again together", "一緒にやり直せばいい"), # MACHINE_TRANSLATED
    0x001D439C: Data(DataType.String, 24, "You can be an apostle", "君が使徒でも構わない"), # MACHINE_TRANSLATED
    0x001D43B4: Data(DataType.String, 20, "You're the one you need", "君は必要な人なんだ"), # MACHINE_TRANSLATED
    0x001D43C8: Data(DataType.String, 28, "It's just an escape", "そんなの逃げでしかないよ"), # MACHINE_TRANSLATED
    0x001D43E4: Data(DataType.String, 24, "Make me a friend again...", "僕ともう一度友達に…"), # MACHINE_TRANSLATED
    0x001D43FC: Data(DataType.String, 12, "That's unfair", "卑怯だよ"),
    0x001D4408: Data(DataType.String, 12, "Why?", "どうして？"),
    0x001D4414: Data(DataType.String, 24, "Why did you appear before me", "何で僕の前に現われたの"), # MACHINE_TRANSLATED
    0x001D442C: Data(DataType.String, 24, "I can't trust that", "そんなの信用できない"), # MACHINE_TRANSLATED
    0x001D4444: Data(DataType.String, 20, "Kill me", "いっそ、殺してよ"), # MACHINE_TRANSLATED
    0x001D4458: Data(DataType.String, 24, "I'd rather die than fight.", "戦うなら死んだ方がいい"),
    0x001D4470: Data(DataType.String, 8, "It's not true.", "嘘だ"),
    0x001D4478: Data(DataType.String, 28, "If you go, seriously beat me", "行くなら本気で僕を倒せよ"), # MACHINE_TRANSLATED
    0x001D4494: Data(DataType.String, 28, "Don't go! Don't go!!", "行かないで、行かないで！"),
    0x001D44B0: Data(DataType.String, 20, "I don't want to fight you.", "君とは戦いたくない"),
    0x001D44C4: Data(DataType.String, 24, "But I don't want to hurt you.", "でも、傷つけたくない"),
    0x001D44DC: Data(DataType.String, 24, "Say you won't go!", "行かないって言って！"),
    0x001D44F4: Data(DataType.String, 16, "I hate that", "そんなの嫌だ"), # MACHINE_TRANSLATED
    0x001D4504: Data(DataType.String, 16, "Don't go!", "行かないで！！"),
    0x001D4514: Data(DataType.String, 28, "I... want to live with you.", "僕は…、君と生きたいんだ"),
    0x001D4530: Data(DataType.String, 12, "Crush him", "握り潰す"),
    0x001D4630: Data(DataType.String, 20, "Angel Advent Event", "使徒出現イベント"),
    0x001D46B8: Data(DataType.String, 12, "Cannot be equipped", "装備不可"), # MACHINE_TRANSLATED
    0x001D46C4: Data(DataType.String, 8, "\n%s％", "\n%s％"),
    0x001D46D0: Data(DataType.String, 24, "%1iAttack List　%2iGo Back", "%1i攻撃リスト　%2i戻る"),
    0x001D46E8: Data(DataType.String, 20, "%1iGo Back　%2iGo Back", "%1i戻る　%2i戻る"),
    0x001D46FC: Data(DataType.String, 8, "−−", "−−"),
    0x001D4714: Data(DataType.String, 8, "%s.%sSec.", "%s.%s秒"),
    0x001D471C: Data(DataType.String, 12, "Proximity (short)", "近接(短)"), # MACHINE_TRANSLATED
    0x001D4728: Data(DataType.String, 16, "Proximity (short to long)", "近接(短〜長)"), # MACHINE_TRANSLATED
    0x001D4738: Data(DataType.String, 12, "Proximity (long)", "近接(長)"), # MACHINE_TRANSLATED
    0x001D4744: Data(DataType.String, 8, "%sm", "%sｍ"), # MACHINE_TRANSLATED
    0x001D474C: Data(DataType.String, 16, "%1iGo Back %2iGo Back", "%1i戻る %2i戻る"),
    0x001D475C: Data(DataType.String, 12, "No effect", "影響無し"), # MACHINE_TRANSLATED
    0x001D4768: Data(DataType.String, 8, "%s／5", "%s／５"),
    0x001D4770: Data(DataType.String, 8, "%s degree", "%s度"), # MACHINE_TRANSLATED
    0x001D4778: Data(DataType.String, 12, "%s degree (one side)", "%s度(片側)"), # MACHINE_TRANSLATED
    0x001D47DC: Data(DataType.String, 8, "Front", "正面"),
    0x001D47E4: Data(DataType.String, 8, "Diagonally forward", "斜め前"), # MACHINE_TRANSLATED
    0x001D47EC: Data(DataType.String, 16, "Front to diagonal front", "正面〜斜め前"), # MACHINE_TRANSLATED
    0x001D47FC: Data(DataType.String, 8, "Right next to", "真横"), # MACHINE_TRANSLATED
    0x001D4804: Data(DataType.String, 16, "Diagonally from front to side", "斜め前〜真横"), # MACHINE_TRANSLATED
    0x001D4814: Data(DataType.String, 12, "Front to side", "正面〜真横"), # MACHINE_TRANSLATED
    0x001D4C68: Data(DataType.String, 24, "There is no empty power building", "空きの電源ビルがない"), # MACHINE_TRANSLATED
    0x001D4C80: Data(DataType.String, 24, "%s changed to act_power", "%sをact_powerにしました"), # MACHINE_TRANSLATED
    0x001D4C98: Data(DataType.String, 28, "There is no non-empty armory building", "空でない武器庫ビルがない"), # MACHINE_TRANSLATED
    0x001D4CB4: Data(DataType.String, 28, "%s changed to act_weapon", "%sをact_weaponにしました"), # MACHINE_TRANSLATED
    0x001D4D28: Data(DataType.String, 28, "Made %s act_attack", "%sをact_attackにしました"), # MACHINE_TRANSLATED
    0x001D4D44: Data(DataType.String, 20, "%s changed to %s", "%sを%sにしました"), # MACHINE_TRANSLATED
    0x001D516C: Data(DataType.String, 24, "Dual Eva Piloting", "エヴァ両機パイロット"),
    0x001D5204: Data(DataType.String, 32, "Spear of Longinus Arrived at Nerv", "ロンギヌスの槍がネルフに到着"),
    0x001D5224: Data(DataType.String, 24, "Spear of Longinus Lost", "ロンギヌスの槍ロスト"),
    0x001D523C: Data(DataType.String, 24, "Dummy Plug Developed", "ダミープラグ完成した"),
    0x001D5254: Data(DataType.String, 12, "S2 Engine", "Ｓ２機関"),
    0x001D5260: Data(DataType.String, 12, "Unit-01 Frozen", "初号機凍結"),
    0x001D526C: Data(DataType.String, 20, "First strategy set", "最初の作戦設定済み"), # MACHINE_TRANSLATED
    0x001D5280: Data(DataType.String, 24, "A.T. Field Attack", "ATフィールドアタック"),
    0x001D5298: Data(DataType.String, 20, "AT field amplification", "ATフィールド増幅"), # MACHINE_TRANSLATED
    0x001D52AC: Data(DataType.String, 16, "Extended uptime", "稼働時間の延長"), # MACHINE_TRANSLATED
    0x001D52BC: Data(DataType.String, 20, "Unit-01 Berserked", "初号機が暴走した"),
    0x001D52D0: Data(DataType.String, 24, "Unit-01 Underwent Fusion & Predation", "初号機が融合＆捕食した"),
    0x001D52E8: Data(DataType.String, 24, "Tokyo-3 Completed", "第3新東京市が完成した"),
    0x001D5300: Data(DataType.String, 32, "New Unit-01, New Unit-00, New Unit-02", "新初号機、新零号機、新弐号機"),
    0x001D5320: Data(DataType.String, 28, "Positron Sniper Debut", "スナイパーホジトロン登場"),
    0x001D533C: Data(DataType.String, 12, "New Weapons Debut", "新武器登場"),
    0x001D5348: Data(DataType.String, 24, "New Weapons Post-Debut", "新武器は初めてでない"),
    0x001D5360: Data(DataType.String, 16, "Interrupted by J.A.", "ＪＡに横やり"),
    0x001D5370: Data(DataType.String, 20, "Magoroku Sword Deployed", "マゴロクソード配備"),
    0x001D5698: Data(DataType.String, 12, "No Equipment", "装備なし"),
    0x001D56BC: Data(DataType.String, 24, "Value ＋ Angel Number × %g ＋ %g", "元値＋使徒番号×%g＋%g"),
    0x001D56D4: Data(DataType.String, 20, "%g ＋ Angel Number × %g", "%g＋使徒番号×%g"),
    0x001D56E8: Data(DataType.String, 24, "Value ＋ Angel Number ×%g−%g", "元値＋使徒番号×%g−%g"),
    0x001D5754: Data(DataType.String, 20, "Angel Number ×%g＋%g", "使徒番号×%g＋%g"),
    0x001D5788: Data(DataType.String, 16, "No Arrival Animations", "出現デモなし"),
    0x001D5798: Data(DataType.String, 16, "No Strategic Communications", "作戦伝達なし"),
    0x001D57A8: Data(DataType.String, 16, "No Sortie Animations", "出撃デモなし"),
    0x001D57B8: Data(DataType.String, 16, "No Events", "イベントなし"),
    0x001D57C8: Data(DataType.String, 16, "No Battle Animations", "戦闘デモなし"),
    0x001D57D8: Data(DataType.String, 16, "No Angel Deaths", "使徒死亡なし"),
    0x001D57E8: Data(DataType.String, 16, "No Eva Deaths", "EVA 死亡なし"),
    0x001D57F8: Data(DataType.String, 16, "No Activity Suspension", "活動停止なし"),
    0x001D5808: Data(DataType.String, 16, "Eva Shut-Off", "エヴァ停止　"),
    0x001D5818: Data(DataType.String, 16, "Angel Shut-Off", "使徒停止　　"),
    0x001D5828: Data(DataType.String, 16, "U.N. Forces Shut-Off", "国連軍停止　"),
    0x001D5838: Data(DataType.String, 16, "Armament Building Shut-Off", "兵装ビル停止"),
    0x001D5848: Data(DataType.String, 16, "Angel Sighted", "使徒が見える"),
    0x001D5858: Data(DataType.String, 16, "J.A.2 Launch", "ＪＡ２出現　"),
    0x001D5868: Data(DataType.String, 12, "No Berserk", "暴走なし"),
    0x001D587C: Data(DataType.String, 4, "○", "○"),
    0x001D5880: Data(DataType.String, 4, "×", "×"),
    0x001D58B0: Data(DataType.String, 80, "      Heapsize %8d\nInitial: Usedsize %8d\nCurrent: Usedsize %8d\n      Freesize %8d\n", "      Heapsize %8d\n初期: Usedsize %8d\n現在: Usedsize %8d\n      Freesize %8d\n"),
    0x001D5900: Data(DataType.String, 24, "Angel Number (%d) is abnormal", "使徒番号(%d)が異常です"),
    0x001D5918: Data(DataType.String, 8, "Unimplemented", "未実装"),
    0x001D5B14: Data(DataType.String, 16, "Mode Modification", "モードの変更"),
    0x001D5B24: Data(DataType.String, 12, "View Angle Modification", "画角の変更"),
    0x001D5B30: Data(DataType.String, 12, "Depression Angle Modification", "ふ角の変更"),
    0x001D5B3C: Data(DataType.String, 12, "Scroll", "スクロール"),
    0x001D5B48: Data(DataType.String, 8, "Light", "ライト"),
    0x001D6538: Data(DataType.String, 8, "? ? ?", "？？？"), # MACHINE_TRANSLATED
    0x001D6540: Data(DataType.String, 12, "No Mode", "モードなし"),
    0x001D654C: Data(DataType.String, 12, "Romantic Comedy", "ラブコメ"),
    0x001D6558: Data(DataType.String, 16, "Mysterious", "ミステリアス"),
    0x001D6568: Data(DataType.String, 12, "Adult", "アダルト"),
    0x001D6574: Data(DataType.String, 8, "School", "学園"),
    0x001D657C: Data(DataType.String, 8, "Father and Son", "親子鷹"),
    0x001D6584: Data(DataType.String, 12, "A Decline", "落ち込み"),
    0x001D6590: Data(DataType.String, 20, "Dredging Up Character's Past", "キャラ掘り起こし"),
    0x001D65A4: Data(DataType.String, 12, "Mood-Building", "盛り上げる"),
    0x001D65B0: Data(DataType.String, 12, "Psychological Characterization", "心理描写"),
    0x001D65BC: Data(DataType.String, 12, "Forced End", "強引終らせ"),
    0x001D6734: Data(DataType.String, 4, "○", "○"),
    0x001D6738: Data(DataType.String, 12, "Dummy-kun", "ダミくん"),
    0x001D6744: Data(DataType.String, 12, "Dummy-san", "ダミさん"),
    0x001D6798: Data(DataType.String, 12, "No Damages", "損害なし"),
    0x001D67A4: Data(DataType.String, 8, "Light Damage", "小破"),
    0x001D67AC: Data(DataType.String, 8, "Medium Damage", "中破"),
    0x001D67B4: Data(DataType.String, 8, "Heavy Damage", "大破"),
    0x001D67BC: Data(DataType.String, 8, "Lost", "ロスト"),
    0x001D67D8: Data(DataType.String, 8, "Minor Injuries", "軽傷"),
    0x001D67E0: Data(DataType.String, 12, "No Injuries", "負傷なし"),
    0x001D67EC: Data(DataType.String, 8, "Serious Injuries", "重傷"),
    0x001D67F4: Data(DataType.String, 8, "Critical Condition", "重体"),
    0x001D67FC: Data(DataType.String, 12, "Shinji Ikari", "碇シンジ"),
    0x001D6808: Data(DataType.String, 24, "Asuka Soryu Langley", "惣流アスカ・ラングレイ"),
    0x001D6820: Data(DataType.String, 12, "Rei Ayanami", "綾波レイ"),
    0x001D682C: Data(DataType.String, 12, "Toji Suzuhara", "鈴原トウジ"),
    0x001D6838: Data(DataType.String, 12, "Kaworu Nagisa", "渚カヲル"),
    0x001D6884: Data(DataType.String, 16, "Unconscious body", "意識不明の重体"), # MACHINE_TRANSLATED
    0x001D6894: Data(DataType.String, 8, "Death", "死亡"),
    0x001D6B34: Data(DataType.String, 16, "Positron Sniper", "ポジトロン・Ｓ"),
    0x001D6B44: Data(DataType.String, 12, "N. Missile", "Νミサイル"),
    0x001D6B50: Data(DataType.String, 20, "Impact Bolt", "インパクトボルト"),
    0x001D6C0C: Data(DataType.String, 12, "Auto", "ＡＵＴＯ"),
    0x001D6C18: Data(DataType.String, 8, "Off", "ＯＦＦ"),
    0x001D6C20: Data(DataType.String, 8, "All", "ＡＬＬ"),
    0x001D6C28: Data(DataType.String, 12, "Normal Victory", "通常勝利"),
    0x001D6C34: Data(DataType.String, 12, "Victory with a Loss", "ロスト勝利"),
    0x001D6C40: Data(DataType.String, 8, "Defeat", "敗北"),
    0x001D6C48: Data(DataType.String, 12, "Victory via Compromise", "和解勝利"),
    0x001D6C54: Data(DataType.String, 12, "Broken victory", "決裂勝利"), # MACHINE_TRANSLATED
    0x001D6C74: Data(DataType.String, 8, "01 HERE", "初HERE"),
    0x001D6C7C: Data(DataType.String, 8, "03 HERE", "参HERE"),
    0x001D6C84: Data(DataType.String, 8, "Enemy HERE", "敵EVA"),
    0x001D6C8C: Data(DataType.String, 8, "00 HERE", "零HERE"),
    0x001D6C94: Data(DataType.String, 8, "02 HERE", "弐HERE"),
    0x001D6C9C: Data(DataType.String, 8, "04 HERE", "四HERE"),
    0x001D6CA4: Data(DataType.String, 8, "Both HERE", "両HERE"),
    0x001D6DB8: Data(DataType.String, 8, "Not Yet Debuted", "未登場"),
    0x001D6DC0: Data(DataType.String, 12, "Sortie Possible", "出撃可能"),
    0x001D6DCC: Data(DataType.String, 8, "Hospitalization", "入院中"),
    0x001D6DD4: Data(DataType.String, 12, "Eva Activation Failure", "EVA起動不可"),
    0x001D6DE0: Data(DataType.String, 12, "Eva Lost", "EVAロスト"),
    0x001D6DEC: Data(DataType.String, 12, "Eva Under Freeze", "EVA凍結中"),
    0x001D6DF8: Data(DataType.String, 8, "Currently Running Away", "家出中"),
    0x001D6E00: Data(DataType.String, 8, "Currently Resigned", "辞職中"),
    0x001D6EAC: Data(DataType.String, 12, "[Next Day]", "「翌日」"),
    0x001D6EB8: Data(DataType.String, 12, "[Several Days Later]", "「数日後」"),
    0x001D6EC4: Data(DataType.String, 16, "[○○ Days Later]", "「○○日後」"),
    0x001D6ED4: Data(DataType.String, 8, "Yes", "は　い"),
    0x001D6EDC: Data(DataType.String, 8, "No", "いいえ"),
    0x001D6F2C: Data(DataType.String, 24, "There is no text", "テキストがありません"),
    0x001D7130: Data(DataType.String, 48, "Eva Unit-01's back-up power terminated.\nActive limit reached.\n", "エヴァ初号機の予備電源終了。\n活動限界です。\n"),
    0x001D7174: Data(DataType.String, 60, "Please catch up with the\n runaway ΘΑ before\n internal power runs out.", "暴走しているΘΑに\n内蔵電源が切れる前に\n追いついて下さい。"),
    0x001D71B0: Data(DataType.String, 92, "ΘΑ is in the direction of the arrow.\nTo catch the runaway ΘΑ in the front\nYou can catch up quickly.", "ΘΑは矢印の方向にいます。\n暴走するΘΑを正面にとらえるほど\n早く追いつくことができます。"), # MACHINE_TRANSLATED
    0x001D720C: Data(DataType.String, 4, "Front", "前"),
    0x001D7210: Data(DataType.String, 4, "Left", "左"),
    0x001D7214: Data(DataType.String, 4, "Right", "右"),
    0x001D72A4: Data(DataType.String, 24, "Begin capture of runaway ΘΑ!", "暴走ΘΑの捕捉開始！"),
    0x001D74A4: Data(DataType.String, 20, "[Acceleration] can be used", "「加速」使用可能"),
    0x001D74B8: Data(DataType.String, 20, "[Speed-Up] can be used", "「増速」使用可能"),
    0x001D74CC: Data(DataType.String, 24, "[Dash] can be used", "「ダッシュ」使用可能"),
    0x001D77D8: Data(DataType.String, 16, "I'm not scared", "怖くなんかない"), # MACHINE_TRANSLATED
    0x001D77E8: Data(DataType.String, 20, "I hate being hated", "嫌われるのは嫌だ"), # MACHINE_TRANSLATED
    0x001D77FC: Data(DataType.String, 24, "You can be disliked by others", "他人から嫌われてもいい"), # MACHINE_TRANSLATED
    0x001D7814: Data(DataType.String, 20, "Not bad for myself", "自分ばかり悪くない"), # MACHINE_TRANSLATED
    0x001D7828: Data(DataType.String, 20, "I'm the bad one...", "悪いのは自分だ…"), # MACHINE_TRANSLATED
    0x001D783C: Data(DataType.String, 16, "So is everyone", "誰だってそうだ"), # MACHINE_TRANSLATED
    0x001D784C: Data(DataType.String, 16, "I also need to give up", "諦めも必要だ"), # MACHINE_TRANSLATED
    0x001D785C: Data(DataType.String, 24, "What's wrong with protecting yourself!", "自分を守って何が悪い！"), # MACHINE_TRANSLATED
    0x001D7874: Data(DataType.String, 8, "No!", "違う！"),
    0x001D787C: Data(DataType.String, 20, "What should I do?", "どうすればいい？"),
    0x001D7890: Data(DataType.String, 24, "It's a lie, nothing good", "嘘だ、いい事なんかない"), # MACHINE_TRANSLATED
    0x001D78A8: Data(DataType.String, 20, "No change needed", "変化なんか要らない"), # MACHINE_TRANSLATED
    0x001D78BC: Data(DataType.String, 20, "And yet people change", "それでも人は変わる"),
    0x001D78D0: Data(DataType.String, 24, "There is no human who does not regret", "後悔しない人間はいない"), # MACHINE_TRANSLATED
    0x001D78E8: Data(DataType.String, 28, "Don't remind me that", "そんな事思い出させないで"), # MACHINE_TRANSLATED
    0x001D7904: Data(DataType.String, 16, "I'm scared", "怖いと思ってる"), # MACHINE_TRANSLATED
    0x001D7914: Data(DataType.String, 24, "It’s scary to look into my heart", "心を覗かれるのは怖い"), # MACHINE_TRANSLATED
    0x001D792C: Data(DataType.String, 28, "I want my heart to be visible to everyone", "心が誰にでも見えればいい"), # MACHINE_TRANSLATED
    0x001D7948: Data(DataType.String, 24, "I haven't hurt anyone!", "僕は誰も傷つけてない！"), # MACHINE_TRANSLATED
    0x001D7960: Data(DataType.String, 24, "I think I've hurt", "傷つけた事はあると思う"), # MACHINE_TRANSLATED
    0x001D7978: Data(DataType.String, 28, "Everyone hides their hearts too much", "みんな心を隠しすぎるんだ"), # MACHINE_TRANSLATED
    0x001D7994: Data(DataType.String, 20, "Everyone is a liar", "みんな嘘つきなんだ"), # MACHINE_TRANSLATED
    0x001D79A8: Data(DataType.String, 28, "I'm hurt because of myself", "僕が傷つくのは自分のせい"), # MACHINE_TRANSLATED
    0x001D79C4: Data(DataType.String, 28, "I'm hurt because of someone else", "僕が傷つくのは他人のせい"), # MACHINE_TRANSLATED
    0x001D79E0: Data(DataType.String, 28, "But I want to like people", "でも、人を好きになりたい"), # MACHINE_TRANSLATED
    0x001D79FC: Data(DataType.String, 20, "I'm afraid to be with other people", "他人といるのが怖い"), # MACHINE_TRANSLATED
    0x001D7A10: Data(DataType.String, 28, "So I'm waiting for a chance", "だからきっかけを待ってる"), # MACHINE_TRANSLATED
    0x001D7A2C: Data(DataType.String, 28, "I don't want to hide my heart", "僕だって心を隠したくない"), # MACHINE_TRANSLATED
    0x001D7A48: Data(DataType.String, 28, "No, I'm not doing that", "違う、そんな事していない"), # MACHINE_TRANSLATED
    0x001D7A64: Data(DataType.String, 28, "To get along well with people", "人と上手くやっていく為だ"), # MACHINE_TRANSLATED
    0x001D7A80: Data(DataType.String, 24, "I don't care about other people", "他人なんてどうでもいい"), # MACHINE_TRANSLATED
    0x001D7A98: Data(DataType.String, 24, "Can't change", "変えることはできない"), # MACHINE_TRANSLATED
    0x001D7AB0: Data(DataType.String, 20, "I'm good enough", "自分だけで充分だ"), # MACHINE_TRANSLATED
    0x001D7AC4: Data(DataType.String, 20, "Can you kill yourself?", "自分を殺せって事？"), # MACHINE_TRANSLATED
    0x001D7AD8: Data(DataType.String, 20, "Will I change?", "僕は変われるの？"), # MACHINE_TRANSLATED
    0x001D7AEC: Data(DataType.String, 16, "Are you a stranger?", "君は他人なの？"), # MACHINE_TRANSLATED
    0x001D7AFC: Data(DataType.String, 20, "You are me", "君は僕自身だろう？"), # MACHINE_TRANSLATED
    0x001D7B10: Data(DataType.String, 16, "I'm scared of changing", "変わる事が怖い"), # MACHINE_TRANSLATED
    0x001D7B20: Data(DataType.String, 20, "Not correct", "正しいわけじゃない"), # MACHINE_TRANSLATED
    0x001D7B34: Data(DataType.String, 16, "I want to change", "僕は変わりたい"), # MACHINE_TRANSLATED
    0x001D7B44: Data(DataType.String, 24, "Will the surroundings change?", "周りは変わらないの？"), # MACHINE_TRANSLATED
    0x001D7B5C: Data(DataType.String, 24, "Why do you hurt me", "何で僕を傷つけるんだ"), # MACHINE_TRANSLATED
    0x001D7B74: Data(DataType.String, 20, "What do I want to do?", "何をして欲しいの？"),
    0x001D7B88: Data(DataType.String, 20, "I don't need someone like you", "君なんて必要ない"),
    0x001D7B9C: Data(DataType.String, 24, "Who are you, really?", "君は本当は何者なの？"),
    0x001D7BB4: Data(DataType.String, 20, "I'll live on my own", "私は一人で生きるの"),
    0x001D7BC8: Data(DataType.String, 20, "I won't be lonely or anything", "寂しくなんかない"),
    0x001D7BDC: Data(DataType.String, 24, "I don't need anyone except Mama", "ママ以外、誰も要らない"),
    0x001D7BF4: Data(DataType.String, 20, "Don't run away", "逃げてなんかない"), # MACHINE_TRANSLATED
    0x001D7C08: Data(DataType.String, 20, "I'm one of the chosen people", "私は選ばれた人間よ"),
    0x001D7C1C: Data(DataType.String, 20, "I'm not a doll", "私は人形じゃない"),
    0x001D7C30: Data(DataType.String, 24, "Mama abandoned me?", "ママは私を捨てたの？"),
    0x001D7C48: Data(DataType.String, 12, "Being alone is scary", "一人が怖い"),
    0x001D7C54: Data(DataType.String, 24, "Is it my fault to be alone?", "一人なのは自分のせい？"), # MACHINE_TRANSLATED
    0x001D7C6C: Data(DataType.String, 24, "Is it because of the other person?", "一人なのは他人のせい？"), # MACHINE_TRANSLATED
    0x001D7C84: Data(DataType.String, 28, "I don't want this...", "こんな事、望んでいない…"), # MACHINE_TRANSLATED
    0x001D7CA0: Data(DataType.String, 16, "This is fine", "これで構わない"), # MACHINE_TRANSLATED
    0x001D7CB0: Data(DataType.String, 16, "Do not rely on others", "他人に頼らない"), # MACHINE_TRANSLATED
    0x001D7CC0: Data(DataType.String, 20, "What should I do?", "どうすればいいの？"),
    0x001D7CD4: Data(DataType.String, 28, "No one protected me.", "誰も私を守ってくれないの"),
    0x001D7CF0: Data(DataType.String, 28, "I'm suffering so much", "こんなに苦しんでいるのに"), # MACHINE_TRANSLATED
    0x001D7D0C: Data(DataType.String, 20, "Others are cold...", "他人って冷たい…"), # MACHINE_TRANSLATED
    0x001D7D20: Data(DataType.String, 24, "I want someone close", "誰か近くにいてほしい"), # MACHINE_TRANSLATED
    0x001D7D38: Data(DataType.String, 24, "Others are not suffering", "他人は苦しんでいない"), # MACHINE_TRANSLATED
    0x001D7D50: Data(DataType.String, 12, "Everyone else, too?", "みんなも？"),
    0x001D7D5C: Data(DataType.String, 20, "I'm not like other people", "私は他の人と違う"),
    0x001D7D70: Data(DataType.String, 12, "I don't know", "わからない"),
    0x001D7D7C: Data(DataType.String, 24, "I don't know who I am", "私、自分がわからない"),
    0x001D7D94: Data(DataType.String, 16, "I have duties", "役目があるわ"),
    0x001D7DA4: Data(DataType.String, 8, "No, it's not that...", "ちがう"),
    0x001D7DAC: Data(DataType.String, 4, "...", "…"),
    0x001D7DB0: Data(DataType.String, 24, "More duties await", "次の役目が待っている"),
    0x001D7DC8: Data(DataType.String, 16, "The data will remain", "データが残る"),
    0x001D7DD8: Data(DataType.String, 16, "I don't need a purpose", "目的なんて無い"),
    0x001D7DE8: Data(DataType.String, 12, "That's fine", "それでいい"),
    0x001D7DF4: Data(DataType.String, 20, "But I think I'll change", "でも変わると思う"),
    0x001D7E08: Data(DataType.String, 12, "Because it's my duty", "役目だから"),
    0x001D7E14: Data(DataType.String, 20, "I pilot the Eva", "私はエヴァに乗る"),
    0x001D7E28: Data(DataType.String, 16, "The hope of humanity", "人類の希望よ"),
    0x001D7E38: Data(DataType.String, 20, "It's beyond just my power", "私だけの力じゃない"),
    0x001D7E4C: Data(DataType.String, 8, "The bonds I share...", "絆よ…"),
    0x001D7E54: Data(DataType.String, 20, "Even so, I am bound", "それでも絆はある"),
    0x001D7E68: Data(DataType.String, 8, "They exist", "あるわ"),
    0x001D7E70: Data(DataType.String, 16, "Memories will remain", "思い出は残る"),
    0x001D7E80: Data(DataType.String, 16, "I won't disappear", "消えたりしない"),
    0x001D7E90: Data(DataType.String, 16, "My ties won't change", "絆は変わらない"),
    0x001D7EA0: Data(DataType.String, 16, "That is still fine", "それでもいい"),
    0x001D7EB0: Data(DataType.String, 24, "Are you in trouble?!", "しんどいことあるか！"),
    0x001D7EC8: Data(DataType.String, 12, "It’s bare!", "素じゃ！"), # MACHINE_TRANSLATED
    0x001D7ED4: Data(DataType.String, 16, "True self?", "ホンマの自分？"),
    0x001D7EE4: Data(DataType.String, 12, "What's wrong?", "何が悪い？"), # MACHINE_TRANSLATED
    0x001D7EF0: Data(DataType.String, 12, "You're wrong!", "ちがう！"),
    0x001D7EFC: Data(DataType.String, 24, "It's not coming!", "それがどないしてん！"), # MACHINE_TRANSLATED
    0x001D7F14: Data(DataType.String, 16, "I'm sorry!", "ちゃうわい！"), # MACHINE_TRANSLATED
    0x001D7F24: Data(DataType.String, 20, "What do you play?", "演じる、って何や？"), # MACHINE_TRANSLATED
    0x001D7F38: Data(DataType.String, 12, "And that is?", "それが？"),
    0x001D7F44: Data(DataType.String, 16, "It might be an akan thing...", "アカン事かも…"), # MACHINE_TRANSLATED
    0x001D7F54: Data(DataType.String, 16, "I don't think", "なんとも思わん"), # MACHINE_TRANSLATED
    0x001D7F64: Data(DataType.String, 16, "I don't know", "しゃあないやん"), # MACHINE_TRANSLATED
    0x001D7F74: Data(DataType.String, 20, "I'm a liar...", "ワシは嘘つきや…"),
    0x001D7F88: Data(DataType.String, 20, "Everyone's a liar...", "みんな嘘つきや…"),
    0x001D7F9C: Data(DataType.String, 12, "So tired...", "しんどい…"),
    0x001D7FA8: Data(DataType.String, 12, "I'm not sure.", "自信ない"),
    0x001D7FB4: Data(DataType.String, 12, "That's right", "そうやな"),
    0x001D7FC0: Data(DataType.String, 16, "I am myself!", "ワシはワシや！"),
    0x001D7FD0: Data(DataType.String, 20, "I don't know", "そんなん知らんわ"), # MACHINE_TRANSLATED
    0x001D7FE4: Data(DataType.String, 8, "Take off", "脱ぐ"), # MACHINE_TRANSLATED
    0x001D7FEC: Data(DataType.String, 12, "Take off", "脱がへん"), # MACHINE_TRANSLATED
    0x001D7FF8: Data(DataType.String, 16, "Returning to Adam", "アダムに還る事"),
    0x001D8008: Data(DataType.String, 12, "It doesn't matter", "構わないよ"),
    0x001D8014: Data(DataType.String, 12, "You exaggerate", "大袈裟だよ"),
    0x001D8020: Data(DataType.String, 12, "I'm ready, besides", "覚悟の上さ"),
    0x001D802C: Data(DataType.String, 16, "If the time comes", "時期が来れば"),
    0x001D803C: Data(DataType.String, 12, "Is that so?", "そうかな？"),
    0x001D8048: Data(DataType.String, 12, "I suppose that's right", "そうだね"),
    0x001D8054: Data(DataType.String, 16, "Following the plan", "計画に従う事"),
    0x001D8064: Data(DataType.String, 12, "No way around it", "仕方ないさ"),
    0x001D8070: Data(DataType.String, 20, "I don't mean that", "そんなつもりないよ"), # MACHINE_TRANSLATED
    0x001D8084: Data(DataType.String, 16, "I'm content!", "満足しているよ"),
    0x001D8094: Data(DataType.String, 12, "Hold your tongue!", "言うなっ！"),
    0x001D80A0: Data(DataType.String, 24, "Going as planned, eh?", "予定通りに行くものか"),
    0x001D80B8: Data(DataType.String, 12, "It's alright", "大丈夫さ"),
    0x001D80C4: Data(DataType.String, 12, "What could it be...?", "…何だろう"),
    0x001D80D0: Data(DataType.String, 12, "Of course I do", "当然だよ"),
    0x001D80DC: Data(DataType.String, 16, "Now I want to forget", "今は忘れたい"),
    0x001D80EC: Data(DataType.String, 20, "No, I am Adam", "いや、僕はアダムだ"),
    0x001D8100: Data(DataType.String, 12, "Probably true", "そうかも"),
    0x001D810C: Data(DataType.String, 20, "Nothing more than curiosity", "興味があるだけさ"),
    0x001D8120: Data(DataType.String, 16, "That's not true", "そうじゃない"),
})
