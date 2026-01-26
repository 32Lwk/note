/* 課題10-3: 台形公式による数値積分 */
/* ∫[0,π] sin(x) dx を計算 */
#include <stdio.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

/* 被積分関数 f(x) = sin(x) */
double f(double x) {
    return sin(x);
}

/* 台形公式による数値積分 */
double trapezoidal(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.5 * (f(a) + f(b));
    
    for (int i = 1; i < n; i++) {
        sum += f(a + i * h);
    }
    
    return h * sum;
}

int main(void) {
    double a = 0.0;
    double b = M_PI;
    double true_value = 2.0;  // ∫[0,π] sin(x) dx = 2
    
    int N_values[] = {100, 200, 400, 800};
    int num_N = sizeof(N_values) / sizeof(N_values[0]);
    
    printf("台形公式による数値積分: ∫[0,π] sin(x) dx\n");
    printf("真値: %.15f\n\n", true_value);
    
    printf("%6s %20s %25s %25s\n", "N", "近似値", "誤差", "h");
    printf("----------------------------------------------------------------------------\n");
    
    for (int i = 0; i < num_N; i++) {
        int N = N_values[i];
        double h = (b - a) / N;
        double approx = trapezoidal(a, b, N);
        double error = fabs(approx - true_value);
        
        printf("%6d %20.15f %25.15e %25.15e\n", N, approx, error, h);
    }
    
    printf("\n誤差の減少率（O(h²)の確認）:\n");
    printf("%6s %20s\n", "N", "誤差/h²");
    printf("----------------------------------------------------------------------------\n");
    
    for (int i = 0; i < num_N; i++) {
        int N = N_values[i];
        double h = (b - a) / N;
        double approx = trapezoidal(a, b, N);
        double error = fabs(approx - true_value);
        double error_per_h2 = error / (h * h);
        
        printf("%6d %20.15e\n", N, error_per_h2);
    }
    
    return 0;
}
