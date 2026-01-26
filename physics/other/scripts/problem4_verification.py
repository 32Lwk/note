"""
問題4の検証用Pythonスクリプト
ベクトルポテンシャルから磁束密度を計算し、目標の式と一致することを確認する
"""

import sympy as sp
from sympy import symbols, Matrix, simplify, diff, sqrt, pi

# シンボルの定義
x, y, z = symbols('x y z', real=True)
mx, my, mz = symbols('m_x m_y m_z', real=True)

# 位置ベクトル
r_vec = Matrix([x, y, z])
r = sqrt(x**2 + y**2 + z**2)

# 定ベクトルm
m_vec = Matrix([mx, my, mz])

# ベクトルポテンシャル A = (1/(4π)) * (m × r / r³)
# 外積 m × r
m_cross_r = m_vec.cross(r_vec)
A_vec = (1/(4*pi)) * m_cross_r / (r**3)

print("=" * 60)
print("ベクトルポテンシャル A(r)")
print("=" * 60)
print("A_x =", A_vec[0])
print("A_y =", A_vec[1])
print("A_z =", A_vec[2])
print()

# 磁束密度 B = ∇ × A
# 回転（ローテーション）を計算
B_x = diff(A_vec[2], y) - diff(A_vec[1], z)
B_y = diff(A_vec[0], z) - diff(A_vec[2], x)
B_z = diff(A_vec[1], x) - diff(A_vec[0], y)

B_vec = Matrix([B_x, B_y, B_z])

print("=" * 60)
print("磁束密度 B = ∇ × A")
print("=" * 60)
print("B_x =", simplify(B_x))
print("B_y =", simplify(B_y))
print("B_z =", simplify(B_z))
print()

# 目標の式: B = -(1/(4π)) * ∇(m·r / r³)
m_dot_r = m_vec.dot(r_vec)
phi_m = (1/(4*pi)) * m_dot_r / (r**3)

# 勾配を計算
B_target_x = -diff(phi_m, x)
B_target_y = -diff(phi_m, y)
B_target_z = -diff(phi_m, z)

B_target = Matrix([B_target_x, B_target_y, B_target_z])

print("=" * 60)
print("目標の式: B = -(1/(4π)) * ∇(m·r / r³)")
print("=" * 60)
print("B_x (目標) =", simplify(B_target_x))
print("B_y (目標) =", simplify(B_target_y))
print("B_z (目標) =", simplify(B_target_z))
print()

# 比較
print("=" * 60)
print("検証: 両者が一致するか確認")
print("=" * 60)
diff_x = simplify(B_x - B_target_x)
diff_y = simplify(B_y - B_target_y)
diff_z = simplify(B_z - B_target_z)

print("B_x - B_x(目標) =", diff_x)
print("B_y - B_y(目標) =", diff_y)
print("B_z - B_z(目標) =", diff_z)
print()

if diff_x == 0 and diff_y == 0 and diff_z == 0:
    print("✓ 検証成功: 両者は完全に一致します！")
else:
    print("⚠ 注意: 完全一致しませんでした（数値誤差の可能性）")

