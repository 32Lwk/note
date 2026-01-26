# 電磁気学演習問題 解答 (2025年12月26日)

## 問題1: 液体中の分極

### (1-1) 電気感受率と誘電率の周波数依存性

**問題:** 極性分子（例：H₂O）を含む液体において、時刻$t=0$で一様な電場$E$を印加したとき、分極ベクトル$P(t)$の大きさが時定数$\tau$で変化し、$P(t) = \varepsilon_0\chi_{e0}E(1 - \exp(-t/\tau))$で与えられる。$\varepsilon_0$は真空の誘電率である。簡単のため、極性分子の分極が液体内の全電場$E$に与える影響は無視する。

$P(t)$が微分方程式$\tau\frac{dP}{dt} + P = \varepsilon_0\chi_{e0}E$を満たすことを用いて、単一周波数$\omega$で振動する電場$E(\omega) = E_0\exp(-i\omega t)$に対する電気感受率$\chi_e(\omega)$を、$\chi_{e0}$、$\tau$、$\omega$で表せ。また、液体の誘電率$\varepsilon(\omega)$の実部と虚部が$\omega$に対してどのように変化するか図示せよ。

**ヒント:** 分極ベクトルが$P(\omega) = P_0\exp(-i\omega t)$のように変化すると仮定し、$\chi_e(\omega) = P(\omega)/(\varepsilon_0 E(\omega))$を計算せよ。

**解答:**

**ステップ1: 微分方程式の確認**

与えられた微分方程式:
$$\tau\frac{dP}{dt} + P = \varepsilon_0\chi_{e0}E$$

この式が$P(t) = \varepsilon_0\chi_{e0}E(1 - \exp(-t/\tau))$を満たすことを確認する。

左辺:
$$\tau\frac{dP}{dt} + P = \tau \cdot \varepsilon_0\chi_{e0}E \cdot \frac{1}{\tau}\exp(-t/\tau) + \varepsilon_0\chi_{e0}E(1 - \exp(-t/\tau))$$

$$= \varepsilon_0\chi_{e0}E\exp(-t/\tau) + \varepsilon_0\chi_{e0}E - \varepsilon_0\chi_{e0}E\exp(-t/\tau) = \varepsilon_0\chi_{e0}E$$

右辺と一致する。✓

**ステップ2: 振動電場に対する分極の応答**

電場が$E(\omega) = E_0\exp(-i\omega t)$で振動する場合、分極も同じ周波数で振動すると仮定する:
$$P(\omega) = P_0\exp(-i\omega t)$$

これを微分方程式に代入する:
$$\tau\frac{dP}{dt} + P = \varepsilon_0\chi_{e0}E$$

$$\tau \cdot (-i\omega)P_0\exp(-i\omega t) + P_0\exp(-i\omega t) = \varepsilon_0\chi_{e0}E_0\exp(-i\omega t)$$

両辺を$\exp(-i\omega t)$で割ると:
$$\tau(-i\omega)P_0 + P_0 = \varepsilon_0\chi_{e0}E_0$$

$$P_0(1 - i\omega\tau) = \varepsilon_0\chi_{e0}E_0$$

$$P_0 = \frac{\varepsilon_0\chi_{e0}E_0}{1 - i\omega\tau}$$

**ステップ3: 電気感受率の計算**

電気感受率の定義:
$$\chi_e(\omega) = \frac{P(\omega)}{\varepsilon_0 E(\omega)} = \frac{P_0\exp(-i\omega t)}{\varepsilon_0 E_0\exp(-i\omega t)} = \frac{P_0}{\varepsilon_0 E_0}$$

したがって:
$$\chi_e(\omega) = \frac{\chi_{e0}}{1 - i\omega\tau}$$

分母を実数化するため、分子と分母に$(1 + i\omega\tau)$を掛ける:
$$\chi_e(\omega) = \frac{\chi_{e0}(1 + i\omega\tau)}{(1 - i\omega\tau)(1 + i\omega\tau)} = \frac{\chi_{e0}(1 + i\omega\tau)}{1 + \omega^2\tau^2}$$

$$= \frac{\chi_{e0}}{1 + \omega^2\tau^2} + i\frac{\chi_{e0}\omega\tau}{1 + \omega^2\tau^2}$$

実部と虚部を分けて:
$$\chi_e(\omega) = \chi_e'(\omega) + i\chi_e''(\omega)$$

ここで:
$$\chi_e'(\omega) = \frac{\chi_{e0}}{1 + \omega^2\tau^2}, \quad \chi_e''(\omega) = \frac{\chi_{e0}\omega\tau}{1 + \omega^2\tau^2}$$

**ステップ4: 誘電率の計算**

誘電率と電気感受率の関係:
$$\varepsilon(\omega) = \varepsilon_0[1 + \chi_e(\omega)] = \varepsilon_0 + \varepsilon_0\chi_e(\omega)$$

$$= \varepsilon_0 + \varepsilon_0\left(\frac{\chi_{e0}}{1 + \omega^2\tau^2} + i\frac{\chi_{e0}\omega\tau}{1 + \omega^2\tau^2}\right)$$

$$= \varepsilon_0\left(1 + \frac{\chi_{e0}}{1 + \omega^2\tau^2}\right) + i\varepsilon_0\frac{\chi_{e0}\omega\tau}{1 + \omega^2\tau^2}$$

実部と虚部を分けて:
$$\varepsilon(\omega) = \varepsilon'(\omega) + i\varepsilon''(\omega)$$

ここで:
$$\varepsilon'(\omega) = \varepsilon_0\left(1 + \frac{\chi_{e0}}{1 + \omega^2\tau^2}\right) = \varepsilon_0 + \frac{\varepsilon_0\chi_{e0}}{1 + \omega^2\tau^2}$$

$$\varepsilon''(\omega) = \varepsilon_0\frac{\chi_{e0}\omega\tau}{1 + \omega^2\tau^2}$$

**ステップ5: 周波数依存性の図示**

$\omega$に対する$\varepsilon'(\omega)$と$\varepsilon''(\omega)$の変化を考察する。

**実部$\varepsilon'(\omega)$:**
- $\omega = 0$のとき: $\varepsilon'(0) = \varepsilon_0(1 + \chi_{e0})$（最大値）
- $\omega \to \infty$のとき: $\varepsilon'(\infty) = \varepsilon_0$（最小値）
- $\omega\tau = 1$のとき: $\varepsilon'(\omega) = \varepsilon_0(1 + \chi_{e0}/2)$（中間値）
- $\omega$が増加すると、$\varepsilon'(\omega)$は単調減少する

**虚部$\varepsilon''(\omega)$:**
- $\omega = 0$のとき: $\varepsilon''(0) = 0$
- $\omega \to \infty$のとき: $\varepsilon''(\infty) = 0$
- $\omega\tau = 1$のとき: $\varepsilon''(\omega) = \varepsilon_0\chi_{e0}/2$（最大値）
- $\omega\tau \ll 1$のとき: $\varepsilon''(\omega) \approx \varepsilon_0\chi_{e0}\omega\tau$（線形増加）
- $\omega\tau \gg 1$のとき: $\varepsilon''(\omega) \approx \varepsilon_0\chi_{e0}/(\omega\tau)$（逆比例減少）

![誘電率の周波数依存性](electromagnetism_exercise_20251226_fig1_dielectric_dispersion.png)

**答え:**

$$\chi_e(\omega) = \frac{\chi_{e0}}{1 - i\omega\tau} = \frac{\chi_{e0}}{1 + \omega^2\tau^2}(1 + i\omega\tau)$$

$$\varepsilon(\omega) = \varepsilon_0\left(1 + \frac{\chi_{e0}}{1 + \omega^2\tau^2}\right) + i\varepsilon_0\frac{\chi_{e0}\omega\tau}{1 + \omega^2\tau^2}$$

**物理的意味と考察:**

1. **緩和時間$\tau$の意味:**
   - $\tau$は極性分子が電場に応答するまでの時間を表す
   - 分子の回転や配向の緩和時間に対応する
   - 液体の粘性や温度に依存する

2. **実部$\varepsilon'(\omega)$の物理的意味:**
   - 誘電率の実部は、電場に対する分極の応答の大きさを表す
   - 低周波数（$\omega\tau \ll 1$）では、分子が電場に完全に追従でき、最大の分極が生じる
   - 高周波数（$\omega\tau \gg 1$）では、分子が電場の変化に追従できず、分極が小さくなる（誘電分散）

3. **虚部$\varepsilon''(\omega)$の物理的意味:**
   - 誘電率の虚部は、電場エネルギーの吸収を表す
   - $\omega\tau = 1$付近で最大となり、この周波数で最も効率的にエネルギーが吸収される
   - これは**誘電損失**や**誘電緩和**と呼ばれる現象である

4. **デバイ緩和モデル:**
   - この結果は、**デバイ緩和モデル**（Debye relaxation model）として知られている
   - 極性液体や誘電体の周波数分散を記述する基本的なモデルである

5. **実験的意義:**
   - 誘電率の周波数依存性を測定することで、分子の緩和時間$\tau$を決定できる
   - 誘電分光法（dielectric spectroscopy）の基礎となる

---

### (1-2) 電場エネルギーの吸収率

**問題:** 液体による電場エネルギーの吸収率を求めよ。前問の単一周波数で振動する電場について、誘電体の微視的な変形エネルギー密度の時間変化率$dw/dt = \text{Re}\{E\} \cdot \text{Re}\{dP/dt\}$の1周期にわたる時間平均$\langle dw/dt \rangle$を、$\varepsilon_0$、$\chi_{e0}$、$\tau$、$\omega$、$E_0$で表せ。

**注意:** $\text{Re}\{\}$は実部を取ることを意味する。$E_0$は一般に複素数である。

**解答:**

**ステップ1: 電場と分極の実部の計算**

電場:
$$E(\omega) = E_0\exp(-i\omega t)$$

実部:
$$\text{Re}\{E\} = \text{Re}\{E_0\exp(-i\omega t)\} = \text{Re}\{E_0(\cos\omega t - i\sin\omega t)\}$$

$E_0$を複素数として$E_0 = |E_0|\exp(i\phi)$と表すと:
$$E(\omega) = |E_0|\exp(i\phi)\exp(-i\omega t) = |E_0|\exp(-i(\omega t - \phi))$$

$$\text{Re}\{E\} = |E_0|\cos(\omega t - \phi)$$

分極:
$$P(\omega) = P_0\exp(-i\omega t) = \frac{\varepsilon_0\chi_{e0}E_0}{1 - i\omega\tau}\exp(-i\omega t)$$

$$= \frac{\varepsilon_0\chi_{e0}|E_0|\exp(i\phi)}{1 - i\omega\tau}\exp(-i\omega t) = \frac{\varepsilon_0\chi_{e0}|E_0|}{1 - i\omega\tau}\exp(-i(\omega t - \phi))$$

実部を計算するため、$1/(1 - i\omega\tau)$を極形式で表す:
$$\frac{1}{1 - i\omega\tau} = \frac{1 + i\omega\tau}{1 + \omega^2\tau^2} = \frac{1}{\sqrt{1 + \omega^2\tau^2}}\exp(i\delta)$$

ここで、$\tan\delta = \omega\tau$、$\delta = \arctan(\omega\tau)$である。

したがって:
$$P(\omega) = \frac{\varepsilon_0\chi_{e0}|E_0|}{\sqrt{1 + \omega^2\tau^2}}\exp(i(\delta - \phi))\exp(-i\omega t)$$

$$= \frac{\varepsilon_0\chi_{e0}|E_0|}{\sqrt{1 + \omega^2\tau^2}}\exp(-i(\omega t - \delta + \phi))$$

実部:
$$\text{Re}\{P\} = \frac{\varepsilon_0\chi_{e0}|E_0|}{\sqrt{1 + \omega^2\tau^2}}\cos(\omega t - \delta + \phi)$$

分極の時間微分:
$$\frac{dP}{dt} = -i\omega P_0\exp(-i\omega t) = -i\omega \frac{\varepsilon_0\chi_{e0}E_0}{1 - i\omega\tau}\exp(-i\omega t)$$

実部:
$$\text{Re}\left\{\frac{dP}{dt}\right\} = \text{Re}\left\{-i\omega \frac{\varepsilon_0\chi_{e0}|E_0|}{\sqrt{1 + \omega^2\tau^2}}\exp(-i(\omega t - \delta + \phi))\right\}$$

$$= \text{Re}\left\{-i\omega \frac{\varepsilon_0\chi_{e0}|E_0|}{\sqrt{1 + \omega^2\tau^2}}[\cos(\omega t - \delta + \phi) - i\sin(\omega t - \delta + \phi)]\right\}$$

$$= \omega \frac{\varepsilon_0\chi_{e0}|E_0|}{\sqrt{1 + \omega^2\tau^2}}\sin(\omega t - \delta + \phi)$$

**ステップ2: エネルギー吸収率の計算**

エネルギー密度の時間変化率:
$$\frac{dw}{dt} = \text{Re}\{E\} \cdot \text{Re}\left\{\frac{dP}{dt}\right\}$$

$$= |E_0|\cos(\omega t - \phi) \cdot \omega \frac{\varepsilon_0\chi_{e0}|E_0|}{\sqrt{1 + \omega^2\tau^2}}\sin(\omega t - \delta + \phi)$$

$$= \omega \frac{\varepsilon_0\chi_{e0}|E_0|^2}{\sqrt{1 + \omega^2\tau^2}}\cos(\omega t - \phi)\sin(\omega t - \delta + \phi)$$

三角関数の積の公式:
$$\cos A \sin B = \frac{1}{2}[\sin(A + B) - \sin(A - B)]$$

ここで、$A = \omega t - \phi$、$B = \omega t - \delta + \phi$とすると:
$$A + B = 2\omega t - \delta, \quad A - B = \phi - \delta$$

したがって:
$$\frac{dw}{dt} = \omega \frac{\varepsilon_0\chi_{e0}|E_0|^2}{2\sqrt{1 + \omega^2\tau^2}}[\sin(2\omega t - \delta) - \sin(\phi - \delta)]$$

**ステップ3: 時間平均の計算**

1周期$T = 2\pi/\omega$にわたる時間平均:
$$\left\langle \frac{dw}{dt} \right\rangle = \frac{1}{T}\int_0^T \frac{dw}{dt} dt = \frac{\omega}{2\pi}\int_0^{2\pi/\omega} \frac{dw}{dt} dt$$

$$= \frac{\omega}{2\pi}\int_0^{2\pi/\omega} \omega \frac{\varepsilon_0\chi_{e0}|E_0|^2}{2\sqrt{1 + \omega^2\tau^2}}[\sin(2\omega t - \delta) - \sin(\phi - \delta)] dt$$

$$= \frac{\omega^2 \varepsilon_0\chi_{e0}|E_0|^2}{4\pi\sqrt{1 + \omega^2\tau^2}}\int_0^{2\pi/\omega} [\sin(2\omega t - \delta) - \sin(\phi - \delta)] dt$$

$\sin(2\omega t - \delta)$の1周期の積分は0である。$\sin(\phi - \delta)$は定数なので:
$$\left\langle \frac{dw}{dt} \right\rangle = -\frac{\omega^2 \varepsilon_0\chi_{e0}|E_0|^2}{4\pi\sqrt{1 + \omega^2\tau^2}}\sin(\phi - \delta) \cdot \frac{2\pi}{\omega}$$

$$= -\frac{\omega \varepsilon_0\chi_{e0}|E_0|^2}{2\sqrt{1 + \omega^2\tau^2}}\sin(\phi - \delta)$$

$\sin(\phi - \delta) = \sin\phi\cos\delta - \cos\phi\sin\delta$であるが、より直接的な方法として、複素数の関係を利用する。

**別のアプローチ: 複素数の実部を直接計算**

より簡潔に、複素数の実部の積の公式を使う:
$$\text{Re}\{z_1\} \cdot \text{Re}\{z_2\} = \frac{1}{2}\text{Re}\{z_1 z_2^*\} + \frac{1}{2}\text{Re}\{z_1 z_2\}$$

ここで、$z_1^*$は$z_1$の複素共役である。

しかし、より直接的な方法として、$E$と$dP/dt$の複素表現を使う:
$$E = E_0\exp(-i\omega t), \quad \frac{dP}{dt} = -i\omega P_0\exp(-i\omega t) = -i\omega \frac{\varepsilon_0\chi_{e0}E_0}{1 - i\omega\tau}\exp(-i\omega t)$$

実部の積の時間平均は:
$$\left\langle \text{Re}\{E\} \cdot \text{Re}\left\{\frac{dP}{dt}\right\} \right\rangle = \frac{1}{2}\text{Re}\left\{E_0 \left(-i\omega \frac{\varepsilon_0\chi_{e0}E_0^*}{1 + i\omega\tau}\right)\right\}$$

ここで、$E_0^*$は$E_0$の複素共役である。

$$= \frac{1}{2}\text{Re}\left\{-i\omega \frac{\varepsilon_0\chi_{e0}|E_0|^2}{1 + i\omega\tau}\right\}$$

$$= \frac{1}{2}\text{Re}\left\{-i\omega \varepsilon_0\chi_{e0}|E_0|^2 \cdot \frac{1 - i\omega\tau}{1 + \omega^2\tau^2}\right\}$$

$$= \frac{1}{2}\text{Re}\left\{-i\omega \varepsilon_0\chi_{e0}|E_0|^2 \cdot \frac{1 - i\omega\tau}{1 + \omega^2\tau^2}\right\}$$

$$= \frac{1}{2}\text{Re}\left\{-i\omega \varepsilon_0\chi_{e0}|E_0|^2 \cdot \frac{1}{1 + \omega^2\tau^2} - \omega^2\tau \varepsilon_0\chi_{e0}|E_0|^2 \cdot \frac{1}{1 + \omega^2\tau^2}\right\}$$

$$= \frac{1}{2}\text{Re}\left\{-i\omega \varepsilon_0\chi_{e0}|E_0|^2 \cdot \frac{1}{1 + \omega^2\tau^2} - \omega^2\tau \varepsilon_0\chi_{e0}|E_0|^2 \cdot \frac{1}{1 + \omega^2\tau^2}\right\}$$

$-i$の実部は0なので、第2項のみが残る:
$$\left\langle \frac{dw}{dt} \right\rangle = -\frac{1}{2} \cdot \frac{\omega^2\tau \varepsilon_0\chi_{e0}|E_0|^2}{1 + \omega^2\tau^2}$$

符号が負になっているが、これはエネルギーが**吸収される**ことを意味する（$dw/dt < 0$はエネルギーが減少することを意味するが、ここでは外部からエネルギーが供給されるため、正の値として解釈する必要がある）。

実際には、$dw/dt$は**単位体積あたりのエネルギー吸収率**なので、正の値が吸収を表す。符号を修正すると:
$$\left\langle \frac{dw}{dt} \right\rangle = \frac{1}{2} \cdot \frac{\omega^2\tau \varepsilon_0\chi_{e0}|E_0|^2}{1 + \omega^2\tau^2}$$

**より正確な導出:**

実部の積の時間平均を直接計算する。$E = E_0\exp(-i\omega t)$、$P = P_0\exp(-i\omega t)$とすると:
$$\text{Re}\{E\} = \frac{E + E^*}{2}, \quad \text{Re}\left\{\frac{dP}{dt}\right\} = \frac{dP/dt + (dP/dt)^*}{2}$$

$$\left\langle \text{Re}\{E\} \cdot \text{Re}\left\{\frac{dP}{dt}\right\} \right\rangle = \frac{1}{4}\left\langle (E + E^*)\left(\frac{dP}{dt} + \left(\frac{dP}{dt}\right)^*\right) \right\rangle$$

$$= \frac{1}{4}\left\langle E\frac{dP}{dt} + E\left(\frac{dP}{dt}\right)^* + E^*\frac{dP}{dt} + E^*\left(\frac{dP}{dt}\right)^* \right\rangle$$

時間平均を取ると、$\exp(\pm 2i\omega t)$の項は0になり、$\exp(0)$の項のみが残る:
$$\left\langle E\left(\frac{dP}{dt}\right)^* \right\rangle = \left\langle E_0\exp(-i\omega t) \cdot i\omega P_0^*\exp(i\omega t) \right\rangle = i\omega E_0 P_0^*$$

$$\left\langle E^*\frac{dP}{dt} \right\rangle = \left\langle E_0^*\exp(i\omega t) \cdot (-i\omega)P_0\exp(-i\omega t) \right\rangle = -i\omega E_0^* P_0$$

したがって:
$$\left\langle \frac{dw}{dt} \right\rangle = \frac{1}{4}[i\omega E_0 P_0^* - i\omega E_0^* P_0] = \frac{i\omega}{4}[E_0 P_0^* - E_0^* P_0]$$

$$= \frac{i\omega}{4} \cdot 2i\text{Im}\{E_0 P_0^*\} = -\frac{\omega}{2}\text{Im}\{E_0 P_0^*\}$$

$P_0 = \varepsilon_0\chi_e(\omega)E_0$なので:
$$E_0 P_0^* = E_0 \varepsilon_0\chi_e^*(\omega)E_0^* = \varepsilon_0\chi_e^*(\omega)|E_0|^2$$

$$\chi_e(\omega) = \frac{\chi_{e0}}{1 - i\omega\tau} = \frac{\chi_{e0}(1 + i\omega\tau)}{1 + \omega^2\tau^2}$$

$$\chi_e^*(\omega) = \frac{\chi_{e0}(1 - i\omega\tau)}{1 + \omega^2\tau^2}$$

$$\text{Im}\{\chi_e^*(\omega)\} = \text{Im}\left\{\frac{\chi_{e0}(1 - i\omega\tau)}{1 + \omega^2\tau^2}\right\} = -\frac{\chi_{e0}\omega\tau}{1 + \omega^2\tau^2}$$

したがって:
$$\left\langle \frac{dw}{dt} \right\rangle = -\frac{\omega}{2}\text{Im}\{E_0 P_0^*\} = -\frac{\omega}{2}\varepsilon_0|E_0|^2\text{Im}\{\chi_e^*(\omega)\}$$

$$= -\frac{\omega}{2}\varepsilon_0|E_0|^2 \cdot \left(-\frac{\chi_{e0}\omega\tau}{1 + \omega^2\tau^2}\right) = \frac{\omega^2\tau \varepsilon_0\chi_{e0}|E_0|^2}{2(1 + \omega^2\tau^2)}$$

**答え:**

$$\left\langle \frac{dw}{dt} \right\rangle = \frac{\omega^2\tau \varepsilon_0\chi_{e0}|E_0|^2}{2(1 + \omega^2\tau^2)}$$

![エネルギー吸収率の周波数依存性](electromagnetism_exercise_20251226_fig2_energy_absorption.png)

**物理的意味と考察:**

1. **エネルギー吸収のメカニズム:**
   - 極性分子が電場の向きに回転・配向する際に、分子間の摩擦や衝突によりエネルギーが散逸する
   - これが誘電損失として現れる

2. **周波数依存性:**
   - $\omega\tau \ll 1$（低周波数）: 分子が電場に完全に追従でき、吸収は小さい
   - $\omega\tau = 1$（緩和周波数）: 最大の吸収が起こる
   - $\omega\tau \gg 1$（高周波数）: 分子が電場の変化に追従できず、吸収は再び小さくなる

3. **誘電率の虚部との関係:**
   - 前問で求めた$\varepsilon''(\omega) = \varepsilon_0\chi_{e0}\omega\tau/(1 + \omega^2\tau^2)$と比較すると:
   $$\left\langle \frac{dw}{dt} \right\rangle = \frac{\omega}{2}\varepsilon''(\omega)|E_0|^2$$
   - これは、誘電率の虚部がエネルギー吸収を表すことを示している

4. **実用的意義:**
   - マイクロ波加熱: 水分子の誘電緩和を利用した加熱技術
   - 誘電分光法: 分子の動的挙動の研究
   - 材料の損失特性の評価

---

## 問題2: 遅延ポテンシャルと電磁場

### (2-1) 電場の積分表示式

**問題:** 真空中で、電荷密度$\rho(\mathbf{r})$と電流密度$\mathbf{i}(\mathbf{r})$が時間変化する場合を考える。スカラーポテンシャル$\phi$とベクトルポテンシャル$\mathbf{A}$が遅延ポテンシャルの公式で与えられ、電場$\mathbf{E}$が$\mathbf{E} = -\nabla\phi - \frac{\partial\mathbf{A}}{\partial t}$で表されることを用いて、電場$\mathbf{E}(\mathbf{r}, t)$が以下の積分表示式で与えられることを示せ:

$$\mathbf{E}(\mathbf{r}, t) = \frac{1}{4\pi\varepsilon_0}\int \left[\frac{\rho(\mathbf{r}', t')(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3} + \frac{1}{c}\frac{\partial\rho(\mathbf{r}', t')}{\partial t}\frac{(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^2} - \frac{1}{c^2}\frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t}\frac{1}{|\mathbf{r} - \mathbf{r}'|}\right] dV'$$

ただし、$t' = t - |\mathbf{r} - \mathbf{r}'|/c$である。

**解答:**

**ステップ1: 遅延ポテンシャルの確認**

遅延ポテンシャル:
$$\phi(\mathbf{r}, t) = \frac{1}{4\pi\varepsilon_0}\int \frac{\rho(\mathbf{r}', t')}{|\mathbf{r} - \mathbf{r}'|} dV'$$

$$\mathbf{A}(\mathbf{r}, t) = \frac{\mu_0}{4\pi}\int \frac{\mathbf{i}(\mathbf{r}', t')}{|\mathbf{r} - \mathbf{r}'|} dV'$$

ここで、$t' = t - |\mathbf{r} - \mathbf{r}'|/c$は遅延時間である。

**ステップ2: 電場の計算**

電場:
$$\mathbf{E} = -\nabla\phi - \frac{\partial\mathbf{A}}{\partial t}$$

**第1項: $-\nabla\phi$の計算**

$$\nabla\phi = \nabla \frac{1}{4\pi\varepsilon_0}\int \frac{\rho(\mathbf{r}', t')}{|\mathbf{r} - \mathbf{r}'|} dV'$$

ここで、$\nabla$は$\mathbf{r}$に関する微分である。$t' = t - |\mathbf{r} - \mathbf{r}'|/c$なので、$\rho(\mathbf{r}', t')$は$\mathbf{r}$に依存する。

$$\nabla \frac{1}{|\mathbf{r} - \mathbf{r}'|} = -\frac{\mathbf{r} - \mathbf{r}'}{|\mathbf{r} - \mathbf{r}'|^3}$$

また、$t'$の$\mathbf{r}$依存性を考慮すると:
$$\nabla t' = \nabla\left(t - \frac{|\mathbf{r} - \mathbf{r}'|}{c}\right) = -\frac{1}{c}\nabla|\mathbf{r} - \mathbf{r}'| = -\frac{1}{c}\frac{\mathbf{r} - \mathbf{r}'}{|\mathbf{r} - \mathbf{r}'|}$$

したがって:
$$\nabla\phi = \frac{1}{4\pi\varepsilon_0}\int \left[\nabla\frac{1}{|\mathbf{r} - \mathbf{r}'|}\rho(\mathbf{r}', t') + \frac{1}{|\mathbf{r} - \mathbf{r}'|}\nabla\rho(\mathbf{r}', t')\right] dV'$$

$$= \frac{1}{4\pi\varepsilon_0}\int \left[-\frac{\mathbf{r} - \mathbf{r}'}{|\mathbf{r} - \mathbf{r}'|^3}\rho(\mathbf{r}', t') + \frac{1}{|\mathbf{r} - \mathbf{r}'|}\frac{\partial\rho(\mathbf{r}', t')}{\partial t'}\nabla t'\right] dV'$$

$$= \frac{1}{4\pi\varepsilon_0}\int \left[-\frac{\mathbf{r} - \mathbf{r}'}{|\mathbf{r} - \mathbf{r}'|^3}\rho(\mathbf{r}', t') - \frac{1}{c}\frac{\partial\rho(\mathbf{r}', t')}{\partial t'}\frac{\mathbf{r} - \mathbf{r}'}{|\mathbf{r} - \mathbf{r}'|^2}\right] dV'$$

したがって:
$$-\nabla\phi = \frac{1}{4\pi\varepsilon_0}\int \left[\frac{\rho(\mathbf{r}', t')(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3} + \frac{1}{c}\frac{\partial\rho(\mathbf{r}', t')}{\partial t'}\frac{(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^2}\right] dV'$$

**第2項: $-\frac{\partial\mathbf{A}}{\partial t}$の計算**

$$\frac{\partial\mathbf{A}}{\partial t} = \frac{\partial}{\partial t}\frac{\mu_0}{4\pi}\int \frac{\mathbf{i}(\mathbf{r}', t')}{|\mathbf{r} - \mathbf{r}'|} dV'$$

$t' = t - |\mathbf{r} - \mathbf{r}'|/c$なので、$\frac{\partial t'}{\partial t} = 1$である。したがって:
$$\frac{\partial\mathbf{A}}{\partial t} = \frac{\mu_0}{4\pi}\int \frac{1}{|\mathbf{r} - \mathbf{r}'|}\frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'} \frac{\partial t'}{\partial t} dV' = \frac{\mu_0}{4\pi}\int \frac{1}{|\mathbf{r} - \mathbf{r}'|}\frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'} dV'$$

$\mu_0 = 1/(\varepsilon_0 c^2)$なので:
$$-\frac{\partial\mathbf{A}}{\partial t} = -\frac{1}{4\pi\varepsilon_0 c^2}\int \frac{1}{|\mathbf{r} - \mathbf{r}'|}\frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'} dV'$$

**ステップ3: 電場の最終形**

2つの項を合わせると:
$$\mathbf{E}(\mathbf{r}, t) = -\nabla\phi - \frac{\partial\mathbf{A}}{\partial t}$$

$$= \frac{1}{4\pi\varepsilon_0}\int \left[\frac{\rho(\mathbf{r}', t')(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3} + \frac{1}{c}\frac{\partial\rho(\mathbf{r}', t')}{\partial t'}\frac{(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^2} - \frac{1}{c^2}\frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'}\frac{1}{|\mathbf{r} - \mathbf{r}'|}\right] dV'$$

ここで、$\frac{\partial\rho(\mathbf{r}', t')}{\partial t'}$は$t'$に関する偏微分であるが、$t' = t - |\mathbf{r} - \mathbf{r}'|/c$なので、$\frac{\partial\rho(\mathbf{r}', t')}{\partial t} = \frac{\partial\rho(\mathbf{r}', t')}{\partial t'}$である。したがって、表記を$\frac{\partial\rho(\mathbf{r}', t')}{\partial t}$に統一できる。

**答え:** 示された。

**物理的意味と考察:**

1. **第1項: 静電場の寄与**
   - $\frac{\rho(\mathbf{r}', t')(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3}$は、クーロンの法則に対応する静電場の寄与
   - ただし、電荷密度は遅延時間$t'$での値である

2. **第2項: 電荷密度の時間変化による寄与**
   - $\frac{1}{c}\frac{\partial\rho}{\partial t}\frac{(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^2}$は、電荷密度の時間変化による電場の寄与
   - これは、電荷の移動や生成・消滅による効果を表す

3. **第3項: 電流密度の時間変化による寄与**
   - $\frac{1}{c^2}\frac{\partial\mathbf{i}}{\partial t}\frac{1}{|\mathbf{r} - \mathbf{r}'|}$は、電流密度の時間変化（加速度電流）による電場の寄与
   - これは、電磁波の放射に対応する項である

4. **遅延時間の意味:**
   - $t' = t - |\mathbf{r} - \mathbf{r}'|/c$は、情報が光速$c$で伝播することを表す
   - 観測点$\mathbf{r}$での時刻$t$の電場は、電荷・電流分布の$t'$時刻の状態に依存する

5. **遠方での挙動:**
   - 遠方（$|\mathbf{r} - \mathbf{r}'| \gg \lambda$、$\lambda$は波長）では、第3項が主要となり、電磁波として伝播する

---

### (2-2) 磁場の公式

**問題:** 同様に、磁場$\mathbf{B}(\mathbf{r}, t)$の公式を導出せよ。参考として、10月3日の問題3を参照せよ。

**解答:**

**ステップ1: 磁場の定義**

磁場:
$$\mathbf{B} = \nabla \times \mathbf{A}$$

ベクトルポテンシャル:
$$\mathbf{A}(\mathbf{r}, t) = \frac{\mu_0}{4\pi}\int \frac{\mathbf{i}(\mathbf{r}', t')}{|\mathbf{r} - \mathbf{r}'|} dV'$$

ここで、$t' = t - |\mathbf{r} - \mathbf{r}'|/c$である。

**ステップ2: 回転の計算**

$$\mathbf{B} = \nabla \times \mathbf{A} = \nabla \times \frac{\mu_0}{4\pi}\int \frac{\mathbf{i}(\mathbf{r}', t')}{|\mathbf{r} - \mathbf{r}'|} dV'$$

ベクトル恒等式:
$$\nabla \times (f\mathbf{v}) = \nabla f \times \mathbf{v} + f\nabla \times \mathbf{v}$$

ここで、$f = 1/|\mathbf{r} - \mathbf{r}'|$、$\mathbf{v} = \mathbf{i}(\mathbf{r}', t')$である。$\mathbf{i}(\mathbf{r}', t')$は$\mathbf{r}'$の関数であり、$\mathbf{r}$には直接依存しないが、$t'$を通じて$\mathbf{r}$に依存する。

$$\nabla \times \frac{\mathbf{i}(\mathbf{r}', t')}{|\mathbf{r} - \mathbf{r}'|} = \nabla\frac{1}{|\mathbf{r} - \mathbf{r}'|} \times \mathbf{i}(\mathbf{r}', t') + \frac{1}{|\mathbf{r} - \mathbf{r}'|}\nabla \times \mathbf{i}(\mathbf{r}', t')$$

$$\nabla\frac{1}{|\mathbf{r} - \mathbf{r}'|} = -\frac{\mathbf{r} - \mathbf{r}'}{|\mathbf{r} - \mathbf{r}'|^3}$$

$\nabla \times \mathbf{i}(\mathbf{r}', t')$を計算する。$\mathbf{i}(\mathbf{r}', t')$は$\mathbf{r}'$の関数であり、$t' = t - |\mathbf{r} - \mathbf{r}'|/c$を通じて$\mathbf{r}$に依存する。

$$\nabla \times \mathbf{i}(\mathbf{r}', t') = \nabla \times \mathbf{i}(\mathbf{r}', t - |\mathbf{r} - \mathbf{r}'|/c)$$

$$= \frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'} \times \nabla t' = \frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'} \times \left(-\frac{1}{c}\frac{\mathbf{r} - \mathbf{r}'}{|\mathbf{r} - \mathbf{r}'|}\right)$$

$$= -\frac{1}{c}\frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'} \times \frac{\mathbf{r} - \mathbf{r}'}{|\mathbf{r} - \mathbf{r}'|}$$

したがって:
$$\mathbf{B} = \frac{\mu_0}{4\pi}\int \left[-\frac{\mathbf{r} - \mathbf{r}'}{|\mathbf{r} - \mathbf{r}'|^3} \times \mathbf{i}(\mathbf{r}', t') - \frac{1}{c}\frac{1}{|\mathbf{r} - \mathbf{r}'|}\frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'} \times \frac{\mathbf{r} - \mathbf{r}'}{|\mathbf{r} - \mathbf{r}'|}\right] dV'$$

$$= \frac{\mu_0}{4\pi}\int \left[\frac{\mathbf{i}(\mathbf{r}', t') \times (\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3} + \frac{1}{c}\frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'} \times \frac{(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^2}\right] dV'$$

$\mu_0 = 1/(\varepsilon_0 c^2)$なので:
$$\mathbf{B}(\mathbf{r}, t) = \frac{1}{4\pi\varepsilon_0 c^2}\int \left[\frac{\mathbf{i}(\mathbf{r}', t') \times (\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3} + \frac{1}{c}\frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'} \times \frac{(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^2}\right] dV'$$

または、より一般的な形として:
$$\mathbf{B}(\mathbf{r}, t) = \frac{\mu_0}{4\pi}\int \left[\frac{\mathbf{i}(\mathbf{r}', t') \times (\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3} + \frac{1}{c}\frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'} \times \frac{(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^2}\right] dV'$$

**答え:**

$$\mathbf{B}(\mathbf{r}, t) = \frac{\mu_0}{4\pi}\int \left[\frac{\mathbf{i}(\mathbf{r}', t') \times (\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3} + \frac{1}{c}\frac{\partial\mathbf{i}(\mathbf{r}', t')}{\partial t'} \times \frac{(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^2}\right] dV'$$

**物理的意味と考察:**

1. **第1項: ビオ・サバールの法則の寄与**
   - $\frac{\mathbf{i}(\mathbf{r}', t') \times (\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3}$は、ビオ・サバールの法則に対応する静磁場の寄与
   - ただし、電流密度は遅延時間$t'$での値である

2. **第2項: 電流密度の時間変化による寄与**
   - $\frac{1}{c}\frac{\partial\mathbf{i}}{\partial t'} \times \frac{(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^2}$は、電流密度の時間変化による磁場の寄与
   - これは、変位電流や電磁誘導に対応する項である

3. **電場と磁場の対称性:**
   - 電場の公式と比較すると、電荷密度と電流密度の役割が対称的であることがわかる
   - これは、マクスウェル方程式の対称性を反映している

4. **電磁波の伝播:**
   - 遠方では、時間変化項が主要となり、電場と磁場が結合して電磁波として伝播する

---

## 問題3: 誘電体球による光の吸収と散乱

### (3-1) 吸収断面積

**問題:** 真空中（誘電率$\varepsilon_0$）に置かれた小さな誘電体球（体積$V$、複素誘電率$\varepsilon = \varepsilon' + i\varepsilon''$）による光の吸収と散乱を考える。入射光は単色光で、外部電場$E_e = E_0\exp(-i\omega t)$が単一周波数$\omega$で振動している。真空中の光のエネルギー流束（ポインティングベクトルの大きさ）$S$の時間平均は$\langle S \rangle = c\varepsilon_0|E_0|^2/2$で与えられる。$c$は光速である。誘電体球は光の波長より十分小さく、その分極は位相が一致した振動双極子$\mathbf{p}$で近似される。

吸収断面積$C_a$を$c$、$V$、$\varepsilon_0$、$\varepsilon'$、$\varepsilon''$、$\omega$で表せ。ただし、吸収断面積は、単位時間あたりの吸収エネルギー$dW_a/dt$の時間平均$\langle dW_a/dt \rangle$を用いて、$C_a = \langle dW_a/dt \rangle / \langle S \rangle$で定義される。

参考として、問題(1-2)と11月14日の問題2の、誘電体球の分極$\mathbf{P}$と電場$E_e$に関する単位体積あたりの吸収エネルギー率の公式を用いよ。

**解答:**

**ステップ1: 誘電体球の分極**

誘電体球が十分小さい場合、球内の電場は一様とみなせる。外部電場$E_e = E_0\exp(-i\omega t)$に対して、球内の電場は境界条件から決定される。

小さな誘電体球の場合、静電場の近似が成り立つ。球内の電場:
$$E_{\text{内部}} = \frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}E_e = \frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}E_0\exp(-i\omega t)$$

分極ベクトル:
$$\mathbf{P} = (\varepsilon - \varepsilon_0)\mathbf{E}_{\text{内部}} = (\varepsilon - \varepsilon_0)\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}E_0\exp(-i\omega t)$$

双極子モーメント:
$$\mathbf{p} = V\mathbf{P} = V(\varepsilon - \varepsilon_0)\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}E_0\exp(-i\omega t)$$

**ステップ2: 単位体積あたりの吸収エネルギー率**

問題(1-2)の結果より、単位体積あたりの吸収エネルギー率の時間平均は:
$$\left\langle \frac{dw}{dt} \right\rangle = \frac{\omega}{2}\varepsilon''(\omega)|E|^2$$

ここで、$E$は球内の電場、$\varepsilon''$は誘電率の虚部である。

球内の電場の大きさ:
$$|E_{\text{内部}}|^2 = \left|\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}E_0\right|^2 = \frac{9\varepsilon_0^2}{|2\varepsilon_0 + \varepsilon|^2}|E_0|^2$$

誘電率の虚部$\varepsilon''$を用いると、球内での単位体積あたりの吸収エネルギー率:
$$\left\langle \frac{dw}{dt} \right\rangle = \frac{\omega}{2}\varepsilon''\left|\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}\right|^2|E_0|^2$$

**ステップ3: 全吸収エネルギー率**

球全体での吸収エネルギー率:
$$\left\langle \frac{dW_a}{dt} \right\rangle = V \left\langle \frac{dw}{dt} \right\rangle = V \cdot \frac{\omega}{2}\varepsilon''\left|\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}\right|^2|E_0|^2$$

**ステップ4: 吸収断面積の計算**

吸収断面積:
$$C_a = \frac{\langle dW_a/dt \rangle}{\langle S \rangle} = \frac{V \cdot \frac{\omega}{2}\varepsilon''\left|\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}\right|^2|E_0|^2}{\frac{c\varepsilon_0|E_0|^2}{2}}$$

$$= \frac{V\omega\varepsilon''}{c\varepsilon_0}\left|\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}\right|^2$$

$\varepsilon = \varepsilon' + i\varepsilon''$なので、$|2\varepsilon_0 + \varepsilon|^2 = |2\varepsilon_0 + \varepsilon' + i\varepsilon''|^2 = (2\varepsilon_0 + \varepsilon')^2 + (\varepsilon'')^2$

したがって:
$$C_a = \frac{V\omega\varepsilon''}{c\varepsilon_0} \cdot \frac{9\varepsilon_0^2}{(2\varepsilon_0 + \varepsilon')^2 + (\varepsilon'')^2}$$

$$= \frac{9V\omega\varepsilon_0\varepsilon''}{c[(2\varepsilon_0 + \varepsilon')^2 + (\varepsilon'')^2]}$$

**より簡潔な表現:**

$\varepsilon'' \ll \varepsilon'$の場合（弱い吸収）:
$$C_a \approx \frac{9V\omega\varepsilon_0\varepsilon''}{c(2\varepsilon_0 + \varepsilon')^2}$$

**答え:**

$$C_a = \frac{9V\omega\varepsilon_0\varepsilon''}{c[(2\varepsilon_0 + \varepsilon')^2 + (\varepsilon'')^2]}$$

![吸収断面積の周波数依存性](electromagnetism_exercise_20251226_fig3_absorption_cross_section.png)

**物理的意味と考察:**

1. **吸収のメカニズム:**
   - 誘電体球内で電場が振動し、分子の分極や電子の遷移によりエネルギーが吸収される
   - 誘電率の虚部$\varepsilon''$が吸収の強さを表す

2. **体積依存性:**
   - 吸収断面積は体積$V$に比例する
   - これは、球が小さい場合の近似である

3. **周波数依存性:**
   - $\omega$に比例する項があるが、$\varepsilon''$も周波数依存性を持つ
   - 実際の吸収スペクトルは、$\varepsilon''(\omega)$の周波数依存性に支配される

4. **誘電率の実部との関係:**
   - 分母に$(2\varepsilon_0 + \varepsilon')^2$が現れる
   - これは、球内の電場が誘電率の実部に依存することを示す

5. **応用:**
   - ナノ粒子による光吸収の研究
   - 太陽電池の光吸収効率の向上
   - 生体組織の光吸収特性の解析

---

### (3-2) 散乱断面積

**問題:** 散乱断面積$C_s$を$c$、$V$、$\varepsilon_0$、$\varepsilon$、$\omega$で表せ。ただし、散乱断面積は、単位時間あたりの散乱エネルギー$dW_s/dt$の時間平均$\langle dW_s/dt \rangle$を用いて、$C_s = \langle dW_s/dt \rangle / \langle S \rangle$で定義される。

時間平均$\langle dW_s/dt \rangle$は、$\langle (\text{Re}\{d^2\mathbf{p}/dt^2\})^2 \rangle / (6\pi\varepsilon_0 c^3)$で与えられる。

**解答:**

**ステップ1: 双極子モーメントの時間微分**

双極子モーメント:
$$\mathbf{p} = V(\varepsilon - \varepsilon_0)\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}E_0\exp(-i\omega t)$$

1階時間微分:
$$\frac{d\mathbf{p}}{dt} = -i\omega V(\varepsilon - \varepsilon_0)\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}E_0\exp(-i\omega t)$$

2階時間微分:
$$\frac{d^2\mathbf{p}}{dt^2} = (i\omega)^2 V(\varepsilon - \varepsilon_0)\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}E_0\exp(-i\omega t) = -\omega^2 V(\varepsilon - \varepsilon_0)\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}E_0\exp(-i\omega t)$$

実部:
$$\text{Re}\left\{\frac{d^2\mathbf{p}}{dt^2}\right\} = \text{Re}\left\{-\omega^2 V(\varepsilon - \varepsilon_0)\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}E_0\exp(-i\omega t)\right\}$$

$E_0$を実数と仮定すると（一般性を失わず、位相を0に取れる）:
$$\text{Re}\left\{\frac{d^2\mathbf{p}}{dt^2}\right\} = -\omega^2 V \text{Re}\left\{(\varepsilon - \varepsilon_0)\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}\right\}E_0\cos\omega t$$

**ステップ2: 散乱エネルギー率の計算**

与えられた公式:
$$\left\langle \frac{dW_s}{dt} \right\rangle = \frac{\left\langle \left(\text{Re}\left\{\frac{d^2\mathbf{p}}{dt^2}\right\}\right)^2 \right\rangle}{6\pi\varepsilon_0 c^3}$$

$$\left(\text{Re}\left\{\frac{d^2\mathbf{p}}{dt^2}\right\}\right)^2 = \omega^4 V^2 \left|\text{Re}\left\{(\varepsilon - \varepsilon_0)\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}\right\}\right|^2 E_0^2\cos^2\omega t$$

時間平均:
$$\langle \cos^2\omega t \rangle = \frac{1}{2}$$

したがって:
$$\left\langle \left(\text{Re}\left\{\frac{d^2\mathbf{p}}{dt^2}\right\}\right)^2 \right\rangle = \frac{\omega^4 V^2}{2}\left|\text{Re}\left\{(\varepsilon - \varepsilon_0)\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}\right\}\right|^2 E_0^2$$

より正確には、$\text{Re}\{z\}^2$の時間平均を計算する必要がある。$z = z_0\exp(-i\omega t)$とすると:
$$\text{Re}\{z\} = |z_0|\cos(\omega t - \phi)$$

$$\langle (\text{Re}\{z\})^2 \rangle = |z_0|^2\langle \cos^2(\omega t - \phi) \rangle = \frac{|z_0|^2}{2}$$

したがって:
$$\left\langle \left(\text{Re}\left\{\frac{d^2\mathbf{p}}{dt^2}\right\}\right)^2 \right\rangle = \frac{\omega^4 V^2}{2}\left|(\varepsilon - \varepsilon_0)\frac{3\varepsilon_0}{2\varepsilon_0 + \varepsilon}\right|^2|E_0|^2$$

$$= \frac{\omega^4 V^2}{2}\left|\frac{3\varepsilon_0(\varepsilon - \varepsilon_0)}{2\varepsilon_0 + \varepsilon}\right|^2|E_0|^2$$

したがって:
$$\left\langle \frac{dW_s}{dt} \right\rangle = \frac{\omega^4 V^2}{12\pi\varepsilon_0 c^3}\left|\frac{3\varepsilon_0(\varepsilon - \varepsilon_0)}{2\varepsilon_0 + \varepsilon}\right|^2|E_0|^2$$

**ステップ3: 散乱断面積の計算**

散乱断面積:
$$C_s = \frac{\langle dW_s/dt \rangle}{\langle S \rangle} = \frac{\frac{\omega^4 V^2}{12\pi\varepsilon_0 c^3}\left|\frac{3\varepsilon_0(\varepsilon - \varepsilon_0)}{2\varepsilon_0 + \varepsilon}\right|^2|E_0|^2}{\frac{c\varepsilon_0|E_0|^2}{2}}$$

$$= \frac{\omega^4 V^2}{12\pi\varepsilon_0 c^3} \cdot \frac{2}{c\varepsilon_0}\left|\frac{3\varepsilon_0(\varepsilon - \varepsilon_0)}{2\varepsilon_0 + \varepsilon}\right|^2$$

$$= \frac{\omega^4 V^2}{6\pi\varepsilon_0^2 c^4}\left|\frac{3\varepsilon_0(\varepsilon - \varepsilon_0)}{2\varepsilon_0 + \varepsilon}\right|^2$$

$$= \frac{\omega^4 V^2}{6\pi c^4}\left|\frac{3(\varepsilon - \varepsilon_0)}{2\varepsilon_0 + \varepsilon}\right|^2$$

$\omega = 2\pi c/\lambda$（$\lambda$は波長）なので、$\omega^4 = (2\pi c/\lambda)^4$であるが、ここでは$\omega$のまま表す。

**答え:**

$$C_s = \frac{\omega^4 V^2}{6\pi c^4}\left|\frac{3(\varepsilon - \varepsilon_0)}{2\varepsilon_0 + \varepsilon}\right|^2$$

![散乱断面積の周波数依存性](electromagnetism_exercise_20251226_fig4_scattering_cross_section.png)

**物理的意味と考察:**

1. **レイリー散乱:**
   - この結果は、**レイリー散乱**（Rayleigh scattering）の公式に対応する
   - 粒子が波長より十分小さい場合の散乱を記述する

2. **周波数依存性:**
   - 散乱断面積は$\omega^4$に比例する（$\lambda^{-4}$に比例）
   - これが、空が青く見える理由である（短波長の光がより強く散乱される）

3. **体積依存性:**
   - 散乱断面積は$V^2$に比例する
   - これは、吸収断面積が$V$に比例するのと対照的である

4. **誘電率依存性:**
   - $|(\varepsilon - \varepsilon_0)/(2\varepsilon_0 + \varepsilon)|^2$の項が現れる
   - 誘電率が真空の誘電率に近い場合、散乱は弱い
   - 誘電率が大きい場合、散乱は強くなる

5. **応用:**
   - 大気中の光散乱（空の色、夕焼け）
   - 生体組織の光散乱
   - ナノ粒子の光散乱特性
   - レーザー光の散乱

---

## 問題4: 界面での反射と透過

### 問題設定の詳細

平面電磁波が真空中から物質へ垂直入射する場合を考える。この問題では、以下の重要な物理現象を理解する必要がある:

1. **電磁波の境界条件:** 電場と磁場の接線成分が連続
2. **特性インピーダンス:** 媒質の電磁的特性を表す重要なパラメータ
3. **反射と透過:** エネルギー保存則に基づく反射率と透過率の関係
4. **位相変化:** 反射波の位相が入射波に対してどのように変化するか

![電磁波の入射・反射・透過の模式図](electromagnetism_exercise_20251226_fig6_wave_reflection_diagram.png)

**図の説明:**
- **青い矢印:** 入射波と透過波の電場（x方向）
- **赤い矢印:** 反射波の電場（x方向、反転）
- **青い丸:** 入射波と透過波の磁場（y方向、画面奥方向）
- **赤い丸:** 反射波の磁場（y方向、画面手前方向）
- **黒い破線:** 界面（z=0）

### (4-1) 反射率

**問題:** 角周波数$\omega$、波数$k$の平面電磁波（$\mathbf{E} = E_0\exp[i(kz - \omega t)]$、$\mathbf{H} = H_0\exp[i(kz - \omega t)]$）が、真空中（誘電率$\varepsilon_0$、透磁率$\mu_0$）から物質（誘電率$\varepsilon$、透磁率$\mu$、$\varepsilon$と$\mu$は実数）へ、$z$方向に垂直に入射する。界面は$z=0$にあり、物質は$z \geq 0$の領域を占める。

$\varepsilon_0$、$\mu_0$、$\varepsilon$、$\mu$を用いて反射率を求めよ。ただし、平面波がマクスウェル方程式を満たす条件の1つである$k = \omega\sqrt{\varepsilon\mu}$の関係を用いよ。講義で用いた近似$\mu = \mu_0$は用いないこと。

**解答:**

**ステップ1: 境界条件の設定**

入射波、反射波、透過波を以下のように表す:

**入射波（真空中、$z < 0$）:**
$$\mathbf{E}_i = E_{i0}\exp[i(k_0 z - \omega t)]\hat{\mathbf{x}}$$
$$\mathbf{H}_i = H_{i0}\exp[i(k_0 z - \omega t)]\hat{\mathbf{y}}$$

ここで、$k_0 = \omega\sqrt{\varepsilon_0\mu_0}$、$H_{i0} = E_{i0}/(\eta_0)$、$\eta_0 = \sqrt{\mu_0/\varepsilon_0}$は真空中の特性インピーダンスである。

**重要なポイント:**
- 平面波では、電場と磁場は互いに垂直で、進行方向にも垂直である（横波）
- 電場と磁場の振幅比は特性インピーダンスで決まる: $E/H = \eta$
- 真空中の特性インピーダンス: $\eta_0 = \sqrt{\mu_0/\varepsilon_0} \approx 377\,\Omega$

**反射波（真空中、$z < 0$）:**
$$\mathbf{E}_r = E_{r0}\exp[i(-k_0 z - \omega t)]\hat{\mathbf{x}}$$
$$\mathbf{H}_r = -H_{r0}\exp[i(-k_0 z - \omega t)]\hat{\mathbf{y}}$$

ここで、$H_{r0} = E_{r0}/(\eta_0)$である。反射波の進行方向が$-z$方向なので、$\mathbf{H}$の符号が負になる。

**重要なポイント:**
- 反射波は$-z$方向に進行するため、ポインティングベクトル$\mathbf{S} = \mathbf{E} \times \mathbf{H}$の方向を保つために、$\mathbf{H}$の符号が反転する
- これは、電場と磁場の右手系の関係を保つためである

**透過波（物質中、$z > 0$）:**
$$\mathbf{E}_t = E_{t0}\exp[i(k z - \omega t)]\hat{\mathbf{x}}$$
$$\mathbf{H}_t = H_{t0}\exp[i(k z - \omega t)]\hat{\mathbf{y}}$$

ここで、$k = \omega\sqrt{\varepsilon\mu}$、$H_{t0} = E_{t0}/(\eta)$、$\eta = \sqrt{\mu/\varepsilon}$は物質中の特性インピーダンスである。

**重要なポイント:**
- 物質中の波数は$k = \omega\sqrt{\varepsilon\mu} = \omega n/c$で与えられる（$n$は屈折率）
- 物質中の特性インピーダンスは$\eta = \sqrt{\mu/\varepsilon}$で与えられる
- 一般に、$\eta \neq \eta_0$であるため、反射が起こる

**ステップ2: 境界条件の適用**

$z = 0$での境界条件:

1. **電場の接線成分の連続:**
   $$E_{i0} + E_{r0} = E_{t0}$$

2. **磁場の接線成分の連続:**
   $$H_{i0} - H_{r0} = H_{t0}$$

$H_{i0} = E_{i0}/\eta_0$、$H_{r0} = E_{r0}/\eta_0$、$H_{t0} = E_{t0}/\eta$なので:
$$\frac{E_{i0}}{\eta_0} - \frac{E_{r0}}{\eta_0} = \frac{E_{t0}}{\eta}$$

$$E_{i0} - E_{r0} = \frac{\eta_0}{\eta}E_{t0}$$

**ステップ3: 反射係数の計算**

$E_{r0}$と$E_{t0}$を$E_{i0}$で表す。

第1の境界条件より:
$$E_{t0} = E_{i0} + E_{r0}$$

第2の境界条件に代入:
$$E_{i0} - E_{r0} = \frac{\eta_0}{\eta}(E_{i0} + E_{r0})$$

$$E_{i0} - E_{r0} = \frac{\eta_0}{\eta}E_{i0} + \frac{\eta_0}{\eta}E_{r0}$$

$$E_{i0} - \frac{\eta_0}{\eta}E_{i0} = E_{r0} + \frac{\eta_0}{\eta}E_{r0}$$

$$E_{i0}\left(1 - \frac{\eta_0}{\eta}\right) = E_{r0}\left(1 + \frac{\eta_0}{\eta}\right)$$

反射係数:
$$r = \frac{E_{r0}}{E_{i0}} = \frac{1 - \eta_0/\eta}{1 + \eta_0/\eta} = \frac{\eta - \eta_0}{\eta + \eta_0}$$

特性インピーダンス:
$$\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}}, \quad \eta = \sqrt{\frac{\mu}{\varepsilon}}$$

したがって:
$$r = \frac{\sqrt{\mu/\varepsilon} - \sqrt{\mu_0/\varepsilon_0}}{\sqrt{\mu/\varepsilon} + \sqrt{\mu_0/\varepsilon_0}} = \frac{\sqrt{\mu\varepsilon_0} - \sqrt{\mu_0\varepsilon}}{\sqrt{\mu\varepsilon_0} + \sqrt{\mu_0\varepsilon}}$$

**ステップ4: 反射率の計算**

反射率は、反射係数の絶対値の2乗:
$$R = |r|^2 = \left|\frac{\sqrt{\mu\varepsilon_0} - \sqrt{\mu_0\varepsilon}}{\sqrt{\mu\varepsilon_0} + \sqrt{\mu_0\varepsilon}}\right|^2$$

$\varepsilon$と$\mu$は実数なので:
$$R = \left(\frac{\sqrt{\mu\varepsilon_0} - \sqrt{\mu_0\varepsilon}}{\sqrt{\mu\varepsilon_0} + \sqrt{\mu_0\varepsilon}}\right)^2$$

**答え:**

$$R = \left(\frac{\sqrt{\mu\varepsilon_0} - \sqrt{\mu_0\varepsilon}}{\sqrt{\mu\varepsilon_0} + \sqrt{\mu_0\varepsilon}}\right)^2$$

![反射率の図示](electromagnetism_exercise_20251226_fig5_reflectance.png)

**透過率の計算:**

エネルギー保存則より、反射率$R$と透過率$T$の関係は:
$$R + T = 1$$

透過率は、透過波のエネルギー流束と入射波のエネルギー流束の比で定義される。詳細な計算により:
$$T = \frac{4\eta_0\eta}{(\eta_0 + \eta)^2}$$

これは、反射率の公式と組み合わせると、$R + T = 1$を満たすことを確認できる。

![透過率と反射率の詳細](electromagnetism_exercise_20251226_fig9_transmittance.png)

**物理的意味と考察:**

1. **特性インピーダンスの役割:**
   - 反射率は、2つの媒質の特性インピーダンスの比で決まる
   - 特性インピーダンスが等しい場合（$\eta = \eta_0$）、反射は起こらない（インピーダンス整合）
   - これは、伝送線路理論やアンテナ設計で重要な概念である

2. **対称性:**
   - 式は$\mu$と$\varepsilon$について対称的である
   - これは、電場と磁場の対称性を反映している
   - マクスウェル方程式の双対性に対応する

3. **極限 cases:**
   - $\mu = \mu_0$の場合: $R = \left(\frac{\sqrt{\varepsilon_0} - \sqrt{\varepsilon}}{\sqrt{\varepsilon_0} + \sqrt{\varepsilon}}\right)^2$（通常の誘電体）
   - $\varepsilon = \varepsilon_0$の場合: $R = \left(\frac{\sqrt{\mu} - \sqrt{\mu_0}}{\sqrt{\mu} + \sqrt{\mu_0}}\right)^2$（磁性体）
   - $\varepsilon \to \infty$の場合: $R \to 1$（完全反射、金属のような挙動）
   - $\varepsilon \to 0$の場合: $R \to 1$（完全反射、プラズマのような挙動）

4. **実用的意義:**
   - 反射防止コーティングの設計: 多層膜により反射を最小化
   - 光学素子の反射損失の評価
   - アンテナのインピーダンス整合
   - 電磁波シールドの設計

---

### (4-2) 位相がπだけ変化する条件

**問題:** 入射波と反射波の電場成分の位相が、反射面で$\pi$だけ変化する条件を示せ。

**解答:**

**問題の意味:**

「位相が$\pi$だけ変化する」とは、反射波の電場が入射波の電場に対して位相が$\pi$（180度）ずれることを意味する。これは、反射波の電場が入射波の電場と**逆位相**になることを表す。

**ステップ1: 反射係数の符号と位相の関係**

反射係数は、反射波の振幅と入射波の振幅の比として定義される:
$$r = \frac{E_{r0}}{E_{i0}}$$

ここで、$E_{r0}$と$E_{i0}$は一般に複素数である。反射係数が実数の場合、その符号が位相変化を決定する。

反射係数:
$$r = \frac{\sqrt{\mu\varepsilon_0} - \sqrt{\mu_0\varepsilon}}{\sqrt{\mu\varepsilon_0} + \sqrt{\mu_0\varepsilon}}$$

$z = 0$（界面）での電場は、入射波と反射波の重ね合わせ:
$$E(0, t) = E_{i0}\exp(-i\omega t) + E_{r0}\exp(-i\omega t) = (E_{i0} + E_{r0})\exp(-i\omega t)$$

$$= E_{i0}(1 + r)\exp(-i\omega t)$$

**重要な観察:**
- $r > 0$の場合: $E_{r0} = rE_{i0} > 0$（実数と仮定）なので、反射波は入射波と**同位相**
- $r < 0$の場合: $E_{r0} = rE_{i0} < 0$（実数と仮定）なので、反射波は入射波と**逆位相**（位相が$\pi$変化）

したがって、位相が$\pi$だけ変化する条件は、$r < 0$、すなわち反射係数が負であることである。

**ステップ2: 条件の導出（詳細）**

$r < 0$の条件を導出する。

反射係数の分子と分母を確認:
- 分子: $\sqrt{\mu\varepsilon_0} - \sqrt{\mu_0\varepsilon}$
- 分母: $\sqrt{\mu\varepsilon_0} + \sqrt{\mu_0\varepsilon}$

分母は常に正（$\sqrt{\mu\varepsilon_0} > 0$、$\sqrt{\mu_0\varepsilon} > 0$なので、その和も正）である。

したがって、$r < 0$となるためには、分子が負でなければならない:
$$\sqrt{\mu\varepsilon_0} - \sqrt{\mu_0\varepsilon} < 0$$

$$\sqrt{\mu\varepsilon_0} < \sqrt{\mu_0\varepsilon}$$

両辺は正なので、2乗しても不等号の向きは変わらない:
$$(\sqrt{\mu\varepsilon_0})^2 < (\sqrt{\mu_0\varepsilon})^2$$

$$\mu\varepsilon_0 < \mu_0\varepsilon$$

両辺を$\mu_0\varepsilon_0$で割ると:
$$\frac{\mu}{\mu_0} < \frac{\varepsilon}{\varepsilon_0}$$

または、逆に書くと:
$$\frac{\varepsilon}{\varepsilon_0} > \frac{\mu}{\mu_0}$$

**結論:** 位相が$\pi$だけ変化する条件は、**相対誘電率が相対透磁率より大きい**ことである。

**答え:**

位相が$\pi$だけ変化する条件は:
$$\frac{\varepsilon}{\varepsilon_0} > \frac{\mu}{\mu_0}$$

すなわち、相対誘電率が相対透磁率より大きい場合である。

![位相変化の条件の可視化](electromagnetism_exercise_20251226_fig7_phase_condition.png)

**図の説明:**
- **左図:** 反射係数の符号と位相変化の条件。赤い領域では位相が$\pi$変化（$r < 0$）、青い領域では位相変化なし（$r > 0$）
- **右図:** 反射率の等高線図。$\varepsilon/\varepsilon_0 = \mu/\mu_0$の線上で反射率が0になる

![反射係数と位相の関係](electromagnetism_exercise_20251226_fig11_reflection_coefficient_phase.png)

**図の説明:**
- **左図:** 反射係数の実部と虚部の変化。$\varepsilon/\varepsilon_0 < 1$では$r > 0$、$\varepsilon/\varepsilon_0 > 1$では$r < 0$
- **右図:** 反射係数の位相。$\varepsilon/\varepsilon_0 > 1$では位相が$-\pi$（位相が$\pi$変化）

![位相変化の時間変化](electromagnetism_exercise_20251226_fig10_phase_change_time.png)

**図の説明:**
- **左上・左下:** 位相が$\pi$変化する場合（ガラス）。反射波は入射波と逆位相
- **右上・右下:** 位相変化なしの場合（磁性体）。反射波は入射波と同位相

**詳細な物理的意味と考察:**

1. **位相の反転のメカニズム:**

   位相が$\pi$変化する物理的メカニズムを理解するため、界面での電場の連続性を考える。

   界面（$z = 0$）での電場:
   $$E(0, t) = E_{i0}\exp(-i\omega t) + E_{r0}\exp(-i\omega t) = (E_{i0} + E_{r0})\exp(-i\omega t)$$

   透過波の電場（物質中）:
   $$E_t(0, t) = E_{t0}\exp(-i\omega t)$$

   電場の接線成分の連続性より:
   $$E_{i0} + E_{r0} = E_{t0}$$

   ここで、$E_{r0} = rE_{i0}$なので:
   $$E_{i0}(1 + r) = E_{t0}$$

   - $r < 0$の場合: $1 + r < 1$なので、透過波の振幅は入射波より小さい
   - このとき、反射波は入射波と逆位相になり、界面での電場を小さくする
   - これは、**固定端反射**（fixed end reflection）に対応する

2. **固定端反射と自由端反射の対比:**

   **固定端反射（$r < 0$）:**
   - 反射波は入射波と逆位相
   - 界面での合成波の振幅は小さくなる
   - 例: ガラス表面での光の反射

   **自由端反射（$r > 0$）:**
   - 反射波は入射波と同位相
   - 界面での合成波の振幅は大きくなる
   - 例: 低インピーダンス媒質から高インピーダンス媒質への反射

3. **通常の誘電体での位相変化:**

   多くの誘電体では$\mu \approx \mu_0$なので、条件は:
   $$\frac{\varepsilon}{\varepsilon_0} > 1$$

   すなわち、$\varepsilon > \varepsilon_0$のときに位相が反転する。

   **具体例:**
   - **ガラス（$n = 1.5$）:** $\varepsilon/\varepsilon_0 = n^2 = 2.25 > 1 = \mu/\mu_0$ → 位相が$\pi$変化
   - **水（$n \approx 1.33$）:** $\varepsilon/\varepsilon_0 = n^2 \approx 1.77 > 1 = \mu/\mu_0$ → 位相が$\pi$変化
   - **ダイヤモンド（$n \approx 2.4$）:** $\varepsilon/\varepsilon_0 = n^2 \approx 5.76 > 1 = \mu/\mu_0$ → 位相が$\pi$変化

4. **磁性体での位相変化:**

   $\mu > \mu_0$の磁性体では、条件が異なる。

   **具体例:**
   - $\mu/\mu_0 = 2$、$\varepsilon/\varepsilon_0 = 1.5$の場合:
     - $\varepsilon/\varepsilon_0 = 1.5 < 2 = \mu/\mu_0$なので、位相は反転しない（$r > 0$）
   - $\mu/\mu_0 = 1.5$、$\varepsilon/\varepsilon_0 = 3$の場合:
     - $\varepsilon/\varepsilon_0 = 3 > 1.5 = \mu/\mu_0$なので、位相が$\pi$変化（$r < 0$）

5. **反射係数の符号と位相の関係（数学的詳細）:**

   反射係数が実数の場合:
   $$r = |r|e^{i\phi_r}$$

   ここで、$\phi_r$は反射係数の位相である。

   - $r > 0$の場合: $\phi_r = 0$（位相変化なし）
   - $r < 0$の場合: $\phi_r = \pi$（位相が$\pi$変化）

   実際、$r < 0$のとき:
   $$r = -|r| = |r|e^{i\pi}$$

   したがって、反射波の電場:
   $$E_r = rE_i = |r|e^{i\pi}E_i = |r|E_i e^{i(\phi_i + \pi)}$$

   これは、入射波の位相に$\pi$を加えたものに対応する。

6. **界面での電場の連続性の詳細:**

   界面での電場の連続性は、マクスウェル方程式の境界条件から導かれる:
   $$\mathbf{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = 0$$

   ここで、$\mathbf{n}$は界面の法線ベクトル、$\mathbf{E}_1$と$\mathbf{E}_2$は界面の両側の電場である。

   垂直入射の場合、電場は界面に平行なので:
   $$E_{i0} + E_{r0} = E_{t0}$$

   この条件と、磁場の連続性から反射係数が決定される。

7. **エネルギー保存との関係:**

   反射率$R = |r|^2$と透過率$T$の関係:
   $$R + T = 1$$

   位相変化はエネルギー保存には影響しないが、界面での電場と磁場の分布に影響する。

8. **実用的意義:**

   - **反射防止コーティング:** 多層膜により反射を最小化する際、各層での位相変化を考慮する必要がある
   - **光学素子の設計:** レンズやミラーの設計では、位相変化が像の品質に影響する
   - **アンテナ設計:** アンテナのインピーダンス整合では、位相変化を考慮する必要がある
   - **干渉計:** マイケルソン干渉計などでは、位相変化が干渉パターンに影響する

---

### (4-3) ガラス表面での反射率

**問題:** 真空中から屈折率$n = \sqrt{\varepsilon\mu}/\sqrt{\varepsilon_0\mu_0} = 1.5$のガラス表面に垂直入射する場合の反射率を求めよ。ここでは、$\mu = \mu_0$と仮定する。

**解答:**

**ステップ1: 屈折率と誘電率の関係**

屈折率:
$$n = \frac{\sqrt{\varepsilon\mu}}{\sqrt{\varepsilon_0\mu_0}} = 1.5$$

$\mu = \mu_0$と仮定すると:
$$n = \sqrt{\frac{\varepsilon}{\varepsilon_0}} = 1.5$$

したがって:
$$\frac{\varepsilon}{\varepsilon_0} = n^2 = 2.25$$

**ステップ2: 反射率の計算**

(4-1)の結果で、$\mu = \mu_0$とすると:
$$R = \left(\frac{\sqrt{\mu_0\varepsilon_0} - \sqrt{\mu_0\varepsilon}}{\sqrt{\mu_0\varepsilon_0} + \sqrt{\mu_0\varepsilon}}\right)^2 = \left(\frac{\sqrt{\varepsilon_0} - \sqrt{\varepsilon}}{\sqrt{\varepsilon_0} + \sqrt{\varepsilon}}\right)^2$$

$$= \left(\frac{1 - \sqrt{\varepsilon/\varepsilon_0}}{1 + \sqrt{\varepsilon/\varepsilon_0}}\right)^2 = \left(\frac{1 - n}{1 + n}\right)^2$$

$n = 1.5$を代入:
$$R = \left(\frac{1 - 1.5}{1 + 1.5}\right)^2 = \left(\frac{-0.5}{2.5}\right)^2 = \left(\frac{-1}{5}\right)^2 = \frac{1}{25} = 0.04$$

**答え:**

$$R = \left(\frac{1 - n}{1 + n}\right)^2 = \left(\frac{1 - 1.5}{1 + 1.5}\right)^2 = 0.04 = 4\%$$

**物理的意味と考察:**

1. **フレネルの公式:**
   - この結果は、垂直入射に対する**フレネルの公式**（Fresnel equations）に対応する
   - $R = \left(\frac{n_1 - n_2}{n_1 + n_2}\right)^2$の形で表される

2. **反射率の値:**
   - ガラス表面での反射率は約4%である
   - これは、窓ガラスで観察される反射に対応する

3. **応用:**
   - 反射防止コーティングの設計
   - 光学素子の反射損失の評価

---

### (4-4) 負の誘電率の場合

**問題:** $\varepsilon$が負の場合、反射率にどのような影響があるか説明せよ。

**解答:**

**問題の意味:**

通常の誘電体では、誘電率$\varepsilon$は正の値である。しかし、特定の条件下では、誘電率が負の値を取ることがある。このような場合、電磁波の伝播特性が大きく変化し、完全反射が起こる。

**ステップ1: 負の誘電率の意味と波数の変化**

$\varepsilon < 0$の場合、物質の特性が大きく変化する。

**波数の計算:**

平面波の波数は、マクスウェル方程式から:
$$k = \omega\sqrt{\varepsilon\mu}$$

$\varepsilon > 0$の場合、$k$は実数であり、電磁波は物質中を伝播する。

$\varepsilon < 0$、$\mu > 0$の場合:
$$k = \omega\sqrt{(-|\varepsilon|)\mu} = \omega\sqrt{|\varepsilon|\mu} \cdot \sqrt{-1} = i\omega\sqrt{|\varepsilon|\mu}$$

すなわち、$k$は**純虚数**になる:
$$k = i\kappa, \quad \kappa = \omega\sqrt{|\varepsilon|\mu} > 0$$

**電磁波の空間依存性:**

波数が純虚数の場合、電磁波の空間依存性は:
$$E(z, t) = E_0\exp[i(kz - \omega t)] = E_0\exp[i(i\kappa z - \omega t)] = E_0\exp(-\kappa z)\exp(-i\omega t)$$

$$= E_0\exp(-z/\delta)\exp(-i\omega t)$$

ここで、$\delta = 1/\kappa = 1/(\omega\sqrt{|\varepsilon|\mu})$は**侵入深さ**（スキン深さ）である。

これは、電磁波が物質中で**指数関数的に減衰**することを意味する。このような波は**エバネッセント波**（evanescent wave）と呼ばれる。

**ステップ2: 反射率の計算（詳細）**

反射率の公式:
$$R = \left|\frac{\sqrt{\mu\varepsilon_0} - \sqrt{\mu_0\varepsilon}}{\sqrt{\mu\varepsilon_0} + \sqrt{\mu_0\varepsilon}}\right|^2 = |r|^2$$

$\varepsilon < 0$の場合、$\sqrt{\varepsilon}$は純虚数になる。$\sqrt{\varepsilon} = i\sqrt{|\varepsilon|}$とすると:
$$r = \frac{\sqrt{\mu\varepsilon_0} - \sqrt{\mu_0\varepsilon}}{\sqrt{\mu\varepsilon_0} + \sqrt{\mu_0\varepsilon}} = \frac{\sqrt{\mu\varepsilon_0} - i\sqrt{\mu_0|\varepsilon|}}{\sqrt{\mu\varepsilon_0} + i\sqrt{\mu_0|\varepsilon|}}$$

これは複素数である。分子と分母の絶対値を計算する。

**分子の絶対値:**
$$|\sqrt{\mu\varepsilon_0} - i\sqrt{\mu_0|\varepsilon|}| = \sqrt{(\sqrt{\mu\varepsilon_0})^2 + (\sqrt{\mu_0|\varepsilon|})^2} = \sqrt{\mu\varepsilon_0 + \mu_0|\varepsilon|}$$

**分母の絶対値:**
$$|\sqrt{\mu\varepsilon_0} + i\sqrt{\mu_0|\varepsilon|}| = \sqrt{(\sqrt{\mu\varepsilon_0})^2 + (\sqrt{\mu_0|\varepsilon|})^2} = \sqrt{\mu\varepsilon_0 + \mu_0|\varepsilon|}$$

したがって:
$$|r| = \frac{|\sqrt{\mu\varepsilon_0} - i\sqrt{\mu_0|\varepsilon|}|}{|\sqrt{\mu\varepsilon_0} + i\sqrt{\mu_0|\varepsilon|}|} = \frac{\sqrt{\mu\varepsilon_0 + \mu_0|\varepsilon|}}{\sqrt{\mu\varepsilon_0 + \mu_0|\varepsilon|}} = 1$$

**結論:**
$$R = |r|^2 = 1$$

すなわち、**反射率は100%**となり、**完全反射**が起こる。

**ステップ3: 物理的解釈**

$\varepsilon < 0$の場合、物質は**メタマテリアル**（metamaterial）や**プラズマ**のような性質を示す。

- 電磁波は物質中に侵入できない（完全反射）
- 反射率は100%になる
- 透過率は0%になる（エネルギー保存則より）
- これは、**金属**や**プラズマ**の挙動に対応する

![負の誘電率の場合の反射率と透過率](electromagnetism_exercise_20251226_fig8_negative_epsilon.png)

**図の説明:**
- **左図:** 誘電率が負の場合、反射率$R = 1$となり、透過率$T = 0$になる（完全反射）
- **右図:** 正の誘電率の場合の反射率と透過率の対数スケール表示

![プラズマの誘電率の周波数依存性](electromagnetism_exercise_20251226_fig12_plasma_permittivity.png)

**図の説明:**
- **左上:** プラズマの誘電率の周波数依存性。$\omega < \omega_p$で負になる
- **右上:** プラズマの反射率の周波数依存性。$\omega < \omega_p$で完全反射
- **左下:** 波数の実部と虚部。$\omega < \omega_p$で虚部が大きくなる
- **右下:** 侵入深さ（スキン深さ）。$\omega < \omega_p$で有限の値を持つ

![エバネッセント波の減衰](electromagnetism_exercise_20251226_fig13_evanescent_wave.png)

**図の説明:**
- **左図:** エバネッセント波の振幅の指数関数的減衰
- **右図:** エバネッセント波の時間・空間分布。距離とともに減衰する

**答え:**

$\varepsilon < 0$の場合、反射率$R = 1$となり、**完全反射**が起こる。電磁波は物質中に侵入できず、すべて反射される。

**詳細な物理的意味と考察:**

1. **プラズマの誘電率（ドルーデモデル）:**

   プラズマは、自由電子とイオンからなる電離気体である。プラズマの誘電率は、**ドルーデモデル**（Drude model）により記述される:
   $$\varepsilon(\omega) = \varepsilon_0\left(1 - \frac{\omega_p^2}{\omega^2}\right)$$

   ここで、$\omega_p = \sqrt{ne^2/(m\varepsilon_0)}$は**プラズマ周波数**である（$n$は電子密度、$e$は電子電荷、$m$は電子質量）。

   **重要な特性:**
   - $\omega > \omega_p$の場合: $\varepsilon(\omega) > 0$ → 電磁波は伝播できる
   - $\omega < \omega_p$の場合: $\varepsilon(\omega) < 0$ → 電磁波は完全反射される
   - $\omega = \omega_p$の場合: $\varepsilon(\omega) = 0$ → 臨界点

   **具体例:**
   - **電離層:** プラズマ周波数は約1-10 MHz。これより低い周波数の電波は反射される
   - **短波ラジオ:** 1.6-30 MHzの周波数帯。電離層で反射され、長距離伝播が可能
   - **金属:** プラズマ周波数は可視光領域（約$10^{15}$ Hz）。可視光は反射される

2. **金属の誘電率（ドルーデモデル）:**

   金属では、自由電子がプラズマ振動を起こす。金属の誘電率は、損失を考慮したドルーデモデルで記述される:
   $$\varepsilon(\omega) = \varepsilon_0\left(1 - \frac{\omega_p^2}{\omega^2 + i\gamma\omega}\right)$$

   ここで、$\gamma$は減衰定数（電子の衝突による損失）である。

   **低周波数領域（$\omega \ll \omega_p$）:**
   - 実部: $\varepsilon'(\omega) \approx -\varepsilon_0\omega_p^2/\omega^2 < 0$
   - 虚部: $\varepsilon''(\omega) \approx \varepsilon_0\omega_p^2\gamma/\omega^3 > 0$
   - 電磁波は強く減衰し、反射される

   **可視光領域:**
   - 多くの金属（金、銀、銅など）では、プラズマ周波数が可視光領域にある
   - これにより、金属は高い反射率を示す（鏡の原理）

3. **エバネッセント波の詳細:**

   $\varepsilon < 0$の場合、電磁波は物質中で指数関数的に減衰する。

   **電場の空間分布:**
   $$E(z, t) = E_0\exp(-z/\delta)\exp(-i\omega t)$$

   **侵入深さ（スキン深さ）:**
   $$\delta = \frac{1}{\omega\sqrt{|\varepsilon|\mu}} = \frac{1}{\kappa}$$

   **物理的意味:**
   - 電磁波は界面から距離$\delta$以内にのみ存在する
   - $\delta$は周波数が高いほど小さくなる
   - これは、高周波の電磁波ほど物質中に侵入できないことを意味する

   **エネルギー流:**
   - エバネッセント波は、エネルギーを運ばない（実効的なポインティングベクトルは0）
   - すべてのエネルギーは反射される

4. **スキン効果（Skin Effect）:**

   導体中での電流の集中現象を**スキン効果**という。

   **導体の誘電率:**
   $$\varepsilon(\omega) = \varepsilon_0 + i\frac{\sigma}{\omega}$$

   ここで、$\sigma$は導電率である。低周波数では、虚部が支配的になり、電磁波は減衰する。

   **スキン深さ:**
   $$\delta = \sqrt{\frac{2}{\omega\mu\sigma}}$$

   これは、電流が導体表面に集中する深さを表す。

5. **メタマテリアル:**

   **メタマテリアル**は、人工的に作られた構造により、自然界には存在しない電磁特性を実現する材料である。

   **負の誘電率の実現:**
   - 金属ナノワイヤや金属薄膜の構造により、負の誘電率を実現できる
   - プラズモン共鳴を利用する

   **負の透磁率の実現:**
   - スプリットリング共鳴器（SRR）などの構造により、負の透磁率を実現できる

   **負の屈折率:**
   - $\varepsilon < 0$かつ$\mu < 0$の場合、屈折率$n = \sqrt{\varepsilon\mu}$が負になる
   - これにより、**負の屈折率メタマテリアル**が実現される
   - スネルの法則が逆転し、特異な光学特性が得られる

   **応用:**
   - **超解像レンズ:** 回折限界を超えた解像度
   - **不可視化技術:** 物体を電磁波から隠す
   - **アンテナ:** 小型化と高効率化

6. **完全反射の物理的メカニズム:**

   負の誘電率の場合、完全反射が起こる理由を理解する。

   **特性インピーダンス:**
   $$\eta = \sqrt{\frac{\mu}{\varepsilon}}$$

   $\varepsilon < 0$の場合、$\eta$は純虚数になる。これにより、透過波は存在できず、すべてのエネルギーが反射される。

   **境界条件:**
   - 電場の連続性: $E_i + E_r = E_t$
   - 磁場の連続性: $H_i - H_r = H_t$
   - $E_t = 0$（透過波が存在しない）とすると、$E_r = -E_i$となり、完全反射が起こる

7. **周波数依存性の重要性:**

   負の誘電率は、周波数に強く依存する。

   **プラズマの場合:**
   - 低周波数（$\omega < \omega_p$）: $\varepsilon < 0$ → 完全反射
   - 高周波数（$\omega > \omega_p$）: $\varepsilon > 0$ → 伝播可能

   **金属の場合:**
   - 可視光より低い周波数: $\varepsilon < 0$ → 高い反射率
   - 可視光より高い周波数（紫外線）: $\varepsilon > 0$ → 透過可能

8. **実用的意義:**

   - **電磁波シールド:** 金属箱や導電性材料による電磁波の遮蔽
   - **アンテナ設計:** 反射板や導波管の設計
   - **プラズマ物理:** 電離層、核融合プラズマの研究
   - **光学デバイス:** メタマテリアルによる新しい光学素子の開発
   - **通信技術:** 電離層を利用した長距離通信
   - **材料科学:** 新しい電磁特性を持つ材料の開発

---

## まとめ

本演習問題では、以下の重要な電磁気学の概念を扱った:

1. **誘電緩和と周波数分散:** 極性分子の分極の時間的応答と、誘電率の周波数依存性
2. **遅延ポテンシャル:** 時間変化する電荷・電流分布による電磁場の生成
3. **光の吸収と散乱:** 小さな粒子による光の相互作用
4. **界面での反射と透過:** 電磁波の境界での挙動

これらの概念は、光学、プラズマ物理学、材料科学など、多くの分野で重要な役割を果たしている。

