# 統計物理学Ⅰ 演習問題解答 Makefile

.PHONY: all figures pdf clean

all: figures pdf

# Pythonで図を生成
figures:
	python3 scripts/generate_figures.py

# LaTeXをコンパイル
pdf: figures
	lualatex -interaction=nonstopmode all_exercises.tex
	lualatex -interaction=nonstopmode all_exercises.tex

clean:
	rm -f all_exercises.aux all_exercises.log all_exercises.out all_exercises.toc
	rm -f all_exercises.pdf
