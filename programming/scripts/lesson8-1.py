import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def lorentz_linear(x, a, b, c, d):
    return (b / np.pi) / ((x - a)**2 + b**2) + c * x + d

if __name__ == '__main__':
    data = np.loadtxt('testdata04.dat', comments='#')
    x_data = data[:, 0]
    y_data = data[:, 1]
    
    p0 = [
        x_data[np.argmax(y_data)],
        (x_data.max() - x_data.min()) / 10.0,
        (y_data[-1] - y_data[0]) / (x_data[-1] - x_data[0]) if len(x_data) > 1 else 0.0,
        np.mean(y_data) * 0.1
    ]
    
    popt, _ = curve_fit(lorentz_linear, x_data, y_data, p0=p0, maxfev=5000)
    a, b, c, d = popt
    
    print(f"フィッティング結果:")
    print(f"  a = {a:.6f}")
    print(f"  b = {b:.6f}")
    print(f"  c = {c:.6f}")
    print(f"  d = {d:.6f}")
    
    x_fit = np.linspace(x_data.min(), x_data.max(), 1000)
    y_fit = lorentz_linear(x_fit, a, b, c, d)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, color='blue', s=30, alpha=0.6, label='Data')
    plt.plot(x_fit, y_fit, 'r-', linewidth=2, label='Fit')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Lorentz (Cauchy) Distribution + Linear Function Fit', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('lesson8-1.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("グラフを lesson8-1.png に保存しました。")

