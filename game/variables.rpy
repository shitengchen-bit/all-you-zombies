# 全局变量与情感系统 - variables.rpy

# ============ 三轴情感系统 ============
# 愤恨：对命运/加害者/宇宙的愤怒
# 释然：接纳、理解、与自己和谈
# 困惑：存在性眩晕、质疑现实
default resentment = 0
default acceptance = 0
default bewilderment = 0

# ============ 信任度（独立系统，0-10）============
# 由共情式选项累积，解锁深层话题与额外文本
default trust = 0

# ============ 话题完成标记 ============
default topic_childhood = False   # T1 童年/孤儿院
default topic_love = False        # T2 初恋/公园
default topic_betrayal = False    # T3 背叛/被抛弃
default topic_loss = False        # T4 失去/医院
default topic_drift = False       # T5 漂泊/现在

# T2中是否提前追问了"他怎么了"（影响T3开场措辞的标记）
default topic_betrayal_hint = False

# ============ 七处"微妙相似"线索收集 ============
default clue_eyes = False      # 1 灰绿眼
default clue_birthmark = False # 2 眉尾胎记
default clue_gesture = False   # 3 握杯姿势
default clue_handwriting = False # 4 笔迹
default clue_kindred = False   # 5 "我们是一类人"
default clue_inner = False     # 6 "身体里住着另一个人"
default clue_silhouette = False # 7 漩涡中剪影重叠

# ============ 线索计数（用于画廊彩蛋）============
default clue_count = 0

# ============ 结局标记 ============
default ending_type = ""   # rage / peace / vertigo / epiphany

# ============ CG 回忆画廊解锁 ============
default gallery_unlocked = []

# ============ 辅助函数 ============
init python:
    def add_clue(clue_name):
        """发现线索时调用：标记并计数，触发演出"""
        global clue_count
        if not store.__dict__.get(clue_name, False):
            setattr(store, clue_name, True)
            store.clue_count += 1
            renpy.play("audio/sfx/clue.ogg", channel="sound")
            renpy.notify("发现了一条线索……")

    def determine_ending():
        """终章判定结局类型"""
        r, a, b = store.resentment, store.acceptance, store.bewilderment
        if r >= 12 and a >= 12 and b >= 12:
            return "epiphany"
        dominant = max(r, a, b)
        if dominant == r:
            return "rage"
        elif dominant == a:
            return "peace"
        else:
            return "vertigo"

    def topics_complete():
        """检查5个话题是否全部完成"""
        return (store.topic_childhood and store.topic_love and
                store.topic_betrayal and store.topic_loss and store.topic_drift)
