#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
電磁気学演習問題6 (2025年12月12日) の図を生成するスクリプト
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

def fig_ex6_3_magnetized_sphere():
    """問題3: 一様に磁化した強磁性体球の磁場"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 磁力線の分布
    a = 1.0
    M = 1.0
    
    # 球
    circle = patches.Circle((0, 0), a, fill=True, alpha=0.3, color='blue', edgecolor='b', linewidth=2, label='強磁性体球')
    ax1.add_patch(circle)
    
    # 磁力線（概念的に）
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    X, Y = np.meshgrid(x, y)
    
    R = np.sqrt(X**2 + Y**2)
    Theta = np.arctan2(Y, X)
    
    # 球外の磁場（双極子場）
    Bx_out = np.where(R > a, 3 * M * a**3 * X * Y / (3 * R**5), 0)
    By_out = np.where(R > a, M * a**3 * (3 * Y**2 - R**2) / (3 * R**5), 0)
    
    # 球内の磁場（一様）
    Bx_in = np.where(R < a, 0, 0)
    By_in = np.where(R < a, 2 * M / 3, 0)
    
    Bx = np.where(R < a, Bx_in, Bx_out)
    By = np.where(R < a, By_in, By_out)
    
    # 正規化
    B_mag = np.sqrt(Bx**2 + By**2)
    Bx[B_mag > 0] /= B_mag[B_mag > 0]
    By[B_mag > 0] /= B_mag[B_mag > 0]
    
    ax1.quiver(X, Y, Bx, By, scale=10, alpha=0.6, color='r', width=0.003)
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$z$', fontsize=12)
    ax1.set_title('磁力線の分布', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    
    # 右図: 磁場の大きさ
    r = np.linspace(0.1, 2, 100)
    theta = np.linspace(0, np.pi, 100)
    R2, Theta2 = np.meshgrid(r, theta)
    
    X2 = R2 * np.cos(Theta2)
    Y2 = R2 * np.sin(Theta2)
    
    # 球内と球外で異なる磁場
    B_inside = np.ones_like(R2) * (2 * M / 3)
    B_outside = M * a**3 / (3 * R2**3) * np.sqrt(1 + 3 * np.cos(Theta2)**2)
    
    B = np.where(R2 < a, B_inside, B_outside)
    
    im = ax2.contourf(X2, Y2, B, levels=20, cmap='viridis')
    circle2 = patches.Circle((0, 0), a, fill=False, edgecolor='k', linewidth=2)
    ax2.add_patch(circle2)
    ax2.set_xlabel('$x$', fontsize=12)
    ax2.set_ylabel('$z$', fontsize=12)
    ax2.set_title('磁場の大きさ', fontsize=14)
    plt.colorbar(im, ax=ax2, label='$|\\boldsymbol{B}|$')
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex6_3_magnetized_sphere.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex6_3_magnetized_sphere.png")

def fig_ex6_1_magnetized_sphere():
    """問題1: 外部磁場中の常磁性体球"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 磁化電流
    a = 1.0
    theta = np.linspace(0, np.pi, 100)
    M = 1.0
    mu_0 = 1.0
    j_M = M * np.sin(theta) / mu_0
    
    ax1.plot(theta, j_M, 'b-', linewidth=2)
    ax1.set_xlabel('$\\theta$', fontsize=12)
    ax1.set_ylabel('$j_M(\\theta)$', fontsize=12)
    ax1.set_title('球面上の磁化電流の線密度', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, np.pi)
    
    # 右図: 磁場の関係
    mu_ratios = np.linspace(1, 5, 100)
    M_norm = 3 * (mu_ratios - 1) / (mu_ratios + 2)
    
    ax2.plot(mu_ratios, M_norm, 'r-', linewidth=2)
    ax2.set_xlabel('$\\mu/\\mu_0$', fontsize=12)
    ax2.set_ylabel('$M/B_0$ (規格化)', fontsize=12)
    ax2.set_title('磁化の透磁率依存性', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex6_1_magnetized_sphere.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex6_1_magnetized_sphere.png")

def fig_ex6_2_magnetic_plate():
    """問題2: 外部磁場中の常磁性体板"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 板面が磁場に平行
    H0 = 1.0
    mu = 2.0
    mu_0 = 1.0
    M_parallel = (mu - mu_0) / mu_0 * H0
    
    ax1.barh([0], [M_parallel], color='blue', alpha=0.6, label='$M_{\\parallel}$')
    ax1.set_xlabel('$M$', fontsize=12)
    ax1.set_ylabel('', fontsize=12)
    ax1.set_title('板面が磁場に平行な場合', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3, axis='x')
    
    # 右図: 板面が磁場に垂直
    M_perp = (mu - mu_0) / mu * H0
    
    ax2.barh([0], [M_perp], color='green', alpha=0.6, label='$M_{\\perp}$')
    ax2.set_xlabel('$M$', fontsize=12)
    ax2.set_ylabel('', fontsize=12)
    ax2.set_title('板面が磁場に垂直な場合', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex6_2_magnetic_plate.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex6_2_magnetic_plate.png")

def fig_ex6_4_energy():
    """問題4: 磁性体の磁気エネルギー"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # インダクタンスとエネルギーの関係
    I = np.linspace(0, 2, 100)
    L = 1.0
    U = 0.5 * L * I**2
    
    ax.plot(I, U, 'b-', linewidth=2)
    ax.set_xlabel('電流 $I$', fontsize=12)
    ax.set_ylabel('磁気エネルギー $U_m$', fontsize=12)
    ax.set_title('磁気エネルギーと電流の関係', fontsize=14)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex6_4_energy.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex6_4_energy.png")

def main():
    """すべての図を生成"""
    print("演習問題6の図を生成中...")
    fig_ex6_1_magnetized_sphere()
    fig_ex6_2_magnetic_plate()
    fig_ex6_3_magnetized_sphere()
    fig_ex6_4_energy()
    print("すべての図の生成が完了しました。")

if __name__ == '__main__':
    main()
