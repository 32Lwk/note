# 問題 5-4 解答: 速度の変換 2

## 問題
O'系がO系に対してx方向の正の方向に一定速度Vで運動している。O系の観測者が、x軸に対して角度θの方向から来る光を観測する。O'系の観測者が同じ光をx'軸に対して角度θ'の方向から来るものとして観測する。

## 解答

### (i) 角度の変換

**問題:** θ'とθの関係を求めよ。

**解答:**

O系での光の速度成分:
$$\vec{V}_1 = (c\cos\theta, c\sin\theta, 0)$$

O'系での光の速度成分:
$$\vec{V}_2 = (c\cos\theta', c\sin\theta', 0)$$

速度変換公式（問題5-3より）:
$$V_{2x} = \frac{V_{1x} - V}{1 - V V_{1x}/c^2}$$
$$V_{2y} = \frac{V_{1y}}{\gamma(1 - V V_{1x}/c^2)}$$

ここで、$\gamma = \frac{1}{\sqrt{1-V^2/c^2}}$、$\beta = V/c$。

光の場合、$|\vec{V}_1| = |\vec{V}_2| = c$である。

$$c\cos\theta' = \frac{c\cos\theta - V}{1 - V c\cos\theta/c^2} = \frac{c\cos\theta - V}{1 - \beta\cos\theta}$$

$$c\sin\theta' = \frac{c\sin\theta}{\gamma(1 - V c\cos\theta/c^2)} = \frac{c\sin\theta}{\gamma(1 - \beta\cos\theta)}$$

したがって:

$$\cos\theta' = \frac{\cos\theta - \beta}{1 - \beta\cos\theta}$$

$$\sin\theta' = \frac{\sin\theta}{\gamma(1 - \beta\cos\theta)}$$

また、$\tan\theta'$を求める:

$$\tan\theta' = \frac{\sin\theta'}{\cos\theta'} = \frac{\sin\theta/\gamma(1 - \beta\cos\theta)}{(\cos\theta - \beta)/(1 - \beta\cos\theta)} = \frac{\sin\theta}{\gamma(\cos\theta - \beta)}$$

**答え:**
$$\cos\theta' = \frac{\cos\theta - \beta}{1 - \beta\cos\theta}$$
$$\sin\theta' = \frac{\sin\theta}{\gamma(1 - \beta\cos\theta)}$$
$$\tan\theta' = \frac{\sin\theta}{\gamma(\cos\theta - \beta)}$$

---

### (ii) θ = π/2 の場合

**問題:** $\theta = \pi/2$のとき、$\theta' = \pi/2 + \Delta\theta$として、$\sin(\Delta\theta)$を求めよ。

**解答:**

$\theta = \pi/2$のとき、$\cos\theta = 0$、$\sin\theta = 1$。

(i)の結果より:

$$\cos\theta' = \frac{0 - \beta}{1 - \beta \cdot 0} = -\beta$$

$$\sin\theta' = \frac{1}{\gamma(1 - \beta \cdot 0)} = \frac{1}{\gamma}$$

$\theta' = \pi/2 + \Delta\theta$より:

$$\cos\theta' = \cos(\pi/2 + \Delta\theta) = -\sin\Delta\theta$$

$$\sin\theta' = \sin(\pi/2 + \Delta\theta) = \cos\Delta\theta$$

したがって:

$$-\sin\Delta\theta = -\beta$$

$$\sin\Delta\theta = \beta$$

また、検算:
$$\cos\Delta\theta = \frac{1}{\gamma}$$

これより:
$$\sin^2\Delta\theta + \cos^2\Delta\theta = \beta^2 + \frac{1}{\gamma^2} = \beta^2 + (1 - \beta^2) = 1$$

正しい。

**答え:** $\sin(\Delta\theta) = \beta = \frac{V}{c}$

