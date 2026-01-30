#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
電磁気学演習問題4 (2025年11月14日) の図を生成するスクリプト
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

def fig_ex4_2_dielectric_sphere():
    """問題2: 外部電場中の誘電体球"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 構造
    a = 1.0
    E0 = 1.0
    
    # 誘電体球
    circle = patches.Circle((0, 0), a, fill=True, alpha=0.3, color='blue', edgecolor='b', linewidth=2, label='誘電体球')
    ax1.add_patch(circle)
    
    # 外部電場（概念的に）
    x = np.linspace(-2, 2, 10)
    y = np.linspace(-2, 2, 10)
    X, Y = np.meshgrid(x, y)
    
    # 外部電場はz方向（図ではy方向）
    U = np.zeros_like(X)
    V = np.ones_like(Y) * E0
    
    ax1.quiver(X, Y, U, V, scale=5, alpha=0.5, color='r', label='外部電場')
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$z$', fontsize=12)
    ax1.set_title('外部電場中の誘電体球', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    
    # 右図: 電場の分布
    r = np.linspace(0.1, 2, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    R, Theta = np.meshgrid(r, theta)
    
    X2 = R * np.cos(Theta)
    Y2 = R * np.sin(Theta)
    
    # 球内と球外で異なる電場
    E_inside = np.ones_like(R) * (3 * E0 / (2 + 1))  # 簡略化: epsilon/epsilon_0 = 2
    E_outside = E0 * (1 + (1 / (2 + 1)) * (a**3 / R**3))
    
    E = np.where(R < a, E_inside, E_outside)
    
    im = ax2.contourf(X2, Y2, E, levels=20, cmap='viridis')
    circle2 = patches.Circle((0, 0), a, fill=False, edgecolor='k', linewidth=2)
    ax2.add_patch(circle2)
    ax2.set_xlabel('$x$', fontsize=12)
    ax2.set_ylabel('$z$', fontsize=12)
    ax2.set_title('電場の分布', fontsize=14)
    plt.colorbar(im, ax=ax2, label='$E$')
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex4_2_dielectric_sphere.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex4_2_dielectric_sphere.png")

def fig_ex4_4_uniform_field():
    """問題4: 一様電場中の誘電体球"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 配置
    a = 1.0
    E0 = 1.0
    
    # 誘電体球
    circle = patches.Circle((0, 0), a, fill=True, alpha=0.3, color='blue', edgecolor='b', linewidth=2)
    ax1.add_patch(circle)
    
    # 一様電場
    x = np.linspace(-2, 2, 15)
    y = np.linspace(-2, 2, 15)
    X, Y = np.meshgrid(x, y)
    
    U = np.zeros_like(X)
    V = np.ones_like(Y) * E0
    
    ax1.quiver(X, Y, U, V, scale=5, alpha=0.6, color='r')
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$z$', fontsize=12)
    ax1.set_title('一様電場中の誘電体球', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    
    # 右図: 等電位線
    r = np.linspace(0.1, 2, 100)
    theta = np.linspace(0, 2*np.pi, 100)
    R, Theta = np.meshgrid(r, theta)
    
    X2 = R * np.cos(Theta)
    Y2 = R * np.sin(Theta)
    
    # 球内と球外で異なる電位
    epsilon_ratio = 2.0  # epsilon/epsilon_0
    phi_inside = -3 * epsilon_ratio / (epsilon_ratio + 2) * E0 * R * np.cos(Theta)
    phi_outside = -E0 * R * np.cos(Theta) + (epsilon_ratio - 1) / (epsilon_ratio + 2) * E0 * a**3 * np.cos(Theta) / R**2
    
    phi = np.where(R < a, phi_inside, phi_outside)
    
    im = ax2.contourf(X2, Y2, phi, levels=20, cmap='RdYlBu')
    circle2 = patches.Circle((0, 0), a, fill=False, edgecolor='k', linewidth=2)
    ax2.add_patch(circle2)
    ax2.contour(X2, Y2, phi, levels=20, colors='black', alpha=0.3, linewidths=0.5)
    ax2.set_xlabel('$x$', fontsize=12)
    ax2.set_ylabel('$z$', fontsize=12)
    ax2.set_title('等電位線', fontsize=14)
    plt.colorbar(im, ax=ax2, label='$\\phi$')
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex4_4_uniform_field.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex4_4_uniform_field.png")

def fig_ex4_1_cavity_field():
    """問題1: 誘電体の内部電場（空洞内電場）"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 空洞の構造
    a = 1.0
    P = 1.0
    
    # 誘電体
    circle_outer = patches.Circle((0, 0), 2*a, fill=True, alpha=0.2, color='blue', edgecolor='b', linewidth=2)
    ax1.add_patch(circle_outer)
    
    # 空洞
    circle_cavity = patches.Circle((0, 0), a, fill=True, alpha=1.0, color='white', edgecolor='k', linewidth=2)
    ax1.add_patch(circle_cavity)
    
    # 分極ベクトル
    ax1.arrow(0, 0, 0, 0.8, head_width=0.1, head_length=0.1, fc='r', ec='r', linewidth=2, label='$\\boldsymbol{P}$')
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$z$', fontsize=12)
    ax1.set_title('誘電体内の球形空洞', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-2.5*a, 2.5*a)
    ax1.set_ylim(-2.5*a, 2.5*a)
    
    # 右図: 空洞内電場
    theta = np.linspace(0, 2*np.pi, 100)
    E_cavity = -P / (3 * 1.0)  # epsilon_0 = 1.0と仮定
    
    ax2.arrow(0, 0, 0, E_cavity, head_width=0.1, head_length=0.1, fc='b', ec='b', linewidth=2)
    ax2.text(0.2, E_cavity/2, '$\\boldsymbol{E}_{\\text{cavity}}$', fontsize=12)
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1.5, 0.5)
    ax2.set_xlabel('$x$', fontsize=12)
    ax2.set_ylabel('$z$', fontsize=12)
    ax2.set_title('空洞内の電場', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex4_1_cavity_field.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex4_1_cavity_field.png")

def fig_ex4_3_dielectric_interface():
    """問題3: 誘電体境界面での鏡像法"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 配置
    a = 1.0
    epsilon_1 = 2.0
    epsilon_2 = 1.0
    
    # 境界面
    ax1.axhline(y=0, color='k', linewidth=2, linestyle='-', label='境界面 $z=0$')
    
    # 点電荷
    ax1.scatter([0], [a], s=300, c='r', marker='+', linewidths=3, label='$q_1$')
    ax1.scatter([0], [-a], s=300, c='b', marker='_', linewidths=3, label='$q_2$')
    
    # 領域の表示
    ax1.fill_between([-2, 2], [0, 0], [2, 2], alpha=0.1, color='blue', label='$\\varepsilon_1$')
    ax1.fill_between([-2, 2], [0, 0], [-2, -2], alpha=0.1, color='green', label='$\\varepsilon_2$')
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$z$', fontsize=12)
    ax1.set_title('誘電体境界面と点電荷', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_aspect('equal')
    
    # 右図: 力の比較
    epsilon_ratios = np.linspace(0.5, 2, 100)
    F1 = (epsilon_ratios - 1) / (epsilon_ratios + 1)
    F2 = (1 - epsilon_ratios) / (1 + epsilon_ratios)
    
    ax2.plot(epsilon_ratios, F1, 'r-', linewidth=2, label='$F_1$')
    ax2.plot(epsilon_ratios, F2, 'b--', linewidth=2, label='$F_2$')
    ax2.axvline(x=1, color='k', linestyle=':', alpha=0.5, label='$\\varepsilon_1 = \\varepsilon_2$')
    ax2.set_xlabel('$\\varepsilon_1/\\varepsilon_2$', fontsize=12)
    ax2.set_ylabel('力（規格化）', fontsize=12)
    ax2.set_title('各電荷に働く力の比較', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex4_3_dielectric_interface.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex4_3_dielectric_interface.png")

def main():
    """すべての図を生成"""
    print("演習問題4の図を生成中...")
    fig_ex4_1_cavity_field()
    fig_ex4_2_dielectric_sphere()
    fig_ex4_3_dielectric_interface()
    fig_ex4_4_uniform_field()
    print("すべての図の生成が完了しました。")

if __name__ == '__main__':
    main()
