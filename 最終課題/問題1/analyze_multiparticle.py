"""
複数粒子・排除体積：N 個の粒子を周期ボックス内でランジュバン運動させ、
排除体積（剛体球）の衝突で反発する簡易モデル。MSD を粒子平均で評価。
"""
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False

kB, T, m, gamma = 1.0, 1.0, 1.0, 1.0
D = kB * T / gamma


def min_image(dr, L):
    """周期 [-L,L] での最小イメージ距離。"""
    return np.where(dr > L, dr - 2 * L, np.where(dr < -L, dr + 2 * L, dr))


def simulate_n_particles(N, L, sigma, dt, n_steps, seed):
    """周期 [-L,L]^2、直径 sigma の剛体球。衝突時は反発。"""
    np.random.seed(seed)
    c1 = gamma / m
    c2 = np.sqrt(2.0 * gamma * kB * T / m)
    n_per_side = int(np.ceil(np.sqrt(N)))
    dx = 2 * L / (n_per_side + 1)
    pos = np.zeros((N, 2))
    vel = np.zeros((N, 2))
    for i in range(N):
        ix, iy = i % n_per_side, i // n_per_side
        pos[i] = [-L + (ix + 1) * dx, -L + (iy + 1) * dx]
    vel += 0.1 * np.random.standard_normal((N, 2))

    def wrap(z):
        return (z + L) % (2 * L) - L

    traj = np.zeros((n_steps + 1, N, 2))
    traj[0] = pos.copy()
    for n in range(n_steps):
        for i in range(N):
            eta = np.random.standard_normal(2)
            vel[i] = vel[i] - c1 * vel[i] * dt + c2 * np.sqrt(dt) * eta
        pos = pos + vel * dt
        pos = wrap(pos)
        for i in range(N):
            for j in range(i + 1, N):
                dr = min_image(pos[j] - pos[i], L)
                d = np.sqrt(np.sum(dr ** 2))
                if d < sigma and d > 1e-10:
                    nvec = dr / d
                    vn = np.dot(vel[j] - vel[i], nvec)
                    if vn < 0:
                        vel[i] = vel[i] + vn * nvec
                        vel[j] = vel[j] - vn * nvec
        traj[n + 1] = pos.copy()
    return traj


def msd_min_image(traj, L):
    """周期境界での MSD（最小イメージ）。"""
    n_t, N, _ = traj.shape
    msd = np.zeros((n_t, N))
    for i in range(N):
        r0 = traj[0, i]
        for t in range(n_t):
            dr = min_image(traj[t, i] - r0, L)
            msd[t, i] = np.sum(dr ** 2)
    return np.mean(msd, axis=1)


# 簡略化: 粒子数少なめ、σ 小さい
N, L, sigma = 8, 4.0, 0.4
dt, n_steps, n_runs = 0.01, 1500, 20
t_arr = np.arange(n_steps + 1) * dt
msd_list = []
for r in range(n_runs):
    traj = simulate_n_particles(N, L, sigma, dt, n_steps, r)
    msd = msd_min_image(traj, L)
    msd_list.append(msd)
msd_mean = np.mean(msd_list, axis=0)
msd_std = np.std(msd_list, axis=0)
msd_free = 4 * D * t_arr
r2_sat = L ** 2

fig, ax = plt.subplots(figsize=(8, 5))
ax.fill_between(t_arr, msd_mean - msd_std, msd_mean + msd_std, alpha=0.3, color='blue')
ax.plot(t_arr, msd_mean, 'b-', lw=2, label=rf'$N={N}$ 粒子・排除体積 $\sigma={sigma}$')
ax.plot(t_arr, msd_free, 'k--', lw=1.5, label=r'自由空間 $4Dt$')
ax.axhline(r2_sat, color='gray', ls=':', alpha=0.8, label=rf'飽和目安 $\sim L^2$')
ax.set_xlabel(r'時間 $t$')
ax.set_ylabel(r'$\langle r^2 \rangle$')
ax.set_title('複数粒子・排除体積（周期境界）')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figures/multiparticle.png', dpi=150)
plt.close()
print("multiparticle.png を保存しました。")
