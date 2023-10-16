import pytest


@pytest.fixture()
def make_zip():
    with zipfile.ZipFile('test_file.zip', mode='w') as zf:
        for file in files:
            add_file = os.path.join(path, file)
            zf.write(add_file)


@pytest.fixture()
def replace_file():
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    os.rename('/Users/bryazgin/PycharmProjects/qa_guru_hw_7/tests/test_file.zip',
              '/Users/bryazgin/PycharmProjects/qa_guru_hw_7/tests/tmp/test_file.zip')
