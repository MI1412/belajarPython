# tipe data string

# catatan : dunder dalam python artinya double underscore
# digunakan untuk memperkaya kelas dalam python
# contoh :
# ini akan error
# class Gasupportlen:
#     pass
# obj = Gasupportlen()
# len(obj)
# untuk memperbaiki kode diatas bisa menggunakan dunder method untuk mengisi class / wadah, contoh :
class Lensupport:
    def __len__(self):
        return 1
obj = Lensupport()
print(len(obj))

# melihat isi method dalam string
# print(dir(str))

# cara menggunakan string
# help(str)

data_str = 'yayaya'

# 1. add string
add_string = data_str.__add__('tes')
print(f"\nini dari method add {add_string}")

# memberikan nilai boolean
# contains
content = data_str.__contains__('z')
print(f'\nini dari method contains {content}')

# mengembalikan nilai objek string jika ada string sesuai true jika tidak sesuai dengan string faslse, dan jika kalau tidak sesuai tipe data mengembalikan nilai notImplement
# 2. eq
eq = data_str.__eq__(data_str)
print(f'\nini dari method eq input {data_str} : {eq}')
eq = data_str.__eq__('tes')
print(f'ini dari method eq input tes : {eq}')
eq = data_str.__eq__(1)
print(f'ini dari method eq input 1 : {eq}\n')

# 3. __format__
format_str = data_str.__format__('>10') # <--- ini adalah untuk format string yang memberikan jarak 10 baris metode ini jarang dilakukan karena lebih baik menggunakn F-string / format() karena proses ini bekerja dibalik layar 
print(f'ini dari method __format__ {format_str}')

# __ge__ juga sama seperti eq tapi yang membedakan adalah method __ge__ digunakan untuk perbandingan string memberi nilai boolean jumlah dari string
# __ge__digunakan untuk membandingkan urutan string
# jika tipe data tidak sesuai maka akan mengembalikan nilai notImplement
# 3. __ge__
ge = data_str.__ge__('10')
print(f'\nini dari method __ge__ input 10 {ge}')
ge = data_str.__ge__('yayayyayaya')
print(f'ini dari method __ge__ input 1 {ge}')
ge = data_str.__ge__(10)
print(f'ini dari method __ge__ input int(10) {ge}')
# __ge__ juga sama seperti operator perbandingan yang lain tapi yang membedakan disini adalah __ge__ menggunakan perbandingan objek string1 dengan objek string2, lihat contoh dibawah 
data_str2 = 'zzzzzzz'
hasil_banding = data_str >= data_str2
print(f"ini hasil banding {data_str} dengan {data_str2} : {hasil_banding}\n")

# untuk menggunakan getattribute string biasa itu tidak perlu karena sudah secara otomatis ditangani dibalik layar 
# 4. getattribute bisa digunakan dalam class
# contoh
class string(str):
    
    # __getattribute__ bisa digunakan untuk logging atau debug, memberi akses kontrol, dan virtual attribute
    # ini mengambil attribute dari super class str
    def __getattribute__(self,name):
        print(f'akses attribute : {name}')
        return super().__getattribute__(name)
objek_string = string(data_str)    
print(f"ini dari objek class string {objek_string.upper()}, tipe {type(objek_string)}\n")

# get item digunakan untuk mengambil suatu item dalam string, indeks awal dimulai dari 0
# 5. __getitem__
get_item = data_str.__getitem__(5)
print(f'ini dari method get_item : {get_item}\n')


# 6. __getnewargs__ mengembalikan dalam tipe tuple
getnewargs = data_str.__getnewargs__()
print(f'ini dari method getnewargs : {getnewargs}')

# so kesimpulan yang ku dapat dari belajar ini adalah Dunder method / double under method itu digunakan untuk menambahkan suatu fungsi kedalam class tersebut
# ada 34 Dunder method pada tipe data string
# ada 47 method dalam tipe data string
