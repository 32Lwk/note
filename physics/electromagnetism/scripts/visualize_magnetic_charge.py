"""
磁気双極子の磁荷分布と磁束密度の可視化
問題4の磁気双極子モーメントmに対応する磁荷分布を図示
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle, FancyArrowPatch
from mpl_toolkits.mplot3d.proj3d import proj_transform

# 日本語フォントの設定
# macOSで利用可能な日本語フォントを使用
try:
    plt.rcParams['font.family'] = 'Hiragino Sans'
except:
    try:
        plt.rcParams['font.family'] = 'Arial Unicode MS'
    except:
        plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# 図1: 磁気双極子の構造図（正負の磁荷の配置）
def plot_dipole_structure():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 双極子の配置（原点を中心に、z軸方向に配置）
    d = 0.3  # 双極子の間隔
    m_magnitude = 1.0  # 双極子モーメントの大きさ
    
    # 正の磁荷（N極）と負の磁荷（S極）
    ax.plot(0, d/2, 'ro', markersize=20, label='正の磁荷 (+q_m)', zorder=3)
    ax.plot(0, -d/2, 'bo', markersize=20, label='負の磁荷 (-q_m)', zorder=3)
    
    # 双極子モーメントベクトル
    ax.arrow(0, -d/2, 0, d, head_width=0.1, head_length=0.1, 
             fc='green', ec='green', linewidth=3, length_includes_head=True, zorder=2)
    ax.text(0.15, 0, 'm', fontsize=16, color='green', weight='bold')
    
    # 磁力線の概略
    theta = np.linspace(0, 2*np.pi, 100)
    for r in [0.5, 0.8, 1.2]:
        x_circle = r * np.cos(theta)
        y_circle = r * np.sin(theta)
        ax.plot(x_circle, y_circle, 'k--', alpha=0.3, linewidth=1)
    
    # 軸の設定
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=0.5, linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linewidth=0.5, linestyle='-', alpha=0.3)
    
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('z', fontsize=12)
    ax.set_title('Magnetic Dipole Structure\n(磁気双極子の構造)', fontsize=14, weight='bold')
    ax.legend(loc='upper right', fontsize=11)
    
    # 説明テキスト
    textstr = '双極子モーメント: m = q_m × d\n(正負の磁荷が微小距離dだけ離れた配置)'
    ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('physics/magnetic_dipole_structure.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("図1を保存: magnetic_dipole_structure.png")

# 図2: 磁束密度のベクトル場（2D、xy平面）
def plot_magnetic_field_2d():
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # グリッドの作成
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    X, Y = np.meshgrid(x, y)
    
    # 原点を除く
    R = np.sqrt(X**2 + Y**2)
    mask = R > 0.1
    
    # 双極子モーメント（z方向）
    m = np.array([0, 0, 1.0])
    
    # 位置ベクトル
    r_vec = np.array([X, Y, np.zeros_like(X)])
    r = np.sqrt(X**2 + Y**2 + 1e-10)
    
    # m·r
    m_dot_r = m[2] * np.zeros_like(X)  # z方向の双極子なので、xy平面では0
    
    # より正確な計算: 3D空間での計算をxy平面に投影
    # 磁位: Φ_m = (1/(4π)) * (m·r / r³)
    # 磁束密度: B = -∇Φ_m
    
    # 3Dでの計算
    Z_plane = np.zeros_like(X)
    r_3d = np.sqrt(X**2 + Y**2 + Z_plane**2 + 1e-10)
    m_dot_r_3d = m[0]*X + m[1]*Y + m[2]*Z_plane
    
    # 磁位
    phi_m = (1/(4*np.pi)) * m_dot_r_3d / (r_3d**3)
    
    # 磁束密度の勾配（数値微分）
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    
    B_x = -np.gradient(phi_m, dx, axis=1)
    B_y = -np.gradient(phi_m, dy, axis=0)
    
    # 原点付近をマスク
    B_x[~mask] = np.nan
    B_y[~mask] = np.nan
    
    # 正規化（表示用）
    B_magnitude = np.sqrt(B_x**2 + B_y**2)
    B_x_norm = B_x / (B_magnitude + 1e-10)
    B_y_norm = B_y / (B_magnitude + 1e-10)
    
    # ベクトル場のプロット
    ax.quiver(X[mask], Y[mask], B_x_norm[mask], B_y_norm[mask], 
              B_magnitude[mask], cmap='viridis', scale=30, width=0.005, alpha=0.7)
    
    # 磁位の等高線
    phi_m_masked = phi_m.copy()
    phi_m_masked[~mask] = np.nan
    contour = ax.contour(X, Y, phi_m_masked, levels=20, colors='gray', alpha=0.4, linewidths=0.5)
    ax.clabel(contour, inline=True, fontsize=8, fmt='%1.2f')
    
    # 原点に双極子を表示
    ax.plot(0, 0, 'ko', markersize=12, zorder=5)
    ax.arrow(0, -0.2, 0, 0.4, head_width=0.1, head_length=0.1,
             fc='green', ec='green', linewidth=2, zorder=6)
    ax.text(0.15, 0, 'm', fontsize=14, color='green', weight='bold')
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Magnetic Flux Density B (xy plane)\n(磁束密度 B, xy平面)', fontsize=14, weight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('physics/magnetic_field_2d.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("図2を保存: magnetic_field_2d.png")

# 図3: 磁束密度のベクトル場（2D、xz平面、双極子軸を含む平面）
def plot_magnetic_field_xz():
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # グリッドの作成
    x = np.linspace(-2, 2, 25)
    z = np.linspace(-2, 2, 25)
    X, Z = np.meshgrid(x, z)
    Y = np.zeros_like(X)  # y=0平面
    
    # 原点を除く
    R = np.sqrt(X**2 + Y**2 + Z**2)
    mask = R > 0.15
    
    # 双極子モーメント（z方向）
    m = np.array([0, 0, 1.0])
    
    # 位置ベクトル
    r = np.sqrt(X**2 + Y**2 + Z**2 + 1e-10)
    m_dot_r = m[0]*X + m[1]*Y + m[2]*Z
    
    # 磁位
    phi_m = (1/(4*np.pi)) * m_dot_r / (r**3)
    
    # 磁束密度の勾配
    dx = x[1] - x[0]
    dz = z[1] - z[0]
    
    B_x = -np.gradient(phi_m, dx, axis=1)
    B_z = -np.gradient(phi_m, dz, axis=0)
    
    # 原点付近をマスク
    B_x[~mask] = np.nan
    B_z[~mask] = np.nan
    
    # 正規化
    B_magnitude = np.sqrt(B_x**2 + B_z**2)
    B_x_norm = B_x / (B_magnitude + 1e-10)
    B_z_norm = B_z / (B_magnitude + 1e-10)
    
    # ベクトル場のプロット
    ax.quiver(X[mask], Z[mask], B_x_norm[mask], B_z_norm[mask],
              B_magnitude[mask], cmap='plasma', scale=25, width=0.005, alpha=0.8)
    
    # 磁位の等高線
    phi_m_masked = phi_m.copy()
    phi_m_masked[~mask] = np.nan
    contour = ax.contour(X, Z, phi_m_masked, levels=25, colors='gray', alpha=0.3, linewidths=0.5)
    
    # 原点に双極子を表示
    ax.plot(0, 0, 'ko', markersize=12, zorder=5)
    ax.arrow(0, -0.3, 0, 0.6, head_width=0.12, head_length=0.12,
             fc='green', ec='green', linewidth=3, zorder=6)
    ax.text(0.2, 0, 'm', fontsize=16, color='green', weight='bold')
    
    # 磁力線の概略（双極子軸に沿った線）
    theta_lines = np.linspace(0, 2*np.pi, 8)
    for theta in theta_lines:
        if abs(theta - np.pi/2) > 0.1 and abs(theta - 3*np.pi/2) > 0.1:
            r_line = np.linspace(0.2, 2, 50)
            x_line = r_line * np.sin(theta)
            z_line = r_line * np.cos(theta)
            ax.plot(x_line, z_line, 'r--', alpha=0.3, linewidth=1)
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('z', fontsize=12)
    ax.set_title('Magnetic Flux Density B (xz plane, through dipole axis)\n(磁束密度 B, xz平面, 双極子軸を含む)', 
                 fontsize=14, weight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('physics/magnetic_field_xz.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("図3を保存: magnetic_field_xz.png")

# 図4: 磁荷分布の概念図
def plot_charge_distribution():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # 左図: 点磁荷双極子の概念
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_aspect('equal')
    
    # 正負の磁荷
    d = 0.2
    circle1 = Circle((0, d/2), 0.15, color='red', alpha=0.7, zorder=3)
    circle2 = Circle((0, -d/2), 0.15, color='blue', alpha=0.7, zorder=3)
    ax1.add_patch(circle1)
    ax1.add_patch(circle2)
    ax1.text(0, d/2, '+', fontsize=20, ha='center', va='center', weight='bold', zorder=4)
    ax1.text(0, -d/2, '-', fontsize=20, ha='center', va='center', weight='bold', zorder=4)
    
    # 双極子モーメント
    ax1.arrow(0, -d/2, 0, d, head_width=0.1, head_length=0.1,
             fc='green', ec='green', linewidth=3, zorder=2)
    ax1.text(0.25, 0, 'm', fontsize=16, color='green', weight='bold')
    
    # 磁力線
    theta = np.linspace(0, 2*np.pi, 100)
    for r in [0.4, 0.7, 1.0, 1.3]:
        x_c = r * np.cos(theta)
        y_c = r * np.sin(theta)
        ax1.plot(x_c, y_c, 'k-', alpha=0.3, linewidth=1.5)
    
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('z', fontsize=12)
    ax1.set_title('Point Magnetic Dipole\n(点磁荷双極子)', fontsize=13, weight='bold')
    ax1.grid(True, alpha=0.3)
    
    # 右図: 磁荷密度の分布（概念）
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_aspect('equal')
    
    # 原点でのデルタ関数的な分布を表現
    x_dist = np.linspace(-1.5, 1.5, 200)
    z_dist = np.linspace(-1.5, 1.5, 200)
    X_dist, Z_dist = np.meshgrid(x_dist, z_dist)
    R_dist = np.sqrt(X_dist**2 + Z_dist**2)
    
    # 磁荷密度（原点での特異点を表現）
    rho_m = np.exp(-R_dist**2 / 0.05) - np.exp(-R_dist**2 / 0.08)  # 正負の磁荷の分布
    
    im = ax2.contourf(X_dist, Z_dist, rho_m, levels=20, cmap='RdBu_r', alpha=0.7)
    plt.colorbar(im, ax=ax2, label='Magnetic Charge Density (conceptual)')
    
    # 双極子モーメント
    ax2.arrow(0, -0.2, 0, 0.4, head_width=0.1, head_length=0.1,
             fc='green', ec='green', linewidth=3, zorder=5)
    ax2.text(0.25, 0, 'm', fontsize=16, color='green', weight='bold', zorder=6)
    
    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('z', fontsize=12)
    ax2.set_title('Magnetic Charge Distribution ρ_m\n(磁荷密度分布, 概念図)', fontsize=13, weight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('physics/magnetic_charge_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("図4を保存: magnetic_charge_distribution.png")

# 図5: 磁位の3D分布（独立した図）
def plot_magnetic_potential_3d():
    fig = plt.figure(figsize=(14, 10))
    ax1 = fig.add_subplot(111, projection='3d')
    
    # グリッドの作成（xz平面、y=0で表示、より高解像度）
    x = np.linspace(-3, 3, 80)
    z = np.linspace(-3, 3, 80)
    X, Z = np.meshgrid(x, z)
    Y = np.zeros_like(X)  # y=0平面
    
    # 原点を除く
    R = np.sqrt(X**2 + Y**2 + Z**2 + 1e-10)
    
    # 双極子モーメント（z方向）
    m = np.array([0, 0, 1.0])
    
    # 位置ベクトル（xz平面、y=0）
    r_3d = np.sqrt(X**2 + Y**2 + Z**2 + 1e-10)
    # 3D空間での内積: m·r = m_x*x + m_y*y + m_z*z
    m_dot_r = m[0]*X + m[1]*Y + m[2]*Z
    
    # 磁位: Φ_m = (1/(4π)) * (m·r / r³)
    phi_m = (1/(4*np.pi)) * m_dot_r / (r_3d**3)
    
    # 原点付近をマスク
    mask = R > 0.2
    phi_m_masked = phi_m.copy()
    phi_m_masked[~mask] = np.nan
    
    # 3Dサーフェスプロット（より見やすく改善）
    # 値の範囲を確認して適切にスケーリング
    vmin_actual = np.nanmin(phi_m_masked)
    vmax_actual = np.nanmax(phi_m_masked)
    vmax_abs = max(abs(vmin_actual), abs(vmax_actual))
    v_range = max(vmax_abs, 0.01)  # 最小値を確保
    
    # X, Z, phi_m_masked で3Dサーフェスをプロット
    surf = ax1.plot_surface(X, Z, phi_m_masked, cmap='RdBu_r', alpha=0.9, 
                           linewidth=0.2, antialiased=True, 
                           vmin=-v_range, vmax=v_range, shade=True,
                           edgecolor='none', rstride=2, cstride=2)
    
    # ワイヤーフレームを追加（オプション、より構造が見える）
    # ax1.plot_wireframe(X, Z, phi_m_masked, alpha=0.1, linewidth=0.3, color='gray')
    
    # 等高線を底面に投影（磁位軸の最小値に）
    z_min_plot = -v_range * 1.1
    contour = ax1.contour(X, Z, phi_m_masked, zdir='z', offset=z_min_plot, 
                         cmap='RdBu_r', alpha=0.6, levels=20, linewidths=0.8)
    # 等高線のラベル（適度な間隔で）
    ax1.clabel(contour, inline=True, fontsize=7, fmt='%1.2f', 
              colors='black', fontweight='bold')
    
    # 軸の設定
    ax1.set_xlabel('x', fontsize=13, labelpad=10)
    ax1.set_ylabel('z', fontsize=13, labelpad=10)
    ax1.set_zlabel('磁位 φ', fontsize=13, labelpad=10)
    ax1.set_title('磁位の3D分布\n(3D distribution of magnetic potential)', 
                  fontsize=16, weight='bold', pad=25)
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)  # z軸の範囲
    
    # z軸の範囲を動的に設定
    z_min = np.nanmin(phi_m_masked)
    z_max = np.nanmax(phi_m_masked)
    z_range = max(abs(z_min), abs(z_max), 0.01)
    ax1.set_zlim(-z_range*1.1, z_range*1.1)
    
    # 視点角度を調整（より見やすく）
    ax1.view_init(elev=30, azim=45)
    
    # グリッドを有効化
    ax1.grid(True, alpha=0.3)
    
    # カラーバー（適切な刻みで）
    tick_step = z_range / 10
    cbar1 = plt.colorbar(surf, ax=ax1, shrink=0.7, aspect=25, pad=0.15,
                         ticks=np.arange(-z_range, z_range*1.1, tick_step))
    cbar1.set_label('磁位 φ', fontsize=12, rotation=270, labelpad=20)
    
    plt.tight_layout()
    plt.savefig('physics/magnetic_potential_3d.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("図5を保存: magnetic_potential_3d.png")

# 図6: 磁束密度ベクトル場（独立した図）
def plot_magnetic_field_vector():
    fig = plt.figure(figsize=(12, 10))
    ax2 = fig.add_subplot(111)
    
    # グリッドの作成（より細かく）
    x2 = np.linspace(-3, 3, 25)
    y2 = np.linspace(-3, 3, 25)
    X2, Y2 = np.meshgrid(x2, y2)
    
    # 原点を除く
    R2 = np.sqrt(X2**2 + Y2**2)
    mask2 = R2 > 0.2
    
    # 双極子モーメント（y方向）
    m2 = np.array([0, 1.0, 0])
    
    # 位置ベクトル
    r2 = np.sqrt(X2**2 + Y2**2 + 1e-10)
    m_dot_r2 = m2[0]*X2 + m2[1]*Y2
    
    # 磁位
    phi_m2 = (1/(4*np.pi)) * m_dot_r2 / (r2**3)
    
    # 磁束密度の勾配
    dx2 = x2[1] - x2[0]
    dy2 = y2[1] - y2[0]
    
    B_x2 = -np.gradient(phi_m2, dx2, axis=1)
    B_y2 = -np.gradient(phi_m2, dy2, axis=0)
    
    # 原点付近をマスク
    B_x2[~mask2] = np.nan
    B_y2[~mask2] = np.nan
    
    # 正規化（表示用にスケール調整）
    B_magnitude2 = np.sqrt(B_x2**2 + B_y2**2)
    scale_factor = 0.3  # ベクトルの長さを調整
    B_x2_scaled = B_x2 * scale_factor
    B_y2_scaled = B_y2 * scale_factor
    
    # ベクトル場のプロット（色で強度を表現）
    ax2.quiver(X2[mask2], Y2[mask2], B_x2_scaled[mask2], B_y2_scaled[mask2],
              B_magnitude2[mask2], cmap='coolwarm', scale=1.0, width=0.003, 
              alpha=0.7, pivot='mid')
    
    # グリッド点を表示（整数座標に）
    x_grid = np.arange(-3, 4, 1)
    y_grid = np.arange(-3, 4, 1)
    X_grid, Y_grid = np.meshgrid(x_grid, y_grid)
    ax2.scatter(X_grid, Y_grid, c='black', s=8, alpha=0.4, zorder=1)
    
    # 正負の磁荷を表示（y軸方向に配置）
    d = 0.15
    ax2.plot(0, d, 'r+', markersize=25, markeredgewidth=4, 
            label='正の磁荷 (Positive magnetic charge)', zorder=5)
    ax2.plot(0, -d, 'b_', markersize=25, markeredgewidth=4, 
            label='負の磁荷 (Negative magnetic charge)', zorder=5)
    
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.set_aspect('equal')
    ax2.set_xlabel('x', fontsize=13)
    ax2.set_ylabel('y', fontsize=13)
    ax2.set_title('磁束密度ベクトル場\n(Magnetic flux density vector field)', 
                 fontsize=16, weight='bold', pad=15)
    ax2.grid(True, alpha=0.2, linestyle='--')
    ax2.legend(loc='upper right', fontsize=11, framealpha=0.9)
    
    plt.tight_layout()
    plt.savefig('physics/magnetic_field_vector.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("図6を保存: magnetic_field_vector.png")

if __name__ == '__main__':
    print("磁気双極子の可視化を開始...")
    plot_dipole_structure()
    plot_magnetic_field_2d()
    plot_magnetic_field_xz()
    plot_charge_distribution()
    plot_magnetic_potential_3d()
    plot_magnetic_field_vector()
    print("\nすべての図の生成が完了しました！")

