"""エラーハンドリング: エラー分類と回復戦略"""

from enum import Enum
from typing import List, Optional, Dict
from pathlib import Path


class ErrorType(Enum):
    """エラータイプの列挙"""
    FATAL = "FATAL"  # 致命的エラー
    CONVERSION = "CONVERSION"  # 変換エラー
    WARNING = "WARNING"  # 警告


class ErrorCategory(Enum):
    """エラーカテゴリの列挙"""
    ENVIRONMENT = "ENVIRONMENT"  # 環境エラー
    FILE = "FILE"  # ファイルエラー
    CONVERSION = "CONVERSION"  # 変換エラー
    LATEX = "LATEX"  # LaTeXエラー
    TEMPLATE = "TEMPLATE"  # テンプレートエラー
    IMAGE = "IMAGE"  # 画像エラー
    FONT = "FONT"  # フォントエラー
    GENERAL = "GENERAL"  # 一般エラー


class ConversionError:
    """変換エラーを表現するクラス"""
    
    def __init__(
        self,
        error_type: ErrorType,
        category: ErrorCategory,
        message: str,
        file_path: Optional[Path] = None,
        suggestions: Optional[List[str]] = None,
        context: Optional[Dict] = None
    ):
        self.error_type = error_type
        self.category = category
        self.message = message
        self.file_path = file_path
        self.suggestions = suggestions or []
        self.context = context or {}
    
    def is_fatal(self) -> bool:
        """致命的エラーかどうか"""
        return self.error_type == ErrorType.FATAL
    
    def is_warning(self) -> bool:
        """警告かどうか"""
        return self.error_type == ErrorType.WARNING


class ErrorHandler:
    """エラーハンドリングを行うクラス"""
    
    def __init__(self):
        self.errors: List[ConversionError] = []
        self.warnings: List[ConversionError] = []
    
    def handle_error(
        self,
        error_type: ErrorType,
        category: ErrorCategory,
        message: str,
        file_path: Optional[Path] = None,
        suggestions: Optional[List[str]] = None,
        context: Optional[Dict] = None
    ) -> ConversionError:
        """
        エラーを処理
        
        Args:
            error_type: エラータイプ
            category: エラーカテゴリ
            message: エラーメッセージ
            file_path: 関連するファイルパス
            suggestions: 解決策の提案
            context: 追加のコンテキスト情報
        
        Returns:
            ConversionErrorオブジェクト
        """
        error = ConversionError(
            error_type=error_type,
            category=category,
            message=message,
            file_path=file_path,
            suggestions=suggestions,
            context=context
        )
        
        if error_type == ErrorType.WARNING:
            self.warnings.append(error)
        else:
            self.errors.append(error)
        
        return error
    
    def handle_pandoc_not_found(self) -> ConversionError:
        """Pandocが見つからない場合のエラー"""
        return self.handle_error(
            error_type=ErrorType.FATAL,
            category=ErrorCategory.ENVIRONMENT,
            message="Pandocが見つかりません",
            suggestions=[
                "Pandocをインストールしてください: https://pandoc.org/installing.html",
                "macOSの場合: brew install pandoc"
            ]
        )
    
    def handle_xelatex_not_found(self) -> ConversionError:
        """XeLaTeXが見つからない場合のエラー"""
        return self.handle_error(
            error_type=ErrorType.FATAL,
            category=ErrorCategory.ENVIRONMENT,
            message="XeLaTeXが見つかりません",
            suggestions=[
                "XeLaTeXをインストールしてください: https://www.tug.org/texlive/",
                "macOSの場合: brew install --cask mactex"
            ]
        )
    
    def handle_font_not_found(self, font_name: str, alternatives: List[str] = None) -> ConversionError:
        """フォントが見つからない場合のエラー"""
        suggestions = [f"フォント '{font_name}' が見つかりません"]
        if alternatives:
            suggestions.append("代替フォント:")
            suggestions.extend([f"  - {alt}" for alt in alternatives])
        
        return self.handle_error(
            error_type=ErrorType.WARNING,
            category=ErrorCategory.FONT,
            message=f"フォント '{font_name}' が見つかりません",
            suggestions=suggestions
        )
    
    def handle_template_error(self, template_path: Path, error_message: str) -> ConversionError:
        """テンプレートエラー"""
        return self.handle_error(
            error_type=ErrorType.CONVERSION,
            category=ErrorCategory.TEMPLATE,
            message=f"テンプレートエラー: {error_message}",
            file_path=template_path,
            suggestions=[
                "テンプレートファイルの構文を確認してください",
                "デフォルトテンプレートを使用することを検討してください"
            ]
        )
    
    def handle_image_not_found(self, image_path: str, md_file: Path) -> ConversionError:
        """画像が見つからない場合の警告"""
        return self.handle_error(
            error_type=ErrorType.WARNING,
            category=ErrorCategory.IMAGE,
            message=f"画像が見つかりません: {image_path}",
            file_path=md_file,
            suggestions=[
                "画像パスを確認してください",
                "画像ファイルが存在するか確認してください"
            ]
        )
    
    def handle_conversion_error(self, file_path: Path, error_message: str) -> ConversionError:
        """変換エラー"""
        return self.handle_error(
            error_type=ErrorType.CONVERSION,
            category=ErrorCategory.CONVERSION,
            message=f"変換エラー: {error_message}",
            file_path=file_path,
            suggestions=[
                "マークダウンファイルの構文を確認してください",
                "エラーログを確認してください",
                "トラブルシューティングガイドを参照してください"
            ]
        )
    
    def handle_latex_error(self, file_path: Path, error_message: str) -> ConversionError:
        """LaTeXコンパイルエラー"""
        return self.handle_error(
            error_type=ErrorType.CONVERSION,
            category=ErrorCategory.LATEX,
            message=f"LaTeXコンパイルエラー: {error_message}",
            file_path=file_path,
            suggestions=[
                "LaTeXの構文エラーを確認してください",
                "必要なパッケージがインストールされているか確認してください",
                "エラーログの詳細を確認してください"
            ]
        )
    
    def clear(self) -> None:
        """エラーと警告をクリア"""
        self.errors.clear()
        self.warnings.clear()
    
    def has_errors(self) -> bool:
        """エラーがあるかどうか"""
        return len(self.errors) > 0
    
    def has_warnings(self) -> bool:
        """警告があるかどうか"""
        return len(self.warnings) > 0
    
    def get_fatal_errors(self) -> List[ConversionError]:
        """致命的エラーのリストを取得"""
        return [e for e in self.errors if e.is_fatal()]
