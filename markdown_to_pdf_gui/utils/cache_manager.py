"""キャッシュ管理: 変更検知によるスキップ"""

import hashlib
import json
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime


class CacheManager:
    """変換結果のキャッシュを管理するクラス"""
    
    def __init__(self, cache_dir: Optional[Path] = None):
        """
        キャッシュマネージャーを初期化
        
        Args:
            cache_dir: キャッシュディレクトリ（Noneの場合はデフォルト）
        """
        if cache_dir is None:
            cache_dir = Path.home() / "Library" / "Application Support" / "MarkdownToPDF" / "cache"
        cache_dir.mkdir(parents=True, exist_ok=True)
        
        self.cache_dir = cache_dir
        self.cache_file = cache_dir / "conversion_cache.json"
        self.cache: Dict = {}
        self.load_cache()
    
    def load_cache(self) -> None:
        """キャッシュを読み込み"""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    self.cache = json.load(f)
            except Exception:
                self.cache = {}
        else:
            self.cache = {}
    
    def save_cache(self) -> None:
        """キャッシュを保存"""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, indent=2, ensure_ascii=False)
        except Exception:
            pass
    
    def get_file_hash(self, file_path: Path) -> str:
        """
        ファイルのハッシュ値を計算
        
        Args:
            file_path: ファイルのパス
        
        Returns:
            ハッシュ値（SHA256）
        """
        if not file_path.exists():
            return ""
        
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception:
            return ""
    
    def should_skip_conversion(
        self,
        md_file: Path,
        pdf_file: Path,
        template_path: Optional[Path] = None,
        header_path: Optional[Path] = None
    ) -> bool:
        """
        変換をスキップできるかどうかを判定
        
        Args:
            md_file: マークダウンファイルのパス
            pdf_file: 出力PDFファイルのパス
            template_path: テンプレートファイルのパス
            header_path: ヘッダーファイルのパス
        
        Returns:
            スキップできる場合はTrue
        """
        # PDFファイルが存在しない場合は変換が必要
        if not pdf_file.exists():
            return False
        
        cache_key = str(md_file)
        
        # マークダウンファイルのハッシュ
        md_hash = self.get_file_hash(md_file)
        
        # テンプレート/ヘッダーファイルのハッシュ
        template_hash = self.get_file_hash(template_path) if template_path else ""
        header_hash = self.get_file_hash(header_path) if header_path else ""
        
        # キャッシュを確認
        if cache_key in self.cache:
            cached = self.cache[cache_key]
            
            # ハッシュが一致し、PDFファイルが存在する場合はスキップ
            if (cached.get('md_hash') == md_hash and
                cached.get('template_hash') == template_hash and
                cached.get('header_hash') == header_hash and
                pdf_file.exists()):
                return True
        
        return False
    
    def update_cache(
        self,
        md_file: Path,
        pdf_file: Path,
        template_path: Optional[Path] = None,
        header_path: Optional[Path] = None
    ) -> None:
        """
        キャッシュを更新
        
        Args:
            md_file: マークダウンファイルのパス
            pdf_file: 出力PDFファイルのパス
            template_path: テンプレートファイルのパス
            header_path: ヘッダーファイルのパス
        """
        cache_key = str(md_file)
        
        self.cache[cache_key] = {
            'md_hash': self.get_file_hash(md_file),
            'template_hash': self.get_file_hash(template_path) if template_path else "",
            'header_hash': self.get_file_hash(header_path) if header_path else "",
            'pdf_file': str(pdf_file),
            'timestamp': datetime.now().isoformat(),
        }
        
        self.save_cache()
    
    def clear_cache(self) -> None:
        """キャッシュをクリア"""
        self.cache = {}
        self.save_cache()
    
    def cleanup_old_cache(self, days: int = 30) -> None:
        """
        古いキャッシュエントリを削除
        
        Args:
            days: 保持する日数
        """
        from datetime import timedelta
        cutoff_date = datetime.now() - timedelta(days=days)
        
        keys_to_remove = []
        for key, value in self.cache.items():
            timestamp_str = value.get('timestamp', '')
            if timestamp_str:
                try:
                    timestamp = datetime.fromisoformat(timestamp_str)
                    if timestamp < cutoff_date:
                        keys_to_remove.append(key)
                except Exception:
                    pass
        
        for key in keys_to_remove:
            del self.cache[key]
        
        if keys_to_remove:
            self.save_cache()
