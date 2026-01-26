#include <stdio.h>
#include <string.h>

/*
  shift_string関数：
  文字列の最初の文字を末尾に回し、
  残りの文字を左に1文字ずつずらす。
  例: "abcde" → "bcdea"
*/

void shift_string(char *c)
{
    int i, n;
    n = strlen(c);         // 文字列の長さ
    char d[n + 1];         // 作業用バッファ

    for (i = 0; i < n - 1; i++) {
        d[i] = c[i + 1];
    }
    d[n - 1] = c[0];       // 最初の文字を最後に
    d[n] = '\0';

    strcpy(c, d);          // 元の配列にコピー
}

int main(void)
{
    char c[] = "abcde";

    puts("変換前：");
    puts(c);

    shift_string(c);

    puts("変換後：");
    puts(c);

    return 0;
}
