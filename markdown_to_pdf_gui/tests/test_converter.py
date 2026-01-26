"""Converterのテスト"""

import pytest
from pathlib import Path
from core.converter import Converter
from core.error_handler import ErrorHandler


class TestConverter:
    """Converterクラスのテスト"""
    
    def test_build_pandoc_command_basic(self):
        """基本的なPandocコマンドの構築"""
        converter = Converter()
        md_file = Path("test.md")
        output_file = Path("test.pdf")
        config = {}
        
        cmd = converter.build_pandoc_command(md_file, output_file, config)
        
        assert "pandoc" in cmd
        assert str(md_file) in cmd
        assert "--pdf-engine" in cmd
        assert "xelatex" in cmd
        assert "--to" in cmd
        assert "pdf" in cmd
        assert str(output_file) in cmd
    
    def test_build_pandoc_command_with_template(self, tmp_path):
        """テンプレート付きのPandocコマンドの構築"""
        converter = Converter()
        md_file = tmp_path / "test.md"
        output_file = tmp_path / "test.pdf"
        template = tmp_path / "template.tex"
        template.write_text("\\documentclass{article}\\begin{document}$body$\\end{document}")
        config = {}
        
        cmd = converter.build_pandoc_command(md_file, output_file, config, template_path=template)
        
        assert "--template" in cmd
        assert str(template) in cmd
    
    def test_build_pandoc_command_with_config(self):
        """設定付きのPandocコマンドの構築"""
        converter = Converter()
        md_file = Path("test.md")
        output_file = Path("test.pdf")
        config = {
            "mainfont": "Test Font",
            "toc": True,
            "toc_depth": 3,
        }
        
        cmd = converter.build_pandoc_command(md_file, output_file, config)
        
        assert "--variable" in " ".join(cmd)
        assert "--toc" in cmd
        assert "--toc-depth" in cmd
        assert "3" in cmd
