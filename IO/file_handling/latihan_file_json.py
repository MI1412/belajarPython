import json
data_json = [1,'tdx',10]
print(json.dumps(data_json)) # print data json
file = open('workfile.txt', mode='w', encoding="utf-8")
x = json.load(file)
print(x)