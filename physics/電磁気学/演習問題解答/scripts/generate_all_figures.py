#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
すべての電磁気学演習問題の図を生成する統合スクリプト
"""

import subprocess
import sys
import os

def main():
    """すべての図生成スクリプトを実行"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)  # 演習問題解答
    scripts = [
        'generate_figures_ex1.py',
        'generate_figures_ex2.py',
        'generate_figures_ex3.py',
        'generate_figures_ex4.py',
        'generate_figures_ex5.py',
        'generate_figures_ex6.py',
        'generate_figures_ex7.py',
    ]
    
    for script in scripts:
        script_path = os.path.join(script_dir, script)
        if os.path.exists(script_path):
            print(f"\n{'='*60}")
            print(f"実行中: {script}")
            print(f"{'='*60}")
            try:
                subprocess.run([sys.executable, script_path], check=True, cwd=parent_dir)
            except subprocess.CalledProcessError as e:
                print(f"エラー: {script} の実行に失敗しました: {e}")
        else:
            print(f"警告: {script} が見つかりません")
    
    print("\nすべての図の生成が完了しました。")

if __name__ == '__main__':
    main()
