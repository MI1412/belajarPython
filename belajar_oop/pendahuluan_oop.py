# oop dalam programming itu bagus untuk membuat program lebih mudah
# konsep oop
'''
1. abstraksi yaitu menggambarkan suatu objek secara biasa
2. pembungkusan / ruang lingkup yaitu suatu objek yang ditempatkan di ruang lingkup tertentu
3. pewarisan yaitu penurunan sifat program dari class induknya ke sub class lainnya / anak anaknya

'''

# contoh : 
# class adalah template atau bisa disebut cetak biru sebelum membuat objek
class hero:
    pass

# ini adalah object
hero1 = hero()
hero2 = hero()

hero1.nama = 'imron'
hero1.stat = 'pelajar'

hero2.nama = 'musa'
hero2.stat = 'pelajar'


print(hero1.__dict__) # menampilkan isi objek dari hero 1
print(hero1.nama)