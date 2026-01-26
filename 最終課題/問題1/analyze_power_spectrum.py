"""
速度のパワースペクトル：VAC のフーリエ変換は Lorentz 型。
揺動散逸定理と結びつく。S(ω) ∝ 1/(ω² + (γ/m)²)
"""
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False


def simulate_with_velocity(T, m, gamma, kB=1.0, dt=0.01, n_steps=2000, seed=None):
    if seed is not None:
        np.random.seed(seed)
    rx, ry = 0.0, 0.0
    vx, vy = 0.0, 0.0
    c1 = gamma / m
    c2 = np.sqrt(2.0 * gamma * kB * T / m)
    vx_arr = np.zeros(n_steps + 1)
    vy_arr = np.zeros(n_steps + 1)
    for n in range(n_steps):
        vx_arr[n] = vx
        vy_arr[n] = vy
        eta_x = np.random.normal(0, 1)
        eta_y = np.random.normal(0, 1)
        vx = vx - c1 * vx * dt + c2 * np.sqrt(dt) * eta_x
        vy = vy - c1 * vy * dt + c2 * np.sqrt(dt) * eta_y
        rx += vx * dt
        ry += vy * dt
    vx_arr[n_steps] = vx
    vy_arr[n_steps] = vy
    return vx_arr, vy_arr


def compute_vac(vx, vy):
    L = len(vx)
    max_tau = min(L // 2, 500)
    C = np.zeros(max_tau)
    for tau in range(max_tau):
        n = L - tau
        C[tau] = np.mean(vx[:n] * vx[tau:tau + n] + vy[:n] * vy[tau:tau + n])
    return C


os.makedirs('figures', exist_ok=True)

kB, dt, n_steps, n_runs = 1.0, 0.01, 2000, 40
T, m, gamma = 1.0, 1.0, 1.0
lam = gamma / m  # 1/緩和時間

vac_list = []
for r in range(n_runs):
    vx, vy = simulate_with_velocity(T, m, gamma, kB, dt, n_steps, seed=r)
    C = compute_vac(vx, vy)
    vac_list.append(C)
C_mean = np.mean(vac_list, axis=0)
tau_arr = np.arange(len(C_mean)) * dt

# パワースペクトル: VAC の FFT。実部が S(ω)。
n_fft = 4096
C_pad = np.zeros(n_fft)
C_pad[: len(C_mean)] = C_mean
ft = np.fft.rfft(C_pad) * dt
freq = np.fft.rfftfreq(n_fft, dt)
S = np.real(ft)
# 理論 Lorentz: S(ω) ∝ 2 C(0) τ / (1 + (ωτ)²), τ = m/γ
tau_relax = m / gamma
C0 = 2.0 * kB * T / m
S_theory = 2.0 * C0 * tau_relax / (1.0 + (2 * np.pi * freq * tau_relax) ** 2)
# 定数倍を合わせる（高さを揃える）
mask = (freq > 0.01) & (freq < 2.0)
if np.max(S_theory[mask]) > 0:
    scale = np.max(S[mask]) / np.max(S_theory[mask])
    S_theory = S_theory * scale

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
ax = axes[0]
ax.plot(tau_arr, C_mean, 'b-', lw=2, label=r'VAC $\langle \mathbf{v}(0)\cdot\mathbf{v}(t) \rangle$')
ax.axhline(0, color='gray', ls=':')
ax.set_xlabel(r'時間 $t$')
ax.set_ylabel(r'$C(t)$')
ax.set_title('速度自己相関関数')
ax.legend()
ax.grid(True, alpha=0.3)

ax = axes[1]
mask = (freq > 0) & (freq < 3.0)
ax.semilogy(2 * np.pi * freq[mask], np.maximum(S[mask], 1e-12), 'b-', lw=2, label='シミュレーション（FFT of VAC）')
ax.semilogy(2 * np.pi * freq[mask], S_theory[mask], 'r--', lw=2, label=r'理論 Lorentz $S \propto 1/(\omega^2 + (\gamma/m)^2)$')
ax.set_xlabel(r'角周波数 $\omega$')
ax.set_ylabel(r'パワースペクトル $S(\omega)$')
ax.set_title('速度のパワースペクトル（揺動散逸）')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figures/power_spectrum.png', dpi=150)
plt.close()
print("power_spectrum.png を保存しました。")
