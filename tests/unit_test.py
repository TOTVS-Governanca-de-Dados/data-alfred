import unittest
import os
import sys
from pathlib import Path

# Assuming your main function is in a module named '__main__'
sys.path.insert(0, '/home/alestan/data-alfred/src/data-alfred')
import __main__ as main_module

class TestMainFunction(unittest.TestCase):
    def setUp(self):
        # Call the main function
        main_module.main()

    def test_data_dirs(self):
        data_dirs = ['data/preprocessed', 'data/raw', 'data/mischaracterized']
        for dir in data_dirs:
            self.assertTrue(Path(dir).is_dir())

    def test_docs(self):
        self.assertTrue(Path('docs').is_dir())
        self.assertTrue(Path('docs/mkdocs.md').is_file())
        self.assertTrue(Path('docs/config.yml').is_file())

    def test_models(self):
        self.assertTrue(Path('models').is_dir())

    def test_notebooks(self):
        self.assertTrue(Path('notebooks').is_dir())

    def test_frontend(self):
        self.assertTrue(Path('frontend').is_dir())
        self.assertTrue(Path('frontend/__init__.py').is_file())
        self.assertTrue(Path('frontend/streamlit_app.py').is_file())

    def test_references(self):
        self.assertTrue(Path('references').is_dir())

    def test_reports(self):
        self.assertTrue(Path('reports').is_dir())

    def test_src_dirs(self):
        src_dirs = ['src/visualization', 'src/data', 'src/features', 'src/models', 'src/tests']
        for dir in src_dirs:
            self.assertTrue(Path(dir).is_dir())
        self.assertTrue(Path('src/__init__.py').is_file())

    def test_root_files(self):
        root_files = ['.env', '.gitignore', 'README.md', 'requirements.txt', 'setup.py', 'test_environment.py', 'Dockerfile']
        for file in root_files:
            self.assertTrue(Path(file).is_file())

if __name__ == '__main__':
    unittest.main()