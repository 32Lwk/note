"""メインウィンドウ: PyQt6のメインウィンドウ実装"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QProgressBar, QTextEdit, QListWidget,
    QMessageBox, QFileDialog, QMenuBar, QMenu
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QShortcut, QKeySequence, QAction
from PyQt6.QtGui import QDragEnterEvent, QDropEvent
from pathlib import Path
from typing import List, Optional
from ..core.environment_checker import EnvironmentChecker
from ..core.converter_thread import ConverterThread
from ..core.error_handler import ErrorHandler
from ..core.config_manager import ConfigManager
from ..core.template_manager import TemplateManager
from ..utils.logger import StructuredLogger
from .settings_dialog import SettingsDialog
from .profile_dialog import ProfileDialog
from .history_dialog import HistoryDialog
from .log_viewer import LogViewer
from ..core.history_manager import HistoryManager


class MainWindow(QMainWindow):
    """メインウィンドウクラス"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markdown to PDF Converter")
        self.setMinimumSize(800, 600)
        
        # コンポーネントの初期化
        self.logger = StructuredLogger()
        self.error_handler = ErrorHandler()
        self.config_manager = ConfigManager()
        self.template_manager = TemplateManager()
        self.history_manager = HistoryManager()
        self.converter_thread: Optional[ConverterThread] = None
        self.selected_files: List[Path] = []
        
        # 設定の読み込み
        self.config_manager.load_config()
        
        # 環境チェック
        self.check_environment()
        
        # UIの構築
        self.setup_ui()
        
        # メニューバーの設定
        self.setup_menu()
        
        # キーボードショートカットの設定
        self.setup_shortcuts()
    
    def setup_shortcuts(self) -> None:
        """キーボードショートカットを設定"""
        # Cmd+O: ファイルを開く
        QShortcut(QKeySequence("Ctrl+O"), self, self.select_files)
        
        # Cmd+,: 設定ダイアログ
        QShortcut(QKeySequence("Ctrl+,"), self, self.show_settings)
        
        # Cmd+R: 変換開始
        QShortcut(QKeySequence("Ctrl+R"), self, self.start_conversion)
        
        # Cmd+H: 履歴
        QShortcut(QKeySequence("Ctrl+H"), self, self.show_history)
    
    def check_environment(self) -> None:
        """環境チェックを実行"""
        checker = EnvironmentChecker()
        success, errors, warnings = checker.check_all()
        
        if not success:
            msg = "環境チェックに失敗しました:\n\n" + "\n".join(errors)
            if warnings:
                msg += "\n\n警告:\n" + "\n".join(warnings)
            msg += "\n\n" + checker.get_installation_instructions()
            
            QMessageBox.critical(self, "環境エラー", msg)
    
    def setup_ui(self) -> None:
        """UIを構築"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # スタイルシートでUIを改善
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QPushButton {
                background-color: #007AFF;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0051D5;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
            QListWidget {
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: white;
            }
            QTextEdit {
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: white;
                font-family: 'Monaco', 'Menlo', monospace;
            }
            QProgressBar {
                border: 1px solid #ddd;
                border-radius: 4px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #007AFF;
                border-radius: 3px;
            }
        """)
        
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # ファイル選択エリア
        file_area = self.create_file_selection_area()
        layout.addWidget(file_area)
        
        # 選択ファイルリスト
        self.file_list = QListWidget()
        self.file_list.setMaximumHeight(150)
        layout.addWidget(QLabel("選択ファイル:"))
        layout.addWidget(self.file_list)
        
        # ボタンエリア
        button_area = self.create_button_area()
        layout.addWidget(button_area)
        
        # 進捗バー
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        
        # ログ表示エリア
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(200)
        layout.addWidget(QLabel("ログ:"))
        layout.addWidget(self.log_text)
    
    def create_file_selection_area(self) -> QWidget:
        """ファイル選択エリアを作成"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        label = QLabel("マークダウンファイルをドラッグ&ドロップするか、\nファイルを選択してください")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border: 2px dashed #ccc; padding: 20px;")
        label.setAcceptDrops(True)
        label.dragEnterEvent = self.drag_enter_event
        label.dropEvent = self.drop_event
        
        layout.addWidget(label)
        
        return widget
    
    def create_button_area(self) -> QWidget:
        """ボタンエリアを作成"""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        
        self.select_button = QPushButton("ファイルを選択")
        self.select_button.clicked.connect(self.select_files)
        layout.addWidget(self.select_button)
        
        self.settings_button = QPushButton("設定")
        self.settings_button.clicked.connect(self.show_settings)
        layout.addWidget(self.settings_button)
        
        self.history_button = QPushButton("履歴")
        self.history_button.clicked.connect(self.show_history)
        layout.addWidget(self.history_button)
        
        self.convert_button = QPushButton("変換開始")
        self.convert_button.clicked.connect(self.start_conversion)
        self.convert_button.setEnabled(False)
        layout.addWidget(self.convert_button)
        
        self.cancel_button = QPushButton("キャンセル")
        self.cancel_button.clicked.connect(self.cancel_conversion)
        self.cancel_button.setEnabled(False)
        layout.addWidget(self.cancel_button)
        
        layout.addStretch()
        
        return widget
    
    def setup_menu(self) -> None:
        """メニューバーを設定"""
        menubar = self.menuBar()
        
        # ファイルメニュー
        file_menu = menubar.addMenu("ファイル")
        
        # PyQt6では、QActionを作成してから追加する必要がある
        open_action = QAction("ファイルを開く", self)
        open_action.setShortcut(QKeySequence("Ctrl+O"))
        open_action.triggered.connect(self.select_files)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("終了", self)
        exit_action.setShortcut(QKeySequence("Ctrl+Q"))
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 設定メニュー
        settings_menu = menubar.addMenu("設定")
        settings_action = QAction("設定...", self)
        settings_action.setShortcut(QKeySequence("Ctrl+,"))
        settings_action.triggered.connect(self.show_settings)
        settings_menu.addAction(settings_action)
        settings_menu.addAction("プロファイル管理...", self.show_profile_dialog)
        
        # 履歴メニュー
        history_menu = menubar.addMenu("履歴")
        history_action = QAction("変換履歴...", self)
        history_action.setShortcut(QKeySequence("Ctrl+H"))
        history_action.triggered.connect(self.show_history)
        history_menu.addAction(history_action)
        
        # ヘルプメニュー
        help_menu = menubar.addMenu("ヘルプ")
        help_menu.addAction("バージョン情報", self.show_version)
        help_menu.addAction("環境チェック", self.check_environment)
        help_menu.addAction("ログビューアー", self.show_log_viewer)
    
    def drag_enter_event(self, event: QDragEnterEvent) -> None:
        """ドラッグエンターイベント"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def drop_event(self, event: QDropEvent) -> None:
        """ドロップイベント"""
        files = []
        for url in event.mimeData().urls():
            file_path = Path(url.toLocalFile())
            if file_path.is_file() and file_path.suffix == '.md':
                files.append(file_path)
            elif file_path.is_dir():
                # ディレクトリの場合は配下の.mdファイルを検索
                files.extend(file_path.rglob('*.md'))
        
        if files:
            self.add_files(files)
    
    def select_files(self) -> None:
        """ファイル選択ダイアログを表示"""
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "マークダウンファイルを選択",
            str(Path.home()),
            "Markdown Files (*.md);;All Files (*)"
        )
        
        if files:
            self.add_files([Path(f) for f in files])
    
    def add_files(self, files: List[Path]) -> None:
        """ファイルを追加"""
        for file_path in files:
            if file_path not in self.selected_files:
                self.selected_files.append(file_path)
                self.file_list.addItem(str(file_path))
        
        self.convert_button.setEnabled(len(self.selected_files) > 0)
        self.log_message(f"{len(files)}個のファイルを追加しました")
    
    def start_conversion(self) -> None:
        """変換を開始"""
        if not self.selected_files:
            QMessageBox.warning(self, "警告", "変換するファイルを選択してください")
            return
        
        # ボタンの状態を更新
        self.convert_button.setEnabled(False)
        self.cancel_button.setEnabled(True)
        self.select_button.setEnabled(False)
        
        # 進捗バーをリセット
        self.progress_bar.setValue(0)
        self.log_text.clear()
        
        # テンプレートの検出（最初のファイルから）
        template_path, header_path = None, None
        if self.selected_files:
            template_path, header_path = self.template_manager.find_templates(
                self.selected_files[0]
            )
        
        # 設定を取得
        config = self.config_manager.get_config()
        
        # 変換スレッドを作成
        self.converter_thread = ConverterThread(
            self.selected_files,
            config=config,
            template_path=template_path,
            header_path=header_path,
            logger=self.logger
        )
        
        # シグナル接続
        self.converter_thread.progress_updated.connect(self.on_progress_updated)
        self.converter_thread.file_completed.connect(self.on_file_completed)
        self.converter_thread.error_occurred.connect(self.on_error_occurred)
        self.converter_thread.finished.connect(self.on_conversion_finished)
        
        # 変換開始
        self.converter_thread.start()
        self.log_message("変換を開始しました...")
    
    def cancel_conversion(self) -> None:
        """変換をキャンセル"""
        if self.converter_thread and self.converter_thread.isRunning():
            self.converter_thread.cancel()
            self.converter_thread.wait()
            self.log_message("変換をキャンセルしました")
            self.on_conversion_finished()
    
    def on_progress_updated(self, progress: int, message: str) -> None:
        """進捗更新"""
        self.progress_bar.setValue(progress)
        self.log_message(message)
    
    def on_file_completed(self, file_path: str, success: bool, message: str) -> None:
        """ファイル変換完了"""
        status = "✓" if success else "✗"
        self.log_message(f"{status} {Path(file_path).name}: {message}")
        
        # 履歴に記録（変換時間はメッセージから抽出を試みる）
        md_file = Path(file_path)
        pdf_file = md_file.parent / f"{md_file.stem}.pdf"
        
        # メッセージから時間を抽出（例: "完了: file.pdf (5.2秒)"）
        import re
        duration_match = re.search(r'\(([\d.]+)秒\)', message)
        duration = float(duration_match.group(1)) if duration_match else 0.0
        
        config = self.config_manager.get_config()
        profile_name = config.get('profile_name')
        error_type = None if success else "CONVERSION_ERROR"
        error_message = None if success else message
        
        self.history_manager.add_history(
            md_file, pdf_file, success, duration,
            profile_name, error_type, error_message
        )
    
    def on_error_occurred(self, error_type: str, category: str, message: str) -> None:
        """エラー発生"""
        self.log_message(f"エラー [{error_type}]: {message}")
        if error_type == "FATAL":
            QMessageBox.critical(self, "致命的エラー", message)
    
    def on_conversion_finished(self) -> None:
        """変換完了"""
        self.convert_button.setEnabled(True)
        self.cancel_button.setEnabled(False)
        self.select_button.setEnabled(True)
        self.progress_bar.setValue(100)
        self.log_message("すべての変換が完了しました")
    
    def log_message(self, message: str) -> None:
        """ログメッセージを追加"""
        self.log_text.append(f"> {message}")
        # 自動スクロール
        scrollbar = self.log_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def show_settings(self) -> None:
        """設定ダイアログを表示"""
        dialog = SettingsDialog(self.config_manager, self)
        if dialog.exec():
            # 設定が保存された場合、再読み込み
            self.config_manager.load_config()
    
    def show_profile_dialog(self) -> None:
        """プロファイル管理ダイアログを表示"""
        dialog = ProfileDialog(self.config_manager, self)
        dialog.exec()
    
    def show_history(self) -> None:
        """変換履歴ダイアログを表示"""
        dialog = HistoryDialog(self.history_manager, self)
        dialog.exec()
    
    def show_log_viewer(self) -> None:
        """ログビューアーを表示"""
        log_dir = Path.home() / "Library" / "Application Support" / "MarkdownToPDF" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        dialog = LogViewer(log_dir, self)
        dialog.exec()
    
    def show_version(self) -> None:
        """バージョン情報を表示"""
        from markdown_to_pdf_gui import __version__
        QMessageBox.information(
            self,
            "バージョン情報",
            f"Markdown to PDF GUI Tool\nバージョン {__version__}"
        )
