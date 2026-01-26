#include <stdio.h>

int main() {
  double x = 0.1;
  double sum = 0.0;
  for (int i = 0; i < 1000000; i++) {
    sum += x;
  }
  printf("sum = %.15f\n", sum);
  return 0;
}

