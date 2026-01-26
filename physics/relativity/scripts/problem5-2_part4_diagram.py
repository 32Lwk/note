import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# 日本語フォントの設定
plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False
# LaTeXレンダリングを有効化（下付き文字のため）
plt.rcParams['text.usetex'] = False  # LaTeXは使わず、matplotlibの数式レンダリングを使用

# パラメータ設定
c = 1.0  # 光速（規格化）
v = 0.6  # 宇宙船の速度（光速の60%）
beta = v / c
gamma = 1 / np.sqrt(1 - beta**2)

# 時刻設定
t1 = 1.0  # 点P到達時刻（S系）
t2 = t1 / gamma  # 点P到達時刻（S'系）
t3 = t2 / gamma  # S'系から見たS系原点の時刻
t_total = 2 * t1  # 往復時間

# 宇宙船の軌跡
# 往路: x = v t (0 ≤ t ≤ t₁)
t_out = np.linspace(0, t1, 100)
x_out = v * t_out
ct_out = c * t_out

# 復路: x = 2v t₁ - v t (t₁ ≤ t ≤ 2t₁)
t_back = np.linspace(t1, t_total, 100)
x_back = 2 * v * t1 - v * t_back
ct_back = c * t_back

# 点Pの座標
x_P = v * t1
ct_P = c * t1

# S'系の同時刻線（速度変化前）
# S'系では、点Pでの時刻t₂と同時刻の点は、S'系のx'軸に平行
# S'系のx'軸は、S系では ct = β x の線
# 同時刻線は、点Pを通り、S'系のx'軸に平行な線
# つまり、ct = β(x - x_P) + ct_P の線
x_simult_Sprime = np.linspace(-0.3, 0.3, 100)
ct_simult_Sprime = beta * (x_simult_Sprime - x_P) + ct_P

# S''系の同時刻線（速度変化後）
# S''系はS系に対して-x方向に速度vで運動
# S''系のx''軸は、S系では ct = -β x の線（符号が逆）
# 同時刻線は、点Pを通り、S''系のx''軸に平行な線
# つまり、ct = -β(x - x_P) + ct_P の線
x_simult_Sdprime = np.linspace(-0.3, 0.3, 100)
ct_simult_Sdprime = -beta * (x_simult_Sdprime - x_P) + ct_P

# S系の原点での時刻
# S'系の同時刻線とS系の原点（x=0）の交点
ct_at_origin_Sprime = beta * (0 - x_P) + ct_P  # これがt₃
# S''系の同時刻線とS系の原点（x=0）の交点
ct_at_origin_Sdprime = -beta * (0 - x_P) + ct_P  # これがt₁

# 図の作成
fig, ax = plt.subplots(figsize=(12, 10))

# 宇宙船の軌跡
ax.plot(x_out, ct_out, 'r-', linewidth=2.5, label='宇宙船の軌跡（往路）')
ax.plot(x_back, ct_back, 'r-', linewidth=2.5, label='宇宙船の軌跡（復路）')

# 点Pをマーク
ax.plot(x_P, ct_P, 'ro', markersize=12, label='点P（速度変化点）', zorder=5)
ax.annotate('P', xy=(x_P, ct_P), xytext=(x_P+0.08, ct_P+0.08),
            fontsize=16, fontweight='bold', color='red', zorder=6)

# t₂を点Pに注釈として追加（S'系での時刻）
ax.annotate(f'$t_2$ = {t2:.3f}\n(S\'系での時刻)', 
            xy=(x_P, ct_P), xytext=(x_P+0.15, ct_P-0.2),
            fontsize=11, fontweight='bold', color='blue',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5),
            zorder=6)

# 原点Oをマーク
ax.plot(0, 0, 'ko', markersize=8, label='原点O', zorder=5)
ax.annotate('O', xy=(0, 0), xytext=(0.05, 0.05),
            fontsize=14, fontweight='bold', zorder=6)

# S'系の同時刻線（速度変化前）
ax.plot(x_simult_Sprime, ct_simult_Sprime, 'b--', linewidth=2, 
        alpha=0.7, label='S\'系の同時刻線（速度変化前）')

# S''系の同時刻線（速度変化後）
ax.plot(x_simult_Sdprime, ct_simult_Sdprime, 'g--', linewidth=2, 
        alpha=0.7, label='S\'\'系の同時刻線（速度変化後）')

# S系の原点での時刻をマーク
ax.plot(0, ct_at_origin_Sprime, 'bs', markersize=10, 
        label=f'S\'系から見たS系原点の時刻 $t_3$ = {ct_at_origin_Sprime:.3f}', zorder=5)
ax.plot(0, ct_at_origin_Sdprime, 'gs', markersize=10, 
        label=f'S\'\'系から見たS系原点の時刻 $t_1$ = {ct_at_origin_Sdprime:.3f}', zorder=5)

# 時刻の差を矢印で示す
arrow = FancyArrowPatch((0.05, ct_at_origin_Sprime), (0.05, ct_at_origin_Sdprime),
                        arrowstyle='<->', mutation_scale=20, 
                        color='purple', linewidth=2.5, zorder=4)
ax.add_patch(arrow)
ax.text(0.12, (ct_at_origin_Sprime + ct_at_origin_Sdprime) / 2,
        f'$\\Delta t = t_1 - t_3$ = {ct_at_origin_Sdprime - ct_at_origin_Sprime:.3f}',
        fontsize=12, fontweight='bold', color='purple',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# 点PからS系原点への補助線
ax.plot([x_P, 0], [ct_P, ct_at_origin_Sprime], 'b:', linewidth=1, alpha=0.5)
ax.plot([x_P, 0], [ct_P, ct_at_origin_Sdprime], 'g:', linewidth=1, alpha=0.5)

# S系の座標軸
ax.axhline(y=0, color='k', linewidth=0.5, alpha=0.3)
ax.axvline(x=0, color='k', linewidth=0.5, alpha=0.3)
ax.grid(True, alpha=0.3, linestyle='--')

# 軸ラベル
ax.set_xlabel('位置 x [規格化単位]', fontsize=14)
ax.set_ylabel('ct [規格化単位]', fontsize=14)
ax.set_title('速度変化時の同時刻の相対性（問題(iv)）', fontsize=16, fontweight='bold')

# 軸の範囲
ax.set_xlim(-0.4, 1.0)
ax.set_ylim(-0.2, 1.5)

# アスペクト比を1:1に
ax.set_aspect('equal', adjustable='box')

# 凡例
ax.legend(loc='upper left', fontsize=10, framealpha=0.9)

# テキスト注釈
info_text = f'パラメータ:\nv = {v:.1f}c, $\\beta$ = {beta:.2f}, $\\gamma$ = {gamma:.2f}\n\n'
info_text += f'時刻の関係:\n$t_1$ = {ct_at_origin_Sdprime:.3f}\n$t_2$ = {t2:.3f}\n$t_3$ = {ct_at_origin_Sprime:.3f}\n\n'
info_text += f'$t_1 - t_3$ = {ct_at_origin_Sdprime - ct_at_origin_Sprime:.3f}\n'
info_text += f'$2(t_1 - t_3)$ = {2*(ct_at_origin_Sdprime - ct_at_origin_Sprime):.3f}'
ax.text(0.65, 0.15, info_text,
        fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig('physics/problem5-2_part4_diagram.png', dpi=300, bbox_inches='tight')
print('時空図を保存しました: physics/problem5-2_part4_diagram.png')
print(f't1 = {ct_at_origin_Sdprime:.3f}, t3 = {ct_at_origin_Sprime:.3f}, t1 - t3 = {ct_at_origin_Sdprime - ct_at_origin_Sprime:.3f}')

