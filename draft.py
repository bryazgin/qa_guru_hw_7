import os, pytest
from zipfile import ZipFile

from PyPDF2 import PdfReader
from io import BytesIO

#проверка txt
with ZipFile('/Users/bryazgin/PycharmProjects/qa_guru_hw_7/tests/tmp/test_file.zip', mode='r') as zf:
    with zf.open('book.txt', 'r') as txt_file:
        f = open(os.path.abspath('tests/resources/book.txt'), 'r')
        assert (txt_file.read().decode('utf-8')) == f.read()


#проверка xls


#проверка pdf

with ZipFile('/Users/bryazgin/PycharmProjects/qa_guru_hw_7/tests/tmp/test_file.zip', mode='r') as zf:
    zip_pdf = PdfReader(BytesIO(zf.read('SQL.pdf')))
    resources_pdf = PdfReader('/Users/bryazgin/PycharmProjects/qa_guru_hw_7/tests/resources/SQL.pdf')
    assert len(zip_pdf.pages) == len(resources_pdf.pages)
    assert zip_pdf.pages[3].extract_text() == resources_pdf.pages[3].extract_text()
