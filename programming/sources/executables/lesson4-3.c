#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define BUF_SIZE 256

float rms_array(float *a, int n)
{
    float sum = 0.0f;
    for (int i = 0; i < n; i++) {
        sum += a[i] * a[i];
    }
    return sqrtf(sum / n);
}

void minmax(float *a, int n, float *min, float *max)
{
    *min = *max = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] < *min) *min = a[i];
        if (a[i] > *max) *max = a[i];
    }
}

int main()
{
    int i, matrix_size;
    float *a, min, max;
    char buf[BUF_SIZE];

    printf("Matrix size = ");
    fgets(buf, sizeof(buf), stdin);
    if (1 != sscanf(buf, "%d", &matrix_size) || matrix_size < 1) {
        fprintf(stderr, "Invalid Matrix size!\n");
        exit(-1);
    }

    a = (float *)malloc(sizeof(float) * matrix_size);
    if (a == NULL) {
        fprintf(stderr, "Cannot allocate memory!\n");
        exit(-1);
    }

    for (i = 0; i < matrix_size; i++) {
        printf("please input vector element %d = ", i + 1);
        fgets(buf, sizeof(buf), stdin);
        if (sscanf(buf, "%f", &a[i]) != 1) {
            fputs("input error\n", stderr);
            exit(-1);
        }
    }

    printf("rms = %5.2f\n", rms_array(a, matrix_size));
    minmax(a, matrix_size, &min, &max);
    printf("min, max = %5.2f, %5.2f\n", min, max);

    free(a);
    return 0;
}
