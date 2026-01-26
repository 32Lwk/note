# トラブルシューティングガイド

## よくある問題と解決策

### 1. Pandocが見つからない

**症状**: 「Pandocが見つかりません」というエラーメッセージが表示される

**解決策**:
1. Pandocがインストールされているか確認:
   ```bash
   pandoc --version
   ```
2. インストールされていない場合:
   - macOS: `brew install pandoc`
   - その他: https://pandoc.org/installing.html

### 2. XeLaTeXが見つからない

**症状**: 「XeLaTeXが見つかりません」というエラーメッセージが表示される

**解決策**:
1. XeLaTeXがインストールされているか確認:
   ```bash
   xelatex --version
   ```
2. インストールされていない場合:
   - macOS: `brew install --cask mactex`
   - その他: https://www.tug.org/texlive/

### 3. フォントが見つからない

**症状**: 警告メッセージが表示される、またはPDFで日本語が正しく表示されない

**解決策**:
1. システムにインストールされているフォントを確認:
   ```bash
   fc-list :lang=ja
   ```
2. 設定で別のフォントを指定:
   - 設定ファイル（`config.json`）で`mainfont`と`cjk_mainfont`を変更

### 4. LaTeXパッケージが不足している

**症状**: LaTeXコンパイルエラーが発生する

**解決策**:
1. 必要なパッケージを確認:
   ```bash
   tlmgr list --only-installed
   ```
2. 不足しているパッケージをインストール:
   ```bash
   sudo tlmgr install xeCJK amsmath amssymb graphicx hyperref geometry
   ```

### 5. 画像が見つからない

**症状**: 警告メッセージが表示される、PDFに画像が表示されない

**解決策**:
1. 画像パスを確認:
   - マークダウンファイルと同じディレクトリ
   - `figures/`サブディレクトリ
   - 親ディレクトリの`figures/`
2. 画像ファイルが存在するか確認
3. 相対パスを使用していることを確認

### 6. 変換がタイムアウトする

**症状**: 大きなファイルの変換が途中で止まる

**解決策**:
1. ファイルサイズを確認（10MB以上の場合は警告が表示されます）
2. ファイルを分割することを検討
3. 画像を最適化する

### 7. テンプレートエラー

**症状**: 「テンプレートエラー」というメッセージが表示される

**解決策**:
1. テンプレートファイルの構文を確認
2. 必須の要素が含まれているか確認:
   - `\documentclass`
   - `\begin{document}` / `\end{document}`
   - `$body$`
3. デフォルトテンプレートを使用することを検討

### 8. 数式が正しく表示されない

**症状**: PDFで数式が正しくレンダリングされない

**解決策**:
1. マークダウンファイルの数式構文を確認:
   - インライン数式: `$...$`
   - ブロック数式: `$$...$$`
2. 数式のペア（開始と終了）が正しいか確認
3. 必要なLaTeXパッケージがインストールされているか確認

## エラーログの確認

エラーログは以下の場所に保存されます:

- アプリケーションログ: `~/Library/Application Support/MarkdownToPDF/logs/app.log`
- エラーログ: `~/Library/Application Support/MarkdownToPDF/logs/errors.log`
- 変換ログ: `~/Library/Application Support/MarkdownToPDF/logs/conversion_log_*.txt`

## サポート

問題が解決しない場合は、エラーログを確認し、詳細なエラーメッセージを記録してください。
