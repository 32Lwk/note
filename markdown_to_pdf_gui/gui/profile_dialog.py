"""プロファイル管理ダイアログ: プロファイルの作成、編集、インポート/エクスポート"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QListWidget,
    QPushButton, QLineEdit, QMessageBox, QFileDialog
)
from PyQt6.QtCore import Qt
from pathlib import Path
from typing import Optional
from ..core.config_manager import ConfigManager


class ProfileDialog(QDialog):
    """プロファイル管理ダイアログクラス"""
    
    def __init__(self, config_manager: ConfigManager, parent=None):
        super().__init__(parent)
        self.config_manager = config_manager
        self.setWindowTitle("プロファイル管理")
        self.setMinimumWidth(500)
        self.setMinimumHeight(400)
        
        self.setup_ui()
        self.refresh_profile_list()
    
    def setup_ui(self) -> None:
        """UIを構築"""
        layout = QVBoxLayout(self)
        
        # プロファイルリスト
        self.profile_list = QListWidget()
        self.profile_list.itemDoubleClicked.connect(self.load_profile)
        layout.addWidget(self.profile_list)
        
        # プロファイル名入力
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("プロファイル名:"))
        self.name_edit = QLineEdit()
        name_layout.addWidget(self.name_edit)
        layout.addLayout(name_layout)
        
        # ボタンエリア
        button_layout = QHBoxLayout()
        
        self.load_button = QPushButton("読み込み")
        self.load_button.clicked.connect(self.load_selected_profile)
        button_layout.addWidget(self.load_button)
        
        self.save_button = QPushButton("保存")
        self.save_button.clicked.connect(self.save_current_as_profile)
        button_layout.addWidget(self.save_button)
        
        self.delete_button = QPushButton("削除")
        self.delete_button.clicked.connect(self.delete_selected_profile)
        button_layout.addWidget(self.delete_button)
        
        button_layout.addStretch()
        
        self.export_button = QPushButton("エクスポート")
        self.export_button.clicked.connect(self.export_profile)
        button_layout.addWidget(self.export_button)
        
        self.import_button = QPushButton("インポート")
        self.import_button.clicked.connect(self.import_profile)
        button_layout.addWidget(self.import_button)
        
        layout.addLayout(button_layout)
        
        # 閉じるボタン
        close_layout = QHBoxLayout()
        close_layout.addStretch()
        self.close_button = QPushButton("閉じる")
        self.close_button.clicked.connect(self.accept)
        close_layout.addWidget(self.close_button)
        layout.addLayout(close_layout)
    
    def refresh_profile_list(self) -> None:
        """プロファイルリストを更新"""
        self.profile_list.clear()
        profiles = self.config_manager.list_profiles()
        for profile in profiles:
            self.profile_list.addItem(profile)
    
    def load_selected_profile(self) -> None:
        """選択されたプロファイルを読み込み"""
        current_item = self.profile_list.currentItem()
        if current_item:
            profile_name = current_item.text()
            if self.config_manager.load_profile(profile_name):
                QMessageBox.information(self, "成功", f"プロファイル '{profile_name}' を読み込みました")
                self.accept()
            else:
                QMessageBox.warning(self, "エラー", f"プロファイル '{profile_name}' の読み込みに失敗しました")
    
    def load_profile(self, item) -> None:
        """プロファイルを読み込み（ダブルクリック時）"""
        profile_name = item.text()
        if self.config_manager.load_profile(profile_name):
            self.accept()
    
    def save_current_as_profile(self) -> None:
        """現在の設定をプロファイルとして保存"""
        profile_name = self.name_edit.text().strip()
        if not profile_name:
            QMessageBox.warning(self, "エラー", "プロファイル名を入力してください")
            return
        
        if self.config_manager.save_profile(profile_name):
            QMessageBox.information(self, "成功", f"プロファイル '{profile_name}' を保存しました")
            self.refresh_profile_list()
            self.name_edit.clear()
        else:
            QMessageBox.warning(self, "エラー", "プロファイルの保存に失敗しました")
    
    def delete_selected_profile(self) -> None:
        """選択されたプロファイルを削除"""
        current_item = self.profile_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, "警告", "削除するプロファイルを選択してください")
            return
        
        profile_name = current_item.text()
        reply = QMessageBox.question(
            self,
            "確認",
            f"プロファイル '{profile_name}' を削除しますか？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            profile_file = self.config_manager.profiles_dir / f"{profile_name}.json"
            if profile_file.exists():
                profile_file.unlink()
                QMessageBox.information(self, "成功", f"プロファイル '{profile_name}' を削除しました")
                self.refresh_profile_list()
    
    def export_profile(self) -> None:
        """プロファイルをエクスポート"""
        current_item = self.profile_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, "警告", "エクスポートするプロファイルを選択してください")
            return
        
        profile_name = current_item.text()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "プロファイルをエクスポート",
            f"{profile_name}.json",
            "JSON Files (*.json);;All Files (*)"
        )
        
        if file_path:
            profile_file = self.config_manager.profiles_dir / f"{profile_name}.json"
            if profile_file.exists():
                import shutil
                shutil.copy2(profile_file, file_path)
                QMessageBox.information(self, "成功", f"プロファイルをエクスポートしました: {file_path}")
            else:
                QMessageBox.warning(self, "エラー", "プロファイルファイルが見つかりません")
    
    def import_profile(self) -> None:
        """プロファイルをインポート"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "プロファイルをインポート",
            str(Path.home()),
            "JSON Files (*.json);;All Files (*)"
        )
        
        if file_path:
            import shutil
            import json
            
            try:
                # ファイルを読み込んで検証
                with open(file_path, 'r', encoding='utf-8') as f:
                    profile_data = json.load(f)
                
                profile_name = profile_data.get('profile_name', Path(file_path).stem)
                
                # プロファイルとして保存
                target_file = self.config_manager.profiles_dir / f"{profile_name}.json"
                shutil.copy2(file_path, target_file)
                
                QMessageBox.information(self, "成功", f"プロファイル '{profile_name}' をインポートしました")
                self.refresh_profile_list()
            
            except Exception as e:
                QMessageBox.warning(self, "エラー", f"プロファイルのインポートに失敗しました: {str(e)}")
