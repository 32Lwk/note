/* 課題11-1: 万有引力による2次元軌道の数値積分（オイラー法）
 * オイラー法: 1次精度、誤差 O(h^2) per step, O(h) globally
 * 講義資料: 情報科学概論11回目
 */
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/* 定数 */
#define GM 1.0
#define m 1.0
#define DT 0.001  /* 時間刻み */
#define T_MAX 10.0  /* 最大時間 */

/* 初期条件 */
double x0_init[] = {0.7, 1.0, 2.0, 3.0};
double y0_init[] = {0.0, 0.0, 0.0, 0.0};
double vx0_init[] = {0.0, 0.0, 0.0, 0.0};
double vy0_init[] = {1.0, 1.0, 1.0, 1.0};

/* 角運動量を計算 */
double calc_Lz(double x, double y, double vx, double vy) {
    return m * (x * vy - y * vx);
}

/* 原点からの距離を計算 */
double calc_r(double x, double y) {
    return sqrt(x * x + y * y);
}

/* 力のx成分 */
double calc_Fx(double x, double y) {
    double r = calc_r(x, y);
    if (r < 1e-10) return 0.0;  /* ゼロ除算を避ける */
    double r3 = r * r * r;
    return -GM * m * x / r3;
}

/* 力のy成分 */
double calc_Fy(double x, double y) {
    double r = calc_r(x, y);
    if (r < 1e-10) return 0.0;  /* ゼロ除算を避ける */
    double r3 = r * r * r;
    return -GM * m * y / r3;
}

/* オイラー法による1ステップ更新
 * 講義資料に従った公式: y(n+1) = yn + h*f(xn, yn)
 * 1次精度、誤差 O(h^2) per step, O(h) globally
 * テイラー展開の1次までを残した近似
 */
void euler_step(double *x, double *y, double *vx, double *vy, double dt) {
    double Fx = calc_Fx(*x, *y);
    double Fy = calc_Fy(*x, *y);
    
    /* 速度を更新 */
    *vx += dt * Fx / m;
    *vy += dt * Fy / m;
    
    /* 位置を更新 */
    *x += dt * (*vx);
    *y += dt * (*vy);
}

/* 数値積分を実行 */
void integrate(int case_num, double x0_val, double y0_val, 
               double vx0_val, double vy0_val, const char *filename) {
    FILE *fp;
    double x = x0_val;
    double y = y0_val;
    double vx = vx0_val;
    double vy = vy0_val;
    double t = 0.0;
    
    if ((fp = fopen(filename, "w")) == NULL) {
        fprintf(stderr, "Cannot open file: %s\n", filename);
        return;
    }
    
    /* ヘッダー行 */
    fprintf(fp, "# t\tLz\tx\ty\n");
    
    while (t <= T_MAX) {
        double Lz = calc_Lz(x, y, vx, vy);
        double r = calc_r(x, y);
        
        /* 原点に近づきすぎた場合は停止 */
        if (r < 0.01) {
            break;
        }
        
        fprintf(fp, "%.10e\t%.15e\t%.15e\t%.15e\n", t, Lz, x, y);
        
        euler_step(&x, &y, &vx, &vy, DT);
        t += DT;
    }
    
    fclose(fp);
}

int main(void) {
    char filename[100];
    
    printf("課題11-1: 万有引力による2次元軌道の数値積分\n");
    printf("時間刻み dt = %.6f\n", DT);
    printf("最大時間 T_MAX = %.1f\n\n", T_MAX);
    
    /* 4つの初期条件で実行 */
    for (int i = 0; i < 4; i++) {
        sprintf(filename, "lesson11-1_case%d.dat", i + 1);
        printf("初期条件 %d: (x, y) = (%.1f, %.1f), (vx, vy) = (%.1f, %.1f)\n",
               i + 1, x0_init[i], y0_init[i], vx0_init[i], vy0_init[i]);
        printf("出力ファイル: %s\n", filename);
        
        integrate(i + 1, x0_init[i], y0_init[i], vx0_init[i], vy0_init[i], filename);
    }
    
    printf("\n計算完了。\n");
    return 0;
}

