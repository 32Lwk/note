#!/bin/bash

# 物理実験学期末試験_詳細解答.md をPDFに変換するスクリプト（シンプル版）
# テンプレートを使わず、ヘッダーファイルのみを使用

cd "$(dirname "$0")"

INPUT_FILE="物理実験学期末試験_詳細解答.md"
OUTPUT_FILE="物理実験学期末試験_詳細解答.pdf"

echo "PDF変換を開始します..."
echo "入力ファイル: $INPUT_FILE"
echo "出力ファイル: $OUTPUT_FILE"

# pandocでPDF変換（テンプレートを使わない方法）
pandoc "$INPUT_FILE" \
  --pdf-engine=xelatex \
  --from=markdown+tex_math_dollars+raw_tex \
  --to=pdf \
  --variable=mainfont:"Hiragino Sans" \
  --variable=CJKmainfont:"Hiragino Sans" \
  --variable=geometry:"margin=2.5cm" \
  --variable=fontsize:"10pt" \
  --variable=documentclass:"article" \
  --variable=toc:"true" \
  --variable=toc-depth:"2" \
  --variable=colorlinks:"true" \
  --variable=linkcolor:"blue" \
  --variable=urlcolor:"blue" \
  --variable=toccolor:"blue" \
  --include-in-header=pandoc_header.tex \
  --standalone \
  --output="$OUTPUT_FILE" \
  2>&1 | tee conversion_log.txt

if [ $? -eq 0 ]; then
  echo ""
  echo "✓ PDF変換が完了しました: $OUTPUT_FILE"
  echo ""
  echo "変換ログは conversion_log.txt に保存されています。"
  echo "図や文字化けがないか確認してください。"
else
  echo ""
  echo "✗ PDF変換中にエラーが発生しました。"
  echo "conversion_log.txt を確認してください。"
  exit 1
fi
