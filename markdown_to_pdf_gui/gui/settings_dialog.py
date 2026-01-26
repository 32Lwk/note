"""設定ダイアログ: 設定の編集UI"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QPushButton, QLineEdit, QSpinBox, QCheckBox, QComboBox,
    QLabel, QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt
from pathlib import Path
from typing import Optional
from ..core.config_manager import ConfigManager


class SettingsDialog(QDialog):
    """設定ダイアログクラス"""
    
    def __init__(self, config_manager: ConfigManager, parent=None):
        super().__init__(parent)
        self.config_manager = config_manager
        self.setWindowTitle("設定")
        self.setMinimumWidth(500)
        
        self.setup_ui()
        self.load_settings()
    
    def setup_ui(self) -> None:
        """UIを構築"""
        layout = QVBoxLayout(self)
        
        form_layout = QFormLayout()
        
        # PDFエンジン
        self.pdf_engine_combo = QComboBox()
        self.pdf_engine_combo.addItems(["xelatex", "pdflatex", "lualatex"])
        form_layout.addRow("PDFエンジン:", self.pdf_engine_combo)
        
        # フォント
        self.mainfont_edit = QLineEdit()
        form_layout.addRow("メインフォント:", self.mainfont_edit)
        
        self.cjk_font_edit = QLineEdit()
        form_layout.addRow("CJKフォント:", self.cjk_font_edit)
        
        # マージン
        self.margin_edit = QLineEdit()
        form_layout.addRow("マージン:", self.margin_edit)
        
        # フォントサイズ
        self.fontsize_edit = QLineEdit()
        form_layout.addRow("フォントサイズ:", self.fontsize_edit)
        
        # 目次
        self.toc_checkbox = QCheckBox()
        form_layout.addRow("目次を生成:", self.toc_checkbox)
        
        # 目次深度
        self.toc_depth_spin = QSpinBox()
        self.toc_depth_spin.setRange(1, 6)
        form_layout.addRow("目次深度:", self.toc_depth_spin)
        
        # セクション番号
        self.number_sections_checkbox = QCheckBox()
        form_layout.addRow("セクション番号を付ける:", self.number_sections_checkbox)
        
        # ハイパーリンク
        self.colorlinks_checkbox = QCheckBox()
        form_layout.addRow("ハイパーリンクを有効化:", self.colorlinks_checkbox)
        
        # リンク色
        self.linkcolor_edit = QLineEdit()
        form_layout.addRow("リンク色:", self.linkcolor_edit)
        
        layout.addLayout(form_layout)
        
        # ボタン
        button_layout = QHBoxLayout()
        
        self.reset_button = QPushButton("リセット")
        self.reset_button.clicked.connect(self.reset_settings)
        button_layout.addWidget(self.reset_button)
        
        button_layout.addStretch()
        
        self.cancel_button = QPushButton("キャンセル")
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_button)
        
        self.save_button = QPushButton("保存")
        self.save_button.clicked.connect(self.save_settings)
        button_layout.addWidget(self.save_button)
        
        layout.addLayout(button_layout)
    
    def load_settings(self) -> None:
        """設定を読み込み"""
        config = self.config_manager.get_config()
        
        self.pdf_engine_combo.setCurrentText(config.get("pdf_engine", "xelatex"))
        self.mainfont_edit.setText(config.get("mainfont", "Hiragino Sans"))
        self.cjk_font_edit.setText(config.get("cjk_mainfont", "Hiragino Sans"))
        
        geometry = config.get("geometry", "margin=2.5cm")
        if "margin=" in geometry:
            margin = geometry.split("margin=")[1].split(",")[0]
            self.margin_edit.setText(margin)
        else:
            self.margin_edit.setText("2.5cm")
        
        self.fontsize_edit.setText(config.get("fontsize", "10pt"))
        self.toc_checkbox.setChecked(config.get("toc", True))
        self.toc_depth_spin.setValue(config.get("toc_depth", 2))
        self.number_sections_checkbox.setChecked(config.get("number_sections", False))
        self.colorlinks_checkbox.setChecked(config.get("colorlinks", True))
        self.linkcolor_edit.setText(config.get("linkcolor", "blue"))
    
    def save_settings(self) -> None:
        """設定を保存"""
        updates = {
            "pdf_engine": self.pdf_engine_combo.currentText(),
            "mainfont": self.mainfont_edit.text(),
            "cjk_mainfont": self.cjk_font_edit.text(),
            "geometry": f"margin={self.margin_edit.text()}",
            "fontsize": self.fontsize_edit.text(),
            "toc": self.toc_checkbox.isChecked(),
            "toc_depth": self.toc_depth_spin.value(),
            "number_sections": self.number_sections_checkbox.isChecked(),
            "colorlinks": self.colorlinks_checkbox.isChecked(),
            "linkcolor": self.linkcolor_edit.text(),
        }
        
        if self.config_manager.update_config(updates):
            if self.config_manager.save_config():
                QMessageBox.information(self, "設定", "設定を保存しました")
                self.accept()
            else:
                QMessageBox.warning(self, "エラー", "設定の保存に失敗しました")
        else:
            QMessageBox.warning(self, "エラー", "設定が無効です")
    
    def reset_settings(self) -> None:
        """設定をリセット"""
        reply = QMessageBox.question(
            self,
            "確認",
            "設定をデフォルトにリセットしますか？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.config_manager.load_default_config()
            self.load_settings()
