"""MarkdownValidatorのテスト"""

import pytest
from pathlib import Path
from core.markdown_validator import MarkdownValidator, ValidationResult


class TestMarkdownValidator:
    """MarkdownValidatorクラスのテスト"""
    
    def test_validate_nonexistent_file(self, tmp_path):
        """存在しないファイルの検証"""
        validator = MarkdownValidator()
        md_file = tmp_path / "nonexistent.md"
        
        result = validator.validate(md_file)
        
        assert not result.is_valid()
        assert len(result.errors) > 0
    
    def test_validate_simple_file(self, tmp_path):
        """シンプルなマークダウンファイルの検証"""
        validator = MarkdownValidator()
        md_file = tmp_path / "test.md"
        md_file.write_text("# Test\n\nThis is a test.", encoding='utf-8')
        
        result = validator.validate(md_file)
        
        assert result.is_valid()
        assert result.encoding == 'utf-8'
    
    def test_detect_emoji(self, tmp_path):
        """絵文字の検出"""
        validator = MarkdownValidator()
        md_file = tmp_path / "test.md"
        md_file.write_text("# Test ⚠️ ⭐", encoding='utf-8')
        
        result = validator.validate(md_file)
        
        assert result.has_emoji
    
    def test_detect_math(self, tmp_path):
        """数式の検出"""
        validator = MarkdownValidator()
        md_file = tmp_path / "test.md"
        md_file.write_text("# Test\n\n$E = mc^2$", encoding='utf-8')
        
        result = validator.validate(md_file)
        
        assert result.has_math
