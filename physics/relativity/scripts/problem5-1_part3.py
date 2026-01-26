#!/usr/bin/env python3
"""
問題 5-1 (iii): ミュー粒子の寿命と速度の計算
"""

import numpy as np

# 定数
c = 3.0e8  # 光速 [m/s]
tau_half = 1.5e-6  # 静止時の半減期 [s]
d = 2.0e4  # 移動距離 [m] (2.0 × 10 km)
N_N0 = 1.0 / 4.0  # 粒子数の比

print("=" * 60)
print("問題 5-1 (iii): ミュー粒子の寿命と速度の計算")
print("=" * 60)
print()

# 1. 平均寿命の計算
# 半減期と平均寿命の関係: τ = τ_{1/2} / ln(2)
tau = tau_half / np.log(2)
print(f"1. 平均寿命の計算")
print(f"   半減期: τ_{1/2} = {tau_half:.2e} s")
print(f"   平均寿命: τ = τ_{1/2} / ln(2) = {tau:.2e} s")
print()

# 2. 粒子数が1/4になるまでの時間
# N = N₀ e^(-t/τ) = N₀/4 より
# e^(-t/τ) = 1/4
# -t/τ = ln(1/4) = -ln(4)
# t = τ ln(4)
t = tau * np.log(4)
print(f"2. 粒子数が1/4になるまでの時間")
print(f"   N/N₀ = e^(-t/τ) = 1/4")
print(f"   t = τ ln(4) = {tau:.2e} × {np.log(4):.4f} = {t:.2e} s")
print()

# 3. 時間の遅れの関係からβを求める
# 時間の遅れ: t = T√(1-β²)
# 地球系での経過時間: T = d/V = d/(βc)
# したがって: t = (d/(βc))√(1-β²)
# 両辺を2乗: t²β²c² = d²(1-β²)
# 整理: β²(t²c² + d²) = d²
# よって: β² = d²/(t²c² + d²)

t_squared_c_squared = t**2 * c**2
d_squared = d**2
denominator = t_squared_c_squared + d_squared
beta_squared = d_squared / denominator
beta = np.sqrt(beta_squared)

print(f"3. 速度比βの計算")
print(f"   時間の遅れの関係: t = (d/(βc))√(1-β²)")
print(f"   両辺を2乗して整理: β² = d²/(t²c² + d²)")
print()
print(f"   計算過程:")
print(f"   t²c² = ({t:.2e})² × ({c:.2e})²")
print(f"        = {t**2:.2e} × {c**2:.2e}")
print(f"        = {t_squared_c_squared:.2e}")
print(f"   d² = ({d:.2e})² = {d_squared:.2e}")
print(f"   t²c² + d² = {t_squared_c_squared:.2e} + {d_squared:.2e}")
print(f"              = {denominator:.2e}")
print(f"   β² = {d_squared:.2e} / {denominator:.2e}")
print(f"      = {beta_squared:.6f}")
print(f"   β = √({beta_squared:.6f}) = {beta:.6f}")
print()

# 4. 1-βの計算
one_minus_beta = 1.0 - beta
print(f"4. 1-βの値")
print(f"   1-β = 1 - {beta:.6f} = {one_minus_beta:.6e}")
print()

# 有効数字1桁で表示
one_minus_beta_1sig = round(one_minus_beta, -int(np.floor(np.log10(abs(one_minus_beta)))))
print(f"5. 答え（有効数字1桁）")
print(f"   1-β = {one_minus_beta_1sig:.1e}")
print()

# 補足情報
V = beta * c
gamma = 1.0 / np.sqrt(1 - beta_squared)
T_earth = d / V

print(f"補足情報:")
print(f"   ミュー粒子の速度: V = βc = {beta:.6f} × {c:.2e} = {V:.2e} m/s")
print(f"   ローレンツ因子: γ = {gamma:.2f}")
print(f"   地球系での経過時間: T = d/V = {d:.2e} / {V:.2e} = {T_earth:.2e} s")
print(f"   時間の遅れの確認: t = T/γ = {T_earth:.2e} / {gamma:.2f} = {T_earth/gamma:.2e} s")
print("=" * 60)

