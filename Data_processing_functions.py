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
    root = ET.Element("Alpha.Net.Agent")
    root.set("Name", elements["element1"]['armName'])
    root.set("NetEnterPort", "1010")
    root.set("ParentAgentPort", "1020")
    ET.SubElement(root, 'Options LoggerLevel="2"')
    root.insert(0, ET.Comment(Comment.netComment5))
    root.insert(1, ET.Comment(Comment.netComment1))
    root.insert(2, ET.Comment(Comment.netComment2))
    root.insert(3, ET.Comment(Comment.netComment3))
    root.insert(4, ET.Comment(Comment.netComment4))
    for value in Comment.listOfnetComments:
        print(value.keys())
    # ET.ElementTree(data).write("test.xml", 'utf-8', xml_declaration=True) записывает в файл значения
    pretty_xml_as_string = xml.dom.minidom.parseString(
        ET.tostring(root, encoding='utf-8', method='xml',
                    xml_declaration=True).decode('UTF-8')).toprettyxml()  # приводим xml к "нормальному" виду
    print(pretty_xml_as_string)
    with open("netxml.txt", "w") as filetowrite:
        filetowrite.write(pretty_xml_as_string)
    # ET.dump(data)
    # mydata = ET.tostring(data, 'utf-8')
    # print(mydata)


def gen_domain_xml_str():
    # root
    root = ET.Element("Alpha.Domain.Agent")
    root.set("Name", "NDA")

    #root-EntryPointNetAgent
    root_entryPointNetAgent = ET.SubElement(root, 'EntryPointNetAgent')
    root_entryPointNetAgent.set("Name", "local")
    root_entryPointNetAgent.set("Address", "127.0.0.1")
    root_entryPointNetAgent.set("Port", "1010")

    # root-InstalledComponents
    root_installedComponents = ET.SubElement(root, 'InstalledComponents')

    # root-InstalledComponents-AlphaServer
    root_installedComponents_alphaServer = ET.SubElement(root_installedComponents, 'Alpha.Server')  # пареметр Alpah.Server в EntryPointNetAgent
    root_installedComponents_alphaServer.set("Name", "Server_1")
    root_installedComponents_alphaServer.set("ServiceName", "Alpha.Server")
    root_installedComponents_alphaServer.set("DefaultActivation", "1")

    # root-Server
    root_server = ET.SubElement(root, 'Server')

    # root-Server-Components
    root_server_components = ET.SubElement(root_server, 'Components')
    root_server_components.set("StoragePath", "c:\DomainStorage\cache\server")

    # root-Server-Components-Component
    root_server_components_component = ET.SubElement(root_server_components, 'Component')
    root_server_components_component.set("InstalledName", "Server_1")
    root_server_components_component.set("Name", "Server")

    # root-Options
    root_options = ET.SubElement(root, 'Options')
    root_options.set("LoggerLevel", "2")

    # приведение к нормальному виду xml
    pretty_xml_as_string = xml.dom.minidom.parseString(
        ET.tostring(root, encoding='utf-8', method='xml',
                    xml_declaration=True).decode('UTF-8')).toprettyxml()  # приводим xml к "нормальному" виду
    print(pretty_xml_as_string)
    with open("domainxml.txt", "w") as filetowrite:
        filetowrite.write(pretty_xml_as_string)