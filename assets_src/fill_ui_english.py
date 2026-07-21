# -*- coding: utf-8 -*-
# 将 tl/english/screens.rpy 和 options.rpy 中的 new "中文" 填成英文
import io, os, re

D = r"C:\Users\sunshuai\all_you_zombies\game\tl\english"

# 中文 -> 英文（界面字符串）
EN = {
    "返回": "Back", "历史": "History", "跳过": "Skip", "自动": "Auto",
    "保存": "Save", "快存": "Q.Save", "快读": "Q.Load", "设置": "Preferences",
    "开始游戏": "Start", "读取": "Load", "关于": "About", "帮助": "Help",
    "退出": "Quit", "主菜单": "Main Menu", "结束回放": "End Replay", "菜单": "Menu",
    "显示": "Display", "声音": "Sound", "文本": "Text", "语言": "Language",
    "窗口": "Window", "全屏": "Fullscreen", "文字速度": "Text Speed",
    "自动前进时间": "Auto-Forward Time", "音乐音量": "Music Volume",
    "音效音量": "Sound Volume", "语音音量": "Voice Volume", "全部静音": "Mute All",
    "转场": "Transitions", "未读文本": "Unseen Text", "选择之后": "After Choices",
    "跳过模式": "Skipping", "测试": "Test", "校准": "Calibrate",
    "第 {} 页": "Page {}", "空档位": "empty slot", "自动存档": "Automatic saves",
    "快速存档": "Quick saves", "是": "Yes", "否": "No",
    "推进对话并激活界面。": "Advances dialogue and activates the interface.",
    "推进对话但不选择选项。": "Advances dialogue without selecting choices.",
    "回退到之前的对话。": "Rolls back to earlier dialogue.",
    "前进到之后的对话。": "Rolls forward to later dialogue.",
    "隐藏用户界面。": "Hides the user interface.",
    "截图。": "Takes a screenshot.",
    "切换对话跳过。": "Toggles dialogue skipping.",
    "按住时跳过对话。": "Skips dialogue while held down.",
    "打开游戏菜单。": "Accesses the game menu.",
    "打开辅助功能菜单。": "Opens the accessibility menu.",
    "在界面中导航。": "Navigate the interface.",
    "对话历史为空。": "The dialogue history is empty.",
    "键盘": "Keyboard", "鼠标": "Mouse", "手柄": "Gamepad",
    "回车": "Enter", "空格": "Space", "方向键": "Arrow Keys",
    "上翻页": "Page Up", "下翻页": "Page Down",
    "左键": "Left Click", "右键": "Right Click", "中键": "Middle Click",
    "滚轮上": "Mouse Wheel Up", "滚轮下": "Mouse Wheel Down",
    # 关于界面
    "原著小说": "Original Story",
    "罗伯特·海因莱因《你们这些还魂尸》": "Robert A. Heinlein, \"All You Zombies\"",
    "改编 · 剧本": "Adaptation & Script",
    "程序": "Code",
    "美术": "Art",
    "sunshuai（AI 辅助生成）": "sunshuai (AI-assisted)",
    "本作是基于海因莱因同名小说的原创同人改编，非商业作品，谨向原作致敬。":
        "An original fan adaptation based on Heinlein's story of the same name. Non-commercial, made in tribute to the original.",
}

def fill_new(path):
    with io.open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    out = []
    changed = 0
    for line in lines:
        m = re.match(r'^(\s*new )"(.*)"\s*$', line)
        if m:
            zh = m.group(2)
            if zh in EN:
                en = EN[zh].replace('"', '\\"')
                out.append('%s"%s"\n' % (m.group(1), en))
                changed += 1
                continue
        out.append(line)
    with io.open(path, "w", encoding="utf-8") as f:
        f.writelines(out)
    return changed

for fn in ["screens.rpy", "options.rpy"]:
    p = os.path.join(D, fn)
    if os.path.exists(p):
        c = fill_new(p)
        print("%s: filled %d English UI strings" % (fn, c))
print("DONE")
