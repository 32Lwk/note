"""Setup script for Markdown to PDF GUI Tool"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="markdown-to-pdf-gui",
    version="1.0.0",
    author="",
    description="マークダウンファイルをPDFに変換するためのGUI管理ツール",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.6.0",
        "pyyaml>=6.0",
        "cairosvg>=2.7.0",
        "chardet>=5.0.0",
        "pypdf>=3.0.0",
        "psutil>=5.9.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "markdown-to-pdf-gui=markdown_to_pdf_gui.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
