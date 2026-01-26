# API ドキュメント

## コアモジュール

### core.converter

#### Converter

Pandocを使用したPDF変換エンジン

**メソッド**:
- `build_pandoc_command()`: Pandocコマンドを構築
- `convert()`: マークダウンファイルをPDFに変換

### core.converter_thread

#### ConverterThread

非同期変換を実行するQThread

**シグナル**:
- `progress_updated(int, str)`: 進捗更新
- `file_completed(str, bool, str)`: ファイル変換完了
- `error_occurred(str, str, str)`: エラー発生

### core.config_manager

#### ConfigManager

設定を管理するクラス

**メソッド**:
- `load_config()`: 設定を読み込み
- `save_config()`: 設定を保存
- `load_profile(name)`: プロファイルを読み込み
- `save_profile(name)`: プロファイルを保存

### core.template_manager

#### TemplateManager

テンプレートを管理するクラス

**メソッド**:
- `find_templates()`: テンプレートとヘッダーファイルを検出
- `validate_template()`: テンプレートのバリデーション

## ユーティリティモジュール

### utils.logger

#### StructuredLogger

構造化ログを管理するクラス

**メソッド**:
- `log_conversion()`: 変換ログを記録
- `log_error()`: エラーログを記録

### utils.path_validator

#### PathValidator

パスの検証と正規化を行うクラス

**メソッド**:
- `validate_path()`: パスを検証し、正規化
- `is_safe_path()`: パスが安全かどうかを確認
