"""
反射壁・周期的境界条件：有限領域 [-L,L]^2 での拡散。
反射では MSD が飽和、周期では距離の周期化により MSD も飽和。
"""
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False

kB, T, m, gamma = 1.0, 1.0, 1.0, 1.0
D = kB * T / gamma


def sim_reflecting(dt, n_steps, L, seed):
    np.random.seed(seed)
    rx, ry = 0.0, 0.0
    vx, vy = 0.0, 0.0
    c1 = gamma / m
    c2 = np.sqrt(2.0 * gamma * kB * T / m)
    t = np.arange(n_steps + 1) * dt
    x, y = np.zeros(n_steps + 1), np.zeros(n_steps + 1)
    x[0], y[0] = 0.0, 0.0
    for n in range(n_steps):
        vx = vx - c1 * vx * dt + c2 * np.sqrt(dt) * np.random.normal(0, 1)
        vy = vy - c1 * vy * dt + c2 * np.sqrt(dt) * np.random.normal(0, 1)
        rx += vx * dt
        ry += vy * dt
        # 反射
        if rx > L:
            rx = 2 * L - rx
            vx = -vx
        elif rx < -L:
            rx = -2 * L - rx
            vx = -vx
        if ry > L:
            ry = 2 * L - ry
            vy = -vy
        elif ry < -L:
            ry = -2 * L - ry
            vy = -vy
        x[n + 1], y[n + 1] = rx, ry
    return t, x, y


def sim_periodic(dt, n_steps, L, seed):
    np.random.seed(seed)
    rx, ry = 0.0, 0.0
    vx, vy = 0.0, 0.0
    c1 = gamma / m
    c2 = np.sqrt(2.0 * gamma * kB * T / m)
    t = np.arange(n_steps + 1) * dt
    x, y = np.zeros(n_steps + 1), np.zeros(n_steps + 1)
    x[0], y[0] = 0.0, 0.0
    for n in range(n_steps):
        vx = vx - c1 * vx * dt + c2 * np.sqrt(dt) * np.random.normal(0, 1)
        vy = vy - c1 * vy * dt + c2 * np.sqrt(dt) * np.random.normal(0, 1)
        rx += vx * dt
        ry += vy * dt
        rx = (rx + L) % (2 * L) - L
        ry = (ry + L) % (2 * L) - L
        x[n + 1], y[n + 1] = rx, ry
    return t, x, y


def min_image_scalar(d, L):
    d = d % (2 * L)
    if d > L:
        d -= 2 * L
    return d


def msd_periodic(x, y, L):
    """周期境界での MSD: 最小イメージ距離。"""
    n = len(x)
    msd = np.zeros(n)
    for i in range(n):
        dx = min_image_scalar(x[i] - x[0], L)
        dy = min_image_scalar(y[i] - y[0], L)
        msd[i] = dx ** 2 + dy ** 2
    return msd


os.makedirs('figures', exist_ok=True)

dt, n_steps, L = 0.01, 3000, 3.0
n_runs = 40
traj_ref = [sim_reflecting(dt, n_steps, L, r) for r in range(n_runs)]
traj_per = [sim_periodic(dt, n_steps, L, r) for r in range(n_runs)]

t = traj_ref[0][0]
msd_ref = np.mean([tr[1] ** 2 + tr[2] ** 2 for tr in traj_ref], axis=0)
msd_per = np.mean([msd_periodic(tr[1], tr[2], L) for tr in traj_per], axis=0)
msd_free = 4 * D * t
# 飽和の目安: 2次元等方 半径L の一様分布なら <r^2> ~ L^2 (程度)
r2_sat = L ** 2

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
ax = axes[0]
ax.plot(t, msd_ref, 'b-', lw=2, label='反射壁')
ax.plot(t, msd_free, 'k--', lw=1.5, label=r'自由空間 $4Dt$')
ax.axhline(r2_sat, color='gray', ls=':', alpha=0.8, label=rf'飽和目安 $\sim L^2$')
ax.set_xlabel(r'時間 $t$')
ax.set_ylabel(r'$\langle r^2 \rangle$')
ax.set_title(rf'反射壁 $[-L,L]^2$（$L={L}$）')
ax.legend()
ax.grid(True, alpha=0.3)

ax = axes[1]
ax.plot(t, msd_per, 'g-', lw=2, label='周期境界')
ax.plot(t, msd_free, 'k--', lw=1.5, label=r'自由空間 $4Dt$')
ax.axhline(r2_sat, color='gray', ls=':', alpha=0.8, label=rf'飽和目安 $\sim L^2$')
ax.set_xlabel(r'時間 $t$')
ax.set_ylabel(r'$\langle r^2 \rangle$')
ax.set_title(rf'周期境界 $[-L,L]^2$（$L={L}$）')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figures/boundary_conditions.png', dpi=150)
plt.close()
print("boundary_conditions.png を保存しました。")
