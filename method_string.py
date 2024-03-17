# method string 
# 1. merubah ukuran huruf semua
data = "Halo Imron"
print("\nhuruf normal :",data)
# besar
data = data.upper()
print("huruf yang sudah diuppercase :",data)

# kecil
data = data.lower()
print("huruf yang sudah dilowercase :",data)

# 2. pengecekan 
# huruf kecil
data = "imron"
print("\ndata :",data)
data = data.islower()
print("imron huruf kecil semua :",data) 

# huruf besar
name = "IMRON"
print("\ndata :",data)
data = name.isupper()
print(name,"huruf besar semua :",data)

# isalpha() mengecek semua teks apakah ada hurufnya
name = "imron"
data = name.isalpha()
print(name,"ada didalam string :",data)
# isalnum() mengecek semua teks apakah ada angkanya
angka = "10"
data = angka.isalnum()
print(angka,"ada didalam string :",data)

# isdecimal() mengecek angka saja
data = angka.isdecimal()
print(angka,"ada didalam string :",data)

# isspace() mengecek apakah ada spasi di string
spasi = "halo imron"
data = spasi.isspace()
print(spasi,"ada spasi didalam :",data)

# istittle() mengecek semua kata dimulai huruf besar
tittle = "Imron"
data = tittle.istitle()
print(tittle,"apakah ini judul :",data)

# mengecek komponen startswith() dan endswith()
cek = "halo imron".startswith('halo')
print("start halo =",cek)

cek = "halo imron".endswith('imron')
print("end imron =",cek)

# penggabungan komponen string join(), split()
# gabung join()
pisah = ["imron","musa","ammar","mama"]
merge = ' '.join(pisah)
print(pisah)
print(merge)

# pisah split()
data = "halo imron"
print(data.split(' '))

# penempatan karakter string rjust(), ljust, center()
kanan = "kanan".rjust(10,"-")
print("----",kanan,"----")

kiri = "kiri".ljust(10,"-")
print("----",kiri,"----")

tengah = "tengah".center(10,"-")
print("----",tengah,"----")

# kebalikannya strip() untuk menghapus argumen method string
tengah = tengah.strip("-")
print("----",tengah,"----")