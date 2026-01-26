"""ConfigManagerのテスト"""

import pytest
import json
from pathlib import Path
from core.config_manager import ConfigManager


class TestConfigManager:
    """ConfigManagerクラスのテスト"""
    
    def test_load_default_config(self, tmp_path):
        """デフォルト設定の読み込み"""
        manager = ConfigManager(config_dir=tmp_path)
        config = manager.get_config()
        
        assert "pdf_engine" in config
        assert "mainfont" in config
        assert config["pdf_engine"] == "xelatex"
    
    def test_save_and_load_config(self, tmp_path):
        """設定の保存と読み込み"""
        manager = ConfigManager(config_dir=tmp_path)
        
        # 設定を更新
        manager.update_config({"toc_depth": 3})
        
        # 保存
        assert manager.save_config()
        
        # 新しいマネージャーで読み込み
        manager2 = ConfigManager(config_dir=tmp_path)
        assert manager2.load_config()
        
        config = manager2.get_config()
        assert config["toc_depth"] == 3
    
    def test_validate_config(self, tmp_path):
        """設定のバリデーション"""
        manager = ConfigManager(config_dir=tmp_path)
        
        # 有効な設定
        valid_config = {
            "pdf_engine": "xelatex",
            "mainfont": "Test Font",
            "toc_depth": 2,
        }
        assert manager.validate_config(valid_config)
        
        # 無効な設定（toc_depthが範囲外）
        invalid_config = {
            "pdf_engine": "xelatex",
            "mainfont": "Test Font",
            "toc_depth": 10,  # 範囲外
        }
        assert not manager.validate_config(invalid_config)
    
    def test_save_and_load_profile(self, tmp_path):
        """プロファイルの保存と読み込み"""
        manager = ConfigManager(config_dir=tmp_path)
        
        # 設定を更新
        manager.update_config({"toc_depth": 3})
        
        # プロファイルとして保存
        assert manager.save_profile("test_profile")
        
        # デフォルト設定に戻す
        manager.load_default_config()
        assert manager.get_config()["toc_depth"] != 3
        
        # プロファイルを読み込み
        assert manager.load_profile("test_profile")
        assert manager.get_config()["toc_depth"] == 3
