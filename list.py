# list dipython adalah sebuah kumpulan data yang dikumpulkan menjadi satu variabel
# di python tidak ada yang namanya array atau bisa disebut list
# contoh

# angka
angka = [1,2,3,4,5]
print(angka[1]) # menampilkan indeks ke 1 adalah 2

# string
name = ["imron","musa","ammar","mama"]
print(name[1]) # menampilkan indeks ke 1 adalah 2

# boolean
boolean = [True,False]
print(boolean[0]) # menampilkan indeks ke 0 adalah true

# data campuran
data = ["imron",13,True]
print(data[0])

# cara alternatif membuat list

data_range = range(0,10,2) # range(start,end,method)
print(data_range)
data_list = list(data_range)
print(data_list[2])

# membuat list dengan for loop, list comprehension

data_list_for = [i**2 for i in range(0,10)] # **2 adalah untuk pangkat
print(data_list_for)

# membuat list pakai for dan if

list_for_if = [i for i in range(0,10) if i != 5]
print(list_for_if)


