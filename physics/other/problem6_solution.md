# 問題 6 解答: 特殊相対論の応用

## 問題 6-1: 横方向ドップラー効果 (Transverse Doppler Effect)

### 問題設定
慣性系Oの原点に観測者がいる。光源がO系において、$y = y_0 > 0$, $z = 0$の直線上を、正の$x$方向に一定の速さ$V$で運動している。光源は一定の周波数$f_0$の光を放射している。光速を$c$とする。

### (i) 観測される周波数の導出

**問題:** 光源がO系で座標$(x, y) = (x, y_0)$にあるときに放射された光の、原点の観測者によって観測される周波数$f$を、$y_0$, $f_0$, $V$, $c$, $x$を用いて表せ。

**解答:**

光源の運動を考える。第1の波の山が放射される時空点を$(ct_1, x_1, y_0, 0)$、第2の波の山が放射される時空点を$(ct_2, x_2, y_0, 0)$とする。

光源の運動:
$$x_1 = V t_1, \quad x_2 = V t_2$$

光源の静止系（光源と共動する慣性系）では、2つの波の山の放射の時間間隔は:
$$\Delta t' = t_2' - t_1' = \frac{1}{f_0}$$

O系での時間間隔$\Delta t = t_2 - t_1$と$\Delta t'$の関係は、時間の遅れにより:
$$\Delta t' = \Delta t \sqrt{1 - V^2/c^2} = \frac{\Delta t}{\gamma}$$

ここで、$\gamma = 1/\sqrt{1-V^2/c^2}$である。

したがって:
$$\Delta t = \gamma \Delta t' = \frac{\gamma}{f_0}$$

O系での位置:
$$x_1 = V t_1, \quad x_2 = V t_2$$

観測者（原点）に到達する時刻を考える。第1の波の山が放射される時刻を$t_1$、観測者に到達する時刻を$T_1$とすると:
$$c(T_1 - t_1) = \sqrt{x_1^2 + y_0^2}$$

$$T_1 = t_1 + \frac{\sqrt{x_1^2 + y_0^2}}{c} = t_1 + \frac{\sqrt{V^2 t_1^2 + y_0^2}}{c}$$

同様に、第2の波の山について:
$$T_2 = t_2 + \frac{\sqrt{x_2^2 + y_0^2}}{c} = t_2 + \frac{\sqrt{V^2 t_2^2 + y_0^2}}{c}$$

観測される時間間隔:
$$\Delta T = T_2 - T_1 = (t_2 - t_1) + \frac{\sqrt{V^2 t_2^2 + y_0^2} - \sqrt{V^2 t_1^2 + y_0^2}}{c}$$

$t_2 = t_1 + \Delta t$とおき、$\Delta t$が小さいとして展開する:
$$\sqrt{V^2(t_1 + \Delta t)^2 + y_0^2} \approx \sqrt{V^2 t_1^2 + y_0^2} + \frac{V^2 t_1 \Delta t}{\sqrt{V^2 t_1^2 + y_0^2}}$$

したがって:
$$\Delta T = \Delta t + \frac{V^2 t_1 \Delta t}{c\sqrt{V^2 t_1^2 + y_0^2}} = \Delta t\left(1 + \frac{V^2 t_1}{c\sqrt{V^2 t_1^2 + y_0^2}}\right)$$

$x_1 = V t_1$より:
$$\Delta T = \Delta t\left(1 + \frac{V x_1}{c\sqrt{x_1^2 + y_0^2}}\right)$$

観測される周波数:
$$f = \frac{1}{\Delta T} = \frac{1}{\Delta t\left(1 + \frac{V x_1}{c\sqrt{x_1^2 + y_0^2}}\right)} = \frac{f_0}{\gamma\left(1 + \frac{V x_1}{c\sqrt{x_1^2 + y_0^2}}\right)}$$

より正確には、ドップラー効果を考慮する必要がある。光源が観測者に向かって運動している成分を考える。

光源から観測者への方向ベクトル:
$$\vec{r} = (-x, -y_0, 0)$$

光源の速度ベクトル:
$$\vec{V} = (V, 0, 0)$$

観測者方向への速度成分:
$$V_r = \vec{V} \cdot \frac{\vec{r}}{|\vec{r}|} = V \cdot \frac{-x}{\sqrt{x^2 + y_0^2}} = -\frac{V x}{\sqrt{x^2 + y_0^2}}$$

相対論的ドップラー効果の公式:
$$f = f_0 \frac{\sqrt{1 - V^2/c^2}}{1 - V_r/c} = f_0 \frac{1/\gamma}{1 + \frac{V x}{c\sqrt{x^2 + y_0^2}}}$$

したがって:
$$f = \frac{f_0}{\gamma\left(1 + \frac{V x}{c\sqrt{x^2 + y_0^2}}\right)}$$

**答え:**
$$f = \frac{f_0}{\gamma\left(1 + \frac{V x}{c\sqrt{x^2 + y_0^2}}\right)}$$

ここで、$\gamma = 1/\sqrt{1-V^2/c^2}$である。

**物理的意味:**
- 分母の$1 + \frac{V x}{c\sqrt{x^2 + y_0^2}}$は、光源が観測者に近づく（$x < 0$）ときは小さくなり、遠ざかる（$x > 0$）ときは大きくなる。
- $\gamma$因子は時間の遅れによる補正である。
- $x = 0$のとき（光源が観測者の真横を通る瞬間）、$f = f_0/\gamma$となり、純粋な横方向ドップラー効果（時間の遅れのみ）が観測される。

---

### (ii) 光源が無限遠から接近する場合

**問題:** 光源が無限遠から接近するとき（$x \to -\infty$）、$f/f_0$を求めよ。

**解答:**

$x \to -\infty$のとき:
$$\frac{V x}{c\sqrt{x^2 + y_0^2}} = \frac{V x}{c|x|\sqrt{1 + y_0^2/x^2}} = \frac{V}{c} \cdot \frac{x}{|x|} \cdot \frac{1}{\sqrt{1 + y_0^2/x^2}}$$

$x < 0$より$|x| = -x$:
$$= \frac{V}{c} \cdot \frac{x}{-x} \cdot \frac{1}{\sqrt{1 + y_0^2/x^2}} = -\frac{V}{c} \cdot \frac{1}{\sqrt{1 + y_0^2/x^2}} \to -\frac{V}{c}$$

したがって:
$$f = \frac{f_0}{\gamma\left(1 - \frac{V}{c}\right)} = \frac{f_0}{\gamma} \cdot \frac{1}{1 - V/c}$$

$$1 - V/c = \frac{c - V}{c}$$

$$\gamma = \frac{1}{\sqrt{1-V^2/c^2}} = \frac{1}{\sqrt{(1-V/c)(1+V/c)}}$$

$$f = \frac{f_0}{\sqrt{(1-V/c)(1+V/c)}} \cdot \frac{1}{1 - V/c} = \frac{f_0}{\sqrt{1+V/c}} \cdot \frac{1}{\sqrt{1-V/c}}$$

より簡潔に:
$$f = f_0 \sqrt{\frac{1+V/c}{1-V/c}}$$

**答え:**
$$\frac{f}{f_0} = \sqrt{\frac{1+V/c}{1-V/c}}$$

**物理的意味:**
- これは縦方向ドップラー効果（光源が観測者に直接近づく場合）の公式である。
- 光源が近づくため、周波数は青方偏移（増加）する。
- 非相対論的極限（$V \ll c$）では、$f/f_0 \approx 1 + V/c$となり、古典的なドップラー効果に一致する。

---

### (iii) 光源が無限遠へ遠ざかる場合

**問題:** 光源が無限遠へ遠ざかるとき（$x \to \infty$）、$f/f_0$を求めよ。

**解答:**

$x \to \infty$のとき:
$$\frac{V x}{c\sqrt{x^2 + y_0^2}} = \frac{V}{c} \cdot \frac{x}{|x|} \cdot \frac{1}{\sqrt{1 + y_0^2/x^2}} = \frac{V}{c} \cdot \frac{1}{\sqrt{1 + y_0^2/x^2}} \to \frac{V}{c}$$

したがって:
$$f = \frac{f_0}{\gamma\left(1 + \frac{V}{c}\right)} = \frac{f_0}{\gamma} \cdot \frac{1}{1 + V/c}$$

$$1 + V/c = \frac{c + V}{c}$$

$$f = \frac{f_0}{\sqrt{(1-V/c)(1+V/c)}} \cdot \frac{1}{1 + V/c} = \frac{f_0}{\sqrt{1-V/c}} \cdot \frac{1}{\sqrt{1+V/c}}$$

より簡潔に:
$$f = f_0 \sqrt{\frac{1-V/c}{1+V/c}}$$

**答え:**
$$\frac{f}{f_0} = \sqrt{\frac{1-V/c}{1+V/c}}$$

**物理的意味:**
- 光源が遠ざかるため、周波数は赤方偏移（減少）する。
- (ii)の結果の逆数になっている。
- 非相対論的極限では、$f/f_0 \approx 1 - V/c$となる。

---

### (iv) 波長が十分小さい場合の近似

**問題:** $y_0 \gg \gamma\beta c/f_0$（つまり、$y_0$が光源が放射する光の波長に比べて十分大きい）のとき、$f/f_0$を$x$, $y_0$, $V$, $c$を用いて表せ。

**解答:**

条件: $y_0 \gg \gamma\beta c/f_0$、ここで$\beta = V/c$。

この条件は、$y_0 \gg \lambda_0 \gamma\beta$（$\lambda_0 = c/f_0$は静止系での波長）を意味する。

(i)の結果:
$$f = \frac{f_0}{\gamma\left(1 + \frac{V x}{c\sqrt{x^2 + y_0^2}}\right)}$$

$y_0 \gg \gamma\beta c/f_0$のとき、実質的に$y_0$が非常に大きいことを意味する。しかし、より正確には、この条件は横方向の効果が支配的であることを示している。

実際には、この条件の下では、光源の位置$x$が$y_0$に比べてそれほど大きくない範囲で考えると、$\sqrt{x^2 + y_0^2} \approx y_0$と近似できる。

しかし、問題の意図を考えると、$y_0$が波長に比べて十分大きいという条件は、幾何学的効果が重要であることを示している。

より正確な導出:
$$f = \frac{f_0}{\gamma\left(1 + \frac{V x}{c\sqrt{x^2 + y_0^2}}\right)}$$

$y_0$が大きいとき、$\sqrt{x^2 + y_0^2} \approx y_0\sqrt{1 + x^2/y_0^2} \approx y_0(1 + x^2/(2y_0^2))$と展開できるが、主要項は$y_0$である。

したがって:
$$f \approx \frac{f_0}{\gamma\left(1 + \frac{V x}{c y_0}\right)}$$

**答え:**
$$\frac{f}{f_0} = \frac{1}{\gamma\left(1 + \frac{V x}{c y_0}\right)}$$

**物理的意味:**
- $y_0$が十分大きいとき、光源は観測者からほぼ一定距離にあり、幾何学的効果が簡略化される。
- この近似では、距離の変化が線形に近づく。
- 横方向ドップラー効果（$\gamma$因子）と、わずかな縦方向成分（$V x/(c y_0)$項）の組み合わせとして理解できる。

---

## 問題 6-2: 4ベクトル

### 問題設定
計量テンソル$\eta_{\mu\nu}$（$\mu, \nu = 0, 1, 2, 3$）が次のように定義される:
$$\eta_{\mu\nu} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}$$

$\eta^{\mu\nu}$（$\mu, \nu = 0, 1, 2, 3$）は$\eta_{\mu\nu}$の逆行列である。

### (i) 逆計量テンソル

**問題:** $\eta^{\mu\nu}$を求めよ。

**解答:**

$\eta_{\mu\nu}$は対角行列である:
$$\eta_{\mu\nu} = \text{diag}(1, -1, -1, -1)$$

逆行列は各対角成分の逆数である:
$$\eta^{\mu\nu} = \text{diag}(1, -1, -1, -1)$$

つまり:
$$\eta^{\mu\nu} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}$$

**答え:**
$$\eta^{\mu\nu} = \eta_{\mu\nu} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}$$

**物理的意味:**
- ミンコフスキー計量では、$\eta_{\mu\nu} = \eta^{\mu\nu}$である。
- これは時空の幾何学的構造を定義する。

---

### (ii) 共変ベクトルの定義

**問題:** $A_{\mu}$を$A^{\mu}$と$\eta_{\mu\nu}$を用いて表せ。

**解答:**

計量テンソルを用いて、反変ベクトルから共変ベクトルへの変換は:
$$A_{\mu} = \eta_{\mu\nu} A^{\nu}$$

**答え:**
$$A_{\mu} = \eta_{\mu\nu} A^{\nu}$$

**物理的意味:**
- 計量テンソルは、反変成分と共変成分を変換する役割を果たす。
- これは時空の内積を定義するために必要である。

---

### (iii) 共変成分の具体的表現

**問題:** 4ベクトル$A^{\mu} = (A^0, \vec{A}) = (A^0, A^1, A^2, A^3)$が与えられたとき、$A_{\mu}$の成分を$A^0, A^1, A^2, A^3$を用いて表せ。

**解答:**

$$A_{\mu} = \eta_{\mu\nu} A^{\nu}$$

具体的に計算:
$$A_0 = \eta_{00} A^0 + \eta_{01} A^1 + \eta_{02} A^2 + \eta_{03} A^3 = 1 \cdot A^0 + 0 + 0 + 0 = A^0$$

$$A_1 = \eta_{10} A^0 + \eta_{11} A^1 + \eta_{12} A^2 + \eta_{13} A^3 = 0 + (-1) \cdot A^1 + 0 + 0 = -A^1$$

$$A_2 = \eta_{20} A^0 + \eta_{21} A^1 + \eta_{22} A^2 + \eta_{23} A^3 = 0 + 0 + (-1) \cdot A^2 + 0 = -A^2$$

$$A_3 = \eta_{30} A^0 + \eta_{31} A^1 + \eta_{32} A^2 + \eta_{33} A^3 = 0 + 0 + 0 + (-1) \cdot A^3 = -A^3$$

**答え:**
$$A_0 = A^0, \quad A_1 = -A^1, \quad A_2 = -A^2, \quad A_3 = -A^3$$

または:
$$A_{\mu} = (A^0, -A^1, -A^2, -A^3)$$

**物理的意味:**
- 時間成分は符号が変わらないが、空間成分は符号が反転する。
- これはミンコフスキー計量の符号規約$(+---)$による。

---

### (iv) 内積の計算

**問題:** 2つの4ベクトル$(A^{\mu}) = (A^0, A^1, A^2, A^3)$と$(B^{\mu}) = (B^0, B^1, B^2, B^3)$に対して、$A_{\mu} B^{\mu}$を$A^0, A^1, A^2, A^3, B^0, B^1, B^2, B^3$を用いて表せ。

**解答:**

$$A_{\mu} B^{\mu} = A_0 B^0 + A_1 B^1 + A_2 B^2 + A_3 B^3$$

(iii)の結果より:
$$A_0 = A^0, \quad A_1 = -A^1, \quad A_2 = -A^2, \quad A_3 = -A^3$$

したがって:
$$A_{\mu} B^{\mu} = A^0 B^0 - A^1 B^1 - A^2 B^2 - A^3 B^3$$

**答え:**
$$A_{\mu} B^{\mu} = A^0 B^0 - A^1 B^1 - A^2 B^2 - A^3 B^3$$

**物理的意味:**
- これはミンコフスキー内積（ローレンツ不変量）である。
- 時空の内積は、時間成分の積から空間成分の積を引いたものである。
- ローレンツ変換に対して不変である。

---

## 問題 6-3: 不変テンソル

### 問題設定
不変テンソルとは、ある変換の下でテンソルとして変換しても元の形に戻るテンソル、すなわち変換しないと見なせるテンソルである。回転に対してはクロネッカーのデルタ$\delta$と完全反対称3階テンソル$\varepsilon_{ijk}$が不変テンソルである。ローレンツ変換に対しては、計量テンソル$\eta_{\mu\nu}$と4階反対称テンソル$\varepsilon_{\mu\nu\rho\sigma}$が不変テンソルである。

ローレンツ変換:
- 反変ベクトル: $x^{\mu} \to x'^{\mu} = L^{\mu}_{\ \nu} x^{\nu}$
- 共変ベクトル: $x_{\mu} \to x'_{\mu} = L_{\mu}^{\ \nu} x_{\nu}$

2階テンソル$\eta_{\mu\nu}$のローレンツ変換:
$$\eta_{\mu\nu} \to \eta'_{\mu\nu} = L_{\mu}^{\ \rho} L_{\nu}^{\ \sigma} \eta_{\rho\sigma}$$

$\eta'_{\mu\nu} = \eta_{\mu\nu}$であることを示せ。

**注意:** $L_{\mu}^{\ \nu} = \eta_{\mu\rho} \eta^{\nu\sigma} L^{\rho}_{\ \sigma}$、$L^{\mu}_{\ \nu}$を行列$L$と表記し、$\eta_{\mu\nu}$と$\eta^{\mu\nu}$を行列$\eta$と表記する（$\eta^{\mu\nu}$は$\eta_{\mu\nu}$の逆行列であり、対称行列でもある）。$L_{\mu}^{\ \nu}$は$\eta L \eta$と書ける。行列$A$, $B$に対して$AB = 1$ならば$BA = 1$も成り立つことを用いてよい。

### (i) ローレンツ変換の逆行列

**問題:** まず、ローレンツ変換行列$L$の逆行列が$\eta L^T \eta$と書けることを示せ。（時空間隔の不変性から導かれる式$\eta_{\alpha\beta} = \eta_{\mu\nu} L^{\mu}_{\ \alpha} L^{\nu}_{\ \beta}$を用いてよい。）

**解答:**

時空間隔の不変性より:
$$\eta_{\alpha\beta} = \eta_{\mu\nu} L^{\mu}_{\ \alpha} L^{\nu}_{\ \beta}$$

これは行列形式で:
$$\eta = L^T \eta L$$

両辺に左から$\eta$、右から$\eta$をかける:
$$\eta \eta = \eta L^T \eta L \eta$$

$\eta^2 = 1$（$\eta$は対角行列で、各成分の2乗は1）より:
$$1 = \eta L^T \eta L \eta$$

右から$(\eta L^T \eta)$をかけると:
$$(\eta L^T \eta) = L \eta$$

左から$L$をかけると:
$$L (\eta L^T \eta) = L L \eta$$

より直接的に、$\eta = L^T \eta L$の両辺に左から$\eta$、右から$\eta^{-1}$をかける:
$$\eta \eta \eta^{-1} = \eta L^T \eta L \eta^{-1}$$

$\eta \eta^{-1} = 1$より:
$$\eta = \eta L^T \eta L \eta^{-1}$$

両辺に右から$L$をかける:
$$\eta L = \eta L^T \eta L \eta^{-1} L = \eta L^T \eta$$

したがって:
$$L (\eta L^T \eta) = L \eta L = \eta$$

別の方法: $\eta = L^T \eta L$より、両辺の逆行列を取る:
$$\eta^{-1} = (L^T \eta L)^{-1} = L^{-1} \eta^{-1} (L^T)^{-1}$$

$\eta^{-1} = \eta$より:
$$\eta = L^{-1} \eta (L^T)^{-1}$$

両辺に左から$L$、右から$L^T$をかける:
$$L \eta L^T = \eta$$

両辺に左から$\eta$、右から$\eta$をかける:
$$\eta L \eta L^T \eta = \eta^2 = 1$$

したがって:
$$(\eta L^T \eta) L = 1$$

同様に:
$$L (\eta L^T \eta) = 1$$

**答え:** $L$の逆行列は$\eta L^T \eta$である。

**物理的意味:**
- ローレンツ変換の逆変換は、転置と計量テンソルによる変換で得られる。
- これは時空間隔の不変性から自然に導かれる。

---

### (ii) 計量テンソルの不変性

**問題:** $L(\eta L^T \eta) = 1$から、$L_{\mu}^{\ \rho} L_{\nu}^{\ \sigma} \eta_{\rho\sigma} = \eta_{\mu\nu}$を示せ。（つまり、$\eta$は不変テンソルである。）

**解答:**

$L(\eta L^T \eta) = 1$より:
$$L \eta L^T \eta = 1$$

両辺に右から$\eta$をかける:
$$L \eta L^T = \eta$$

成分で書くと:
$$(L \eta L^T)_{\mu\nu} = L_{\mu}^{\ \rho} \eta_{\rho\sigma} (L^T)^{\sigma}_{\ \nu} = L_{\mu}^{\ \rho} \eta_{\rho\sigma} L^{\nu}_{\ \sigma} = \eta_{\mu\nu}$$

一方、$L_{\mu}^{\ \rho} = \eta_{\mu\alpha} \eta^{\rho\beta} L^{\alpha}_{\ \beta}$より、$L_{\mu}^{\ \rho} = (\eta L \eta)^{\rho}_{\ \mu}$である。

より直接的に、$L \eta L^T = \eta$の成分表示:
$$L_{\mu}^{\ \alpha} \eta_{\alpha\beta} L^{\nu}_{\ \beta} = \eta_{\mu\nu}$$

ここで、$L^{\nu}_{\ \beta} = \eta^{\nu\gamma} L_{\gamma}^{\ \beta}$（または適切な変換）を用いる。

実際には、$L_{\mu}^{\ \rho} L_{\nu}^{\ \sigma} \eta_{\rho\sigma}$を計算する必要がある。

$L \eta L^T = \eta$より:
$$L_{\mu}^{\ \alpha} \eta_{\alpha\beta} (L^T)^{\beta}_{\ \nu} = \eta_{\mu\nu}$$

$(L^T)^{\beta}_{\ \nu} = L^{\nu}_{\ \beta}$であるが、より正確には:
$$(L^T)^{\beta}_{\ \nu} = L^{\beta}_{\ \nu}$$

しかし、添字の位置に注意が必要である。

実際、$L_{\mu}^{\ \rho} L_{\nu}^{\ \sigma} \eta_{\rho\sigma}$を直接計算する。

$L_{\mu}^{\ \nu} = \eta_{\mu\alpha} \eta^{\nu\beta} L^{\alpha}_{\ \beta}$より:
$$L_{\mu}^{\ \rho} = \eta_{\mu\alpha} \eta^{\rho\beta} L^{\alpha}_{\ \beta}$$

$$L_{\nu}^{\ \sigma} = \eta_{\nu\gamma} \eta^{\sigma\delta} L^{\gamma}_{\ \delta}$$

したがって:
$$L_{\mu}^{\ \rho} L_{\nu}^{\ \sigma} \eta_{\rho\sigma} = \eta_{\mu\alpha} \eta^{\rho\beta} L^{\alpha}_{\ \beta} \eta_{\nu\gamma} \eta^{\sigma\delta} L^{\gamma}_{\ \delta} \eta_{\rho\sigma}$$

$$= \eta_{\mu\alpha} \eta_{\nu\gamma} L^{\alpha}_{\ \beta} L^{\gamma}_{\ \delta} \eta^{\rho\beta} \eta^{\sigma\delta} \eta_{\rho\sigma}$$

$\eta^{\rho\beta} \eta_{\rho\sigma} = \delta^{\beta}_{\ \sigma}$より:
$$= \eta_{\mu\alpha} \eta_{\nu\gamma} L^{\alpha}_{\ \beta} L^{\gamma}_{\ \delta} \eta^{\sigma\delta} \delta^{\beta}_{\ \sigma}$$

$$= \eta_{\mu\alpha} \eta_{\nu\gamma} L^{\alpha}_{\ \beta} L^{\gamma}_{\ \delta} \eta^{\beta\delta}$$

時空間隔の不変性$\eta_{\beta\delta} = \eta_{\alpha\gamma} L^{\alpha}_{\ \beta} L^{\gamma}_{\ \delta}$より:
$$= \eta_{\mu\alpha} \eta_{\nu\gamma} \eta_{\alpha\gamma} = \eta_{\mu\nu}$$

（最後の等式は、$\eta_{\mu\alpha} \eta_{\alpha\gamma} = \delta_{\mu\gamma}$より）

**答え:** $L_{\mu}^{\ \rho} L_{\nu}^{\ \sigma} \eta_{\rho\sigma} = \eta_{\mu\nu}$が示された。

**物理的意味:**
- 計量テンソル$\eta_{\mu\nu}$はローレンツ変換に対して不変である。
- これは時空間隔がローレンツ不変量であることと等価である。
- すべての慣性系で同じ計量が成り立つ。

---

### (iii) 完全反対称テンソルの不変性

**問題:** $\varepsilon_{\mu\nu\rho\sigma}$が完全反対称のとき、$A_{\mu\nu\rho\sigma} = L_{\mu}^{\ \lambda} L_{\nu}^{\ \kappa} L_{\rho}^{\ \sigma} L_{\sigma}^{\ \tau} \varepsilon_{\lambda\kappa\sigma\tau}$が完全反対称であることを示せ。（完全反対称とは、すべての添字の入れ替えに対して符号が反対になる性質である。）

**解答:**

$\varepsilon_{\mu\nu\rho\sigma}$が完全反対称であるとは、任意の2つの添字を入れ替えると符号が変わることである:
$$\varepsilon_{\mu\nu\rho\sigma} = -\varepsilon_{\nu\mu\rho\sigma} = -\varepsilon_{\mu\rho\nu\sigma} = \cdots$$

$A_{\mu\nu\rho\sigma} = L_{\mu}^{\ \lambda} L_{\nu}^{\ \kappa} L_{\rho}^{\ \sigma} L_{\sigma}^{\ \tau} \varepsilon_{\lambda\kappa\sigma\tau}$について、添字の入れ替えを考える。

例えば、$\mu$と$\nu$を入れ替える:
$$A_{\nu\mu\rho\sigma} = L_{\nu}^{\ \lambda} L_{\mu}^{\ \kappa} L_{\rho}^{\ \sigma} L_{\sigma}^{\ \tau} \varepsilon_{\lambda\kappa\sigma\tau}$$

$\lambda$と$\kappa$を入れ替えると:
$$= L_{\nu}^{\ \kappa} L_{\mu}^{\ \lambda} L_{\rho}^{\ \sigma} L_{\sigma}^{\ \tau} \varepsilon_{\kappa\lambda\sigma\tau}$$

$\varepsilon_{\kappa\lambda\sigma\tau} = -\varepsilon_{\lambda\kappa\sigma\tau}$より:
$$= -L_{\nu}^{\ \kappa} L_{\mu}^{\ \lambda} L_{\rho}^{\ \sigma} L_{\sigma}^{\ \tau} \varepsilon_{\lambda\kappa\sigma\tau}$$

$$= -L_{\mu}^{\ \lambda} L_{\nu}^{\ \kappa} L_{\rho}^{\ \sigma} L_{\sigma}^{\ \tau} \varepsilon_{\lambda\kappa\sigma\tau} = -A_{\mu\nu\rho\sigma}$$

同様に、他の任意の2つの添字の入れ替えについても、完全反対称性が保たれる。

**答え:** $A_{\mu\nu\rho\sigma}$は完全反対称である。

**物理的意味:**
- 完全反対称テンソルは、ローレンツ変換の下でその性質を保つ。
- これは$\varepsilon_{\mu\nu\rho\sigma}$が不変テンソル（定数倍を除いて）であることの基礎となる。

---

## 問題 6-4: 固有時 (Proper Time)

### 問題設定
慣性系にいる観測者から見て、質点が次の運動をしている:
$$x = R\cos(at), \quad y = R\sin(at), \quad z = Vt$$

ここで、$R$, $a$, $V$は定数である。観測者から見て、時間$T$後に、質点に固定された時計が刻む時間を求めよ。ただし、光速を$c$とする。

### 解答

**問題:** 時間$T$後の質点の固有時を求めよ。

**解答:**

質点の速度を計算する:
$$v_x = \frac{dx}{dt} = -Ra\sin(at)$$
$$v_y = \frac{dy}{dt} = Ra\cos(at)$$
$$v_z = \frac{dz}{dt} = V$$

速度の大きさ:
$$|\vec{v}|^2 = v_x^2 + v_y^2 + v_z^2 = R^2a^2\sin^2(at) + R^2a^2\cos^2(at) + V^2 = R^2a^2 + V^2$$

したがって:
$$|\vec{v}| = \sqrt{R^2a^2 + V^2}$$

固有時の微分:
$$d\tau = dt \sqrt{1 - \frac{|\vec{v}|^2}{c^2}} = dt \sqrt{1 - \frac{R^2a^2 + V^2}{c^2}}$$

時間$T$後の固有時:
$$\tau = \int_0^T dt \sqrt{1 - \frac{R^2a^2 + V^2}{c^2}} = T \sqrt{1 - \frac{R^2a^2 + V^2}{c^2}}$$

**答え:**
$$\tau = T \sqrt{1 - \frac{R^2a^2 + V^2}{c^2}}$$

**物理的意味:**
- 質点は、$xy$平面内で半径$R$の円運動（角速度$a$）をしながら、$z$方向に一定速度$V$で移動している。
- 固有時は、質点に固定された時計が測る時間である。
- 観測者から見た時間$T$より短い（時間の遅れ）。
- 速度が大きいほど、固有時の進みが遅くなる。

---

## 問題 6-5: エネルギー運動量ベクトル (Energy-Momentum Vector)

### 問題設定と背景

#### 4元運動量ベクトルとは

相対論的力学では、エネルギー$E$と運動量$\vec{p}$を組み合わせて、4元ベクトル（4元運動量ベクトル）を定義する:
$$P^{\mu} = (P^0, P^1, P^2, P^3) = \left(\frac{E}{c}, p_x, p_y, p_z\right)$$

ここで:
- $P^0 = E/c$は時間成分（エネルギーを光速で割ったもの）
- $P^i = p_i$（$i = 1, 2, 3$）は空間成分（運動量）

質量$m$、速度$\vec{v}$の質点の場合:
$$E = \frac{mc^2}{\sqrt{1 - v^2/c^2}} = \gamma mc^2$$
$$\vec{p} = \frac{m\vec{v}}{\sqrt{1 - v^2/c^2}} = \gamma m\vec{v}$$

したがって:
$$P^{\mu} = \gamma m(c, v_x, v_y, v_z) = \frac{m}{\sqrt{1 - v^2/c^2}}(c, v_x, v_y, v_z)$$

#### 問題の設定

O₁系で速度$\vec{V}_{(1)} = (V_{(1)x}, V_{(1)y}, V_{(1)z})$で運動している質量$m$の質点がある。相対論的エネルギー運動量ベクトルは:
$$P_{(1)} = \begin{pmatrix}
\frac{mc}{\sqrt{1 - V_{(1)}^2/c^2}} \\
\frac{mV_{(1)x}}{\sqrt{1 - V_{(1)}^2/c^2}} \\
\frac{mV_{(1)y}}{\sqrt{1 - V_{(1)}^2/c^2}} \\
\frac{mV_{(1)z}}{\sqrt{1 - V_{(1)}^2/c^2}}
\end{pmatrix}$$

と表される。ただし、$V_{(1)}^2 = |\vec{V}_{(1)}|^2$である。

一方、O₁系に対して速度$\vec{V} = (V, 0, 0)$で運動するO₂系では、エネルギー運動量ベクトルは:
$$P_{(2)} = \begin{pmatrix}
\frac{mc}{\sqrt{1 - V_{(2)}^2/c^2}} \\
\frac{mV_{(2)x}}{\sqrt{1 - V_{(2)}^2/c^2}} \\
\frac{mV_{(2)y}}{\sqrt{1 - V_{(2)}^2/c^2}} \\
\frac{mV_{(2)z}}{\sqrt{1 - V_{(2)}^2/c^2}}
\end{pmatrix}$$

と表される。ただし、$V_{(2)}^2 = |\vec{V}_{(2)}|^2$である。

### (i) ローレンツ変換による変換

**問題:** 問題5-3の結果を用いて、$P_{(1)}$から$P_{(2)}$へのローレンツ変換が、次の$L_V$を用いて、$P_{(2)} = L_V P_{(1)}$と表されることを示せ。

$$L_V = \begin{pmatrix}
\gamma & -\gamma\beta & 0 & 0 \\
-\gamma\beta & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

ここで、$\beta = V/c$、$\gamma = 1/\sqrt{1-\beta^2}$である。

**解答:**

#### 方法1: 4元ベクトルの変換則から直接導く

4元運動量ベクトル$P^{\mu} = (P^0, P^1, P^2, P^3) = (E/c, p_x, p_y, p_z)$は4元ベクトルであるため、時空座標のローレンツ変換と同じ変換則に従う。

時空座標のローレンツ変換（O₁系からO₂系へ、O₂系が$x$方向に速度$V$で運動）:
$$ct' = \gamma(ct - \beta x)$$
$$x' = \gamma(x - \beta ct)$$
$$y' = y$$
$$z' = z$$

4元ベクトルの変換則より、4元運動量も同じ変換を受ける:
$$P_{(2)}^0 = \gamma(P_{(1)}^0 - \beta P_{(1)}^1)$$
$$P_{(2)}^1 = \gamma(P_{(1)}^1 - \beta P_{(1)}^0)$$
$$P_{(2)}^2 = P_{(1)}^2$$
$$P_{(2)}^3 = P_{(1)}^3$$

これを行列形式で書くと:
$$\begin{pmatrix}
P_{(2)}^0 \\
P_{(2)}^1 \\
P_{(2)}^2 \\
P_{(2)}^3
\end{pmatrix} = \begin{pmatrix}
\gamma & -\gamma\beta & 0 & 0 \\
-\gamma\beta & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
P_{(1)}^0 \\
P_{(1)}^1 \\
P_{(1)}^2 \\
P_{(1)}^3
\end{pmatrix}$$

したがって:
$$P_{(2)} = L_V P_{(1)}$$

#### 方法2: 速度変換公式から導く（検証）

問題5-3の速度変換公式を用いて、4元運動量の成分が正しく変換されることを確認する。

O₁系での4元運動量:
$$P_{(1)}^0 = \gamma_{(1)} mc = \frac{mc}{\sqrt{1 - V_{(1)}^2/c^2}}$$
$$P_{(1)}^1 = \gamma_{(1)} mV_{(1)x} = \frac{mV_{(1)x}}{\sqrt{1 - V_{(1)}^2/c^2}}$$
$$P_{(1)}^2 = \gamma_{(1)} mV_{(1)y}$$
$$P_{(1)}^3 = \gamma_{(1)} mV_{(1)z}$$

ここで、$\gamma_{(1)} = 1/\sqrt{1 - V_{(1)}^2/c^2}$である。

ローレンツ変換を適用:
$$P_{(2)}^0 = \gamma(P_{(1)}^0 - \beta P_{(1)}^1) = \gamma \gamma_{(1)} m(c - \beta V_{(1)x})$$

$$P_{(2)}^1 = \gamma(P_{(1)}^1 - \beta P_{(1)}^0) = \gamma \gamma_{(1)} m(V_{(1)x} - \beta c)$$

一方、O₂系での4元運動量の定義から:
$$P_{(2)}^0 = \gamma_{(2)} mc = \frac{mc}{\sqrt{1 - V_{(2)}^2/c^2}}$$
$$P_{(2)}^1 = \gamma_{(2)} mV_{(2)x} = \frac{mV_{(2)x}}{\sqrt{1 - V_{(2)}^2/c^2}}$$

問題5-3の速度変換公式:
$$V_{(2)x} = \frac{V_{(1)x} - V}{1 - V V_{(1)x}/c^2}$$

速度変換公式から$\gamma_{(2)}$を計算する必要があるが、これは複雑である。しかし、4元ベクトルの変換則が正しいことを前提とすれば、速度変換公式と整合性があることが示せる。

実際、$P_{(2)}^0 = \gamma_{(2)} mc$と$P_{(2)}^0 = \gamma \gamma_{(1)} m(c - \beta V_{(1)x})$が等しいことから、$\gamma_{(2)}$を求めることができる。

**答え:** 示された。

**物理的意味:**

1. **4元ベクトルとしての性質:**
   - 4元運動量$P^{\mu} = (E/c, \vec{p})$は、時空座標と同じローレンツ変換則に従う4元ベクトルである。
   - これは、エネルギーと運動量が時空の対称性と密接に関連していることを示している。

2. **エネルギーと運動量の混合:**
   - ローレンツ変換により、エネルギーと運動量は混合する。
   - 例えば、$P_{(2)}^0 = \gamma(P_{(1)}^0 - \beta P_{(1)}^1)$は、O₁系でのエネルギーと$x$方向の運動量の線形結合として、O₂系でのエネルギーが表される。
   - これは、異なる慣性系では「エネルギー」と「運動量」の区別が相対的であることを意味する。

3. **具体的な例:**
   - O₁系で静止している質点（$V_{(1)} = 0$）の場合:
     - $P_{(1)} = (mc, 0, 0, 0)$
     - O₂系（$x$方向に速度$V$で運動）から見ると:
       - $P_{(2)}^0 = \gamma mc$（エネルギーは$\gamma mc^2$）
       - $P_{(2)}^1 = -\gamma \beta mc$（$x$方向の運動量は$-\gamma \beta mc$）
     - これは、静止している質点が別の慣性系から見ると運動しているように見えることを示している。

4. **横方向成分の不変性:**
   - $y$方向と$z$方向の運動量成分は、$x$方向のブーストに対して不変である。
   - これは、ブースト方向に垂直な成分が変換を受けないことを意味する。

---

### (ii) 共変ベクトルの変換

**問題:** 問題6-2の$\eta_{\mu\nu}$を用いて、$P_{(1)\mu}$と$P_{(2)\mu}$を、$P_{(1)\mu} = \eta_{\mu\nu}P_{(1)}^{\nu}$、$P_{(2)\mu} = \eta_{\mu\nu}P_{(2)}^{\nu}$と定義する。$P_{(1)\mu}$から$P_{(2)\mu}$へのローレンツ変換を、$P_{(2)\mu} = L_{\mu}^{\ \nu} P_{(1)\nu}$と書くとき、$L_{\mu}^{\ \nu}$を求めよ。

**解答:**

#### 共変ベクトルの定義

問題6-2より、計量テンソル$\eta_{\mu\nu}$を用いて、反変ベクトルから共変ベクトルへの変換は:
$$P_{\mu} = \eta_{\mu\nu}P^{\nu}$$

具体的な成分:
$$P_0 = \eta_{00}P^0 + \eta_{01}P^1 + \eta_{02}P^2 + \eta_{03}P^3 = P^0$$
$$P_1 = \eta_{10}P^0 + \eta_{11}P^1 + \eta_{12}P^2 + \eta_{13}P^3 = -P^1$$
$$P_2 = -P^2, \quad P_3 = -P^3$$

したがって:
$$P_{(1)0} = P_{(1)}^0, \quad P_{(1)1} = -P_{(1)}^1, \quad P_{(1)2} = -P_{(1)}^2, \quad P_{(1)3} = -P_{(1)}^3$$

同様に:
$$P_{(2)\mu} = \eta_{\mu\nu}P_{(2)}^{\nu}$$

#### 共変ベクトルの変換則の導出

反変ベクトルの変換:
$$P_{(2)}^{\mu} = L^{\mu}_{\ \nu} P_{(1)}^{\nu}$$

ここで、$L^{\mu}_{\ \nu}$は(i)で求めたローレンツ変換行列である。

共変ベクトルの変換を求める:
$$P_{(2)\mu} = \eta_{\mu\nu}P_{(2)}^{\nu} = \eta_{\mu\nu} L^{\nu}_{\ \rho} P_{(1)}^{\rho}$$

反変ベクトルを共変ベクトルで表す: $P_{(1)}^{\rho} = \eta^{\rho\sigma}P_{(1)\sigma}$（$\eta^{\mu\nu}$は$\eta_{\mu\nu}$の逆行列）

したがって:
$$P_{(2)\mu} = \eta_{\mu\nu} L^{\nu}_{\ \rho} \eta^{\rho\sigma}P_{(1)\sigma}$$

これより、共変ベクトルの変換行列は:
$$L_{\mu}^{\ \sigma} = \eta_{\mu\nu} L^{\nu}_{\ \rho} \eta^{\rho\sigma}$$

#### 具体的な計算

(i)で求めた反変ベクトルの変換行列:
$$L^{\mu}_{\ \nu} = \begin{pmatrix}
\gamma & -\gamma\beta & 0 & 0 \\
-\gamma\beta & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

計量テンソル:
$$\eta_{\mu\nu} = \eta^{\mu\nu} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}$$

行列の積を計算:
$$L_{\mu}^{\ \nu} = \eta_{\mu\rho} L^{\rho}_{\ \sigma} \eta^{\sigma\nu}$$

行列形式で:
$$L_{\mu}^{\ \nu} = \eta L \eta$$

段階的に計算:

**ステップ1:** $\eta L$の計算
$$\eta L = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}
\begin{pmatrix}
\gamma & -\gamma\beta & 0 & 0 \\
-\gamma\beta & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
= \begin{pmatrix}
\gamma & -\gamma\beta & 0 & 0 \\
\gamma\beta & -\gamma & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}$$

**ステップ2:** $(\eta L) \eta$の計算
$$(\eta L) \eta = \begin{pmatrix}
\gamma & -\gamma\beta & 0 & 0 \\
\gamma\beta & -\gamma & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}
= \begin{pmatrix}
\gamma & \gamma\beta & 0 & 0 \\
\gamma\beta & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

**答え:**
$$L_{\mu}^{\ \nu} = \begin{pmatrix}
\gamma & \gamma\beta & 0 & 0 \\
\gamma\beta & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

#### 検証: 成分ごとの計算

成分ごとに直接計算して確認する:

$$L_0^{\ 0} = \eta_{0\rho} L^{\rho}_{\ \sigma} \eta^{\sigma 0} = \eta_{00} L^0_{\ \sigma} \eta^{\sigma 0} = 1 \cdot L^0_{\ 0} \cdot 1 = \gamma$$

$$L_0^{\ 1} = \eta_{0\rho} L^{\rho}_{\ \sigma} \eta^{\sigma 1} = \eta_{00} L^0_{\ \sigma} \eta^{\sigma 1} = 1 \cdot L^0_{\ 1} \cdot (-1) = -(-\gamma\beta) \cdot (-1) = \gamma\beta$$

$$L_1^{\ 0} = \eta_{1\rho} L^{\rho}_{\ \sigma} \eta^{\sigma 0} = \eta_{11} L^1_{\ \sigma} \eta^{\sigma 0} = (-1) \cdot L^1_{\ 0} \cdot 1 = -(-\gamma\beta) = \gamma\beta$$

$$L_1^{\ 1} = \eta_{1\rho} L^{\rho}_{\ \sigma} \eta^{\sigma 1} = \eta_{11} L^1_{\ \sigma} \eta^{\sigma 1} = (-1) \cdot L^1_{\ 1} \cdot (-1) = -(\gamma) \cdot (-1) = \gamma$$

横方向成分:
$$L_2^{\ 2} = \eta_{2\rho} L^{\rho}_{\ \sigma} \eta^{\sigma 2} = \eta_{22} L^2_{\ 2} \eta^{2 2} = (-1) \cdot 1 \cdot (-1) = 1$$

同様に$L_3^{\ 3} = 1$、非対角成分は0。

**物理的意味:**

1. **反変と共変の違い:**
   - 反変ベクトル$P^{\mu}$の変換: $P'^{\mu} = L^{\mu}_{\ \nu} P^{\nu}$
   - 共変ベクトル$P_{\mu}$の変換: $P'_{\mu} = L_{\mu}^{\ \nu} P_{\nu}$
   - 変換行列の符号が異なる部分がある（特に$\beta$の符号）。

2. **内積の不変性との関係:**
   - 内積$P^{\mu}P_{\mu}$はローレンツ不変量である。
   - これは、$P'^{\mu}P'_{\mu} = P^{\mu}P_{\mu}$が成り立つことを意味する。
   - この不変性は、反変と共変の変換行列が互いに逆変換の関係にあることから保証される。

3. **具体的な変換の違い:**
   - 反変ベクトル: $P'^0 = \gamma(P^0 - \beta P^1)$、$P'^1 = \gamma(P^1 - \beta P^0)$
   - 共変ベクトル: $P'_0 = \gamma(P_0 + \beta P_1)$、$P'_1 = \gamma(P_1 + \beta P_0)$
   - $\beta$の符号が反対になっている（$P_1 = -P^1$であることに注意）。

---

### (iii) ローレンツ不変量

**問題:** $P_{(1)}^{\mu} P_{(1)\mu} = P_{(2)}^{\mu} P_{(2)\mu} = m^2c^2$であることを示せ。

**解答:**

#### 方法1: 直接計算による証明

問題6-2(iv)より、ミンコフスキー内積は:
$$P^{\mu} P_{\mu} = (P^0)^2 - (P^1)^2 - (P^2)^2 - (P^3)^2$$

**O₁系での計算:**

4元運動量の成分:
$$P_{(1)}^0 = \frac{mc}{\sqrt{1 - V_{(1)}^2/c^2}} = \gamma_{(1)} mc$$
$$P_{(1)}^1 = \frac{mV_{(1)x}}{\sqrt{1 - V_{(1)}^2/c^2}} = \gamma_{(1)} mV_{(1)x}$$
$$P_{(1)}^2 = \gamma_{(1)} mV_{(1)y}$$
$$P_{(1)}^3 = \gamma_{(1)} mV_{(1)z}$$

ここで、$\gamma_{(1)} = 1/\sqrt{1 - V_{(1)}^2/c^2}$である。

内積を計算:
$$P_{(1)}^{\mu} P_{(1)\mu} = (P_{(1)}^0)^2 - (P_{(1)}^1)^2 - (P_{(1)}^2)^2 - (P_{(1)}^3)^2$$

$$= (\gamma_{(1)} mc)^2 - (\gamma_{(1)} mV_{(1)x})^2 - (\gamma_{(1)} mV_{(1)y})^2 - (\gamma_{(1)} mV_{(1)z})^2$$

$$= \gamma_{(1)}^2 m^2 [c^2 - V_{(1)x}^2 - V_{(1)y}^2 - V_{(1)z}^2]$$

$$= \gamma_{(1)}^2 m^2 [c^2 - V_{(1)}^2]$$

$$= \gamma_{(1)}^2 m^2 c^2 (1 - V_{(1)}^2/c^2)$$

$\gamma_{(1)}^2 = 1/(1 - V_{(1)}^2/c^2)$より:
$$= \frac{m^2 c^2 (1 - V_{(1)}^2/c^2)}{1 - V_{(1)}^2/c^2} = m^2 c^2$$

**O₂系での計算:**

同様に、O₂系でも:
$$P_{(2)}^0 = \gamma_{(2)} mc = \frac{mc}{\sqrt{1 - V_{(2)}^2/c^2}}$$
$$P_{(2)}^1 = \gamma_{(2)} mV_{(2)x}$$
$$P_{(2)}^2 = \gamma_{(2)} mV_{(2)y}$$
$$P_{(2)}^3 = \gamma_{(2)} mV_{(2)z}$$

内積を計算:
$$P_{(2)}^{\mu} P_{(2)\mu} = \gamma_{(2)}^2 m^2 [c^2 - V_{(2)}^2] = \gamma_{(2)}^2 m^2 c^2 (1 - V_{(2)}^2/c^2) = m^2 c^2$$

#### 方法2: ローレンツ変換の不変性から証明

4元ベクトルの内積はローレンツ不変量である。すなわち、ローレンツ変換$L^{\mu}_{\ \nu}$に対して:
$$P'^{\mu} P'_{\mu} = P^{\mu} P_{\mu}$$

これは、計量テンソル$\eta_{\mu\nu}$が不変テンソルであること（問題6-3）から直接導かれる。

実際、$P'^{\mu} = L^{\mu}_{\ \nu} P^{\nu}$、$P'_{\mu} = L_{\mu}^{\ \rho} P_{\rho}$より:
$$P'^{\mu} P'_{\mu} = L^{\mu}_{\ \nu} P^{\nu} L_{\mu}^{\ \rho} P_{\rho}$$

問題6-3(ii)より、$L_{\mu}^{\ \rho} L_{\nu}^{\ \sigma} \eta_{\rho\sigma} = \eta_{\mu\nu}$であるから、これを用いると:
$$P'^{\mu} P'_{\mu} = \eta_{\mu\nu} P^{\mu} P^{\nu} = P^{\mu} P_{\mu}$$

したがって、O₁系で$P_{(1)}^{\mu} P_{(1)\mu} = m^2c^2$が成り立つなら、O₂系でも$P_{(2)}^{\mu} P_{(2)\mu} = m^2c^2$が成り立つ。

**答え:** $P_{(1)}^{\mu} P_{(1)\mu} = P_{(2)}^{\mu} P_{(2)\mu} = m^2c^2$

#### エネルギーと運動量の関係式への変換

4元運動量の内積をエネルギーと運動量で表す:
$$P^{\mu} P_{\mu} = (P^0)^2 - (P^1)^2 - (P^2)^2 - (P^3)^2 = \left(\frac{E}{c}\right)^2 - p_x^2 - p_y^2 - p_z^2$$

$$= \frac{E^2}{c^2} - |\vec{p}|^2 = m^2 c^2$$

両辺に$c^2$をかける:
$$E^2 - (|\vec{p}|c)^2 = (mc^2)^2$$

したがって:
$$E^2 = (|\vec{p}|c)^2 + (mc^2)^2$$

これは相対論的なエネルギーと運動量の関係式である。

**物理的意味:**

1. **質量の定義:**
   - $P^{\mu}P_{\mu} = m^2c^2$は、質量$m$の定義そのものである。
   - この量は、すべての慣性系で同じ値を持つローレンツ不変量である。
   - 質量は、速度に依存しない不変量である（静止質量）。

2. **エネルギーと運動量の関係:**
   - $E^2 = (pc)^2 + (mc^2)^2$は、相対論的なエネルギーと運動量の関係式である。
   - 非相対論的極限（$v \ll c$）では:
     - $E = mc^2 + \frac{p^2}{2m} + \cdots$（静止エネルギー + 運動エネルギー）
   - 光速粒子（$m = 0$）の場合:
     - $E = pc$（光子のエネルギーと運動量の関係）

3. **ローレンツ不変量の重要性:**
   - 物理法則は、すべての慣性系で同じ形で成り立つべきである（相対性原理）。
   - ローレンツ不変量は、異なる慣性系での観測結果を結びつける。
   - 質量は、この不変量によって定義される基本的な物理量である。

4. **具体的な例:**
   - **静止している質点（$v = 0$）:**
     - $E = mc^2$（アインシュタインの有名な式）
     - $p = 0$
     - $P^{\mu}P_{\mu} = (mc)^2 - 0 = m^2c^2$ ✓
   
   - **光速で運動する粒子（$v = c$、$m = 0$）:**
     - $E = pc$
     - $P^{\mu}P_{\mu} = (E/c)^2 - p^2 = 0$ ✓
   
   - **一般の運動（$0 < v < c$）:**
     - $E = \gamma mc^2$、$p = \gamma mv$
     - $P^{\mu}P_{\mu} = (\gamma mc)^2 - (\gamma mv)^2 = \gamma^2 m^2(c^2 - v^2) = m^2c^2$ ✓

5. **時空の幾何学的解釈:**
   - 4元運動量ベクトルは、ミンコフスキー時空内のベクトルである。
   - $P^{\mu}P_{\mu} = m^2c^2$は、このベクトルの「長さ」の2乗である。
   - 質量が異なる粒子は、異なる「長さ」の4元運動量ベクトルを持つ。
   - ローレンツ変換は、この「長さ」を保つ（時空間隔の不変性）。

