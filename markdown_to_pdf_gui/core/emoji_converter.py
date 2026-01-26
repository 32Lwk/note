"""絵文字変換: 絵文字→LaTeXコマンド変換"""

import re
from typing import Dict, List, Tuple


class EmojiConverter:
    """絵文字をLaTeXコマンドに変換するクラス"""
    
    def __init__(self):
        # 絵文字→LaTeXコマンドのマッピング
        self.emoji_map: Dict[str, str] = {
            '⚠️': r'\warning{}',
            '⭐': r'\staricon{}',
            '✅': r'\checkmark{}',
            '❌': r'\times{}',
            'ℹ️': r'\info{}',
            '📝': r'\note{}',
            '💡': r'\idea{}',
            '🔍': r'\search{}',
            '📌': r'\pin{}',
            '🔗': r'\link{}',
        }
        
        # 絵文字パターン（Unicode範囲）
        self.emoji_pattern = re.compile(
            r'[\U0001F300-\U0001F9FF]|'  # 絵文字範囲1
            r'[\U0001FA00-\U0001FAFF]|'  # 絵文字範囲2
            r'[\U00002600-\U000026FF]|'  # 記号・絵文字
            r'[\U00002700-\U000027BF]|'  # 記号・絵文字
            r'[\U0001F600-\U0001F64F]|'  # 顔文字
            r'[\U0001F680-\U0001F6FF]|'  # 交通・地図記号
            r'[\U0001F1E0-\U0001F1FF]'   # 国旗
        )
    
    def convert(self, content: str) -> Tuple[str, List[str]]:
        """
        マークダウンコンテンツ内の絵文字をLaTeXコマンドに変換
        
        Args:
            content: 変換するマークダウンコンテンツ
        
        Returns:
            (変換後のコンテンツ, 変換された絵文字のリスト)
        """
        converted_emojis = []
        converted_content = content
        
        # マッピングされている絵文字を変換
        for emoji, latex_cmd in self.emoji_map.items():
            if emoji in converted_content:
                converted_content = converted_content.replace(emoji, latex_cmd)
                converted_emojis.append(emoji)
        
        # その他の絵文字を検出（警告用）
        other_emojis = set(self.emoji_pattern.findall(converted_content))
        for emoji in other_emojis:
            if emoji not in self.emoji_map:
                converted_emojis.append(emoji)
        
        return converted_content, list(set(converted_emojis))
    
    def add_mapping(self, emoji: str, latex_command: str) -> None:
        """
        カスタム絵文字マッピングを追加
        
        Args:
            emoji: 絵文字
            latex_command: LaTeXコマンド（例: r'\custom{}'）
        """
        self.emoji_map[emoji] = latex_command
    
    def get_missing_emojis(self, content: str) -> List[str]:
        """
        マッピングされていない絵文字を検出
        
        Args:
            content: 検索するコンテンツ
        
        Returns:
            マッピングされていない絵文字のリスト
        """
        all_emojis = set(self.emoji_pattern.findall(content))
        missing = [e for e in all_emojis if e not in self.emoji_map]
        return missing
    
    def generate_latex_definitions(self, emojis: List[str]) -> str:
        """
        検出された絵文字用のLaTeXコマンド定義を生成
        
        Args:
            emojis: 定義が必要な絵文字のリスト
        
        Returns:
            LaTeXコマンド定義の文字列
        """
        definitions = []
        definitions.append("% 絵文字用のLaTeXコマンド定義")
        definitions.append("\\usepackage{pifont}")
        
        # 既存のマッピング
        if '⚠️' in emojis:
            definitions.append("\\newcommand{\\warning}{\\ding{73}}")
        if '⭐' in emojis:
            definitions.append("\\newcommand{\\staricon}{\\ding{72}}")
        
        # その他の絵文字は警告として記録
        for emoji in emojis:
            if emoji not in self.emoji_map:
                # デフォルトのコマンド名を生成
                cmd_name = f"emoji{hash(emoji) % 10000}"
                definitions.append(f"% 未定義の絵文字: {emoji}")
                definitions.append(f"% \\newcommand{{\\{cmd_name}}}{{}}")
        
        return "\n".join(definitions)
