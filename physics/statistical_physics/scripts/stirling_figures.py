import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.special import gamma

# 日本語フォントの設定
rcParams['font.family'] = 'Hiragino Sans'
rcParams['axes.unicode_minus'] = False

# 図1: ガンマ関数の被積分関数 t^x e^(-t) の概形
def plot_gamma_integrand():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    t = np.linspace(0, 10, 1000)
    
    # x=2の場合
    x1 = 2
    f1 = t**x1 * np.exp(-t)
    axes[0].plot(t, f1, 'b-', linewidth=2.5, label=f'$f(t) = t^{{{x1}}} e^{{-t}}$')
    axes[0].axvline(x=x1, color='r', linestyle='--', linewidth=1.5, alpha=0.7, label=f'$t = {x1}$ (極大点)')
    axes[0].plot(x1, x1**x1 * np.exp(-x1), 'ro', markersize=10, label='極大値')
    axes[0].set_xlabel('$t$', fontsize=14)
    axes[0].set_ylabel('$f(t) = t^x e^{-t}$', fontsize=14)
    axes[0].set_title(f'$\\Gamma(x+1)$ の被積分関数 ($x={x1}$)', fontsize=16, pad=20)
    axes[0].legend(fontsize=11)
    axes[0].grid(True, alpha=0.3, linestyle='--')
    axes[0].set_xlim(0, 10)
    axes[0].set_ylim(0, None)
    
    # x=5の場合
    x2 = 5
    f2 = t**x2 * np.exp(-t)
    axes[1].plot(t, f2, 'g-', linewidth=2.5, label=f'$f(t) = t^{{{x2}}} e^{{-t}}$')
    axes[1].axvline(x=x2, color='r', linestyle='--', linewidth=1.5, alpha=0.7, label=f'$t = {x2}$ (極大点)')
    axes[1].plot(x2, x2**x2 * np.exp(-x2), 'ro', markersize=10, label='極大値')
    axes[1].set_xlabel('$t$', fontsize=14)
    axes[1].set_ylabel('$f(t) = t^x e^{-t}$', fontsize=14)
    axes[1].set_title(f'$\\Gamma(x+1)$ の被積分関数 ($x={x2}$)', fontsize=16, pad=20)
    axes[1].legend(fontsize=11)
    axes[1].grid(True, alpha=0.3, linestyle='--')
    axes[1].set_xlim(0, 12)
    axes[1].set_ylim(0, None)
    
    plt.tight_layout()
    plt.savefig('physics/statistical_physics_fig5_gamma_integrand.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("図5を保存しました: statistical_physics_fig5_gamma_integrand.png")

# 図2: D次元球の体積（D=1,2,3,4,5の場合）
def plot_d_sphere_volume():
    fig, ax = plt.subplots(figsize=(10, 7))
    
    R = 1.0  # 半径を1に規格化
    D_values = [1, 2, 3, 4, 5]
    colors = ['blue', 'green', 'red', 'purple', 'orange']
    
    for D, color in zip(D_values, colors):
        # ガンマ関数を用いた体積公式
        V_D = (np.pi**(D/2) * R**D) / gamma(D/2 + 1)
        ax.bar(D, V_D, color=color, alpha=0.7, label=f'$D={D}$')
        ax.text(D, V_D + 0.2, f'${V_D:.3f}$', ha='center', fontsize=10)
    
    ax.set_xlabel('次元 $D$', fontsize=14)
    ax.set_ylabel('体積 $V_D(R=1)$', fontsize=14)
    ax.set_title('D次元球の体積 ($R=1$)', fontsize=16, pad=20)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, linestyle='--', axis='y')
    ax.set_xticks(D_values)
    ax.set_ylim(0, 5)
    
    plt.tight_layout()
    plt.savefig('physics/statistical_physics_fig6_d_sphere_volume.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("図6を保存しました: statistical_physics_fig6_d_sphere_volume.png")

# 図3: 古典理想気体の状態数密度（問6のピーク）
def plot_ideal_gas_density():
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # パラメータ
    N = 100  # 粒子数（大きい数値でピークが明確に）
    T = 1.0  # 温度
    kB = 1.0
    beta = 1.0 / (kB * T)
    
    # エネルギー範囲
    E = np.linspace(0.1, 3*N*kB*T, 1000)
    
    # W_N(E) は E^(3N/2-1) に比例（定数因子は省略）
    # 実際の計算には定数因子が必要だが、形状を見るため
    # 正規化してプロット
    log_W = (3*N/2 - 1) * np.log(E)  # 定数項は省略
    integrand = np.exp(log_W - beta * E)
    
    # 正規化
    integrand = integrand / np.max(integrand)
    
    ax.plot(E / (N*kB*T), integrand, 'b-', linewidth=2.5, label='$W_N(E) e^{-\\beta E}$')
    
    # ピークの位置（E* = (3N/2 - 1) k_B T ≈ 3N/2 k_B T）
    E_star = (3*N/2 - 1) * kB * T
    ax.axvline(x=E_star/(N*kB*T), color='r', linestyle='--', 
               linewidth=2, label=f'$E^* = {E_star/(N*kB*T):.2f} N k_B T$')
    
    ax.set_xlabel('$E / (N k_B T)$', fontsize=14)
    ax.set_ylabel('正規化された値', fontsize=14)
    ax.set_title('古典理想気体の状態数密度 ($N=100$)', fontsize=16, pad=20)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 1.1)
    
    plt.tight_layout()
    plt.savefig('physics/statistical_physics_fig7_ideal_gas_density.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("図7を保存しました: statistical_physics_fig7_ideal_gas_density.png")

if __name__ == '__main__':
    print("統計物理学の追加図を作成中...")
    plot_gamma_integrand()
    plot_d_sphere_volume()
    plot_ideal_gas_density()
    print("すべての図を作成しました！")

