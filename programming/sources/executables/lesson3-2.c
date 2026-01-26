/* 課題3-2 二次方程式の解 */
#include <stdio.h>
#include <math.h>

int main(void)
{
    double a, b, c;
    double D, real, imag, x1, x2;

    printf("二次方程式 a x^2 + b x + c = 0\n");
    printf("a, b, c を入力してください: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    D = b * b - 4 * a * c; // 判別式

    if (D > 0) {
        x1 = (-b + sqrt(D)) / (2 * a);
        x2 = (-b - sqrt(D)) / (2 * a);
        printf("異なる2実数解: x = %.4f, %.4f\n", x1, x2);
    }
    else if (D == 0) {
        x1 = -b / (2 * a);
        printf("重解: x = %.4f (double)\n", x1);
    }
    else {
        real = -b / (2 * a);
        imag = sqrt(-D) / (2 * a);
        printf("複素数解: x = %.4f + %.4fi, %.4f - %.4fi\n", real, imag, real, imag);
    }

    return 0;
}
