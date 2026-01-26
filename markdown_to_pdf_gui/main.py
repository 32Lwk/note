"""エントリーポイント: アプリケーションの起動"""

import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow


def main():
    """メイン関数"""
    app = QApplication(sys.argv)
    app.setApplicationName("Markdown to PDF Converter")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
