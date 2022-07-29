import Data_processing_functions as DP_funk
import xml.etree.ElementTree as ET  # подключаем The ElementTree XML
import GlobalVariables
import os


# запись данных в файл
def save_data_to_file(fileName, textSave):
    with open(fileName, "w") as filetowrite:
        filetowrite.write(textSave)


# поиск файлов с разрешением omx
def get_file_name():
    current_dir = os.getcwd()  # получаем каталог, где запускается скрипт
    files_in_dir = os.listdir(current_dir)
    files_list = []
    for f in files_in_dir:
        if ".omx" in f:
            files_list.append(f)
    if len(files_list) > 1:  # выбор файла
        print('Необходимо выбрать файл для использования:')
        [print(files_list.index(i) + 1, i) for i in files_list]
        for i in range(3):
            temp = input()
            if temp.isdigit() and 1 <= int(temp) <= len(files_list)+1:
                print("Выбран файл", files_list[int(temp)-1])
                return files_list[int(temp)-1]
                break
            else:
                print('Необходимо ввести число от 1, количество попыток', 2 - i, ':')
    elif len(files_list) == 1:
        print("Наеден файл:", files_list[0])
        return files_list[0]
    else:
        print("Файлы не найдены")
        return ""

# чтение данных из файла
def get_data_from_file(file_name):
    with open(file_name, 'r', encoding="UTF-8") as f:  # Проходим по всем строкам файла проекта
        tree = ET.parse(f)
        GlobalVariables.rootTree = tree.getroot()
