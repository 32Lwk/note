"""マークダウンファイルの前処理と検証"""

import chardet
from pathlib import Path
from typing import List, Tuple, Optional, Dict
import re


class ValidationResult:
    """検証結果を保持するクラス"""
    
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.encoding: Optional[str] = None
        self.image_paths: List[Path] = []
        self.missing_images: List[str] = []
        self.broken_links: List[str] = []
        self.file_size: int = 0
        self.has_emoji: bool = False
        self.has_math: bool = False
    
    def is_valid(self) -> bool:
        """エラーがない場合はTrue"""
        return len(self.errors) == 0


class MarkdownValidator:
    """マークダウンファイルの検証を行うクラス"""
    
    def __init__(self):
        self.emoji_pattern = re.compile(
            r'[\U0001F300-\U0001F9FF]|'  # 絵文字範囲1
            r'[\U0001FA00-\U0001FAFF]|'  # 絵文字範囲2
            r'[\U00002600-\U000026FF]|'  # 記号・絵文字
            r'[\U00002700-\U000027BF]'   # 記号・絵文字
        )
        self.math_inline_pattern = re.compile(r'\$[^$]+\$')
        self.math_block_pattern = re.compile(r'\$\$[\s\S]*?\$\$')
        self.image_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
        self.link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    def validate(self, md_file: Path) -> ValidationResult:
        """
        マークダウンファイルを検証
        
        Args:
            md_file: マークダウンファイルのパス
        
        Returns:
            ValidationResultオブジェクト
        """
        result = ValidationResult()
        
        if not md_file.exists():
            result.errors.append(f"ファイルが存在しません: {md_file}")
            return result
        
        # ファイルサイズの確認
        result.file_size = md_file.stat().st_size
        if result.file_size > 10 * 1024 * 1024:  # 10MB
            result.warnings.append(
                f"ファイルサイズが大きいです ({result.file_size / 1024 / 1024:.1f}MB)。"
                "処理に時間がかかる可能性があります。"
            )
        
        # エンコーディングの検出
        result.encoding = self._detect_encoding(md_file)
        if result.encoding is None:
            result.errors.append("ファイルのエンコーディングを検出できませんでした")
            return result
        
        # ファイルの読み込み
        try:
            with open(md_file, 'r', encoding=result.encoding) as f:
                content = f.read()
        except UnicodeDecodeError:
            result.errors.append(f"ファイルの読み込みに失敗しました（エンコーディング: {result.encoding}）")
            return result
        
        # 画像パスの確認
        self._check_images(content, md_file, result)
        
        # リンクの確認
        self._check_links(content, md_file, result)
        
        # 特殊文字の検出
        if self.emoji_pattern.search(content):
            result.has_emoji = True
        
        # 数式の検出
        if self.math_inline_pattern.search(content) or self.math_block_pattern.search(content):
            result.has_math = True
            # 数式の構文チェック
            self._check_math_syntax(content, result)
        
        return result
    
    def _detect_encoding(self, file_path: Path) -> Optional[str]:
        """エンコーディングを検出"""
        try:
            with open(file_path, 'rb') as f:
                raw_data = f.read()
                detected = chardet.detect(raw_data)
                if detected['confidence'] > 0.7:
                    return detected['encoding']
        except Exception:
            pass
        
        # デフォルトはUTF-8
        return 'utf-8'
    
    def _check_images(self, content: str, md_file: Path, result: ValidationResult) -> None:
        """画像パスの存在を確認"""
        matches = self.image_pattern.findall(content)
        md_dir = md_file.parent
        
        for alt_text, img_path in matches:
            # パスの解決
            resolved_path = self._resolve_image_path(img_path, md_dir)
            if resolved_path and resolved_path.exists():
                result.image_paths.append(resolved_path)
            else:
                result.missing_images.append(img_path)
                result.warnings.append(f"画像が見つかりません: {img_path}")
    
    def _resolve_image_path(self, img_path: str, base_dir: Path) -> Optional[Path]:
        """画像パスを解決"""
        # 絶対パスの場合
        if Path(img_path).is_absolute():
            return Path(img_path) if Path(img_path).exists() else None
        
        # 相対パスの場合、複数の場所を試す
        search_paths = [
            base_dir / img_path,
            base_dir / "figures" / img_path,
            base_dir.parent / "figures" / img_path,
        ]
        
        for path in search_paths:
            if path.exists():
                return path
        
        return None
    
    def _check_links(self, content: str, md_file: Path, result: ValidationResult) -> None:
        """リンクの妥当性を確認"""
        matches = self.link_pattern.findall(content)
        md_dir = md_file.parent
        
        for link_text, link_url in matches:
            # 内部リンク（アンカーリンク）の確認
            if link_url.startswith('#'):
                # アンカーリンクの存在確認は後で実装（マークダウンのパースが必要）
                continue
            
            # 外部URLの確認はスキップ（ネットワークアクセスが必要）
            if link_url.startswith('http://') or link_url.startswith('https://'):
                continue
            
            # 相対パスの場合、ファイルの存在確認
            if not link_url.startswith('/'):
                link_path = md_dir / link_url
                if not link_path.exists():
                    result.broken_links.append(link_url)
                    result.warnings.append(f"リンク先が見つかりません: {link_url}")
    
    def _check_math_syntax(self, content: str, result: ValidationResult) -> None:
        """数式の構文チェック（基本的なペア確認）"""
        # インライン数式のペア確認
        inline_matches = self.math_inline_pattern.findall(content)
        for match in inline_matches:
            if match.count('$') != 2:
                result.warnings.append(f"インライン数式の構文が不正です: {match[:50]}")
        
        # ブロック数式のペア確認
        block_matches = self.math_block_pattern.findall(content)
        for match in block_matches:
            if match.count('$$') != 2:
                result.warnings.append(f"ブロック数式の構文が不正です: {match[:50]}")
