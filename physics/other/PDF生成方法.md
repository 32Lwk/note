# PDF生成方法と改行問題の解決

## 問題の原因

Pandocで日本語を含むMarkdownをPDF化する際に、以下の問題が発生することがあります：

1. **日本語の自動改行が機能しない**: XeLaTeXのデフォルト設定では、日本語の改行が適切に行われない場合がある
2. **長いテキストがページ幅を超える**: 改行が行われず、テキストがページ外にはみ出す
3. **数式が長すぎる**: 長い数式がページ幅を超える

## 解決方法

### 1. LaTeXヘッダーファイルの使用

`latex_header.tex`ファイルを作成し、以下の設定を追加：

```latex
% 日本語の改行設定（XeLaTeXの標準機能）
\XeTeXlinebreaklocale "ja"
\XeTeXlinebreakskip = 0pt plus 1pt

% 長いテキストの折り返しを許可
\sloppy

% 日本語の改行を改善
\setlength{\emergencystretch}{3em}
\hyphenpenalty=10000
\exhyphenpenalty=10000

% 長い数式の折り返し
\allowdisplaybreaks
```

### 2. Pandocコマンドの実行

```bash
pandoc statistical_physics_exercise6_solution.md \
  -o statistical_physics_exercise6_solution.pdf \
  --pdf-engine=xelatex \
  -H latex_header.tex \
  -V mainfont="Hiragino Mincho ProN" \
  -V geometry:margin=2cm
```

## 各設定の説明

### `\XeTeXlinebreaklocale "ja"`
- 日本語の改行規則を有効にする
- XeLaTeXで日本語を扱う際に必要

### `\XeTeXlinebreakskip = 0pt plus 1pt`
- 改行時のスペース調整
- 改行を柔軟に行うための設定

### `\sloppy`
- 厳密な行幅制限を緩和
- 長い単語やテキストがページ外にはみ出すのを防ぐ

### `\setlength{\emergencystretch}{3em}`
- 緊急時の行幅調整
- 改行が困難な場合に、行幅を少し広げて調整

### `\hyphenpenalty=10000` と `\exhyphenpenalty=10000`
- ハイフネーション（単語の途中での改行）を無効化
- 日本語では不要なため、無効化することで改行を改善

### `\allowdisplaybreaks`
- 数式環境での改行を許可
- 長い数式がページをまたぐ場合に改行を許可

## マージンの調整

必要に応じて、マージンを調整できます：

```bash
-V geometry:margin=2.5cm  # マージンを大きくする
-V geometry:margin=1.5cm  # マージンを小さくする
```

## トラブルシューティング

### エラーが発生する場合

1. **パッケージが見つからない**: BasicTeXには一部のパッケージが含まれていない場合があります。必要に応じて追加インストール：
   ```bash
   sudo tlmgr install <パッケージ名>
   ```

2. **フォントが見つからない**: システムにインストールされているフォント名を確認：
   ```bash
   fc-list :lang=ja
   ```

## 推奨コマンド（完全版）

```bash
cd /Users/yuto/itphy/physics
pandoc statistical_physics_exercise6_solution.md \
  -o statistical_physics_exercise6_solution.pdf \
  --pdf-engine=xelatex \
  -H latex_header.tex \
  -V mainfont="Hiragino Mincho ProN" \
  -V geometry:margin=2cm \
  --toc \
  --toc-depth=2
```

`--toc`と`--toc-depth=2`は目次を追加するオプションです（任意）。

