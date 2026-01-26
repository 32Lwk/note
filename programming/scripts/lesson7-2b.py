import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 日本語フォントの設定
# macOSで利用可能な日本語フォントを検索
font_found = False
for f in fm.fontManager.ttflist:
    if 'Hiragino' in f.name:
        plt.rcParams['font.family'] = f.name
        font_found = True
        break

if not font_found:
    # Hiraginoが見つからない場合は、他の日本語フォントを検索
    for f in fm.fontManager.ttflist:
        if 'AppleGothic' in f.name or 'Arial Unicode' in f.name:
            plt.rcParams['font.family'] = f.name
            font_found = True
            break

# 物理定数の定義
c = 2.99792458e8  # m/s (光速)
h = 6.626068e-34  # J s (プランク定数)
k = 1.3806504e-23  # J/K (ボルツマン定数)

# 課題7-2(a): 関数定義
def I(x, y):
    """
    黒体放射の単位波長あたりの放射強度
    x: 波長 λ [m]
    y: 温度 T [K]
    戻り値: 放射強度 I [J/(m^2 s str m)]
    """
    numerator = 2 * h * c**2 / x**5
    denominator = np.exp(h * c / (x * k * y)) - 1
    return numerator / denominator

# 課題7-2(b): 2次元プロット
if __name__ == '__main__':
    # 波長を対数スケールでサンプリング: 1 nm から 1 cm
    wavelength = np.logspace(-9, -2, 1000)  # 1e-9 m から 1e-2 m
    
    # 温度のリスト
    temperatures = [60000, 6000, 600]  # K
    
    plt.figure(figsize=(10, 7))
    
    for T in temperatures:
        intensity = I(wavelength, T)
        plt.plot(wavelength, intensity, label=f'T = {T} K', linewidth=2)
        
        # 最大値の波長を探す
        max_idx = np.argmax(intensity)
        max_wavelength = wavelength[max_idx]
        max_intensity = intensity[max_idx]
        plt.plot(max_wavelength, max_intensity, 'ro', markersize=8)
        print(f'T = {T} K: 最大放射強度の波長 = {max_wavelength:.1e} m = {max_wavelength*1e9:.1f} nm')
    
    # 軸の設定
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('波長 λ [m]', fontsize=12)
    plt.ylabel('放射強度 I [J/(m² s str m)]', fontsize=12)
    plt.title('黒体放射強度スペクトル', fontsize=14)
    plt.grid(True, alpha=0.3, which='both')
    plt.legend(loc='best', fontsize=10)
    
    # PNGファイルに保存
    plt.savefig('lesson7-2b.png', dpi=300, bbox_inches='tight')
    print("\nグラフを lesson7-2b.png に保存しました。")
    plt.close()

