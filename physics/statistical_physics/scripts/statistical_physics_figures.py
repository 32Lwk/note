import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントの設定
rcParams['font.family'] = 'Hiragino Sans'
rcParams['axes.unicode_minus'] = False

# 図1: 調和振動子のエネルギー準位
def plot_energy_levels():
    fig, ax = plt.subplots(figsize=(8, 10))
    
    # パラメータ
    hbar_omega = 1.0  # 規格化
    m_max = 4
    
    # エネルギー準位
    m_values = np.arange(0, m_max + 1)
    energies = hbar_omega * (m_values + 0.5)
    
    # 水平線を描画
    for i, (m, E) in enumerate(zip(m_values, energies)):
        ax.plot([0, 1], [E, E], 'b-', linewidth=2)
        ax.text(1.1, E, f'$E_{{{m}}} = {m + 0.5:.1f}\\hbar\\omega$', 
                fontsize=12, verticalalignment='center')
        ax.text(-0.1, E, f'$m={m}$', fontsize=11, 
                horizontalalignment='right', verticalalignment='center')
    
    # 矢印で準位間隔を示す
    for i in range(m_max):
        E_mid = (energies[i] + energies[i+1]) / 2
        ax.annotate('', xy=(0.5, energies[i+1]), xytext=(0.5, energies[i]),
                   arrowprops=dict(arrowstyle='<->', color='red', lw=2))
        ax.text(0.6, E_mid, f'$\\Delta E = \\hbar\\omega$', 
                fontsize=11, color='red', verticalalignment='center')
    
    # 零点エネルギーに注釈
    ax.annotate('零点エネルギー', xy=(0.5, energies[0]), 
               xytext=(0.5, energies[0] - 0.3),
               arrowprops=dict(arrowstyle='->', color='green', lw=1.5),
               fontsize=11, color='green', ha='center')
    
    ax.set_xlim(-0.3, 2.5)
    ax.set_ylim(-0.2, energies[-1] + 0.5)
    ax.set_xlabel('', fontsize=12)
    ax.set_ylabel('エネルギー $E$', fontsize=14)
    ax.set_title('調和振動子のエネルギー準位', fontsize=16, pad=20)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xticks([])
    
    plt.tight_layout()
    plt.savefig('physics/statistical_physics_fig1_energy_levels.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("図1を保存しました: statistical_physics_fig1_energy_levels.png")

# 図2: ボルツマン因子の温度依存性
def plot_boltzmann_factor():
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # エネルギー範囲
    E = np.linspace(0, 5, 1000)
    
    # 異なる温度でのボルツマン因子
    temperatures = [0.5, 1.0, 2.0]
    colors = ['blue', 'green', 'red']
    labels = ['$T = 0.5$', '$T = 1.0$', '$T = 2.0$']
    
    for T, color, label in zip(temperatures, colors, labels):
        beta = 1.0 / T  # k_B = 1として規格化
        P = np.exp(-beta * E)
        ax.plot(E, P, color=color, linewidth=2.5, label=label)
    
    ax.set_xlabel('エネルギー $E$', fontsize=14)
    ax.set_ylabel('ボルツマン因子 $e^{-\\beta E}$', fontsize=14)
    ax.set_title('ボルツマン因子の温度依存性', fontsize=16, pad=20)
    ax.legend(fontsize=12, loc='upper right')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1.1)
    
    # 説明テキスト
    ax.text(0.7, 0.85, '温度が高いほど\n高エネルギー状態の\n確率が大きくなる', 
            fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
            verticalalignment='top')
    
    plt.tight_layout()
    plt.savefig('physics/statistical_physics_fig2_boltzmann.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("図2を保存しました: statistical_physics_fig2_boltzmann.png")

# 図3: エネルギー準位と状態の縮退（N=3の場合）
def plot_energy_degeneracy():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    hbar_omega = 1.0
    N = 3
    
    # Mの値と対応するエネルギー
    M_values = [0, 1, 2, 3]
    energies = [hbar_omega * (M + N/2) for M in M_values]
    
    # 各Mに対する状態の例
    states = {
        0: ['(0,0,0)'],
        1: ['(1,0,0)', '(0,1,0)', '(0,0,1)'],
        2: ['(2,0,0)', '(0,2,0)', '(0,0,2)', '(1,1,0)', '(1,0,1)', '(0,1,1)'],
        3: ['(3,0,0)', '(0,3,0)', '(0,0,3)', '(2,1,0)', '(2,0,1)', '(1,2,0)', 
            '(0,2,1)', '(1,0,2)', '(0,1,2)', '(1,1,1)']
    }
    
    # エネルギー準位を描画
    for i, (M, E) in enumerate(zip(M_values, energies)):
        # 水平線
        ax.plot([0, 1], [E, E], 'b-', linewidth=3)
        
        # エネルギーラベル
        ax.text(-0.15, E, f'$M={M}$', fontsize=12, 
                horizontalalignment='right', verticalalignment='center')
        ax.text(1.1, E, f'$E = {M + N/2:.1f}\\hbar\\omega$', 
                fontsize=12, verticalalignment='center')
        
        # 状態の数を表示
        num_states = len(states[M])
        ax.text(0.5, E + 0.15, f'{num_states}個の状態', 
                fontsize=10, ha='center', color='red', weight='bold')
        
        # 状態の例を表示（最初の3つまで）
        state_text = ', '.join(states[M][:3])
        if len(states[M]) > 3:
            state_text += f', ... ({num_states}個)'
        ax.text(1.8, E, state_text, fontsize=9, 
                verticalalignment='center', style='italic')
    
    ax.set_xlim(-0.4, 4.5)
    ax.set_ylim(energies[0] - 0.3, energies[-1] + 0.5)
    ax.set_xlabel('', fontsize=12)
    ax.set_ylabel('エネルギー $E$', fontsize=14)
    ax.set_title(f'エネルギー準位と状態の縮退 ($N={N}$)', fontsize=16, pad=20)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xticks([])
    
    # 説明テキスト
    ax.text(2.5, energies[-1] + 0.3, 
            '同じエネルギーを持つ複数の\n量子状態が存在する（縮退）', 
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5),
            verticalalignment='bottom')
    
    plt.tight_layout()
    plt.savefig('physics/statistical_physics_fig3_degeneracy.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("図3を保存しました: statistical_physics_fig3_degeneracy.png")

# 図4: 比熱の温度依存性（アインシュタイン比熱）
def plot_heat_capacity():
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # 温度範囲（規格化温度 T/T_E）
    T_ratio = np.linspace(0.01, 3, 1000)
    
    # アインシュタイン比熱
    # C_V/(Nk_B) = (θ_E/T)^2 * exp(θ_E/T) / (exp(θ_E/T) - 1)^2
    # ここで θ_E = ħω/k_B = T_E
    # T_ratio = T/T_E とすると、θ_E/T = 1/T_ratio
    x = 1.0 / T_ratio
    C_V = x**2 * np.exp(x) / (np.exp(x) - 1)**2
    
    ax.plot(T_ratio, C_V, 'b-', linewidth=2.5, label='アインシュタイン比熱')
    
    # デュロン・プティの法則（高温極限）
    ax.axhline(y=1.0, color='r', linestyle='--', linewidth=2, 
              label='デュロン・プティの法則 ($C_V = Nk_B$)')
    
    # アインシュタイン温度の位置
    ax.axvline(x=1.0, color='green', linestyle=':', linewidth=1.5, alpha=0.7)
    ax.text(1.0, 0.05, '$T_E = \\hbar\\omega/k_B$', 
            fontsize=11, rotation=90, verticalalignment='bottom',
            horizontalalignment='right', color='green')
    
    ax.set_xlabel('温度 $T/T_E$ (規格化)', fontsize=14)
    ax.set_ylabel('比熱 $C_V/(Nk_B)$', fontsize=14)
    ax.set_title('アインシュタイン比熱の温度依存性', fontsize=16, pad=20)
    ax.legend(fontsize=12, loc='upper left')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 1.1)
    
    # 説明テキスト
    ax.text(2.2, 0.3, 
            '低温: 指数関数的に減少\n高温: デュロン・プティの法則\nに近づく', 
            fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
            verticalalignment='top')
    
    plt.tight_layout()
    plt.savefig('physics/statistical_physics_fig4_heat_capacity.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("図4を保存しました: statistical_physics_fig4_heat_capacity.png")

if __name__ == '__main__':
    print("統計物理学の図を作成中...")
    plot_energy_levels()
    plot_boltzmann_factor()
    plot_energy_degeneracy()
    plot_heat_capacity()
    print("すべての図を作成しました！")

