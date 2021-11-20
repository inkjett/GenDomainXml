""""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
"""
# словарь
elements = {"armName": "", "ethernet_adapter_1": ""}

# чтение файла open_file.txt
with open("open_file.txt", 'r', encoding="UTF-8") as f:
    while 8:
        line = f.readline()
        if not line:
            break
        if "<dp:domain-node" in line:
            while "</dp:domain-node" not in line:
                print(line)
                line = f.readline()
            print(line)