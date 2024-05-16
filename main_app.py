import numpy as np

# kalau mengimport nama file tidak boleh sesuai dengan nama module yang diimport
# contoh menampilkan module numpy
# print(numpy)

# membuat matrix
list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

# jika diprint
print(f'ini list a : {list_a}') # yang list ada pemisah koma
print(list_a*2) # kalau list dikali 2 bukan menghitung tetapi mengkali jumlah list lagi / bisa disebut menambah list yang sama 
# print(list_a**2) ini tidak bisa di kuadratkan
print(f'ini array a : {vector_a}') # array tidak ada pemisah array
print(f"ini array a dikuadrat : {vector_a**2}") # ini bisa dikuadratkan
print(f'ini array a dikali 5 : {vector_a*5}') # ini akan mengkali 5 di jumlah array

matrix_b = np.array([(1,2),(3,4)])
print(f"ini matrix b : \n{matrix_b}")
print(f"ini matrix b kuadrat : \n{matrix_b**2}")
print(f"ini matrix b dikali 5: \n{matrix_b*5}")


#  membuat matrix kosong dengan format 2 x 2 
zeroes_c = np.zeros((2,2))
print(f'ini adalah zeroes c : \n{zeroes_c}')

#  membuat matrix 1 dengan format 2x2
ones_d = np.ones((2,2))
print(f'ini adalah ones d : \n{ones_d}')

jumlah = matrix_b + matrix_b**2 + ones_d
print(f'\njumlah : \n{jumlah}')

