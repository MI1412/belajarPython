# input digunakan hasil ketikan dari user
data = input("masukkan data : ")
print("output : ",data,type(data))
#hasil output berupa string

#jika ingin mengatur tipe data maka bisa dicasting secara langsung
#contoh
data_int = int(input("masukkan angka : "))
print("output : ",data_int,"tipe data : ",type(data_int))

data_float = float(input("masukkan angka : "))
print("output : ",data_float,"tipe data : ",type(data_float))

data_bool = bool(int(input("masukkan data : ")))
print("output : ",data_bool,"tipe data : ",type(data_bool))