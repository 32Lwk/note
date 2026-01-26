"""Pandoc変換エンジン: 基本的な変換機能"""

import subprocess
from pathlib import Path
from typing import Dict, Optional, List
from .error_handler import ErrorHandler, ErrorType, ErrorCategory


class Converter:
    """Pandocを使用したPDF変換エンジン"""
    
    def __init__(self, error_handler: Optional[ErrorHandler] = None):
        self.error_handler = error_handler or ErrorHandler()
    
    def build_pandoc_command(
        self,
        md_file: Path,
        output_file: Path,
        config: Dict,
        template_path: Optional[Path] = None,
        header_path: Optional[Path] = None
    ) -> List[str]:
        """
        Pandocコマンドを構築
        
        Args:
            md_file: 入力マークダウンファイル
            output_file: 出力PDFファイル
            config: 変換設定
            template_path: テンプレートファイルのパス
            header_path: ヘッダーファイルのパス
        
        Returns:
            Pandocコマンドの引数リスト
        """
        cmd = ["pandoc", str(md_file)]
        
        # PDFエンジン
        pdf_engine = config.get("pdf_engine", "xelatex")
        cmd.extend(["--pdf-engine", pdf_engine])
        
        # 入力形式
        from_format = config.get("from", "markdown+tex_math_dollars+raw_tex")
        cmd.extend(["--from", from_format])
        
        # 出力形式
        cmd.extend(["--to", "pdf"])
        
        # テンプレート
        if template_path and template_path.exists():
            cmd.extend(["--template", str(template_path)])
        
        # ヘッダーファイル
        if header_path and header_path.exists():
            cmd.extend(["--include-in-header", str(header_path)])
        
        # 変数
        variables = {
            "mainfont": config.get("mainfont", "Hiragino Sans"),
            "CJKmainfont": config.get("cjk_mainfont", "Hiragino Sans"),
            "geometry": config.get("geometry", "margin=2.5cm"),
            "fontsize": config.get("fontsize", "10pt"),
            "documentclass": config.get("documentclass", "article"),
        }
        
        for key, value in variables.items():
            cmd.extend(["--variable", f"{key}:{value}"])
        
        # 目次
        if config.get("toc", True):
            cmd.append("--toc")
            toc_depth = config.get("toc_depth", 2)
            cmd.extend(["--toc-depth", str(toc_depth)])
        
        # セクション番号
        if config.get("number_sections", False):
            cmd.append("--number-sections")
        
        # ハイパーリンク
        if config.get("colorlinks", True):
            linkcolor = config.get("linkcolor", "blue")
            urlcolor = config.get("urlcolor", "blue")
            toccolor = config.get("toccolor", "blue")
            cmd.extend(["--variable", f"colorlinks:true"])
            cmd.extend(["--variable", f"linkcolor:{linkcolor}"])
            cmd.extend(["--variable", f"urlcolor:{urlcolor}"])
            cmd.extend(["--variable", f"toccolor:{toccolor}"])
        
        # スタンドアロン
        cmd.append("--standalone")
        
        # 出力ファイル
        cmd.extend(["--output", str(output_file)])
        
        return cmd
    
    def convert(
        self,
        md_file: Path,
        output_dir: Optional[Path] = None,
        config: Optional[Dict] = None,
        template_path: Optional[Path] = None,
        header_path: Optional[Path] = None
    ) -> tuple[bool, Optional[Path], str]:
        """
        マークダウンファイルをPDFに変換
        
        Args:
            md_file: 入力マークダウンファイル
            output_dir: 出力ディレクトリ（Noneの場合はmd_fileと同じディレクトリ）
            config: 変換設定
            template_path: テンプレートファイルのパス
            header_path: ヘッダーファイルのパス
        
        Returns:
            (成功フラグ, 出力PDFファイルパス, エラーメッセージ)
        """
        if config is None:
            config = {}
        
        if output_dir is None:
            output_dir = md_file.parent
        
        output_file = output_dir / f"{md_file.stem}.pdf"
        
        # コマンドの構築
        cmd = self.build_pandoc_command(
            md_file, output_file, config, template_path, header_path
        )
        
        # Pandocの実行
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300,  # 5分のタイムアウト
                check=False
            )
            
            if result.returncode == 0:
                if output_file.exists():
                    return True, output_file, ""
                else:
                    error_msg = "PDFファイルが生成されませんでした"
                    self.error_handler.handle_conversion_error(md_file, error_msg)
                    return False, None, error_msg
            else:
                error_msg = result.stderr or "変換に失敗しました"
                self.error_handler.handle_conversion_error(md_file, error_msg)
                return False, None, error_msg
        
        except subprocess.TimeoutExpired:
            error_msg = "変換がタイムアウトしました（5分以上）"
            self.error_handler.handle_conversion_error(md_file, error_msg)
            return False, None, error_msg
        
        except FileNotFoundError:
            error_msg = "Pandocが見つかりません"
            self.error_handler.handle_pandoc_not_found()
            return False, None, error_msg
        
        except Exception as e:
            error_msg = f"予期しないエラー: {str(e)}"
            self.error_handler.handle_conversion_error(md_file, error_msg)
            return False, None, error_msg
