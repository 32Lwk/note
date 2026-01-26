import numpy as np
import matplotlib.pyplot as plt

# 日本語フォントの設定
plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False  # マイナス記号の文字化け対策

# 関数定義
def f(x):
    return 9 * x * np.exp(-x**2) + 1

# 1階導関数
def df(x):
    return 9 * np.exp(-x**2) * (1 - 2 * x**2)

# 2階導関数
def d2f(x):
    return 9 * np.exp(-x**2) * (4 * x**3 - 6 * x)

# 極値点を求める（f'(x) = 0）
def find_extrema():
    # f'(x) = 9exp(-x^2)(1 - 2x^2) = 0
    # 1 - 2x^2 = 0 より x = ±1/√2
    x_extrema = np.array([-1/np.sqrt(2), 1/np.sqrt(2)])
    y_extrema = f(x_extrema)
    return x_extrema, y_extrema

# 変曲点を求める（f''(x) = 0）
def find_inflection_points():
    # f''(x) = 9exp(-x^2)(4x^3 - 6x) = 0
    # 4x^3 - 6x = 0 より x(4x^2 - 6) = 0
    # x = 0 または x = ±√(3/2)
    x_inflection = np.array([-np.sqrt(3/2), 0, np.sqrt(3/2)])
    y_inflection = f(x_inflection)
    return x_inflection, y_inflection

if __name__ == '__main__':
    # xの範囲を設定
    x = np.linspace(-3, 3, 1000)
    y = f(x)
    
    # 極値点と変曲点を求める
    x_extrema, y_extrema = find_extrema()
    x_inflection, y_inflection = find_inflection_points()
    
    # グラフを描画
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='f(x) = 9x exp(-x²) + 1')
    
    # 極値点をプロット
    plt.plot(x_extrema, y_extrema, 'ro', markersize=10, label='極値点', zorder=5)
    for i, (xe, ye) in enumerate(zip(x_extrema, y_extrema)):
        plt.annotate(f'({xe:.3f}, {ye:.3f})', 
                    xy=(xe, ye), 
                    xytext=(10, 10), 
                    textcoords='offset points',
                    fontsize=9,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
    
    # 変曲点をプロット
    plt.plot(x_inflection, y_inflection, 'gs', markersize=10, label='変曲点', zorder=5)
    for i, (xi, yi) in enumerate(zip(x_inflection, y_inflection)):
        plt.annotate(f'({xi:.3f}, {yi:.3f})', 
                    xy=(xi, yi), 
                    xytext=(10, -20), 
                    textcoords='offset points',
                    fontsize=9,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='cyan', alpha=0.7))
    
    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x)', fontsize=12)
    plt.title('062400506', fontsize=14)  # 学籍番号を設定（実際の学籍番号に変更してください）
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    plt.tight_layout()
    plt.savefig('lesson10-1.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("グラフを lesson10-1.png に保存しました。")
    print(f"\n極値点:")
    for xe, ye in zip(x_extrema, y_extrema):
        print(f"  x = {xe:.6f}, f(x) = {ye:.6f}")
    print(f"\n変曲点:")
    for xi, yi in zip(x_inflection, y_inflection):
        print(f"  x = {xi:.6f}, f(x) = {yi:.6f}")
