#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
電磁気学演習問題7 (2025年12月26日) の図を生成するスクリプト
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

def fig_ex7_1_dielectric_dispersion():
    """問題1: 誘電率の周波数依存性（実部と虚部）"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # パラメータ
    chi_0 = 1.0
    tau = 1.0
    epsilon_0 = 1.0
    
    # 周波数範囲
    omega_tau = np.logspace(-2, 2, 1000)
    omega = omega_tau / tau
    
    # 実部と虚部
    epsilon_real = epsilon_0 * (1 + chi_0 / (1 + omega_tau**2))
    epsilon_imag = epsilon_0 * chi_0 * omega_tau / (1 + omega_tau**2)
    
    # 左図: 線形スケール
    ax1.plot(omega_tau, epsilon_real / epsilon_0, 'b-', linewidth=2, label='実部 $\\varepsilon\'/\\varepsilon_0$')
    ax1.plot(omega_tau, epsilon_imag / epsilon_0, 'r--', linewidth=2, label='虚部 $\\varepsilon\'\'/\\varepsilon_0$')
    ax1.axvline(x=1, color='k', linestyle=':', alpha=0.5, label='$\\omega\\tau = 1$')
    ax1.set_xlabel('$\\omega\\tau$', fontsize=12)
    ax1.set_ylabel('$\\varepsilon/\\varepsilon_0$', fontsize=12)
    ax1.set_title('誘電率の周波数依存性（線形スケール）', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 5)
    
    # 右図: 対数スケール
    ax2.semilogx(omega_tau, epsilon_real / epsilon_0, 'b-', linewidth=2, label='実部 $\\varepsilon\'/\\varepsilon_0$')
    ax2.semilogx(omega_tau, epsilon_imag / epsilon_0, 'r--', linewidth=2, label='虚部 $\\varepsilon\'\'/\\varepsilon_0$')
    ax2.axvline(x=1, color='k', linestyle=':', alpha=0.5, label='$\\omega\\tau = 1$')
    ax2.set_xlabel('$\\omega\\tau$', fontsize=12)
    ax2.set_ylabel('$\\varepsilon/\\varepsilon_0$', fontsize=12)
    ax2.set_title('誘電率の周波数依存性（対数スケール）', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0.01, 100)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex7_1_dielectric_dispersion.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex7_1_dielectric_dispersion.png")

def fig_ex7_4_reflection():
    """問題4: 媒質境界面での電磁波の反射"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 反射の概念図
    # 入射波
    z_inc = np.linspace(-2, 0, 100)
    E_inc = np.cos(2 * np.pi * z_inc)
    ax1.plot(z_inc, E_inc, 'b-', linewidth=2, label='入射波')
    
    # 反射波
    z_ref = np.linspace(-2, 0, 100)
    E_ref = 0.2 * np.cos(2 * np.pi * (-z_ref) + np.pi)  # 位相がπずれる
    ax1.plot(z_ref, E_ref, 'r--', linewidth=2, label='反射波')
    
    # 透過波
    z_trans = np.linspace(0, 2, 100)
    E_trans = 0.8 * np.cos(2 * np.pi * z_trans)
    ax1.plot(z_trans, E_trans, 'g-', linewidth=2, label='透過波')
    
    # 境界面
    ax1.axvline(x=0, color='k', linewidth=2, linestyle='-', label='境界面')
    ax1.fill_between([-2, 0], [-2, -2], [2, 2], alpha=0.1, color='blue', label='真空')
    ax1.fill_between([0, 2], [-2, -2], [2, 2], alpha=0.1, color='green', label='媒質')
    
    ax1.set_xlabel('$z$', fontsize=12)
    ax1.set_ylabel('$E$', fontsize=12)
    ax1.set_title('電磁波の反射と透過', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-1.5, 1.5)
    
    # 右図: 反射率の屈折率依存性
    n = np.linspace(1, 5, 1000)
    R = ((n - 1) / (n + 1))**2
    
    ax2.plot(n, R * 100, 'b-', linewidth=2)
    ax2.axvline(x=1.5, color='r', linestyle='--', alpha=0.5, label='ガラス ($n=1.5$)')
    ax2.axhline(y=4, color='r', linestyle='--', alpha=0.5)
    ax2.set_xlabel('屈折率 $n$', fontsize=12)
    ax2.set_ylabel('反射率 $R$ [\%]', fontsize=12)
    ax2.set_title('反射率の屈折率依存性', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(1, 5)
    ax2.set_ylim(0, 50)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex7_4_reflection.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex7_4_reflection.png")

def fig_ex7_2_retarded_potential():
    """問題2: 遅延ポテンシャル"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 遅延時間の概念
    r = np.linspace(0.1, 3, 100)
    c = 1.0
    t = 1.0
    t_prime = t - r / c
    
    ax1.plot(r, t_prime, 'b-', linewidth=2, label='$t\' = t - r/c$')
    ax1.axhline(y=0, color='r', linestyle='--', alpha=0.5, label='$t\' = 0$')
    ax1.set_xlabel('距離 $r$', fontsize=12)
    ax1.set_ylabel('遅延時間 $t\'$', fontsize=12)
    ax1.set_title('遅延時間の距離依存性', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # 右図: 電場の時間変化（概念的に）
    t_vals = np.linspace(0, 2*np.pi, 100)
    r_vals = [0.5, 1.0, 2.0]
    
    for r_val in r_vals:
        t_prime_vals = t_vals - r_val / c
        E = np.cos(t_prime_vals)
        ax2.plot(t_vals, E, linewidth=2, label=f'$r = {r_val}$')
    
    ax2.set_xlabel('観測時間 $t$', fontsize=12)
    ax2.set_ylabel('電場 $E$', fontsize=12)
    ax2.set_title('遅延による電場の時間変化', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex7_2_retarded_potential.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex7_2_retarded_potential.png")

def fig_ex7_3_scattering():
    """問題3: 微小誘電体球による光の吸収と散乱"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 吸収断面積
    omega = np.linspace(0.1, 10, 100)
    V = 1.0
    c = 1.0
    epsilon_0 = 1.0
    epsilon_double_prime = 0.1
    
    C_a = V * omega * epsilon_double_prime / (c * epsilon_0)
    
    ax1.plot(omega, C_a, 'r-', linewidth=2)
    ax1.set_xlabel('角振動数 $\\omega$', fontsize=12)
    ax1.set_ylabel('吸収断面積 $C_a$', fontsize=12)
    ax1.set_title('吸収断面積の周波数依存性', fontsize=14)
    ax1.grid(True, alpha=0.3)
    
    # 右図: 散乱断面積
    epsilon_prime = 2.0
    epsilon_0 = 1.0
    C_s = 8 * np.pi / 3 * omega**4 * V**2 / c**4 * ((epsilon_prime - epsilon_0) / (epsilon_prime + 2*epsilon_0))**2
    
    ax2.loglog(omega, C_s, 'b-', linewidth=2)
    ax2.set_xlabel('角振動数 $\\omega$', fontsize=12)
    ax2.set_ylabel('散乱断面積 $C_s$', fontsize=12)
    ax2.set_title('散乱断面積の周波数依存性（レイリー散乱）', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ex7_3_scattering.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/ex7_3_scattering.png")

def main():
    """すべての図を生成"""
    print("演習問題7の図を生成中...")
    fig_ex7_1_dielectric_dispersion()
    fig_ex7_2_retarded_potential()
    fig_ex7_3_scattering()
    fig_ex7_4_reflection()
    print("すべての図の生成が完了しました。")

if __name__ == '__main__':
    main()
