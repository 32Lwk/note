import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def hubble_law(D, H):
    return H * D

if __name__ == '__main__':
    data_lines = []
    with open('Hubble.dat', 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split()
            try:
                velocity = float(parts[-2])
                distance = float(parts[-1])
                data_lines.append([distance, abs(velocity)])
            except (ValueError, IndexError):
                continue
    
    data = np.array(data_lines)
    distance = data[:, 0]
    velocity = data[:, 1]
    
    popt, pcov = curve_fit(hubble_law, distance, velocity)
    H_fit = popt[0]
    H_std = np.sqrt(pcov[0, 0])
    
    print(f"フィッティング結果:")
    print(f"  ハッブル定数 H = {H_fit:.2f} ± {H_std:.2f} km/s/Mpc")
    
    age_billion_years = 9.778e11 / H_fit / 1e9
    print(f"\n宇宙年齢の概算: {age_billion_years:.2f} 十億年")
    
    D_fit = np.linspace(0, distance.max() * 1.1, 100)
    v_fit = hubble_law(D_fit, H_fit)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(distance, velocity, color='blue', s=50, alpha=0.7, label='Data')
    plt.plot(D_fit, v_fit, 'r-', linewidth=2, label=f'Fit (H = {H_fit:.2f} km/s/Mpc)')
    plt.xlabel('Distance D [Mpc]', fontsize=12)
    plt.ylabel('Recession velocity v [km/s]', fontsize=12)
    plt.title('Hubble Law Fit', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('lesson8-2.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("グラフを lesson8-2.png に保存しました。")

