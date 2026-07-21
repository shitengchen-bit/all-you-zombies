# 第一幕：倾听 - ch1_listening.rpy
# 5个话题块自由探索 + 闪回。时代分层调色随闪回切换。

# ============================================================
# 话题选择枢纽
# ============================================================
label act1_hub:

    scene bg bar_main
    show john neutral at right
    with dissolve

    # 检查是否5个话题全部完成
    if topics_complete():
        jump act2_offer

    mono "（时钟滴答。雨声不断。)"
    mono "（他坐在我面前，像一本被雨水泡皱的书。)"
    mono "（而我，可以翻开任何一页。)"

    menu:
        n "你想从哪里问起？"

        "「说说你的童年吧。」" if not topic_childhood:
            jump topic_childhood

        "「你爱过什么人吗？」" if not topic_love:
            jump topic_love

        "「后来呢？那个人。」" if not topic_betrayal and topic_love:
            jump topic_betrayal

        "「医院里……发生了什么？」" if not topic_loss and topic_betrayal and trust >= 3:
            jump topic_loss

        "「这些年，你是怎么过的？」" if not topic_drift and topic_loss:
            jump topic_drift

        "「……」（给他续一杯酒，不问）":
            $ trust += 1
            mono "（有些时候，不问，比问更有用。)"
            n "我给他续了酒。他看了我一眼，那眼神软了一瞬。"
            jump act1_hub


# ============================================================
# T1 童年 / 孤儿院 (1945-1963)
# 调色：冷灰蓝 + 苍白，留一丝微光
# ============================================================
label topic_childhood:

    scene bg bar_main
    show john neutral at right

    john "童年。"
    n "他重复了一遍这个词，像是在嚼一块石头。"
    john "我的童年，得从一扇门外说起。"

    # ----- 转场进入闪回 -----
    scene black
    with fade
    mono "（他的声音低下去。酒吧的灯光，仿佛也跟着暗了。)"
    mono "（然后，我看见了那扇门。)"

    # ----- 闪回 FB-01：孤儿院 -----
    scene bg orphanage_ext
    with slow_dissolve
    # play music "audio/bgm/orphanage.ogg"

    n "1945年。克利夫兰。冬天。"
    n "雪下得很大。一家孤儿院的铁门，锈迹斑斑。"

    scene cg baby_left
    with dissolve

    n "一个包裹被放在台阶上。包裹里是一个婴儿。"
    n "没有字条。没有名字。"
    n "只有襁褓里，一张冻得发紫的小脸。"

    # ----- 第二处线索：眉尾胎记 -----
    $ add_clue("clue_birthmark")
    mono "（修女把婴儿抱起来的时候，我注意到——)"
    mono "（她的左眉尾，有一道极细的胎记。淡得几乎看不见。)"
    mono "（……和我的，一模一样。)"

    scene bg orphanage_int
    with dissolve

    n "他们给她起名叫简。"
    n "简在孤儿院里长大。她很聪明，聪明得不像话。"
    n "但她也怪。怪得让别的孩子躲着她，让修女们摇头。"

    jane "为什么我和别人不一样？"
    n "七岁的简问修女。修女没有回答。"

    jane "我没有爸爸，也没有妈妈。我连自己从哪里来都不知道。"
    n "她站在窗前，看着外面的雪。"
    jane "我是不是……捡来的？"

    mono "（不知道为什么，看着那扇铁门，看着雪里那个小小的包裹——)"
    mono "（我的心口，闷闷地疼。)"
    mono "（像是我来过这里。像是……我欠了这里，一笔还不清的债。)"

    n "简十岁那年，第一次发现自己和别人「不一样」。"
    n "她的身体里，有一些……说不清楚的东西。"
    n "她不敢告诉任何人。她只是更加沉默，更加格格不入。"

    jane "（我一定是什么地方坏了。)"
    jane "（所以才会被扔掉。)"

    # ----- 回到酒吧 -----
    scene bg bar_main
    show john neutral at right
    with slow_dissolve

    john "她从小就觉得，自己是坏的。"
    john "被扔掉的东西，肯定是坏的。她一直是这么想的。"

    menu:
        bart "……"

        "「谁这么狠心，把一个婴儿扔在雪地里。」":
            $ resentment += 2
            john "狠心？"
            n "他冷笑。"
            john "也许吧。但你知道吗，我后来想过——"
            john "也许把她放在那儿的人，是唯一一个……知道该把她放在哪儿的人。"

        "「也许，那是命运的安排。」":
            $ acceptance += 1
            $ bewilderment += 1
            john "命运。"
            n "他盯着酒杯里晃动的琥珀色。"
            john "你信命运？"
            john "我从前不信。现在……我不知道了。"

        "「她不是坏的。她只是……与众不同。」":
            $ trust += 2
            $ acceptance += 1
            n "他抬起头，看着我。那双灰绿色的眼睛，颤了一下。"
            john "……与众不同。"
            john "你是第一个，没用「怪」这个字的人。"

    $ topic_childhood = True
    jump act1_hub


# ============================================================
# T2 初恋 / 公园 (1963春)
# 调色：柔金 + 嫩绿 + 樱粉，一切发光
# ============================================================
label topic_love:

    scene bg bar_main
    show john neutral at right

    john "爱。"
    n "他说这个字的时候，声音轻得像是怕惊动什么。"
    john "我这一生，只爱过一次。"
    john "就那么一次。"

    scene black
    with fade
    mono "（他闭上了眼睛。)"
    mono "（于是，1963年的春天，来了。)"

    # ----- 闪回 FB-02：公园初恋 -----
    scene bg park_spring
    with slow_dissolve
    # play music "audio/bgm/park_love.ogg"

    n "1963年。四月。公园里的樱花开了。"
    n "阳光从花瓣的缝隙里漏下来，碎成一地金子。"

    n "简十八岁了。她坐在长椅上，膝盖上摊着一本书，但她没在看。"
    n "她在看人来人往，心里想：没有一个人，是为我而来的。"

    n "然后，一个男人在她身边坐下了。"

    show stranger silhouette at center
    with dissolve

    n "他看起来很普通。但简一抬头，就愣住了。"
    n "因为那个男人，正用一种她从未见过的眼神看着她。"
    n "像是……认识她。认识了一辈子。"

    stranger "你在看人。"
    jane "……什么？"
    stranger "你坐在这儿，看人来人往。你在想——没有一个人是为我而来的。"
    n "简的书从膝盖上滑下去了。"
    jane "你……你怎么知道我在想什么？"
    stranger "因为我也这么想过。"
    n "他笑了。"
    stranger "很多年，每一天，都这么想。"

    # ----- 第三处线索：握杯姿势（呼应序章铺垫）-----
    $ add_clue("clue_gesture")
    mono "（他们聊了很久。)"
    mono "（简说，那个男人买了一杯热可可，握杯子的姿势很奇怪——)"
    mono "（小指微翘，手腕很柔。)"
    mono "（「和我一模一样。」她说。)"
    mono "（「我从来没见过别人那样拿杯子。」)"

    n "那是简第一次，遇到一个「懂」她的人。"
    n "他说出的每一句话，都像是从她心里抄出来的。"
    n "她的孤独，她的格格不入，她身体里那个说不清楚的秘密——"
    n "他全都知道。全都能接住。"

    jane "为什么……你好像什么都懂我？"
    stranger "因为我们是同一类人。"
    n "他说这句话的时候，看着她的眼睛。"
    stranger "这世上，再没有第二个人，比我更懂你。"

    scene cg first_kiss
    with dissolve

    n "樱花落下来的时候，他吻了她。"
    n "那是简十八年的人生里，第一次，感觉到自己不是坏的。"
    n "第一次，感觉到——原来我，也是可以被人这样温柔对待的。"

    jane "（原来我不是坏的。)"
    jane "（原来我，也是可以被爱的。)"

    mono "（奇怪。明明是在听别人的故事。)"
    mono "（可我的心口，为什么会这么疼？)"
    mono "（刚才有一瞬间，我差点脱口而出——「那是我一生中最幸福的一天」。)"
    mono "（……我怎么会这么想？我又不认识她。)"

    # ----- 回到酒吧 -----
    scene bg bar_main
    show john neutral at right
    with slow_dissolve

    n "他讲到这里，停住了。他的手指无意识地摩挲着杯沿。"
    john "那是我这辈子，唯一一次觉得……自己是完整的。"

    menu:
        bart "……"

        "「我比谁都懂那种感觉。」":
            $ bewilderment += 2
            n "这句话脱口而出。说完，我自己都愣了一下。"
            john "……你怎么会懂？"
            mono "（因为那就是我。)"
            mono "（不。不能说。)"
            bart "……直觉。"

        "（为他感到心痛）":
            $ acceptance += 1
            mono "（我看着他。看着这个还不知道一切的他。)"
            mono "（心痛得像被那只杯子砸了一下。)"
            bart "……那一定很美好。"

        "「然后呢？他怎么了？」":
            $ topic_betrayal_hint = True
            n "他的脸，一下子暗了下去。"
            john "……他？"
            john "他消失了。"

    $ topic_love = True
    jump act1_hub


# ============================================================
# T3 背叛 / 公园诀别 (1963)
# 调色：褪色金 + 灰蓝（同一公园，冷调）
# ============================================================
label topic_betrayal:

    scene bg bar_main
    show john neutral at right

    john "你问，他怎么了。"
    n "他一口喝干了杯里的酒。"
    john "他跑了。像所有男人一样。"
    john "不。比所有男人都狠。"

    scene black
    with fade

    # ----- 闪回 FB-03：公园诀别 -----
    scene bg park_night
    with slow_dissolve
    # play music "audio/bgm/park_loss.ogg"

    n "还是那个公园。还是那张长椅。"
    n "但樱花谢了。天黑了。月亮是冷的。"

    n "简坐在那里，从黄昏坐到深夜。"
    n "她等的人，没有来。"

    scene cg empty_bench
    with dissolve

    n "第二天，她没有等到。第三天，也没有。"
    n "那个说「再没有第二个人比我更懂你」的男人，"
    n "从这个世界上，彻底消失了。"
    n "像从来没有存在过。"

    jane "为什么？"
    n "她摸着那张长椅，指尖冰凉。"
    jane "你明明说，我们是同一类人。"
    jane "你明明说，你懂我。"
    jane "……骗子。"

    n "一个月后，简发现自己怀孕了。"
    n "她摸着肚子，站在公园门口，笑了，又哭了。"
    jane "（至少……至少我还有你。)"
    jane "（至少，这世界上还有一个，和我血脉相连的人。)"

    # ----- 回到酒吧 -----
    scene bg bar_main
    show john neutral at right
    with slow_dissolve

    john "她后来一直在想，那天晚上，那个男人不是「跑了」。"
    john "他像是……凭空消失了。"
    n "他抬起眼。"
    john "像是被人从这个世界上，一把抹掉了。连一点痕迹，都没留下。"

    menu:
        bart "……"

        "「那个男人该死。」":
            $ resentment += 3
            john "该死？"
            n "他笑出了声，笑得很难听。"
            john "哈。你知道吗，我后来也这么想。"
            john "我恨了他很多年。恨得……"
            n "他顿了顿，声音低下去。"
            john "恨得，像是在恨我自己。"

        "「他真的……懂你吗？」":
            $ bewilderment += 2
            john "懂我？"
            n "他怔住了。"
            john "他是我见过最懂我的人。懂到……可怕。"
            john "有时候我半夜醒来，会想——"
            john "他会不会，根本就是……"
            n "他没有说下去。"

        "「你恨他吗？」":
            $ acceptance += 1
            $ bewilderment += 1
            john "恨。"
            n "他说得很快。"
            john "……也，不恨。"
            john "我不知道。我真的不知道。"

    $ topic_betrayal = True
    jump act1_hub


# ============================================================
# T4 失去 / 医院 (1964)
# 调色：消毒白 + 冷青 + 荧光灯绿
# ============================================================
label topic_loss:

    scene bg bar_main
    show john neutral at right

    n "他沉默了很久。久到雨声都显得吵了。"
    john "接下来这一段，我从来没跟任何人讲过。"
    john "连写故事的时候，都不敢写。"

    scene black
    with fade
    mono "（他的声音在发抖。)"
    mono "（我知道，接下来他要讲的，是最痛的那一段。)"
    mono "（可奇怪的是……我好像，早就知道会是怎样。)"

    # ----- 闪回 FB-04：医院觉醒 -----
    scene bg hospital_corridor
    with slow_dissolve
    # play music "audio/bgm/hospital.ogg"

    n "1964年。医院。白色的走廊，长得没有尽头。"
    n "荧光灯管在头顶嗡嗡作响，把一切都照得惨白。"

    n "简要生了。"
    n "可是生产不顺利。血，很多血。医生们冲进冲出。"

    scene cg surgery
    with dissolve

    n "手术台上，灯光白得刺眼。"
    n "医生在她的身体里，发现了一件让所有人沉默的事。"

    n "她的身体里，同时长着两套器官。"
    n "女性的，和男性的。"
    n "她不是「坏」了。她从来都不是。"
    n "她只是——从出生起，就同时是两个人。"

    jane "（原来我不是坏的。)"
    jane "（原来我只是……两个人。)"

    n "可是生产毁了一切。医生告诉她，她再也无法以女人的身体活下去了。"
    n "他们要「修复」她。"
    n "修复的方式，是把她，变成一个男人。"

    # ----- 婴儿被偷走 -----
    scene cg baby_taken
    with dissolve

    n "她在病床上醒来，第一句话是问孩子。"
    n "护士的眼神躲闪着。"
    n "那个女婴——她的女儿——在夜里，被一个陌生人抱走了。"
    n "没有人知道是谁。没有人追回来。"

    jane "我的孩子呢？"
    n "没有人回答她。"
    jane "我的孩子呢！！"

    mono "（那个被抱走的婴儿……)"
    mono "（我的心口，又闷闷地疼起来。疼得我几乎站不住。)"
    mono "（那个「陌生人」。那个抱走她的人。)"
    mono "（我好像……认识他。)"
    mono "（不。不只是认识。可那种感觉，我说不上来。)"

    # ----- 雨夜街道 -----
    scene bg street_rain
    with dissolve

    n "几个星期后。一个下着雨的夜晚。"
    n "一个瘦削的年轻人，从医院走出来，站在雨里。"
    n "他剪了短发，穿着不合身的男装。"
    n "他低头看着自己的手——那双手，曾经那么柔软。"

    n "简死了。"
    n "活下来的，是约翰。"

    # ----- 回到酒吧 -----
    scene bg bar_main
    show john neutral at right
    with slow_dissolve

    n "酒吧里，他坐在我对面。"
    n "他抬起手，看着自己的手。那双手，小指依然微微翘着。"
    john "他们拿走了我的孩子，拿走了我的身体，拿走了「她」。"
    john "然后告诉我：现在，你是个男人了。好好活。"

    # ----- 第六处线索：身体里住着另一个人 -----
    $ add_clue("clue_inner")
    john "可是你知道吗，酒保。"
    john "这么多年，我一直觉得——"
    john "我身体里，还住着另一个人。"
    john "她还在。她一直在我身体里，敲着墙。"

    menu:
        bart "……"

        "「他们怎么能这样对你。」":
            $ resentment += 2
            john "怎么不能？"
            n "他扯了扯嘴角。"
            john "在医生眼里，我不是人。我是个「病例」。"
            john "一个需要被「修正」的错误。"

        "「你终于，成为了你自己。」":
            $ acceptance += 2
            n "他猛地抬头，瞪着我。"
            john "成为我自己？"
            n "他盯着我看了很久，很久。"
            john "……你这话，真奇怪。"
            john "奇怪得……像是你知道些什么。"

        "「她还在。她一直都在。」":
            $ bewilderment += 2
            $ trust += 1
            n "他的眼眶，一下子红了。"
            john "……你怎么会这么说。"
            john "从来没有人……"
            n "他别过头去，不让我看他的眼睛。"

    $ topic_loss = True
    jump act1_hub


# ============================================================
# T5 漂泊 / 现在 (1964-1970)
# 纯对话，无闪回
# ============================================================
label topic_drift:

    scene bg bar_main
    show john neutral at right

    john "后来的事，就无聊了。"
    john "一个没有过去的人，在城市里漂着。"

    n "他把那叠稿子又拿了出来，在吧台上摊开。"
    john "我试过很多工作。都干不长。"
    john "后来我发现，我唯一会的事，就是写。"
    john "写那些女人的故事。被抛弃的，独自生孩子的，深夜里哭的。"

    john "编辑说，我写得比真女人还真。"
    n "他笑了，笑得像哭。"
    john "当然了。因为那不是编的。"
    john "每一个字，都是从我身上剐下来的。"

    menu:
        bart "……"

        "「你写的是她。你身体里的那个她。」":
            $ acceptance += 2
            $ bewilderment += 1
            n "他握笔的手，停住了。"
            john "……"
            john "也许吧。"
            john "也许「未婚妈妈」，从来就不是一个笔名。"
            john "是我给她的……一座坟。"

        "「至少，你还能写。」":
            $ acceptance += 1
            john "至少我还能写。"
            n "他重复了一遍，点点头。"
            john "是啊。至少，我还能把她们的话说出来。"
            john "替她们，也替我自己。"

        "「这世道，配不上你写的东西。」":
            $ resentment += 2
            john "配不上？"
            n "他把稿子收起来，动作很重。"
            john "这世道，连「我」这种东西，都容不下。"
            john "它凭什么，配得上别的。"

    n "他喝完了最后一口酒。"
    n "杯底朝天。"
    john "这就是我了，酒保。"
    john "一个孤儿，一个骗子的情人，一个被偷走孩子的母亲，一个莫名其妙的男人。"
    john "一个……写别人忏悔的骗子。"

    mono "（不。)"
    mono "（你不是骗子。)"
    mono "（你是这个世界上最诚实的人。)"
    mono "（因为你的整个人生，就是一个真相。)"
    mono "（一个，你即将亲眼看见的真相。)"

    $ topic_drift = True
    jump act1_hub
