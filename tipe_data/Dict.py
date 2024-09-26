# tipe data dictionary adalah tipe data mapping

# contoh pada class
# class dict(maping, **kwargs)

# dict bisa dibuat:

# 1. dengan koma = {key: value}
a = {
    "key":"value"
}
print(a)
# 2. dengan dict komprehension = {x:x**2 for x in range(70)}
a = {a:a**2 for a in range(3)}
print(a)
# 3. dengan constructor = dict(['tes',80])
print(dict([('foo',800),('bar',99),('tes',80)]))


# contoh ilustrasi

a=dict(satu=1,dua=2,tiga=3)
# contoh dict asli
b={'satu':1,'dua':2,'tiga':3}
# contoh dict dengan function zip
c=dict(zip(['satu','dua','tiga'],[1,2,3]))
# contoh dict construct
d=dict([('satu',1),('dua',2),('tiga',3)])
# 
e=dict({'satu':1,'dua':2,'tiga':3})

compare = a == b == c == d == e
print(compare) # ini akan true krn semua diatas sama

# list() mengambil key kemudian dimasukkan ke list
print(list(a))

# len() mengambil total dict
print(len(a))

# d[key] mengambil mapping dari d
print(d['dua'])

class counter(dict):
    def __mising__(self,key):
        return 0

x = counter()

# set dict
x['ada']='ada'
x['kosong'] = "ada"
print(x['kosong'])
print(x)

# hapus dict 
del x['kosong']
print(f"x: {x}")

# key in dict mengecek key ada didalam dict
makesure = 'ada' in x
print(f"key in x: {makesure}")

# key not in dict
makesure = 'kosong' not in x
print(f"not key in x: {makesure}\n")

# iter(x) mengembalikan dalam bentuk iterator yang  di ada dictionary
iterate = iter(x.keys())
for i in iterate:
    print(i)

# clear() menghapus semua isi dict
# x.clear()
# print(x)

# copy()
z = x.copy()
print(f"copy an dari x: {z}")

# classmethod fromkeys(iterable, value=none,/)
# Membuat dict baru dengan kunci dari iterable (list, tuple, set) dan nilai default atau set nilai
new_dict = dict.fromkeys(['a','b','c'], a)
print(new_dict)

# get(key, default=none) mengambil dict kalau isi salah mengembalikan default value
print(a.get(0,'null'))

# items() mengambil items dari dict
print(a.items())
# selengkapnya di dict view objek

# keys() mengembalikan kunci dari dict
print(a.keys())
   
# pop(key[,default])
a.pop('satu')