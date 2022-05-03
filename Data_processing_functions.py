import xml.etree.ElementTree as ET  # подключаем The ElementTree XML
import CommentForXml as Comment
import xml.dom.minidom
import GlobalVariables as GV



# словарь
elements = {"element1": {"armName": "", "ethernet-adapter": "", "ethernet-adapter_1": "", "io-server": ""},
            "element2": {"armName": "", "ethernet-adapter": "", "ethernet-adapter_1": "", "io-server": ""}}




def gen_net_xml_str():
    # root
    root = ET.Element("Alpha.Net.Agent")
    root.set("Name", elements["element1"]['armName'])
    root.set("NetEnterPort", "1010")
    root.set("ParentAgentPort", "1020")

    # root.Options
    ET.SubElement(root, 'Options LoggerLevel="2"')

    for index, value in enumerate(
            Comment.listOfnetComments):  # циклом проходим по списку комментариев и добавляем их в xml
        root.insert(index, ET.Comment(value))
    pretty_xml_as_string = xml.dom.minidom.parseString(
        ET.tostring(root, encoding='utf-8', method='xml',
                    xml_declaration=True).decode('UTF-8')).toprettyxml()  # приводим xml к "нормальному" виду
    GV.net_pretty_xml = pretty_xml_as_string


def gen_domain_xml_str_1():
    # root
    root = ET.Element("Alpha.Domain.Agent")
    root.set("Name", "NDA")
    root.insert(0, ET.Comment(Comment.domaincomment1))

    # root.EntryPointNetAgent
    root_entryPointNetAgent = ET.SubElement(root, 'EntryPointNetAgent')
    root_entryPointNetAgent.set("Name", "local")
    root_entryPointNetAgent.set("Address", "127.0.0.1")
    root_entryPointNetAgent.set("Port", "1010")
    root_entryPointNetAgent.insert(0, ET.Comment(Comment.domaincomment2))

    # root.InstalledComponents
    root_installedComponents = ET.SubElement(root, 'InstalledComponents')

    # root.InstalledComponents.AlphaServer
    root_installedComponents_alphaServer = ET.SubElement(root_installedComponents,
                                                         'Alpha.Server')  # пареметр Alpah.Server в EntryPointNetAgent
    root_installedComponents_alphaServer.set("Name", "Server_1")
    root_installedComponents_alphaServer.set("ServiceName", "Alpha.Server")
    root_installedComponents_alphaServer.set("DefaultActivation", "1")

    # root.Server
    root_server = ET.SubElement(root, 'Server')
    root_server.insert(0, ET.Comment(Comment.domaincomment3))
    root_server.insert(1, ET.Comment(Comment.domaincomment4))

    # root.Server.Components
    root_server_components = ET.SubElement(root_server, 'Components')

    root_server_components.set("StoragePath", "c:\DomainStorage\cache\server")
    root_server_components.insert(0, ET.Comment(Comment.domaincomment5))

    # root.Server.Components.Component
    root_server_components_component = ET.SubElement(root_server_components, 'Component')
    root_server_components_component.set("InstalledName", "Server_1")
    root_server_components_component.set("Name", elements["element1"]["io-server"])
    root_server_components_component.insert(0, ET.Comment(Comment.domaincomment6))

    # root.Options
    root_options = ET.SubElement(root, 'Options')
    root_options.set("LoggerLevel", "2")
    root_options.insert(0, ET.Comment(Comment.domaincomment7))
    root_options.insert(1, ET.Comment(Comment.domaincomment8))

    # приведение к нормальному виду xml
    pretty_xml_as_string = xml.dom.minidom.parseString(
        ET.tostring(root, encoding='utf-8', method='xml',
                    xml_declaration=True).decode('UTF-8')).toprettyxml()  # приводим xml к "нормальному" виду
    GV.domain_pretty_xml = pretty_xml_as_string
    print("domainFileGentrated")


def gen_domain_xml_str():
    domain_address = ""
    # get_data_from_Tree(GV.rootTree)
    for i in GV.rootTree:  # проходим по всему дереву
        if i.tag == "{automation.deployment}domain": # ищем тег с названием домена
            GV.domain_Name = i.get("name") # ищем имя домена
            get_data_from_Tree(i.get("address"), i) # вызываем рекурсивную функицю по поиску нужных эелементов
            GV.domain_exemplar_dict[GV.domain_Name] = {
                GV.domain_Name: {'domain_address': GV.domain_address, 'ethernet_address': GV.ethernet_address, 'server_name': GV.server_name}} # добавляем в словрь новую строку
    # for i in GV.domain_exemplar_dict.keys():  # просмотр эелемнтов словаря
    #     print(GV.domain_exemplar_dict[i].items())
    # for child in GV.rootTree:
    #     print(child.tag, "=", child.attrib)
    #     #print(child.get("domain"), "=", child.get('address'))
        #print(root[0].text)


def get_data_from_Tree(_domain_address, value_in):
    GV.domain_address = _domain_address
    for x in value_in:
        if x.tag == "{automation.deployment}domain-node":
            # print("ARM=", x.get("address"))
            GV.ARM = x.get("address")
        if x.tag == "{automation.ethernet}ethernet-adapter":
            # print("addressEthernet=", x.get("address"))
            GV.ethernet_address = x.get("address")
        if x.tag == "{server}io-server":
            # print("nameServer=", x.get("name"))
            GV.server_name = x.get("name")
        get_data_from_Tree(_domain_address, x)

def select_domain():
    domain_len = len(GV.domain_exemplar_dict)
    print(domain_len)
    # dict - {ключ: значение}
    if domain_len > 1:
        print("Необходимо выбрать Домен для генерации xml файлов \nДоступные домены:")
        for i in GV.domain_exemplar_dict:
            print(list(GV.domain_exemplar_dict.keys()).index(i)+1, i)
        # for count, i in enumerate(GV.domain_exemplar_dict):  # i - ключи словаря GV.domain_exemplar_dict, выводим
        #     # наеденые домены
        #     print(count+1, i)
