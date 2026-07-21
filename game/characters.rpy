# 角色定义 - characters.rpy
# 所有角色均为原创戏剧化改编形象

# 叙述/内心独白（酒保的第一人称内心声音，无名字框，斜体）
define narr = Character(None, kind=nvl, what_italic=True)
# 注：实际用 Character(None) 作旁白；内心独白用专门的 monologue
define mono = Character(None, what_prefix="", what_italic=True,
                        what_color="#a8b0a0")

# 酒保（玩家扮演的角色，开口说话时）
# 灰绿色调，呼应共有特征"灰绿眼"
define bart = Character("酒保", color="#6b8e7f", what_color="#d8e0d0")

# 约翰 / "未婚妈妈"（酒馆叙述者，男性外表+微妙女性暗示）
# 苦涩的琥珀褐
define john = Character("约翰", color="#a06a3c", what_color="#e8d8c0")

# 简（少女时期，1945-1963，明确女性）
# 温暖的玫瑰金
define jane = Character("简", color="#c08497", what_color="#f0dce0")

# 公园里的陌生男人（实为重返的约翰，神秘、逆光）
# 朦胧的灰蓝
define stranger = Character("???", color="#7a8aa0", what_color="#d0d8e0")

# 时间局相关（旁白式系统音）
define bureau = Character("时间局", color="#5a7a9a", what_color="#c0d0e0")

# 通用旁白（环境描写、转场）
define n = Character(None)
