# 自定义转场与基础图像定义 - definitions.rpy
# 修复 lint 报告的未定义转场（slow_dissolve/slow_fade/flash）与 white 图像

# ============ 自定义转场 ============
# 慢速溶解（用于闪回浸入/返回，1.5秒）
define slow_dissolve = Dissolve(1.5)

# 慢速淡出（用于沉重场景切换，1.5秒）
define slow_fade = Fade(1.5, 0.0, 1.5)

# 白闪（用于时间旅行启动的强光，快速白闪）
define flash = Fade(0.4, 0.2, 0.4, color="#ffffff")

# ============ 基础纯色图像 ============
# 白色场景（时间旅行强光过渡用）
image white = Solid("#ffffff")

# 黑色场景（标准黑场，Ren'Py 通常内置 black，此处确保可用）
image black = Solid("#000000")
