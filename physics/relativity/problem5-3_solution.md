# 問題 5-3 解答: 速度の変換

## 問題
慣性系O₁系（座標$(t, x, y, z)$）と、O₁系に対してx方向の正の方向に速度Vで運動している慣性系O₂系（座標$(t', x', y', z')$）がある。

## 解答

### (i) 速度の変換公式

**問題:** O₁系で速度$\vec{V}_1 = (V_{1x}, V_{1y}, V_{1z}) = (dx/dt, dy/dt, dz/dt)$で運動している粒子の、O₂系での速度$\vec{V}_2 = (V_{2x}, V_{2y}, V_{2z}) = (dx'/dt', dy'/dt', dz'/dt')$を求めよ。光速をcとする。

**解答:**

ローレンツ変換:
$$t' = \gamma\left(t - \frac{Vx}{c^2}\right)$$
$$x' = \gamma(x - Vt)$$
$$y' = y$$
$$z' = z$$

ここで、$\gamma = \frac{1}{\sqrt{1-V^2/c^2}}$、$\beta = V/c$。

速度の変換を求めるため、微分を計算する。

$$dt' = \gamma\left(dt - \frac{Vdx}{c^2}\right) = \gamma dt\left(1 - \frac{V}{c^2}\frac{dx}{dt}\right) = \gamma dt\left(1 - \frac{V V_{1x}}{c^2}\right)$$

$$dx' = \gamma(dx - Vdt) = \gamma dt\left(\frac{dx}{dt} - V\right) = \gamma dt(V_{1x} - V)$$

$$dy' = dy = V_{1y} dt$$

$$dz' = dz = V_{1z} dt$$

したがって:

$$V_{2x} = \frac{dx'}{dt'} = \frac{\gamma dt(V_{1x} - V)}{\gamma dt(1 - V V_{1x}/c^2)} = \frac{V_{1x} - V}{1 - V V_{1x}/c^2}$$

$$V_{2y} = \frac{dy'}{dt'} = \frac{V_{1y} dt}{\gamma dt(1 - V V_{1x}/c^2)} = \frac{V_{1y}}{\gamma(1 - V V_{1x}/c^2)}$$

$$V_{2z} = \frac{dz'}{dt'} = \frac{V_{1z} dt}{\gamma dt(1 - V V_{1x}/c^2)} = \frac{V_{1z}}{\gamma(1 - V V_{1x}/c^2)}$$

**答え:**
$$V_{2x} = \frac{V_{1x} - V}{1 - V V_{1x}/c^2}$$
$$V_{2y} = \frac{V_{1y}}{\gamma(1 - V V_{1x}/c^2)}$$
$$V_{2z} = \frac{V_{1z}}{\gamma(1 - V V_{1x}/c^2)}$$

---

### (ii) 光速不変の証明

**問題:** 次の式を示せ:
$$c^2 - |\vec{V}_2|^2 = \frac{(c^2 - |\vec{V}_1|^2)(1 - V^2/c^2)}{(1 - V V_{1x}/c^2)^2}$$

そして、$V < c$かつ$|\vec{V}_1| < c$ならば$|\vec{V}_2| < c$であることを示せ。

**解答:**

まず、$|\vec{V}_2|^2$を計算する:

$$|\vec{V}_2|^2 = V_{2x}^2 + V_{2y}^2 + V_{2z}^2$$

$$= \frac{(V_{1x} - V)^2}{(1 - V V_{1x}/c^2)^2} + \frac{V_{1y}^2}{\gamma^2(1 - V V_{1x}/c^2)^2} + \frac{V_{1z}^2}{\gamma^2(1 - V V_{1x}/c^2)^2}$$

$$= \frac{1}{(1 - V V_{1x}/c^2)^2}\left[(V_{1x} - V)^2 + \frac{V_{1y}^2 + V_{1z}^2}{\gamma^2}\right]$$

$\gamma^2 = \frac{1}{1-V^2/c^2}$より:

$$= \frac{1}{(1 - V V_{1x}/c^2)^2}\left[(V_{1x} - V)^2 + (V_{1y}^2 + V_{1z}^2)(1 - V^2/c^2)\right]$$

$$= \frac{1}{(1 - V V_{1x}/c^2)^2}\left[V_{1x}^2 - 2V V_{1x} + V^2 + (V_{1y}^2 + V_{1z}^2) - (V_{1y}^2 + V_{1z}^2)V^2/c^2\right]$$

$$= \frac{1}{(1 - V V_{1x}/c^2)^2}\left[V_{1x}^2 + V_{1y}^2 + V_{1z}^2 - 2V V_{1x} + V^2 - (V_{1y}^2 + V_{1z}^2)V^2/c^2\right]$$

$$= \frac{1}{(1 - V V_{1x}/c^2)^2}\left[|\vec{V}_1|^2 - 2V V_{1x} + V^2 - (|\vec{V}_1|^2 - V_{1x}^2)V^2/c^2\right]$$

$$= \frac{1}{(1 - V V_{1x}/c^2)^2}\left[|\vec{V}_1|^2 - 2V V_{1x} + V^2 - |\vec{V}_1|^2 V^2/c^2 + V_{1x}^2 V^2/c^2\right]$$

$$= \frac{1}{(1 - V V_{1x}/c^2)^2}\left[|\vec{V}_1|^2(1 - V^2/c^2) - 2V V_{1x} + V^2 + V_{1x}^2 V^2/c^2\right]$$

$$= \frac{1}{(1 - V V_{1x}/c^2)^2}\left[|\vec{V}_1|^2(1 - V^2/c^2) - 2V V_{1x}(1 - V V_{1x}/c^2) + V^2(1 - V_{1x}^2/c^2)\right]$$

より直接的な計算:

$$|\vec{V}_2|^2 = \frac{(V_{1x} - V)^2 + (V_{1y}^2 + V_{1z}^2)(1 - V^2/c^2)}{(1 - V V_{1x}/c^2)^2}$$

$$= \frac{V_{1x}^2 - 2V V_{1x} + V^2 + (|\vec{V}_1|^2 - V_{1x}^2)(1 - V^2/c^2)}{(1 - V V_{1x}/c^2)^2}$$

$$= \frac{V_{1x}^2 - 2V V_{1x} + V^2 + |\vec{V}_1|^2 - V_{1x}^2 - |\vec{V}_1|^2 V^2/c^2 + V_{1x}^2 V^2/c^2}{(1 - V V_{1x}/c^2)^2}$$

$$= \frac{- 2V V_{1x} + V^2 + |\vec{V}_1|^2 - |\vec{V}_1|^2 V^2/c^2 + V_{1x}^2 V^2/c^2}{(1 - V V_{1x}/c^2)^2}$$

$$= \frac{|\vec{V}_1|^2(1 - V^2/c^2) - 2V V_{1x} + V^2 + V_{1x}^2 V^2/c^2}{(1 - V V_{1x}/c^2)^2}$$

$$= \frac{|\vec{V}_1|^2(1 - V^2/c^2) - 2V V_{1x} + V^2(1 + V_{1x}^2/c^2)}{(1 - V V_{1x}/c^2)^2}$$

別のアプローチ: 直接$c^2 - |\vec{V}_2|^2$を計算する。

$$c^2 - |\vec{V}_2|^2 = c^2 - \frac{(V_{1x} - V)^2 + (V_{1y}^2 + V_{1z}^2)(1 - V^2/c^2)}{(1 - V V_{1x}/c^2)^2}$$

$$= \frac{c^2(1 - V V_{1x}/c^2)^2 - (V_{1x} - V)^2 - (V_{1y}^2 + V_{1z}^2)(1 - V^2/c^2)}{(1 - V V_{1x}/c^2)^2}$$

$$= \frac{(c - V V_{1x}/c)^2 - (V_{1x} - V)^2 - (|\vec{V}_1|^2 - V_{1x}^2)(1 - V^2/c^2)}{(1 - V V_{1x}/c^2)^2}$$

$$= \frac{c^2 - 2V V_{1x} + V^2 V_{1x}^2/c^2 - V_{1x}^2 + 2V V_{1x} - V^2 - (|\vec{V}_1|^2 - V_{1x}^2)(1 - V^2/c^2)}{(1 - V V_{1x}/c^2)^2}$$

$$= \frac{c^2 + V^2 V_{1x}^2/c^2 - V_{1x}^2 - V^2 - |\vec{V}_1|^2(1 - V^2/c^2) + V_{1x}^2(1 - V^2/c^2)}{(1 - V V_{1x}/c^2)^2}$$

$$= \frac{c^2(1 - V^2/c^2) - |\vec{V}_1|^2(1 - V^2/c^2)}{(1 - V V_{1x}/c^2)^2}$$

$$= \frac{(c^2 - |\vec{V}_1|^2)(1 - V^2/c^2)}{(1 - V V_{1x}/c^2)^2}$$

したがって、示された。

$V < c$かつ$|\vec{V}_1| < c$のとき:
- $c^2 - |\vec{V}_1|^2 > 0$
- $1 - V^2/c^2 > 0$
- $(1 - V V_{1x}/c^2)^2 > 0$（$|V V_{1x}| \leq |V||\vec{V}_1| < c^2$より）

したがって:
$$c^2 - |\vec{V}_2|^2 > 0$$

つまり、$|\vec{V}_2| < c$である。

**答え:** 示された。$V < c$かつ$|\vec{V}_1| < c$ならば$|\vec{V}_2| < c$。

---

### (iii) V → c の極限

**問題:** $V \to c$のとき、$\vec{V}_2 \to (-c, 0, 0)$であることを示せ。

**解答:**

$V \to c$のとき、$\gamma \to \infty$である。

$$V_{2x} = \frac{V_{1x} - V}{1 - V V_{1x}/c^2}$$

$V \to c$のとき:
$$V_{2x} \to \frac{V_{1x} - c}{1 - c V_{1x}/c^2} = \frac{V_{1x} - c}{1 - V_{1x}/c} = \frac{c(V_{1x}/c - 1)}{1 - V_{1x}/c} = -c$$

$$V_{2y} = \frac{V_{1y}}{\gamma(1 - V V_{1x}/c^2)} \to 0$$（$\gamma \to \infty$より）

$$V_{2z} = \frac{V_{1z}}{\gamma(1 - V V_{1x}/c^2)} \to 0$$（$\gamma \to \infty$より）

**答え:** $\vec{V}_2 \to (-c, 0, 0)$

---

### (iv) 光速粒子の変換

**問題:** $\vec{V}_1 \to (c, 0, 0)$のとき、$\vec{V}_2 \to (c, 0, 0)$であることを示せ。

**解答:**

$\vec{V}_1 = (c, 0, 0)$のとき:

$$V_{2x} = \frac{c - V}{1 - V c/c^2} = \frac{c - V}{1 - V/c} = \frac{c(1 - V/c)}{1 - V/c} = c$$

$$V_{2y} = \frac{0}{\gamma(1 - V c/c^2)} = 0$$

$$V_{2z} = \frac{0}{\gamma(1 - V c/c^2)} = 0$$

したがって、$\vec{V}_2 = (c, 0, 0)$である。

**答え:** $\vec{V}_2 \to (c, 0, 0)$

