"""既存スクリプトの解析: .shスクリプトとYAML設定ファイルから設定を抽出"""

import re
import yaml
from pathlib import Path
from typing import Dict, Optional, List
import json


class ScriptParser:
    """既存の変換スクリプトを解析して設定を抽出するクラス"""
    
    def __init__(self):
        self.config: Dict = {}
    
    def parse_script(self, script_path: Path) -> Optional[Dict]:
        """
        .shスクリプトを解析して設定を抽出
        
        Args:
            script_path: スクリプトファイルのパス
        
        Returns:
            抽出された設定辞書、失敗時はNone
        """
        if not script_path.exists() or script_path.suffix != '.sh':
            return None
        
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            return None
        
        config = {}
        
        # pandocコマンドの検出
        pandoc_match = re.search(r'pandoc\s+"?([^"]+\.md)"?', content)
        if pandoc_match:
            config['input_file'] = pandoc_match.group(1)
        
        # オプションの抽出
        options = self._extract_pandoc_options(content)
        config.update(options)
        
        # テンプレート/ヘッダーファイルの検出
        template_match = re.search(r'--template=([^\s]+)', content)
        if template_match:
            config['template_path'] = template_match.group(1)
        
        header_match = re.search(r'--include-in-header=([^\s]+)|-H\s+([^\s]+)', content)
        if header_match:
            config['header_path'] = header_match.group(1) or header_match.group(2)
        
        return config if config else None
    
    def parse_yaml_config(self, yaml_path: Path) -> Optional[Dict]:
        """
        YAML設定ファイルを解析
        
        Args:
            yaml_path: YAMLファイルのパス
        
        Returns:
            抽出された設定辞書、失敗時はNone
        """
        if not yaml_path.exists() or yaml_path.suffix not in ['.yaml', '.yml']:
            return None
        
        try:
            with open(yaml_path, 'r', encoding='utf-8') as f:
                yaml_data = yaml.safe_load(f)
            
            if yaml_data is None:
                return None
            
            # YAMLデータをJSON互換の形式に変換
            config = self._yaml_to_config(yaml_data)
            return config
        except Exception:
            return None
    
    def _extract_pandoc_options(self, content: str) -> Dict:
        """pandocコマンドからオプションを抽出"""
        options = {}
        
        # --pdf-engine
        match = re.search(r'--pdf-engine=(\w+)', content)
        if match:
            options['pdf_engine'] = match.group(1)
        
        # --from
        match = re.search(r'--from=([^\s]+)', content)
        if match:
            options['from'] = match.group(1)
        
        # --variable オプション
        var_matches = re.finditer(r'--variable=([^:]+):([^\s]+)', content)
        for match in var_matches:
            var_name = match.group(1).strip()
            var_value = match.group(2).strip().strip('"\'')
            options[var_name] = var_value
        
        # -V オプション（短縮形）
        v_matches = re.finditer(r'-V\s+([^:]+):([^\s]+)', content)
        for match in v_matches:
            var_name = match.group(1).strip()
            var_value = match.group(2).strip().strip('"\'')
            options[var_name] = var_value
        
        # --toc
        if '--toc' in content:
            options['toc'] = True
        
        # --toc-depth
        match = re.search(r'--toc-depth[=:](\d+)', content)
        if match:
            options['toc_depth'] = int(match.group(1))
        
        # --number-sections
        if '--number-sections' in content:
            options['number_sections'] = True
        
        return options
    
    def _yaml_to_config(self, yaml_data: Dict) -> Dict:
        """YAMLデータを設定形式に変換"""
        config = {}
        
        # 直接マッピング
        direct_mappings = {
            'pdf-engine': 'pdf_engine',
            'toc': 'toc',
            'toc-depth': 'toc_depth',
            'colorlinks': 'colorlinks',
            'linkcolor': 'linkcolor',
            'urlcolor': 'urlcolor',
            'toccolor': 'toccolor',
            'documentclass': 'documentclass',
            'fontsize': 'fontsize',
            'mainfont': 'mainfont',
            'CJKmainfont': 'cjk_mainfont',
        }
        
        for yaml_key, config_key in direct_mappings.items():
            if yaml_key in yaml_data:
                config[config_key] = yaml_data[yaml_key]
        
        # geometryの処理
        if 'geometry' in yaml_data:
            geometry = yaml_data['geometry']
            if isinstance(geometry, list):
                config['geometry'] = ','.join(geometry)
            elif isinstance(geometry, str):
                config['geometry'] = geometry
        
        return config
    
    def find_configs_in_directory(self, directory: Path) -> List[Dict]:
        """
        ディレクトリ内の設定ファイルを検索
        
        Args:
            directory: 検索するディレクトリ
        
        Returns:
            見つかった設定のリスト
        """
        configs = []
        
        # .shスクリプトの検索
        for script_file in directory.glob('*.sh'):
            if 'convert' in script_file.name.lower() or 'pdf' in script_file.name.lower():
                config = self.parse_script(script_file)
                if config:
                    config['source'] = str(script_file)
                    configs.append(config)
        
        # YAML設定ファイルの検索
        for yaml_file in directory.glob('*.yaml'):
            if 'pandoc' in yaml_file.name.lower() or 'config' in yaml_file.name.lower():
                config = self.parse_yaml_config(yaml_file)
                if config:
                    config['source'] = str(yaml_file)
                    configs.append(config)
        
        for yaml_file in directory.glob('*.yml'):
            if 'pandoc' in yaml_file.name.lower() or 'config' in yaml_file.name.lower():
                config = self.parse_yaml_config(yaml_file)
                if config:
                    config['source'] = str(yaml_file)
                    configs.append(config)
        
        return configs
