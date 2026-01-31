#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
電磁気学 過去問 解答・解説用の図を生成するスクリプト
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
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


# ========== 2023年度 問題2 ==========

def fig_em2023_dielectric_vertical():
    """2023 問題2(2-1)(2-2): 誘電体板を外部電場に垂直に置いた場合"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)

    # 誘電体板（水平帯）
    rect = Rectangle((-1.5, -0.4), 3, 0.8, facecolor='lightblue', edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(0, 0, r'誘電体 $\varepsilon$', fontsize=12, ha='center', va='center')

    # 外部電場 E0（上向き矢印）
    ax.annotate('', xy=(0.5, 1.5), xytext=(0.5, 0.6),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(0.7, 1.05, r'$\mathbf{E}_0$', fontsize=14, color='red')

    # 内部電場 E（上向き、短い矢印）
    ax.annotate('', xy=(-0.5, 0.2), xytext=(-0.5, -0.2),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.text(-0.7, 0, r'$\mathbf{E}$', fontsize=12, color='blue')

    # D は連続
    ax.text(1.2, -1.5, r'$\mathbf{D} = \varepsilon_0 \mathbf{E}_0$（連続）', fontsize=11)
    ax.text(1.2, -2.2, r'$\mathbf{E} = \frac{\varepsilon_0}{\varepsilon}\mathbf{E}_0$', fontsize=11)
    ax.set_title('問題2(2-1)(2-2): 誘電体板を垂直に置いた場合', fontsize=14)
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$z$', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em2023_dielectric_vertical.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em2023_dielectric_vertical.png")


def fig_em2023_dielectric_tilted():
    """2023 問題2(2-3): 誘電体板を斜めに置いた場合"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)

    # 斜めの板（平行四辺形）
    theta = np.deg2rad(30)
    w, h = 2.0, 0.5
    x1, y1 = -w*np.cos(theta) + h*np.sin(theta)/2, -w*np.sin(theta) - h*np.cos(theta)/2
    rect = mpatches.Polygon([
        [x1, y1],
        [x1 + w*np.cos(theta), y1 + w*np.sin(theta)],
        [x1 + w*np.cos(theta) - h*np.sin(theta), y1 + w*np.sin(theta) + h*np.cos(theta)],
        [x1 - h*np.sin(theta), y1 + h*np.cos(theta)]
    ], facecolor='lightblue', edgecolor='black', linewidth=2)
    ax.add_patch(rect)

    # E0 と法線のなす角 θ0
    ax.annotate('', xy=(0, 1.5), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(0.3, 0.8, r'$\mathbf{E}_0$', fontsize=14, color='red')
    ax.text(0.8, 0.3, r'$\theta_0$', fontsize=14)
    ax.set_title('問題2(2-3): 誘電体板を斜めに置いた場合（法線と $\\mathbf{E}_0$ のなす角 $\\theta_0$）', fontsize=14)
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$z$', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em2023_dielectric_tilted.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em2023_dielectric_tilted.png")


def fig_em2023_conductor_plate():
    """2023 問題2(2-4): 導体板を電場に垂直に置いたときの静電誘導"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)

    # 導体板
    rect = Rectangle((-1.5, -0.4), 3, 0.8, facecolor='lightgray', edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(0, 0, '導体', fontsize=12, ha='center', va='center')

    # 上面 +σ、下面 -σ
    ax.text(1.2, 0.5, r'$+\sigma$', fontsize=14, color='blue')
    ax.text(1.2, -0.5, r'$-\sigma$', fontsize=14, color='blue')

    # 外部電場 E0
    ax.annotate('', xy=(0.5, 1.5), xytext=(0.5, 0.6),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(0.7, 1.05, r'$\mathbf{E}_0$', fontsize=14, color='red')
    ax.text(1.2, -1.8, r'$\sigma = \varepsilon_0 E_0$', fontsize=12)
    ax.set_title('問題2(2-4): 導体板を垂直に置いたときの静電誘導', fontsize=14)
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$z$', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em2023_conductor_plate.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em2023_conductor_plate.png")


def fig_em2023_intensity_decay():
    """2023 問題3(3-2): 金属内部での光の強度の減衰 I_1(z) = I_0(1-R)exp(-2βz)"""
    z = np.linspace(0, 3, 200)
    beta = 1.0  # 規格化
    R = 0.9
    I0 = 1.0
    I1 = I0 * (1 - R) * np.exp(-2 * beta * z)
    delta = 1 / beta  # スキン深度

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(z, I1, 'b-', linewidth=2, label=r'$I_1(z) = I_0(1-R)e^{-2\beta z}$')
    ax.axvline(delta, color='gray', linestyle='--', alpha=0.8, label=r'スキン深度 $\delta = 1/\beta$')
    ax.axhline(I0 * (1 - R) / np.e, color='gray', linestyle=':', alpha=0.7)
    ax.set_xlabel(r'$z$（金属内部の深さ）', fontsize=12)
    ax.set_ylabel(r'強度 $I_1$', fontsize=12)
    ax.set_title('問題3(3-2): 金属内部での光の強度の減衰（$z=0$ が金属表面）', fontsize=14)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, I0 * (1 - R) * 1.05)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em2023_intensity_decay.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em2023_intensity_decay.png")


def fig_em2023_metal_reflection():
    """2023 問題3: 真空から金属表面への垂直入射と反射・減衰"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(-1, 4)
    ax.set_ylim(-2, 2)
    ax.axvline(0, color='black', linewidth=2, label='境界 z=0')
    ax.axhline(0, color='gray', linewidth=0.5)

    # 真空側
    ax.fill_between([-1, 0], -2, 2, facecolor='white', alpha=0.5)
    ax.text(-0.5, 1.2, '真空', fontsize=12)
    # 金属側
    ax.fill_between([0, 4], -2, 2, facecolor='silver', alpha=0.5)
    ax.text(2, 1.2, '金属', fontsize=12)

    # 入射・反射・透過（矢印）
    ax.annotate('', xy=(-0.8, 0.5), xytext=(-0.2, 0.5),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.text(-0.6, 0.7, '入射', fontsize=10, color='blue')
    ax.annotate('', xy=(-0.2, -0.5), xytext=(-0.8, -0.5),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(-0.6, -0.7, '反射', fontsize=10, color='green')
    ax.annotate('', xy=(1.5, 0.3), xytext=(0.1, 0.3),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(0.8, 0.5, r'透過（減衰 $e^{-\beta z}$）', fontsize=10, color='red')
    ax.set_xlabel('$z$', fontsize=12)
    ax.set_title('問題3: 金属表面への垂直入射（反射率 $R$、内部で減衰）', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em2023_metal_reflection.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em2023_metal_reflection.png")


def fig_em2023_metal_slab():
    """2023 問題3(3-3): 厚み d の金属板と多重反射"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(-1, 4)
    ax.set_ylim(-2, 2)
    ax.axvline(0, color='black', linewidth=2)
    ax.axvline(2, color='black', linewidth=2)
    ax.axhline(0, color='gray', linewidth=0.5)

    ax.fill_between([-1, 0], -2, 2, facecolor='white', alpha=0.5)
    ax.text(-0.5, 1.2, '真空', fontsize=12)
    ax.fill_between([0, 2], -2, 2, facecolor='silver', alpha=0.5)
    ax.text(1, 1.2, r'金属（厚み $d$）', fontsize=12)
    ax.fill_between([2, 4], -2, 2, facecolor='white', alpha=0.5)
    ax.text(3, 1.2, '真空', fontsize=12)

    ax.annotate('', xy=(0.2, 0.5), xytext=(-0.5, 0.5),
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
    ax.annotate('', xy=(1.8, 0.3), xytext=(0.3, 0.3),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax.annotate('', xy=(2.5, 0.4), xytext=(1.9, 0.4),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
    ax.text(1, -1.2, '多重反射により透過光を足し合わせる', fontsize=11, ha='center')
    ax.set_xlabel('$z$', fontsize=12)
    ax.set_title('問題3(3-3): 厚み $d$ の金属板を通過後の強度 $I_2$', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em2023_metal_slab.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em2023_metal_slab.png")


# ========== 2024年度 問題2 ==========

def fig_em2024_ferro_sphere_field():
    """2024 問題2(2-3): 強誘電体球内外の電気力線と電束線の概略（xz平面）"""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)

    # 球
    circle = Circle((0, 0), 1, facecolor='lightblue', edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(0, 0, r'$\mathbf{P}$', fontsize=14, ha='center', va='center')

    # 内部: ε0 E は下向き、D は上向き（概略の矢印）
    ax.annotate('', xy=(0.3, -0.3), xytext=(0.3, 0.3),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.text(0.5, 0, r'$\varepsilon_0\mathbf{E}$', fontsize=11, color='blue')
    ax.annotate('', xy=(-0.3, 0.3), xytext=(-0.3, -0.3),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(-0.6, 0, r'$\mathbf{D}$', fontsize=11, color='red')

    # 外部の力線（双極子型の概略）
    th = np.linspace(0.3, np.pi - 0.3, 8)
    for t in th:
        r = 1.5
        x, y = r * np.cos(t), r * np.sin(t)
        dx, dy = np.cos(t), np.sin(t)
        ax.quiver(x, y, -dx*0.3, -dy*0.3, color='blue', scale=5)
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$z$', fontsize=12)
    ax.set_title('問題2(2-3): 強誘電体球内外の電気力線・電束線の概略（$xz$ 平面）', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em2024_ferro_sphere_field.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em2024_ferro_sphere_field.png")


def fig_em2024_D_vs_eps0E():
    """2024 問題2(2-4): 強誘電体球内部での D と ε0 E の関係（概念図）"""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)

    # 自発分極のみの状態: E = -P/(3ε0), D = (2/3)P なので
    # 横軸 ε0 E = -P/3、縦軸 D = 2P/3。P=1 とすると点 (-1/3, 2/3)
    P = 1.0
    eps0E = -P / 3
    D_val = 2 * P / 3
    ax.plot(eps0E, D_val, 'ro', markersize=12, label=r'自発分極のみ（(2-3)の状態）')
    ax.annotate(r'$(-\frac{P}{3}, \frac{2P}{3})$', xy=(eps0E, D_val), xytext=(eps0E + 0.3, D_val + 0.1),
                fontsize=12, arrowprops=dict(arrowstyle='->', color='gray'))

    ax.set_xlabel(r'$\varepsilon_0 E$（横軸）', fontsize=12)
    ax.set_ylabel(r'$D$（縦軸）', fontsize=12)
    ax.set_title('問題2(2-4): 強誘電体球内部での $\\mathbf{D}$ と $\\varepsilon_0\\mathbf{E}$ の関係', fontsize=14)
    ax.legend(loc='upper left', fontsize=10)
    ax.set_xlim(-0.8, 0.5)
    ax.set_ylim(-0.2, 1.0)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em2024_D_vs_eps0E.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em2024_D_vs_eps0E.png")


# ========== 2024年度 問題3 ==========

def fig_em2024_chi_real():
    """2024 問題3(3-2): 電気感受率の実部 Re[χe(ω)]"""
    omega = np.linspace(0.01, 5, 200)
    tau = 1.0
    chi0 = 1.0
    chi_real = chi0 / (1 + (omega * tau)**2)
    omega0 = 1 / tau
    chi_at_omega0 = chi0 / 2

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(omega, chi_real, 'b-', linewidth=2, label=r'$\mathrm{Re}[\chi_e(\omega)] = \chi_0/(1+\omega^2\tau^2)$')
    ax.axvline(omega0, color='gray', linestyle='--', alpha=0.8, label=r'$\omega_0 = 1/\tau$')
    ax.plot(omega0, chi_at_omega0, 'ro', markersize=10)
    ax.text(omega0 + 0.15, chi_at_omega0, r'$\chi_0/2$', fontsize=12)
    ax.set_xlabel(r'$\omega$', fontsize=12)
    ax.set_ylabel(r'$\mathrm{Re}[\chi_e(\omega)]$', fontsize=12)
    ax.set_title('問題3(3-2): 電気感受率の実部（$\\omega_0 = 1/\\tau$ で $\\chi_0/2$）', fontsize=14)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, chi0 * 1.1)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em2024_chi_real.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em2024_chi_real.png")


def fig_em2024_eps_imag():
    """2024 問題3(3-3): 水の誘電率の虚部 ε'' の概略（ω0 と ω1 のピーク）"""
    omega = np.linspace(0.01, 3, 300)
    tau = 1.0
    omega0 = 1 / tau
    omega1 = 2.0  # 赤外共鳴の例
    chi0 = 1.0
    # 緩和型: Im(χ) ∝ ωτ/(1+ω^2τ^2)
    eps_imag_relax = chi0 * (omega * tau) / (1 + (omega * tau)**2)
    # 共鳴型（ローレンツ型）のピークを追加
    gamma1 = 0.2
    eps_imag_resonance = 0.5 * gamma1 * omega / ((omega1**2 - omega**2)**2 + (gamma1 * omega)**2)
    eps_imag_resonance = eps_imag_resonance / (eps_imag_resonance.max() + 1e-10) * 0.5
    eps_imag = eps_imag_relax + eps_imag_resonance

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(omega, eps_imag, 'b-', linewidth=2, label=r"$\varepsilon''$ の概略")
    ax.axvline(omega0, color='green', linestyle='--', alpha=0.8, label=r'$\omega_0$（緩和）')
    ax.axvline(omega1, color='red', linestyle='--', alpha=0.8, label=r'$\omega_1$（赤外共鳴）')
    ax.set_xlabel(r'$\omega$', fontsize=12)
    ax.set_ylabel(r"$\varepsilon''$", fontsize=12)
    ax.set_title("問題3(3-3): 水の誘電率の虚部（$\\omega_0$ で緩和型、$\\omega_1$ で共鳴型）", fontsize=14)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, None)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em2024_eps_imag.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em2024_eps_imag.png")


# ========== 2024再 問題4 ==========

def fig_em2024retake_sigma_omega():
    """2024再 問題4(4-3): 複素電気伝導率の実部 σ' と虚部 σ'' """
    omega = np.linspace(0.01, 4, 200)
    gamma = 1.0
    nq2m = 1.0  # nq^2/m を 1 に規格化
    sigma_prime = nq2m * gamma / (gamma**2 + omega**2)
    sigma_doubleprime = nq2m * omega / (gamma**2 + omega**2)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(omega, sigma_prime, 'b-', linewidth=2, label=r"$\sigma' = \mathrm{Re}[\sigma(\omega)]$")
    ax.plot(omega, sigma_doubleprime, 'r-', linewidth=2, label=r"$\sigma'' = \mathrm{Im}[\sigma(\omega)]$")
    ax.axvline(gamma, color='gray', linestyle='--', alpha=0.7, label=r'$\omega = \gamma$')
    ax.set_xlabel(r'$\omega$', fontsize=12)
    ax.set_ylabel(r"$\sigma', \sigma''$", fontsize=12)
    ax.set_title("問題4(4-3): 複素電気伝導率の実部・虚部の周波数依存性", fontsize=14)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 4)
    ax.set_ylim(0, None)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em2024retake_sigma_omega.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em2024retake_sigma_omega.png")


# ========== 物理的考察用の概念図 ==========

def fig_em_maxwell_concept():
    """問題1: Maxwell方程式の源の概念図（電場の源はρ+ρ_p、磁場の源はi+i_M）"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    ax.text(2, 5, r'電場 $\mathbf{E}$ の源', fontsize=14, fontweight='bold')
    ax.text(2, 4, r'真電荷 $\rho$ + 分極電荷 $\rho_p$', fontsize=12)
    ax.text(2, 3, r'$\nabla\cdot\mathbf{E} = (\rho+\rho_p)/\varepsilon_0$', fontsize=11)
    ax.text(6, 5, r'磁場 $\mathbf{B}$ の源', fontsize=14, fontweight='bold')
    ax.text(6, 4, r'真電流 $\mathbf{i}$ + 磁化電流 $\mathbf{i}_M$', fontsize=12)
    ax.text(6, 3, r'$\nabla\times\mathbf{B} = \mu_0(\mathbf{i}+\mathbf{i}_M)$', fontsize=11)
    ax.text(5, 1.5, '物質中では分極・磁化による「見かけの」電荷・電流が現れる', fontsize=11, ha='center')
    ax.set_title('問題1: 物質中のMaxwell方程式の物理的意味（電場・磁場の源）', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em_maxwell_concept.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em_maxwell_concept.png")


def fig_em_boundary_D_E():
    """問題2: 境界でのDの法線連続・Eの接線連続の原理図"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axhline(0, color='black', linewidth=2)
    ax.axhline(0, color='gray', linewidth=0.5, xmin=-2, xmax=0)
    ax.fill_between([-2, 2], 0, 2, facecolor='lightyellow', alpha=0.7)
    ax.fill_between([-2, 2], -2, 0, facecolor='lightblue', alpha=0.7)
    ax.text(1.2, 1.2, '真空', fontsize=12)
    ax.text(1.2, -1.2, '誘電体', fontsize=12)
    ax.annotate('', xy=(0.8, 0.3), xytext=(0.8, -0.3),
                arrowprops=dict(arrowstyle='<->', color='green', lw=2))
    ax.text(1.0, 0, r'$D_{\mathrm{n}}$ 連続', fontsize=11, color='green')
    ax.annotate('', xy=(-0.3, 0.8), xytext=(-0.3, -0.8),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax.text(-0.9, 0, r'$E_{\mathrm{t}}$ 連続', fontsize=11, color='red')
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$z$（法線）', fontsize=12)
    ax.set_title('問題2: 境界条件の原理（真電荷が表面にないとき $D_{\\mathrm{n}}$ 連続、$E_{\\mathrm{t}}$ 連続）', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em_boundary_D_E.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em_boundary_D_E.png")


def fig_em_depolarization_sphere():
    """問題2(2024): 2つの帯電球による分極の再現と脱分極電場"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    # 2つの球（+ρ と -ρ）
    c1 = Circle((0, 0.3), 0.4, facecolor='red', alpha=0.4, edgecolor='red', linewidth=2)
    c2 = Circle((0, -0.3), 0.4, facecolor='blue', alpha=0.4, edgecolor='blue', linewidth=2)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.text(0.6, 0.3, r'$+\rho$', fontsize=14, color='red')
    ax.text(0.6, -0.3, r'$-\rho$', fontsize=14, color='blue')
    ax.text(0, 0, r'$\mathbf{E}_p = -\mathbf{P}/(3\varepsilon_0)$', fontsize=12, ha='center')
    ax.annotate('', xy=(0, -0.5), xytext=(0, 0.5),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.text(0.3, 0, '脱分極電場', fontsize=10)
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$z$', fontsize=12)
    ax.set_title('問題2(2024): 一様分極の等価モデル（2つの帯電球）と脱分極電場の向き', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em_depolarization_sphere.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em_depolarization_sphere.png")


def fig_em_debye_relaxation():
    """問題3(2024): 分極の時間応答 P(t) と周波数応答 χ(ω) の物理"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    t = np.linspace(0, 4, 200)
    P = 1 - np.exp(-t)
    ax1.plot(t, P, 'b-', linewidth=2)
    ax1.axhline(1, color='gray', linestyle='--', alpha=0.7)
    ax1.axvline(1, color='gray', linestyle='--', alpha=0.7)
    ax1.set_xlabel(r'$t/\tau$', fontsize=12)
    ax1.set_ylabel(r'$P(t)/(\varepsilon_0\chi_0 E)$', fontsize=12)
    ax1.set_title('分極の時間応答（時定数 τ で飽和）', fontsize=12)
    ax1.grid(True, alpha=0.3)
    omega = np.linspace(0.01, 4, 200)
    chi_r = 1 / (1 + omega**2)
    ax2.plot(omega, chi_r, 'b-', linewidth=2)
    ax2.axvline(1, color='gray', linestyle='--', alpha=0.7)
    ax2.axhline(0.5, color='gray', linestyle='--', alpha=0.7)
    ax2.set_xlabel(r'$\omega\tau$', fontsize=12)
    ax2.set_ylabel(r'$\mathrm{Re}[\chi_e]/\chi_0$', fontsize=12)
    ax2.set_title(r'周波数応答（$\omega \sim 1/\tau$ で減衰）', fontsize=12)
    ax2.grid(True, alpha=0.3)
    plt.suptitle('問題3(2024): 誘電緩和の物理（遅い応答 → 高周波で感受率低下）', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em_debye_relaxation.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em_debye_relaxation.png")


def fig_em_drude_physics():
    """問題4(2024再): 電子の運動と伝導率の周波数依存の物理"""
    fig, ax = plt.subplots(figsize=(8, 5))
    omega = np.linspace(0.01, 3, 200)
    gamma = 1.0
    sig_r = gamma / (gamma**2 + omega**2)
    sig_i = omega / (gamma**2 + omega**2)
    ax.plot(omega, sig_r, 'b-', linewidth=2, label=r"$\sigma'$（実部：ジュール損失）")
    ax.plot(omega, sig_i, 'r-', linewidth=2, label=r"$\sigma''$（虚部：慣性）")
    ax.axvline(gamma, color='gray', linestyle='--', alpha=0.7)
    ax.set_xlabel(r'$\omega/\gamma$', fontsize=12)
    ax.set_ylabel(r"$\sigma', \sigma''$（規格化）", fontsize=12)
    ax.set_title("問題4: 高周波で $\\sigma'$ が減る理由（電子の慣性・位相遅れ）", fontsize=14)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'em_drude_physics.png'), dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"生成: {OUTPUT_DIR}/em_drude_physics.png")


def main():
    """すべての図を生成する"""
    print("電磁気学 過去問 図の生成を開始します...")
    fig_em_maxwell_concept()
    fig_em_boundary_D_E()
    fig_em_depolarization_sphere()
    fig_em_debye_relaxation()
    fig_em_drude_physics()
    fig_em2023_dielectric_vertical()
    fig_em2023_dielectric_tilted()
    fig_em2023_conductor_plate()
    fig_em2023_intensity_decay()
    fig_em2023_metal_reflection()
    fig_em2023_metal_slab()
    fig_em2024_ferro_sphere_field()
    fig_em2024_D_vs_eps0E()
    fig_em2024_chi_real()
    fig_em2024_eps_imag()
    fig_em2024retake_sigma_omega()
    print("すべての図の生成が完了しました。")


if __name__ == '__main__':
    main()
