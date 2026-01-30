# 電磁気学演習問題解答 - ビルド
# 使い方: このディレクトリで make または make pdf

LATEX = lualatex
MAIN = all_exercises
BUILD_DIR = build

.PHONY: pdf clean figures clean-build

# 合冊 PDF を build/ に出力し、このディレクトリにも all_exercises.pdf をコピー
# - で始めることで lualatex のフォント警告等による終了コードを無視
pdf:
	@mkdir -p $(BUILD_DIR)
	-$(LATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR) $(MAIN).tex
	-$(LATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR) $(MAIN).tex
	@cp $(BUILD_DIR)/$(MAIN).pdf $(MAIN).pdf
	@echo "出力: $(MAIN).pdf （このディレクトリ）"

# 個別の exercise をコンパイルする場合（補助ファイルは build/ に）
exercise1 exercise2 exercise3 exercise4 exercise5 exercise6 exercise7:
	@mkdir -p $(BUILD_DIR)
	-$(LATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR) exercise$(subst exercise,,$@).tex
	-$(LATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR) exercise$(subst exercise,,$@).tex
	@echo "出力: $(BUILD_DIR)/exercise$(subst exercise,,$@).pdf"

# 図をすべて生成（scripts から実行、figures/ に出力）
figures:
	python3 scripts/generate_all_figures.py

# build/ を削除
clean-build:
	rm -rf $(BUILD_DIR)

# ルートに残った補助ファイルを削除
clean-aux:
	rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk

clean: clean-build clean-aux
