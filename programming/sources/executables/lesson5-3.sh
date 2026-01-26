#!/bin/bash

gcc kadai5-2.c -o kadai5-2

for n in 16 32 64 128 256 512
do
  echo "=== データ数: $n ==="
  ./kadai5-2 <<< "$n" > result$n.txt
  tail -n 1 result$n.txt   # 平均値のみ表示
  echo ""
done
