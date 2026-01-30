# 統計物理1 過去問 解答・解説

2023年度再試験・2024年度本試験・2025年度本試験の解答・解説をLaTeX形式でまとめたドキュメントです。

## 構成

- **past_exam_solutions.tex** … メインのLaTeXファイル（ltjsarticle、日本語フォント Hiragino）
- **body/** … 年度別の解答本文
  - body_2023.tex … 2023年度再試験（問題I 理想気体の混合、問題II 変な気体、問題III 調和振動子）
  - body_2024.tex … 2024年度本試験（問題I 断熱自由膨張、問題II 左右に仕切られた容器）
  - body_2025.tex … 2025年度本試験（問題I 架空の気体、問題II 2種類の理想気体）
- **figures/** … 図（PNG、300dpi）
- **scripts/generate_figures.py** … 図を生成するPythonスクリプト

## ビルド方法

### 図の生成

```bash
python3 scripts/generate_figures.py
```

（要: Python 3, matplotlib, numpy）

### PDFの作成

```bash
lualatex past_exam_solutions.tex
lualatex past_exam_solutions.tex
```

または

```bash
make
```

（要: LuaLaTeX）

## 注意

- 数式の導出は省略せず段階的に記述しています。
- 図は理解を助ける概念図・グラフです。問題文の図とは異なる場合があります。
