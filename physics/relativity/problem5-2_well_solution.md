# 問題 5-2 解答: ポテンシャルの井戸での束縛状態

## 問題
質量$m$の粒子が以下のポテンシャルに束縛されている場合を考える：
$$V(x) = \begin{cases}
\infty & (x < 0) \\
-V_0 & (0 < x < a) \\
0 & (x > a)
\end{cases}$$

ここで$V_0 > 0$、$a > 0$である。$a$の値を固定し、$V_0$を変化させて（$V_0 > 0$の範囲で）束縛状態の存在を調べる。束縛状態が存在しない条件を$V_0$について求めよ。

$u(x)$はハミルトニアンの固有関数、$E$はエネルギー固有値（束縛状態では$-V_0 < E < 0$）である。

## 解答

### (i) $x = 0$での条件

**問題:** $u(x)$が$x = 0$で満たすべき条件を書け。

**解答:**

$x < 0$の領域ではポテンシャルが無限大なので、粒子はこの領域に存在できない。したがって、波動関数は$x = 0$で0でなければならない。

**答え:** $u(0) = 0$

---

### (ii) $x = \infty$での条件

**問題:** $u(x)$が$x = \infty$で満たすべき条件を書け。

**解答:**

束縛状態では、波動関数は無限遠で0に収束しなければならない（規格化可能であるため）。

**答え:** $u(\infty) = 0$

---

### (iii) $0 < x < a$での時間に依存しないシュレーディンガー方程式

**問題:** $0 < x < a$での時間に依存しないシュレーディンガー方程式を書け。

**解答:**

時間に依存しないシュレーディンガー方程式は：
$$-\frac{\hbar^2}{2m}\frac{d^2u}{dx^2} + V(x)u = Eu$$

$0 < x < a$では$V(x) = -V_0$なので：
$$-\frac{\hbar^2}{2m}\frac{d^2u}{dx^2} - V_0 u = Eu$$

整理すると：
$$-\frac{\hbar^2}{2m}\frac{d^2u}{dx^2} = (E + V_0)u$$

**答え:** $-\frac{\hbar^2}{2m}\frac{d^2u}{dx^2} = (E + V_0)u$

---

### (iv) $x > a$での時間に依存しないシュレーディンガー方程式

**問題:** $x > a$での時間に依存しないシュレーディンガー方程式を書け。

**解答:**

$x > a$では$V(x) = 0$なので：
$$-\frac{\hbar^2}{2m}\frac{d^2u}{dx^2} = Eu$$

束縛状態では$E < 0$なので、これは減衰解を与える。

**答え:** $-\frac{\hbar^2}{2m}\frac{d^2u}{dx^2} = Eu$

---

### (v) $0 < x < a$での解

**問題:** (iii)のシュレーディンガー方程式の解で、(i)の条件を満たすものを$q = \sqrt{2m(V_0 + E)}/\hbar$を用いて表せ。

**解答:**

(iii)の方程式は：
$$\frac{d^2u}{dx^2} = -\frac{2m(E + V_0)}{\hbar^2}u = -q^2 u$$

ここで$q = \sqrt{2m(V_0 + E)}/\hbar$である。束縛状態では$E > -V_0$なので$q > 0$である。

一般解は：
$$u(x) = A\sin(qx) + B\cos(qx)$$

(i)の条件$u(0) = 0$より：
$$u(0) = B = 0$$

したがって：
$$u(x) = A\sin(qx) \quad (0 < x < a)$$

**答え:** $u(x) = A\sin(qx) \quad (0 < x < a)$

---

### (vi) $x > a$での解

**問題:** (iv)のシュレーディンガー方程式の解で、(ii)の条件を満たすものを$\kappa = \sqrt{2m|E|}/\hbar$を用いて表せ。

**解答:**

(iv)の方程式は：
$$\frac{d^2u}{dx^2} = \frac{2mE}{\hbar^2}u$$

束縛状態では$E < 0$なので、$|E| = -E$とすると：
$$\frac{d^2u}{dx^2} = -\frac{2m|E|}{\hbar^2}u = -\kappa^2 u$$

ここで$\kappa = \sqrt{2m|E|}/\hbar > 0$である。

一般解は：
$$u(x) = C e^{\kappa x} + D e^{-\kappa x}$$

(ii)の条件$u(\infty) = 0$より、$C = 0$でなければならない。したがって：
$$u(x) = D e^{-\kappa x} \quad (x > a)$$

**答え:** $u(x) = D e^{-\kappa x} \quad (x > a)$

---

### (vii) $x = a$での連続条件

**問題:** 固有関数$u(x)$とその導関数$du(x)/dx$が$x = a$で満たすべき2つの連続条件を求めよ。

**解答:**

波動関数とその導関数は連続でなければならない。

$0 < x < a$での解: $u(x) = A\sin(qx)$
- $u(a) = A\sin(qa)$
- $\frac{du}{dx}(a) = Aq\cos(qa)$

$x > a$での解: $u(x) = D e^{-\kappa x}$
- $u(a) = D e^{-\kappa a}$
- $\frac{du}{dx}(a) = -D\kappa e^{-\kappa a}$

連続条件：
1. $u(a)$の連続: $A\sin(qa) = D e^{-\kappa a}$
2. $\frac{du}{dx}(a)$の連続: $Aq\cos(qa) = -D\kappa e^{-\kappa a}$

**答え:**
- $A\sin(qa) = D e^{-\kappa a}$
- $Aq\cos(qa) = -D\kappa e^{-\kappa a}$

---

### (viii) 束縛状態が存在しない条件

**問題:** (vii)の2つの条件を組み合わせると、$\kappa = -q\cot(qa)$が導かれる。この条件を$\lambda = 2mV_0a^2/\hbar^2$、$y = qa$を用いて書き直すと：
$$\frac{\sqrt{\lambda - y^2}}{y} = \tan\left(y - \frac{\pi}{2}\right)$$
となる。この式の左辺と右辺をプロットして、この式を満たす$y$が存在しない$\lambda$の条件を求め、そこから束縛状態が存在しない$V_0$の条件を求めよ。

**解答:**

(vii)の2つの条件から：
$$\frac{Aq\cos(qa)}{A\sin(qa)} = \frac{-D\kappa e^{-\kappa a}}{D e^{-\kappa a}}$$

したがって：
$$q\cot(qa) = -\kappa$$

すなわち：
$$\kappa = -q\cot(qa)$$

ここで、$\lambda = 2mV_0a^2/\hbar^2$、$y = qa$とすると：
$$q = \frac{y}{a}, \quad \kappa = \sqrt{\frac{2m|E|}{\hbar^2}}$$

また、$q^2 = \frac{2m(V_0 + E)}{\hbar^2}$、$\kappa^2 = \frac{2m|E|}{\hbar^2}$より：
$$q^2 - \kappa^2 = \frac{2mV_0}{\hbar^2}$$

したがって：
$$\left(\frac{y}{a}\right)^2 - \kappa^2 = \frac{2mV_0}{\hbar^2} = \frac{\lambda}{a^2}$$

$$\kappa^2 = \frac{y^2 - \lambda}{a^2}$$

束縛状態では$E < 0$なので、$q^2 = \frac{2m(V_0 + E)}{\hbar^2} < \frac{2mV_0}{\hbar^2} = \frac{\lambda}{a^2}$、すなわち$y^2 < \lambda$である。

したがって：
$$\kappa = \frac{\sqrt{\lambda - y^2}}{a}$$

$\kappa = -q\cot(qa)$より：
$$\frac{\sqrt{\lambda - y^2}}{a} = -\frac{y}{a}\cot(y)$$

整理すると：
$$\frac{\sqrt{\lambda - y^2}}{y} = -\cot(y) = \tan\left(y - \frac{\pi}{2}\right)$$

この式を満たす$y$が存在するかどうかを調べるため、左辺と右辺をプロットする。

左辺: $f_L(y) = \frac{\sqrt{\lambda - y^2}}{y}$（$0 < y < \sqrt{\lambda}$）
右辺: $f_R(y) = \tan\left(y - \frac{\pi}{2}\right)$

グラフを描いて、交点が存在しない条件を求める。

左辺$f_L(y) = \frac{\sqrt{\lambda - y^2}}{y}$は：
- $y \to 0^+$のとき、$f_L(y) \to +\infty$
- $y \to \sqrt{\lambda}^-$のとき、$f_L(y) \to 0$
- 単調減少関数

右辺$f_R(y) = \tan\left(y - \frac{\pi}{2}\right)$は：
- $y = \frac{\pi}{2}$で特異点を持つ
- $y < \frac{\pi}{2}$の範囲で定義される

束縛状態が存在するためには、$0 < y < \min(\sqrt{\lambda}, \frac{\pi}{2})$の範囲で交点が存在する必要がある。

$\lambda$が小さいとき、$\sqrt{\lambda} < \frac{\pi}{2}$となり、左辺は$y = \sqrt{\lambda}$で0になる。一方、右辺は$y = \sqrt{\lambda} < \frac{\pi}{2}$で有限の値を持つ。したがって、$\lambda$が十分小さいとき、交点が存在しない可能性がある。

臨界条件は、左辺と右辺が接するとき、すなわち$y = \frac{\pi}{2}$のとき$\lambda = \left(\frac{\pi}{2}\right)^2 = \frac{\pi^2}{4}$である。

グラフ描画プログラム（`problem5-2_well_graph.py`）で確認すると、$\lambda < \frac{\pi^2}{4}$のとき、交点が存在しない（または唯一の交点が$y = \frac{\pi}{2}$で接する）ことが確認できる。

**答え:** 

束縛状態が存在しない条件は：
$$\lambda < \frac{\pi^2}{4}$$

すなわち：
$$\frac{2mV_0a^2}{\hbar^2} < \frac{\pi^2}{4}$$

したがって：
$$V_0 < \frac{\pi^2\hbar^2}{8ma^2}$$

![交点のグラフ](problem5-2_well_intersection.png)

上図は、異なる$\lambda$値での左辺（青線）と右辺（赤破線）のグラフである。$\lambda$が小さいとき、交点が存在しないことが確認できる。

