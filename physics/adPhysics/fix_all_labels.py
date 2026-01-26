#!/usr/bin/env python3
"""
plots.pyのすべてのラベル設定を修正するスクリプト
mathtextパーサーの問題を回避するため、すべてのset_xlabel, set_ylabel, set_title, set_zlabelの呼び出しをsafe_set_labelでラップ
"""

import re
import sys

def fix_labels_in_file(filepath):
    """ファイル内のすべてのset_xlabel, set_ylabel, set_title, set_zlabelの呼び出しを修正"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # set_xlabel, set_ylabel, set_title, set_zlabelの呼び出しを検出
        patterns = [
            (r'(\s+)(\w+)\.set_xlabel\(([^)]+)\)', r'\1safe_set_label(\2.set_xlabel, \3)'),
            (r'(\s+)(\w+)\.set_ylabel\(([^)]+)\)', r'\1safe_set_label(\2.set_ylabel, \3)'),
            (r'(\s+)(\w+)\.set_zlabel\(([^)]+)\)', r'\1safe_set_label(\2.set_zlabel, \3)'),
        ]
        
        # set_titleは数式を含まない可能性があるので、$記号がある場合のみ修正
        if re.search(r'set_title.*\$', line):
            line = re.sub(r'(\s+)(\w+)\.set_title\(([^)]+)\)', r'\1safe_set_label(\2.set_title, \3)', line)
        
        # 他のパターンを修正
        for pattern, replacement in patterns:
            line = re.sub(pattern, replacement, line)
        
        fixed_lines.append(line)
        i += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    print(f"修正完了: {filepath}")

if __name__ == '__main__':
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'plots.py'
    fix_labels_in_file(filepath)
