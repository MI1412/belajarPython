# contoh = list()
# # menampilkan isi list
# print(dir(contoh))

# contoh = []
# angka = [2,4,6,7,8,9]
# # menambahkan angka ke dalam list
# angka.append(90)
# angka.append(50)
# print(f"\nangka dari list {angka}")

# # akses indeks 
# print(f'indeks dari angka ke 1 : {angka[1]}')

# # jika mengakses indeks adlah negatif maka python akan menghitung list dari belakang ke depan
# print(f'ini indeks negatif -1 : {angka[-1]}')

# # slicing
# # mirip seperti looping
# print(f'contoh dari slicing dari indeks 1 - 5 : {angka[1:5]}')

# contoh = [124,'yayaya',True,7.88,[51,False]]

# rolls = [4,1,8,5,1,2,4,5]

numbers = [1,2,3]

letters = ['a','b','c']

# adds = numbers + letters 
# print(f'contoh penambahan list menggunakan + : {adds}')

# concatenation
isi_list = dir(numbers)

print(f'isi list angka {isi_list}')
isi_list = dir(letters)
print(f'\nisi list huruf : {isi_list}')

# untuk menggunakan salah satu method dari list cukup ketik help()
help(numbers.reverse)
