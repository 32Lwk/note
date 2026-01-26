import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle
import matplotlib.patches as mpatches
import platform
from matplotlib import font_manager

# 日本語フォントの設定
if platform.system() == 'Darwin':  # macOS
    # macOSで利用可能な日本語フォントを探す
    fonts_to_try = ['Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'AppleGothic', 'Arial Unicode MS']
    font_found = False
    for font_name in fonts_to_try:
        # システムにインストールされているフォントを確認
        available_fonts = [f.name for f in font_manager.fontManager.ttflist]
        if font_name in available_fonts:
            plt.rcParams['font.family'] = font_name
            font_found = True
            break
    if not font_found:
        # フォールバック: システムのデフォルト日本語フォントを使用
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'AppleGothic', 'Arial Unicode MS', 'DejaVu Sans']
elif platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'MS Gothic'
else:  # Linux
    plt.rcParams['font.family'] = 'Noto Sans CJK JP'

# 負の符号の表示を正しくする
plt.rcParams['axes.unicode_minus'] = False

# 図1: 問題(1)の確率の可視化
fig1, axes1 = plt.subplots(1, 3, figsize=(15, 5))

# (1-i) すべて赤球
ax1 = axes1[0]
ax1.bar(['すべて赤球', 'その他'], [1/27, 26/27], color=['red', 'lightgray'])
ax1.set_ylabel('確率')
ax1.set_title('(1-i) すべて赤球である確率')
ax1.set_ylim(0, 1)
ax1.text(0, 1/27 + 0.02, f'{1/27:.4f}', ha='center', fontsize=12)

# (1-ii) すべて異なる色
ax2 = axes1[1]
ax2.bar(['すべて異なる色', 'その他'], [6/27, 21/27], color=['blue', 'lightgray'])
ax2.set_ylabel('確率')
ax2.set_title('(1-ii) すべて異なる色である確率')
ax2.set_ylim(0, 1)
ax2.text(0, 6/27 + 0.02, f'{6/27:.4f}', ha='center', fontsize=12)

# (1-iii) ちょうど1個だけが赤球
ax3 = axes1[2]
ax3.bar(['ちょうど1個が赤', 'その他'], [12/27, 15/27], color=['green', 'lightgray'])
ax3.set_ylabel('確率')
ax3.set_title('(1-iii) ちょうど1個だけが赤球である確率')
ax3.set_ylim(0, 1)
ax3.text(0, 12/27 + 0.02, f'{12/27:.4f}', ha='center', fontsize=12)

plt.tight_layout()
plt.savefig('math_probability_fig1.png', dpi=300, bbox_inches='tight')
plt.close()

# 図2: 問題(2-i)の確率の可視化
fig2, ax2 = plt.subplots(figsize=(10, 6))

# 袋Fから3個取り出す場合の数と確率
combinations = [
    ('赤2・白1', 1, 1/10, 'P+2, Q+1'),
    ('赤2・黒1', 2, 2/10, 'P+2, Q+0'),
    ('赤1・白1・黒1', 4, 4/10, 'P+1, Q+1'),
    ('赤1・黒2', 2, 2/10, 'P+1, Q+0'),
    ('赤0・白1・黒2', 1, 1/10, 'P+0, Q+1')
]

labels = [f'{c[0]}\n({c[3]})' for c in combinations]
counts = [c[1] for c in combinations]
probs = [c[2] for c in combinations]

colors = ['red' if '赤2' in c[0] else 'orange' if '赤1' in c[0] else 'blue' for c in combinations]

bars = ax2.bar(range(len(combinations)), probs, color=colors, alpha=0.7)
ax2.set_xlabel('取り出し方')
ax2.set_ylabel('確率')
ax2.set_title('(2-i) 袋Fから3個の球を取り出す確率分布')
ax2.set_xticks(range(len(combinations)))
ax2.set_xticklabels(labels, rotation=45, ha='right')
ax2.set_ylim(0, 0.5)

# 確率の値を表示
for i, (bar, prob) in enumerate(zip(bars, probs)):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.01,
             f'{prob:.2f}\n({counts[i]}/10)',
             ha='center', va='bottom', fontsize=9)

# p=1, q=1となる組み合わせを強調
ax2.bar(2, probs[2], color='green', alpha=0.5, edgecolor='green', linewidth=3)
ax2.text(2, probs[2] + 0.03, 'p=1, q=1', ha='center', fontsize=10, 
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

plt.tight_layout()
plt.savefig('math_probability_fig2.png', dpi=300, bbox_inches='tight')
plt.close()

# 図3: 問題(2-ii)の確率の可視化
fig3, ax3 = plt.subplots(figsize=(12, 8))

# 2回の操作でp=3, q=1となる4つのケース
cases = [
    ('ケース1-1', '1回目: 赤1・白1・黒1\n2回目: 赤2・黒1', 2/5 * 1/5, 'P+1→+2, Q+1→+0'),
    ('ケース1-2', '1回目: 赤1・黒2\n2回目: 赤2・白1', 1/5 * 1/10, 'P+1→+2, Q+0→+1'),
    ('ケース2-1', '1回目: 赤2・白1\n2回目: 赤1・黒2', 1/10 * 1/5, 'P+2→+1, Q+1→+0'),
    ('ケース2-2', '1回目: 赤2・黒1\n2回目: 赤1・白1・黒1', 1/5 * 2/5, 'P+2→+1, Q+0→+1')
]

case_names = [c[0] for c in cases]
case_probs = [c[2] for c in cases]
case_descriptions = [c[1] for c in cases]

bars = ax3.bar(range(len(cases)), case_probs, color=['red', 'blue', 'green', 'orange'], alpha=0.7)
ax3.set_xlabel('ケース')
ax3.set_ylabel('確率')
ax3.set_title('(2-ii) 2回の操作でp=3, q=1となる確率（各ケース）')
ax3.set_xticks(range(len(cases)))
ax3.set_xticklabels(case_names)
ax3.set_ylim(0, max(case_probs) * 1.3)

# 確率の値を表示
for i, (bar, prob, desc) in enumerate(zip(bars, case_probs, case_descriptions)):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + max(case_probs) * 0.05,
             f'{prob:.4f}\n{desc}',
             ha='center', va='bottom', fontsize=8)

# 合計確率を表示
total_prob = sum(case_probs)
ax3.axhline(y=total_prob, color='black', linestyle='--', linewidth=2, label=f'合計: {total_prob:.4f}')
ax3.text(len(cases)/2 - 0.5, total_prob + max(case_probs) * 0.05,
         f'合計確率: {total_prob:.4f} = 1/5',
         ha='center', fontsize=12, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
ax3.legend()

plt.tight_layout()
plt.savefig('math_probability_fig3.png', dpi=300, bbox_inches='tight')
plt.close()

# 図4: 問題(2-iii)の確率の可視化
fig4, axes4 = plt.subplots(1, 2, figsize=(16, 6))

# 左図: p+q=4となる各ケースの確率
ax4a = axes4[0]
cases_iii = [
    ('(4, 0)', 1/625, 'p>q'),
    ('(3, 1)', 2/625, 'p>q'),
    ('(2, 2)', 3/1250, 'p=q'),
    ('(1, 3)', 1/1250, 'p<q'),
    ('(0, 4)', 1/10000, 'p<q')
]

case_labels = [c[0] for c in cases_iii]
case_probs_iii = [c[1] for c in cases_iii]
case_relations = [c[2] for c in cases_iii]

colors_iii = ['green' if r == 'p>q' else 'red' if r == 'p<q' else 'gray' for r in case_relations]

bars4a = ax4a.bar(range(len(cases_iii)), case_probs_iii, color=colors_iii, alpha=0.7)
ax4a.set_xlabel('(p, q)')
ax4a.set_ylabel('確率')
ax4a.set_title('(2-iii) p+q=4となる各ケースの確率')
ax4a.set_xticks(range(len(cases_iii)))
ax4a.set_xticklabels(case_labels)

# 確率の値を表示
for i, (bar, prob) in enumerate(zip(bars4a, case_probs_iii)):
    height = bar.get_height()
    ax4a.text(bar.get_x() + bar.get_width()/2., height + max(case_probs_iii) * 0.1,
             f'{prob:.6f}',
             ha='center', va='bottom', fontsize=9)

# 凡例
green_patch = mpatches.Patch(color='green', label='p>q', alpha=0.7)
gray_patch = mpatches.Patch(color='gray', label='p=q', alpha=0.7)
red_patch = mpatches.Patch(color='red', label='p<q', alpha=0.7)
ax4a.legend(handles=[green_patch, gray_patch, red_patch])

# 右図: 条件付き確率の計算
ax4b = axes4[1]

# p+q=4の全確率
total_prob_4 = sum(case_probs_iii)
# p>qかつp+q=4の確率
p_greater_q_prob = case_probs_iii[0] + case_probs_iii[1]

categories = ['P(p>q ∩ p+q=4)', 'P(p+q=4)の\nその他', 'P(p+q=4)']
values = [p_greater_q_prob, total_prob_4 - p_greater_q_prob, total_prob_4]
colors_b = ['green', 'lightgray', 'blue']

bars4b = ax4b.bar(categories, values, color=colors_b, alpha=0.7)
ax4b.set_ylabel('確率')
ax4b.set_title('(2-iii) 条件付き確率の計算')

# 確率の値を表示
for bar, val in zip(bars4b, values):
    height = bar.get_height()
    ax4b.text(bar.get_x() + bar.get_width()/2., height + max(values) * 0.02,
             f'{val:.6f}',
             ha='center', va='bottom', fontsize=10)

# 条件付き確率を表示
conditional_prob = p_greater_q_prob / total_prob_4
ax4b.text(1.5, max(values) * 0.7,
         f'P(p>q | p+q=4)\n= {p_greater_q_prob:.6f} / {total_prob_4:.6f}\n= {conditional_prob:.6f}\n= {conditional_prob*27:.0f}/27',
         ha='center', fontsize=11, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

plt.tight_layout()
plt.savefig('math_probability_fig4.png', dpi=300, bbox_inches='tight')
plt.close()

# 図5: 問題(2)の操作の流れの可視化
fig5, ax5 = plt.subplots(figsize=(14, 8))

# 数直線上の点P, Qの移動を可視化
# (2-i)の例
ax5.text(0.1, 0.9, '(2-i) 1回の操作後、p=1, q=1', fontsize=14, fontweight='bold',
         transform=ax5.transAxes)

# 数直線
ax5.axhline(y=0.7, xmin=0.1, xmax=0.9, color='black', linewidth=2)
ax5.plot([0.1, 0.1], [0.65, 0.75], 'k-', linewidth=2)  # 原点
ax5.text(0.1, 0.6, '0', ha='center', fontsize=12)

# Pの移動
ax5.arrow(0.1, 0.72, 0.1, 0, head_width=0.02, head_length=0.01, 
          fc='blue', ec='blue', linewidth=2)
ax5.plot([0.2, 0.2], [0.65, 0.75], 'b-', linewidth=2)
ax5.text(0.2, 0.6, 'P=1', ha='center', fontsize=10, color='blue')

# Qの移動
ax5.arrow(0.1, 0.68, 0.1, 0, head_width=0.02, head_length=0.01, 
          fc='red', ec='red', linewidth=2)
ax5.plot([0.2, 0.2], [0.65, 0.75], 'r-', linewidth=2)
ax5.text(0.2, 0.55, 'Q=1', ha='center', fontsize=10, color='red')

ax5.text(0.15, 0.8, '赤1・白1・黒1\nを取り出す', ha='center', fontsize=10,
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# (2-ii)の例
ax5.text(0.1, 0.4, '(2-ii) 2回の操作後、p=3, q=1', fontsize=14, fontweight='bold',
         transform=ax5.transAxes)

# 数直線
ax5.axhline(y=0.2, xmin=0.1, xmax=0.9, color='black', linewidth=2)
ax5.plot([0.1, 0.1], [0.15, 0.25], 'k-', linewidth=2)  # 原点
ax5.text(0.1, 0.1, '0', ha='center', fontsize=12)

# 1回目
ax5.arrow(0.1, 0.22, 0.15, 0, head_width=0.015, head_length=0.01, 
          fc='blue', ec='blue', linewidth=1.5)
ax5.text(0.175, 0.3, '1回目\nP+1, Q+1', ha='center', fontsize=8, color='blue',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

# 2回目
ax5.arrow(0.25, 0.22, 0.15, 0, head_width=0.015, head_length=0.01, 
          fc='blue', ec='blue', linewidth=1.5)
ax5.plot([0.4, 0.4], [0.15, 0.25], 'b-', linewidth=2)
ax5.text(0.4, 0.1, 'P=3', ha='center', fontsize=10, color='blue')

ax5.text(0.325, 0.3, '2回目\nP+2, Q+0', ha='center', fontsize=8, color='blue',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

ax5.text(0.25, 0.05, 'Q=1 (1回目のみ白球を含む)', ha='center', fontsize=10, color='red')

ax5.set_xlim(0, 1)
ax5.set_ylim(0, 1)
ax5.axis('off')

plt.tight_layout()
plt.savefig('math_probability_fig5.png', dpi=300, bbox_inches='tight')
plt.close()

print("図の作成が完了しました。")
print("- math_probability_fig1.png: 問題(1)の確率")
print("- math_probability_fig2.png: 問題(2-i)の確率分布")
print("- math_probability_fig3.png: 問題(2-ii)の各ケースの確率")
print("- math_probability_fig4.png: 問題(2-iii)の条件付き確率")
print("- math_probability_fig5.png: 操作の流れの可視化")

