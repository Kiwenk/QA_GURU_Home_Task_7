import os
import shutil
import zipfile
import pytest
from script_os import FILES_DIR, FOLDER_DIR
#import download_files



@pytest.fixture(scope="session", autouse=True)
def packing_files_into_archive():
    if not os.path.exists(FOLDER_DIR):  # проверяем существует ли папка
        os.mkdir(FOLDER_DIR)  # создаем папку если её нет
    # if not os.path.exists(FILES_DIR):
    #     os.mkdir(FILES_DIR)
    with zipfile.ZipFile(os.path.join(FOLDER_DIR, "archive.zip"), 'w') as zf:  # создаем архив
        for file in os.listdir(FILES_DIR):  # добавляем файлы в архив
            zf.write(os.path.join(FILES_DIR, file), file)  # добавляем файл в архив

    yield
    shutil.rmtree(FOLDER_DIR)  # удаляем папку со всеми файлами и подпапками


