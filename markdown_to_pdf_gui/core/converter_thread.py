"""非同期変換エンジン: QThreadを使用した非同期処理"""

from enum import Enum
from pathlib import Path
from typing import Dict, Optional, List, Tuple
import time
from PyQt6.QtCore import QThread, pyqtSignal
from .converter import Converter
from .error_handler import ErrorHandler, ErrorType, ErrorCategory
from .markdown_validator import MarkdownValidator
from .performance_monitor import PerformanceMonitor
from .emoji_converter import EmojiConverter
from .image_processor import ImageProcessor
from .figure_generator import FigureGenerator
from .pdf_validator import PDFValidator
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
        self.performance_monitor = PerformanceMonitor()
        self.emoji_converter = EmojiConverter()
        self.image_processor = ImageProcessor()
        self.figure_generator = FigureGenerator()
        self.pdf_validator = PDFValidator()
        self.state = ConversionState.IDLE
        self._cancelled = False
        self.conversion_durations: Dict[Path, float] = {}
    
    def run(self) -> None:
        """変換処理を実行"""
        try:
            total_files = len(self.md_files)
            overall_start_time = time.time()
            
            for idx, md_file in enumerate(self.md_files):
                if self.isInterruptionRequested() or self._cancelled:
                    self.state = ConversionState.CANCELLED
                    self.state_changed.emit(self.state.value, 0.0)
                    return
                
                # パフォーマンス監視開始
                self.performance_monitor.start_conversion(md_file)
                
                # 前処理
                self.state = ConversionState.PREPROCESSING
                progress = (idx / total_files) * 100
                self.state_changed.emit(self.state.value, progress)
                
                # 残り時間推定
                elapsed = time.time() - overall_start_time
                remaining = self.performance_monitor.estimate_remaining_time(idx, total_files, elapsed)
                if remaining:
                    remaining_str = f"（残り約{remaining/60:.1f}分）"
                else:
                    remaining_str = ""
                
                self.progress_updated.emit(int(progress), f"前処理中: {md_file.name}{remaining_str}")
                
                # 図生成スクリプトの実行（オプション）
                if self.config.get("auto_generate_figures", False):
                    executed, figure_warnings = self.figure_generator.process_markdown_file(
                        md_file, auto_execute=True
                    )
                    for warning in figure_warnings:
                        self.progress_updated.emit(int(progress), f"警告: {warning}")
                
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
                
                # 絵文字変換（オプション）
                if self.config.get("emoji_conversion", True) and validation_result.has_emoji:
                    # マークダウンファイルの内容を読み込んで変換
                    try:
                        with open(md_file, 'r', encoding=validation_result.encoding or 'utf-8') as f:
                            content = f.read()
                        converted_content, converted_emojis = self.emoji_converter.convert(content)
                        # 変換後の内容を一時ファイルに保存（実際の実装では前処理として統合）
                    except Exception:
                        pass  # エラー時はスキップ
                
                # 画像処理（SVG変換など）
                if validation_result.image_paths:
                    processed_images, image_warnings = self.image_processor.process_images(
                        md_file, validation_result.image_paths,
                        convert_svg=self.config.get("svg_to_png", True)
                    )
                    for warning in image_warnings:
                        self.progress_updated.emit(int(progress), f"警告: {warning}")
                
                # 画像処理（SVG変換など）
                if validation_result.image_paths:
                    processed_images, image_warnings = self.image_processor.process_images(
                        md_file, validation_result.image_paths,
                        convert_svg=self.config.get("svg_to_png", True)
                    )
                    for warning in image_warnings:
                        self.progress_updated.emit(int(progress), f"警告: {warning}")
                
                # 変換
                self.state = ConversionState.CONVERTING
                progress = ((idx + 0.5) / total_files) * 100
                self.state_changed.emit(self.state.value, progress)
                
                # メモリ監視
                self.performance_monitor.update_memory()
                memory_ok, memory_msg = self.performance_monitor.check_memory_limit()
                if not memory_ok:
                    self.error_occurred.emit("WARNING", "PERFORMANCE", memory_msg)
                
                self.progress_updated.emit(int(progress), f"変換中: {md_file.name}")
                
                conversion_start_time = time.time()
                success, output_file, error_msg = self.converter.convert(
                    md_file,
                    self.output_dir,
                    self.config,
                    self.template_path,
                    self.header_path
                )
                conversion_duration = time.time() - conversion_start_time
                self.conversion_durations[md_file] = conversion_duration
                
                # 後処理
                self.state = ConversionState.POSTPROCESSING
                progress = ((idx + 0.9) / total_files) * 100
                self.state_changed.emit(self.state.value, progress)
                self.progress_updated.emit(int(progress), f"後処理中: {md_file.name}")
                
                if success and output_file:
                    # PDF検証
                    pdf_result = self.pdf_validator.validate(output_file)
                    if pdf_result.is_valid:
                        # メタデータの設定
                        title = md_file.stem
                        self.pdf_validator.set_metadata(output_file, title=title)
                        
                        # パフォーマンス統計
                        perf_stats = self.performance_monitor.end_conversion()
                        actual_duration = self.conversion_durations.get(md_file, 0.0)
                        if actual_duration == 0.0:
                            actual_duration = perf_stats.get('duration', 0.0)
                        
                        self.file_completed.emit(str(md_file), True, f"完了: {output_file.name} ({actual_duration:.1f}秒)")
                        if self.logger:
                            self.logger.log_conversion(
                                str(md_file),
                                True,
                                None,
                                f"出力: {output_file}",
                                {
                                    "output_file": str(output_file),
                                    "duration": perf_stats['duration'],
                                    "memory_used": perf_stats['memory_used'],
                                }
                            )
                    else:
                        error_msg = "; ".join(pdf_result.errors)
                        self.file_completed.emit(str(md_file), False, f"PDF検証エラー: {error_msg}")
                else:
                    actual_duration = self.conversion_durations.get(md_file, 0.0)
                    self.file_completed.emit(str(md_file), False, error_msg or "変換に失敗しました")
                    if self.logger:
                        self.logger.log_conversion(
                            str(md_file),
                            False,
                            "CONVERSION_ERROR",
                            error_msg or "変換に失敗しました",
                            {"duration": actual_duration}
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
