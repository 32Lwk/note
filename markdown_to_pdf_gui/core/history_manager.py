"""変換履歴管理: 履歴の記録、検索、フィルタ"""

import json
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
from dataclasses import dataclass, asdict


@dataclass
class ConversionHistory:
    """変換履歴のデータクラス"""
    timestamp: str
    md_file: str
    pdf_file: str
    success: bool
    duration: float  # 秒
    file_size_before: int
    file_size_after: int
    profile_name: Optional[str] = None
    error_type: Optional[str] = None
    error_message: Optional[str] = None


class HistoryManager:
    """変換履歴を管理するクラス"""
    
    def __init__(self, history_file: Optional[Path] = None):
        """
        履歴マネージャーを初期化
        
        Args:
            history_file: 履歴ファイルのパス（Noneの場合はデフォルト）
        """
        if history_file is None:
            history_dir = Path.home() / "Library" / "Application Support" / "MarkdownToPDF"
            history_dir.mkdir(parents=True, exist_ok=True)
            history_file = history_dir / "conversion_history.json"
        
        self.history_file = history_file
        self.history: List[ConversionHistory] = []
        self.load_history()
    
    def load_history(self) -> None:
        """履歴を読み込み"""
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.history = [
                        ConversionHistory(**item) for item in data
                    ]
            except Exception:
                self.history = []
        else:
            self.history = []
    
    def save_history(self) -> None:
        """履歴を保存"""
        try:
            data = [asdict(h) for h in self.history]
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception:
            pass
    
    def add_history(
        self,
        md_file: Path,
        pdf_file: Path,
        success: bool,
        duration: float,
        profile_name: Optional[str] = None,
        error_type: Optional[str] = None,
        error_message: Optional[str] = None
    ) -> None:
        """
        履歴を追加
        
        Args:
            md_file: マークダウンファイルのパス
            pdf_file: PDFファイルのパス
            success: 成功フラグ
            duration: 変換時間（秒）
            profile_name: 使用したプロファイル名
            error_type: エラータイプ（失敗時）
            error_message: エラーメッセージ（失敗時）
        """
        file_size_before = md_file.stat().st_size if md_file.exists() else 0
        file_size_after = pdf_file.stat().st_size if pdf_file.exists() and success else 0
        
        entry = ConversionHistory(
            timestamp=datetime.now().isoformat(),
            md_file=str(md_file),
            pdf_file=str(pdf_file),
            success=success,
            duration=duration,
            file_size_before=file_size_before,
            file_size_after=file_size_after,
            profile_name=profile_name,
            error_type=error_type,
            error_message=error_message
        )
        
        self.history.append(entry)
        self.save_history()
    
    def get_history(
        self,
        limit: Optional[int] = None,
        success_only: Optional[bool] = None,
        profile_name: Optional[str] = None
    ) -> List[ConversionHistory]:
        """
        履歴を取得（フィルタ対応）
        
        Args:
            limit: 取得件数の上限
            success_only: 成功のみ取得するか
            profile_name: プロファイル名でフィルタ
        
        Returns:
            履歴のリスト
        """
        filtered = self.history
        
        if success_only is not None:
            filtered = [h for h in filtered if h.success == success_only]
        
        if profile_name:
            filtered = [h for h in filtered if h.profile_name == profile_name]
        
        # 新しい順にソート
        filtered.sort(key=lambda x: x.timestamp, reverse=True)
        
        if limit:
            filtered = filtered[:limit]
        
        return filtered
    
    def search_history(self, query: str) -> List[ConversionHistory]:
        """
        履歴を検索
        
        Args:
            query: 検索クエリ（ファイル名に含まれる文字列）
        
        Returns:
            検索結果のリスト
        """
        query_lower = query.lower()
        results = [
            h for h in self.history
            if query_lower in h.md_file.lower() or query_lower in h.pdf_file.lower()
        ]
        results.sort(key=lambda x: x.timestamp, reverse=True)
        return results
    
    def get_statistics(self) -> Dict:
        """
        統計情報を取得
        
        Returns:
            統計情報の辞書
        """
        total = len(self.history)
        successful = sum(1 for h in self.history if h.success)
        failed = total - successful
        
        total_duration = sum(h.duration for h in self.history)
        avg_duration = total_duration / total if total > 0 else 0
        
        return {
            'total_conversions': total,
            'successful': successful,
            'failed': failed,
            'success_rate': successful / total if total > 0 else 0,
            'total_duration': total_duration,
            'average_duration': avg_duration,
        }
    
    def clear_history(self) -> None:
        """履歴をクリア"""
        self.history = []
        self.save_history()
    
    def cleanup_old_history(self, days: int = 90) -> None:
        """
        古い履歴を削除
        
        Args:
            days: 保持する日数
        """
        from datetime import timedelta
        cutoff_date = datetime.now() - timedelta(days=days)
        
        self.history = [
            h for h in self.history
            if datetime.fromisoformat(h.timestamp) >= cutoff_date
        ]
        self.save_history()
