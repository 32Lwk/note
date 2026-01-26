"""設定マイグレーション: バージョン管理、バックアップ"""

import shutil
from pathlib import Path
from typing import Dict


class ConfigMigrator:
    """設定のマイグレーションを行うクラス"""
    
    def migrate(self, config: Dict, from_version: str, to_version: str) -> Dict:
        """
        設定をバージョン間で移行
        
        Args:
            config: 移行する設定
            from_version: 現在のバージョン
            to_version: 移行先のバージョン
        
        Returns:
            移行後の設定
        """
        # 現在は1.0.0のみなので、移行ロジックは実装しない
        # 将来のバージョンアップ時に実装
        
        migrated_config = config.copy()
        migrated_config['version'] = to_version
        
        return migrated_config
    
    def backup(self, config_path: Path) -> bool:
        """
        設定ファイルをバックアップ
        
        Args:
            config_path: 設定ファイルのパス
        
        Returns:
            成功した場合はTrue
        """
        try:
            backup_path = config_path.with_suffix('.json.backup')
            shutil.copy2(config_path, backup_path)
            return True
        except Exception:
            return False
