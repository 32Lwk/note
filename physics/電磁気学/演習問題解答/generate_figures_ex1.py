#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
電磁気学演習問題1 (2025年10月3日) の図を生成するスクリプト
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
from matplotlib import font_manager
import os

# 日本語フォント設定
plt.rcParams['font.family'] = 'Hiragino Sans'  # macOS
# Windows: 'MS Gothic', Linux: 'DejaVu Sans'

# 解像度設定
DPI = 300

# 出力ディレクトリ
OUTPUT_DIR = 'figures'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fig_ex1_1_electric_field():
    """問題1-1: 球殻内外の電場の大きさのr依存性"""
    # パラメータ
    a = 2.0  # 外半径
    b = 1.0  # 内半径
    rho = 1.0  # 電荷密度
    epsilon_0 = 1.0  # 真空の誘電率（規格化）
    
    # rの範囲
    r1 = np.linspace(0, b, 100)
    r2 = np.linspace(b, a, 100)
    r3 = np.linspace(a, 3*a, 100)
    
    # 各領域での電場
    E1 = np.zeros_like(r1)  # r < b
    E2 = rho / (3 * epsilon_0) * (r2 - b**3 / r2**2)  # b <= r <= a
    E3 = rho * (a**3 - b**3) / (3 * epsilon_0 * r3**2)  # r > a
    
    # プロット
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(r1, E1, 'b-', linewidth=2, label='$r < b$')
    ax.plot(r2, E2, 'r-', linewidth=2, label='$b \\leq r \\leq a$')
    ax.plot(r3, E3, 'g-', linewidth=2, label='$r > a$')
    ax.axvline(x=b, color='k', linestyle='--', alpha=0.5, label='$r = b$')
    ax.axvline(x=a, color='k', linestyle='--', alpha=0.5, label='$r = a$')
    ax.set_xlabel('$r$', fontsize=14)
    ax.set_ylabel('$E(r)$', fontsize=14)
    ax.set_title('球殻内外の電場の大きさ', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 3*a)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex1_1_electric_field.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex1_1_electric_field.png")

def fig_ex1_1_potential():
    """問題1-1: 球殻内外の電位のr依存性"""
    # パラメータ
    a = 2.0
    b = 1.0
    rho = 1.0
    epsilon_0 = 1.0
    
    # rの範囲
    r1 = np.linspace(0, b, 100)
    r2 = np.linspace(b, a, 100)
    r3 = np.linspace(a, 3*a, 100)
    
    # 各領域での電位
    phi1 = rho * (a**2 - b**2) / (2 * epsilon_0) * np.ones_like(r1)  # r < b
    phi2 = rho / (3 * epsilon_0) * (3*a**2 - r2**2) / 2 - rho * b**3 / (3 * epsilon_0 * r2)  # b <= r <= a
    phi3 = rho * (a**3 - b**3) / (3 * epsilon_0 * r3)  # r > a
    
    # プロット
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(r1, phi1, 'b-', linewidth=2, label='$r < b$')
    ax.plot(r2, phi2, 'r-', linewidth=2, label='$b \\leq r \\leq a$')
    ax.plot(r3, phi3, 'g-', linewidth=2, label='$r > a$')
    ax.axvline(x=b, color='k', linestyle='--', alpha=0.5)
    ax.axvline(x=a, color='k', linestyle='--', alpha=0.5)
    ax.set_xlabel('$r$', fontsize=14)
    ax.set_ylabel('$\\phi(r)$', fontsize=14)
    ax.set_title('球殻内外の電位', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 3*a)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex1_1_potential.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex1_1_potential.png")

def fig_ex1_1_geometry():
    """問題1-1: 球殻の幾何学的構造"""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # パラメータ
    a = 2.0
    b = 1.0
    
    # 球面の描画
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    u, v = np.meshgrid(u, v)
    
    # 外側の球面
    x_a = a * np.sin(v) * np.cos(u)
    y_a = a * np.sin(v) * np.sin(u)
    z_a = a * np.cos(v)
    ax.plot_surface(x_a, y_a, z_a, alpha=0.3, color='blue', label='$r = a$')
    
    # 内側の球面
    x_b = b * np.sin(v) * np.cos(u)
    y_b = b * np.sin(v) * np.sin(u)
    z_b = b * np.cos(v)
    ax.plot_surface(x_b, y_b, z_b, alpha=0.3, color='red', label='$r = b$')
    
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$y$', fontsize=12)
    ax.set_zlabel('$z$', fontsize=12)
    ax.set_title('球殻の幾何学的構造', fontsize=14)
    ax.set_box_aspect([1,1,1])
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex1_1_geometry.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex1_1_geometry.png")

def fig_ex1_4_circular_current():
    """問題4-1: 円形電流が作る磁場"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # パラメータ
    a = 1.0  # 円の半径
    I = 1.0
    mu_0 = 1.0
    
    # 円形電流の描画
    phi = np.linspace(0, 2*np.pi, 100)
    x_circle = a * np.cos(phi)
    y_circle = a * np.sin(phi)
    z_circle = np.zeros_like(phi)
    ax.plot(x_circle, y_circle, z_circle, 'b-', linewidth=3, label='円形電流')
    
    # z軸上の磁場ベクトル
    z_vals = np.linspace(-2*a, 2*a, 20)
    for z in z_vals:
        if abs(z) > 0.1:  # z=0付近を避ける
            B_mag = mu_0 * I * a**2 / (2 * (a**2 + z**2)**(3/2))
            ax.quiver(0, 0, z, 0, 0, B_mag*0.5, color='r', arrow_length_ratio=0.3, alpha=0.6)
    
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$y$', fontsize=12)
    ax.set_zlabel('$z$', fontsize=12)
    ax.set_title('円形電流が作る磁場（z軸上）', fontsize=14)
    ax.legend(fontsize=10)
    ax.set_box_aspect([1,1,1])
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex1_4_circular_current.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex1_4_circular_current.png")

def fig_ex1_4_solenoid():
    """問題4-2: 無限ソレノイドの磁場分布"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # パラメータ
    a = 1.0
    n = 1.0
    I = 1.0
    mu_0 = 1.0
    
    # 左図: ソレノイドの構造
    z_vals = np.linspace(-3*a, 3*a, 100)
    for i in range(-3, 4):
        circle = patches.Circle((0, i*a), a, fill=False, edgecolor='b', linewidth=2)
        ax1.add_patch(circle)
    
    ax1.set_xlim(-2*a, 2*a)
    ax1.set_ylim(-3.5*a, 3.5*a)
    ax1.set_aspect('equal')
    ax1.set_xlabel('$r$', fontsize=12)
    ax1.set_ylabel('$z$', fontsize=12)
    ax1.set_title('ソレノイドの構造', fontsize=14)
    ax1.grid(True, alpha=0.3)
    
    # 右図: 磁場の大きさ
    r_vals = np.linspace(0, 2*a, 100)
    B_inside = mu_0 * n * I * np.ones_like(r_vals[r_vals < a])
    B_outside = np.zeros_like(r_vals[r_vals >= a])
    
    ax2.plot(r_vals[r_vals < a], B_inside, 'r-', linewidth=2, label='内部 ($r < a$)')
    ax2.plot(r_vals[r_vals >= a], B_outside, 'b-', linewidth=2, label='外部 ($r > a$)')
    ax2.axvline(x=a, color='k', linestyle='--', alpha=0.5, label='$r = a$')
    ax2.set_xlabel('$r$', fontsize=12)
    ax2.set_ylabel('$B(r)$', fontsize=12)
    ax2.set_title('磁場の分布', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex1_4_solenoid.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex1_4_solenoid.png")

def fig_ex1_5_coaxial():
    """問題5: 同軸円筒抵抗体の構造とポインティングベクトル"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # パラメータ
    a = 2.0
    b = 1.0
    i = 1.0
    sigma = 1.0
    
    # 左図: 構造
    circle_outer = patches.Circle((0, 0), a, fill=False, edgecolor='b', linewidth=2, label='外側 ($r = a$)')
    circle_inner = patches.Circle((0, 0), b, fill=False, edgecolor='r', linewidth=2, label='内側 ($r = b$)')
    ax1.add_patch(circle_outer)
    ax1.add_patch(circle_inner)
    ax1.set_xlim(-2.5*a, 2.5*a)
    ax1.set_ylim(-2.5*a, 2.5*a)
    ax1.set_aspect('equal')
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$y$', fontsize=12)
    ax1.set_title('同軸円筒抵抗体の構造', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # 右図: ポインティングベクトルの大きさ
    r_vals = np.linspace(b, a, 100)
    S_mag = i**2 * (r_vals**2 - b**2) / (2 * sigma * r_vals)
    
    ax2.plot(r_vals, S_mag, 'r-', linewidth=2)
    ax2.axvline(x=b, color='k', linestyle='--', alpha=0.5, label='$r = b$')
    ax2.axvline(x=a, color='k', linestyle='--', alpha=0.5, label='$r = a$')
    ax2.set_xlabel('$r$', fontsize=12)
    ax2.set_ylabel('$|\\boldsymbol{S}|$', fontsize=12)
    ax2.set_title('ポインティングベクトルの大きさ', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex1_5_coaxial.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex1_5_coaxial.png")

def fig_ex1_6_wave():
    """問題6: 電磁波の進行"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # パラメータ
    k = 1.0
    omega = 1.0
    c = omega / k
    
    # 時間発展
    z_vals = np.linspace(0, 4*np.pi/k, 200)
    t_vals = [0, np.pi/(2*omega), np.pi/omega]
    colors = ['b', 'r', 'g']
    labels = ['$t = 0$', '$t = \\pi/(2\\omega)$', '$t = \\pi/\\omega$']
    
    for i, t in enumerate(t_vals):
        E = np.cos(k * z_vals - omega * t)
        ax1.plot(z_vals, E, color=colors[i], linewidth=2, label=labels[i])
    
    ax1.set_xlabel('$z$', fontsize=12)
    ax1.set_ylabel('$E(z,t)$', fontsize=12)
    ax1.set_title('電磁波の時間発展', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # 位相速度と群速度
    omega_vals = np.linspace(0.1, 5, 100)
    k_vals = omega_vals / c
    v_phase = omega_vals / k_vals
    v_group = np.ones_like(omega_vals) * c
    
    ax2.plot(omega_vals, v_phase, 'b-', linewidth=2, label='位相速度 $v_p$')
    ax2.plot(omega_vals, v_group, 'r--', linewidth=2, label='群速度 $v_g$')
    ax2.axhline(y=c, color='k', linestyle=':', alpha=0.5, label='$c$')
    ax2.set_xlabel('$\\omega$', fontsize=12)
    ax2.set_ylabel('速度', fontsize=12)
    ax2.set_title('位相速度と群速度', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex1_6_wave.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex1_6_wave.png")

def main():
    """すべての図を生成"""
    print("演習問題1の図を生成中...")
    fig_ex1_1_electric_field()
    fig_ex1_1_potential()
    fig_ex1_1_geometry()
    fig_ex1_4_circular_current()
    fig_ex1_4_solenoid()
    fig_ex1_5_coaxial()
    fig_ex1_6_wave()
    print("すべての図の生成が完了しました。")

if __name__ == '__main__':
    main()
