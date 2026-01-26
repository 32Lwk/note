#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define MAX_TRIES 1000000

/* 昇順判定 */
int is_sorted(double *x, int n) {
    for (int i = 1; i < n; i++) {
        if (x[i - 1] > x[i]) return 0;
    }
    return 1;
}

/* Fisher–Yates シャッフル */
void shuffle(double *x, int n) {
    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        double tmp = x[i];
        x[i] = x[j];
        x[j] = tmp;
    }
}

/* qsort 比較関数 */
int cmp_double(const void *a, const void *b) {
    double da = *(const double*)a;
    double db = *(const double*)b;
    if (da < db) return -1;
    if (da > db) return 1;
    return 0;
}

int main(void) {
    int n;
    printf("要素数 n を入力してください: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        fprintf(stderr, "不正な入力です。\n");
        return 1;
    }

    double *x = malloc(sizeof(double) * n);
    if (!x) {
        fprintf(stderr, "メモリ確保失敗。\n");
        return 1;
    }

    printf("%d 個の実数を入力してください:\n", n);
    for (int i = 0; i < n; i++) {
        if (scanf("%lf", &x[i]) != 1) {
            fprintf(stderr, "入力エラー。\n");
            free(x);
            return 1;
        }
    }

    srand((unsigned)time(NULL));

    printf("\n=== Pray Sort 開始 ===\n");

    int success = 0;
    for (int attempt = 0; attempt <= MAX_TRIES; attempt++) {
        if (is_sorted(x, n)) {
            printf("祈りが通じました！（%d回目の祈りで成功）\n", attempt);
            success = 1;
            break;
        }
        if (attempt < MAX_TRIES) {
            printf("pray (%d)\n", attempt + 1);
            shuffle(x, n);
        }
    }

    if (!success) {
        printf("祈りが足りません。qsort()で頑張ります。\n");
        qsort(x, n, sizeof(double), cmp_double);
        printf("がんばりました。\n");
    }

    printf("\nソート後の配列:\n");
    for (int i = 0; i < n; i++) printf("%.2f ", x[i]);
    printf("\n");

    // 平均・分散などの計算
    double sum = 0.0, sum2 = 0.0;
    for (int i = 0; i < n; i++) {
        sum += x[i];
        sum2 += x[i] * x[i];
    }

    double mu = sum / n;
    double var = (sum2 / n) - (mu * mu);
    double min = x[0];
    double max = x[n - 1];

    printf("平均 μ = %.4f\n", mu);
    printf("分散 σ^2 = %.4f\n", var);
    printf("最小値 min = %.4f\n", min);
    printf("最大値 max = %.4f\n", max);

    free(x);
    return 0;
}
