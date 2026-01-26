"""
電磁気学演習問題 (2025年12月26日) の図示用スクリプト
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントの設定
rcParams['font.family'] = 'Hiragino Sans'
rcParams['axes.unicode_minus'] = False

# 図1: 問題1-1 誘電率の実部と虚部の周波数依存性
def plot_dielectric_dispersion():
    """誘電率の実部と虚部の周波数依存性をプロット"""
    # パラメータ設定
    chi_e0 = 1.0  # 静的電気感受率
    epsilon_0 = 1.0  # 真空の誘電率（規格化）
    tau = 1.0  # 緩和時間
    
    # 周波数範囲 (omega*tau)
    omega_tau = np.logspace(-2, 2, 1000)
    omega = omega_tau / tau
    
    # 実部と虚部の計算
    epsilon_prime = epsilon_0 * (1 + chi_e0 / (1 + omega_tau**2))
    epsilon_double_prime = epsilon_0 * chi_e0 * omega_tau / (1 + omega_tau**2)
    
    # プロット
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 左図: 線形スケール
    ax1.plot(omega_tau, epsilon_prime / epsilon_0, 'b-', linewidth=2, label=r'$\varepsilon\'(\omega)/\varepsilon_0$ (実部)')
    ax1.plot(omega_tau, epsilon_double_prime / epsilon_0, 'r-', linewidth=2, label=r'$\varepsilon\'\'(\omega)/\varepsilon_0$ (虚部)')
    ax1.axvline(x=1, color='gray', linestyle='--', alpha=0.5, label=r'$\omega\tau = 1$')
    ax1.set_xlabel(r'$\omega\tau$', fontsize=12)
    ax1.set_ylabel(r'$\varepsilon/\varepsilon_0$', fontsize=12)
    ax1.set_title('誘電率の周波数依存性 (線形スケール)', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 5)
    
    # 右図: 対数スケール
    ax2.loglog(omega_tau, epsilon_prime / epsilon_0, 'b-', linewidth=2, label=r'$\varepsilon\'(\omega)/\varepsilon_0$ (実部)')
    ax2.loglog(omega_tau, epsilon_double_prime / epsilon_0, 'r-', linewidth=2, label=r'$\varepsilon\'\'(\omega)/\varepsilon_0$ (虚部)')
    ax2.axvline(x=1, color='gray', linestyle='--', alpha=0.5, label=r'$\omega\tau = 1$')
    ax2.set_xlabel(r'$\omega\tau$', fontsize=12)
    ax2.set_ylabel(r'$\varepsilon/\varepsilon_0$', fontsize=12)
    ax2.set_title('誘電率の周波数依存性 (対数スケール)', fontsize=12)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig1_dielectric_dispersion.png', dpi=200, bbox_inches='tight')
    print("図1を保存しました: electromagnetism_exercise_20251226_fig1_dielectric_dispersion.png")
    plt.close()

# 図2: 問題1-2 エネルギー吸収率の周波数依存性
def plot_energy_absorption():
    """エネルギー吸収率の周波数依存性をプロット"""
    # パラメータ設定
    chi_e0 = 1.0
    epsilon_0 = 1.0
    tau = 1.0
    E0 = 1.0  # 規格化
    
    # 周波数範囲
    omega_tau = np.logspace(-2, 2, 1000)
    omega = omega_tau / tau
    
    # エネルギー吸収率の計算
    dw_dt = omega**2 * tau * epsilon_0 * chi_e0 * E0**2 / (2 * (1 + omega_tau**2))
    
    # 規格化（最大値で割る）
    dw_dt_normalized = dw_dt / np.max(dw_dt)
    
    # プロット
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.semilogx(omega_tau, dw_dt_normalized, 'b-', linewidth=2, label=r'$\langle dw/dt \rangle$ (規格化)')
    ax.axvline(x=1, color='r', linestyle='--', alpha=0.7, label=r'$\omega\tau = 1$ (最大吸収)')
    ax.set_xlabel(r'$\omega\tau$', fontsize=12)
    ax.set_ylabel(r'規格化されたエネルギー吸収率', fontsize=12)
    ax.set_title('エネルギー吸収率の周波数依存性', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xlim(1e-2, 1e2)
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig2_energy_absorption.png', dpi=200, bbox_inches='tight')
    print("図2を保存しました: electromagnetism_exercise_20251226_fig2_energy_absorption.png")
    plt.close()

# 図3: 問題3-1 吸収断面積の周波数依存性
def plot_absorption_cross_section():
    """吸収断面積の周波数依存性をプロット"""
    # パラメータ設定
    V = 1.0  # 体積（規格化）
    epsilon_0 = 1.0
    epsilon_prime = 2.0 * epsilon_0  # 誘電率の実部
    c = 1.0  # 光速（規格化）
    
    # 虚部の周波数依存性（デバイ緩和モデル）
    chi_e0 = 0.5
    tau = 1.0
    omega_tau = np.logspace(-1, 2, 1000)
    omega = omega_tau / tau
    
    epsilon_double_prime = epsilon_0 * chi_e0 * omega_tau / (1 + omega_tau**2)
    
    # 吸収断面積の計算
    denominator = (2 * epsilon_0 + epsilon_prime)**2 + epsilon_double_prime**2
    C_a = 9 * V * omega * epsilon_0 * epsilon_double_prime / (c * denominator)
    
    # 規格化
    C_a_normalized = C_a / np.max(C_a)
    
    # プロット
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.semilogx(omega_tau, C_a_normalized, 'b-', linewidth=2, label=r'$C_a$ (規格化)')
    ax.axvline(x=1, color='r', linestyle='--', alpha=0.7, label=r'$\omega\tau = 1$')
    ax.set_xlabel(r'$\omega\tau$', fontsize=12)
    ax.set_ylabel(r'規格化された吸収断面積', fontsize=12)
    ax.set_title('吸収断面積の周波数依存性', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xlim(1e-1, 1e2)
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig3_absorption_cross_section.png', dpi=200, bbox_inches='tight')
    print("図3を保存しました: electromagnetism_exercise_20251226_fig3_absorption_cross_section.png")
    plt.close()

# 図4: 問題3-2 散乱断面積の周波数依存性
def plot_scattering_cross_section():
    """散乱断面積の周波数依存性をプロット"""
    # パラメータ設定
    V = 1.0  # 体積（規格化）
    epsilon_0 = 1.0
    epsilon = 2.0 * epsilon_0  # 誘電率（実数と仮定）
    c = 1.0  # 光速（規格化）
    
    # 周波数範囲
    omega = np.logspace(0, 3, 1000)
    
    # 散乱断面積の計算
    epsilon_diff = epsilon - epsilon_0
    denominator = 2 * epsilon_0 + epsilon
    C_s = omega**4 * V**2 / (6 * np.pi * c**4) * (3 * epsilon_diff / denominator)**2
    
    # 規格化（対数スケール用）
    C_s_normalized = C_s / C_s[0]  # 最初の値で割る
    
    # プロット
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.loglog(omega, C_s_normalized, 'b-', linewidth=2, label=r'$C_s \propto \omega^4$')
    ax.set_xlabel(r'$\omega$ [rad/s]', fontsize=12)
    ax.set_ylabel(r'規格化された散乱断面積', fontsize=12)
    ax.set_title('散乱断面積の周波数依存性 (レイリー散乱)', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, which='both')
    
    # ω^4の傾きを示す参考線
    omega_ref = np.logspace(0, 3, 100)
    C_s_ref = omega_ref**4 / omega_ref[0]**4
    ax.loglog(omega_ref, C_s_ref, 'r--', alpha=0.5, linewidth=1, label=r'$\omega^4$ の傾き')
    ax.legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig4_scattering_cross_section.png', dpi=200, bbox_inches='tight')
    print("図4を保存しました: electromagnetism_exercise_20251226_fig4_scattering_cross_section.png")
    plt.close()

# 図5: 問題4-1, 4-3 反射率の図示
def plot_reflectance():
    """反射率の図示"""
    # パラメータ設定
    mu_0 = 1.0
    epsilon_0 = 1.0
    
    # ケース1: mu = mu_0 の場合（通常の誘電体）
    mu_1 = mu_0
    epsilon_ratio_1 = np.logspace(-1, 1, 1000)  # epsilon/epsilon_0
    epsilon_1 = epsilon_ratio_1 * epsilon_0
    
    # 反射率の計算
    sqrt_mu_epsilon_0 = np.sqrt(mu_1 * epsilon_0)
    sqrt_mu_0_epsilon = np.sqrt(mu_0 * epsilon_1)
    R_1 = ((sqrt_mu_epsilon_0 - sqrt_mu_0_epsilon) / (sqrt_mu_epsilon_0 + sqrt_mu_0_epsilon))**2
    
    # ケース2: 屈折率 n = sqrt(epsilon/epsilon_0) の場合
    n = np.linspace(0.5, 3.0, 1000)
    R_n = ((1 - n) / (1 + n))**2
    
    # プロット
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 左図: 誘電率比に対する反射率
    ax1.semilogx(epsilon_ratio_1, R_1, 'b-', linewidth=2, label=r'$\mu = \mu_0$')
    ax1.axvline(x=1, color='gray', linestyle='--', alpha=0.5, label=r'$\varepsilon = \varepsilon_0$')
    ax1.set_xlabel(r'$\varepsilon/\varepsilon_0$', fontsize=12)
    ax1.set_ylabel(r'反射率 $R$', fontsize=12)
    ax1.set_title('反射率の誘電率依存性 ($\mu = \mu_0$)', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3, which='both')
    ax1.set_ylim(0, 1)
    
    # ガラス (n=1.5) の位置を示す
    n_glass = 1.5
    epsilon_glass = n_glass**2 * epsilon_0
    R_glass = ((1 - n_glass) / (1 + n_glass))**2
    ax1.axvline(x=epsilon_glass/epsilon_0, color='r', linestyle='--', alpha=0.7, label=f'ガラス (n={n_glass})')
    ax1.plot(epsilon_glass/epsilon_0, R_glass, 'ro', markersize=8)
    ax1.legend(fontsize=10)
    
    # 右図: 屈折率に対する反射率
    ax2.plot(n, R_n, 'b-', linewidth=2, label=r'$R = \left(\frac{1-n}{1+n}\right)^2$')
    ax2.axvline(x=1, color='gray', linestyle='--', alpha=0.5, label=r'$n = 1$ (真空)')
    ax2.axvline(x=1.5, color='r', linestyle='--', alpha=0.7, label='ガラス (n=1.5)')
    ax2.plot(1.5, ((1-1.5)/(1+1.5))**2, 'ro', markersize=8)
    ax2.set_xlabel(r'屈折率 $n$', fontsize=12)
    ax2.set_ylabel(r'反射率 $R$', fontsize=12)
    ax2.set_title('反射率の屈折率依存性', fontsize=12)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0.5, 3.0)
    ax2.set_ylim(0, 1)
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig5_reflectance.png', dpi=200, bbox_inches='tight')
    print("図5を保存しました: electromagnetism_exercise_20251226_fig5_reflectance.png")
    plt.close()

# 図6: 問題4 電磁波の入射・反射・透過の模式図
def plot_wave_reflection_diagram():
    """電磁波の入射・反射・透過の模式図"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 界面の位置
    interface_x = 0
    
    # 電場と磁場の矢印を描画
    # 入射波（左側、z < 0）
    z_inc = np.linspace(-3, -0.5, 20)
    # 電場（x方向）
    for z in z_inc[::4]:
        ax.arrow(z, 0, 0, 0.3, head_width=0.1, head_length=0.05, fc='blue', ec='blue', alpha=0.6)
    # 磁場（y方向、画面奥方向）
    for z in z_inc[::4]:
        ax.plot([z], [0], 'bo', markersize=8, alpha=0.6)
    
    # 反射波（左側、z < 0）
    z_ref = np.linspace(-0.5, -3, 20)
    # 電場（x方向、反転）
    for z in z_ref[::4]:
        ax.arrow(z, 0, 0, -0.3, head_width=0.1, head_length=0.05, fc='red', ec='red', alpha=0.6)
    # 磁場（y方向、画面手前方向）
    for z in z_ref[::4]:
        ax.plot([z], [0], 'ro', markersize=8, alpha=0.6)
    
    # 透過波（右側、z > 0）
    z_trans = np.linspace(0.5, 3, 20)
    # 電場（x方向）
    for z in z_trans[::4]:
        ax.arrow(z, 0, 0, 0.25, head_width=0.1, head_length=0.05, fc='green', ec='green', alpha=0.6)
    # 磁場（y方向、画面奥方向）
    for z in z_trans[::4]:
        ax.plot([z], [0], 'go', markersize=8, alpha=0.6)
    
    # 界面の線
    ax.axvline(x=interface_x, color='black', linewidth=2, linestyle='--', label='界面 (z=0)')
    
    # 領域のラベル
    ax.text(-1.5, 0.5, '真空中\n(z < 0)', fontsize=12, ha='center', 
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    ax.text(1.5, 0.5, '物質中\n(z > 0)', fontsize=12, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
    
    # 進行方向の矢印
    ax.arrow(-2.5, -0.6, 1.5, 0, head_width=0.1, head_length=0.15, fc='blue', ec='blue', linewidth=2)
    ax.text(-1.5, -0.8, '入射波', fontsize=10, ha='center', color='blue')
    
    ax.arrow(-1.5, -0.6, -1.5, 0, head_width=0.1, head_length=0.15, fc='red', ec='red', linewidth=2)
    ax.text(-2.5, -0.8, '反射波', fontsize=10, ha='center', color='red')
    
    ax.arrow(0.5, -0.6, 1.5, 0, head_width=0.1, head_length=0.15, fc='green', ec='green', linewidth=2)
    ax.text(1.5, -0.8, '透過波', fontsize=10, ha='center', color='green')
    
    # 凡例
    from matplotlib.patches import FancyArrowPatch
    ax.plot([], [], 'b-', linewidth=2, label='電場 E (入射・透過)')
    ax.plot([], [], 'r-', linewidth=2, label='電場 E (反射)')
    ax.plot([], [], 'bo', markersize=8, label='磁場 H (画面奥)')
    ax.plot([], [], 'ro', markersize=8, label='磁場 H (画面手前)')
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1.2, 0.8)
    ax.set_xlabel('z方向', fontsize=12)
    ax.set_ylabel('x方向（電場方向）', fontsize=12)
    ax.set_title('電磁波の入射・反射・透過の模式図', fontsize=12)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig6_wave_reflection_diagram.png', dpi=200, bbox_inches='tight')
    print("図6を保存しました: electromagnetism_exercise_20251226_fig6_wave_reflection_diagram.png")
    plt.close()

# 図7: 問題4-2 位相変化の条件の可視化
def plot_phase_condition():
    """位相がπだけ変化する条件の可視化"""
    # パラメータ範囲
    epsilon_ratio = np.logspace(-1, 1, 200)  # ε/ε₀
    mu_ratio = np.logspace(-1, 1, 200)  # μ/μ₀
    
    Epsilon, Mu = np.meshgrid(epsilon_ratio, mu_ratio)
    
    # 反射係数の符号を計算
    sqrt_mu_epsilon_0 = np.sqrt(Mu * 1.0)  # μ/μ₀ * ε₀/ε₀ = μ/μ₀
    sqrt_mu_0_epsilon = np.sqrt(1.0 * Epsilon)  # μ₀/μ₀ * ε/ε₀ = ε/ε₀
    
    # 反射係数 r = (sqrt(με₀) - sqrt(μ₀ε)) / (sqrt(με₀) + sqrt(μ₀ε))
    numerator = sqrt_mu_epsilon_0 - sqrt_mu_0_epsilon
    denominator = sqrt_mu_epsilon_0 + sqrt_mu_0_epsilon
    r = numerator / denominator
    
    # 位相がπ変化する条件: r < 0, すなわち ε/ε₀ > μ/μ₀
    phase_condition = Epsilon > Mu
    
    # プロット
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 反射係数の符号
    im1 = ax1.contourf(Epsilon, Mu, np.sign(r), levels=[-1, 0, 1], cmap='RdYlBu', alpha=0.6)
    ax1.contour(Epsilon, Mu, r, levels=[0], colors='black', linewidths=2)
    ax1.plot(epsilon_ratio, epsilon_ratio, 'k--', linewidth=2, label=r'$\varepsilon/\varepsilon_0 = \mu/\mu_0$')
    ax1.fill_between(epsilon_ratio, 0, epsilon_ratio, alpha=0.3, color='red', label='位相がπ変化 (r < 0)')
    ax1.fill_between(epsilon_ratio, epsilon_ratio, 10, alpha=0.3, color='blue', label='位相変化なし (r > 0)')
    ax1.set_xlabel(r'$\varepsilon/\varepsilon_0$', fontsize=12)
    ax1.set_ylabel(r'$\mu/\mu_0$', fontsize=12)
    ax1.set_title('反射係数の符号と位相変化の条件', fontsize=12)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3, which='both')
    ax1.set_xlim(0.1, 10)
    ax1.set_ylim(0.1, 10)
    
    # 右図: 反射率の等高線
    R = ((sqrt_mu_epsilon_0 - sqrt_mu_0_epsilon) / (sqrt_mu_epsilon_0 + sqrt_mu_0_epsilon))**2
    im2 = ax2.contourf(Epsilon, Mu, R, levels=20, cmap='viridis', alpha=0.8)
    ax2.contour(Epsilon, Mu, R, levels=[0.1, 0.25, 0.5, 0.75, 0.9], colors='white', linewidths=1)
    ax2.plot(epsilon_ratio, epsilon_ratio, 'r--', linewidth=2, label=r'$\varepsilon/\varepsilon_0 = \mu/\mu_0$ (R=0)')
    cbar = plt.colorbar(im2, ax=ax2)
    cbar.set_label('反射率 R', fontsize=10)
    ax2.set_xlabel(r'$\varepsilon/\varepsilon_0$', fontsize=12)
    ax2.set_ylabel(r'$\mu/\mu_0$', fontsize=12)
    ax2.set_title('反射率の等高線図', fontsize=12)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3, which='both')
    ax2.set_xlim(0.1, 10)
    ax2.set_ylim(0.1, 10)
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig7_phase_condition.png', dpi=200, bbox_inches='tight')
    print("図7を保存しました: electromagnetism_exercise_20251226_fig7_phase_condition.png")
    plt.close()

# 図8: 問題4-4 負の誘電率の場合の挙動
def plot_negative_epsilon():
    """負の誘電率の場合の反射率と透過率"""
    # パラメータ設定
    epsilon_0 = 1.0
    mu_0 = 1.0
    mu = mu_0
    
    # 誘電率の範囲（負の値も含む）
    epsilon_ratio = np.linspace(-5, 5, 1000)  # ε/ε₀
    epsilon = epsilon_ratio * epsilon_0
    
    # 反射率の計算
    sqrt_mu_epsilon_0 = np.sqrt(mu * epsilon_0)
    sqrt_mu_0 = np.sqrt(mu_0)
    
    # 複素数の場合を考慮
    R = np.zeros_like(epsilon_ratio)
    for i, eps in enumerate(epsilon):
        if eps >= 0:
            # 正の誘電率
            sqrt_eps = np.sqrt(eps)
            sqrt_mu_0_epsilon = sqrt_mu_0 * sqrt_eps
            r = (sqrt_mu_epsilon_0 - sqrt_mu_0_epsilon) / (sqrt_mu_epsilon_0 + sqrt_mu_0_epsilon)
            R[i] = abs(r)**2
        else:
            # 負の誘電率
            sqrt_eps_abs = np.sqrt(abs(eps))
            sqrt_mu_0_epsilon = 1j * sqrt_mu_0 * sqrt_eps_abs
            r = (sqrt_mu_epsilon_0 - sqrt_mu_0_epsilon) / (sqrt_mu_epsilon_0 + sqrt_mu_0_epsilon)
            R[i] = abs(r)**2
    
    # 透過率 T = 1 - R（エネルギー保存）
    T = 1 - R
    
    # プロット
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 左図: 反射率と透過率
    ax1.plot(epsilon_ratio, R, 'b-', linewidth=2, label='反射率 R')
    ax1.plot(epsilon_ratio, T, 'r-', linewidth=2, label='透過率 T')
    ax1.axvline(x=0, color='gray', linestyle='--', alpha=0.5, label=r'$\varepsilon = 0$')
    ax1.axvline(x=1, color='green', linestyle='--', alpha=0.5, label=r'$\varepsilon = \varepsilon_0$')
    ax1.axhline(y=1, color='black', linestyle=':', alpha=0.5)
    ax1.set_xlabel(r'$\varepsilon/\varepsilon_0$', fontsize=12)
    ax1.set_ylabel('反射率・透過率', fontsize=12)
    ax1.set_title('負の誘電率の場合の反射率と透過率', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(0, 1.1)
    ax1.fill_between([-5, 0], 0, 1.1, alpha=0.2, color='red', label='負の誘電率領域')
    
    # 右図: 対数スケール（正の値のみ）
    epsilon_ratio_pos = np.logspace(-2, 1, 1000)
    epsilon_pos = epsilon_ratio_pos * epsilon_0
    sqrt_mu_epsilon_0 = np.sqrt(mu * epsilon_0)
    sqrt_mu_0_epsilon_pos = np.sqrt(mu_0 * epsilon_pos)
    R_pos = ((sqrt_mu_epsilon_0 - sqrt_mu_0_epsilon_pos) / (sqrt_mu_epsilon_0 + sqrt_mu_0_epsilon_pos))**2
    T_pos = 1 - R_pos
    
    ax2.loglog(epsilon_ratio_pos, R_pos, 'b-', linewidth=2, label='反射率 R')
    ax2.loglog(epsilon_ratio_pos, T_pos, 'r-', linewidth=2, label='透過率 T')
    ax2.axvline(x=1, color='green', linestyle='--', alpha=0.5, label=r'$\varepsilon = \varepsilon_0$')
    ax2.set_xlabel(r'$\varepsilon/\varepsilon_0$', fontsize=12)
    ax2.set_ylabel('反射率・透過率', fontsize=12)
    ax2.set_title('反射率と透過率（対数スケール、正の誘電率）', fontsize=12)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, which='both')
    ax2.set_xlim(1e-2, 10)
    ax2.set_ylim(1e-4, 1)
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig8_negative_epsilon.png', dpi=200, bbox_inches='tight')
    print("図8を保存しました: electromagnetism_exercise_20251226_fig8_negative_epsilon.png")
    plt.close()

# 図9: 問題4 透過率の詳細
def plot_transmittance():
    """透過率の詳細な図示"""
    # パラメータ設定
    epsilon_0 = 1.0
    mu_0 = 1.0
    
    # ケース1: mu = mu_0 の場合
    mu_1 = mu_0
    epsilon_ratio_1 = np.logspace(-1, 1, 1000)
    epsilon_1 = epsilon_ratio_1 * epsilon_0
    
    sqrt_mu_epsilon_0 = np.sqrt(mu_1 * epsilon_0)
    sqrt_mu_0_epsilon = np.sqrt(mu_0 * epsilon_1)
    R_1 = ((sqrt_mu_epsilon_0 - sqrt_mu_0_epsilon) / (sqrt_mu_epsilon_0 + sqrt_mu_0_epsilon))**2
    T_1 = 1 - R_1  # 透過率
    
    # ケース2: 屈折率 n
    n = np.linspace(0.5, 3.0, 1000)
    R_n = ((1 - n) / (1 + n))**2
    T_n = 1 - R_n
    
    # プロット
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 左図: 誘電率比に対する透過率
    ax1.semilogx(epsilon_ratio_1, T_1, 'b-', linewidth=2, label='透過率 T')
    ax1.semilogx(epsilon_ratio_1, R_1, 'r--', linewidth=2, label='反射率 R')
    ax1.axvline(x=1, color='gray', linestyle='--', alpha=0.5, label=r'$\varepsilon = \varepsilon_0$')
    ax1.axhline(y=1, color='black', linestyle=':', alpha=0.3)
    ax1.set_xlabel(r'$\varepsilon/\varepsilon_0$', fontsize=12)
    ax1.set_ylabel('透過率・反射率', fontsize=12)
    ax1.set_title('透過率と反射率の誘電率依存性 ($\mu = \mu_0$)', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3, which='both')
    ax1.set_ylim(0, 1.1)
    
    # ガラスの位置
    n_glass = 1.5
    epsilon_glass = n_glass**2 * epsilon_0
    T_glass = 1 - ((1 - n_glass) / (1 + n_glass))**2
    ax1.axvline(x=epsilon_glass/epsilon_0, color='green', linestyle='--', alpha=0.7)
    ax1.plot(epsilon_glass/epsilon_0, T_glass, 'go', markersize=8, label=f'ガラス (n={n_glass}, T={T_glass:.3f})')
    ax1.legend(fontsize=10)
    
    # 右図: 屈折率に対する透過率
    ax2.plot(n, T_n, 'b-', linewidth=2, label='透過率 T')
    ax2.plot(n, R_n, 'r--', linewidth=2, label='反射率 R')
    ax2.axvline(x=1, color='gray', linestyle='--', alpha=0.5, label=r'$n = 1$ (真空)')
    ax2.axvline(x=1.5, color='green', linestyle='--', alpha=0.7, label='ガラス (n=1.5)')
    ax2.plot(1.5, T_n[np.argmin(np.abs(n - 1.5))], 'go', markersize=8)
    ax2.set_xlabel(r'屈折率 $n$', fontsize=12)
    ax2.set_ylabel('透過率・反射率', fontsize=12)
    ax2.set_title('透過率と反射率の屈折率依存性', fontsize=12)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0.5, 3.0)
    ax2.set_ylim(0, 1.1)
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig9_transmittance.png', dpi=200, bbox_inches='tight')
    print("図9を保存しました: electromagnetism_exercise_20251226_fig9_transmittance.png")
    plt.close()

# 図10: 問題4-2 位相変化の時間変化の可視化
def plot_phase_change_time_evolution():
    """位相変化の時間変化の可視化"""
    # パラメータ設定
    omega = 1.0
    E_i0 = 1.0  # 入射波の振幅
    
    # ケース1: 位相がπ変化する場合（r < 0）
    # 例: ガラス（n=1.5, mu=mu_0）
    n1 = 1.5
    r1 = (1 - n1) / (1 + n1)  # r < 0
    E_r0_1 = r1 * E_i0
    
    # ケース2: 位相変化なしの場合（r > 0）
    # 例: 磁性体（mu/mu_0 = 2, epsilon/epsilon_0 = 1）
    mu_ratio = 2.0
    epsilon_ratio = 1.0
    sqrt_mu_epsilon_0 = np.sqrt(mu_ratio * 1.0)
    sqrt_mu_0_epsilon = np.sqrt(1.0 * epsilon_ratio)
    r2 = (sqrt_mu_epsilon_0 - sqrt_mu_0_epsilon) / (sqrt_mu_epsilon_0 + sqrt_mu_0_epsilon)  # r > 0
    E_r0_2 = r2 * E_i0
    
    # 時間範囲
    t = np.linspace(0, 4 * np.pi / omega, 1000)
    z = 0  # 界面での観測
    
    # 電場の計算
    # 入射波
    E_i = E_i0 * np.exp(1j * (omega * z - omega * t))
    
    # ケース1: 位相がπ変化
    E_r_1 = E_r0_1 * np.exp(1j * (-omega * z - omega * t))
    E_total_1 = E_i + E_r_1
    
    # ケース2: 位相変化なし
    E_r_2 = E_r0_2 * np.exp(1j * (-omega * z - omega * t))
    E_total_2 = E_i + E_r_2
    
    # 実部を取る
    E_i_real = np.real(E_i)
    E_r_1_real = np.real(E_r_1)
    E_total_1_real = np.real(E_total_1)
    E_r_2_real = np.real(E_r_2)
    E_total_2_real = np.real(E_total_2)
    
    # プロット
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 左上: ケース1 - 入射波と反射波
    ax1.plot(t, E_i_real, 'b-', linewidth=2, label=f'入射波 (E_i, r={r1:.3f})')
    ax1.plot(t, E_r_1_real, 'r-', linewidth=2, label=f'反射波 (E_r, 位相π変化)')
    ax1.plot(t, E_total_1_real, 'g-', linewidth=2, label='合成波 (E_i + E_r)')
    ax1.axhline(y=0, color='black', linestyle='--', alpha=0.3)
    ax1.set_xlabel('時間 $t$', fontsize=12)
    ax1.set_ylabel('電場 $E$', fontsize=12)
    ax1.set_title('位相がπ変化する場合 (ガラス, $r < 0$)', fontsize=12)
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 4 * np.pi / omega)
    
    # 右上: ケース2 - 入射波と反射波
    ax2.plot(t, E_i_real, 'b-', linewidth=2, label=f'入射波 (E_i, r={r2:.3f})')
    ax2.plot(t, E_r_2_real, 'r-', linewidth=2, label=f'反射波 (E_r, 位相変化なし)')
    ax2.plot(t, E_total_2_real, 'g-', linewidth=2, label='合成波 (E_i + E_r)')
    ax2.axhline(y=0, color='black', linestyle='--', alpha=0.3)
    ax2.set_xlabel('時間 $t$', fontsize=12)
    ax2.set_ylabel('電場 $E$', fontsize=12)
    ax2.set_title('位相変化なしの場合 (磁性体, $r > 0$)', fontsize=12)
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 4 * np.pi / omega)
    
    # 左下: ケース1 - 位相の関係
    phase_i = np.angle(E_i)
    phase_r_1 = np.angle(E_r_1)
    phase_diff_1 = phase_r_1 - phase_i
    
    # 位相を[-π, π]の範囲に正規化
    phase_diff_1 = np.angle(np.exp(1j * phase_diff_1))
    
    ax3.plot(t, phase_i, 'b-', linewidth=2, label='入射波の位相')
    ax3.plot(t, phase_r_1, 'r-', linewidth=2, label='反射波の位相')
    ax3.axhline(y=np.pi, color='gray', linestyle='--', alpha=0.5, label=r'$\pi$')
    ax3.axhline(y=-np.pi, color='gray', linestyle='--', alpha=0.5, label=r'$-\pi$')
    ax3.set_xlabel('時間 $t$', fontsize=12)
    ax3.set_ylabel('位相 [rad]', fontsize=12)
    ax3.set_title('位相がπ変化する場合の位相関係', fontsize=12)
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(0, 4 * np.pi / omega)
    ax3.set_ylim(-np.pi - 0.5, np.pi + 0.5)
    
    # 右下: ケース2 - 位相の関係
    phase_r_2 = np.angle(E_r_2)
    phase_diff_2 = phase_r_2 - phase_i
    phase_diff_2 = np.angle(np.exp(1j * phase_diff_2))
    
    ax4.plot(t, phase_i, 'b-', linewidth=2, label='入射波の位相')
    ax4.plot(t, phase_r_2, 'r-', linewidth=2, label='反射波の位相')
    ax4.axhline(y=0, color='gray', linestyle='--', alpha=0.5, label='0')
    ax4.set_xlabel('時間 $t$', fontsize=12)
    ax4.set_ylabel('位相 [rad]', fontsize=12)
    ax4.set_title('位相変化なしの場合の位相関係', fontsize=12)
    ax4.legend(fontsize=9)
    ax4.grid(True, alpha=0.3)
    ax4.set_xlim(0, 4 * np.pi / omega)
    ax4.set_ylim(-np.pi - 0.5, np.pi + 0.5)
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig10_phase_change_time.png', dpi=200, bbox_inches='tight')
    print("図10を保存しました: electromagnetism_exercise_20251226_fig10_phase_change_time.png")
    plt.close()

# 図11: 問題4-2 反射係数と位相の関係
def plot_reflection_coefficient_phase():
    """反射係数と位相の関係"""
    # パラメータ設定
    mu_0 = 1.0
    epsilon_0 = 1.0
    
    # ケース1: mu = mu_0 の場合
    mu_1 = mu_0
    epsilon_ratio_1 = np.logspace(-1, 1, 1000)
    epsilon_1 = epsilon_ratio_1 * epsilon_0
    
    sqrt_mu_epsilon_0 = np.sqrt(mu_1 * epsilon_0)
    sqrt_mu_0_epsilon = np.sqrt(mu_0 * epsilon_1)
    r_1 = (sqrt_mu_epsilon_0 - sqrt_mu_0_epsilon) / (sqrt_mu_epsilon_0 + sqrt_mu_0_epsilon)
    
    # 反射係数の位相
    phase_1 = np.angle(r_1)
    
    # プロット
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 左図: 反射係数の実部と虚部
    ax1.semilogx(epsilon_ratio_1, np.real(r_1), 'b-', linewidth=2, label='反射係数の実部 Re(r)')
    ax1.semilogx(epsilon_ratio_1, np.imag(r_1), 'r--', linewidth=2, label='反射係数の虚部 Im(r)')
    ax1.axhline(y=0, color='black', linestyle='--', alpha=0.3)
    ax1.axvline(x=1, color='gray', linestyle='--', alpha=0.5, label=r'$\varepsilon = \varepsilon_0$')
    ax1.set_xlabel(r'$\varepsilon/\varepsilon_0$', fontsize=12)
    ax1.set_ylabel('反射係数 $r$', fontsize=12)
    ax1.set_title('反射係数の実部と虚部 ($\mu = \mu_0$)', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3, which='both')
    ax1.set_ylim(-1.1, 1.1)
    
    # 右図: 反射係数の位相
    ax2.semilogx(epsilon_ratio_1, phase_1, 'b-', linewidth=2, label='反射係数の位相')
    ax2.axhline(y=0, color='gray', linestyle='--', alpha=0.5, label='位相 = 0')
    ax2.axhline(y=-np.pi, color='red', linestyle='--', alpha=0.5, label=r'位相 = $-\pi$')
    ax2.axvline(x=1, color='gray', linestyle='--', alpha=0.5, label=r'$\varepsilon = \varepsilon_0$')
    ax2.set_xlabel(r'$\varepsilon/\varepsilon_0$', fontsize=12)
    ax2.set_ylabel('位相 [rad]', fontsize=12)
    ax2.set_title('反射係数の位相 ($\mu = \mu_0$)', fontsize=12)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, which='both')
    ax2.set_ylim(-np.pi - 0.2, 0.2)
    
    # ガラスの位置
    n_glass = 1.5
    epsilon_glass = n_glass**2 * epsilon_0
    r_glass = (1 - n_glass) / (1 + n_glass)
    phase_glass = np.angle(r_glass)
    ax1.axvline(x=epsilon_glass/epsilon_0, color='green', linestyle='--', alpha=0.7)
    ax1.plot(epsilon_glass/epsilon_0, r_glass, 'go', markersize=8, label=f'ガラス (n={n_glass})')
    ax2.axvline(x=epsilon_glass/epsilon_0, color='green', linestyle='--', alpha=0.7)
    ax2.plot(epsilon_glass/epsilon_0, phase_glass, 'go', markersize=8, label=f'ガラス (n={n_glass})')
    ax1.legend(fontsize=9)
    ax2.legend(fontsize=9)
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig11_reflection_coefficient_phase.png', dpi=200, bbox_inches='tight')
    print("図11を保存しました: electromagnetism_exercise_20251226_fig11_reflection_coefficient_phase.png")
    plt.close()

# 図12: 問題4-4 プラズマの誘電率の周波数依存性
def plot_plasma_permittivity():
    """プラズマの誘電率の周波数依存性"""
    # パラメータ設定
    omega_p = 1.0  # プラズマ周波数（規格化）
    epsilon_0 = 1.0
    
    # 周波数範囲
    omega_ratio = np.logspace(-1, 1, 1000)  # ω/ω_p
    omega = omega_ratio * omega_p
    
    # プラズマの誘電率（ドルーデモデル）
    epsilon_plasma = epsilon_0 * (1 - omega_p**2 / omega**2)
    epsilon_ratio_plasma = epsilon_plasma / epsilon_0
    
    # 反射率の計算
    mu_0 = 1.0
    mu = mu_0
    sqrt_mu_epsilon_0 = np.sqrt(mu * epsilon_0)
    
    R_plasma = np.zeros_like(omega_ratio)
    for i, eps in enumerate(epsilon_plasma):
        if eps >= 0:
            sqrt_mu_0_epsilon = np.sqrt(mu_0 * eps)
            r = (sqrt_mu_epsilon_0 - sqrt_mu_0_epsilon) / (sqrt_mu_epsilon_0 + sqrt_mu_0_epsilon)
            R_plasma[i] = abs(r)**2
        else:
            sqrt_eps_abs = np.sqrt(abs(eps))
            sqrt_mu_0_epsilon = 1j * np.sqrt(mu_0) * sqrt_eps_abs
            r = (sqrt_mu_epsilon_0 - sqrt_mu_0_epsilon) / (sqrt_mu_epsilon_0 + sqrt_mu_0_epsilon)
            R_plasma[i] = abs(r)**2
    
    # プロット
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 左上: 誘電率の周波数依存性
    ax1.plot(omega_ratio, epsilon_ratio_plasma, 'b-', linewidth=2, label=r'$\varepsilon(\omega)/\varepsilon_0$')
    ax1.axhline(y=0, color='black', linestyle='--', alpha=0.5, label=r'$\varepsilon = 0$')
    ax1.axvline(x=1, color='red', linestyle='--', alpha=0.7, label=r'$\omega = \omega_p$')
    ax1.set_xlabel(r'$\omega/\omega_p$', fontsize=12)
    ax1.set_ylabel(r'$\varepsilon(\omega)/\varepsilon_0$', fontsize=12)
    ax1.set_title('プラズマの誘電率の周波数依存性', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3, which='both')
    ax1.set_xscale('log')
    ax1.fill_between(omega_ratio, -10, 0, alpha=0.2, color='red', label='負の誘電率領域')
    ax1.set_ylim(-5, 2)
    
    # 右上: 反射率の周波数依存性
    ax2.semilogx(omega_ratio, R_plasma, 'b-', linewidth=2, label='反射率 R')
    ax2.axvline(x=1, color='red', linestyle='--', alpha=0.7, label=r'$\omega = \omega_p$')
    ax2.axhline(y=1, color='black', linestyle=':', alpha=0.5, label='完全反射')
    ax2.set_xlabel(r'$\omega/\omega_p$', fontsize=12)
    ax2.set_ylabel('反射率 $R$', fontsize=12)
    ax2.set_title('プラズマの反射率の周波数依存性', fontsize=12)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, which='both')
    ax2.set_ylim(0, 1.1)
    
    # 左下: 波数の実部と虚部
    k_real = np.zeros_like(omega_ratio)
    k_imag = np.zeros_like(omega_ratio)
    for i, eps in enumerate(epsilon_plasma):
        if eps >= 0:
            k = omega[i] * np.sqrt(eps * mu)
            k_real[i] = np.real(k)
            k_imag[i] = np.imag(k)
        else:
            k = 1j * omega[i] * np.sqrt(abs(eps) * mu)
            k_real[i] = 0
            k_imag[i] = np.imag(k)
    
    ax3.semilogx(omega_ratio, k_real, 'b-', linewidth=2, label='波数の実部 Re(k)')
    ax3.semilogx(omega_ratio, k_imag, 'r--', linewidth=2, label='波数の虚部 Im(k)')
    ax3.axvline(x=1, color='red', linestyle='--', alpha=0.7, label=r'$\omega = \omega_p$')
    ax3.set_xlabel(r'$\omega/\omega_p$', fontsize=12)
    ax3.set_ylabel('波数 $k$', fontsize=12)
    ax3.set_title('プラズマ中の波数の実部と虚部', fontsize=12)
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3, which='both')
    
    # 右下: 侵入深さ（スキン深さ）
    delta = np.zeros_like(omega_ratio)
    for i, eps in enumerate(epsilon_plasma):
        if eps < 0:
            delta[i] = 1.0 / (omega[i] * np.sqrt(abs(eps) * mu))
        else:
            delta[i] = np.inf
    
    # 無限大の値を除外してプロット
    valid_indices = delta < 1e3
    ax4.semilogx(omega_ratio[valid_indices], delta[valid_indices], 'b-', linewidth=2, label='侵入深さ $\delta$')
    ax4.axvline(x=1, color='red', linestyle='--', alpha=0.7, label=r'$\omega = \omega_p$')
    ax4.set_xlabel(r'$\omega/\omega_p$', fontsize=12)
    ax4.set_ylabel('侵入深さ $\delta$', fontsize=12)
    ax4.set_title('プラズマ中の電磁波の侵入深さ（スキン深さ）', fontsize=12)
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig12_plasma_permittivity.png', dpi=200, bbox_inches='tight')
    print("図12を保存しました: electromagnetism_exercise_20251226_fig12_plasma_permittivity.png")
    plt.close()

# 図13: 問題4-4 エバネッセント波の減衰
def plot_evanescent_wave():
    """エバネッセント波の減衰の可視化"""
    # パラメータ設定
    omega = 1.0
    mu = 1.0
    epsilon_0 = 1.0
    
    # 負の誘電率の場合
    epsilon_neg = -2.0 * epsilon_0
    
    # 波数（純虚数）
    k_imag = omega * np.sqrt(abs(epsilon_neg) * mu)
    k = 1j * k_imag
    
    # 空間範囲
    z = np.linspace(0, 5 / k_imag, 1000)
    
    # 電場の振幅（指数関数的に減衰）
    E_amplitude = np.exp(-k_imag * z)
    
    # 時間変化も考慮
    t = np.linspace(0, 4 * np.pi / omega, 100)
    z_grid, t_grid = np.meshgrid(z, t)
    
    # 電場の実部（2D配列）
    # E_amplitudeは1D配列なので、2Dに拡張
    E_amplitude_2d = np.tile(E_amplitude, (len(t), 1))  # (N_t, N_z)
    E_real = E_amplitude_2d * np.cos(omega * t_grid)
    
    # プロット
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 左図: 電場の振幅の減衰
    ax1.plot(z, E_amplitude, 'b-', linewidth=2, label=r'$|E(z)| \propto e^{-z/\delta}$')
    ax1.axhline(y=1/np.e, color='red', linestyle='--', alpha=0.7, label=r'$1/e$')
    # スキン深さの位置
    delta = 1.0 / k_imag
    ax1.axvline(x=delta, color='red', linestyle='--', alpha=0.7, label=r'$\delta = 1/(\omega\sqrt{|\varepsilon|\mu})$')
    ax1.set_xlabel('距離 $z$', fontsize=12)
    ax1.set_ylabel('電場の振幅 $|E(z)|$', fontsize=12)
    ax1.set_title('エバネッセント波の減衰（負の誘電率）', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')
    
    # 右図: 電場の時間・空間分布
    im = ax2.contourf(z_grid, t_grid, E_real, levels=20, cmap='RdBu', alpha=0.8)
    ax2.set_xlabel('距離 $z$', fontsize=12)
    ax2.set_ylabel('時間 $t$', fontsize=12)
    ax2.set_title('エバネッセント波の時間・空間分布', fontsize=12)
    plt.colorbar(im, ax=ax2, label='電場 $E(z,t)$')
    
    plt.tight_layout()
    plt.savefig('electromagnetism_exercise_20251226_fig13_evanescent_wave.png', dpi=200, bbox_inches='tight')
    print("図13を保存しました: electromagnetism_exercise_20251226_fig13_evanescent_wave.png")
    plt.close()

# メイン関数
def main():
    """すべての図を生成"""
    print("電磁気学演習問題の図を生成中...")
    plot_dielectric_dispersion()
    plot_energy_absorption()
    plot_absorption_cross_section()
    plot_scattering_cross_section()
    plot_reflectance()
    plot_wave_reflection_diagram()
    plot_phase_condition()
    plot_negative_epsilon()
    plot_transmittance()
    plot_phase_change_time_evolution()
    plot_reflection_coefficient_phase()
    plot_plasma_permittivity()
    plot_evanescent_wave()
    print("すべての図の生成が完了しました。")

if __name__ == "__main__":
    main()

