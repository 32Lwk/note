# 電磁気学演習問題 解答・解説

名古屋大学 理学部物理学科 電磁気学演習（全7回）の解答・解説です。

## フォルダ構成

```
演習問題解答/
├── all_exercises.tex    # 第1回〜第7回を1冊にまとめたメインの LaTeX
├── exercise1.tex … exercise7.tex   # 各回の元原稿（単体でもコンパイル可）
├── body/                # 合冊用の本文（各回の \section 以降）
│   ├── exercise1_body.tex … exercise7_body.tex
├── figures/             # 図（PNG）
├── scripts/             # 図生成スクリプト（Python）
│   ├── generate_figures_ex1.py … generate_figures_ex7.py
│   └── generate_all_figures.py
├── build/               # ビルド出力（PDF と .aux/.log 等）※ make で生成
├── Makefile
└── README.md
```

## 合冊 PDF の作成

このディレクトリで次を実行すると、`build/all_exercises.pdf` ができます。

```bash
make pdf
```

または手動で LuaLaTeX を実行する場合（出力を `build/` にまとめる場合）:

```bash
mkdir -p build
lualatex -output-directory=build all_exercises.tex
lualatex -output-directory=build all_exercises.tex
```

## 各回だけコンパイルする場合

```bash
make exercise1   # → build/exercise1.pdf
# または
lualatex -output-directory=build exercise1.tex
lualatex -output-directory=build exercise1.tex
```

## 図の生成

図は `figures/` に出力されます。このディレクトリで実行してください。

```bash
make figures
# または
python3 scripts/generate_all_figures.py
```

- Python 3 と matplotlib が必要です。
- 日本語表示には日本語フォント（例: Hiragino Sans）が必要です。

## body ファイルの更新

`exerciseN.tex` を編集したあと、合冊用の本文だけを切り出した `body/exerciseN_body.tex` を更新する必要があります。  
本文は「\tableofcontents の次の \newpage の後」から「\end{document} の前」までです。手動でコピーするか、次のように抽出できます。

```bash
sed -n '38,/^\\end{document}$/p' exercise1.tex | sed '$d' > body/exercise1_body.tex
# 同様に exercise2.tex … exercise7.tex に対しても実行
```

## 注意事項

- ビルド時の作業ディレクトリは「演習問題解答」にしてください（`all_exercises.tex` や `figures/` の相対パスに依存します）。
- 補助ファイル（.aux, .log 等）は `build/` に出力するか、`.gitignore` で無視する想定です。
