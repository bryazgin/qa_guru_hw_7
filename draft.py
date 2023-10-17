import os, pytest
from zipfile import ZipFile
from pypdf import PdfReader

#проверка txt
with ZipFile('/Users/sergeybryazgin/PycharmProjects/qa_guru_hw_7/tests/tmp/test_file.zip', mode='r') as zf:
    with zf.open('book.txt', 'r') as txt_file:
        f = open(os.path.abspath('tests/resources/book.txt'), 'r')
        assert (txt_file.read().decode('utf-8')) == f.read()


#проверка xls


#проверка pdf

with ZipFile('/Users/sergeybryazgin/PycharmProjects/qa_guru_hw_7/tests/tmp/test_file.zip', mode='r') as zf:
    with zf.open('SQL.pdf', 'r') as pdf_file:
        reader = PdfReader('/Users/sergeybryazgin/PycharmProjects/qa_guru_hw_7/tests/resources/SQL.pdf')
        for page in range(len(reader.pages)):
            content = reader.pages[page]
            print(content.extract_text())
        assert (pdf_file.read().decode('utf-8')) == f.read()

