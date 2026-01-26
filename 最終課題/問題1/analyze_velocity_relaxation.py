"""
平均二乗速度 <v²>(t) の緩和：初期 v=0 から熱平衡 2k_B T/m への収束。
等分配則への緩和を可視化する。
"""
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False


def simulate_brownian_motion_with_velocity(T, m, gamma, kB=1.0, dt=0.01, n_steps=1000, seed=None):
    """位置と速度の時系列。初期 v=0。"""
    if seed is not None:
        np.random.seed(seed)
    rx, ry = 0.0, 0.0
    vx, vy = 0.0, 0.0
    coeff1 = gamma / m
    coeff2 = np.sqrt(2.0 * gamma * kB * T / m)
    t = np.arange(n_steps + 1) * dt
    vx_arr = np.zeros(n_steps + 1)
    vy_arr = np.zeros(n_steps + 1)
    vx_arr[0], vy_arr[0] = 0.0, 0.0
    for n in range(n_steps):
        eta_x = np.random.normal(0, 1)
        eta_y = np.random.normal(0, 1)
        vx = vx - coeff1 * vx * dt + coeff2 * np.sqrt(dt) * eta_x
        vy = vy - coeff1 * vy * dt + coeff2 * np.sqrt(dt) * eta_y
        rx += vx * dt
        ry += vy * dt
        vx_arr[n + 1] = vx
        vy_arr[n + 1] = vy
    return t, vx_arr, vy_arr


os.makedirs('figures', exist_ok=True)

kB, dt, n_steps, n_runs = 1.0, 0.01, 1000, 100
T, m, gamma = 1.0, 1.0, 1.0
v2_eq = 2.0 * kB * T / m  # 熱平衡での <v²>

v2_list = []
for run in range(n_runs):
    t, vx, vy = simulate_brownian_motion_with_velocity(T, m, gamma, kB, dt, n_steps, seed=run)
    v2_list.append(vx**2 + vy**2)

v2_mean = np.mean(v2_list, axis=0)
v2_std = np.std(v2_list, axis=0)
t_arr = np.arange(n_steps + 1) * dt
# 理論: <v²>(t) = (2 k_B T / m) [1 - exp(-2 γ t / m)]
theory = v2_eq * (1.0 - np.exp(-2.0 * gamma / m * t_arr))

fig, ax = plt.subplots(figsize=(8, 5))
ax.fill_between(t_arr, v2_mean - v2_std, v2_mean + v2_std, alpha=0.3, color='blue')
ax.plot(t_arr, v2_mean, 'b-', lw=2, label=r'シミュレーション $\langle v^2 \rangle(t)$')
ax.plot(t_arr, theory, 'r--', lw=2, label=r'理論 $\frac{2k_B T}{m}\left[1 - e^{-2\gamma t/m}\right]$')
ax.axhline(v2_eq, color='gray', linestyle=':', alpha=0.8, label=rf'熱平衡 $\langle v^2 \rangle = 2k_B T/m = {v2_eq:.2f}$')
ax.set_xlabel(r'時間 $t$')
ax.set_ylabel(r'$\langle v^2 \rangle$')
ax.set_title(r'平均二乗速度の緩和（$v(0)=0$ → 熱平衡）')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_xlim(0, t_arr[-1])
plt.tight_layout()
plt.savefig('figures/velocity_relaxation.png', dpi=150)
plt.close()
print("velocity_relaxation.png を保存しました。")
