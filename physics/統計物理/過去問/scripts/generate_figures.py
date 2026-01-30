#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計物理1 過去問 解答・解説用の図を生成するスクリプト
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import os
import platform

# 日本語フォント設定 (macOS: Hiragino Sans, Windows: MS Gothic, Linux: DejaVu Sans)
if platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'Hiragino Sans'
elif platform.system() == 'Windows':
    plt.rcParams['font.family'] = ['MS Gothic', 'Yu Gothic']
else:
    plt.rcParams['font.family'] = 'DejaVu Sans'

DPI = 300
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(BASE_DIR, 'figures')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def fig_past2023_ex1_setup():
    """2023再 問題I: 左右に仕切られた容器の概念図"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # 外枠（容器）
    rect = FancyBboxPatch((0.5, 1), 9, 4, boxstyle="round,pad=0.02",
                          edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(rect)

    # 仕切り壁（中央）
    ax.axvline(x=5, ymin=0.2, ymax=0.8, color='black', linewidth=2)
    ax.text(5.2, 4.2, '仕切り壁', fontsize=11)
    ax.text(5.2, 0.8, '断熱壁', fontsize=10, color='gray')

    # 左室
    ax.text(2.5, 4.5, r'$T_A$, $V_A$', fontsize=14)
    ax.text(2.5, 3.5, '1 モル', fontsize=12)
    ax.text(2.5, 0.5, '断熱壁', fontsize=10, color='gray')

    # 右室
    ax.text(7.5, 4.5, r'$T_B$, $V_B$', fontsize=14)
    ax.text(7.5, 3.5, '2 モル', fontsize=12)

    ax.set_title('2023再 問題I: 理想気体の混合（初期状態）', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2023_ex1_setup.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2023_ex1_setup.png")


def fig_past2023_ex1_energy_flow():
    """2023再 問題I: 透熱壁を通した熱の流れと内部エネルギー保存"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    rect = FancyBboxPatch((0.5, 1), 9, 4, boxstyle="round,pad=0.02",
                          edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(rect)
    ax.axvline(x=5, ymin=0.2, ymax=0.8, color='black', linewidth=2)
    ax.text(5.1, 4.2, '透熱壁', fontsize=11)
    ax.text(2.5, 4.2, r'$T_A$ (高温)', fontsize=11, color='red')
    ax.text(2.5, 3.2, r'熱 $Q \to$', fontsize=11, ha='center')
    ax.text(7.5, 4.2, r'$T_B$ (低温)', fontsize=11, color='blue')
    ax.text(7.5, 3.2, '← 熱 $Q$', fontsize=11, ha='center')
    ax.annotate('', xy=(4.5, 3.5), xytext=(5.5, 3.5),
                arrowprops=dict(arrowstyle='->', color='orange', lw=2))
    ax.text(5, 3.0, '熱の流れ', fontsize=10, ha='center', color='orange')
    ax.text(5, 0.5, r'$U_{\mathrm{total}}=\mathrm{const}$', fontsize=11, ha='center')
    ax.set_title('問1: 透熱壁を通して熱が流れ、両室の温度が $T$ で一致', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2023_ex1_energy_flow.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2023_ex1_energy_flow.png")


def fig_past2023_ex1_Tmin():
    """2023再 問題I 問4: 算術平均と幾何平均の関係"""
    T_A, T_B = 400, 200  # 例
    T_arith = (T_A + 2*T_B) / 3  # 問1の温度
    T_geom = (T_A**(1/3)) * (T_B**(2/3))  # T_min

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh([0], [T_geom], height=0.3, color='blue', alpha=0.7, label=r'$T_{\mathrm{min}}$ (幾何平均)')
    ax.barh([0.5], [T_arith], height=0.3, color='green', alpha=0.7, label=r'問1の $T$ (算術平均)')
    ax.axvline(T_B, color='gray', linestyle='--', alpha=0.7, label=r'$T_B$')
    ax.axvline(T_A, color='gray', linestyle=':', alpha=0.7, label=r'$T_A$')
    ax.set_yticks([0, 0.5])
    ax.set_yticklabels([r'$T_{\mathrm{min}}$', r'問1の $T$'])
    ax.set_xlabel(r'温度 $T$ (K)', fontsize=12)
    ax.set_title('問4: 終状態の温度の取り得る範囲（$T_{\mathrm{min}} <$ 問1の $T$）', fontsize=12)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3, axis='x')
    ax.set_xlim(T_B - 20, T_A + 20)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2023_ex1_Tmin.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2023_ex1_Tmin.png")


def fig_past2023_ex2_E_p():
    """2023再 問題II: 変な気体の E(T) と p(T)"""
    T = np.linspace(0.5, 3, 100)
    sigma, V = 1.0, 1.0
    E = (3/4) * sigma * T**4 * V
    p = (1/4) * sigma * T**4

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(T, E, 'b-', linewidth=2)
    ax1.set_xlabel(r'$T$', fontsize=12)
    ax1.set_ylabel(r'$E(T,V)$', fontsize=12)
    ax1.set_title(r'内部エネルギー $E = \frac{3}{4}\sigma T^4 V$', fontsize=12)
    ax1.grid(True, alpha=0.3)

    ax2.plot(T, p, 'r-', linewidth=2)
    ax2.set_xlabel(r'$T$', fontsize=12)
    ax2.set_ylabel(r'$p(T)$', fontsize=12)
    ax2.set_title(r'圧力 $p = \frac{1}{4}\sigma T^4$（$V$ に依存しない）', fontsize=12)
    ax2.grid(True, alpha=0.3)

    plt.suptitle('問題II: 変な気体 $S(T,V) = \sigma T^3 V$', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2023_ex2_E_p.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2023_ex2_E_p.png")


def fig_past2023_ex3_W_P():
    """2023再 問題III: P(E) ∝ W_N(M) exp(-βE) のピーク"""
    from math import factorial
    N, beta_hw = 20, 0.5  # 例
    M_vals = np.arange(0, 80)
    W = np.array([factorial(M + N - 1) / (factorial(N-1) * factorial(M)) if M + N - 1 >= 0 else 0 for M in M_vals])
    W = np.where(np.isfinite(W), W, 0)
    E_vals = M_vals  # E/(ℏω) = M
    P = W * np.exp(-beta_hw * E_vals)
    P = P / P.max()

    M_star = N / (np.exp(beta_hw) - 1)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(E_vals, P, 'b-', linewidth=2, label=r'$P(E) \propto W_N(M) e^{-\beta E}$')
    ax.axvline(M_star, color='red', linestyle='--', linewidth=2, label=r'$E^*/(\hbar\omega) = N/(e^{\beta\hbar\omega}-1)$')
    ax.set_xlabel(r'$E/(\hbar\omega) = M$', fontsize=12)
    ax.set_ylabel('規格化した $P(E)$', fontsize=12)
    ax.set_title('問題III: エネルギー分布のピーク（$N=20$, $\\beta\\hbar\\omega=0.5$）', fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2023_ex3_W_P.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2023_ex3_W_P.png")


def fig_past2023_oscillator_Z():
    """2023再 問題III: 調和振動子の分配関数と平均エネルギー（概念）"""
    beta_hw = np.linspace(0.2, 3, 100)
    Z1 = 1 / (1 - np.exp(-beta_hw))
    E_avg = 1 / (np.exp(beta_hw) - 1)  # ⟨E⟩/(ℏω)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(beta_hw, Z1, 'b-', linewidth=2)
    ax1.set_xlabel(r'$\beta \hbar \omega$', fontsize=12)
    ax1.set_ylabel(r'$Z_1$', fontsize=12)
    ax1.set_title(r'1個の調和振動子の分配関数 $Z_1 = \frac{1}{1-e^{-\beta\hbar\omega}}$', fontsize=12)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 3)

    ax2.plot(beta_hw, E_avg, 'r-', linewidth=2)
    ax2.set_xlabel(r'$\beta \hbar \omega$', fontsize=12)
    ax2.set_ylabel(r'$\langle E \rangle / (\hbar\omega)$', fontsize=12)
    ax2.set_title(r'平均エネルギー $\langle E \rangle = \frac{\hbar\omega}{e^{\beta\hbar\omega}-1}$', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 3)

    plt.suptitle('N個の独立な調和振動子（問題III）', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2023_oscillator_Z.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2023_oscillator_Z.png")


def fig_past2024_ex1_path():
    """2024 問題I: 断熱自由膨張と準静的断熱過程の経路"""
    fig, ax = plt.subplots(figsize=(8, 6))
    V_vals = np.array([1.0, 2.0, 1.0])  # V, V', V
    T_vals = np.array([300, 300, 300 * (2.0)**(1/2)])  # T, T'=T, T'' (c=2の例)
    ax.plot(V_vals, T_vals, 'bo-', linewidth=2, markersize=10)
    ax.annotate(r'$(T,V)$', xy=(1, 300), xytext=(0.85, 280), fontsize=12)
    ax.annotate(r'$(T\',V\')$', xy=(2, 300), xytext=(1.9, 280), fontsize=12)
    ax.annotate(r'$(T\'\',V)$', xy=(1, T_vals[2]), xytext=(0.7, T_vals[2]+15), fontsize=12)
    ax.annotate('断熱自由膨張', xy=(1.5, 300), fontsize=11, ha='center')
    ax.annotate('準静的断熱', xy=(1.5, 320), fontsize=11, ha='center')
    ax.set_xlabel(r'体積 $V$', fontsize=12)
    ax.set_ylabel(r'温度 $T$ (K)', fontsize=12)
    ax.set_title('2024 問題I: $(T,V) \\to (T\',V\') \\to (T\'\',V)$ の経路', fontsize=14)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2024_ex1_path.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2024_ex1_path.png")


def fig_past2024_ex1_why_entropy():
    """2024 問題I: 断熱自由膨張でエントロピーが増大する理由"""
    fig, ax = plt.subplots(figsize=(8, 5))
    V_vals = [1, 2]
    S_vals = [0, np.log(2)]  # ΔS = NR ln(V'/V) のイメージ
    ax.plot(V_vals, S_vals, 'bo-', linewidth=2, markersize=12)
    ax.annotate(r'$(T,V)$', xy=(1, 0), xytext=(0.85, -0.15), fontsize=12)
    ax.annotate(r'$(T,V\')$', xy=(2, np.log(2)), xytext=(1.9, np.log(2)+0.1), fontsize=12)
    ax.fill_between([1, 2], [0, np.log(2)], alpha=0.2)
    ax.set_xlabel(r'体積 $V$', fontsize=12)
    ax.set_ylabel(r'エントロピー $S$（任意単位）', fontsize=12)
    ax.set_title('断熱自由膨張: $V \\to V\'$ で気体が広がり $\\Delta S = NR\\ln(V\'/V) > 0$', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2024_ex1_why_entropy.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2024_ex1_why_entropy.png")


def fig_past2024_ex2_entropy_same_diff():
    """2024 問題II: 同一種ΔS=0 vs 異種ΔS>0 の概念"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 5)
    ax1.axis('off')
    rect1 = FancyBboxPatch((0.5, 1), 4, 3, boxstyle="round,pad=0.02", edgecolor='black', facecolor='lightblue', alpha=0.3)
    ax1.add_patch(rect1)
    ax1.text(2.5, 2.5, '同一種\n壁取り外し\n$\\Delta S = 0$', fontsize=12, ha='center')
    ax1.set_title('同一種: 可逆、$\\Delta S = 0$', fontsize=12)

    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 5)
    ax2.axis('off')
    rect2 = FancyBboxPatch((0.5, 1), 4, 3, boxstyle="round,pad=0.02", edgecolor='black', facecolor='lightgreen', alpha=0.3)
    ax2.add_patch(rect2)
    ax2.text(2.5, 2.5, '異種混合\n壁取り外し\n$\\Delta S > 0$', fontsize=12, ha='center')
    ax2.set_title('異種: 不可逆、$\\Delta S > 0$', fontsize=12)

    plt.suptitle('問題II: 同一種と異種でエントロピー変化が異なる', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2024_ex2_entropy_same_diff.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2024_ex2_entropy_same_diff.png")


def fig_past2024_ex2_setup():
    """2024 問題II: 透熱壁で仕切られた容器"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    rect = FancyBboxPatch((0.5, 1), 9, 4, boxstyle="round,pad=0.02",
                          edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(rect)
    ax.axvline(x=5, ymin=0.2, ymax=0.8, color='black', linewidth=2)
    ax.text(5.15, 4.2, '透熱壁', fontsize=11)
    ax.text(2.5, 4.3, r'$N_A$ モル', fontsize=12)
    ax.text(2.5, 3.3, r'温度 $T$', fontsize=11)
    ax.text(7.5, 4.3, r'$N_B$ モル', fontsize=12)
    ax.text(7.5, 3.3, r'温度 $T$', fontsize=11)
    ax.set_title('2024 問題II: 左右に仕切られた容器（透熱壁）', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2024_ex2_setup.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2024_ex2_setup.png")


def fig_past2025_ex1_entropy():
    """2025 問題I: 架空の気体の S(U,V) と経路の概念"""
    U = np.linspace(0.5, 3, 50)
    V = np.linspace(0.5, 2, 50)
    U_grid, V_grid = np.meshgrid(U, V)
    # S ∝ ln(U^{3/2} V^2) の等高線の代わりに、簡易的に T = 2U/(3NR) の等高線
    T_contour = U_grid / V_grid  # 簡易的な関係

    fig, ax = plt.subplots(figsize=(8, 6))
    cs = ax.contour(U_grid, V_grid, T_contour, levels=8, colors='gray', alpha=0.6)
    ax.clabel(cs, inline=True, fontsize=9)
    ax.plot([1, 1, 1.5], [1, 2, 1], 'b-o', linewidth=2, markersize=8,
            label=r'$(T,V)\to(T\',V\')\to(T\'\',V)$')
    ax.set_xlabel(r'$U/N$ (任意単位)', fontsize=12)
    ax.set_ylabel(r'$V/N$ (任意単位)', fontsize=12)
    ax.set_title('2025 問題I: 架空の気体の状態変化の概念図', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2025_ex1_entropy.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2025_ex1_entropy.png")


def fig_past2025_ex1_why_T():
    """2025 問題I: 1/T = ∂S/∂U の意味"""
    U = np.linspace(0.5, 3, 50)
    S = np.log(U**1.5)  # S ∝ ln(U^{3/2}) のイメージ
    dSdU = 1.5 / U
    T = 1 / dSdU  # T = 1/(∂S/∂U)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(U, S, 'b-', linewidth=2)
    ax1.set_xlabel(r'$U$', fontsize=12)
    ax1.set_ylabel(r'$S(U,V)$', fontsize=12)
    ax1.set_title(r'$S \propto \ln(U^{3/2})$ のとき傾き $dS/dU = 1/T$', fontsize=12)
    ax1.grid(True, alpha=0.3)

    ax2.plot(U, T, 'r-', linewidth=2)
    ax2.set_xlabel(r'$U$', fontsize=12)
    ax2.set_ylabel(r'$T$', fontsize=12)
    ax2.set_title(r'$T = 2U/(3NR)$（$1/T = \partial S/\partial U$）', fontsize=12)
    ax2.grid(True, alpha=0.3)

    plt.suptitle('問題I: 温度は $1/T = (\\partial S/\\partial U)_V$ で定義される', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2025_ex1_why_T.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2025_ex1_why_T.png")


def fig_past2025_ex2_energy_balance():
    """2025 問題II: 透熱壁を通した熱の流れとエネルギー収支"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    rect = FancyBboxPatch((0.5, 1), 9, 4, boxstyle="round,pad=0.02",
                          edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(rect)
    ax.axvline(x=5, ymin=0.2, ymax=0.8, color='black', linewidth=2)
    ax.text(5.1, 4.2, '透熱壁', fontsize=11)
    ax.text(2.5, 4.5, r'気体A: $T_L$', fontsize=11, color='red')
    ax.text(2.5, 3.5, r'$U_A = 3RT_L$', fontsize=10)
    ax.text(7.5, 4.5, r'気体B: $T_R$', fontsize=11, color='blue')
    ax.text(7.5, 3.5, r'$U_B = 3RT_R$', fontsize=10)
    ax.annotate('', xy=(4.5, 2.5), xytext=(5.5, 2.5),
                arrowprops=dict(arrowstyle='->', color='orange', lw=2))
    ax.text(5, 2.0, '熱の流れ', fontsize=10, ha='center', color='orange')
    ax.text(5, 0.6, r'終状態: $T = (T_L+T_R)/2$, $U_{\mathrm{total}} = \mathrm{const}$', fontsize=10, ha='center')
    ax.set_title('問題II: 透熱壁に替えると熱が流れ、両室の温度が $T$ で一致', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2025_ex2_energy_balance.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/past2025_ex2_energy_balance.png")


def fig_past2025_ex2_setup():
    """2025 問題II: 2種類の気体、断熱壁で仕切られた容器"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    rect = FancyBboxPatch((0.5, 1), 9, 4, boxstyle="round,pad=0.02",
                          edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(rect)
    ax.axvline(x=5, ymin=0.2, ymax=0.8, color='black', linewidth=2)
    ax.text(5.1, 4.2, '仕切り壁', fontsize=11)
    ax.text(5.1, 0.8, '断熱壁', fontsize=10, color='gray')
    ax.text(2.5, 4.5, r'$T_L$, $V_L$', fontsize=12)
    ax.text(2.5, 3.5, '気体A 1モル', fontsize=11)
    ax.text(7.5, 4.5, r'$T_R$, $V_R$', fontsize=12)
    ax.text(7.5, 3.5, '気体B 2モル', fontsize=11)
    ax.text(2.5, 0.5, '断熱壁', fontsize=10, color='gray')
    ax.set_title('2025 問題II: 2種類の理想気体（断熱壁で仕切り）', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'past2025_ex2_setup.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print("生成: " + os.path.join(OUTPUT_DIR, 'past2025_ex2_setup.png'))


def main():
    """すべての図を生成"""
    print("統計物理1 過去問の図を生成します...")
    fig_past2023_ex1_setup()
    fig_past2023_ex1_energy_flow()
    fig_past2023_ex1_Tmin()
    fig_past2023_ex2_E_p()
    fig_past2023_ex3_W_P()
    fig_past2023_oscillator_Z()
    fig_past2024_ex1_path()
    fig_past2024_ex1_why_entropy()
    fig_past2024_ex2_entropy_same_diff()
    fig_past2024_ex2_setup()
    fig_past2025_ex1_entropy()
    fig_past2025_ex1_why_T()
    fig_past2025_ex2_energy_balance()
    fig_past2025_ex2_setup()
    print("すべての図の生成が完了しました。")


if __name__ == '__main__':
    main()
