"""図生成スクリプトの自動実行"""

import subprocess
from pathlib import Path
from typing import List, Optional, Tuple
import os


class FigureGenerator:
    """図生成スクリプトを実行するクラス"""
    
    def __init__(self):
        self.executed_scripts: List[Path] = []
    
    def detect_scripts(self, md_file_dir: Path) -> List[Path]:
        """
        図生成スクリプトを検出
        
        Args:
            md_file_dir: マークダウンファイルのディレクトリ
        
        Returns:
            検出されたスクリプトファイルのパスリスト
        """
        scripts = []
        
        # .pyスクリプトを検索
        for py_file in md_file_dir.glob("*.py"):
            # 図生成スクリプトの可能性があるファイル名パターン
            name_lower = py_file.name.lower()
            if any(keyword in name_lower for keyword in ['figure', 'plot', 'generate', 'graph']):
                scripts.append(py_file)
        
        return scripts
    
    def should_regenerate(self, script_path: Path, figures_dir: Optional[Path] = None) -> bool:
        """
        図の再生成が必要かどうかを判定
        
        Args:
            script_path: スクリプトファイルのパス
            figures_dir: 図ファイルのディレクトリ（Noneの場合はscript_pathと同じディレクトリ）
        
        Returns:
            再生成が必要な場合はTrue
        """
        if figures_dir is None:
            figures_dir = script_path.parent / "figures"
        
        if not script_path.exists():
            return False
        
        script_mtime = script_path.stat().st_mtime
        
        # 図ディレクトリが存在しない場合は生成が必要
        if not figures_dir.exists():
            return True
        
        # 図ファイルが存在しない場合は生成が必要
        image_extensions = ['.png', '.jpg', '.jpeg', '.pdf', '.svg']
        has_images = any(
            f.suffix.lower() in image_extensions
            for f in figures_dir.iterdir()
            if f.is_file()
        )
        if not has_images:
            return True
        
        # スクリプトが図ファイルより新しい場合は再生成が必要
        for img_file in figures_dir.iterdir():
            if img_file.is_file() and img_file.suffix.lower() in image_extensions:
                img_mtime = img_file.stat().st_mtime
                if script_mtime > img_mtime:
                    return True
        
        return False
    
    def execute_script(self, script_path: Path, working_dir: Optional[Path] = None) -> Tuple[bool, str]:
        """
        Pythonスクリプトを実行
        
        Args:
            script_path: 実行するスクリプトファイルのパス
            working_dir: 作業ディレクトリ（Noneの場合はscript_pathのディレクトリ）
        
        Returns:
            (成功フラグ, エラーメッセージ)
        """
        if working_dir is None:
            working_dir = script_path.parent
        
        if not script_path.exists():
            return False, f"スクリプトファイルが存在しません: {script_path}"
        
        try:
            # Pythonスクリプトを実行
            result = subprocess.run(
                ["python3", str(script_path)],
                cwd=str(working_dir),
                capture_output=True,
                text=True,
                timeout=300,  # 5分のタイムアウト
                check=False
            )
            
            if result.returncode == 0:
                self.executed_scripts.append(script_path)
                return True, ""
            else:
                error_msg = result.stderr or "スクリプトの実行に失敗しました"
                return False, error_msg
        
        except subprocess.TimeoutExpired:
            return False, "スクリプトの実行がタイムアウトしました（5分以上）"
        
        except FileNotFoundError:
            return False, "python3が見つかりません"
        
        except Exception as e:
            return False, f"予期しないエラー: {str(e)}"
    
    def process_markdown_file(self, md_file: Path, auto_execute: bool = False) -> Tuple[List[Path], List[str]]:
        """
        マークダウンファイルに関連する図生成スクリプトを処理
        
        Args:
            md_file: マークダウンファイルのパス
            auto_execute: 自動実行するか（Falseの場合は検出のみ）
        
        Returns:
            (実行されたスクリプトのリスト, 警告メッセージのリスト)
        """
        md_dir = md_file.parent
        scripts = self.detect_scripts(md_dir)
        executed = []
        warnings = []
        
        for script in scripts:
            figures_dir = md_dir / "figures"
            if self.should_regenerate(script, figures_dir):
                if auto_execute:
                    success, error_msg = self.execute_script(script)
                    if success:
                        executed.append(script)
                    else:
                        warnings.append(f"スクリプト実行エラー ({script.name}): {error_msg}")
                else:
                    warnings.append(f"図の再生成が必要です: {script.name}")
        
        return executed, warnings
