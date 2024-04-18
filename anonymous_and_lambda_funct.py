
def kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat 7 = {kuadrat(7)}")


# lambda function
# output = lambda argumen : expression
kuadrat = lambda angka:angka**2
print(f"hasil kuadrat memakai lambda = {kuadrat(9)}")

pangkat = lambda num,pow : num**pow
print(f"hasil 2 input lambda berpangkat = {pangkat(2,4)}")

# fungsi lambda :
# 1. sorting list menurut alphabet
# general
data_list = ['imron','musa','amir']
data_list.sort()
print(f'\nlist disorted = {data_list}')

# memakai sort list panjang huruf
def panjang_list(nama):
    return len(nama)
data_list.sort(key=panjang_list)
print(f"\nsorted list dengan len = {data_list}")

# sort pakai lambda
data_list = ['imron','musa','amir']
data_list.sort(key=lambda nama:len(nama))
print(f"\nsorted list len dgn lambda = {data_list}")

# filter
data_angka = [1,2,4,5,6,7,8,9,0]
def kurang_dari_lima(angka):
    return angka < 5
data_angka_baru = list(filter(lambda x:x<7,data_angka))
print(f"angka difilter kurang dari 7 {data_angka_baru}")
# genap
data_genap = list(filter(lambda x:(x%2 == 0),data_angka))
print(f"\ndata genap : {data_genap}")

# ganjil
data_ganjil = list(filter(lambda x:(x%2 == 1),data_angka))
print(f"\ndata ganjil : {data_ganjil}")

# kelipatan 3
kelipatan_3 = list(filter(lambda x:(x%3 == 0),data_angka))
print(f"\nkelipatan tiga : {kelipatan_3}")

# anonymus funct 
# currying <- haskell curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f'\nfungsi biasa : {data_hasil}')

# dengan currying
def pangkat(n):
    return lambda angka:angka**n
print(f"pangkat dengan anonymus funct : {pangkat(2)(3)}") # pangkat(param pangkat) (angka)