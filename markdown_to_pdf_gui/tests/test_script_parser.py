"""ScriptParserのテスト"""

import pytest
from pathlib import Path
from core.script_parser import ScriptParser


class TestScriptParser:
    """ScriptParserクラスのテスト"""
    
    def test_parse_simple_script(self, tmp_path):
        """シンプルなスクリプトの解析"""
        parser = ScriptParser()
        script_file = tmp_path / "convert.sh"
        script_file.write_text(
            "#!/bin/bash\n"
            "pandoc test.md --pdf-engine=xelatex -o test.pdf\n",
            encoding='utf-8'
        )
        
        config = parser.parse_script(script_file)
        
        assert config is not None
        assert config.get('pdf_engine') == 'xelatex'
    
    def test_parse_yaml_config(self, tmp_path):
        """YAML設定ファイルの解析"""
        parser = ScriptParser()
        yaml_file = tmp_path / "config.yaml"
        yaml_file.write_text(
            "pdf-engine: xelatex\n"
            "toc: true\n"
            "toc-depth: 2\n",
            encoding='utf-8'
        )
        
        config = parser.parse_yaml_config(yaml_file)
        
        assert config is not None
        assert config.get('pdf_engine') == 'xelatex'
        assert config.get('toc') is True
