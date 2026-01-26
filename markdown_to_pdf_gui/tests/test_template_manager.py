"""TemplateManagerのテスト"""

import pytest
from pathlib import Path
from core.template_manager import TemplateManager


class TestTemplateManager:
    """TemplateManagerクラスのテスト"""
    
    def test_find_templates_in_same_directory(self, tmp_path):
        """同一ディレクトリのテンプレート検出"""
        manager = TemplateManager()
        
        md_file = tmp_path / "test.md"
        md_file.write_text("# Test")
        
        template_file = tmp_path / "pandoc_template.tex"
        template_file.write_text("\\documentclass{article}\\begin{document}$body$\\end{document}")
        
        header_file = tmp_path / "pandoc_header.tex"
        header_file.write_text("% header")
        
        template, header = manager.find_templates(md_file)
        
        assert template == template_file
        assert header == header_file
    
    def test_find_default_templates(self, tmp_path):
        """デフォルトテンプレートの検出"""
        manager = TemplateManager()
        
        md_file = tmp_path / "test.md"
        md_file.write_text("# Test")
        
        template, header = manager.find_templates(md_file)
        
        # デフォルトテンプレートが存在する場合
        if manager.default_template_dir.exists():
            assert template is not None
            assert header is not None
    
    def test_validate_template(self, tmp_path):
        """テンプレートのバリデーション"""
        manager = TemplateManager()
        
        # 有効なテンプレート
        valid_template = tmp_path / "valid.tex"
        valid_template.write_text(
            "\\documentclass{article}\n"
            "\\begin{document}\n"
            "$body$\n"
            "\\end{document}"
        )
        
        is_valid, errors = manager.validate_template(valid_template)
        assert is_valid
        assert len(errors) == 0
        
        # 無効なテンプレート（$body$がない）
        invalid_template = tmp_path / "invalid.tex"
        invalid_template.write_text(
            "\\documentclass{article}\n"
            "\\begin{document}\n"
            "\\end{document}"
        )
        
        is_valid, errors = manager.validate_template(invalid_template)
        assert not is_valid
        assert len(errors) > 0
