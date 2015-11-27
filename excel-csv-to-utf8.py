__author__ = 'mmaks'
"""
Скрипт для перевода CSV-выгрузки из Excel в кодировку UTF-8.
Скрипт запускается из папки с данными, итерирует по всем файлам в ней (кроме .py и скрытых) и сохраняет копии файлов в UTF-8 в соседнюю папку "data-encoded"
"""

import os

os.mkdir('../data-encoded')
for filename in os.listdir(os.getcwd()):
    if filename.startswith(".") or filename.endswith(".py"):
        continue
    print(filename)
    with open(filename, 'r', encoding='windows-1251') as sourceFile:
        with open('../data-encoded/' + filename, 'w', encoding='utf-8') as resultFile:
            for line in sourceFile:
                resultFile.write(line)