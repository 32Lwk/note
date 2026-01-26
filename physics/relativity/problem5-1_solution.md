# 問題 5-1 解答: ローレンツ変換による長さと時間の変化

## 問題
ローレンツ変換による長さと時間の変化に関する問題。

## 解答

### (i) 長さの収縮

**問題:** 慣性系の観測者が、長さ1.0 × 10 mのロッドが、その長さの方向に3.0 × 10 km/sの速度で運動しているのを見る。観測者にはロッドはどれだけ短く見えるか。光速c = 3.0 × 10⁵ km/sとする。

**解答:**

与えられた値:
- 静止時の長さ: $L_0 = 1.0 \times 10$ m = 10 m
- 速度: $v = 3.0 \times 10$ km/s = 30 km/s = $3.0 \times 10^4$ m/s
- 光速: $c = 3.0 \times 10^5$ km/s = $3.0 \times 10^8$ m/s

速度比:
$$\beta = \frac{v}{c} = \frac{3.0 \times 10^4}{3.0 \times 10^8} = 1.0 \times 10^{-4}$$

ローレンツ因子（$\beta \ll 1$の近似）:
$$\gamma = \frac{1}{\sqrt{1-\beta^2}} \approx 1 + \frac{\beta^2}{2}$$

観測される長さ（長さの収縮）:
$$L = \frac{L_0}{\gamma} \approx L_0\left(1 - \frac{\beta^2}{2}\right)$$

短くなる長さ:
$$\Delta L = L_0 - L \approx L_0 \frac{\beta^2}{2} = 10 \times \frac{(10^{-4})^2}{2} = 10 \times \frac{10^{-8}}{2} = 5.0 \times 10^{-8} \text{ m}$$

**答え:** $5.0 \times 10^{-8}$ m

---

### (ii) 時間の遅れ

**問題:** ロケットが地球に対して速度Vで飛行している。$(V/c)^2 = 0.99$のとき、ロケットが地球を通過してから地球で1時間経過したとき、ロケット内ではどれだけの時間が経過しているか。

**解答:**

与えられた値:
- $(V/c)^2 = 0.99$
- 地球での経過時間: $\Delta t = 1$ 時間

速度比:
$$\frac{V}{c} = \sqrt{0.99} \approx 0.995$$

ローレンツ因子:
$$\gamma = \frac{1}{\sqrt{1-(V/c)^2}} = \frac{1}{\sqrt{1-0.99}} = \frac{1}{\sqrt{0.01}} = \frac{1}{0.1} = 10$$

ロケット内の時間（時間の遅れ）:
$$\Delta t' = \frac{\Delta t}{\gamma} = \frac{1}{10} = 0.1 \text{ 時間} = 6 \text{ 分}$$

**答え:** 0.1時間（6分）

---

### (iii) ミュー粒子の寿命

**問題:** 宇宙線が大気中の原子と衝突して生成されるミュー粒子は、自然に電子とニュートリノに崩壊する。静止時の半減期は$1.5 \times 10^{-6}$秒である。地球表面から約$2.0 \times 10$ kmの高さで生成されたミュー粒子が、地球表面に到達するまでに初期の数の1/4に減少した。ミュー粒子の速度をV、光速をc、$\beta = V/c$とするとき、$1-\beta$の値を求めよ。答えは有効数字1桁で。

**解答:**

与えられた値:
- 静止時の半減期: $\tau_0 = 1.5 \times 10^{-6}$ 秒
- 移動距離: $d = 2.0 \times 10$ km = $2.0 \times 10^4$ m
- 粒子数の減少: $N/N_0 = 1/4$

崩壊の法則:
$$N = N_0 e^{-t/\tau}$$

ここで、$t$は粒子の静止系での経過時間、$\tau$は平均寿命である。

半減期と平均寿命の関係:
$$\tau = \frac{\tau_{1/2}}{\ln 2} = \frac{1.5 \times 10^{-6}}{\ln 2} \approx 2.16 \times 10^{-6} \text{ 秒}$$

粒子数が1/4になる条件:
$$\frac{N}{N_0} = e^{-t/\tau} = \frac{1}{4}$$

$$t = \tau \ln 4 = 2.16 \times 10^{-6} \times \ln 4 \approx 2.16 \times 10^{-6} \times 1.386 \approx 3.0 \times 10^{-6} \text{ 秒}$$

地球系での経過時間:
$$T = \frac{d}{V} = \frac{2.0 \times 10^4}{V}$$

時間の遅れの関係:
$$t = \frac{T}{\gamma} = T\sqrt{1-\beta^2} = \frac{d}{V}\sqrt{1-\beta^2}$$

したがって:
$$3.0 \times 10^{-6} = \frac{2.0 \times 10^4}{V}\sqrt{1-\beta^2}$$

$$V = \frac{2.0 \times 10^4}{3.0 \times 10^{-6}}\sqrt{1-\beta^2} = \frac{2.0 \times 10^{10}}{3.0}\sqrt{1-\beta^2}$$

$\beta = V/c$より:
$$\beta c = \frac{2.0 \times 10^{10}}{3.0}\sqrt{1-\beta^2}$$

$$c = 3.0 \times 10^8 \text{ m/s}$$として:

$$\beta = \frac{2.0 \times 10^{10}}{3.0 \times 10^8 \times 3.0}\sqrt{1-\beta^2} = \frac{2.0 \times 10^2}{9.0}\sqrt{1-\beta^2} \approx 22.2\sqrt{1-\beta^2}$$

これは$\beta$が1に非常に近いことを示している。$\beta \approx 1$の近似を使うと、$1-\beta^2 = (1-\beta)(1+\beta) \approx 2(1-\beta)$

より正確に計算するため、別のアプローチを取る。

時間の遅れから:
$$t = T\sqrt{1-\beta^2}$$

$$T = \frac{d}{V} = \frac{d}{\beta c}$$

$$t = \frac{d}{\beta c}\sqrt{1-\beta^2}$$

$$t\beta c = d\sqrt{1-\beta^2}$$

両辺を2乗:
$$t^2\beta^2 c^2 = d^2(1-\beta^2)$$

$$t^2\beta^2 c^2 = d^2 - d^2\beta^2$$

$$t^2\beta^2 c^2 + d^2\beta^2 = d^2$$

$$\beta^2(t^2 c^2 + d^2) = d^2$$

$$\beta^2 = \frac{d^2}{t^2 c^2 + d^2}$$

数値を代入:
- $d = 2.0 \times 10^4$ m
- $t = 3.0 \times 10^{-6}$ s
- $c = 3.0 \times 10^8$ m/s

$$t^2 c^2 = (3.0 \times 10^{-6})^2 \times (3.0 \times 10^8)^2 = 9.0 \times 10^{-12} \times 9.0 \times 10^{16} = 8.1 \times 10^5$$

$$d^2 = (2.0 \times 10^4)^2 = 4.0 \times 10^8$$

$$t^2 c^2 + d^2 = 8.1 \times 10^5 + 4.0 \times 10^8 \approx 4.0 \times 10^8$$

$$\beta^2 = \frac{4.0 \times 10^8}{4.0 \times 10^8} \approx 1.0$$

より正確に:
$$\beta^2 = \frac{4.0 \times 10^8}{4.0081 \times 10^8} \approx 0.998$$

$$\beta \approx 0.999$$

$$1-\beta \approx 1 - 0.999 = 0.001 = 1 \times 10^{-3}$$

有効数字1桁で:
**答え:** $1-\beta = 1 \times 10^{-3}$

---

### (iv) 同時刻の相対性

**問題:** 慣性系Oにおいて、x軸上で9.0 × 10³ km離れた2つの位置で、時刻t=0に同時に2つのライトが点灯した。この事象を、O系に対してx軸の正の方向に光速の80%の速度で運動しているO'系から観測する。2つのライトはO系に対して静止している。

**(a) O'系では、2つのライトは異なる時刻に点灯したように見える。この時刻差を求めよ。光速c = 3.0 × 10⁵ km/sとする。**

**解答:**

ローレンツ変換を用いる。

与えられた値:
- O系での距離: $\Delta x = 9.0 \times 10^3$ km = $9.0 \times 10^6$ m
- O系での時刻差: $\Delta t = 0$
- O'系の速度: $v = 0.8c$
- 光速: $c = 3.0 \times 10^5$ km/s = $3.0 \times 10^8$ m/s

ローレンツ変換:
$$t' = \gamma\left(t - \frac{vx}{c^2}\right)$$

2つの事象（ライト1とライト2）について:
- 事象1: $(x_1, t_1 = 0)$
- 事象2: $(x_2, t_2 = 0)$、ただし $x_2 - x_1 = \Delta x$

O'系での時刻:
$$t'_1 = \gamma\left(0 - \frac{vx_1}{c^2}\right) = -\gamma\frac{vx_1}{c^2}$$

$$t'_2 = \gamma\left(0 - \frac{vx_2}{c^2}\right) = -\gamma\frac{vx_2}{c^2}$$

時刻差:
$$\Delta t' = t'_2 - t'_1 = -\gamma\frac{v(x_2 - x_1)}{c^2} = -\gamma\frac{v\Delta x}{c^2}$$

ローレンツ因子:
$$\gamma = \frac{1}{\sqrt{1-\beta^2}} = \frac{1}{\sqrt{1-0.8^2}} = \frac{1}{\sqrt{1-0.64}} = \frac{1}{\sqrt{0.36}} = \frac{1}{0.6} = \frac{5}{3}$$

数値を代入:
$$\Delta t' = -\frac{5}{3} \times \frac{0.8c \times 9.0 \times 10^6}{c^2} = -\frac{5}{3} \times \frac{0.8 \times 9.0 \times 10^6}{3.0 \times 10^8}$$

$$= -\frac{5}{3} \times \frac{7.2 \times 10^6}{3.0 \times 10^8} = -\frac{5}{3} \times 2.4 \times 10^{-2} = -\frac{12}{3} \times 10^{-2} = -4.0 \times 10^{-2} \text{ 秒}$$

負の符号は、O'系から見て、より後方（負のx方向）のライトが先に点灯したように見えることを意味する。

**答え:** $4.0 \times 10^{-2}$ 秒（絶対値）

---

**(b) O'系では、ライトが点灯した瞬間の2つのライトの位置間の距離はいくらか。**

**解答:**

長さの収縮を考慮する。

O系での距離: $\Delta x = 9.0 \times 10^3$ km

O'系での距離（長さの収縮）:
$$\Delta x' = \frac{\Delta x}{\gamma} = \frac{9.0 \times 10^3}{5/3} = 9.0 \times 10^3 \times \frac{3}{5} = 5.4 \times 10^3 \text{ km}$$

**答え:** $5.4 \times 10^3$ km

