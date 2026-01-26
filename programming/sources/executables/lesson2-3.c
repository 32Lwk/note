/* Report: Lesson 2-3 */
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  char buf[50]; /* 50字制限 */
    double kpc, km;
    const double PC_TO_M = 3.086e16;  /* 1pc = 3.086 x 10^16 m */
    const double M_TO_KM = 1.0e-3;    /* 1km = 1000m */

    printf(" 何kpcを変換したいですか？ (kiloparsec): ");
    fgets(buf, sizeof(buf), stdin);
    if (sscanf(buf, "%lf", &kpc) != 1) {
        fputs("input error\n", stderr);
        exit(-1);
    }

    /* 1kpc = 1000pc, 1pc = 3.086e16 m, 1km = 1000m */
    km = kpc * 1000.0 * PC_TO_M * M_TO_KM;

    printf("kpc = %f\n", kpc);
    printf("km  = %e\n", km);

    return 0;
}

