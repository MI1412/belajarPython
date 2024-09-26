# macam macam kumpulan nilai
# list, tuple, set, dictionary
contoh_list = []
contoh_tuple = () # tuple bersifat immutable
contoh_set = {}
contoh_dictionary = {'a':10}

# <--lists
# di python tidak ada yang namanya array tapi disebut list

contoh = [1,5,7,8,9] #<-- ini list
print(contoh)
print(contoh[0]) # akses index secara langsung
print(contoh[1:4]) # akses index list
print(contoh[2:5])

contoh2 = [90,11,12,546,42] + contoh # list sebelumnya akan digabung
print(contoh2)

contoh2.append(90) # menambahkan list baru
contoh2.append(90 ** 4) # menambahkan list baru
print(contoh2)

rgb = ["red","green","blue"]
rgba = rgb
print(id(rgb) == id(rgba)) # id() = id dari variabel
rgba.append("alph")
print(rgba)
print(rgb)

correct_rgba = rgba[:] # inisiasi membuat list kosong
correct_rgba[-1] = "alpha"
print(correct_rgba)
print(rgba)
# <--built function

# len()
print(len(contoh))
print(len(contoh2))

# replace and remove
contoh[0:3] = ["i","n","i"," ","direplace"]
print(contoh)

contoh[2]="dihapus"
contoh[4]="dihapus"
print(contoh)

# set list kosong
contoh[:]=[]
print(contoh)

# <--list list bercabang
a = [1,2,4,5]
b = ["p","a","d","d"]
x = [[12,45,6,12], [True, False]]

print(x[1][1], x[0][1])

# <--collection
a = {
    "p":10,
    "lol":100100
}

print(a)

list_arr = (10,212,242,12,4,1,2,5)
print(list_arr)