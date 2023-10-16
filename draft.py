import os, pytest
from zipfile import ZipFile

with ZipFile('/Users/sergeybryazgin/PycharmProjects/qa_guru_hw_7/tests/tmp/test_file.zip', mode='r') as zf:
    with zf.open('book.txt', 'r') as txt_file:
        #print(txt_file.read().decode('utf-8'))
        f = open(os.path.abspath('tests/resources/book.txt'), 'r')
        #print(f.read())
        assert f.read() == txt_file.read().decode('utf-8')

#f.close()
#txt_file.close()