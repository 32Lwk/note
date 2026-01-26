# Markdown to PDF GUI Tool

マークダウンファイルをPDFに変換するためのGUI管理ツールです。

## 機能

- **GUIインターフェース**: 直感的で使いやすいグラフィカルユーザーインターフェース
- **ドラッグ&ドロップ**: ファイルをドラッグ&ドロップで簡単に選択
- **バッチ変換**: 複数のマークダウンファイルを一度に変換
- **非同期処理**: UIをブロックせずに変換を実行
- **既存スクリプトとの統合**: 既存の変換スクリプトから設定を自動読み込み
- **テンプレート自動検出**: マークダウンファイルと同じディレクトリのテンプレートを自動検出
- **エラーハンドリング**: 詳細なエラーメッセージとトラブルシューティング支援

## 要件

### 必須

- Python 3.8以上
- Pandoc: https://pandoc.org/installing.html
- XeLaTeX: https://www.tug.org/texlive/
- 日本語フォント（Hiragino Sansなど）

### インストール方法

#### macOS

```bash
# Pandoc
brew install pandoc

# XeLaTeX
brew install --cask mactex
```

## インストール

### 1. 依存関係のインストール

```bash
cd markdown_to_pdf_gui
pip install -r requirements.txt
```

### 2. アプリケーションの実行

```bash
python main.py
```

または

```bash
python -m markdown_to_pdf_gui.main
```

## 使用方法

### 基本的な使い方

1. アプリケーションを起動
2. マークダウンファイルをドラッグ&ドロップするか、「ファイルを選択」ボタンで選択
3. 「変換開始」ボタンをクリック
4. 変換が完了すると、マークダウンファイルと同じディレクトリにPDFが生成されます

### 既存スクリプトからの移行

既存の`convert_to_pdf.sh`などのスクリプトを使用している場合、同じディレクトリにあるテンプレートファイル（`pandoc_template.tex`、`pandoc_header.tex`など）が自動的に検出され、使用されます。

## 設定

設定は `~/Library/Application Support/MarkdownToPDF/config.json` に保存されます。

### 設定項目

- `pdf_engine`: PDFエンジン（デフォルト: "xelatex"）
- `mainfont`: メインフォント（デフォルト: "Hiragino Sans"）
- `cjk_mainfont`: CJKフォント（デフォルト: "Hiragino Sans"）
- `geometry`: ページレイアウト（デフォルト: "margin=2.5cm"）
- `toc`: 目次を生成するか（デフォルト: true）
- `toc_depth`: 目次の深度（デフォルト: 2）
- その他、Pandocのオプションに対応

## トラブルシューティング

### Pandocが見つからない

エラーメッセージが表示された場合、Pandocがインストールされているか確認してください。

```bash
pandoc --version
```

### XeLaTeXが見つからない

XeLaTeXがインストールされているか確認してください。

```bash
xelatex --version
```

### フォントが見つからない

システムにインストールされているフォントを確認してください。

```bash
fc-list :lang=ja
```

設定で別のフォントを指定することもできます。

### LaTeXパッケージが不足している

必要なLaTeXパッケージがインストールされているか確認してください。

```bash
tlmgr list --only-installed
```

不足しているパッケージをインストール:

```bash
sudo tlmgr install <パッケージ名>
```

## 開発

### プロジェクト構造

```
markdown_to_pdf_gui/
├── main.py                 # エントリーポイント
├── gui/                    # GUIコンポーネント
├── core/                   # コア機能
├── utils/                  # ユーティリティ
├── templates/              # デフォルトテンプレート
└── config/                 # デフォルト設定
```

### テスト

```bash
pytest
```

## ライセンス

MIT License

## バージョン

現在のバージョン: 1.0.0
