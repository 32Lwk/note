#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
電磁気学演習問題3 (2025年10月31日) の図を生成するスクリプト
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
import os

# 日本語フォント設定
plt.rcParams['font.family'] = 'Hiragino Sans'

# 解像度設定
DPI = 300

# 出力ディレクトリ
OUTPUT_DIR = 'figures'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fig_ex3_1_dipole():
    """問題1: 電気双極子の配置と電位"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 双極子の配置
    s = 1.0
    q = 1.0
    
    ax1.scatter([0], [s/2], s=300, c='r', marker='+', linewidths=3, label='$+q$')
    ax1.scatter([0], [-s/2], s=300, c='b', marker='_', linewidths=3, label='$-q$')
    ax1.plot([0, 0], [-s/2, s/2], 'k--', linewidth=2, alpha=0.5, label='双極子軸')
    
    # 電場線（概念的に）
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    X, Y = np.meshgrid(x, y)
    
    # 双極子の電位（近似）
    R = np.sqrt(X**2 + Y**2)
    R[R < 0.3] = 0.3  # 特異点を避ける
    phi = (Y) / R**3  # 双極子がz方向を向いている場合
    
    ax1.contour(X, Y, phi, levels=20, colors='gray', alpha=0.3, linewidths=0.5)
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$z$', fontsize=12)
    ax1.set_title('電気双極子の配置', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    
    # 右図: 電位の分布
    r = np.linspace(0.5, 3, 100)
    theta = np.linspace(0, np.pi, 100)
    R, Theta = np.meshgrid(r, theta)
    
    # 双極子の電位: phi = (p cos theta) / (4 pi epsilon_0 r^2)
    Phi = np.cos(Theta) / R**2
    
    im = ax2.contourf(R * np.sin(Theta), R * np.cos(Theta), Phi, levels=20, cmap='RdYlBu')
    ax2.set_xlabel('$x$', fontsize=12)
    ax2.set_ylabel('$z$', fontsize=12)
    ax2.set_title('双極子の電位分布', fontsize=14)
    plt.colorbar(im, ax=ax2)
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex3_1_dipole.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex3_1_dipole.png")

def fig_ex3_2_capacitor():
    """問題2: 誘電体入り同心導体球殻コンデンサー"""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # パラメータ
    a = 1.0
    b = 2.0
    
    # 球面の描画
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    u, v = np.meshgrid(u, v)
    
    # 内側の球面
    x_a = a * np.sin(v) * np.cos(u)
    y_a = a * np.sin(v) * np.sin(u)
    z_a = a * np.cos(v)
    ax.plot_surface(x_a, y_a, z_a, alpha=0.3, color='blue', label='$r = a$')
    
    # 外側の球面
    x_b = b * np.sin(v) * np.cos(u)
    y_b = b * np.sin(v) * np.sin(u)
    z_b = b * np.cos(v)
    ax.plot_surface(x_b, y_b, z_b, alpha=0.3, color='red', label='$r = b$')
    
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$y$', fontsize=12)
    ax.set_zlabel('$z$', fontsize=12)
    ax.set_title('誘電体入り同心導体球殻コンデンサー', fontsize=14)
    ax.set_box_aspect([1,1,1])
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex3_2_capacitor.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex3_2_capacitor.png")

def fig_ex3_3_image_charge():
    """問題3: 接地導体球と点電荷（鏡像法）"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 配置図
    a = 1.0
    d = 2.0
    q = 1.0
    q_prime = -a * q / d
    d_prime = a**2 / d
    
    # 導体球
    circle = patches.Circle((0, 0), a, fill=False, edgecolor='k', linewidth=2, label='導体球')
    ax1.add_patch(circle)
    
    # 点電荷
    ax1.scatter([d], [0], s=300, c='r', marker='+', linewidths=3, label='点電荷 $q$')
    # 鏡像電荷
    ax1.scatter([d_prime], [0], s=300, c='b', marker='_', linewidths=3, label='鏡像電荷 $q\'$')
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$y$', fontsize=12)
    ax1.set_title('接地導体球と点電荷（鏡像法）', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-0.5, 2.5)
    ax1.set_ylim(-1.5, 1.5)
    
    # 右図: 電位の分布（概念的に）
    x = np.linspace(-1, 3, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    
    # 点電荷と鏡像電荷による電位
    R1 = np.sqrt((X - d)**2 + Y**2)
    R2 = np.sqrt((X - d_prime)**2 + Y**2)
    R1[R1 < 0.1] = 0.1
    R2[R2 < 0.1] = 0.1
    
    phi = q / R1 + q_prime / R2
    
    # 導体球の外側のみ表示
    R_sphere = np.sqrt(X**2 + Y**2)
    phi[R_sphere < a] = np.nan
    
    im = ax2.contourf(X, Y, phi, levels=20, cmap='RdYlBu')
    circle2 = patches.Circle((0, 0), a, fill=False, edgecolor='k', linewidth=2)
    ax2.add_patch(circle2)
    ax2.set_xlabel('$x$', fontsize=12)
    ax2.set_ylabel('$y$', fontsize=12)
    ax2.set_title('電位分布', fontsize=14)
    plt.colorbar(im, ax=ax2)
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex3_3_image_charge.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex3_3_image_charge.png")

def fig_ex3_4_induced_dipole():
    """問題4: 微小導体球の誘起双極子"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 配置
    a = 0.5
    d = 2.0
    
    # 導体球
    circle = patches.Circle((0, 0), a, fill=True, alpha=0.3, color='blue', edgecolor='b', linewidth=2)
    ax1.add_patch(circle)
    
    # 点電荷
    ax1.scatter([0], [d], s=300, c='r', marker='+', linewidths=3, label='$-q$')
    ax1.scatter([0], [-d], s=300, c='b', marker='_', linewidths=3, label='$+q$')
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$z$', fontsize=12)
    ax1.set_title('微小導体球と点電荷の配置', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2.5, 2.5)
    
    # 右図: 誘導電荷面密度
    theta = np.linspace(0, np.pi, 100)
    E0 = 1.0
    epsilon_0 = 1.0
    sigma = 3 * epsilon_0 * E0 * np.cos(theta)
    
    ax2.plot(theta, sigma, 'r-', linewidth=2)
    ax2.set_xlabel('$\\theta$', fontsize=12)
    ax2.set_ylabel('$\\sigma(\\theta)$', fontsize=12)
    ax2.set_title('導体球表面の誘導電荷面密度', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, np.pi)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex3_4_induced_dipole.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex3_4_induced_dipole.png")

def fig_ex3_5_point_charge_dielectric():
    """問題5: 誘電体中の点電荷"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 電場の分布
    r = np.linspace(0.1, 3, 100)
    q = 1.0
    epsilon = 2.0
    epsilon_0 = 1.0
    
    E = q / (4 * np.pi * epsilon * r**2)
    
    ax1.plot(r, E, 'b-', linewidth=2, label='誘電体中')
    E_vacuum = q / (4 * np.pi * epsilon_0 * r**2)
    ax1.plot(r, E_vacuum, 'r--', linewidth=2, label='真空中')
    ax1.set_xlabel('$r$', fontsize=12)
    ax1.set_ylabel('$E(r)$', fontsize=12)
    ax1.set_title('誘電体中の点電荷が作る電場', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 3)
    
    # 右図: 分極ベクトル
    P = (1 - epsilon_0/epsilon) * q / (4 * np.pi * r**2)
    
    ax2.plot(r, P, 'g-', linewidth=2)
    ax2.set_xlabel('$r$', fontsize=12)
    ax2.set_ylabel('$P(r)$', fontsize=12)
    ax2.set_title('分極ベクトルの大きさ', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex3_5_point_charge_dielectric.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex3_5_point_charge_dielectric.png")

def main():
    """すべての図を生成"""
    print("演習問題3の図を生成中...")
    fig_ex3_1_dipole()
    fig_ex3_2_capacitor()
    fig_ex3_3_image_charge()
    fig_ex3_4_induced_dipole()
    fig_ex3_5_point_charge_dielectric()
    print("すべての図の生成が完了しました。")

if __name__ == '__main__':
    main()
