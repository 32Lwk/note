#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

int main(void) {
    FILE *fp;
    const char filename[] = "butterfly.dat";
    const int n = 100;

    if ((fp = fopen(filename, "w")) == NULL) {
        fprintf(stderr, "Cannot open file: %s\n", filename);
        return EXIT_FAILURE;
    }

    for (int i = 0; i < n; ++i) {
        double th = 2.0 * M_PI * i / n;
        double term =
            exp(cos(th)) - 2.0 * cos(4.0 * th) - pow(sin(th / 12.0), 5);
        double x = sin(th) * term;
        double y = cos(th) * term;
        fprintf(fp, "%lf  %lf\n", x, y);
    }

    fclose(fp);
    return EXIT_SUCCESS;
}

