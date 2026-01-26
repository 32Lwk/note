"""
外力下のブラウン運動：一定力 F を x 方向に加えた場合のドリフト＋拡散。
<m dv/dt = -γ v + F + ξ> → 定常ドリフト v_drift = F/γ, <x> = (F/γ)t,
変動は拡散と同じ D = k_B T/γ。
"""
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False


def simulate_drift_diffusion(T, m, gamma, F, kB=1.0, dt=0.01, n_steps=1000, seed=None):
    """m dv/dt = -γ v + F + ξ, 力は x 方向のみ。"""
    if seed is not None:
        np.random.seed(seed)
    rx, ry = 0.0, 0.0
    vx, vy = 0.0, 0.0
    coeff1 = gamma / m
    coeff2 = np.sqrt(2.0 * gamma * kB * T / m)
    drift_coeff = F / m * dt
    t = np.arange(n_steps + 1) * dt
    x = np.zeros(n_steps + 1)
    y = np.zeros(n_steps + 1)
    x[0], y[0] = 0.0, 0.0
    for n in range(n_steps):
        eta_x = np.random.normal(0, 1)
        eta_y = np.random.normal(0, 1)
        vx = vx - coeff1 * vx * dt + drift_coeff + coeff2 * np.sqrt(dt) * eta_x
        vy = vy - coeff1 * vy * dt + coeff2 * np.sqrt(dt) * eta_y
        rx += vx * dt
        ry += vy * dt
        x[n + 1] = rx
        y[n + 1] = ry
    return t, x, y


os.makedirs('figures', exist_ok=True)

kB, dt, n_steps, n_runs = 1.0, 0.01, 1000, 50
T, m, gamma = 1.0, 1.0, 1.0
F = 0.5
v_drift = F / gamma
D = kB * T / gamma

trajectories = []
for run in range(n_runs):
    t, x, y = simulate_drift_diffusion(T, m, gamma, F, kB, dt, n_steps, seed=run)
    trajectories.append((t, x, y))

t_arr = trajectories[0][0]
x_mean = np.mean([tr[1] for tr in trajectories], axis=0)
y_mean = np.mean([tr[2] for tr in trajectories], axis=0)
x_var = np.var([tr[1] for tr in trajectories], axis=0)
y_var = np.var([tr[2] for tr in trajectories], axis=0)
# 理論: <x> = v_drift * t, Var(x) ≈ 2 D t (長時間), Var(y) ≈ 2 D t
x_theory = v_drift * t_arr
var_theory = 2.0 * D * t_arr

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 左: 軌道のサンプル数本 + 平均
ax = axes[0]
for i, (_, x, y) in enumerate(trajectories[:8]):
    ax.plot(x, y, '-', alpha=0.5, color='steelblue')
ax.plot(x_mean, y_mean, 'r-', lw=2.5, label=r'平均 $\langle \mathbf{r} \rangle$')
ax.plot(x_mean[0], y_mean[0], 'ko', ms=8, label='原点')
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_title(r'外力 $F_x = F$ 下の軌道（$F = {:.2f}$）'.format(F))
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

# 右: <x>(t), Var(x)(t), Var(y)(t)
ax = axes[1]
ax.plot(t_arr, x_mean, 'b-', lw=2, label=r'$\langle x \rangle$ シミュレーション')
ax.plot(t_arr, x_theory, 'b--', lw=1.5, label=r'理論 $\langle x \rangle = (F/\gamma)t$')
ax.plot(t_arr, x_var, 'g-', lw=2, label=r'$\mathrm{Var}(x)$')
ax.plot(t_arr, y_var, 'orange', lw=2, alpha=0.9, label=r'$\mathrm{Var}(y)$')
ax.plot(t_arr, var_theory, 'k--', lw=1.5, label=r'理論 $\mathrm{Var} \approx 2Dt$')
ax.set_xlabel(r'時間 $t$')
ax.set_ylabel(r'$\langle x \rangle$ / $\mathrm{Var}$')
ax.set_title('ドリフトと分散の時間発展')
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figures/drift_diffusion.png', dpi=150)
plt.close()
print("drift_diffusion.png を保存しました。")
