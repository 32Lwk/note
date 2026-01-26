"""テンプレート管理: 自動検出、優先順位実装"""

from pathlib import Path
from typing import List, Tuple, Optional
import re


class TemplateManager:
    """テンプレートを管理するクラス"""
    
    def __init__(self):
        self.default_template_dir = Path(__file__).parent.parent / "templates"
    
    def find_templates(
        self,
        md_file: Path,
        user_template: Optional[Path] = None,
        user_header: Optional[Path] = None
    ) -> Tuple[Optional[Path], Optional[Path]]:
        """
        テンプレートとヘッダーファイルを検出（優先順位に従う）
        
        Args:
            md_file: マークダウンファイルのパス
            user_template: ユーザー指定のテンプレート
            user_header: ユーザー指定のヘッダー
        
        Returns:
            (テンプレートパス, ヘッダーパス)
        """
        template_path = None
        header_path = None
        
        # 1. ユーザー指定を最優先
        if user_template and user_template.exists():
            template_path = user_template
        
        if user_header and user_header.exists():
            header_path = user_header
        
        # 2. 同一ディレクトリを検索
        md_dir = md_file.parent
        if template_path is None:
            template_path = self._find_in_directory(md_dir, ['pandoc_template.tex'])
        
        if header_path is None:
            header_path = self._find_in_directory(
                md_dir,
                ['pandoc_header.tex', 'latex_header.tex']
            )
        
        # 3. 親ディレクトリのtemplates/フォルダ
        if template_path is None:
            parent_templates = md_dir.parent / "templates"
            if parent_templates.exists():
                template_path = self._find_in_directory(
                    parent_templates,
                    ['pandoc_template.tex', 'template.tex']
                )
        
        if header_path is None:
            parent_templates = md_dir.parent / "templates"
            if parent_templates.exists():
                header_path = self._find_in_directory(
                    parent_templates,
                    ['pandoc_header.tex', 'latex_header.tex', 'header.tex']
                )
        
        # 4. デフォルトテンプレート
        if template_path is None:
            default_template = self.default_template_dir / "default_template.tex"
            if default_template.exists():
                template_path = default_template
        
        if header_path is None:
            default_header = self.default_template_dir / "default_header.tex"
            if default_header.exists():
                header_path = default_header
        
        return template_path, header_path
    
    def _find_in_directory(self, directory: Path, filenames: List[str]) -> Optional[Path]:
        """ディレクトリ内でファイルを検索"""
        for filename in filenames:
            file_path = directory / filename
            if file_path.exists():
                return file_path
        return None
    
    def validate_template(self, template_path: Path) -> Tuple[bool, List[str]]:
        """
        テンプレートのバリデーション
        
        Args:
            template_path: テンプレートファイルのパス
        
        Returns:
            (有効かどうか, エラーメッセージのリスト)
        """
        errors = []
        
        if not template_path.exists():
            return False, ["テンプレートファイルが存在しません"]
        
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 基本的な構文チェック
            if '\\documentclass' not in content:
                errors.append("\\documentclassが見つかりません")
            
            if '\\begin{document}' not in content:
                errors.append("\\begin{document}が見つかりません")
            
            if '\\end{document}' not in content:
                errors.append("\\end{document}が見つかりません")
            
            if '$body$' not in content:
                errors.append("$body$が見つかりません（pandocテンプレートとして必要）")
            
            # 必須パッケージの確認
            required_packages = ['xeCJK', 'graphicx', 'hyperref']
            for package in required_packages:
                if f'\\usepackage{{{package}}}' not in content:
                    errors.append(f"必須パッケージ {package} が見つかりません")
        
        except Exception as e:
            return False, [f"テンプレートの読み込みエラー: {str(e)}"]
        
        return len(errors) == 0, errors
    
    def detect_custom_commands(self, header_path: Path) -> List[str]:
        """
        カスタムLaTeXコマンドを検出
        
        Args:
            header_path: ヘッダーファイルのパス
        
        Returns:
            検出されたコマンド名のリスト
        """
        commands = []
        
        if not header_path.exists():
            return commands
        
        try:
            with open(header_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # \newcommandを検出
            pattern = r'\\newcommand\{?\\([^}]+)\}?'
            matches = re.findall(pattern, content)
            commands.extend(matches)
        
        except Exception:
            pass
        
        return commands
