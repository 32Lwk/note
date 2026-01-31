#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計物理学Ⅰ 演習問題の図を生成するスクリプト
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# 日本語フォント設定 (macOS: Hiragino Sans, Windows: MS Gothic, Linux: DejaVu Sans)
import platform
if platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'Hiragino Sans'
elif platform.system() == 'Windows':
    plt.rcParams['font.family'] = ['MS Gothic', 'Yu Gothic']
else:
    plt.rcParams['font.family'] = 'DejaVu Sans'

# 解像度設定
DPI = 300

# 出力ディレクトリ (スクリプトの1階層上のfigures)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'figures')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def fig_ex1_ideal_gas_3d():
    """演習1-II: 理想気体の状態方程式の3次元図 (p-V-T)"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    R, N = 8.31, 1.0  # 気体定数, モル数
    V = np.linspace(0.02, 0.1, 20)
    T = np.linspace(200, 400, 20)
    V_grid, T_grid = np.meshgrid(V, T)
    p = N * R * T_grid / V_grid
    
    # 等温線、等圧線、等積線を描く
    ax.plot_surface(V_grid * 1000, T_grid, p / 1e5, cmap='viridis', alpha=0.7)
    
    # 等温線の例 (T=300K)
    V_line = np.linspace(0.02, 0.1, 50)
    T_const = 300
    p_line = N * R * T_const / V_line
    ax.plot(V_line * 1000, np.full_like(V_line, T_const), p_line / 1e5, 'r-', lw=2, label='等温線 (T=300K)')
    
    # 等圧線の例 (p=1e5 Pa)
    p_const = 1e5
    T_line = np.linspace(250, 350, 50)
    V_line2 = N * R * T_line / p_const
    ax.plot(V_line2 * 1000, T_line, np.full_like(T_line, p_const / 1e5), 'b-', lw=2, label='等圧線 (p=1気圧)')
    
    ax.set_xlabel('$V$ (L)', fontsize=12)
    ax.set_ylabel('$T$ (K)', fontsize=12)
    ax.set_zlabel('$p$ (気圧)', fontsize=12)
    ax.set_title('理想気体の状態方程式 $pV = NRT$ の3次元表示', fontsize=14)
    ax.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex1_ideal_gas_3d.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex1_ideal_gas_3d.png")


def fig_ex2_van_der_waals():
    """演習2-I問3: ファンデルワールス方程式の無次元化グラフ"""
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    
    def vdw_dimensionless(T_tilde, V_tilde):
        """無次元化ファンデルワールス: p̃ = 8T̃/(3Ṽ-1) - 3/Ṽ^2"""
        return 8 * T_tilde / (3 * V_tilde - 1) - 3 / (V_tilde**2)
    
    V_tilde = np.linspace(0.35, 3, 200)  # Ṽ > 1/3 で有効
    
    # (a) T̃ > 1 (臨界温度以上)
    ax = axes[0]
    for T_tilde in [1.2, 1.5, 2.0]:
        p_tilde = vdw_dimensionless(T_tilde, V_tilde)
        p_tilde = np.where(np.isfinite(p_tilde) & (p_tilde > 0), p_tilde, np.nan)
        ax.plot(1/V_tilde, p_tilde, label=f'$\\tilde{{T}} = {T_tilde}$')
    ax.set_xlabel('$1/\\tilde{V}$', fontsize=12)
    ax.set_ylabel('$\\tilde{p}$', fontsize=12)
    ax.set_title('$\\tilde{T} > 1$ (臨界温度以上)', fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 3)
    
    # (b) T̃ ≈ 1 (臨界温度付近)
    ax = axes[1]
    for T_tilde in [0.95, 1.0, 1.05]:
        p_tilde = vdw_dimensionless(T_tilde, V_tilde)
        p_tilde = np.where(np.isfinite(p_tilde) & (p_tilde > 0), p_tilde, np.nan)
        ax.plot(1/V_tilde, p_tilde, label=f'$\\tilde{{T}} = {T_tilde}$')
    ax.set_xlabel('$1/\\tilde{V}$', fontsize=12)
    ax.set_ylabel('$\\tilde{p}$', fontsize=12)
    ax.set_title('$\\tilde{T} \\approx 1$ (臨界温度付近)', fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 3)
    
    # (c) T̃ < 1 (臨界温度以下)
    ax = axes[2]
    for T_tilde in [0.5, 0.7, 0.9]:
        p_tilde = vdw_dimensionless(T_tilde, V_tilde)
        p_tilde = np.where(np.isfinite(p_tilde) & (p_tilde > 0), p_tilde, np.nan)
        ax.plot(1/V_tilde, p_tilde, label=f'$\\tilde{{T}} = {T_tilde}$')
    ax.set_xlabel('$1/\\tilde{V}$', fontsize=12)
    ax.set_ylabel('$\\tilde{p}$', fontsize=12)
    ax.set_title('$\\tilde{T} < 1$ (臨界温度以下)', fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 3)
    
    plt.suptitle('ファンデルワールス状態方程式の無次元化: $\\tilde{p} = 8\\tilde{T}/(3\\tilde{V}-1) - 3/\\tilde{V}^2$', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex2_van_der_waals.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex2_van_der_waals.png")


def fig_ex2_pressure_height():
    """演習2-III: 圧力の高さ依存性 (気圧の式)"""
    z = np.linspace(0, 10000, 200)  # m
    M, g, R, T = 0.029, 9.8, 8.31, 290  # kg/mol, m/s^2, J/(mol·K), K
    p0 = 1.013e5  # 1気圧
    p = p0 * np.exp(-M * g * z / (R * T))
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(z / 1000, p / p0, 'b-', linewidth=2)
    ax.axhline(y=0.5, color='r', linestyle='--', label='$p/p_0 = 0.5$')
    ax.set_xlabel('高さ $z$ (km)', fontsize=12)
    ax.set_ylabel('$p(z)/p_0$', fontsize=12)
    ax.set_title('圧力の高さ依存性: $p(z) = p_0 \\exp(-Mgz/RT)$', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 10)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex2_pressure_height.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex2_pressure_height.png")


def fig_ex2_pressure_concept():
    """演習2-III: 微小円筒に作用する力の概念図"""
    fig, ax = plt.subplots(figsize=(6, 8))
    
    # 容器の形状
    rect = plt.Rectangle((0.3, 0.2), 0.4, 0.6, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    
    # 微小部分
    dz = 0.15
    z0 = 0.4
    inner = plt.Rectangle((0.35, z0), 0.3, dz, facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(inner)
    
    # 力の矢印
    ax.annotate('', xy=(0.5, z0 + dz + 0.05), xytext=(0.5, z0 + dz),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(0.55, z0 + dz + 0.02, '$p(z+dz)S$', fontsize=11)
    
    ax.annotate('', xy=(0.5, z0 - 0.05), xytext=(0.5, z0),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(0.55, z0 - 0.08, '$p(z)S$', fontsize=11)
    
    ax.annotate('', xy=(0.5, z0 + dz/2 - 0.02), xytext=(0.5, z0 + dz/2 + 0.02),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.text(0.15, z0 + dz/2, '$mg$', fontsize=11)
    
    ax.text(0.5, z0 - 0.2, '$S$ (断面積)', fontsize=11)
    ax.text(0.15, z0 + dz/2 + 0.1, '$z$', fontsize=11)
    ax.text(0.15, z0 + dz + 0.05, '$z+dz$', fontsize=11)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('容器内の微小円筒に作用する力', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex2_pressure_concept.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex2_pressure_concept.png")


def fig_ex3_pv_paths():
    """演習3-I: 3つの経路 (1→A→2, 1→B→2, 1→C→2)"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # 状態1と2
    V1, T1 = 1.0, 300
    V2, T2 = 2.0, 400
    R, N = 8.31, 1.0
    p1 = N * R * T1 / V1
    p2 = N * R * T2 / V2
    
    # 経路1: 定積→定圧 (1→A→2)
    V_A, T_A = V1, T2
    p_A = N * R * T_A / V_A
    ax.plot([V1, V1, V2], [T1, T2, T2], 'g-o', label='経路1 (定積→定圧)', linewidth=2)
    
    # 経路2: 等温→定積 (1→B→2)
    T_B = T1
    V_B = N * R * T_B / p2
    ax.plot([V1, V_B, V2], [T1, T1, T2], 'b-s', label='経路2 (等温→定積)', linewidth=2)
    
    # 経路3: 断熱→定積 (1→C→2)
    gamma = 5/3
    V_C = V1 * (T1 / T2) ** (1 / (gamma - 1))
    ax.plot([V1, V_C, V2], [T1, T2, T2], 'r-^', label='経路3 (断熱→定積)', linewidth=2)
    
    ax.scatter([V1, V2], [T1, T2], s=100, c='black', zorder=5)
    ax.text(V1, T1 - 20, '1', fontsize=12)
    ax.text(V2, T2 + 10, '2', fontsize=12)
    
    ax.set_xlabel('$V$', fontsize=12)
    ax.set_ylabel('$T$ (K)', fontsize=12)
    ax.set_title('理想気体の2状態を結ぶ3つの経路 (T-V図)', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.5, 2.5)
    ax.set_ylim(250, 450)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex3_pv_paths.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex3_pv_paths.png")


def fig_ex3_mayer_cycle():
    """演習3-III: Mayerサイクル"""
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    p1, V1, T1 = 2e5, 0.01, 300
    p2, V2 = 1e5, 0.02
    T2 = T1  # 自由膨張では温度不変
    T3 = T1 * V2 / V1  # 等圧過程後
    
    # 状態点
    points = [(p1/1e5, V1*1000, T1), (p2/1e5, V2*1000, T2), (p2/1e5, V1*1000, T3)]
    
    # 1→2 自由断熱膨張 (波線で表現は点線で)
    ax.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], [points[0][2], points[1][2]], 
            'b--', linewidth=2, label='自由断熱膨張')
    # 2→3 等圧過程
    ax.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], [points[1][2], points[2][2]], 
            'r-', linewidth=2, label='等圧過程')
    # 3→1 等積過程
    ax.plot([points[2][0], points[0][0]], [points[2][1], points[0][1]], [points[2][2], points[0][2]], 
            'g-', linewidth=2, label='等積過程')
    
    for i, (p, v, t) in enumerate(points):
        ax.scatter([p], [v], [t], s=80)
        ax.text(p, v, t, f'  {i+1}', fontsize=11)
    
    ax.set_xlabel('$p$ (気圧)')
    ax.set_ylabel('$V$ (L)')
    ax.set_zlabel('$T$ (K)')
    ax.set_title('Mayerサイクル')
    ax.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex3_mayer_cycle.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex3_mayer_cycle.png")


def fig_ex3_adiabatic_lapse():
    """演習3-IV: 断熱減率の概念図"""
    fig, ax = plt.subplots(figsize=(6, 8))
    
    z = np.linspace(0, 5000, 100)
    gamma = 1.41
    M, g, R = 28.9e-3, 9.8, 8.32
    Gamma = (gamma - 1) * M * g / (gamma * R)  # K/m
    T0 = 288
    T = T0 - Gamma * z
    
    ax.plot(T, z / 1000, 'b-', linewidth=2)
    ax.set_xlabel('温度 $T$ (K)', fontsize=12)
    ax.set_ylabel('高度 $z$ (km)', fontsize=12)
    ax.set_title('大気の断熱減率: $dT/dz = -\\frac{(\\gamma-1)Mg}{\\gamma R}$', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex3_adiabatic_lapse.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex3_adiabatic_lapse.png")


def fig_ex4_carnot_otto():
    """演習4-II: カルノーサイクルとオットーサイクル"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # (a) カルノーサイクル T-V
    ax = axes[0]
    TH, TL = 400, 300
    VA, VD, VB, VC = 1.0, 1.5, 2.0, 3.0
    
    ax.plot([VA, VB], [TH, TH], 'b-', linewidth=2)
    ax.plot([VB, VC], [TH, TL], 'g-', linewidth=2)
    ax.plot([VC, VD], [TL, TL], 'r-', linewidth=2)
    ax.plot([VD, VA], [TL, TH], 'm-', linewidth=2)
    ax.scatter([VA, VB, VC, VD], [TH, TH, TL, TL], s=80)
    for lab, x, y in [('A', VA, TH), ('B', VB, TH), ('C', VC, TL), ('D', VD, TL)]:
        ax.text(x, y, f'  {lab}', fontsize=11)
    ax.set_xlabel('$V$', fontsize=12)
    ax.set_ylabel('$T$', fontsize=12)
    ax.set_title('(a) カルノーサイクル', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # (b) オットーサイクル T-V
    ax = axes[1]
    V1, V2 = 2.0, 1.0  # V1 > V2
    TA, TB, TC, TD = 300, 600, 400, 200
    
    ax.plot([V1, V2], [TA, TB], 'b-', linewidth=2)  # A→B 断熱圧縮
    ax.plot([V2, V2], [TB, TC], 'g-', linewidth=2)  # B→C 定積
    ax.plot([V2, V1], [TC, TD], 'r-', linewidth=2)  # C→D 断熱膨張
    ax.plot([V1, V1], [TD, TA], 'm-', linewidth=2)  # D→A 定積
    ax.scatter([V1, V2, V2, V1], [TA, TB, TC, TD], s=80)
    for lab, x, y in [('A', V1, TA), ('B', V2, TB), ('C', V2, TC), ('D', V1, TD)]:
        ax.text(x, y, f'  {lab}', fontsize=11)
    ax.set_xlabel('$V$', fontsize=12)
    ax.set_ylabel('$T$', fontsize=12)
    ax.set_title('(b) オットーサイクル', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    plt.suptitle('熱機関のT-V線図', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex4_carnot_otto.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex4_carnot_otto.png")


def fig_ex4_adiabatic_intersection():
    """演習4-V: 2つの断熱線が交わると仮定した場合の矛盾 (概念図)"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    V = np.linspace(1, 4, 100)
    gamma = 5/3
    
    # 2つの断熱線 (T V^{γ-1} = const)
    const1, const2 = 300, 350
    T1 = const1 / V**(gamma - 1)
    T2 = const2 / V**(gamma - 1)
    
    ax.plot(V, T1, 'b-', linewidth=2, label='断熱線1')
    ax.plot(V, T2, 'r-', linewidth=2, label='断熱線2')
    
    # 交点付近を拡大して「交差」を描く（実際は交わらないが、矛盾を示すための仮定）
    V_cross = 2.5
    T_cross = 200
    ax.scatter([V_cross], [T_cross], s=100, c='green', zorder=5)
    ax.text(V_cross, T_cross - 30, '交点?\n(仮定)', fontsize=10)
    
    # 等温線
    T_iso = 250
    ax.axhline(y=T_iso, color='gray', linestyle='--', alpha=0.7, label='等温線')
    
    ax.set_xlabel('$V$', fontsize=12)
    ax.set_ylabel('$T$', fontsize=12)
    ax.set_title('2つの断熱線が交わるという仮定（矛盾を導くための図）', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1, 4)
    ax.set_ylim(100, 350)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex4_adiabatic_intersection.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex4_adiabatic_intersection.png")


def fig_ex5_entropy_paths():
    """演習5-I: 経路Aと経路Bによるエントロピー計算"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    T_star, V_star = 250, 1.0
    T, V = 350, 2.0
    gamma = 5/3
    
    # 経路A: 等温(T*)→断熱 (T*,V*)→(T*,V')→(T,V), V'は断熱線上
    V_prime = V * (T / T_star) ** (1 / (gamma - 1))
    ax.plot([V_star, V_prime, V], [T_star, T_star, T], 'r-o', linewidth=2, label='経路A')
    
    # 経路B: 断熱→等温 (T*,V*)→(T',V)→(T,V), T'=T*(V*/V)^{γ-1}
    T_prime_B = T_star * (V_star / V) ** (gamma - 1)
    ax.plot([V_star, V, V], [T_star, T_prime_B, T], 'g-s', linewidth=2, label='経路B')
    
    ax.scatter([V_star, V], [T_star, T], s=100, c='black')
    ax.text(V_star, T_star - 15, '$(T^*, V^*)$', fontsize=10)
    ax.text(V, T + 10, '$(T, V)$', fontsize=10)
    
    ax.set_xlabel('$V$', fontsize=12)
    ax.set_ylabel('$T$', fontsize=12)
    ax.set_title('エントロピー計算の2つの経路 (T-V図)', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex5_entropy_paths.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex5_entropy_paths.png")


def fig_ex6_binomial_poisson():
    """演習6-V: 二項分布とポアソン分布"""
    from scipy.special import comb
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    N, p = 50, 0.2
    n_vals = np.arange(0, N + 1)
    P_binom = np.array([comb(N, n) * p**n * (1-p)**(N-n) for n in n_vals])
    
    ax = axes[0]
    ax.bar(n_vals, P_binom, color='steelblue', alpha=0.7)
    ax.set_xlabel('$n$', fontsize=12)
    ax.set_ylabel('$P(n)$', fontsize=12)
    ax.set_title(f'二項分布 ($N={N}$, $p={p}$)', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # ポアソン分布
    a = N * p  # 平均
    n_vals2 = np.arange(0, 25)
    import math
    P_poisson = np.exp(-a) * np.power(a, n_vals2) / np.array([math.factorial(int(n)) for n in n_vals2])
    
    ax = axes[1]
    ax.bar(n_vals2, P_poisson, color='coral', alpha=0.7)
    ax.plot(n_vals, P_binom, 'b.-', markersize=4, label='二項分布')
    ax.set_xlabel('$n$', fontsize=12)
    ax.set_ylabel('$P(n)$', fontsize=12)
    ax.set_title(f'ポアソン分布 ($a = \\langle n \\rangle = {a}$)', fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.suptitle('二項分布とポアソン分布', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex6_binomial_poisson.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex6_binomial_poisson.png")


def fig_ex7_gamma_integrand():
    """演習7-I問2: Γ(x+1)の被積分関数 t^x e^{-t} の概形"""
    t = np.linspace(0.01, 10, 500)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    for x in [1, 2, 5, 10]:
        f = t**x * np.exp(-t)
        ax.plot(t, f, label=f'$x = {x}$', linewidth=2)
    
    ax.set_xlabel('$t$', fontsize=12)
    ax.set_ylabel('$t^x e^{-t}$', fontsize=12)
    ax.set_title('$\\Gamma(x+1)$の被積分関数 $t^x e^{-t}$ の概形', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 10)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex7_gamma_integrand.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex7_gamma_integrand.png")


def fig_ex7_stirling_error():
    """演習7-I問4: スターリング近似の相対誤差"""
    from scipy.special import factorial
    
    N_vals = np.arange(2, 21, dtype=int)
    exact = np.array([float(factorial(n)) for n in N_vals])
    approx = np.sqrt(2 * np.pi * N_vals) * (N_vals ** N_vals) * np.exp(-N_vals)
    rel_error = np.abs(exact - approx) / exact
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.semilogy(N_vals, rel_error, 'bo-', linewidth=2, markersize=6)
    ax.set_xlabel('$N$', fontsize=12)
    ax.set_ylabel('相対誤差', fontsize=12)
    ax.set_title('スターリング近似 $N! \\approx \\sqrt{2\\pi N} N^N e^{-N}$ の相対誤差', fontsize=14)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex7_stirling_error.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex7_stirling_error.png")


def fig_ex7_W_exp_betaE():
    """演習7-IV問6: W_N(E) exp(-βE) のピーク"""
    c = 1.5  # 3/2 for monatomic
    N = 20   # 小さめにしてオーバーフローを防ぐ
    kB_T = 1.0
    beta = 1 / kB_T
    E_star = c * N * kB_T  # ピーク位置
    
    E = np.linspace(E_star * 0.5, E_star * 1.5, 500)
    # W_N(E) ∝ E^{cN-1} for ideal gas, 対数で計算してオーバーフロー回避
    log_W = (c * N - 1) * np.log(E)
    log_integrand = log_W - beta * E
    log_integrand = log_integrand - np.max(log_integrand)
    integrand = np.exp(log_integrand)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(E, integrand, 'b-', linewidth=2)
    ax.axvline(x=E_star, color='r', linestyle='--', label=f'$E^* = cN k_B T = {E_star:.0f}$')
    ax.set_xlabel('$E$', fontsize=12)
    ax.set_ylabel('$W_N(E) e^{-\\beta E}$ (規格化)', fontsize=12)
    ax.set_title('被積分関数 $W_N(E) e^{-\\beta E}$ の鋭いピーク', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex7_W_exp_betaE.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex7_W_exp_betaE.png")


def fig_ex1_heat_capacity():
    """演習1-I: 定積比熱の概念図（熱量と温度変化の関係）"""
    fig, ax = plt.subplots(figsize=(8, 5))
    T = np.linspace(0, 30, 100)
    Q = 0.7 * 100 * T  # m=100g, Cv=0.7 の例
    ax.fill_between(T, 0, Q, alpha=0.3)
    ax.plot(T, Q, 'b-', linewidth=2)
    ax.axhline(y=140, color='r', linestyle='--', alpha=0.7)
    ax.axvline(x=20, color='r', linestyle='--', alpha=0.7)
    ax.set_xlabel('温度変化 $\\Delta T$ (K)', fontsize=12)
    ax.set_ylabel('必要な熱量 $Q$ (J)', fontsize=12)
    ax.set_title('定積条件: $Q = m C_v \\Delta T$（比例関係）', fontsize=14)
    ax.annotate('$Q = m C_v \\Delta T$\n(直線の傾き=$m C_v$)', xy=(15, 105), fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 250)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex1_heat_capacity.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex1_heat_capacity.png")


def fig_ex4_max_work():
    """演習4-I: 最大仕事の原理（p-V図上の面積比較）"""
    fig, ax = plt.subplots(figsize=(8, 6))
    V = np.linspace(1, 3, 100)
    p_iso = 1 / V  # 等温線 p ∝ 1/V（規格化）
    ax.fill_between(V, 0, p_iso, alpha=0.3, color='blue')
    ax.plot(V, p_iso, 'b-', linewidth=2, label='準静的等温（面積=仕事）')
    ax.axvline(x=1, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(x=3, color='gray', linestyle='--', alpha=0.5)
    ax.annotate('自由膨張\n$W=0$\n(面積なし)', xy=(1.5, 0.2), fontsize=10)
    ax.set_xlabel('$V$', fontsize=12)
    ax.set_ylabel('$p$', fontsize=12)
    ax.set_title('最大仕事の原理: 準静的等温の面積が最大の仕事', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.5, 3.5)
    ax.set_ylim(0, 1.2)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex4_max_work.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex4_max_work.png")


def fig_ex4_mini_carnot():
    """演習4-III: 微小カルノーサイクルの概念図"""
    fig, ax = plt.subplots(figsize=(8, 6))
    V = np.linspace(1, 4, 100)
    T1, T2 = 300, 310
    p1 = T1 / V
    p2 = T2 / V
    ax.plot(V, p1, 'b-', linewidth=2, label=f'等温線 $T$')
    ax.plot(V, p2, 'r-', linewidth=2, label=f'等温線 $T+dT$')
    # 微小サイクルを四角形で示す
    V_range = [1.5, 2.5]
    ax.fill_between([V_range[0], V_range[1], V_range[1], V_range[0]],
                    [T1/V_range[0], T1/V_range[1], T2/V_range[1], T2/V_range[0]],
                    alpha=0.3, color='green')
    ax.set_xlabel('$V$', fontsize=12)
    ax.set_ylabel('$p$', fontsize=12)
    ax.set_title('微小カルノーサイクル: 等温線$T$と$T+dT$、2本の断熱線で囲まれる', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex4_mini_carnot.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex4_mini_carnot.png")


def fig_ex5_free_expansion():
    """演習5-I問4,5: 断熱自由膨張の概念図"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    # 左: 膨張前
    ax = axes[0]
    rect1 = plt.Rectangle((0.2, 0.3), 0.3, 0.4, facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(rect1)
    ax.text(0.35, 0.5, '気体\n$(T,V)$', ha='center', fontsize=11)
    ax.text(0.35, 0.15, '真空', ha='center', fontsize=10, color='gray')
    ax.axvline(x=0.5, color='black', linewidth=2, linestyle='-')
    ax.text(0.5, 0.9, '壁（仕切り）', ha='center', fontsize=10)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('膨張前: 体積$V$、温度$T$', fontsize=12)
    # 右: 膨張後
    ax = axes[1]
    rect2 = plt.Rectangle((0.1, 0.2), 0.8, 0.6, facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(rect2)
    ax.text(0.5, 0.5, '気体\n$(T, V_{\\mathrm{f}})$\n$Q=0, W=0$\n$\\Delta U=0$→$T$不変', ha='center', fontsize=10)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('膨張後: 体積$V_{\\mathrm{f}}$、温度$T$（理想気体では不変）', fontsize=12)
    plt.suptitle('断熱自由膨張: 壁を瞬間的に取り除く', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex5_free_expansion.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex5_free_expansion.png")


def fig_ex6_mixing():
    """演習6-IV: 2成分混合の概念図"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    # 左: 混合前
    ax = axes[0]
    rect1 = plt.Rectangle((0.1, 0.2), 0.35, 0.6, facecolor='lightblue', edgecolor='blue', linewidth=2)
    rect2 = plt.Rectangle((0.55, 0.2), 0.35, 0.6, facecolor='lightcoral', edgecolor='red', linewidth=2)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.axvline(x=0.5, color='black', linewidth=2)
    ax.text(0.275, 0.5, '成分1\n$V_1$, $N_1$', ha='center', fontsize=11)
    ax.text(0.725, 0.5, '成分2\n$V_2$, $N_2$', ha='center', fontsize=11)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('混合前: 仕切りで分離', fontsize=12)
    # 右: 混合後
    ax = axes[1]
    rect3 = plt.Rectangle((0.1, 0.2), 0.8, 0.6, facecolor='lavender', edgecolor='purple', linewidth=2)
    ax.add_patch(rect3)
    ax.text(0.5, 0.5, '混合気体\n各成分が体積$V$に広がる\n$\\Delta S > 0$', ha='center', fontsize=11)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('混合後: 仕切りを外す', fontsize=12)
    plt.suptitle('2成分気体の混合（不可逆過程）', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex6_mixing.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex6_mixing.png")


def fig_ex1_gaussian():
    """演習1-IV: ガウス分布の概形"""
    x = np.linspace(-5, 5, 300)
    mu, sigma = 0, 1
    P = (1 / np.sqrt(2 * np.pi * sigma**2)) * np.exp(-(x - mu)**2 / (2 * sigma**2))
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, P, 'b-', linewidth=2)
    ax.axvline(x=mu, color='r', linestyle='--', alpha=0.7, label=f'$\\mu = {mu}$')
    ax.fill_between(x, P, alpha=0.3)
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$P(x)$', fontsize=12)
    ax.set_title('ガウス分布 $P(x) = \\frac{1}{\\sqrt{2\\pi\\sigma^2}} e^{-(x-\\mu)^2/(2\\sigma^2)}$', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex1_gaussian.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex1_gaussian.png")


def main():
    """すべての図を生成"""
    print("統計物理学 演習問題の図を生成します...")
    fig_ex1_ideal_gas_3d()
    fig_ex1_heat_capacity()
    fig_ex1_gaussian()
    fig_ex2_van_der_waals()
    fig_ex2_pressure_height()
    fig_ex2_pressure_concept()
    fig_ex3_pv_paths()
    fig_ex3_mayer_cycle()
    fig_ex3_adiabatic_lapse()
    fig_ex4_carnot_otto()
    fig_ex4_max_work()
    fig_ex4_mini_carnot()
    fig_ex4_adiabatic_intersection()
    fig_ex5_entropy_paths()
    fig_ex5_free_expansion()
    fig_ex6_binomial_poisson()
    fig_ex6_mixing()
    fig_ex7_gamma_integrand()
    fig_ex7_stirling_error()
    fig_ex7_W_exp_betaE()
    print("すべての図の生成が完了しました。")


if __name__ == '__main__':
    main()
