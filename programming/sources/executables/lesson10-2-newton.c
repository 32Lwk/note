/* 課題10-2(1): Newton-Raphson法 */
#include <stdio.h>
#include <math.h>

#define ACC 1.0e-12
#define MAX_ITER 100

/* 関数 f(x) = 9x exp(-x^2) + 1 */
double f(double x) {
    return 9.0 * x * exp(-x * x) + 1.0;
}

/* 導関数 f'(x) = 9exp(-x^2)(1 - 2x^2) */
double dfdx(double x) {
    return 9.0 * exp(-x * x) * (1.0 - 2.0 * x * x);
}

int main(void) {
    double x, xt, res;
    int iter;
    
    printf("Newton-Raphson法による方程式 f(x) = 9x exp(-x^2) + 1 = 0 の解法\n\n");
    
    /* 収束しやすい初期値の例 */
    printf("=== 収束しやすい初期値の例 ===\n");
    x = -0.1;  // 解に近い初期値（解は約-0.11付近）
    printf("初期値: x = %.15f\n\n", x);
    
    iter = 0;
    do {
        if (iter >= MAX_ITER) {
            printf("最大反復回数に達しました。\n");
            break;
        }
        xt = x;
        double df = dfdx(x);
        if (fabs(df) < 1.0e-15) {
            printf("導関数が0に近すぎます。\n");
            break;
        }
        x = xt - f(x) / df;
        res = fabs(x - xt);
        iter++;
        printf("反復 %2d: x = %25.16f, |xt-x| = %25.16e, |f(x)| = %25.16e\n", 
               iter, x, res, fabs(f(x)));
    } while (res >= ACC);
    
    printf("\n最終結果:\n");
    printf("近似解: x = %25.16f\n", x);
    printf("反復回数: %d\n", iter);
    printf("最終ステップでの |f(x)| = %25.16e\n\n", fabs(f(x)));
    
    /* 収束しづらい（または発散する）初期値の例 */
    printf("=== 収束しづらい（または発散する）初期値の例 ===\n");
    x = -0.7;  // 極値点（x = -0.707）に近い初期値（導関数が0に近い）
    printf("初期値: x = %.15f\n\n", x);
    
    iter = 0;
    do {
        if (iter >= MAX_ITER) {
            printf("最大反復回数に達しました。\n");
            break;
        }
        xt = x;
        double df = dfdx(x);
        if (fabs(df) < 1.0e-15) {
            printf("導関数が0に近すぎます。\n");
            break;
        }
        x = xt - f(x) / df;
        res = fabs(x - xt);
        iter++;
        printf("反復 %2d: x = %25.16f, |xt-x| = %25.16e, |f(x)| = %25.16e\n", 
               iter, x, res, fabs(f(x)));
        if (fabs(x) > 10.0) {
            printf("発散している可能性があります。\n");
            break;
        }
    } while (res >= ACC);
    
    printf("\n最終結果:\n");
    printf("近似解: x = %25.16f\n", x);
    printf("反復回数: %d\n", iter);
    printf("最終ステップでの |f(x)| = %25.16e\n", fabs(f(x)));
    
    return 0;
}
