"""設定管理: JSON + YAML対応、バリデーション"""

import json
import yaml
from pathlib import Path
from typing import Dict, Optional, List
from .config_migrator import ConfigMigrator


class ConfigManager:
    """設定を管理するクラス"""
    
    def __init__(self, config_dir: Optional[Path] = None):
        """
        設定マネージャーを初期化
        
        Args:
            config_dir: 設定ディレクトリ（Noneの場合はデフォルト）
        """
        if config_dir is None:
            config_dir = Path.home() / "Library" / "Application Support" / "MarkdownToPDF"
        config_dir.mkdir(parents=True, exist_ok=True)
        
        self.config_dir = config_dir
        self.config_file = config_dir / "config.json"
        self.profiles_dir = config_dir / "profiles"
        self.profiles_dir.mkdir(exist_ok=True)
        
        self.migrator = ConfigMigrator()
        self.config: Dict = {}
        self.load_default_config()
    
    def load_default_config(self) -> None:
        """デフォルト設定を読み込み"""
        default_config_path = Path(__file__).parent.parent / "config" / "default_config.json"
        if default_config_path.exists():
            with open(default_config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            # フォールバック: ハードコードされたデフォルト設定
            self.config = {
                "version": "1.0.0",
                "profile_name": "default",
                "pdf_engine": "xelatex",
                "mainfont": "Hiragino Sans",
                "cjk_mainfont": "Hiragino Sans",
                "geometry": "margin=2.5cm",
                "fontsize": "10pt",
                "documentclass": "article",
                "toc": True,
                "toc_depth": 2,
                "number_sections": False,
                "colorlinks": True,
                "linkcolor": "blue",
                "urlcolor": "blue",
                "toccolor": "blue",
            }
    
    def load_config(self) -> bool:
        """
        設定ファイルを読み込み
        
        Returns:
            成功した場合はTrue
        """
        if not self.config_file.exists():
            return False
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                loaded_config = json.load(f)
            
            # バージョンチェックとマイグレーション
            if 'version' in loaded_config:
                current_version = loaded_config['version']
                if current_version != self.config.get('version', '1.0.0'):
                    loaded_config = self.migrator.migrate(
                        loaded_config,
                        current_version,
                        self.config.get('version', '1.0.0')
                    )
            
            # バリデーション
            if self.validate_config(loaded_config):
                self.config.update(loaded_config)
                return True
            else:
                return False
        
        except Exception:
            return False
    
    def save_config(self) -> bool:
        """
        設定を保存
        
        Returns:
            成功した場合はTrue
        """
        try:
            # バックアップ
            if self.config_file.exists():
                self.migrator.backup(self.config_file)
            
            # バリデーション
            if not self.validate_config(self.config):
                return False
            
            # 保存
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            
            return True
        
        except Exception:
            return False
    
    def validate_config(self, config: Dict) -> bool:
        """
        設定をバリデーション
        
        Args:
            config: 検証する設定
        
        Returns:
            有効な場合はTrue
        """
        # 必須項目のチェック
        required_fields = ["pdf_engine", "mainfont"]
        for field in required_fields:
            if field not in config:
                return False
        
        # 値の範囲チェック
        if "toc_depth" in config:
            toc_depth = config["toc_depth"]
            if not isinstance(toc_depth, int) or toc_depth < 1 or toc_depth > 6:
                return False
        
        # ファイルパスの存在確認（指定されている場合）
        if "template_path" in config and config["template_path"]:
            if not Path(config["template_path"]).exists():
                return False
        
        if "header_path" in config and config["header_path"]:
            if not Path(config["header_path"]).exists():
                return False
        
        return True
    
    def get_config(self) -> Dict:
        """現在の設定を取得"""
        return self.config.copy()
    
    def update_config(self, updates: Dict) -> bool:
        """
        設定を更新
        
        Args:
            updates: 更新する設定項目
        
        Returns:
            成功した場合はTrue
        """
        self.config.update(updates)
        return self.validate_config(self.config)
    
    def load_profile(self, profile_name: str) -> bool:
        """
        プロファイルを読み込み
        
        Args:
            profile_name: プロファイル名
        
        Returns:
            成功した場合はTrue
        """
        profile_file = self.profiles_dir / f"{profile_name}.json"
        if not profile_file.exists():
            return False
        
        try:
            with open(profile_file, 'r', encoding='utf-8') as f:
                profile_config = json.load(f)
            
            if self.validate_config(profile_config):
                self.config.update(profile_config)
                self.config['profile_name'] = profile_name
                return True
        
        except Exception:
            pass
        
        return False
    
    def save_profile(self, profile_name: str) -> bool:
        """
        現在の設定をプロファイルとして保存
        
        Args:
            profile_name: プロファイル名
        
        Returns:
            成功した場合はTrue
        """
        profile_file = self.profiles_dir / f"{profile_name}.json"
        
        try:
            profile_config = self.config.copy()
            profile_config['profile_name'] = profile_name
            
            if not self.validate_config(profile_config):
                return False
            
            with open(profile_file, 'w', encoding='utf-8') as f:
                json.dump(profile_config, f, indent=2, ensure_ascii=False)
            
            return True
        
        except Exception:
            return False
    
    def list_profiles(self) -> List[str]:
        """
        利用可能なプロファイルのリストを取得
        
        Returns:
            プロファイル名のリスト
        """
        profiles = []
        for profile_file in self.profiles_dir.glob("*.json"):
            profiles.append(profile_file.stem)
        return profiles
    
    def load_yaml_config(self, yaml_path: Path) -> bool:
        """
        YAML設定ファイルを読み込み
        
        Args:
            yaml_path: YAMLファイルのパス
        
        Returns:
            成功した場合はTrue
        """
        if not yaml_path.exists():
            return False
        
        try:
            with open(yaml_path, 'r', encoding='utf-8') as f:
                yaml_data = yaml.safe_load(f)
            
            if yaml_data is None:
                return False
            
            # YAMLデータを設定形式に変換
            config = self._yaml_to_config(yaml_data)
            
            if self.validate_config(config):
                self.config.update(config)
                return True
        
        except Exception:
            pass
        
        return False
    
    def _yaml_to_config(self, yaml_data: Dict) -> Dict:
        """YAMLデータを設定形式に変換"""
        config = {}
        
        direct_mappings = {
            'pdf-engine': 'pdf_engine',
            'toc': 'toc',
            'toc-depth': 'toc_depth',
            'colorlinks': 'colorlinks',
            'linkcolor': 'linkcolor',
            'urlcolor': 'urlcolor',
            'toccolor': 'toccolor',
            'documentclass': 'documentclass',
            'fontsize': 'fontsize',
            'mainfont': 'mainfont',
            'CJKmainfont': 'cjk_mainfont',
        }
        
        for yaml_key, config_key in direct_mappings.items():
            if yaml_key in yaml_data:
                config[config_key] = yaml_data[yaml_key]
        
        # geometryの処理
        if 'geometry' in yaml_data:
            geometry = yaml_data['geometry']
            if isinstance(geometry, list):
                config['geometry'] = ','.join(geometry)
            elif isinstance(geometry, str):
                config['geometry'] = geometry
        
        return config
