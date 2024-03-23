# nested list adalah sebuah list bersarang
data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")

list_2d = [data_0,data_1]
print(f"ini adalah list 2d = {list_2d}")

# contoh penggunaan 
peserta0 = ["ucup",20,"laki laki"]
peserta1 = ["nina",19,"perempuan"]
peserta2 = ["otong",18,"laki laki"]

list_peserta = [peserta0,peserta1,peserta2]
print(f"peserta = {list_peserta}\n")

for peserta in list_peserta:
    print(f"nama : {peserta[0]}")
    print(f"umur : {peserta[1]}")
    print(f"jenis kelamin : \n{peserta[2]}\n")
    
# tetapi ada masalah pada reference
list_copy = list_peserta.copy()
print(f"peserta : {list_copy}")

peserta[0] = "mort"
print(f"peserta : {list_copy}")