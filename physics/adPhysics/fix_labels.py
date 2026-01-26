#!/usr/bin/env python3
"""
plots.pyのすべてのラベル設定を修正するスクリプト
mathtextパーサーの問題を回避するため、$...$形式を\(...\)形式に変更
"""

import re

def fix_labels_in_file(filepath):
    """ファイル内のすべてのset_xlabel, set_ylabel, set_title, set_zlabelの呼び出しを修正"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # $...$形式を\(...\)形式に変更する関数
    def replace_dollar_math(match):
        label = match.group(1)
        # $...$形式を\(...\)形式に変更
        label = re.sub(r'\$([^$]+)\$', r'\\(\1\\)', label)
        return f'{match.group(0).split("(")[0]}({label}'
    
    # set_xlabel, set_ylabel, set_title, set_zlabelの呼び出しを修正
    patterns = [
        (r'(\.set_xlabel\()([^)]+)(\))', r'\1\2\3'),
        (r'(\.set_ylabel\()([^)]+)(\))', r'\1\2\3'),
        (r'(\.set_title\()([^)]+)(\))', r'\1\2\3'),
        (r'(\.set_zlabel\()([^)]+)(\))', r'\1\2\3'),
    ]
    
    # $...$形式を\(...\)形式に変更
    def fix_math_in_string(match):
        full_match = match.group(0)
        # 文字列内の$...$形式を\(...\)形式に変更
        fixed = re.sub(r'\$([^$]+)\$', r'\\(\1\\)', full_match)
        return fixed
    
    # 文字列リテラル内の$...$形式を\(...\)形式に変更
    content = re.sub(r"('[^']*\$[^']*')", fix_math_in_string, content)
    content = re.sub(r'("[^"]*\$[^"]*")', fix_math_in_string, content)
    content = re.sub(r"(r'[^']*\$[^']*')", fix_math_in_string, content)
    content = re.sub(r'(r"[^"]*\$[^"]*")', fix_math_in_string, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"修正完了: {filepath}")

if __name__ == '__main__':
    import sys
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'plots.py'
    fix_labels_in_file(filepath)
