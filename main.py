import xml.etree.ElementTree as ET  # подключаем  The ElementTree XML

# словарь
elements = {"armName": "", "ethernet-adapter": "", "ethernet-adapter_1": ""}
domainElements = ("eth:ethernet-adapter", "srv:io-server", "dp:domain-node name=")


def find_element(linefunk):
    if linefunk.find("eth:ethernet-adapter") != -1:  # ищем стевой адаптер eth:ethernet-adapter
        temp_tree = ET.fromstring("<" + linefunk.split(":")[1])  # убираем eth: из eth:ethernet-adapter
        elements["ethernet-adapter"] = temp_tree.get("address")  # записываем адрес в элемент ethernet-adapter адрес
        print(elements["ethernet-adapter"])
    elif linefunk.find("dp:domain-node name=") != -1:  # ищем стевой адаптер dp:domain-node name=
        temp = ("<" + linefunk.split(":")[1]).split(">")[
                   0] + "/>"  # убираем dp: из dp:domain-node name и добавляем / в конец конструкции
        temp_tree = ET.fromstring(temp)
        elements['armName'] = temp_tree.get("address")  # записываем название в элемент armName
        print(elements["armName"])


# чтение файла open_file.txt
with open("open_file.txt", 'r', encoding="UTF-8") as f:  # Проходим по всем строкам файла проекта
    while 8:  # бесконечный цикл
        line = f.readline()  # записываем в переменную line каждую строку из файла
        if not line:  # если стрки кончились выходим из цикла
            break
        if "<dp:domain-node" in line:  # ищем начало домена
            while "</dp:domain-node" not in line:  # пока нет закрывающей конструкции </dp:domain-node выполняем поиск элементов
                find_element(line)  # функция поиск эелемнта
                line = f.readline()  # с ледующая линия в рамках dp:domain-node
            print("all_done")
