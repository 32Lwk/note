CC = gcc
CFLAGS = -Wall -O2 -lm
PYTHON = python3
DATA_DIR = data
FIGURES_DIR = figures

# ディレクトリを作成
$(DATA_DIR):
	mkdir -p $(DATA_DIR)

$(FIGURES_DIR):
	mkdir -p $(FIGURES_DIR)

# ターゲット
all: normal_rand brownian_motion $(DATA_DIR) $(FIGURES_DIR)

# 正規分布乱数生成プログラム
normal_rand: normal_rand.c
	$(CC) $(CFLAGS) -o normal_rand normal_rand.c -lm

# ブラウン運動シミュレーションプログラム
brownian_motion: brownian_motion.c
	$(CC) $(CFLAGS) -o brownian_motion brownian_motion.c -lm

# 課題(1): 正規分布乱数のヒストグラム
task1: normal_rand $(DATA_DIR) $(FIGURES_DIR)
	@echo "正規分布乱数を生成中..."
	./normal_rand 50 > $(DATA_DIR)/normal_rand_50.dat
	./normal_rand 100 > $(DATA_DIR)/normal_rand_100.dat
	./normal_rand 1000 > $(DATA_DIR)/normal_rand.dat
	@echo "ヒストグラムを描画中..."
	$(PYTHON) plot_normal_rand.py 50
	$(PYTHON) plot_normal_rand.py 100
	$(PYTHON) plot_normal_rand.py 1000

# 課題(2): ブラウン運動のシミュレーション
task2: brownian_motion $(DATA_DIR)
	@echo "ブラウン運動のシミュレーションを実行中..."
	./brownian_motion > $(DATA_DIR)/trajectory.dat

# 課題(3): 軌道の可視化
task3: brownian_motion $(DATA_DIR) $(FIGURES_DIR)
	@echo "軌道を可視化中..."
	$(PYTHON) visualize_trajectories.py 5

# 課題(4): 平均二乗変位の計算
task4: brownian_motion $(DATA_DIR) $(FIGURES_DIR)
	@echo "平均二乗変位を計算中..."
	$(PYTHON) visualize_msd.py 5

# 課題(5): 拡散係数の解析
task5: $(FIGURES_DIR)
	@echo "拡散係数を解析中..."
	$(PYTHON) analyze_diffusion.py
	$(PYTHON) plot_msd_parameters.py

# 課題(6): エネルギー分布関数
task6: brownian_motion $(DATA_DIR) $(FIGURES_DIR)
	@echo "エネルギー分布関数を解析中..."
	$(PYTHON) analyze_energy.py

# すべての課題を実行
all_tasks: task1 task2 task3 task4 task5 task6
	@echo "すべての課題が完了しました！"

# レポートのPDF生成
report: $(FIGURES_DIR)
	@echo "レポートを生成中..."
	lualatex -interaction=nonstopmode report.tex > /dev/null 2>&1
	lualatex -interaction=nonstopmode report.tex > /dev/null 2>&1
	@echo "レポート生成完了: report.pdf"

# クリーンアップ
clean:
	rm -f normal_rand brownian_motion
	rm -rf $(DATA_DIR) $(FIGURES_DIR)
	rm -f report.pdf report.aux report.log report.out report.dvi report.map

.PHONY: all task1 task2 task3 task4 task5 task6 all_tasks clean report
