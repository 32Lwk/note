/* 課題10-4: シンプソン公式による数値積分 */
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

/* シンプソン公式による数値積分 */
double simpson(double a, double b, int n) {
    if (n % 2 != 0) {
        n++;  // nは偶数である必要がある
    }
    
    double h = (b - a) / n;
    double sum = f(a) + f(b);
    
    // 奇数インデックス（i=1,3,5,...）の項: 係数4
    for (int i = 1; i < n; i += 2) {
        sum += 4.0 * f(a + i * h);
    }
    
    // 偶数インデックス（i=2,4,6,...）の項: 係数2
    for (int i = 2; i < n; i += 2) {
        sum += 2.0 * f(a + i * h);
    }
    
    return (h / 3.0) * sum;
}

int main(void) {
    double a = 0.0;
    double b = M_PI;
    double true_value = 2.0;  // ∫[0,π] sin(x) dx = 2
    
    int N_values[] = {100, 200, 400, 800};
    int num_N = sizeof(N_values) / sizeof(N_values[0]);
    
    printf("シンプソン公式による数値積分: ∫[0,π] sin(x) dx\n");
    printf("真値: %.15f\n\n", true_value);
    
    printf("%6s %20s %25s %25s\n", "N", "近似値", "誤差", "h");
    printf("----------------------------------------------------------------------------\n");
    
    for (int i = 0; i < num_N; i++) {
        int N = N_values[i];
        double h = (b - a) / N;
        double approx = simpson(a, b, N);
        double error = fabs(approx - true_value);
        
        printf("%6d %20.15f %25.15e %25.15e\n", N, approx, error, h);
    }
    
    printf("\n誤差の減少率（O(h⁴)の確認）:\n");
    printf("%6s %20s\n", "N", "誤差/h⁴");
    printf("----------------------------------------------------------------------------\n");
    
    for (int i = 0; i < num_N; i++) {
        int N = N_values[i];
        double h = (b - a) / N;
        double approx = simpson(a, b, N);
        double error = fabs(approx - true_value);
        double error_per_h4 = error / (h * h * h * h);
        
        printf("%6d %20.15e\n", N, error_per_h4);
    }
    
    return 0;
}
