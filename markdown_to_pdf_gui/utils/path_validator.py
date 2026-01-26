"""パス検証: セキュリティ対策（パストラバーサル防止）"""

from pathlib import Path
from typing import Optional
import os


class PathValidator:
    """パスの検証と正規化を行うクラス（セキュリティ対策）"""
    
    @staticmethod
    def validate_path(path: str, base_dir: Optional[Path] = None) -> Optional[Path]:
        """
        パスを検証し、正規化する
        
        Args:
            path: 検証するパス
            base_dir: ベースディレクトリ（相対パスの解決に使用）
        
        Returns:
            正規化されたPathオブジェクト、無効な場合はNone
        """
        try:
            # パスを正規化
            if base_dir is not None:
                # 相対パスの場合、ベースディレクトリからの相対パスとして解決
                resolved = (base_dir / path).resolve()
                # ベースディレクトリの外に出ていないか確認
                if not resolved.is_relative_to(base_dir.resolve()):
                    return None
                return resolved
            else:
                # 絶対パスの場合
                resolved = Path(path).resolve()
                return resolved
        except (ValueError, OSError):
            return None
    
    @staticmethod
    def is_safe_path(path: Path, base_dir: Optional[Path] = None) -> bool:
        """
        パスが安全かどうかを確認（パストラバーサル防止）
        
        Args:
            path: 確認するパス
            base_dir: ベースディレクトリ
        
        Returns:
            安全な場合はTrue
        """
        try:
            resolved = path.resolve()
            
            # ベースディレクトリが指定されている場合、その中に含まれるか確認
            if base_dir is not None:
                base_resolved = base_dir.resolve()
                return resolved.is_relative_to(base_resolved)
            
            return True
        except (ValueError, OSError):
            return False
    
    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """
        ファイル名をサニタイズ（危険な文字を除去）
        
        Args:
            filename: サニタイズするファイル名
        
        Returns:
            サニタイズされたファイル名
        """
        # 危険な文字を除去
        dangerous_chars = ['/', '\\', '..', '\x00']
        sanitized = filename
        for char in dangerous_chars:
            sanitized = sanitized.replace(char, '')
        
        return sanitized
    
    @staticmethod
    def ensure_directory_exists(path: Path) -> bool:
        """
        ディレクトリが存在することを確認し、存在しない場合は作成
        
        Args:
            path: ディレクトリパス
        
        Returns:
            成功した場合はTrue
        """
        try:
            path.mkdir(parents=True, exist_ok=True)
            return True
        except (OSError, PermissionError):
            return False
