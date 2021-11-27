import Data_processing_functions as DP_funk

def getDataFromFile(FileName):
    # чтение файла open_file.txt
    with open(FileName, 'r', encoding="UTF-8") as f:  # Проходим по всем строкам файла проекта
        while 8:  # бесконечный цикл
            line = f.readline()  # записываем в переменную line каждую строку из файла
            if not line:  # если стрки кончились выходим из цикла
                break
            if "<dp:domain-node" in line:  # ищем начало домена
                while "</dp:domain-node" not in line:  # пока нет закрывающей конструкции </dp:domain-node выполняем поиск элементов
                    DP_funk.find_element(line)  # функция поиск эелемнта
                    line = f.readline()  # с ледующая линия в рамках dp:domain-node
                print("all_done")


