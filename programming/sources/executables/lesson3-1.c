/* 課題3-1 */
#include <stdio.h>

int main(void)
{
    int i = 1;
    int A = 0, B = 0, C = 1;
    double D = 0.0;

    for( ; ; ) {
        A += i;
        B += i * i *i;
        C *= i;
        D += 1.0 / (i * i);
        if(i >= 10) break;
        i++;
    }

    printf("A = %d\n", A);
    printf("B = %d\n", B);
    printf("C = %d\n", C);
    printf("D = %.10f\n", D);

    return 0;
}
