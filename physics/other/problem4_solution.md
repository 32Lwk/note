# 問題4 解答

## 問題
真空中の磁場が、原点から位置ベクトルrに作るベクトルポテンシャル A(r) を考える。
適当な定ベクトルmを用いてA(r)が次のように表せるとする。

$$
A(r) = \frac{1}{4\pi} \frac{m \times r}{r^3}
$$

このとき、磁束密度Bは次のようになることを示せ（原点以外）。

$$
B(r) = -\frac{1}{4\pi} \nabla\left(\frac{m \cdot r}{r^3}\right)
$$

また、磁荷が磁場を作っている場合、これはどのような磁荷分布に対応するか。

## 解答

### 1. 磁束密度の導出

磁束密度はベクトルポテンシャルの回転（ローテーション）で与えられる：

$$
B = \nabla \times A
$$

与えられたベクトルポテンシャルを代入すると：

$$
B = \nabla \times \left[\frac{1}{4\pi} \frac{m \times r}{r^3}\right] = \frac{1}{4\pi} \nabla \times \left(\frac{m \times r}{r^3}\right)
$$

ここで、ベクトル恒等式を用いる：

$$
\nabla \times (A \times B) = A(\nabla \cdot B) - B(\nabla \cdot A) + (B \cdot \nabla)A - (A \cdot \nabla)B
$$

$A = m$（定ベクトル）、$B = r/r^3$ として適用すると：

$$
\nabla \times \left(m \times \frac{r}{r^3}\right) = m\left(\nabla \cdot \frac{r}{r^3}\right) - \frac{r}{r^3}(\nabla \cdot m) + \left(\frac{r}{r^3} \cdot \nabla\right)m - (m \cdot \nabla)\frac{r}{r^3}
$$

mは定ベクトルなので：
- $\nabla \cdot m = 0$
- $\left(\frac{r}{r^3} \cdot \nabla\right)m = 0$

したがって：

$$
\nabla \times \left(m \times \frac{r}{r^3}\right) = m\left(\nabla \cdot \frac{r}{r^3}\right) - (m \cdot \nabla)\frac{r}{r^3}
$$

ヒント $r/r^3 = -\nabla(1/r)$ を用いると：

$$
\nabla \cdot \frac{r}{r^3} = \nabla \cdot \left(-\nabla\frac{1}{r}\right) = -\nabla^2\frac{1}{r}
$$

原点以外では $\nabla^2(1/r) = 0$ なので：

$$
\nabla \cdot \frac{r}{r^3} = 0
$$

次に、$(m \cdot \nabla)(r/r^3)$ を計算する：

$$
(m \cdot \nabla)\frac{r}{r^3} = (m \cdot \nabla)\left(-\nabla\frac{1}{r}\right) = -\nabla\left[(m \cdot \nabla)\frac{1}{r}\right]
$$

ここで、$(m \cdot \nabla)(1/r) = m \cdot \nabla(1/r)$ であり、$\nabla(1/r) = -r/r^3$ より：

$$
(m \cdot \nabla)\frac{1}{r} = m \cdot \left(-\frac{r}{r^3}\right) = -\frac{m \cdot r}{r^3}
$$

したがって：

$$
(m \cdot \nabla)\frac{r}{r^3} = -\nabla\left(-\frac{m \cdot r}{r^3}\right) = \nabla\left(\frac{m \cdot r}{r^3}\right)
$$

以上より：

$$
\nabla \times \left(m \times \frac{r}{r^3}\right) = 0 - \nabla\left(\frac{m \cdot r}{r^3}\right) = -\nabla\left(\frac{m \cdot r}{r^3}\right)
$$

したがって：

$$
B = \frac{1}{4\pi} \left[-\nabla\left(\frac{m \cdot r}{r^3}\right)\right] = -\frac{1}{4\pi} \nabla\left(\frac{m \cdot r}{r^3}\right)
$$

これで目標の式が導出された。

### 2. 磁荷分布の対応

磁束密度が $B = -\nabla \Phi_m$ の形で表される場合、$\Phi_m$ は磁位（磁気ポテンシャル）である。

$$
B = -\frac{1}{4\pi} \nabla\left(\frac{m \cdot r}{r^3}\right) = -\nabla\left[\frac{1}{4\pi}\frac{m \cdot r}{r^3}\right]
$$

したがって、磁位は：

$$
\Phi_m = \frac{1}{4\pi}\frac{m \cdot r}{r^3}
$$

これは電気双極子の電位 $\Phi = \frac{1}{4\pi\epsilon_0}\frac{p \cdot r}{r^3}$ と同様の形である。

磁荷密度 $\rho_m$ は磁位のラプラシアンで与えられる：

$$
\rho_m = -\mu_0 \nabla^2 \Phi_m
$$

原点での特異性を考慮すると、これは**磁気双極子モーメントmを持つ点磁荷双極子**に対応する。

具体的には：
- 原点に磁気双極子モーメントmが存在する
- これは正負の磁荷が微小距離だけ離れた配置（双極子）に対応する
- 磁束密度の分布は、電気双極子の電場分布と同様の形になる

