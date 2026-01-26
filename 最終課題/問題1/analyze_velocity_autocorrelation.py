"""
速度自己相関関数 C(t) = <v(0)·v(t)> の計算と理論との比較。
Green-Kubo関係による拡散係数の導出も行う。
"""
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False


def simulate_brownian_motion_with_velocity(T, m, gamma, kB=1.0, dt=0.01, n_steps=1000, seed=None):
    """位置と速度の時系列を返す。"""
    if seed is not None:
        np.random.seed(seed)
    rx, ry = 0.0, 0.0
    vx, vy = 0.0, 0.0
    coeff1 = gamma / m
    coeff2 = np.sqrt(2.0 * gamma * kB * T / m)
    t = np.zeros(n_steps + 1)
    x = np.zeros(n_steps + 1)
    y = np.zeros(n_steps + 1)
    vx_arr = np.zeros(n_steps + 1)
    vy_arr = np.zeros(n_steps + 1)
    t[0] = 0.0
    x[0] = rx
    y[0] = ry
    vx_arr[0] = vx
    vy_arr[0] = vy
    for n in range(n_steps):
        eta_x = np.random.normal(0, 1)
        eta_y = np.random.normal(0, 1)
        vx = vx - coeff1 * vx * dt + coeff2 * np.sqrt(dt) * eta_x
        vy = vy - coeff1 * vy * dt + coeff2 * np.sqrt(dt) * eta_y
        rx += vx * dt
        ry += vy * dt
        t[n + 1] = (n + 1) * dt
        x[n + 1] = rx
        y[n + 1] = ry
        vx_arr[n + 1] = vx
        vy_arr[n + 1] = vy
    return t, x, y, vx_arr, vy_arr


def compute_velocity_autocorrelation(vx_list, vy_list):
    """
    複数軌道から速度自己相関 C(tau) = <v(0)·v(tau)> を計算。
    各軌道で C_i(tau) = (1/(L-tau)) sum_t [ vx(t)vx(t+tau) + vy(t)vy(t+tau) ] を求め、 run 平均。
    """
    L = len(vx_list[0])
    max_tau = L // 2  # 相関が減衰する範囲で十分
    n_runs = len(vx_list)
    C = np.zeros(max_tau)
    for tau in range(max_tau):
        s = 0.0
        count = 0
        for run in range(n_runs):
            vx = vx_list[run]
            vy = vy_list[run]
            for t in range(L - tau):
                s += vx[t] * vx[t + tau] + vy[t] * vy[t + tau]
                count += 1
        C[tau] = s / count if count > 0 else 0.0
    return C


def green_kubo_D(C, dt, m, kB, T):
    """
    Green-Kubo: D = (1/2) ∫_0^∞ <v(0)·v(t)> dt
    数値的には D ≈ (1/2) * sum_tau C(tau) * dt。減衰完了まで積分。
    """
    integ = np.sum(C) * dt
    return 0.5 * integ


os.makedirs('figures', exist_ok=True)

kB, dt, n_steps, n_runs = 1.0, 0.01, 1000, 30
T, m, gamma = 1.0, 1.0, 1.0
tau_relax = m / gamma  # 緩和時間

vx_list = []
vy_list = []
for run in range(n_runs):
    _, _, _, vx, vy = simulate_brownian_motion_with_velocity(T, m, gamma, kB, dt, n_steps, seed=run)
    vx_list.append(vx)
    vy_list.append(vy)

C = compute_velocity_autocorrelation(vx_list, vy_list)
tau_arr = np.arange(len(C)) * dt
C0_theory = 2.0 * kB * T / m  # 2次元等分配
C_norm = C / C[0] if C[0] != 0 else C / (C0_theory + 1e-12)
theory = np.exp(-gamma / m * tau_arr)

# Green-Kubo による D
D_gk = green_kubo_D(C, dt, m, kB, T)
D_einstein = kB * T / gamma
print(f"Green-Kubo D = {D_gk:.6f}, Einstein D = k_B T/γ = {D_einstein:.6f}")

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(tau_arr, C_norm, 'b-', linewidth=2, label=r'シミュレーション $C(t)/C(0)$')
ax.plot(tau_arr, theory, 'r--', linewidth=2, label=r'理論 $\exp(-\gamma t/m)$')
ax.axvline(tau_relax, color='gray', linestyle=':', label=rf'緩和時間 $\tau=m/\gamma={tau_relax:.2f}$')
ax.set_xlabel(r'時間 $t$')
ax.set_ylabel(r'$C(t)\,/\,C(0)$')
ax.set_title('速度自己相関関数と理論との比較')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_xlim(0, min(tau_arr[-1], 5 * tau_relax))
plt.tight_layout()
plt.savefig('figures/velocity_autocorrelation.png', dpi=150)
plt.close()

print("velocity_autocorrelation.png を保存しました。")
