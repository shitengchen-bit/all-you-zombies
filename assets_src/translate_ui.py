# -*- coding: utf-8 -*-
# 批量将 screens.rpy / options.rpy 的英文 UI 字符串替换为中文
# 仅替换 _("...") 形式的完整字符串，避免误伤子串
import io, os

GAME = r"C:\Users\sunshuai\all_you_zombies\game"

# 英文 -> 中文 映射（玩家可见的界面字符串）
MAP = {
    # 快捷菜单
    "Back": "返回",
    "History": "历史",
    "Skip": "跳过",
    "Auto": "自动",
    "Save": "保存",
    "Q.Save": "快存",
    "Q.Load": "快读",
    "Prefs": "设置",
    # 主菜单 / 游戏菜单
    "Start": "开始游戏",
    "Load": "读取",
    "Preferences": "设置",
    "About": "关于",
    "Help": "帮助",
    "Quit": "退出",
    "Return": "返回",
    "Main Menu": "主菜单",
    "End Replay": "结束回放",
    "Menu": "菜单",
    # 偏好设置分类与选项
    "Display": "显示",
    "Sound": "声音",
    "Text": "文本",
    "Language": "语言",
    "Window": "窗口",
    "Fullscreen": "全屏",
    "Text Speed": "文字速度",
    "Auto-Forward Time": "自动前进时间",
    "Music Volume": "音乐音量",
    "Sound Volume": "音效音量",
    "Voice Volume": "语音音量",
    "Mute All": "全部静音",
    "Transitions": "转场",
    "Unseen Text": "未读文本",
    "After Choices": "选择之后",
    "Skipping": "跳过模式",
    "Test": "测试",
    "Calibrate": "校准",
    # 存档/读档
    "Page {}": "第 {} 页",
    "empty slot": "空档位",
    "Automatic saves": "自动存档",
    "Quick saves": "快速存档",
    # 通用
    "Yes": "是",
    "No": "否",
    # 帮助/操作说明
    "Advances dialogue and activates the interface.": "推进对话并激活界面。",
    "Advances dialogue without selecting choices.": "推进对话但不选择选项。",
    "Rolls back to earlier dialogue.": "回退到之前的对话。",
    "Rolls forward to later dialogue.": "前进到之后的对话。",
    "Hides the user interface.": "隐藏用户界面。",
    "Takes a screenshot.": "截图。",
    "Toggles dialogue skipping.": "切换对话跳过。",
    "Skips dialogue while held down.": "按住时跳过对话。",
    "Accesses the game menu.": "打开游戏菜单。",
    "Opens the accessibility menu.": "打开辅助功能菜单。",
    "Navigate the interface.": "在界面中导航。",
    "The dialogue history is empty.": "对话历史为空。",
    # 帮助中的输入设备/按键（保留通用术语，部分汉化）
    "Keyboard": "键盘",
    "Mouse": "鼠标",
    "Gamepad": "手柄",
    "Enter": "回车",
    "Space": "空格",
    "Arrow Keys": "方向键",
    "Page Up": "上翻页",
    "Page Down": "下翻页",
    "Left Click": "左键",
    "Right Click": "右键",
    "Middle Click": "中键",
    "Mouse Wheel Up": "滚轮上",
    "Mouse Wheel Down": "滚轮下",
    "Ctrl": "Ctrl",
    "Tab": "Tab",
    "Escape": "Esc",
}

def apply_map(path):
    with io.open(path, "r", encoding="utf-8") as f:
        content = f.read()
    count = 0
    for en, zh in MAP.items():
        needle = '_("%s")' % en
        repl = '_("%s")' % zh
        if needle in content:
            n = content.count(needle)
            content = content.replace(needle, repl)
            count += n
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return count

for fn in ["screens.rpy", "options.rpy"]:
    p = os.path.join(GAME, fn)
    if os.path.exists(p):
        c = apply_map(p)
        print("%s: replaced %d UI strings" % (fn, c))
print("DONE")
