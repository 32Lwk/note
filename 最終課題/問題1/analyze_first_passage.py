"""
初到達時間（first-passage time）：原点から半径 R の円に初めて到達する時間の分布。
2次元拡散では平均初到達時間 ≈ R²/(4D)。多数回の試行でヒストグラム化。
"""
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False


def simulate_until_first_passage(T, m, gamma, R, kB=1.0, dt=0.01, max_steps=50000, seed=None):
    """|r| >= R になった最初の時刻を返す。超えなければ max_steps * dt。"""
    if seed is not None:
        np.random.seed(seed)
    rx, ry = 0.0, 0.0
    vx, vy = 0.0, 0.0
    coeff1 = gamma / m
    coeff2 = np.sqrt(2.0 * gamma * kB * T / m)
    for n in range(max_steps):
        r2 = rx * rx + ry * ry
        if r2 >= R * R:
            return (n + 1) * dt
        eta_x = np.random.normal(0, 1)
        eta_y = np.random.normal(0, 1)
        vx = vx - coeff1 * vx * dt + coeff2 * np.sqrt(dt) * eta_x
        vy = vy - coeff1 * vy * dt + coeff2 * np.sqrt(dt) * eta_y
        rx += vx * dt
        ry += vy * dt
    return max_steps * dt


os.makedirs('figures', exist_ok=True)

kB, dt = 1.0, 0.01
T, m, gamma = 1.0, 1.0, 1.0
D = kB * T / gamma
R = 2.0
n_runs = 2000
max_steps = 50000

fpt = np.array([simulate_until_first_passage(T, m, gamma, R, kB, dt, max_steps, seed=r) for r in range(n_runs)])
# 理論: 2次元、原点から半径 R の円への平均初到達時間 = R²/(4D)
tau_theory = R * R / (4.0 * D)
mean_fpt = np.mean(fpt)
print(f"R={R}, D={D:.4f}, 理論平均初到達時間 R²/(4D)={tau_theory:.4f}, サンプル平均={mean_fpt:.4f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

ax = axes[0]
ax.hist(fpt, bins=50, density=True, alpha=0.7, color='steelblue', edgecolor='black', label='ヒストグラム')
ax.axvline(mean_fpt, color='red', linestyle='-', lw=2, label=rf'サンプル平均 ${mean_fpt:.2f}$')
ax.axvline(tau_theory, color='green', linestyle='--', lw=2, label=rf'理論 $R^2/(4D) = {tau_theory:.2f}$')
ax.set_xlabel(r'初到達時間 $t$')
ax.set_ylabel('確率密度')
ax.set_title(rf'初到達時間の分布（$R = {R}$, $D = k_B T/\gamma = {D:.2f}$）')
ax.legend()
ax.grid(True, alpha=0.3)

# 右: サンプル軌道の例（R の円に到達するまで）
ax = axes[1]
np.random.seed(123)
rx, ry = 0.0, 0.0
vx, vy = 0.0, 0.0
coeff1 = gamma / m
coeff2 = np.sqrt(2.0 * gamma * kB * T / m)
path_x, path_y = [0.0], [0.0]
for n in range(max_steps):
    if rx * rx + ry * ry >= R * R:
        break
    eta_x = np.random.normal(0, 1)
    eta_y = np.random.normal(0, 1)
    vx = vx - coeff1 * vx * dt + coeff2 * np.sqrt(dt) * eta_x
    vy = vy - coeff1 * vy * dt + coeff2 * np.sqrt(dt) * eta_y
    rx += vx * dt
    ry += vy * dt
    path_x.append(rx)
    path_y.append(ry)

theta = np.linspace(0, 2 * np.pi, 200)
ax.plot(np.array(path_x), np.array(path_y), 'b-', lw=1.5, label='軌道')
ax.plot(R * np.cos(theta), R * np.sin(theta), 'r--', lw=2, label=rf'目標円 $r=R={R}$')
ax.plot(0, 0, 'ko', ms=8, label='原点')
ax.plot(path_x[-1], path_y[-1], 'go', ms=8, label='初到達点')
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_title('初到達までのかかる軌道の例')
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('figures/first_passage_time.png', dpi=150)
plt.close()
print("first_passage_time.png を保存しました。")
