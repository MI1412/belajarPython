# 1. mode menulis file
    # mode write akan membuat file baru jika belum ada
    # ketika ada file yang sama menulis yang baru akan overwrite teks yang ditulis
    
# with open("data_1.txt",mode='w',encoding='utf-8') as file:
#     file.write('ppppp\n')

# 2. mode append menambahkan teks baru tanpa menimpa

with open("data_2.txt",mode='w',encoding='utf-8') as file:
    # file.write('ini ditulis dengan mode append\n')
    file.write('mode append itu adalah "a"')
    
# 3. mode r+ akan menimpa teks jika ada file yang sama
with open("data_1.txt",'r+',encoding='utf-8') as file:
    file.write("menambah dengan r+\n")
    file.write('halo')

with open("data_1.txt",'r+',encoding='utf-8') as file:
    file.write('hehehhha') # akan menimpa sesuai panjang teks yang diberi
    
with open("data_1.txt","r+",encoding='utf-8') as file:
    data = file.read()
    print(data)


