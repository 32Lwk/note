/* 課題10-2(2): 二分法 */
#include <stdio.h>
#include <math.h>

#define ACC 1.0e-12
#define MAX_ITER 100

/* 関数 f(x) = 9x exp(-x^2) + 1 */
double f(double x) {
    return 9.0 * x * exp(-x * x) + 1.0;
}

int main(void) {
    double a, b, c, fa, fb, fc;
    int iter;
    
    printf("二分法による方程式 f(x) = 9x exp(-x^2) + 1 = 0 の解法\n\n");
    
    /* 解がありそうな区間1: [-0.2, 0] */
    printf("=== 区間1: [-0.2, 0] ===\n");
    a = -0.2;
    b = 0.0;
    fa = f(a);
    fb = f(b);
    
    if (fa * fb > 0.0) {
        printf("エラー: 区間 [%.2f, %.2f] で f(a) と f(b) が同符号です。\n", a, b);
        printf("f(%.2f) = %.15e, f(%.2f) = %.15e\n", a, fa, b, fb);
    } else {
        printf("初期区間: [%.2f, %.2f]\n", a, b);
        printf("f(%.2f) = %.15e, f(%.2f) = %.15e\n\n", a, fa, b, fb);
        
        iter = 0;
        do {
            if (iter >= MAX_ITER) {
                printf("最大反復回数に達しました。\n");
                break;
            }
            c = (a + b) / 2.0;
            fc = f(c);
            iter++;
            
            printf("反復 %2d: [%.15f, %.15f], c = %.15f, f(c) = %.15e\n", 
                   iter, a, b, c, fc);
            
            if (fabs(fc) < ACC) {
                printf("f(c) が十分に小さい値になりました。\n");
                break;
            }
            
            if (fa * fc < 0.0) {
                b = c;
                fb = fc;
            } else {
                a = c;
                fa = fc;
            }
        } while (fabs(b - a) >= ACC);
        
        printf("\n最終結果:\n");
        printf("近似解: x = %.15f\n", c);
        printf("反復回数: %d\n", iter);
        printf("最終ステップでの |f(x)| = %.15e\n", fabs(fc));
        printf("区間の幅: %.15e\n\n", fabs(b - a));
    }
    
    /* 解がありそうな区間2: [-2, -1.5] */
    printf("=== 区間2: [-2, -1.5] ===\n");
    a = -2.0;
    b = -1.5;
    fa = f(a);
    fb = f(b);
    
    if (fa * fb > 0.0) {
        printf("エラー: 区間 [%.2f, %.2f] で f(a) と f(b) が同符号です。\n", a, b);
        printf("f(%.2f) = %.15e, f(%.2f) = %.15e\n", a, fa, b, fb);
    } else {
        printf("初期区間: [%.2f, %.2f]\n", a, b);
        printf("f(%.2f) = %.15e, f(%.2f) = %.15e\n\n", a, fa, b, fb);
        
        iter = 0;
        do {
            if (iter >= MAX_ITER) {
                printf("最大反復回数に達しました。\n");
                break;
            }
            c = (a + b) / 2.0;
            fc = f(c);
            iter++;
            
            printf("反復 %2d: [%.15f, %.15f], c = %.15f, f(c) = %.15e\n", 
                   iter, a, b, c, fc);
            
            if (fabs(fc) < ACC) {
                printf("f(c) が十分に小さい値になりました。\n");
                break;
            }
            
            if (fa * fc < 0.0) {
                b = c;
                fb = fc;
            } else {
                a = c;
                fa = fc;
            }
        } while (fabs(b - a) >= ACC);
        
        printf("\n最終結果:\n");
        printf("近似解: x = %.15f\n", c);
        printf("反復回数: %d\n", iter);
        printf("最終ステップでの |f(x)| = %.15e\n", fabs(fc));
        printf("区間の幅: %.15e\n", fabs(b - a));
    }
    
    return 0;
}
