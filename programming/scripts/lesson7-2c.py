import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
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

# 課題7-2(c): 2次元カラーマップ
if __name__ == '__main__':
    # 波長: 1 nm から 1 cm (対数スケール)
    wavelength = np.logspace(-9, -2, 200)  # 1e-9 m から 1e-2 m
    
    # 温度: 100 K から 100000 K (対数スケール)
    temperature = np.logspace(2, 5, 200)  # 100 K から 100000 K
    
    # メッシュグリッドを作成
    W, T = np.meshgrid(wavelength, temperature)
    
    # 放射強度を計算
    Intensity = I(W, T)
    
    # カラーマップを作成
    plt.figure(figsize=(12, 8))
    
    # 放射強度の範囲を設定: 100 から 10^19 J/(m^2 s str m)
    im = plt.pcolormesh(W, T, Intensity, 
                        norm=mcolors.LogNorm(vmin=1e2, vmax=1e19),
                        cmap='hot', shading='auto')
    
    # カラーバーを追加
    cbar = plt.colorbar(im)
    cbar.set_label('放射強度 I [J/(m² s str m)]', fontsize=12)
    
    # 軸の設定
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('波長 λ [m]', fontsize=12)
    plt.ylabel('温度 T [K]', fontsize=12)
    plt.title('黒体放射強度の2次元カラーマップ', fontsize=14)
    
    # PNGファイルに保存
    plt.savefig('lesson7-2c.png', dpi=300, bbox_inches='tight')
    print("グラフを lesson7-2c.png に保存しました。")
    plt.close()

