import numpy as np
import matplotlib.pyplot as plt

# xの範囲を定義: -2π < x < 2π
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# 各関数を計算
y1 = np.sin(2*x)      # y = sin(2x)
y2 = np.cos(x)        # y = cos(x)
y3 = np.tan(x)        # y = tan(x)
y4 = np.exp(0.2*x)    # y = exp(0.2x)

# グラフを作成
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y = sin(2x)', linewidth=2)
plt.plot(x, y2, label='y = cos(x)', linewidth=2)
plt.plot(x, y3, label='y = tan(x)', linewidth=2)
plt.plot(x, y4, label='y = exp(0.2x)', linewidth=2)

# グラフの設定
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Graph of Multiple Functions', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(loc='best', fontsize=10)

# y軸の範囲を調整（tan(x)が発散するため）
plt.ylim(-5, 5)

# PNGファイルに保存
plt.savefig('lesson7-1.png', dpi=300, bbox_inches='tight')
print("グラフを lesson7-1.png に保存しました。")

plt.close()

