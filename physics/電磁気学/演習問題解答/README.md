# 電磁気学演習問題 解答・解説

このディレクトリには、電磁気学の演習問題（全7回）の解答・解説が含まれています。

## ファイル構成

- `exercise1.tex` - 第1回 (2025年10月3日) の解答
- `exercise2.tex` - 第2回 (2025年10月17日) の解答
- `exercise3.tex` - 第3回 (2025年10月31日) の解答（作成中）
- `exercise4.tex` - 第4回 (2025年11月14日) の解答（作成中）
- `exercise5.tex` - 第5回 (2025年11月28日) の解答（作成中）
- `exercise6.tex` - 第6回 (2025年12月12日) の解答（作成中）
- `exercise7.tex` - 第7回 (2025年12月26日) の解答（作成中）

## 図の生成

各演習問題に対応する図生成スクリプト：
- `generate_figures_ex1.py` - 第1回の図を生成
- `generate_figures_ex2.py` - 第2回の図を生成
- `generate_all_figures.py` - すべての図を生成

## コンパイル方法

```bash
# LuaLaTeXでコンパイル
lualatex exercise1.tex
lualatex exercise2.tex
# ... 他のファイルも同様
```

## 注意事項

- すべての図は`figures/`ディレクトリに保存されます
- 図の生成にはPython 3とmatplotlibが必要です
- 日本語フォント（Hiragino Sans）がインストールされている必要があります
