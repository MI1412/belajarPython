# menggunakan items() !!!!
bio = {'nama':'pppp','hobi':'game'}
for k,v in bio.items():
    print(k,v)

# menggunakan enumerate() !!!!pelajari enumerate() funct
for i,v in enumerate((1,2,3)):
    print(f"i:{i} v:{v}")
    
print('\n')
for i,v in enumerate(('t','e','s')):
    print(i,v)

# untuk mengulangi dari dua iterable secara bersamaan bisa menggunakan zip !!!!
key = ['nama','alamat','hobi']
value = ['peltod','SBY','tes']
print('\n')
for k,v in zip(key,value):
    print(f"key({k}) {v}")

# untuk mengulang urutan secara terbalik bisa menggunakan reversed() !!!!
urutan = [10,9,2,1,8,7,6,5,4,3]
for i in reversed(urutan):
    print(i)
print('\n')
# untuk mengurutkan gunakan sorted() !!!!
for i in sorted(urutan):
    print(i)
    
# untuk mengurutkan dan menghilangkan elemen duplikat bisa menggunakan set()

print('\n')
c = urutan + [1,2,3,4,5,6,7]
print(f'c: {c}')
for i in set(c):
    print(f"set: {i}")

# terkadang ingin mengubah list saat looping itu lebih mudah tetapi lebih aman lagi membuat list baru

import math
baris_data = [8.2,float('NaN'),19.11,float('NaN'),90.9,53.6]
data_filter = []
for value in baris_data:
    if not math.isnan(value):
        data_filter.append(value) # menyimpan baris_data di list baru

print(f"data filter: {data_filter}")
print(baris_data)