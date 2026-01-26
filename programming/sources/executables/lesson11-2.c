/* 課題11-2: 斜方投射の境界値問題
 * 投射角度と投射距離から初速度を求める
 * 講義資料: 情報科学概論11回目（斜方投射の例を参考）
 * 線形内挿による着地点の計算: x = (x1*z0 - x0*z1)/(z0-z1)
 */
#include <stdio.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

#define G 9.8  /* 重力加速度 [m/s^2] */
#define ACC 1.0e-8  /* 収束判定の精度 */
#define MAX_ITER 100  /* 最大反復回数 */
#define DT 0.001  /* 数値積分の時間刻み */

/* 角度を度からラジアンに変換 */
double deg_to_rad(double deg) {
    return deg * M_PI / 180.0;
}

/* 斜方投射の到達距離を計算（数値積分、講義資料に従った線形内挿を使用）*/
double calculate_range(double v0, double theta) {
    double x = 0.0;
    double y = 0.0;
    double vx = v0 * cos(theta);
    double vy = v0 * sin(theta);
    double t = 0.0;
    
    double x0 = 0.0, y0 = 0.0;  /* 着地点通過前の点 */
    double x1, y1;  /* 着地点通過後の点 */
    
    /* y >= 0 の間で計算を続ける */
    while (y >= 0.0) {
        /* 前の点を保存 */
        x0 = x;
        y0 = y;
        
        /* 次の点を計算 */
        x += vx * DT;
        y += vy * DT;
        vy -= G * DT;
        t += DT;
        
        /* 発散を防ぐ */
        if (t > 100.0) break;
    }
    
    /* 着地点通過後の点 */
    x1 = x;
    y1 = y;
    
    /* 線形内挿で着地点を求める（講義資料の公式: x = (x1*z0 - x0*z1)/(z0-z1)）*/
    /* ここでは z が y 座標に相当（z0 = y0 > 0, z1 = y1 < 0）*/
    if (fabs(y0 - y1) < 1e-10) {
        return x0;  /* y0とy1がほぼ等しい場合 */
    }
    double x_landing = (x1 * y0 - x0 * y1) / (y0 - y1);
    
    return x_landing;
}

/* 二分法による初速度の探索 */
double bisection_method(double theta, double target_range, 
                        double v0_min, double v0_max, int *iter_count) {
    double a = v0_min;
    double b = v0_max;
    double c, fa, fb, fc, range;
    int iter = 0;
    
    fa = calculate_range(a, theta) - target_range;
    fb = calculate_range(b, theta) - target_range;
    
    if (fa * fb > 0.0) {
        printf("エラー: 区間 [%.2f, %.2f] で符号が一致しません。\n", a, b);
        return -1.0;
    }
    
    do {
        if (iter >= MAX_ITER) {
            printf("最大反復回数に達しました。\n");
            break;
        }
        
        c = (a + b) / 2.0;
        range = calculate_range(c, theta);
        fc = range - target_range;
        iter++;
        
        printf("反復 %2d: v0 = %15.8f, 到達距離 = %15.8f, 誤差 = %15.8e\n",
               iter, c, range, fabs(fc));
        
        if (fabs(fc) < ACC) {
            break;
        }
        
        if (fa * fc < 0.0) {
            b = c;
            fb = fc;
        } else {
            a = c;
            fa = fc;
        }
    } while (fabs(b - a) >= ACC);
    
    *iter_count = iter;
    return c;
}

/* ニュートン法による初速度の探索（高精度版）*/
double newton_method(double theta, double target_range, 
                     double v0_init, int *iter_count) {
    double v0 = v0_init;
    double v0_old;
    double range, error, derror;
    double h = 1.0e-6;  /* 数値微分の刻み */
    int iter = 0;
    
    do {
        if (iter >= MAX_ITER) {
            printf("最大反復回数に達しました。\n");
            break;
        }
        
        v0_old = v0;
        range = calculate_range(v0, theta);
        error = range - target_range;
        
        /* 数値微分 */
        double range_plus = calculate_range(v0 + h, theta);
        derror = (range_plus - range) / h;
        
        if (fabs(derror) < 1.0e-15) {
            printf("導関数が0に近すぎます。\n");
            break;
        }
        
        v0 = v0_old - error / derror;
        
        /* 負の値にならないように */
        if (v0 < 0.0) {
            v0 = v0_old / 2.0;
        }
        
        iter++;
        printf("反復 %2d: v0 = %15.8f, 到達距離 = %15.8f, 誤差 = %15.8e\n",
               iter, v0, range, fabs(error));
        
        if (fabs(error) < ACC) {
            break;
        }
    } while (fabs(v0 - v0_old) >= ACC);
    
    *iter_count = iter;
    return v0;
}

int main(void) {
    double theta_deg, target_range;
    double theta;
    double v0_bisection, v0_newton;
    int iter_bisection, iter_newton;
    
    printf("斜方投射の境界値問題: 投射角度と投射距離から初速度を求める\n\n");
    
    printf("投射角度（度）を入力してください: ");
    if (scanf("%lf", &theta_deg) != 1) {
        fprintf(stderr, "入力エラー\n");
        return 1;
    }
    
    printf("投射距離（m）を入力してください: ");
    if (scanf("%lf", &target_range) != 1) {
        fprintf(stderr, "入力エラー\n");
        return 1;
    }
    
    theta = deg_to_rad(theta_deg);
    
    printf("\n=== 入力値 ===\n");
    printf("投射角度: %.2f 度\n", theta_deg);
    printf("投射距離: %.2f m\n\n", target_range);
    
    /* 二分法による解法 */
    printf("=== 二分法による解法 ===\n");
    /* 初速度の範囲を適切に設定 */
    double v0_min = 1.0;
    double v0_max = 100.0;
    
    v0_bisection = bisection_method(theta, target_range, v0_min, v0_max, &iter_bisection);
    
    if (v0_bisection > 0.0) {
        printf("\n二分法の結果:\n");
        printf("初速度 v0 = %.8f m/s\n", v0_bisection);
        printf("反復回数: %d\n", iter_bisection);
        
        double final_range = calculate_range(v0_bisection, theta);
        printf("実際の到達距離: %.8f m\n", final_range);
        printf("誤差: %.8e m\n\n", fabs(final_range - target_range));
    }
    
    /* ニュートン法による解法（高精度版）*/
    printf("=== ニュートン法による解法（高精度版）===\n");
    /* 二分法の結果を初期値として使用 */
    double v0_init = (v0_bisection > 0.0) ? v0_bisection : 10.0;
    
    v0_newton = newton_method(theta, target_range, v0_init, &iter_newton);
    
    printf("\nニュートン法の結果:\n");
    printf("初速度 v0 = %.8f m/s\n", v0_newton);
    printf("反復回数: %d\n", iter_newton);
    
    double final_range_newton = calculate_range(v0_newton, theta);
    printf("実際の到達距離: %.8f m\n", final_range_newton);
    printf("誤差: %.8e m\n", fabs(final_range_newton - target_range));
    
    printf("\n=== 精度向上の比較 ===\n");
    if (v0_bisection > 0.0) {
        printf("二分法の反復回数: %d\n", iter_bisection);
        printf("ニュートン法の反復回数: %d\n", iter_newton);
        printf("計算回数の減少: %.1f%%\n", 
               100.0 * (1.0 - (double)iter_newton / iter_bisection));
        
        double error_bisection = fabs(calculate_range(v0_bisection, theta) - target_range);
        double error_newton = fabs(calculate_range(v0_newton, theta) - target_range);
        if (error_bisection > 0.0) {
            printf("誤差の減少: %.1f%%\n", 
                   100.0 * (1.0 - error_newton / error_bisection));
        }
    }
    
    return 0;
}

