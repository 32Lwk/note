#include <stdio.h>

int main() {
  double sum1, sum2;
  sum1 = sum2 = 0.0;
  for (int i = 1; i <= 200000; i++) {
    sum1 += 1.0 / i;
  }
  for (int i = 200000; i >= 1; i--) {
    sum2 += 1.0 / i;
  }
  printf("sum1=%.15f\nsum2=%.15f\n", sum1, sum2);
  return 0;
}

