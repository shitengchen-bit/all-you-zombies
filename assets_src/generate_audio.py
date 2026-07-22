# -*- coding: utf-8 -*-
# 合成占位环境音（BGM + SFX）。原创合成音频，非版权素材。
# 用 numpy/scipy 生成氛围垫音（无缝循环）与音效，保存为 WAV。
import os
import numpy as np
from scipy.io import wavfile
from scipy.signal import lfilter

SR = 44100
BASE = r"C:\Users\sunshuai\all_you_zombies\game\audio"

def m2f(n):
    return 440.0 * (2.0 ** ((n - 69) / 12.0))

def lowpass(x, cutoff, sr=SR):
    rc = 1.0 / (2.0 * np.pi * cutoff)
    dt = 1.0 / sr
    a = dt / (rc + dt)
    return lfilter([a], [1.0, a - 1.0], x)

def highpass(x, cutoff, sr=SR):
    rc = 1.0 / (2.0 * np.pi * cutoff)
    dt = 1.0 / sr
    a = rc / (rc + dt)
    return lfilter([a, -a], [1.0, a - 1.0], x)

def osc(freq, dur, sr=SR):
    t = np.arange(int(dur * sr)) / sr
    return np.sin(2.0 * np.pi * freq * t)

def pad(notes, dur, sr=SR, detune=2.0, trem_rate=0.15, trem_depth=0.25,
        brightness=1200.0, noise_amt=0.015, voices=3):
    """氛围垫音：多音符 + 失谐多声部 + 颤音 + 低通 + 微弱噪声纹理。"""
    n = int(dur * sr)
    t = np.arange(n) / sr
    out = np.zeros(n)
    for m in notes:
        f = m2f(m)
        for v in range(voices):
            det = f * (1.0 + (v - (voices - 1) / 2.0) * detune / 1000.0)
            phase = np.random.uniform(0, 2 * np.pi)
            out += np.sin(2.0 * np.pi * det * t + phase) / voices
    out /= len(notes)
    # 颤音（缓慢幅度调制）
    lfo = 1.0 - trem_depth * (0.5 + 0.5 * np.sin(2.0 * np.pi * trem_rate * t))
    out *= lfo
    # 低通控制明暗
    out = lowpass(out, brightness)
    # 微弱噪声纹理（空气感）
    if noise_amt > 0:
        nz = np.random.randn(n)
        nz = lowpass(nz, brightness * 0.8)
        out += nz * noise_amt
    return out

def seamless_loop(audio, cf_sec=5.0, sr=SR):
    """交叉淡入淡出制作无缝循环。"""
    cf = int(cf_sec * sr)
    L = len(audio)
    result = audio[0:L - cf].copy()
    head = audio[0:cf]
    tail = audio[L - cf:L]
    fade = np.linspace(0.0, 1.0, cf)
    result[0:cf] = head * fade + tail * (1.0 - fade)
    return result

def envelope(audio, attack=2.0, release=2.0, sr=SR):
    n = len(audio)
    a = int(attack * sr)
    r = int(release * sr)
    env = np.ones(n)
    if a > 0:
        env[:a] = np.linspace(0, 1, a)
    if r > 0:
        env[-r:] = np.linspace(1, 0, r)
    return audio * env

def save(path, audio, sr=SR, gain=0.8):
    audio = np.asarray(audio, dtype=np.float64)
    peak = np.max(np.abs(audio))
    if peak > 0:
        audio = audio / peak * gain
    audio = np.clip(audio, -1.0, 1.0)
    wavfile.write(path, sr, (audio * 32767).astype(np.int16))
    print("  wrote %s (%.1fs, %.2fMB)" % (os.path.basename(path), len(audio)/sr,
          os.path.getsize(path)/1e6))

def make_bgm(name, notes, dur=30.0, **kw):
    gain = kw.pop("gain", 0.7)
    raw = pad(notes, dur, **kw)
    raw = envelope(raw, attack=2.5, release=2.5)
    loop = seamless_loop(raw, cf_sec=5.0)
    save(os.path.join(BASE, "bgm", name + ".wav"), loop, gain=gain)

# ---------------- BGM 轨道 ----------------
print("Generating BGM...")
# 酒吧主题：noir 小调七和弦，低沉阴郁
make_bgm("bar_main", [45, 48, 52, 55], brightness=750, trem_rate=0.13, trem_depth=0.3, noise_amt=0.02)
# 孤儿院：冷寂开放五度 + 极弱高音
make_bgm("orphanage", [45, 52], brightness=550, trem_rate=0.08, trem_depth=0.2, noise_amt=0.025, gain=0.55)
# 初恋：温暖大调，明亮轻柔
make_bgm("park_love", [48, 52, 55, 57], brightness=2200, trem_rate=0.3, trem_depth=0.2, noise_amt=0.01, gain=0.65)
# 被抛弃：小调，更低更暗
make_bgm("park_loss", [45, 48, 52], brightness=850, trem_rate=0.11, trem_depth=0.3, noise_amt=0.02, gain=0.6)
# 医院：低频嗡鸣 + 心跳 + 冷高音
def hospital():
    dur = 30.0
    n = int(dur * SR)
    t = np.arange(n) / SR
    hum = np.sin(2*np.pi*55*t) * 0.4
    hum = lowpass(hum, 200)
    # 心跳（约60BPM，lub-dub）
    beat = np.zeros(n)
    bpm = 1.0  # 1Hz
    for bt in np.arange(0, dur, 1.0/bpm):
        i0 = int(bt * SR)
        seg = np.arange(int(0.18*SR))/SR
        thump = np.sin(2*np.pi*50*seg) * np.exp(-seg*22)
        if i0 + len(thump) < n:
            beat[i0:i0+len(thump)] += thump * 0.5
        i1 = int((bt+0.12)*SR)
        if i1 + len(thump) < n:
            beat[i1:i1+len(thump)] += thump * 0.3
    beat = lowpass(beat, 150)
    sterile = np.sin(2*np.pi*m2f(81)*t) * 0.04  # 冷高音
    out = hum + beat + sterile
    out = envelope(out, 2.5, 2.5)
    loop = seamless_loop(out, 5.0)
    save(os.path.join(BASE, "bgm", "hospital.wav"), loop, gain=0.7)
hospital()
# 时间漩涡：不和谐和弦 + 旋转声像调制
def vortex():
    dur = 30.0
    n = int(dur*SR); t = np.arange(n)/SR
    notes = [45, 51, 55, 58]
    out = np.zeros(n)
    for k, m in enumerate(notes):
        f = m2f(m)
        lfo = 0.5 + 0.5*np.sin(2*np.pi*0.1*t + k*np.pi/2)  # 相位错开旋转
        out += np.sin(2*np.pi*f*t) * lfo / len(notes)
    out = lowpass(out, 1500)
    out += np.random.randn(n)*0.01
    out = envelope(out, 2.5, 2.5)
    loop = seamless_loop(out, 5.0)
    save(os.path.join(BASE, "bgm", "time_vortex.wav"), loop, gain=0.65)
vortex()
# 时间旅行：电子脉冲合成
def timetravel():
    dur = 30.0
    n = int(dur*SR); t = np.arange(n)/SR
    base = np.sin(2*np.pi*m2f(45)*t) + 0.5*np.sin(2*np.pi*m2f(52)*t)
    # 加入谐波使其更"电子"
    base += 0.3*np.sin(2*np.pi*m2f(45)*2*t) + 0.2*np.sin(2*np.pi*m2f(45)*3*t)
    pulse = 0.5 + 0.5*np.sin(2*np.pi*1.5*t)  # 1.5Hz 脉冲
    out = base * pulse * 0.4
    out = lowpass(out, 2500)
    out = envelope(out, 2.0, 2.0)
    loop = seamless_loop(out, 5.0)
    save(os.path.join(BASE, "bgm", "timetravel.wav"), loop, gain=0.6)
timetravel()
# 1993房间：安静温暖
make_bgm("room_1993", [48, 55, 57], brightness=1500, trem_rate=0.1, trem_depth=0.18, noise_amt=0.012, gain=0.5)
# 结局基础
make_bgm("ending_base", [45, 48, 52], brightness=1000, trem_rate=0.12, trem_depth=0.25, gain=0.6)
# 结局-愤恨：不和谐低簇，急促
make_bgm("ending_rage", [45, 46, 52], brightness=700, trem_rate=0.5, trem_depth=0.4, noise_amt=0.02, gain=0.65)
# 结局-释然：解决的大调，缓慢明亮
make_bgm("ending_peace", [48, 52, 55, 57], brightness=2000, trem_rate=0.1, trem_depth=0.18, noise_amt=0.01, gain=0.65)
# 结局-困惑：摇摆交替 + 颤音
def vertigo():
    dur = 30.0
    n = int(dur*SR); t = np.arange(n)/SR
    chordA = sum(np.sin(2*np.pi*m2f(m)*t) for m in [45,52])/2
    chordB = sum(np.sin(2*np.pi*m2f(m)*t) for m in [46,53])/2
    mix = 0.5 + 0.5*np.sin(2*np.pi*0.12*t)
    out = chordA*mix + chordB*(1-mix)
    vib = 1.0 + 0.003*np.sin(2*np.pi*5*t)  # 轻微音高颤抖
    out = out * 0.4
    out = lowpass(out, 1200)
    out = envelope(out, 2.5, 2.5)
    loop = seamless_loop(out, 5.0)
    save(os.path.join(BASE, "bgm", "ending_vertigo.wav"), loop, gain=0.6)
vertigo()
# 结局-顿悟：明亮丰满大调 + 微光高谐波
make_bgm("ending_epiphany", [48, 52, 55, 57, 60], brightness=3000, trem_rate=0.15, trem_depth=0.2, noise_amt=0.008, gain=0.65)

# ---------------- SFX ----------------
print("Generating SFX...")
# 雨声（循环）：滤波白噪声
def rain():
    dur = 12.0
    n = int(dur*SR)
    nz = np.random.randn(n)
    nz = lowpass(nz, 4000)
    nz = highpass(nz, 200)
    # 轻微起伏
    t = np.arange(n)/SR
    nz *= 0.7 + 0.3*np.sin(2*np.pi*0.2*t)
    nz = envelope(nz, 1.0, 1.0)
    loop = seamless_loop(nz, 2.0)
    save(os.path.join(BASE, "sfx", "rain.wav"), loop, gain=0.35)
rain()
# 线索发现：清脆铃叮
def clue():
    dur = 1.8
    t = np.arange(int(dur*SR))/SR
    tone = np.sin(2*np.pi*880*t) + 0.5*np.sin(2*np.pi*1320*t) + 0.3*np.sin(2*np.pi*1760*t)
    tone *= np.exp(-t*3.0)
    save(os.path.join(BASE, "sfx", "clue.wav"), tone, gain=0.5)
clue()

print("DONE")
