# 主入口 - script.rpy
# 串联所有章节：序章 → 第一幕 → 第二幕 → 第三幕 → 终章

# 游戏从 start 标签开始
label start:

    # 初始化情感系统（default 已声明，此处确保重置）
    $ resentment = 0
    $ acceptance = 0
    $ bewilderment = 0
    $ trust = 0
    $ clue_count = 0
    $ ending_type = ""

    # 序章：打烊之前
    call prologue from _call_prologue

    # 第一幕：倾听（话题枢纽，内部跳转第二幕）
    # prologue 末尾 jump act1_hub；act1_hub 在5话题完成后 jump act2_offer

    # 第二幕：提议（末尾 jump act3_jump）
    # 第三幕：穿越（末尾 jump ending_hub）
    # 终章：衔尾蛇（判定结局 → credits → return）

    return
