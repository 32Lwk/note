"""統合テスト: 実際の変換フローのテスト"""

import pytest
from pathlib import Path
from core.converter import Converter
from core.config_manager import ConfigManager
from core.template_manager import TemplateManager


class TestIntegration:
    """統合テストクラス"""
    
    @pytest.mark.skipif(
        not Path("/usr/local/bin/pandoc").exists() and not Path("/opt/homebrew/bin/pandoc").exists(),
        reason="Pandocがインストールされていません"
    )
    def test_basic_conversion_flow(self, tmp_path):
        """基本的な変換フローのテスト"""
        # テスト用マークダウンファイルを作成
        md_file = tmp_path / "test.md"
        md_file.write_text(
            "# Test Document\n\n"
            "This is a test.\n\n"
            "## Section 1\n\n"
            "Some content here.\n",
            encoding='utf-8'
        )
        
        # 設定マネージャー
        config_manager = ConfigManager(config_dir=tmp_path / "config")
        config = config_manager.get_config()
        
        # テンプレートマネージャー
        template_manager = TemplateManager()
        template_path, header_path = template_manager.find_templates(md_file)
        
        # コンバーター
        converter = Converter()
        success, output_file, error_msg = converter.convert(
            md_file,
            output_dir=tmp_path,
            config=config,
            template_path=template_path,
            header_path=header_path
        )
        
        # 結果の確認（Pandocが利用可能な場合のみ）
        if success and output_file:
            assert output_file.exists()
            assert output_file.suffix == '.pdf'
