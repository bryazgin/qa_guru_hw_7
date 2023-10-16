import  os, pytest
from zipfile import ZipFile


path = os.path.abspath('resources')
files = os.listdir(path)

with ZipFile('test_file.zip', mode='w') as zf:
    for file in files:
        add_file = os.path.join(path, file)
        zf.write(add_file)

if not os.path.exists('tmp'):
    os.mkdir('tmp')
os.rename('/Users/bryazgin/PycharmProjects/qa_guru_hw_7/tests/test_file.zip',
          '/Users/bryazgin/PycharmProjects/qa_guru_hw_7/tests/tmp/test_file.zip')

#def file_check():
    #проверить, что файл в архиве является тем, что был в resources
    #for file in ZipFile(''):
        #zip_info = ZipFile.read('test_file.zip')

