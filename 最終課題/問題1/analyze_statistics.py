"""
統計上の考察：正規分布・エネルギー分布の K-S 検定、拡散係数の誤差評価。
速度成分 vx, vy のガウス性検定も行う。
"""
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os
from scipy import stats

plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False

os.makedirs('data', exist_ok=True)
os.makedirs('figures', exist_ok=True)


def simulate_brownian_motion(T, m, gamma, kB=1.0, dt=0.01, n_steps=1000, seed=None):
    if seed is not None:
        np.random.seed(seed)
    rx, ry = 0.0, 0.0
    vx, vy = 0.0, 0.0
    coeff1 = gamma / m
    coeff2 = np.sqrt(2.0 * gamma * kB * T / m)
    vx_arr = []
    vy_arr = []
    for n in range(n_steps + 1):
        vx_arr.append(vx)
        vy_arr.append(vy)
        if n == n_steps:
            break
        eta_x = np.random.normal(0, 1)
        eta_y = np.random.normal(0, 1)
        vx = vx - coeff1 * vx * dt + coeff2 * np.sqrt(dt) * eta_x
        vy = vy - coeff1 * vy * dt + coeff2 * np.sqrt(dt) * eta_y
        rx += vx * dt
        ry += vy * dt
    return np.array(vx_arr), np.array(vy_arr)


def fit_diffusion_coefficient(t, x, y):
    """MSD の長時間傾きから D を推定。"""
    n = len(t)
    t_fit = t[n // 2:]
    msd = x[n // 2:] ** 2 + y[n // 2:] ** 2
    return np.mean(msd / (4.0 * t_fit))


def run_normal_ks_test():
    """Box-Muller 正規乱数に対して K-S 検定。C プログラムを利用。"""
    n_samples = 2000
    path = os.path.join('data', 'normal_rand_ks.dat')
    exe = './normal_rand'
    if not os.path.isfile(exe):
        print("normal_rand が存在しません。numpy で代替します。")
        np.random.seed(42)
        data = np.random.standard_normal(n_samples)
    else:
        with open(path, 'w') as f:
            subprocess.run([exe, str(n_samples)], stdout=f)
        data = np.loadtxt(path)

    ks_stat, p_value = stats.kstest(data, 'norm', args=(0, 1))
    print(f"正規分布 K-S: 統計量={ks_stat:.5f}, p値={p_value:.5f}")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(data, bins=30, density=True, alpha=0.7, color='steelblue', edgecolor='black', label='ヒストグラム')
    x = np.linspace(-3.5, 3.5, 300)
    ax.plot(x, stats.norm.pdf(x, 0, 1), 'r-', lw=2, label=r'理論 $N(0,1)$')
    ax.set_xlabel('値')
    ax.set_ylabel('確率密度')
    ax.set_title(f'正規分布乱数の検定（K-S 検定 $p$ = {p_value:.4f}）')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('figures/normal_rand_ks_test.png', dpi=150)
    plt.close()
    return ks_stat, p_value


def run_energy_ks_test():
    """運動エネルギー分布の指数分布への K-S 検定。"""
    kB, dt, n_steps = 1.0, 0.01, 1000
    T, m, gamma = 1.0, 1.0, 1.0
    n_runs = 20
    energies = []
    for run in range(n_runs):
        vx, vy = simulate_brownian_motion(T, m, gamma, kB, dt, n_steps, seed=run)
        E = 0.5 * m * (vx ** 2 + vy ** 2)
        energies.extend(E)
    energies = np.array(energies)

    scale = kB * T
    ks_stat, p_value = stats.kstest(energies, 'expon', args=(0, scale))
    print(f"エネルギー分布 K-S: 統計量={ks_stat:.5f}, p値={p_value:.5f}")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(energies, bins=40, density=True, alpha=0.7, color='forestgreen', edgecolor='black', label='ヒストグラム')
    E_max = min(energies.max(), 8 * kB * T)
    E_range = np.linspace(1e-6, E_max, 200)
    ax.plot(E_range, (1 / (kB * T)) * np.exp(-E_range / (kB * T)), 'r-', lw=2,
            label=rf'理論 $P(E)\propto\exp(-E/k_B T)$')
    ax.set_xlabel(r'運動エネルギー $E$')
    ax.set_ylabel('確率密度')
    ax.set_title(f'運動エネルギー分布の検定（K-S 検定 $p$ = {p_value:.4f}）')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, E_max)
    plt.tight_layout()
    plt.savefig('figures/energy_distribution_ks_test.png', dpi=150)
    plt.close()
    return ks_stat, p_value


def run_velocity_components_test():
    """vx, vy のガウス性（マクスウェル分布の成分）をヒストグラムで示す。"""
    kB, dt, n_steps = 1.0, 0.01, 1000
    T, m, gamma = 1.0, 1.0, 1.0
    n_runs = 15
    vx_all = []
    vy_all = []
    for run in range(n_runs):
        vx, vy = simulate_brownian_motion(T, m, gamma, kB, dt, n_steps, seed=run)
        vx_all.extend(vx)
        vy_all.extend(vy)
    vx_all = np.array(vx_all)
    vy_all = np.array(vy_all)
    sigma = np.sqrt(kB * T / m)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, v, lab in zip(axes, [vx_all, vy_all], [r'$v_x$', r'$v_y$']):
        ax.hist(v, bins=40, density=True, alpha=0.7, color='teal', edgecolor='black', label='ヒストグラム')
        x = np.linspace(v.min(), v.max(), 200)
        ax.plot(x, stats.norm.pdf(x, 0, sigma), 'r-', lw=2, label=rf'理論 $N(0,\,k_B T/m)$')
        ax.set_xlabel(lab)
        ax.set_ylabel('確率密度')
        ax.legend()
        ax.grid(True, alpha=0.3)
    axes[0].set_title(r'速度成分 $v_x$ の分布')
    axes[1].set_title(r'速度成分 $v_y$ の分布')
    plt.suptitle('速度成分のガウス性（マクスウェル分布）', y=1.02)
    plt.tight_layout()
    plt.savefig('figures/velocity_components_gaussian.png', dpi=150)
    plt.close()


def run_diffusion_error_bars():
    """拡散係数の試行間ばらつき（標準偏差）を評価し、理論値と比較。"""
    kB, dt, n_steps = 1.0, 0.01, 1000
    n_runs = 40

    def sim_traj(T, m, gamma, run):
        vx, vy = simulate_brownian_motion(T, m, gamma, kB, dt, n_steps, seed=run)
        rx = np.zeros(n_steps + 1)
        ry = np.zeros(n_steps + 1)
        rx[0], ry[0] = 0.0, 0.0
        for n in range(n_steps):
            rx[n + 1] = rx[n] + vx[n] * dt
            ry[n + 1] = ry[n] + vy[n] * dt
        t = np.arange(n_steps + 1) * dt
        return t, rx, ry

    T_vals = [0.5, 1.0, 2.0, 5.0]
    m_vals = [0.5, 1.0, 2.0]
    gamma_vals = [0.5, 1.0, 2.0]

    def run_sweep(param_vals, vary='T'):
        D_means, D_stds, D_theory = [], [], []
        for p in param_vals:
            if vary == 'T':
                T, m, gamma = p, 1.0, 1.0
            elif vary == 'm':
                T, m, gamma = 1.0, p, 1.0
            else:
                T, m, gamma = 1.0, 1.0, p
            D_theory.append(kB * T / gamma)
            D_list = []
            for r in range(n_runs):
                t, x, y = sim_traj(T, m, gamma, r)
                D_list.append(fit_diffusion_coefficient(t, x, y))
            D_means.append(np.mean(D_list))
            D_stds.append(np.std(D_list))
        return np.array(D_means), np.array(D_stds), np.array(D_theory), param_vals

    Dm_T, Ds_T, Dt_T, Tv = run_sweep(T_vals, 'T')
    Dm_m, Ds_m, Dt_m, mv = run_sweep(m_vals, 'm')
    Dm_g, Ds_g, Dt_g, gv = run_sweep(gamma_vals, 'gamma')

    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    axes[0].errorbar(Tv, Dm_T, yerr=Ds_T, fmt='bs', capsize=5, label='シミュレーション')
    axes[0].plot(Tv, Dt_T, 'ro-', lw=2, label=r'理論 $D=k_B T/\gamma$')
    axes[0].set_xlabel('温度 $T$')
    axes[0].set_ylabel('拡散係数 $D$')
    axes[0].set_title('温度依存性（誤差棒は試行間標準偏差）')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].errorbar(mv, Dm_m, yerr=Ds_m, fmt='bs', capsize=5, label='シミュレーション')
    axes[1].plot(mv, Dt_m, 'ro-', lw=2, label=r'理論 $D=k_B T/\gamma$')
    axes[1].set_xlabel('質量 $m$')
    axes[1].set_ylabel('拡散係数 $D$')
    axes[1].set_title('質量依存性（誤差棒は試行間標準偏差）')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    axes[2].errorbar(gv, Dm_g, yerr=Ds_g, fmt='bs', capsize=5, label='シミュレーション')
    axes[2].plot(gv, Dt_g, 'ro-', lw=2, label=r'理論 $D=k_B T/\gamma$')
    axes[2].set_xlabel(r'摩擦係数 $\gamma$')
    axes[2].set_ylabel('拡散係数 $D$')
    axes[2].set_title('摩擦係数依存性（誤差棒は試行間標準偏差）')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('figures/diffusion_coefficient_error_bars.png', dpi=150)
    plt.close()
    print("diffusion_coefficient_error_bars.png を保存しました。")


if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    if base:
        os.chdir(base)
    run_normal_ks_test()
    run_energy_ks_test()
    run_velocity_components_test()
    run_diffusion_error_bars()
    print("統計解析・図の生成が完了しました。")
