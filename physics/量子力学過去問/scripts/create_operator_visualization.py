#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演算子の作用の視覚化スクリプト
PDF化した際にも数式が正しく表示されるように画像として生成
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import numpy as np

# 日本語フォントの設定
plt.rcParams['font.family'] = 'DejaVu Sans'
# 日本語を表示するためのフォント設定（システムに応じて変更可能）
try:
    # macOSの場合
    plt.rcParams['font.family'] = 'Hiragino Sans'
except:
    try:
        # Linuxの場合
        plt.rcParams['font.family'] = 'Noto Sans CJK JP'
    except:
        # フォールバック
        plt.rcParams['font.family'] = 'sans-serif'

plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False

# 図1: 演算子の作用の方向
fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.axis('off')

# 演算子と状態の配置
x_start = 0.1
x_mid = 0.5
x_end = 0.9
y = 0.5

# 演算子のボックス
operator_box = mpatches.FancyBboxPatch(
    (x_start, y-0.15), 0.2, 0.3,
    boxstyle="round,pad=0.05",
    facecolor='lightblue',
    edgecolor='black',
    linewidth=2
)
ax1.add_patch(operator_box)
ax1.text(x_start+0.1, y, r'$\hat{a}$', ha='center', va='center', fontsize=20, fontweight='bold')

# 状態のボックス
state_box = mpatches.FancyBboxPatch(
    (x_end-0.2, y-0.15), 0.2, 0.3,
    boxstyle="round,pad=0.05",
    facecolor='lightgreen',
    edgecolor='black',
    linewidth=2
)
ax1.add_patch(state_box)
ax1.text(x_end-0.1, y, r'$|0\rangle$', ha='center', va='center', fontsize=20, fontweight='bold')

# 矢印
arrow = mpatches.FancyArrowPatch(
    (x_start+0.2, y), (x_end-0.2, y),
    arrowstyle='->', mutation_scale=30, linewidth=3, color='red'
)
ax1.add_patch(arrow)

# ラベル
ax1.text(x_mid, y+0.25, '演算子 → 状態', ha='center', fontsize=16, fontweight='bold')
ax1.text(x_start+0.1, y-0.35, '演算子', ha='center', fontsize=14, color='blue')
ax1.text(x_end-0.1, y-0.35, '状態', ha='center', fontsize=14, color='green')

# 数式
ax1.text(0.5, 0.15, r'$\hat{a}|0\rangle$', ha='center', fontsize=24, 
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/physics/量子力学過去問/images/operator_action_direction.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# 図2: ブラとケットの間に演算子が挟まれる場合
fig2, ax2 = plt.subplots(figsize=(12, 5))
ax2.axis('off')

# 配置
x_bra = 0.1
x_op = 0.5
x_ket = 0.9
y = 0.5

# ブラのボックス
bra_box = mpatches.FancyBboxPatch(
    (x_bra, y-0.15), 0.15, 0.3,
    boxstyle="round,pad=0.05",
    facecolor='lightcoral',
    edgecolor='black',
    linewidth=2
)
ax2.add_patch(bra_box)
ax2.text(x_bra+0.075, y, r'$\langle n|$', ha='center', va='center', fontsize=18, fontweight='bold')

# 演算子のボックス
op_box = mpatches.FancyBboxPatch(
    (x_op-0.1, y-0.15), 0.2, 0.3,
    boxstyle="round,pad=0.05",
    facecolor='lightblue',
    edgecolor='black',
    linewidth=2
)
ax2.add_patch(op_box)
ax2.text(x_op, y, r'$\hat{a}$', ha='center', va='center', fontsize=20, fontweight='bold')

# ケットのボックス
ket_box = mpatches.FancyBboxPatch(
    (x_ket-0.15, y-0.15), 0.15, 0.3,
    boxstyle="round,pad=0.05",
    facecolor='lightgreen',
    edgecolor='black',
    linewidth=2
)
ax2.add_patch(ket_box)
ax2.text(x_ket-0.075, y, r'$|m\rangle$', ha='center', va='center', fontsize=18, fontweight='bold')

# 矢印1: ブラ → 演算子
arrow1 = mpatches.FancyArrowPatch(
    (x_bra+0.15, y), (x_op-0.1, y),
    arrowstyle='->', mutation_scale=25, linewidth=2.5, color='red'
)
ax2.add_patch(arrow1)

# 矢印2: 演算子 → ケット
arrow2 = mpatches.FancyArrowPatch(
    (x_op+0.1, y), (x_ket-0.15, y),
    arrowstyle='->', mutation_scale=25, linewidth=2.5, color='red'
)
ax2.add_patch(arrow2)

# 下向きの矢印（内積を取る）
arrow3 = mpatches.FancyArrowPatch(
    (x_op, y-0.15), (x_op, y-0.4),
    arrowstyle='->', mutation_scale=25, linewidth=2.5, color='purple'
)
ax2.add_patch(arrow3)

# ラベル
ax2.text(0.5, y+0.25, 'ブラ → 演算子 → ケット', ha='center', fontsize=16, fontweight='bold')
ax2.text(x_bra+0.075, y-0.35, 'ブラ', ha='center', fontsize=14, color='red')
ax2.text(x_op, y-0.35, '演算子', ha='center', fontsize=14, color='blue')
ax2.text(x_ket-0.075, y-0.35, 'ケット', ha='center', fontsize=14, color='green')
ax2.text(x_op+0.15, y-0.3, '内積を取る', ha='left', fontsize=14, color='purple', fontweight='bold')

# 数式
ax2.text(0.5, 0.1, r'$\langle n|\hat{a}|m\rangle$', ha='center', fontsize=24,
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/physics/量子力学過去問/images/operator_sandwiched.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# 図3: 複数の演算子が連続する場合
fig3, ax3 = plt.subplots(figsize=(14, 5))
ax3.axis('off')

# 配置
x_op1 = 0.15
x_op2 = 0.4
x_ket = 0.7
y = 0.5

# 演算子1のボックス
op1_box = mpatches.FancyBboxPatch(
    (x_op1, y-0.15), 0.15, 0.3,
    boxstyle="round,pad=0.05",
    facecolor='lightblue',
    edgecolor='black',
    linewidth=2
)
ax3.add_patch(op1_box)
ax3.text(x_op1+0.075, y, r'$\hat{a}^\dagger$', ha='center', va='center', fontsize=18, fontweight='bold')

# 演算子2のボックス
op2_box = mpatches.FancyBboxPatch(
    (x_op2, y-0.15), 0.15, 0.3,
    boxstyle="round,pad=0.05",
    facecolor='lightcyan',
    edgecolor='black',
    linewidth=2
)
ax3.add_patch(op2_box)
ax3.text(x_op2+0.075, y, r'$\hat{a}$', ha='center', va='center', fontsize=18, fontweight='bold')

# ケットのボックス
ket_box = mpatches.FancyBboxPatch(
    (x_ket-0.1, y-0.15), 0.2, 0.3,
    boxstyle="round,pad=0.05",
    facecolor='lightgreen',
    edgecolor='black',
    linewidth=2
)
ax3.add_patch(ket_box)
ax3.text(x_ket, y, r'$|0\rangle$', ha='center', va='center', fontsize=18, fontweight='bold')

# 矢印1: 演算子2 → ケット（まず内側から）
arrow1 = mpatches.FancyArrowPatch(
    (x_op2+0.15, y), (x_ket-0.1, y),
    arrowstyle='->', mutation_scale=25, linewidth=2.5, color='red', linestyle='--'
)
ax3.add_patch(arrow1)
ax3.text((x_op2+0.15+x_ket-0.1)/2, y+0.15, '① まず内側から', ha='center', fontsize=12, color='red')

# 矢印2: 演算子1 → 演算子2の結果
arrow2 = mpatches.FancyArrowPatch(
    (x_op1+0.15, y), (x_op2, y),
    arrowstyle='->', mutation_scale=25, linewidth=2.5, color='blue'
)
ax3.add_patch(arrow2)
ax3.text((x_op1+0.15+x_op2)/2, y-0.3, '② 次に外側', ha='center', fontsize=12, color='blue')

# ラベル
ax3.text(0.5, y+0.35, '複数の演算子が連続する場合：右から左へ（内側から外側へ）', 
         ha='center', fontsize=16, fontweight='bold')

# 数式
ax3.text(0.5, 0.1, r'$\hat{a}^\dagger\hat{a}|0\rangle = \hat{a}^\dagger(\hat{a}|0\rangle)$', 
         ha='center', fontsize=22,
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/physics/量子力学過去問/images/multiple_operators.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("画像の生成が完了しました:")
print("1. operator_action_direction.png - 演算子の作用の方向")
print("2. operator_sandwiched.png - ブラとケットの間に演算子が挟まれる場合")
print("3. multiple_operators.png - 複数の演算子が連続する場合")
