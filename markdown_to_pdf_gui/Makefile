.PHONY: install test clean build app

install:
	pip install -r requirements.txt
	python setup.py install

test:
	pytest tests/ -v

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

build:
	python setup.py sdist bdist_wheel

app:
	pyinstaller --windowed --name "MarkdownToPDF" --icon=icon.icns main.py
