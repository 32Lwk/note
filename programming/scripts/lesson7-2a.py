import numpy as np

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

if __name__ == '__main__':
    print("=" * 50)
    print("課題7-2(a): 関数定義")
    print("=" * 50)
    print("Python関数定義:")
    print("c = 2.99792458e8  # m/s")
    print("h = 6.626068e-34  # J s")
    print("k = 1.3806504e-23  # J/K")
    print()
    print("def I(x, y):")
    print("    numerator = 2 * h * c**2 / x**5")
    print("    denominator = np.exp(h * c / (x * k * y)) - 1")
    print("    return numerator / denominator")

