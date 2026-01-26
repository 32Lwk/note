#!/bin/bash

# 力学特論演習問題解答のPDF生成スクリプト
# 目次とアウトラインを含むPDFを生成します

cd "$(dirname "$0")" || exit

echo "PDFを生成中..."

# pandocでMarkdownからPDFに変換
# --toc: 目次を追加
# --toc-depth=3: 目次にセクション、サブセクション、サブサブセクションまで含める
# -H: LaTeXヘッダーファイルを指定
# --pdf-engine=xelatex: XeLaTeXを使用（日本語対応）
# -V geometry: ページレイアウトの設定
# --number-sections: セクション番号を追加

pandoc "力学特論演習問題解答.md" \
  --toc \
  --toc-depth=3 \
  -H "../latex_header.tex" \
  --pdf-engine=xelatex \
  -V geometry:margin=2cm \
  --number-sections \
  -o "力学特論演習問題解答.pdf"

if [ $? -eq 0 ]; then
    echo "PDFの生成が完了しました: 力学特論演習問題解答.pdf"
    echo "目次とアウトラインが含まれています。"
else
    echo "エラー: PDFの生成に失敗しました。"
    exit 1
fi

