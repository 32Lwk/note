"""構造化ログ管理"""

import logging
import json
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime
from logging.handlers import RotatingFileHandler


class StructuredLogger:
    """構造化ログを管理するクラス"""
    
    def __init__(self, log_dir: Optional[Path] = None):
        """
        ロガーを初期化
        
        Args:
            log_dir: ログファイルの保存ディレクトリ
        """
        if log_dir is None:
            log_dir = Path.home() / ".markdown_to_pdf_gui" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        self.log_dir = log_dir
        self.app_log_path = log_dir / "app.log"
        self.error_log_path = log_dir / "errors.log"
        
        # アプリケーションログの設定
        self.app_logger = logging.getLogger("markdown_to_pdf_gui.app")
        self.app_logger.setLevel(logging.DEBUG)
        
        # ローテーション設定: 10MBごと、最大5ファイル
        app_handler = RotatingFileHandler(
            self.app_log_path,
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8'
        )
        app_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        )
        self.app_logger.addHandler(app_handler)
        
        # エラーログの設定
        self.error_logger = logging.getLogger("markdown_to_pdf_gui.error")
        self.error_logger.setLevel(logging.ERROR)
        
        error_handler = RotatingFileHandler(
            self.error_log_path,
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8'
        )
        error_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        )
        self.error_logger.addHandler(error_handler)
    
    def log_conversion(
        self,
        file_path: str,
        success: bool,
        error_type: Optional[str] = None,
        message: Optional[str] = None,
        context: Optional[Dict] = None
    ) -> None:
        """
        変換ログを記録（構造化形式）
        
        Args:
            file_path: 変換したファイルのパス
            success: 成功フラグ
            error_type: エラータイプ（失敗時）
            message: メッセージ
            context: 追加のコンテキスト情報
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": "ERROR" if not success else "INFO",
            "category": "CONVERSION",
            "file": file_path,
            "success": success,
        }
        
        if error_type:
            log_entry["error_type"] = error_type
        
        if message:
            log_entry["message"] = message
        
        if context:
            log_entry["context"] = context
        
        log_json = json.dumps(log_entry, ensure_ascii=False, indent=2)
        
        if success:
            self.app_logger.info(log_json)
        else:
            self.error_logger.error(log_json)
            self.app_logger.error(log_json)
    
    def log_error(
        self,
        error_type: str,
        message: str,
        category: str = "GENERAL",
        context: Optional[Dict] = None,
        suggestions: Optional[list] = None
    ) -> None:
        """
        エラーログを記録（構造化形式）
        
        Args:
            error_type: エラータイプ
            message: エラーメッセージ
            category: エラーカテゴリ
            context: 追加のコンテキスト情報
            suggestions: 解決策の提案
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": "ERROR",
            "category": category,
            "error_type": error_type,
            "message": message,
        }
        
        if context:
            log_entry["context"] = context
        
        if suggestions:
            log_entry["suggestions"] = suggestions
        
        log_json = json.dumps(log_entry, ensure_ascii=False, indent=2)
        self.error_logger.error(log_json)
        self.app_logger.error(log_json)
    
    def create_conversion_log(self, md_file: Path) -> Path:
        """
        変換ごとの個別ログファイルを作成
        
        Args:
            md_file: 変換するマークダウンファイル
        
        Returns:
            ログファイルのパス
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"conversion_log_{timestamp}.txt"
        log_path = self.log_dir / log_filename
        
        return log_path
    
    def info(self, message: str) -> None:
        """情報ログ"""
        self.app_logger.info(message)
    
    def warning(self, message: str) -> None:
        """警告ログ"""
        self.app_logger.warning(message)
    
    def error(self, message: str) -> None:
        """エラーログ"""
        self.app_logger.error(message)
        self.error_logger.error(message)
    
    def debug(self, message: str) -> None:
        """デバッグログ"""
        self.app_logger.debug(message)
