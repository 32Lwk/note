"""非同期変換エンジン: QThreadを使用した非同期処理"""

from enum import Enum
from pathlib import Path
from typing import Dict, Optional, List
from PyQt6.QtCore import QThread, pyqtSignal
from .converter import Converter
from .error_handler import ErrorHandler, ErrorType, ErrorCategory
from .markdown_validator import MarkdownValidator
from ..utils.logger import StructuredLogger


class ConversionState(Enum):
    """変換状態の列挙"""
    IDLE = "idle"
    PREPROCESSING = "preprocessing"
    CONVERTING = "converting"
    POSTPROCESSING = "postprocessing"
    COMPLETED = "completed"
    ERROR = "error"
    CANCELLED = "cancelled"


class ConverterThread(QThread):
    """非同期変換を実行するQThread"""
    
    # シグナル定義
    progress_updated = pyqtSignal(int, str)  # 進捗率(0-100), メッセージ
    state_changed = pyqtSignal(str, float)  # 状態, 進捗率
    file_completed = pyqtSignal(str, bool, str)  # ファイル名, 成功/失敗, メッセージ
    error_occurred = pyqtSignal(str, str, str)  # エラータイプ, カテゴリ, メッセージ
    
    def __init__(
        self,
        md_files: List[Path],
        output_dir: Optional[Path] = None,
        config: Optional[Dict] = None,
        template_path: Optional[Path] = None,
        header_path: Optional[Path] = None,
        logger: Optional[StructuredLogger] = None
    ):
        super().__init__()
        self.md_files = md_files
        self.output_dir = output_dir
        self.config = config or {}
        self.template_path = template_path
        self.header_path = header_path
        self.logger = logger
        
        self.converter = Converter()
        self.validator = MarkdownValidator()
        self.error_handler = ErrorHandler()
        self.state = ConversionState.IDLE
        self._cancelled = False
    
    def run(self) -> None:
        """変換処理を実行"""
        try:
            total_files = len(self.md_files)
            
            for idx, md_file in enumerate(self.md_files):
                if self.isInterruptionRequested() or self._cancelled:
                    self.state = ConversionState.CANCELLED
                    self.state_changed.emit(self.state.value, 0.0)
                    return
                
                # 前処理
                self.state = ConversionState.PREPROCESSING
                progress = (idx / total_files) * 100
                self.state_changed.emit(self.state.value, progress)
                self.progress_updated.emit(int(progress), f"前処理中: {md_file.name}")
                
                # マークダウンファイルの検証
                validation_result = self.validator.validate(md_file)
                
                if not validation_result.is_valid():
                    error_msg = "; ".join(validation_result.errors)
                    self.error_handler.handle_conversion_error(md_file, error_msg)
                    self.file_completed.emit(str(md_file), False, error_msg)
                    if self.logger:
                        self.logger.log_conversion(
                            str(md_file),
                            False,
                            "VALIDATION_ERROR",
                            error_msg
                        )
                    continue
                
                # 警告の処理
                for warning in validation_result.warnings:
                    self.error_handler.handle_error(
                        ErrorType.WARNING,
                        ErrorCategory.FILE,
                        warning,
                        md_file
                    )
                
                # 変換
                self.state = ConversionState.CONVERTING
                progress = ((idx + 0.5) / total_files) * 100
                self.state_changed.emit(self.state.value, progress)
                self.progress_updated.emit(int(progress), f"変換中: {md_file.name}")
                
                success, output_file, error_msg = self.converter.convert(
                    md_file,
                    self.output_dir,
                    self.config,
                    self.template_path,
                    self.header_path
                )
                
                # 後処理
                self.state = ConversionState.POSTPROCESSING
                progress = ((idx + 0.9) / total_files) * 100
                self.state_changed.emit(self.state.value, progress)
                self.progress_updated.emit(int(progress), f"後処理中: {md_file.name}")
                
                if success and output_file:
                    # PDF検証（簡易版）
                    if output_file.exists():
                        self.file_completed.emit(str(md_file), True, f"完了: {output_file.name}")
                        if self.logger:
                            self.logger.log_conversion(
                                str(md_file),
                                True,
                                None,
                                f"出力: {output_file}",
                                {"output_file": str(output_file)}
                            )
                    else:
                        self.file_completed.emit(str(md_file), False, "PDFファイルが生成されませんでした")
                else:
                    self.file_completed.emit(str(md_file), False, error_msg or "変換に失敗しました")
                    if self.logger:
                        self.logger.log_conversion(
                            str(md_file),
                            False,
                            "CONVERSION_ERROR",
                            error_msg or "変換に失敗しました"
                        )
                
                # 完了
                progress = ((idx + 1) / total_files) * 100
                self.state_changed.emit(ConversionState.COMPLETED.value, progress)
                self.progress_updated.emit(int(progress), f"完了: {md_file.name}")
            
            self.state = ConversionState.COMPLETED
            self.state_changed.emit(self.state.value, 100.0)
        
        except Exception as e:
            self.state = ConversionState.ERROR
            self.state_changed.emit(self.state.value, 0.0)
            error_msg = f"予期しないエラー: {str(e)}"
            self.error_occurred.emit("FATAL", "GENERAL", error_msg)
            if self.logger:
                self.logger.log_error(
                    "UNEXPECTED_ERROR",
                    error_msg,
                    "GENERAL"
                )
    
    def cancel(self) -> None:
        """変換をキャンセル"""
        self._cancelled = True
        self.requestInterruption()
