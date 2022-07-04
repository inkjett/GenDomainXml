import Data_processing_functions as DP_funk
import os as files
import xml.etree.ElementTree as ET  # подключаем The ElementTree XML
import GlobalVariables
import os


def get_data_from_file_1(file_name):  # чтение данных из файла
    with open(file_name, 'r', encoding="UTF-8") as f:  # Проходим по всем строкам файла проекта
        while 8:  # бесконечный цикл
            line = f.readline()  # записываем в переменную line каждую строку из файла
            if not line:  # если стрки кончились выходим из цикла
                break
            if " <dp:domain name=" in line:  # ищем начало домена
                while "</dp:domain>" not in line:  # пока нет закрывающей конструкции </dp:domain> выполняем поиск элементов
                    DP_funk.find_element(line)  # функция поиск эелемнта
                    line = f.readline()  # с ледующая линия в рамках dp:domain-node
                print("all_done")


def save_data_to_file(fileName, textSave):  # запись данных в файл
    with open(fileName, "w") as filetowrite:
        filetowrite.write(textSave)


def get_file_name():
    current_dir = os.getcwd()  # получаем каталог, где запускается скрипт
    files_in_dir = os.listdir(current_dir)
    for f in files_in_dir:
        if ".omx" in f:
            print(f)


def get_data_from_file(file_name):  # чтение данных из файла
    with open(file_name, 'r', encoding="UTF-8") as f:  # Проходим по всем строкам файла проекта
        tree = ET.parse(f)
        GlobalVariables.rootTree = tree.getroot()
