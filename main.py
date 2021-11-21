# словарь
elements = {"armName": "", "ethernet-adapter": "", "ethernet-adapter_1": ""}
domainElements = ("eth:ethernet-adapter", "srv:io-server")

def GetParametr (strIn):
    temp = strIn[line.find("address="): len(strIn)]
    temp = temp[temp.find("\"")+1: temp.rfind("\"")]
    print (temp)

def find_element(linefromfile):
    for i in domainElements:
        if i in linefromfile:
           if line.find("address=") != -1:
               GetParametr(line)


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
