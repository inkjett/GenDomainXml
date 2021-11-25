import xml.dom.minidom
import json
# словарь
elements = {"armName": "", "ethernet-adapter": "", "ethernet-adapter_1": ""}
domainElements = ("eth:ethernet-adapter", "srv:io-server", "dp:domain-node name=")


def find_element(line):
    if line.find("ethernet-adapter") != -1:
        print(line)
        dom = xml.dom.minidom.parseString("<" + line.split(":")[1])
        #dom.normalize()
        print(json.dumps(dom.__dict__) )
        print(dom.getElementsByTagName("name"))
        #elements["ethernet-adapter"] = temp
        #print(elements["ethernet-adapter"])
    """elif line.find("domain-node name=") != -1:
        temp = line[line.find("address="): len(line)]
        temp = temp[temp.find("\"") + 1: temp.rfind("\"")]
        elements["armName"] = temp
        print(elements["armName"])"""


# чтение файла open_file.txt
with open("open_file.txt", 'r', encoding="UTF-8") as f:
    while 8:
        line = f.readline()
        if not line:
            break
        if "<dp:domain-node" in line:
            while "</dp:domain-node" not in line:
                find_element(line)
                line = f.readline()
            print("all_done")
