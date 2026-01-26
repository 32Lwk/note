"""
問題4-1, 4-2: 箱の中の粒子の波動関数の可視化
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.font_manager as fm

# 日本語フォントの設定（macOS用）
japanese_fonts = ['Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Arial Unicode MS', 'AppleGothic', 'Osaka']
font_found = None
for font_name in japanese_fonts:
    try:
        font_path = fm.findfont(fm.FontProperties(family=font_name))
        if font_path:
            font_found = font_name
            break
    except:
        continue

if font_found:
    rcParams['font.family'] = font_found
    print(f"日本語フォントを使用: {font_found}")
else:
    import platform
    if platform.system() == 'Darwin':  # macOS
        rcParams['font.family'] = 'Hiragino Sans'
    else:
        rcParams['font.family'] = 'sans-serif'
    print("デフォルトフォントを使用")

rcParams['font.size'] = 12
rcParams['axes.unicode_minus'] = False

# ========== 問題4-1 ==========
print("問題4-1の図を作成中...")

# パラメータ
a = 1.0  # 井戸の幅
C = np.sqrt(72 / (49 * a))  # 規格化定数

# 位置座標
x = np.linspace(0, a, 1000)

# 固有関数
def u_n(x, n, a):
    """エネルギー固有関数"""
    return np.sqrt(2/a) * np.sin(n * np.pi * x / a)

# 初期波動関数
def psi_initial(x, a, C):
    """問題4-1の初期波動関数"""
    mask = (x > 0) & (x < a)
    psi = np.zeros_like(x)
    psi[mask] = C * (np.sin(np.pi * x[mask] / a) + 
                     0.5 * np.sin(2 * np.pi * x[mask] / a) + 
                     (1/3) * np.sin(3 * np.pi * x[mask] / a))
    return psi

# 展開係数
A1 = 6/7
A2 = 3/7
A3 = 2/7

# 展開された波動関数
psi_expanded = A1 * u_n(x, 1, a) + A2 * u_n(x, 2, a) + A3 * u_n(x, 3, a)

# 図の作成
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('問題4-1: 箱の中の粒子 No.1', fontsize=16, fontweight='bold')

# (a) 初期波動関数と固有関数
ax = axes[0, 0]
ax.plot(x, psi_initial(x, a, C), 'b-', linewidth=2, label='初期波動関数 ψ(x)')
ax.plot(x, u_n(x, 1, a), 'r--', linewidth=1.5, alpha=0.7, label='u₁(x) (基底状態)')
ax.plot(x, u_n(x, 2, a), 'g--', linewidth=1.5, alpha=0.7, label='u₂(x) (第1励起状態)')
ax.plot(x, u_n(x, 3, a), 'm--', linewidth=1.5, alpha=0.7, label='u₃(x) (第2励起状態)')
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=a, color='k', linestyle='-', linewidth=0.5)
ax.set_xlabel('位置 x', fontsize=12)
ax.set_ylabel('波動関数', fontsize=12)
ax.set_title('(a) 初期波動関数と固有関数', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-0.1*a, 1.1*a)

# (b) 確率密度
ax = axes[0, 1]
ax.plot(x, psi_initial(x, a, C)**2, 'b-', linewidth=2, label='|ψ(x)|²')
ax.plot(x, u_n(x, 1, a)**2, 'r--', linewidth=1.5, alpha=0.7, label='|u₁(x)|²')
ax.plot(x, u_n(x, 2, a)**2, 'g--', linewidth=1.5, alpha=0.7, label='|u₂(x)|²')
ax.plot(x, u_n(x, 3, a)**2, 'm--', linewidth=1.5, alpha=0.7, label='|u₃(x)|²')
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=a, color='k', linestyle='-', linewidth=0.5)
ax.set_xlabel('位置 x', fontsize=12)
ax.set_ylabel('確率密度', fontsize=12)
ax.set_title('(b) 確率密度', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-0.1*a, 1.1*a)

# (c) 展開係数の比較
ax = axes[1, 0]
n_values = [1, 2, 3]
A_values = [A1, A2, A3]
probabilities = [A1**2, A2**2, A3**2]
ax.bar([n - 0.2 for n in n_values], A_values, width=0.4, label='展開係数 |Aₙ|', color='skyblue', alpha=0.7)
ax.bar([n + 0.2 for n in n_values], probabilities, width=0.4, label='確率 |Aₙ|²', color='coral', alpha=0.7)
ax.set_xlabel('量子数 n', fontsize=12)
ax.set_ylabel('値', fontsize=12)
ax.set_title('(c) 展開係数と確率', fontsize=12)
ax.set_xticks(n_values)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, axis='y')

# (d) 展開の確認
ax = axes[1, 1]
ax.plot(x, psi_initial(x, a, C), 'b-', linewidth=2, label='初期波動関数 ψ(x)')
ax.plot(x, psi_expanded, 'r--', linewidth=2, alpha=0.7, label='展開: Σ Aₙuₙ(x)')
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=a, color='k', linestyle='-', linewidth=0.5)
ax.set_xlabel('位置 x', fontsize=12)
ax.set_ylabel('波動関数', fontsize=12)
ax.set_title('(d) 展開の確認', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-0.1*a, 1.1*a)

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/physics/量子力学過去問/figures/problem4_1_wavefunctions.png', dpi=300, bbox_inches='tight')
print("問題4-1の図を保存しました: figures/problem4_1_wavefunctions.png")
plt.close()

# ========== 問題4-2 ==========
print("問題4-2の図を作成中...")

# パラメータ
a = 1.0  # 井戸の幅（中心から端まで）

# 位置座標
x = np.linspace(-a, a, 1000)

# 固有関数（対称ポテンシャル）
def u_n_symmetric(x, n, a):
    """対称ポテンシャルのエネルギー固有関数"""
    mask = (x >= -a) & (x <= a)
    u = np.zeros_like(x)
    if n % 2 == 1:  # 奇数: コサイン
        u[mask] = np.sqrt(1/a) * np.cos(n * np.pi * x[mask] / (2*a))
    else:  # 偶数: サイン
        u[mask] = np.sqrt(1/a) * np.sin(n * np.pi * x[mask] / (2*a))
    return u

# 初期波動関数（左半分に局在）
def psi_initial_left(x, a):
    """問題4-2の初期波動関数（左半分に局在）"""
    mask = (x > -a) & (x < 0)
    psi = np.zeros_like(x)
    psi[mask] = np.sqrt(1/a)
    return psi

# 展開係数の計算（数値積分）
def calculate_A_n(n, a, num_points=1000):
    """展開係数A_nを数値積分で計算"""
    x = np.linspace(-a, a, num_points)
    dx = 2*a / num_points
    u_n = u_n_symmetric(x, n, a)
    psi = psi_initial_left(x, a)
    A_n = np.trapz(u_n * psi, x)
    return A_n

# 展開係数の計算
A1 = calculate_A_n(1, a)
A2 = calculate_A_n(2, a)

# 図の作成
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('問題4-2: 箱の中の粒子 No.2', fontsize=16, fontweight='bold')

# (a) 初期波動関数と固有関数
ax = axes[0, 0]
ax.plot(x, psi_initial_left(x, a), 'b-', linewidth=2, label='初期波動関数 ψ(x)')
ax.plot(x, u_n_symmetric(x, 1, a), 'r--', linewidth=1.5, alpha=0.7, label='u₁(x) (基底状態, 偶関数)')
ax.plot(x, u_n_symmetric(x, 2, a), 'g--', linewidth=1.5, alpha=0.7, label='u₂(x) (第1励起状態, 奇関数)')
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='--', linewidth=1, alpha=0.5, label='中心 x=0')
ax.axvline(x=-a, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=a, color='k', linestyle='-', linewidth=0.5)
ax.set_xlabel('位置 x', fontsize=12)
ax.set_ylabel('波動関数', fontsize=12)
ax.set_title('(a) 初期波動関数と固有関数', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-1.2*a, 1.2*a)

# (b) 確率密度
ax = axes[0, 1]
ax.plot(x, psi_initial_left(x, a)**2, 'b-', linewidth=2, label='|ψ(x)|²')
ax.plot(x, u_n_symmetric(x, 1, a)**2, 'r--', linewidth=1.5, alpha=0.7, label='|u₁(x)|²')
ax.plot(x, u_n_symmetric(x, 2, a)**2, 'g--', linewidth=1.5, alpha=0.7, label='|u₂(x)|²')
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='--', linewidth=1, alpha=0.5)
ax.axvline(x=-a, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=a, color='k', linestyle='-', linewidth=0.5)
ax.set_xlabel('位置 x', fontsize=12)
ax.set_ylabel('確率密度', fontsize=12)
ax.set_title('(b) 確率密度', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-1.2*a, 1.2*a)

# (c) 展開係数の比較
ax = axes[1, 0]
n_values = [1, 2]
A_values = [A1, A2]
probabilities = [A1**2, A2**2]
ax.bar([n - 0.2 for n in n_values], A_values, width=0.4, label='展開係数 |Aₙ|', color='skyblue', alpha=0.7)
ax.bar([n + 0.2 for n in n_values], probabilities, width=0.4, label='確率 |Aₙ|²', color='coral', alpha=0.7)
ax.set_xlabel('量子数 n', fontsize=12)
ax.set_ylabel('値', fontsize=12)
ax.set_title('(c) 展開係数と確率', fontsize=12)
ax.set_xticks(n_values)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, axis='y')
# 理論値の表示
ax.text(1, A1, f'理論値: 2/π ≈ {2/np.pi:.3f}', fontsize=9, ha='left', va='bottom')
ax.text(2, abs(A2), f'理論値: 2/π ≈ {2/np.pi:.3f}', fontsize=9, ha='left', va='bottom')

# (d) 展開の確認
ax = axes[1, 1]
psi_expanded = A1 * u_n_symmetric(x, 1, a) + A2 * u_n_symmetric(x, 2, a)
ax.plot(x, psi_initial_left(x, a), 'b-', linewidth=2, label='初期波動関数 ψ(x)')
ax.plot(x, psi_expanded, 'r--', linewidth=2, alpha=0.7, label='展開: A₁u₁(x) + A₂u₂(x)')
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='--', linewidth=1, alpha=0.5)
ax.axvline(x=-a, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=a, color='k', linestyle='-', linewidth=0.5)
ax.set_xlabel('位置 x', fontsize=12)
ax.set_ylabel('波動関数', fontsize=12)
ax.set_title('(d) 展開の確認', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-1.2*a, 1.2*a)

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/physics/量子力学過去問/figures/problem4_2_wavefunctions.png', dpi=300, bbox_inches='tight')
print("問題4-2の図を保存しました: figures/problem4_2_wavefunctions.png")
plt.close()

# ========== 問題4-3 ==========
print("問題4-3の図を作成中...")

# 具体例のエルミート行列
M = np.array([[2, 1], [1, 2]])

# 固有値と固有ベクトルの計算
eigenvals, eigenvecs = np.linalg.eigh(M)
lambda1, lambda2 = eigenvals
v1, v2 = eigenvecs[:, 0], eigenvecs[:, 1]

# 規格化（既に規格化されているが確認）
v1 = v1 / np.linalg.norm(v1)
v2 = v2 / np.linalg.norm(v2)

# 図の作成
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('問題4-3: 線形代数の復習 - エルミート行列の具体例', fontsize=16, fontweight='bold')

# (a) 固有ベクトルの可視化
ax = axes[0]
# 座標軸
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
# 固有ベクトル
ax.arrow(0, 0, v1[0], v1[1], head_width=0.1, head_length=0.1, fc='r', ec='r', linewidth=2, label=f'固有ベクトル v₁ (固有値 λ₁={lambda1:.1f})')
ax.arrow(0, 0, v2[0], v2[1], head_width=0.1, head_length=0.1, fc='g', ec='g', linewidth=2, label=f'固有ベクトル v₂ (固有値 λ₂={lambda2:.1f})')
# 単位円
theta = np.linspace(0, 2*np.pi, 100)
ax.plot(np.cos(theta), np.sin(theta), 'k--', linewidth=1, alpha=0.3, label='単位円')
ax.set_xlabel('x成分', fontsize=12)
ax.set_ylabel('y成分', fontsize=12)
ax.set_title('(a) 固有ベクトルの可視化', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# (b) 対角化の概念図
ax = axes[1]
# 元の行列の作用
test_vecs = np.array([[1, 0], [0, 1], [1, 1], [-1, 1]]) * 0.5
colors = ['b', 'g', 'm', 'c']
for i, (vec, color) in enumerate(zip(test_vecs, colors)):
    transformed = M @ vec
    ax.arrow(0, 0, vec[0], vec[1], head_width=0.05, head_length=0.05, 
             fc=color, ec=color, linewidth=1.5, alpha=0.5, linestyle='--')
    ax.arrow(0, 0, transformed[0], transformed[1], head_width=0.05, head_length=0.05, 
             fc=color, ec=color, linewidth=2)
    # ラベル
    ax.text(vec[0]+0.1, vec[1]+0.1, f'v{i+1}', fontsize=9, color=color)
    ax.text(transformed[0]+0.1, transformed[1]+0.1, f'M·v{i+1}', fontsize=9, color=color, fontweight='bold')
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
ax.set_xlabel('x成分', fontsize=12)
ax.set_ylabel('y成分', fontsize=12)
ax.set_title('(b) 行列の作用（対角化前）', fontsize=12)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/physics/量子力学過去問/figures/problem4_3_linear_algebra.png', dpi=300, bbox_inches='tight')
print("問題4-3の図を保存しました: figures/problem4_3_linear_algebra.png")
plt.close()

# ========== 問題4-4 ==========
print("問題4-4の図を作成中...")

# 不確定性関係の図
# 位置と運動量の不確定性の関係を可視化

# ガウス型波動関数（最小不確定性状態）
def gaussian_wavefunction(x, x0, sigma_x):
    """ガウス型波動関数"""
    return (1/(np.pi*sigma_x**2)**(1/4)) * np.exp(-(x-x0)**2/(2*sigma_x**2))

# 運動量表示でのガウス型
def gaussian_momentum(p, p0, sigma_p):
    """運動量表示でのガウス型"""
    return (1/(np.pi*sigma_p**2)**(1/4)) * np.exp(-(p-p0)**2/(2*sigma_p**2))

# 不確定性関係: Δx * Δp >= ħ/2
hbar = 1.0
min_product = hbar / 2

# 異なる不確定性の組み合わせ
sigma_x_values = np.array([0.3, 0.5, 0.7, 1.0])
sigma_p_values = min_product / sigma_x_values

# 位置座標
x = np.linspace(-3, 3, 1000)
p = np.linspace(-3, 3, 1000)

# 図の作成
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('問題4-4: 演算子の交換関係と不確定性関係', fontsize=16, fontweight='bold')

# (a) 位置表示での波動関数（異なる不確定性）
ax = axes[0, 0]
for i, (sigma_x, color) in enumerate(zip(sigma_x_values, ['r', 'g', 'b', 'm'])):
    psi = gaussian_wavefunction(x, 0, sigma_x)
    ax.plot(x, psi, color=color, linewidth=2, label=f'Δx = {sigma_x:.2f}')
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='--', linewidth=1, alpha=0.5)
ax.set_xlabel('位置 x', fontsize=12)
ax.set_ylabel('波動関数 ψ(x)', fontsize=12)
ax.set_title('(a) 位置表示での波動関数', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# (b) 運動量表示での波動関数
ax = axes[0, 1]
for i, (sigma_p, color) in enumerate(zip(sigma_p_values, ['r', 'g', 'b', 'm'])):
    phi = gaussian_momentum(p, 0, sigma_p)
    ax.plot(p, phi, color=color, linewidth=2, label=f'Δp = {sigma_p:.2f}')
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='--', linewidth=1, alpha=0.5)
ax.set_xlabel('運動量 p', fontsize=12)
ax.set_ylabel('波動関数 φ(p)', fontsize=12)
ax.set_title('(b) 運動量表示での波動関数', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# (c) 不確定性関係の図
ax = axes[1, 0]
# 不確定性関係の境界（双曲線）
sigma_x_plot = np.linspace(0.1, 2.0, 1000)
sigma_p_min = min_product / sigma_x_plot
ax.plot(sigma_x_plot, sigma_p_min, 'r-', linewidth=2, label='最小不確定性: Δx·Δp = ħ/2')
# 許容される領域
ax.fill_between(sigma_x_plot, sigma_p_min, 3, alpha=0.2, color='green', label='許容される領域')
# 具体例の点
for sigma_x, sigma_p, color in zip(sigma_x_values, sigma_p_values, ['r', 'g', 'b', 'm']):
    ax.plot(sigma_x, sigma_p, 'o', color=color, markersize=8, label=f'Δx={sigma_x:.2f}, Δp={sigma_p:.2f}')
ax.set_xlabel('位置の不確定性 Δx', fontsize=12)
ax.set_ylabel('運動量の不確定性 Δp', fontsize=12)
ax.set_title('(c) 不確定性関係: Δx·Δp ≥ ħ/2', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 2.0)
ax.set_ylim(0, 1.5)

# (d) 不確定性の積
ax = axes[1, 1]
products = sigma_x_values * sigma_p_values
ax.bar(range(len(products)), products, color=['r', 'g', 'b', 'm'], alpha=0.7)
ax.axhline(y=min_product, color='r', linestyle='--', linewidth=2, label='最小値 ħ/2')
ax.set_xlabel('状態', fontsize=12)
ax.set_ylabel('不確定性の積 Δx·Δp', fontsize=12)
ax.set_title('(d) 不確定性の積', fontsize=12)
ax.set_xticks(range(len(products)))
ax.set_xticklabels([f'状態{i+1}' for i in range(len(products))])
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, axis='y')
ax.text(1.5, min_product + 0.05, f'最小値 = {min_product:.3f}', fontsize=10, color='r', fontweight='bold')

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/physics/量子力学過去問/figures/problem4_4_uncertainty.png', dpi=300, bbox_inches='tight')
print("問題4-4の図を保存しました: figures/problem4_4_uncertainty.png")
plt.close()

print("すべての図の作成が完了しました。")
