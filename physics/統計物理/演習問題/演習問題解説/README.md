# 統計物理学Ⅰ 演習問題 解答・解説

統計物理学Ⅰの演習問題（演習1〜7）の解答・解説をLaTeX形式でまとめたものです。

## 構成

- `all_exercises.tex` - メインドキュメント
- `body/` - 各回の解答本文（exercise1_body.tex 〜 exercise7_body.tex）
- `figures/` - 図ファイル（Pythonで生成）
- `scripts/generate_figures.py` - 図生成スクリプト

## ビルド方法

### 必要な環境

- LuaLaTeX（日本語対応）
- Python 3 + matplotlib, numpy, scipy

### ビルド手順

```bash
# 図の生成
python3 scripts/generate_figures.py

# PDFの生成（2回実行で参照を解決）
lualatex all_exercises.tex
lualatex all_exercises.tex
```

または Makefile を使用：

```bash
make all
```

## 演習の内容

- **演習1**: 熱力学の基礎、理想気体、ガウス積分、ガンマ関数
- **演習2**: ファンデルワールス気体、圧力の高さ依存性、示量・示強変数
- **演習3**: 経路に依存する熱量と仕事、Mayerサイクル、断熱減率
- **演習4**: 最大仕事の原理、カルノー・オットー機関、内部エネルギー
- **演習5**: エントロピー、自由膨張、熱接触
- **演習6**: 熱力学関係式、輪ゴム、混合気体、ポアソン分布
- **演習7**: スターリングの公式、D次元球、調和振動子、古典理想気体
