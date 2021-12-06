import xml.etree.ElementTree as ET  # подключаем  The ElementTree XML
import CommentForXml as Comment
import xml.dom.minidom

# словарь
elements = {"element1": {"armName": "", "ethernet-adapter": "", "ethernet-adapter_1": "", "io-server": ""},
            "element2": {"armName": "", "ethernet-adapter": "", "ethernet-adapter_1": "", "io-server": ""}}


def find_element(linefunk):
    if linefunk.find("eth:ethernet-adapter") != -1:  # ищем стевой адаптер eth:ethernet-adapter
        temp_tree = ET.fromstring("<" + linefunk.split(":")[1])  # убираем eth: из eth:ethernet-adapter
        elements["element1"]["ethernet-adapter"] = temp_tree.get("address")  # записываем адрес в элемент ethernet-adapter адрес
    elif linefunk.find("dp:domain-node name=") != -1:  # ищем название домена
        temp = ("<" + linefunk.split(":")[1]).split(">")[
                   0] + "/>"  # убираем dp: из dp:domain-node name и добавляем / в конец конструкции
        temp_tree = ET.fromstring(temp)
        elements["element1"]['armName'] = temp_tree.get("address")  # записываем название в элемент armName
    elif linefunk.find("srv:io-server name") != -1:  # ищем название сервера
        temp = ("<" + linefunk.split(":")[1]).split(">")[
                   0] + "/>"  # убираем srv: из srv:io-server name и добавляем / в конец конструкции
        temp_tree = ET.fromstring(temp)
        elements["element1"]['io-server'] = temp_tree.get("name")  # записываем название в элемент armName


def gen_net_xml_str():
    data = ET.Element("Alpha.Net.Agent")
    data.set("Name", elements["element1"]['armName'])
    data.set("NetEnterPort", "1010")
    data.set("ParentAgentPort", "1020")
    ET.SubElement(data, 'Options LoggerLevel="2"')
    data.insert(0, ET.Comment(Comment.netComment1))
    data.insert(1, ET.Comment(Comment.netComment2))
    data.insert(2, ET.Comment(Comment.netComment3))
    data.insert(3, ET.Comment(Comment.netComment4))
    ET.ElementTree(data).write("test.xml", 'utf-8', xml_declaration=True)
    # ET.dump(data)
    # mydata = ET.tostring(data, 'utf-8')
    # print(mydata)

def gen_domain_xml_str():
    data = ET.Element("Alpha.Domain.Agent")
    data.set("Name", "NDA")
    EntryPointNetAgent = ET.SubElement(data, 'EntryPointNetAgent')
    EntryPointNetAgent.set("Name", "local")
    pretty_xml_as_string = xml.dom.minidom.parseString(
        ET.tostring(data, encoding='utf-8', method='xml',
                    xml_declaration=True).decode('UTF-8')).toprettyxml()  # приводим xml к "нормальному" виду
    print(pretty_xml_as_string)