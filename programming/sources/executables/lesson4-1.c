#include <stdio.h>

void convert(int *a, int *b) 
{
    int n = 6; 
    int old_a = *a;
    int old_b = *b;
    *a = 2 * (n + 1) * old_b + old_a;
    *b = 2 * old_a - old_b;
}

int main()
{
    int a = 1, b = 2;
    convert(&a, &b);
    printf("%d %d\n", a, b);
    return 0;
}
