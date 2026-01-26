"""統計収集: 使用統計の収集と表示"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from .history_manager import HistoryManager


class StatisticsCollector:
    """統計情報を収集するクラス"""
    
    def __init__(self, history_manager: HistoryManager):
        """
        統計収集器を初期化
        
        Args:
            history_manager: 履歴マネージャー
        """
        self.history_manager = history_manager
        self.stats_file = Path.home() / "Library" / "Application Support" / "MarkdownToPDF" / "statistics.json"
        self.enabled = True  # 設定で有効/無効を切り替え可能
    
    def record_conversion(
        self,
        file_path: str,
        config: Dict,
        duration: float,
        success: bool
    ) -> None:
        """
        変換履歴を記録（HistoryManager経由）
        
        Args:
            file_path: 変換したファイルのパス
            config: 使用した設定
            duration: 変換時間（秒）
            success: 成功フラグ
        """
        if not self.enabled:
            return
        
        # HistoryManagerに記録（既に実装済み）
        # このメソッドは将来の拡張用
        pass
    
    def get_statistics(self) -> Dict:
        """
        統計情報を集計して返す
        
        Returns:
            統計情報の辞書
        """
        if not self.enabled:
            return {}
        
        # HistoryManagerから統計を取得
        stats = self.history_manager.get_statistics()
        
        # 追加の統計情報
        history = self.history_manager.get_history()
        
        # よく使用する設定
        profile_usage = {}
        for entry in history:
            profile = entry.profile_name or "デフォルト"
            profile_usage[profile] = profile_usage.get(profile, 0) + 1
        
        most_used_profile = max(profile_usage.items(), key=lambda x: x[1])[0] if profile_usage else None
        
        # 日別の変換回数（過去30日）
        daily_counts = {}
        cutoff_date = datetime.now() - timedelta(days=30)
        for entry in history:
            entry_date = datetime.fromisoformat(entry.timestamp)
            if entry_date >= cutoff_date:
                date_key = entry_date.strftime("%Y-%m-%d")
                daily_counts[date_key] = daily_counts.get(date_key, 0) + 1
        
        stats.update({
            'most_used_profile': most_used_profile,
            'profile_usage': profile_usage,
            'daily_counts': daily_counts,
            'last_30_days_total': sum(daily_counts.values()),
        })
        
        return stats
    
    def export_statistics(self, format: str = 'json') -> Optional[str]:
        """
        統計情報をエクスポート
        
        Args:
            format: エクスポート形式（'json'のみ対応）
        
        Returns:
            エクスポートされたデータの文字列、失敗時はNone
        """
        if not self.enabled:
            return None
        
        stats = self.get_statistics()
        
        if format == 'json':
            return json.dumps(stats, indent=2, ensure_ascii=False)
        
        return None
    
    def save_statistics(self) -> None:
        """統計情報をファイルに保存"""
        if not self.enabled:
            return
        
        stats = self.get_statistics()
        try:
            self.stats_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=2, ensure_ascii=False)
        except Exception:
            pass
    
    def load_statistics(self) -> Dict:
        """統計情報をファイルから読み込み"""
        if not self.stats_file.exists():
            return {}
        
        try:
            with open(self.stats_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
