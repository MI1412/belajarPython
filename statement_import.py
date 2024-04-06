# import digunakan untuk mengambil library atau packages dari luar
# fungsi import digunakan untuk mengambil program dari eksternal .py
# import juga bisa digunakan untuk memecah kode

# 1. untuk menyambung program
import program_print

# 2. import dengan data
import variabel


# data ada di namespace variabel
print(variabel.name) # variabel.name (.) adalah namespace variabel

# 3. import dengan funct
import funct_mtk
hasil = funct_mtk.operasimtk(4,5)
print(f"hasil {hasil}")