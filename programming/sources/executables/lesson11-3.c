/* 課題11-3: 万有引力による2次元軌道の数値積分（4次精度ルンゲ・クッタ法）
 * 4次精度ルンゲ・クッタ法: 4段、誤差 O(h^5) per step, O(h^4) globally
 * 講義資料: 情報科学概論11回目
 * オイラー法と比較して精度が大幅に向上する
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

/* 4次精度ルンゲ・クッタ法による1ステップ更新
 * 講義資料に従った公式:
 * k1 = f(xn, yn)
 * k2 = f(xn + h/2, yn + h/2*k1)
 * k3 = f(xn + h/2, yn + h/2*k2)
 * k4 = f(xn + h, yn + h*k3)
 * y(n+1) = yn + h/6*(k1 + 2*k2 + 2*k3 + k4)
 * 誤差: O(h^5) per step, O(h^4) globally
 */
void rk4_step(double *x, double *y, double *vx, double *vy, double dt) {
    double k1_x, k1_y, k1_vx, k1_vy;
    double k2_x, k2_y, k2_vx, k2_vy;
    double k3_x, k3_y, k3_vx, k3_vy;
    double k4_x, k4_y, k4_vx, k4_vy;
    
    double x_temp, y_temp, vx_temp, vy_temp;
    
    /* k1の計算 */
    k1_x = *vx;
    k1_y = *vy;
    k1_vx = calc_Fx(*x, *y) / m;
    k1_vy = calc_Fy(*x, *y) / m;
    
    /* k2の計算 */
    x_temp = *x + dt * k1_x / 2.0;
    y_temp = *y + dt * k1_y / 2.0;
    vx_temp = *vx + dt * k1_vx / 2.0;
    vy_temp = *vy + dt * k1_vy / 2.0;
    k2_x = vx_temp;
    k2_y = vy_temp;
    k2_vx = calc_Fx(x_temp, y_temp) / m;
    k2_vy = calc_Fy(x_temp, y_temp) / m;
    
    /* k3の計算 */
    x_temp = *x + dt * k2_x / 2.0;
    y_temp = *y + dt * k2_y / 2.0;
    vx_temp = *vx + dt * k2_vx / 2.0;
    vy_temp = *vy + dt * k2_vy / 2.0;
    k3_x = vx_temp;
    k3_y = vy_temp;
    k3_vx = calc_Fx(x_temp, y_temp) / m;
    k3_vy = calc_Fy(x_temp, y_temp) / m;
    
    /* k4の計算 */
    x_temp = *x + dt * k3_x;
    y_temp = *y + dt * k3_y;
    vx_temp = *vx + dt * k3_vx;
    vy_temp = *vy + dt * k3_vy;
    k4_x = vx_temp;
    k4_y = vy_temp;
    k4_vx = calc_Fx(x_temp, y_temp) / m;
    k4_vy = calc_Fy(x_temp, y_temp) / m;
    
    /* 最終的な更新 */
    *x += dt * (k1_x + 2.0 * k2_x + 2.0 * k3_x + k4_x) / 6.0;
    *y += dt * (k1_y + 2.0 * k2_y + 2.0 * k3_y + k4_y) / 6.0;
    *vx += dt * (k1_vx + 2.0 * k2_vx + 2.0 * k3_vx + k4_vx) / 6.0;
    *vy += dt * (k1_vy + 2.0 * k2_vy + 2.0 * k3_vy + k4_vy) / 6.0;
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
        
        rk4_step(&x, &y, &vx, &vy, DT);
        t += DT;
    }
    
    fclose(fp);
}

int main(void) {
    char filename[100];
    
    printf("課題11-3: 万有引力による2次元軌道の数値積分（ルンゲ・クッタ法）\n");
    printf("時間刻み dt = %.6f\n", DT);
    printf("最大時間 T_MAX = %.1f\n\n", T_MAX);
    
    /* 4つの初期条件で実行 */
    for (int i = 0; i < 4; i++) {
        sprintf(filename, "lesson11-3_case%d.dat", i + 1);
        printf("初期条件 %d: (x, y) = (%.1f, %.1f), (vx, vy) = (%.1f, %.1f)\n",
               i + 1, x0_init[i], y0_init[i], vx0_init[i], vy0_init[i]);
        printf("出力ファイル: %s\n", filename);
        
        integrate(i + 1, x0_init[i], y0_init[i], vx0_init[i], vy0_init[i], filename);
    }
    
    printf("\n計算完了。\n");
    return 0;
}

