"""変換履歴ダイアログ: 履歴の表示、検索、フィルタ"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QLineEdit, QComboBox, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt
from pathlib import Path
from datetime import datetime
from ..core.history_manager import HistoryManager


class HistoryDialog(QDialog):
    """変換履歴ダイアログクラス"""
    
    def __init__(self, history_manager: HistoryManager, parent=None):
        super().__init__(parent)
        self.history_manager = history_manager
        self.setWindowTitle("変換履歴")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        
        self.setup_ui()
        self.refresh_history()
    
    def setup_ui(self) -> None:
        """UIを構築"""
        layout = QVBoxLayout(self)
        
        # 検索・フィルタエリア
        filter_layout = QHBoxLayout()
        
        filter_layout.addWidget(QLabel("検索:"))
        self.search_edit = QLineEdit()
        self.search_edit.textChanged.connect(self.on_search_changed)
        filter_layout.addWidget(self.search_edit)
        
        filter_layout.addWidget(QLabel("フィルタ:"))
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["すべて", "成功のみ", "失敗のみ"])
        self.filter_combo.currentIndexChanged.connect(self.on_filter_changed)
        filter_layout.addWidget(self.filter_combo)
        
        layout.addLayout(filter_layout)
        
        # 履歴テーブル
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(7)
        self.history_table.setHorizontalHeaderLabels([
            "日時", "ファイル", "PDF", "状態", "時間", "サイズ", "プロファイル"
        ])
        self.history_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        layout.addWidget(self.history_table)
        
        # 統計情報
        stats_layout = QHBoxLayout()
        self.stats_label = QLabel()
        stats_layout.addWidget(self.stats_label)
        stats_layout.addStretch()
        layout.addLayout(stats_layout)
        
        # ボタン
        button_layout = QHBoxLayout()
        
        self.refresh_button = QPushButton("更新")
        self.refresh_button.clicked.connect(self.refresh_history)
        button_layout.addWidget(self.refresh_button)
        
        self.clear_button = QPushButton("履歴をクリア")
        self.clear_button.clicked.connect(self.clear_history)
        button_layout.addWidget(self.clear_button)
        
        button_layout.addStretch()
        
        self.close_button = QPushButton("閉じる")
        self.close_button.clicked.connect(self.accept)
        button_layout.addWidget(self.close_button)
        
        layout.addLayout(button_layout)
    
    def refresh_history(self) -> None:
        """履歴を更新"""
        # フィルタを適用
        success_only = None
        if self.filter_combo.currentText() == "成功のみ":
            success_only = True
        elif self.filter_combo.currentText() == "失敗のみ":
            success_only = False
        
        # 検索クエリ
        query = self.search_edit.text().strip()
        
        if query:
            history = self.history_manager.search_history(query)
        else:
            history = self.history_manager.get_history(limit=100, success_only=success_only)
        
        # テーブルに表示
        self.history_table.setRowCount(len(history))
        for row, entry in enumerate(history):
            # 日時
            timestamp = datetime.fromisoformat(entry.timestamp)
            self.history_table.setItem(row, 0, QTableWidgetItem(timestamp.strftime("%Y-%m-%d %H:%M:%S")))
            
            # ファイル名
            md_name = Path(entry.md_file).name
            self.history_table.setItem(row, 1, QTableWidgetItem(md_name))
            
            # PDFファイル名
            pdf_name = Path(entry.pdf_file).name if entry.success else "-"
            self.history_table.setItem(row, 2, QTableWidgetItem(pdf_name))
            
            # 状態
            status = "✓ 成功" if entry.success else f"✗ 失敗 ({entry.error_type or 'エラー'})"
            status_item = QTableWidgetItem(status)
            if not entry.success:
                status_item.setForeground(Qt.GlobalColor.red)
            self.history_table.setItem(row, 3, status_item)
            
            # 時間
            duration_str = f"{entry.duration:.1f}秒"
            self.history_table.setItem(row, 4, QTableWidgetItem(duration_str))
            
            # サイズ
            size_str = f"{entry.file_size_before / 1024:.1f}KB → {entry.file_size_after / 1024:.1f}KB"
            self.history_table.setItem(row, 5, QTableWidgetItem(size_str))
            
            # プロファイル
            profile = entry.profile_name or "デフォルト"
            self.history_table.setItem(row, 6, QTableWidgetItem(profile))
        
        # 列幅を調整
        self.history_table.resizeColumnsToContents()
        
        # 統計情報を更新
        stats = self.history_manager.get_statistics()
        stats_text = (
            f"総変換回数: {stats['total_conversions']} | "
            f"成功: {stats['successful']} | "
            f"失敗: {stats['failed']} | "
            f"成功率: {stats['success_rate']*100:.1f}% | "
            f"平均時間: {stats['average_duration']:.1f}秒"
        )
        self.stats_label.setText(stats_text)
    
    def on_search_changed(self) -> None:
        """検索クエリが変更されたとき"""
        self.refresh_history()
    
    def on_filter_changed(self) -> None:
        """フィルタが変更されたとき"""
        self.refresh_history()
    
    def clear_history(self) -> None:
        """履歴をクリア"""
        reply = QMessageBox.question(
            self,
            "確認",
            "すべての履歴を削除しますか？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.history_manager.clear_history()
            self.refresh_history()
            QMessageBox.information(self, "完了", "履歴をクリアしました")
