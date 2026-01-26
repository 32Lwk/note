"""環境チェッカー: Pandoc、XeLaTeX、フォントの存在確認"""

import subprocess
import shutil
from typing import List, Tuple, Optional
from pathlib import Path


class EnvironmentChecker:
    """環境依存関係をチェックするクラス"""
    
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.pandoc_version: Optional[str] = None
        self.xelatex_version: Optional[str] = None
        self.available_fonts: List[str] = []
    
    def check_all(self) -> Tuple[bool, List[str], List[str]]:
        """
        すべての依存関係をチェック
        
        Returns:
            (成功フラグ, エラーリスト, 警告リスト)
        """
        self.errors.clear()
        self.warnings.clear()
        
        # Pandocのチェック
        if not self.check_pandoc():
            self.errors.append("Pandocが見つかりません。インストールしてください: https://pandoc.org/installing.html")
        
        # XeLaTeXのチェック
        if not self.check_xelatex():
            self.errors.append("XeLaTeXが見つかりません。インストールしてください: https://www.tug.org/texlive/")
        
        # フォントのチェック
        self.check_fonts()
        
        # オプション: Inkscapeのチェック
        if not self.check_inkscape():
            self.warnings.append("Inkscapeが見つかりません（SVG変換用、オプション）")
        
        return len(self.errors) == 0, self.errors, self.warnings
    
    def check_pandoc(self) -> bool:
        """Pandocの存在を確認"""
        pandoc_path = shutil.which("pandoc")
        if pandoc_path is None:
            return False
        
        try:
            result = subprocess.run(
                ["pandoc", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                # バージョン情報の最初の行を取得
                self.pandoc_version = result.stdout.split('\n')[0]
                return True
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        
        return False
    
    def check_xelatex(self) -> bool:
        """XeLaTeXの存在を確認"""
        xelatex_path = shutil.which("xelatex")
        if xelatex_path is None:
            return False
        
        try:
            result = subprocess.run(
                ["xelatex", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                # バージョン情報の最初の行を取得
                self.xelatex_version = result.stdout.split('\n')[0]
                return True
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        
        return False
    
    def check_fonts(self) -> None:
        """日本語フォントの存在を確認"""
        try:
            result = subprocess.run(
                ["fc-list", ":lang=ja"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                fonts = result.stdout.strip().split('\n')
                self.available_fonts = [f.split(':')[0] for f in fonts if f]
                
                # Hiragino Sansの確認
                hiragino_found = any("Hiragino" in f for f in self.available_fonts)
                if not hiragino_found:
                    self.warnings.append(
                        "Hiragino Sansフォントが見つかりません。"
                        "macOSでは通常インストールされていますが、"
                        "他のフォントを使用する場合は設定で変更できます。"
                    )
        except (subprocess.TimeoutExpired, FileNotFoundError):
            self.warnings.append("fc-listコマンドが見つかりません（フォント確認スキップ）")
    
    def check_inkscape(self) -> bool:
        """Inkscapeの存在を確認（オプション）"""
        return shutil.which("inkscape") is not None
    
    def check_latex_packages(self) -> Tuple[bool, List[str]]:
        """
        LaTeXパッケージの存在を確認
        
        Returns:
            (成功フラグ, 不足パッケージリスト)
        """
        missing_packages = []
        required_packages = [
            "xeCJK",
            "amsmath",
            "amssymb",
            "graphicx",
            "hyperref",
            "geometry",
            "booktabs",
            "longtable",
            "pifont",
            "float",
            "fancyvrb",
            "setspace",
            "parskip",
            "fancyhdr",
        ]
        
        try:
            result = subprocess.run(
                ["tlmgr", "list", "--only-installed"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                installed_packages = result.stdout.lower()
                for package in required_packages:
                    if package.lower() not in installed_packages:
                        missing_packages.append(package)
        except (subprocess.TimeoutExpired, FileNotFoundError):
            # tlmgrが見つからない場合は警告のみ
            self.warnings.append("tlmgrコマンドが見つかりません（LaTeXパッケージ確認スキップ）")
            return True, []  # エラーとはしない
        
        return len(missing_packages) == 0, missing_packages
    
    def get_installation_instructions(self) -> str:
        """インストール方法の説明を取得"""
        instructions = []
        
        if not self.check_pandoc():
            instructions.append(
                "Pandocのインストール:\n"
                "  macOS: brew install pandoc\n"
                "  または: https://pandoc.org/installing.html"
            )
        
        if not self.check_xelatex():
            instructions.append(
                "XeLaTeXのインストール:\n"
                "  macOS: brew install --cask mactex\n"
                "  または: https://www.tug.org/texlive/"
            )
        
        return "\n\n".join(instructions)
