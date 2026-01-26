/* 課題3-3 ポインター引数を使った平均・分散・標準偏差の計算 */
#include <stdio.h>
#include <math.h>

// 平均
double average(double *x)
{
    double sum = 0.0;
    for (int i = 0; i < 5; i++) {
        sum += x[i];
    }
    return sum / 5.0;
}

// 分散
double variance(double *x)
{
    double mu = average(x);
    double sum_sq = 0.0;
    for (int i = 0; i < 5; i++) {
        sum_sq += x[i] * x[i];
    }
    return (sum_sq / 5.0) - (mu * mu);
}

int main(void)
{
    double x[5];
    double mu, sigma2, sigma;

    printf("5個の実数を入力してください: ");
    for (int i = 0; i < 5; i++) {
        scanf("%lf", &x[i]);
    }

    mu = average(x);
    sigma2 = variance(x);
    sigma = sqrt(sigma2);

    printf("平均 (μ) = %.4f\n", mu);
    printf("分散 (σ^2) = %.4f\n", sigma2);
    printf("標準偏差 (σ) = %.4f\n", sigma);

    return 0;
}
