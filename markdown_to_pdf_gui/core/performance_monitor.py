"""パフォーマンス監視: メモリ監視とパフォーマンス最適化"""

import time
import psutil
from pathlib import Path
from typing import Dict, Optional, List, Tuple
from datetime import datetime


class PerformanceMonitor:
    """パフォーマンスを監視するクラス"""
    
    def __init__(self):
        self.start_time: Optional[float] = None
        self.start_memory: Optional[int] = None
        self.peak_memory: int = 0
        self.process = psutil.Process()
    
    def start_conversion(self, file_path: Path) -> None:
        """
        変換開始時の監視を開始
        
        Args:
            file_path: 変換するファイルのパス
        """
        self.start_time = time.time()
        self.start_memory = self.process.memory_info().rss
        self.peak_memory = self.start_memory
    
    def update_memory(self) -> None:
        """メモリ使用量を更新"""
        current_memory = self.process.memory_info().rss
        if current_memory > self.peak_memory:
            self.peak_memory = current_memory
    
    def end_conversion(self) -> Dict:
        """
        変換終了時の統計を取得
        
        Returns:
            統計情報の辞書
        """
        elapsed = 0.0
        memory_used = 0
        
        if self.start_time is not None:
            elapsed = time.time() - self.start_time
        
        if self.start_memory is not None:
            self.update_memory()
            memory_used = self.peak_memory - self.start_memory
        
        return {
            'duration': elapsed,
            'memory_used': memory_used,
            'peak_memory': self.peak_memory,
        }
    
    def reset(self) -> None:
        """監視をリセット"""
        self.start_time = None
        self.start_memory = None
        self.peak_memory = 0
    
    def check_memory_limit(self, limit_mb: int = 2000) -> Tuple[bool, str]:
        """
        メモリ使用量の上限をチェック
        
        Args:
            limit_mb: メモリ上限（MB）
        
        Returns:
            (上限内かどうか, メッセージ)
        """
        self.update_memory()
        current_mb = self.peak_memory / 1024 / 1024
        
        if current_mb > limit_mb:
            return False, f"メモリ使用量が上限を超えています: {current_mb:.1f}MB / {limit_mb}MB"
        
        return True, f"メモリ使用量: {current_mb:.1f}MB / {limit_mb}MB"
    
    def get_system_info(self) -> Dict:
        """
        システム情報を取得
        
        Returns:
            システム情報の辞書
        """
        return {
            'cpu_count': psutil.cpu_count(),
            'memory_total': psutil.virtual_memory().total,
            'memory_available': psutil.virtual_memory().available,
            'memory_percent': psutil.virtual_memory().percent,
        }
    
    def estimate_remaining_time(
        self,
        completed_files: int,
        total_files: int,
        elapsed_time: float
    ) -> Optional[float]:
        """
        残り時間を推定
        
        Args:
            completed_files: 完了したファイル数
            total_files: 総ファイル数
            elapsed_time: 経過時間（秒）
        
        Returns:
            推定残り時間（秒）、推定できない場合はNone
        """
        if completed_files == 0 or total_files == 0:
            return None
        
        avg_time_per_file = elapsed_time / completed_files
        remaining_files = total_files - completed_files
        estimated_remaining = avg_time_per_file * remaining_files
        
        return estimated_remaining
