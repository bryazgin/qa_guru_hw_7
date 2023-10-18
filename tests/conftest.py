import pytest, os, utils
from zipfile import ZipFile



path = os.path.abspath('resources')
files = os.listdir(path)

@pytest.fixture(scope='session', autouse=True)
def make_zip():
    with ZipFile('test_file.zip', mode='a') as zf:
        for file in files:
            add_file = os.path.join(path, file)
            zf.write(add_file, arcname=add_file.split("/")[-1])


@pytest.fixture(scope='session', autouse=True)
def replace_file():
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    os.rename(os.path.join(utils.TESTS_PATH, 'test_file.zip'), utils.ZIP_PATH)
