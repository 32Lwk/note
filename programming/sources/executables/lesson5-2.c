#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
  課題5-2 一括版
  [-a,a] の範囲で乱数を生成し、平均値を求めるプログラム。
  学籍番号 062400506 → a = 7
*/

double generate_random(double a)
{
    // [0,1] → [-a,a] への変換
    return ((double)rand() / RAND_MAX) * 2 * a - a;
}

int main(void)
{
    int n, i;
    double a = 7.0;   // n=6 → a=7
    double x, sum = 0.0;

    printf("データ数を入力してください: ");
    scanf("%d", &n);

    srand((unsigned)time(NULL)); // 乱数初期化

    FILE *fp = fopen("rand_data.txt", "w");
    if (fp == NULL) {
        perror("ファイルオープン失敗");
        return 1;
    }

    // 乱数生成＋書き込み＋平均計算
    for (i = 0; i < n; i++) {
        x = generate_random(a);
        fprintf(fp, "%f\n", x);
        sum += x;
    }

    fclose(fp);

    double mean = sum / n;
    printf("平均値: %f\n", mean);

    return 0;
}
