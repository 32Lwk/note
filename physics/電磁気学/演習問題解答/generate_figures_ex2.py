#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
電磁気学演習問題2 (2025年10月17日) の図を生成するスクリプト
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# 日本語フォント設定
plt.rcParams['font.family'] = 'Hiragino Sans'

# 解像度設定
DPI = 300

# 出力ディレクトリ
OUTPUT_DIR = 'figures'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fig_ex2_3_charge_decay():
    """問題3: 導体内の電荷密度の時間的減少"""
    # パラメータ
    rho_0 = 1.0
    tau = 1.0  # 時定数
    
    # 時間
    t = np.linspace(0, 5*tau, 1000)
    
    # 電荷密度
    rho = rho_0 * np.exp(-t/tau)
    
    # プロット
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(t/tau, rho/rho_0, 'b-', linewidth=2)
    ax.axhline(y=1/np.e, color='r', linestyle='--', alpha=0.5, label='$1/e$')
    ax.axvline(x=1, color='r', linestyle='--', alpha=0.5)
    ax.set_xlabel('$t/\\tau$', fontsize=14)
    ax.set_ylabel('$\\rho(t)/\\rho_0$', fontsize=14)
    ax.set_title('導体内の電荷密度の時間的減少', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 5)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex2_3_charge_decay.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex2_3_charge_decay.png")

def fig_ex2_4_conductor_plate():
    """問題4: 導体板に誘起される電荷と電場の変化"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 電場の分布
    z = np.linspace(-2, 2, 100)
    E = np.zeros_like(z)
    E[z > 0] = 1.0  # 導体前方
    E[z < 0] = 0.0  # 導体後方
    
    ax1.plot(z, E, 'b-', linewidth=2)
    ax1.axvline(x=0, color='k', linestyle='--', linewidth=2, label='導体板')
    ax1.set_xlabel('$z$', fontsize=12)
    ax1.set_ylabel('$E$', fontsize=12)
    ax1.set_title('導体導入後の電場分布', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(-0.2, 1.2)
    
    # 右図: 電荷分布の概念図
    x = np.linspace(-2, 2, 100)
    y = np.zeros_like(x)
    sigma = np.ones_like(x) * 0.5  # 正の電荷密度
    
    ax2.plot(x, y, 'k-', linewidth=3, label='導体板')
    ax2.fill_between(x, -0.1, 0.1, alpha=0.3, color='blue', label='誘起電荷')
    ax2.set_xlabel('$x$', fontsize=12)
    ax2.set_ylabel('$y$', fontsize=12)
    ax2.set_title('導体面上の誘起電荷', fontsize=14)
    ax2.set_aspect('equal')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(-2, 2)
    ax2.set_ylim(-1, 1)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex2_4_conductor_plate.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex2_4_conductor_plate.png")

def fig_ex2_6_image_charge():
    """問題6: 接地導体平面と点電荷（鏡像法）"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 配置図
    # 点電荷
    ax1.scatter([0], [1], s=200, c='r', marker='+', linewidths=3, label='点電荷 $q$')
    # 鏡像電荷
    ax1.scatter([0], [-1], s=200, c='b', marker='_', linewidths=3, label='鏡像電荷 $-q$')
    # 導体板
    ax1.axhline(y=0, color='k', linewidth=3, linestyle='-', label='導体板 ($z=0$)')
    
    # 電場線（概念的に）
    z = np.linspace(0.1, 2, 50)
    for x_offset in [-1, 0, 1]:
        E_z = 1 / (x_offset**2 + z**2)**(3/2)
        ax1.plot([x_offset]*len(z), z, 'g--', alpha=0.3, linewidth=1)
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$z$', fontsize=12)
    ax1.set_title('鏡像法による配置', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_aspect('equal')
    
    # 右図: 電荷面密度の分布
    r = np.linspace(0, 3, 100)
    d = 1.0
    q = 1.0
    sigma = q * d / (2 * np.pi * (r**2 + d**2)**(3/2))
    
    ax2.plot(r, sigma, 'r-', linewidth=2)
    ax2.set_xlabel('$r = \\sqrt{x^2 + y^2}$', fontsize=12)
    ax2.set_ylabel('$\\sigma(r)$', fontsize=12)
    ax2.set_title('導体面上の電荷面密度分布', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex2_6_image_charge.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex2_6_image_charge.png")

def fig_ex2_1_energy_flow():
    """問題1: Maxwell方程式とエネルギー流れ"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: ポインティングベクトルの概念図
    x = np.linspace(-2, 2, 10)
    y = np.linspace(-2, 2, 10)
    X, Y = np.meshgrid(x, y)
    
    # 電場と磁場（概念的に）
    Ex = np.ones_like(X)
    Ey = np.zeros_like(Y)
    Hx = np.zeros_like(X)
    Hy = np.ones_like(Y)
    
    # ポインティングベクトル S = E × H
    Sx = Ey * 0 - Ex * 0  # z方向
    Sy = np.zeros_like(Y)
    
    ax1.quiver(X, Y, Ex, Ey, scale=5, alpha=0.6, color='r', label='電場 $\\boldsymbol{E}$', width=0.003)
    ax1.quiver(X, Y, Hx, Hy, scale=5, alpha=0.6, color='b', label='磁場 $\\boldsymbol{H}$', width=0.003)
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$y$', fontsize=12)
    ax1.set_title('電場と磁場の関係', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    
    # 右図: エネルギー密度の時間変化（概念的に）
    t = np.linspace(0, 2*np.pi, 100)
    W = 1 + 0.3 * np.sin(t)
    S_flux = -0.5 * np.cos(t)
    iE = 0.2 * np.ones_like(t)
    
    ax2.plot(t, W, 'b-', linewidth=2, label='$W$ (エネルギー密度)')
    ax2.plot(t, S_flux, 'r--', linewidth=2, label='$-\\nabla \\cdot \\boldsymbol{S}$')
    ax2.plot(t, iE, 'g:', linewidth=2, label='$\\boldsymbol{i} \\cdot \\boldsymbol{E}$')
    ax2.set_xlabel('時間', fontsize=12)
    ax2.set_ylabel('値', fontsize=12)
    ax2.set_title('エネルギー保存則の各項', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex2_1_energy_flow.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex2_1_energy_flow.png")

def fig_ex2_2_ohm_law():
    """問題2: 導体内の自由電子の運動とOhmの法則"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 電子の運動
    t = np.linspace(0, 5, 100)
    v = 1 - np.exp(-t)  # 定常状態への収束
    
    ax1.plot(t, v, 'b-', linewidth=2, label='速度 $v(t)$')
    ax1.axhline(y=1, color='r', linestyle='--', alpha=0.5, label='定常速度')
    ax1.set_xlabel('時間 $t$', fontsize=12)
    ax1.set_ylabel('速度 $v$', fontsize=12)
    ax1.set_title('電子の速度の時間変化', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # 右図: 電流密度と電場の関係
    E = np.linspace(0, 2, 100)
    sigma = 1.0
    i = sigma * E
    
    ax2.plot(E, i, 'r-', linewidth=2)
    ax2.set_xlabel('電場 $E$', fontsize=12)
    ax2.set_ylabel('電流密度 $i$', fontsize=12)
    ax2.set_title('Ohmの法則 $i = \\sigma E$', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex2_2_ohm_law.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex2_2_ohm_law.png")

def main():
    """すべての図を生成"""
    print("演習問題2の図を生成中...")
    fig_ex2_1_energy_flow()
    fig_ex2_2_ohm_law()
    fig_ex2_3_charge_decay()
    fig_ex2_4_conductor_plate()
    fig_ex2_6_image_charge()
    print("すべての図の生成が完了しました。")

if __name__ == '__main__':
    main()
