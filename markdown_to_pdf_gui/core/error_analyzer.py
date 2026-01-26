"""エラーログ分析: エラーパターンの集計と解決策の提案"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from collections import Counter


class ErrorAnalyzer:
    """エラーログを分析するクラス"""
    
    def __init__(self, log_dir: Optional[Path] = None):
        """
        エラー分析器を初期化
        
        Args:
            log_dir: ログディレクトリ（Noneの場合はデフォルト）
        """
        if log_dir is None:
            log_dir = Path.home() / "Library" / "Application Support" / "MarkdownToPDF" / "logs"
        self.log_dir = log_dir
    
    def analyze_patterns(self, log_files: Optional[List[Path]] = None, days: int = 30) -> Dict:
        """
        エラーパターンを集計
        
        Args:
            log_files: 分析するログファイルのリスト（Noneの場合は自動検出）
            days: 分析する日数
        
        Returns:
            エラーパターンの集計結果
        """
        if log_files is None:
            log_files = self._find_recent_logs(days)
        
        error_counts = Counter()
        error_types = Counter()
        error_by_category = Counter()
        
        cutoff_date = datetime.now() - timedelta(days=days)
        
        for log_file in log_files:
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip():
                            try:
                                log_entry = json.loads(line)
                                if log_entry.get('level') == 'ERROR':
                                    error_type = log_entry.get('error_type', 'UNKNOWN')
                                    category = log_entry.get('category', 'GENERAL')
                                    
                                    error_counts[error_type] += 1
                                    error_types[error_type] += 1
                                    error_by_category[category] += 1
                            except json.JSONDecodeError:
                                pass
            except Exception:
                pass
        
        return {
            'total_errors': sum(error_counts.values()),
            'error_types': dict(error_types),
            'error_by_category': dict(error_by_category),
            'most_common_errors': error_counts.most_common(10),
        }
    
    def suggest_solutions(self, error_type: str) -> List[str]:
        """
        エラータイプに応じた解決策を提案
        
        Args:
            error_type: エラータイプ
        
        Returns:
            解決策のリスト
        """
        solutions_map = {
            'LATEX_COMPILE_ERROR': [
                "LaTeXの構文エラーを確認してください",
                "必要なパッケージがインストールされているか確認してください",
                "エラーログの詳細を確認してください",
            ],
            'FONT_NOT_FOUND': [
                "フォントがシステムにインストールされているか確認してください",
                "設定で別のフォントを指定してください",
                "fc-listコマンドで利用可能なフォントを確認してください",
            ],
            'TEMPLATE_ERROR': [
                "テンプレートファイルの構文を確認してください",
                "デフォルトテンプレートを使用することを検討してください",
            ],
            'IMAGE_NOT_FOUND': [
                "画像パスを確認してください",
                "画像ファイルが存在するか確認してください",
                "相対パスが正しいか確認してください",
            ],
            'PANDOC_NOT_FOUND': [
                "Pandocをインストールしてください: https://pandoc.org/installing.html",
                "macOSの場合: brew install pandoc",
            ],
            'XELATEX_NOT_FOUND': [
                "XeLaTeXをインストールしてください: https://www.tug.org/texlive/",
                "macOSの場合: brew install --cask mactex",
            ],
        }
        
        return solutions_map.get(error_type, ["エラーログを確認してください"])
    
    def _find_recent_logs(self, days: int) -> List[Path]:
        """最近のログファイルを検出"""
        if not self.log_dir.exists():
            return []
        
        cutoff_date = datetime.now() - timedelta(days=days)
        log_files = []
        
        for log_file in self.log_dir.glob("*.log"):
            try:
                if log_file.stat().st_mtime >= cutoff_date.timestamp():
                    log_files.append(log_file)
            except Exception:
                pass
        
        # 変換ログも含める
        for log_file in self.log_dir.glob("conversion_log_*.txt"):
            try:
                if log_file.stat().st_mtime >= cutoff_date.timestamp():
                    log_files.append(log_file)
            except Exception:
                pass
        
        return log_files
