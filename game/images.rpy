# 图像显式定义 - images.rpy
# 显式映射每个图像标签到文件路径（不依赖自动定义，避免下划线/空格歧义）
# 路径相对于 game/ 目录

# ============ 场景背景 (1920x1080, 时代分层调色) ============
image bg bar_main = "images/bg/bar_.jpg"               # 1970 酒吧（主场景，阴暗颓废）
image bg orphanage_ext = "images/bg/orphanage.jpg"      # 1945 孤儿院外观（冷灰蓝）
image bg orphanage_int = "images/bg/orphanage.jpg"      # 1945 孤儿院内部（冷灰蓝）
image bg park_spring = "images/bg/park_sp.jpg"          # 1963 公园·春（明亮温暖）
image bg park_night = "images/bg/park_n.jpg"            # 1963 公园·夜（冷调诀别）
image bg hospital_corridor = "images/bg/hospital_corr.jpg"  # 1964 医院走廊（临床冷）
image bg street_rain = "images/bg/street_.jpg"          # 1964 雨夜街道（湿冷霓虹）
image bg time_lab = "images/bg/time.jpg"                # 1970 时间实验室（冰冷科技）
image bg time_vortex = "images/bg/time_vo.jpg"          # 时间漩涡（抽象）
image bg bureau_office = "images/bg/bureau_of.jpg"      # 1985 时间局办公室（灰）
image bg room_1993 = "images/bg/room_.jpg"              # 1993 房间（暮色暖灰）

# ============ 事件 CG ============
image cg baby_left = "images/cg/baby_.jpg"              # T1 婴儿被弃
image cg first_kiss = "images/cg/first_.jpg"            # T2 初吻
image cg empty_bench = "images/cg/empty_b.jpg"          # T3 空长椅
image cg surgery = "images/cg/sur.jpg"                  # T4 手术台觉醒
image cg baby_taken = "images/cg/baby_t.jpg"            # T4 婴儿被抱走
image cg time_pod = "images/cg/time.jpg"                # 第二幕 时间舱启动
image cg silhouettes = "images/cg/silhoue.jpg"          # 第三幕 漩涡剪影
image cg baby_returned = "images/cg/baby_retu.jpg"      # 第三幕 酒保送回婴儿
image cg ouroboros_light = "images/cg/ouroboros_l.jpg"  # 顿悟结局 衔尾蛇光环
image cg scar = "images/cg/.jpg"                        # 隐藏结局 剖腹产疤痕
image cg all_forms = "images/cg/all_f.jpg"              # 彩蛋 全形态合影

# ============ 角色立绘 ============
image john neutral = "images/john/neutral.png"              # 约翰/叙述者（男性外表+女性暗示）
image jane neutral = "images/jane/neutral.png"              # 简（少女，明确女性）
image stranger silhouette = "images/stranger/silhouette.png"  # 公园里的陌生男人（逆光剪影）
