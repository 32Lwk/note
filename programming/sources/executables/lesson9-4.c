#include <stdio.h>
#include <math.h>

#define ACC 1.0e-12 

double f(double x) {
  return cos(x) + x * log(x) - 1.0;
}

double dfdx(double x) {
  return -sin(x) + log(x) + 1.0;
}

int main() {
  double x, xt, res;
  
  x = 1.0; 
  
  printf("Newton法による方程式 f(x) = cos(x) + x*ln(x) - 1 = 0 の解法\n");
  printf("初期値: x = %.15f\n\n", x);
  
  do { 
    xt = x;
    x = xt - f(x) / dfdx(x); 
    res = fabs(x - xt);
    printf("x=%25.16f, |xt-x|=%25.16e, |f(x)|=%25.16e\n", x, res, fabs(f(x)));
  } while (res >= ACC); 
  
  printf("\n最終結果:\n");
  printf("近似解: x = %25.16f\n", x);
  printf("最終ステップでの |f(x)| = %25.16e\n", fabs(f(x)));
  
  return 0;
}

