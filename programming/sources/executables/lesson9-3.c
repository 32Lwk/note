#include <stdio.h>
#include <math.h>

int main() {
  double a = 1.0, b = -10000.1, c = 1.0;
  double d = b * b - 4.0 * a * c;
  double sqrt_d = sqrt(d);
  
  // 方法1：標準的な2次方程式の解の公式
  double x1_standard = (-b + sqrt_d) / (2.0 * a);
  double x2_standard = (-b - sqrt_d) / (2.0 * a);
  
  // 方法2：桁落ち回避公式
  double x1_avoid, x2_avoid;
  if (b > 0) {
    x2_avoid = (-b - sqrt_d) / (2.0 * a);
    x1_avoid = c / (a * x2_avoid);
  } else {
    x1_avoid = (-b + sqrt_d) / (2.0 * a);
    x2_avoid = c / (a * x1_avoid);
  }
  
  printf("方法1（標準公式）:\n");
  printf("x1 = %.15f\n", x1_standard);
  printf("x2 = %.15f\n", x2_standard);
  printf("\n方法2（桁落ち回避公式）:\n");
  printf("x1 = %.15f\n", x1_avoid);
  printf("x2 = %.15f\n", x2_avoid);
  
  printf("\n検証（方法1）:\n");
  printf("f(x1) = %.15e\n", x1_standard * x1_standard - 10000.1 * x1_standard + 1.0);
  printf("f(x2) = %.15e\n", x2_standard * x2_standard - 10000.1 * x2_standard + 1.0);
  printf("\n検証（方法2）:\n");
  printf("f(x1) = %.15e\n", x1_avoid * x1_avoid - 10000.1 * x1_avoid + 1.0);
  printf("f(x2) = %.15e\n", x2_avoid * x2_avoid - 10000.1 * x2_avoid + 1.0);
  
  printf("\n=== その他の例：√(1+x) - 1 の桁落ち回避 ===\n");
  double x_small = 1e-10;
  
  // 方法1：直接計算
  double result1 = sqrt(1.0 + x_small) - 1.0;
  
  // 方法2：有理化
  double sqrt_1px = sqrt(1.0 + x_small);
  double result2 = x_small / (sqrt_1px + 1.0);
  
  printf("x = %.15e\n", x_small);
  printf("方法1（直接計算）: √(1+x) - 1 = %.15e\n", result1);
  printf("方法2（有理化）: x / (√(1+x) + 1) = %.15e\n", result2);
  
  return 0;
}

