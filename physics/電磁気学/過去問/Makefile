# 電磁気学過去問 - ビルド
# 使い方: このディレクトリで make または make pdf

LATEX = lualatex
MAIN = past_exam_solutions
BUILD_DIR = build

.PHONY: pdf clean figures clean-build clean-aux

# 過去問解答 PDF を build/ に出力し、このディレクトリにも past_exam_solutions.pdf をコピー
# - で始めることで lualatex のフォント警告等による終了コードを無視
pdf:
	@mkdir -p $(BUILD_DIR)
	-$(LATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR) $(MAIN).tex
	-$(LATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR) $(MAIN).tex
	@cp $(BUILD_DIR)/$(MAIN).pdf $(MAIN).pdf
	@echo "出力: $(MAIN).pdf （このディレクトリ）"

# 図をすべて生成（scripts から実行、figures/ に出力）
figures:
	python3 scripts/generate_figures.py

# build/ を削除
clean-build:
	rm -rf $(BUILD_DIR)

# ルートに残った補助ファイルを削除
clean-aux:
	rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk

clean: clean-build clean-aux
