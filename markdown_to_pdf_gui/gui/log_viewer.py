"""ログビューアー: GUI内ログビューアー（検索・フィルタ）"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTextEdit,
    QPushButton, QLineEdit, QComboBox, QLabel, QFileDialog
)
from PyQt6.QtCore import Qt
from pathlib import Path
from typing import List, Optional, Dict
import json
import re


class LogViewer(QDialog):
    """ログビューアーダイアログクラス"""
    
    def __init__(self, log_dir: Path, parent=None):
        super().__init__(parent)
        self.log_dir = log_dir
        self.setWindowTitle("ログビューアー")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        
        self.setup_ui()
        self.load_logs()
    
    def setup_ui(self) -> None:
        """UIを構築"""
        layout = QVBoxLayout(self)
        
        # 検索・フィルタエリア
        filter_layout = QHBoxLayout()
        
        filter_layout.addWidget(QLabel("検索:"))
        self.search_edit = QLineEdit()
        self.search_edit.textChanged.connect(self.filter_logs)
        filter_layout.addWidget(self.search_edit)
        
        filter_layout.addWidget(QLabel("レベル:"))
        self.level_combo = QComboBox()
        self.level_combo.addItems(["すべて", "ERROR", "WARNING", "INFO", "DEBUG"])
        self.level_combo.currentIndexChanged.connect(self.filter_logs)
        filter_layout.addWidget(self.level_combo)
        
        layout.addLayout(filter_layout)
        
        # ログ表示エリア
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setFontFamily("Monaco")
        self.log_text.setFontPointSize(10)
        layout.addWidget(self.log_text)
        
        # ボタン
        button_layout = QHBoxLayout()
        
        self.refresh_button = QPushButton("更新")
        self.refresh_button.clicked.connect(self.load_logs)
        button_layout.addWidget(self.refresh_button)
        
        self.export_button = QPushButton("エクスポート")
        self.export_button.clicked.connect(self.export_logs)
        button_layout.addWidget(self.export_button)
        
        button_layout.addStretch()
        
        self.close_button = QPushButton("閉じる")
        self.close_button.clicked.connect(self.accept)
        button_layout.addWidget(self.close_button)
        
        layout.addLayout(button_layout)
    
    def load_logs(self) -> None:
        """ログを読み込み"""
        self.all_logs = []
        
        # アプリケーションログ
        app_log = self.log_dir / "app.log"
        if app_log.exists():
            self.load_text_log(app_log, "APP")
        
        # エラーログ
        error_log = self.log_dir / "errors.log"
        if error_log.exists():
            self.load_text_log(error_log, "ERROR")
        
        # 変換ログ（最新の10個）
        conversion_logs = sorted(
            self.log_dir.glob("conversion_log_*.txt"),
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )[:10]
        
        for log_file in conversion_logs:
            self.load_text_log(log_file, "CONVERSION")
        
        self.filter_logs()
    
    def load_text_log(self, log_file: Path, log_type: str) -> None:
        """テキストログを読み込み"""
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    self.all_logs.append({
                        'type': log_type,
                        'content': line.strip(),
                        'file': log_file.name
                    })
        except Exception:
            pass
    
    def load_json_log(self, log_file: Path) -> None:
        """JSON形式のログを読み込み"""
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        try:
                            log_entry = json.loads(line)
                            self.all_logs.append({
                                'type': log_entry.get('category', 'GENERAL'),
                                'level': log_entry.get('level', 'INFO'),
                                'content': self.format_json_log(log_entry),
                                'file': log_file.name
                            })
                        except json.JSONDecodeError:
                            pass
        except Exception:
            pass
    
    def format_json_log(self, log_entry: Dict) -> str:
        """JSONログエントリをフォーマット"""
        timestamp = log_entry.get('timestamp', '')
        level = log_entry.get('level', 'INFO')
        category = log_entry.get('category', 'GENERAL')
        message = log_entry.get('message', '')
        
        return f"[{timestamp}] [{level}] [{category}] {message}"
    
    def filter_logs(self) -> None:
        """ログをフィルタ"""
        search_query = self.search_edit.text().lower()
        level_filter = self.level_combo.currentText()
        
        filtered_logs = []
        for log in self.all_logs:
            # レベルフィルタ
            if level_filter != "すべて":
                log_level = log.get('level', 'INFO')
                if log_level != level_filter:
                    continue
            
            # 検索クエリ
            if search_query:
                if search_query not in log['content'].lower():
                    continue
            
            filtered_logs.append(log)
        
        # 表示
        self.log_text.clear()
        for log in filtered_logs[-1000:]:  # 最新1000件まで
            color = self.get_log_color(log.get('level', 'INFO'))
            self.log_text.append(f"<span style='color: {color};'>{log['content']}</span>")
        
        # 自動スクロール
        scrollbar = self.log_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def get_log_color(self, level: str) -> str:
        """ログレベルの色を取得"""
        colors = {
            'ERROR': 'red',
            'WARNING': 'orange',
            'INFO': 'black',
            'DEBUG': 'gray',
        }
        return colors.get(level, 'black')
    
    def export_logs(self) -> None:
        """ログをエクスポート"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "ログをエクスポート",
            str(Path.home() / "logs_export.txt"),
            "Text Files (*.txt);;All Files (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    for log in self.all_logs:
                        f.write(f"{log['content']}\n")
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.information(self, "成功", f"ログをエクスポートしました: {file_path}")
            except Exception as e:
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "エラー", f"エクスポートに失敗しました: {str(e)}")
