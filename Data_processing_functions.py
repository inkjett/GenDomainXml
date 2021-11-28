import xml.etree.ElementTree as ET  # подключаем  The ElementTree XML

# словарь
elements = {"element1": {"armName": "", "ethernet-adapter": "", "ethernet-adapter_1": "", "io-server": ""},
            "element2": {"armName": "", "ethernet-adapter": "", "ethernet-adapter_1": "", "io-server": ""}}


def find_element(linefunk):
    if linefunk.find("eth:ethernet-adapter") != -1:  # ищем стевой адаптер eth:ethernet-adapter
        temp_tree = ET.fromstring("<" + linefunk.split(":")[1])  # убираем eth: из eth:ethernet-adapter
        elements["element1"]["ethernet-adapter"] = temp_tree.get("address")  # записываем адрес в элемент ethernet-adapter адрес
        #print(elements["ethernet-adapter"])
    elif linefunk.find("dp:domain-node name=") != -1:  # ищем название домена
        temp = ("<" + linefunk.split(":")[1]).split(">")[
                   0] + "/>"  # убираем dp: из dp:domain-node name и добавляем / в конец конструкции
        temp_tree = ET.fromstring(temp)
        elements["element1"]['armName'] = temp_tree.get("address")  # записываем название в элемент armName
        #print(elements["armName"])
    elif linefunk.find("srv:io-server name") != -1:  # ищем название сервера
        temp = ("<" + linefunk.split(":")[1]).split(">")[
                   0] + "/>"  # убираем srv: из srv:io-server name и добавляем / в конец конструкции
        temp_tree = ET.fromstring(temp)
        elements["element1"]['io-server'] = temp_tree.get("name")  # записываем название в элемент armName
        #print(elements["io-server"])

def GenNetXMLStr():
    data = ET.Element("Alpha.Net.Agent")
    data.set("Name", elements["element1"]['armName'])
    data.set("NetEnterPort", "1010")
    data.set("ParentAgentPort", "1020")
    data.
    item1 = ET.Elemnt(data, '<Options LoggerLevel="2"/>')
    mydata = ET.tostring(data)
    print(mydata)