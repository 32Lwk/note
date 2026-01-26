#include <stdio.h>

void swap_array(int *a, int i, int j)
{
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

int main()
{
    int i;
    int a[] = {0,1,2,3,4,5,6};

    swap_array(a, 1, 3);

    for (i = 0; i < sizeof(a)/sizeof(a[0]); i++)
        printf("%d\n", a[i]);

    return 0;
}
