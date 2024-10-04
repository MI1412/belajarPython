# Agregasi adalah hubungan "memiliki" antara dua kelas di mana satu kelas dapat berisi objek dari kelas lain, tetapi objek tersebut dapat eksis secara independen dari kelas yang memilikinya.

# contoh

class Buku:
    def __init__(self, judul):
        self.judul = judul

class Perpustakaan:
    def __init__(self):
        self.buku_list = []  # Daftar untuk menyimpan buku

    def tambah_buku(self, buku):
        self.buku_list.append(buku)  # Menambahkan buku ke daftar

# Penggunaan
buku1 = Buku("Belajar Python")
buku2 = Buku("Belajar Java")

perpustakaan = Perpustakaan()
perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)

# Menampilkan daftar buku
for buku in perpustakaan.buku_list:
    print(buku.judul,type(buku))

