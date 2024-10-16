import re

# NAME
#     re - Support for regular expressions (RE).

filename = input("nama file: ")


with open(filename,'r',encoding='utf-8') as f:
    isi = f.read()
    print(re.findall("a.b",isi))