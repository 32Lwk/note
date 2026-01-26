"""EmojiConverterのテスト"""

import pytest
from core.emoji_converter import EmojiConverter


class TestEmojiConverter:
    """EmojiConverterクラスのテスト"""
    
    def test_convert_warning_emoji(self):
        """警告絵文字の変換"""
        converter = EmojiConverter()
        content = "⚠️ 注意してください"
        
        converted, emojis = converter.convert(content)
        
        assert r'\warning{}' in converted
        assert '⚠️' in emojis
    
    def test_convert_star_emoji(self):
        """星絵文字の変換"""
        converter = EmojiConverter()
        content = "⭐ 重要"
        
        converted, emojis = converter.convert(content)
        
        assert r'\staricon{}' in converted
        assert '⭐' in emojis
    
    def test_add_custom_mapping(self):
        """カスタムマッピングの追加"""
        converter = EmojiConverter()
        converter.add_mapping('✅', r'\checkmark{}')
        
        content = "✅ 完了"
        converted, _ = converter.convert(content)
        
        assert r'\checkmark{}' in converted
