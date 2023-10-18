import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
TESTS_PATH = os.path.join(PROJECT_ROOT_PATH, 'tests')
RESOURCES_PATH = os.path.join(TESTS_PATH, 'resources')
TMP_PATH = os.path.join(TESTS_PATH, 'tmp')
ZIP_PATH = os.path.join(TMP_PATH, 'test_file.zip')
