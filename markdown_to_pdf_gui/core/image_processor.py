"""画像処理: SVG→PNG変換、サイズ調整、graphicspath自動設定"""

import subprocess
from pathlib import Path
from typing import List, Optional, Tuple
import shutil


class ImageProcessor:
    """画像処理を行うクラス"""
    
    def __init__(self):
        self.temp_dir: Optional[Path] = None
        self.has_cairosvg = shutil.which("cairosvg") is not None
        self.has_inkscape = shutil.which("inkscape") is not None
    
    def process_images(
        self,
        md_file: Path,
        image_paths: List[Path],
        convert_svg: bool = True
    ) -> Tuple[List[Path], List[str]]:
        """
        画像を処理（SVG変換、パス解決など）
        
        Args:
            md_file: マークダウンファイルのパス
            image_paths: 画像ファイルのパスリスト
            convert_svg: SVGをPNGに変換するか
        
        Returns:
            (処理済み画像パスのリスト, 警告メッセージのリスト)
        """
        warnings = []
        processed_paths = []
        md_dir = md_file.parent
        
        for img_path in image_paths:
            if not img_path.exists():
                warnings.append(f"画像が見つかりません: {img_path}")
                continue
            
            # SVGファイルの処理
            if img_path.suffix.lower() == '.svg' and convert_svg:
                converted_path = self.convert_svg_to_png(img_path, md_dir)
                if converted_path:
                    processed_paths.append(converted_path)
                else:
                    warnings.append(f"SVG変換に失敗しました: {img_path}")
                    processed_paths.append(img_path)  # 元のパスを使用
            else:
                processed_paths.append(img_path)
        
        return processed_paths, warnings
    
    def convert_svg_to_png(self, svg_path: Path, output_dir: Optional[Path] = None) -> Optional[Path]:
        """
        SVGファイルをPNGに変換
        
        Args:
            svg_path: SVGファイルのパス
            output_dir: 出力ディレクトリ（Noneの場合はsvg_pathと同じディレクトリ）
        
        Returns:
            変換されたPNGファイルのパス、失敗時はNone
        """
        if output_dir is None:
            output_dir = svg_path.parent
        
        png_path = output_dir / f"{svg_path.stem}.png"
        
        # cairosvgを使用
        if self.has_cairosvg:
            try:
                result = subprocess.run(
                    ["cairosvg", str(svg_path), "-o", str(png_path)],
                    capture_output=True,
                    text=True,
                    timeout=30,
                    check=False
                )
                if result.returncode == 0 and png_path.exists():
                    return png_path
            except (subprocess.TimeoutExpired, FileNotFoundError):
                pass
        
        # Inkscapeを使用（フォールバック）
        if self.has_inkscape:
            try:
                result = subprocess.run(
                    ["inkscape", str(svg_path), "--export-filename", str(png_path)],
                    capture_output=True,
                    text=True,
                    timeout=30,
                    check=False
                )
                if result.returncode == 0 and png_path.exists():
                    return png_path
            except (subprocess.TimeoutExpired, FileNotFoundError):
                pass
        
        return None
    
    def find_image_directories(self, md_file: Path) -> List[Path]:
        """
        画像ディレクトリを検出
        
        Args:
            md_file: マークダウンファイルのパス
        
        Returns:
            画像ディレクトリのパスリスト
        """
        directories = []
        md_dir = md_file.parent
        
        # 検索パス
        search_paths = [
            md_dir,
            md_dir / "figures",
            md_dir.parent / "figures",
        ]
        
        for path in search_paths:
            if path.exists() and path.is_dir():
                # 画像ファイルが含まれているか確認
                image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.pdf']
                has_images = any(
                    f.suffix.lower() in image_extensions
                    for f in path.iterdir()
                    if f.is_file()
                )
                if has_images:
                    directories.append(path)
        
        return directories
    
    def generate_graphicspath(self, directories: List[Path]) -> str:
        """
        graphicspathコマンドを生成
        
        Args:
            directories: 画像ディレクトリのパスリスト
        
        Returns:
            LaTeXのgraphicspathコマンド
        """
        if not directories:
            return ""
        
        paths = [f"{{{str(d)}}}" for d in directories]
        return f"\\graphicspath{{{','.join(paths)}}}"
    
    def optimize_image(self, image_path: Path, max_size: Optional[Tuple[int, int]] = None) -> Optional[Path]:
        """
        画像を最適化（リサイズなど）
        
        Args:
            image_path: 画像ファイルのパス
            max_size: 最大サイズ（幅, 高さ）、Noneの場合は最適化しない
        
        Returns:
            最適化された画像のパス、失敗時はNone
        """
        # 将来的にPIL/Pillowを使用して実装
        # 現在は未実装（パスをそのまま返す）
        return image_path
