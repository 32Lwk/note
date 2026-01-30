# 統計物理1 過去問 解答・解説
MAIN = past_exam_solutions
LATEX = lualatex

.PHONY: all figures pdf clean

all: figures pdf

figures:
	python3 scripts/generate_figures.py

pdf: $(MAIN).tex body/*.tex
	$(LATEX) -interaction=nonstopmode $(MAIN).tex
	$(LATEX) -interaction=nonstopmode $(MAIN).tex

clean:
	rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).toc
	rm -f $(MAIN).pdf
