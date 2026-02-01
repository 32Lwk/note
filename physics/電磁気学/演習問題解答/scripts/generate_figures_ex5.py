#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
電磁気学演習問題5 (2025年11月28日) の図を生成するスクリプト
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# 日本語フォント設定
plt.rcParams['font.family'] = 'Hiragino Sans'

# 解像度設定
DPI = 300

# 出力ディレクトリ
OUTPUT_DIR = 'figures'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fig_ex5_1_dielectric_half_space():
    """問題1: 半無限空間の誘電体と点電荷"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 配置
    d = 1.0
    
    # 境界面
    ax1.axhline(y=0, color='k', linewidth=2, linestyle='-', label='境界面 $z=0$')
    
    # 点電荷
    ax1.scatter([0], [d], s=300, c='r', marker='+', linewidths=3, label='点電荷 $q$')
    
    # 領域の表示
    ax1.fill_between([-2, 2], [0, 0], [2, 2], alpha=0.1, color='blue', label='真空')
    ax1.fill_between([-2, 2], [0, 0], [-2, -2], alpha=0.1, color='green', label='誘電体')
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$z$', fontsize=12)
    ax1.set_title('半無限空間の誘電体と点電荷', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_aspect('equal')
    
    # 右図: 分極電荷面密度の分布
    r = np.linspace(0, 3, 100)
    q = 1.0
    d = 1.0
    epsilon = 2.0
    epsilon_0 = 1.0
    sigma = -(epsilon - epsilon_0) * q * d / (2 * np.pi * (epsilon + epsilon_0) * (r**2 + d**2)**(3/2))
    
    ax2.plot(r, sigma, 'r-', linewidth=2)
    ax2.set_xlabel('$r = \\sqrt{x^2 + y^2}$', fontsize=12)
    ax2.set_ylabel('$\\sigma\'(r)$', fontsize=12)
    ax2.set_title('誘電体表面の分極電荷面密度', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex5_1_dielectric_half_space.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex5_1_dielectric_half_space.png")

def fig_ex5_2_capacitor():
    """問題2: 平行板コンデンサー"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: コンデンサーの構造
    d = 1.0
    L = 2.0
    x_dielectric = 1.0
    
    # 極板
    ax1.plot([-L, L], [d/2, d/2], 'k-', linewidth=3, label='極板')
    ax1.plot([-L, L], [-d/2, -d/2], 'k-', linewidth=3)
    
    # 誘電体
    ax1.fill_between([-L, x_dielectric], [-d/2, -d/2], [d/2, d/2], alpha=0.3, color='blue', label='誘電体')
    ax1.fill_between([x_dielectric, L], [-d/2, -d/2], [d/2, d/2], alpha=0.1, color='gray', label='真空')
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$z$', fontsize=12)
    ax1.set_title('誘電体が部分的に挿入されたコンデンサー', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-L, L)
    ax1.set_ylim(-1, 1)
    
    # 右図: エネルギーと力
    x = np.linspace(0, L, 100)
    Q = 1.0
    d = 1.0
    A = L * 1.0
    epsilon_0 = 1.0
    epsilon = 2.0
    A_prime = x * 1.0
    
    U = Q**2 * d / (2 * (epsilon_0 * A + (epsilon - epsilon_0) * A_prime))
    F = Q**2 * d * (epsilon - epsilon_0) * 1.0 / (2 * (epsilon_0 * A + (epsilon - epsilon_0) * A_prime)**2)
    
    ax2_twin = ax2.twinx()
    ax2.plot(x, U, 'b-', linewidth=2, label='エネルギー $U$')
    ax2_twin.plot(x, F, 'r--', linewidth=2, label='力 $F$')
    ax2.set_xlabel('誘電体の挿入長さ $x$', fontsize=12)
    ax2.set_ylabel('エネルギー $U$', fontsize=12, color='b')
    ax2_twin.set_ylabel('力 $F$', fontsize=12, color='r')
    ax2.set_title('エネルギーと力の関係', fontsize=14)
    ax2.tick_params(axis='y', labelcolor='b')
    ax2_twin.tick_params(axis='y', labelcolor='r')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex5_2_capacitor.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex5_2_capacitor.png")

def fig_ex5_3_energy():
    """問題3: 誘電体の電気エネルギー"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # エネルギー密度の概念図
    r = np.linspace(0.1, 3, 100)
    E = 1 / r**2
    D = 2 * E  # epsilon = 2*epsilon_0と仮定
    W = 0.5 * E * D
    
    ax.plot(r, W, 'b-', linewidth=2, label='エネルギー密度 $W$')
    ax.set_xlabel('$r$', fontsize=12)
    ax.set_ylabel('$W$', fontsize=12)
    ax.set_title('誘電体中の電気エネルギー密度', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex5_3_energy.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex5_3_energy.png")

def fig_ex5_5_magnetic_dipole():
    """問題5: 電流ループと磁気双極子
    右ねじの法則: xy平面で反時計回りの電流 → 磁気双極子モーメントは +z 方向
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 円形電流ループ（反時計回り: φ 増加で (1,0,0)→(0,1,0)→(-1,0,0)→(0,-1,0)）
    # 右ねじの法則で m は +z を向く
    phi = np.linspace(0, 2*np.pi, 100)
    a = 1.0
    x_circle = a * np.cos(phi)
    y_circle = a * np.sin(phi)
    z_circle = np.zeros_like(phi)
    ax.plot(x_circle, y_circle, z_circle, 'b-', linewidth=3, label='電流ループ')
    
    # 磁気双極子モーメント（右ねじの法則: 反時計回り電流 → m は +z）
    ax.quiver(0, 0, 0, 0, 0, 1, color='r', arrow_length_ratio=0.3, linewidth=3, label='$\\boldsymbol{m}$')
    
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$y$', fontsize=12)
    ax.set_zlabel('$z$', fontsize=12)
    ax.set_title('電流ループと磁気双極子モーメント', fontsize=14)
    ax.legend(fontsize=10)
    ax.set_box_aspect([1,1,1])
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex5_5_magnetic_dipole.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex5_5_magnetic_dipole.png")

def fig_ex5_4_magnetic_field():
    """問題4: 磁気双極子が作る磁場
    B = (1/4π)[3(m·r)r/r^5 - m/r^3], m=(0,0,1). 赤道面(z=0)では B は -z 方向。
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 磁気双極子 m = (0, 0, 1)
    ax.quiver(0, 0, 0, 0, 0, 1, color='r', arrow_length_ratio=0.3, linewidth=3, label='$\\boldsymbol{m}$')
    
    # 磁力線（赤道面 z=0 のみ。理論: m が +z のとき赤道面では B は常に -z 方向）
    theta = np.linspace(0, 2*np.pi, 20)
    r_cyl = np.linspace(0.6, 2, 10)  # 原点を避ける（r≥0.6）
    Theta, R_cyl = np.meshgrid(theta, r_cyl)
    
    X = R_cyl * np.sin(Theta)
    Y = R_cyl * np.cos(Theta)
    Z = np.zeros_like(X)
    
    r_sph = np.sqrt(X**2 + Y**2 + Z**2)
    r_sph = np.maximum(r_sph, 0.01)
    
    # B = (1/4π)[3(m·r)r/r^5 - m/r^3], m=(0,0,1). 赤道面では Bx=By=0, Bz = -1/r^3 < 0
    Bx = 3 * X * Z / (r_sph**5)
    By = 3 * Y * Z / (r_sph**5)
    Bz = (3 * Z**2 - r_sph**2) / (r_sph**5)
    
    # 向きのみ表示（単位ベクトル）にしてスケールの影響を除き、下向きであることを明確に
    B_norm = np.sqrt(Bx**2 + By**2 + Bz**2)
    B_norm = np.maximum(B_norm, 1e-10)
    u, v, w = Bx/B_norm, By/B_norm, Bz/B_norm
    ax.quiver(X, Y, Z, u, v, w, length=0.25, normalize=True, alpha=0.7, color='b')
    
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$y$', fontsize=12)
    ax.set_zlabel('$z$', fontsize=12)
    ax.set_title('磁気双極子が作る磁場', fontsize=14)
    ax.legend(fontsize=10)
    ax.set_box_aspect([1,1,1])
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex5_4_magnetic_field.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex5_4_magnetic_field.png")

def main():
    """すべての図を生成"""
    print("演習問題5の図を生成中...")
    fig_ex5_1_dielectric_half_space()
    fig_ex5_2_capacitor()
    fig_ex5_3_energy()
    fig_ex5_4_magnetic_field()
    fig_ex5_5_magnetic_dipole()
    print("すべての図の生成が完了しました。")

if __name__ == '__main__':
    main()
