# manipulasi string
# 1. menyambung string (concatenate)
# menggunakan operator +
data = "ini"
nama_tengah = "penyambungan"
nama_akhir = "string"

nama_lengkap = data +" "+ nama_tengah +" "+ nama_akhir
print("\n",nama_lengkap)

# 2. menghitung panjang string menggunakan sintaks len (lenght)
panjang = len(nama_lengkap)
print("panjang string :",panjang)

# 3. operator untuk string
# mengecek komponen char atau teks didalam string menggunakan sintaks in
check = "str"
status = check in nama_lengkap
print(check,"ada di",nama_lengkap,"=\n",status)

# memakai not
check = "str"
status = check not in nama_lengkap
print(check,"ada di",nama_lengkap,"=\n",status,"\n")

# mengulang string
print("wk"*10)

# indexing
print("\nindeks ke-0 :",nama_lengkap[0])
print("\nindeks ke-9 :",nama_lengkap[9])
print("\nindeks ke 0-9 :",nama_lengkap[0:9],)
print("\nindeks ke 10-23 :",nama_lengkap[10:23])
print("\nindeks ke 0,2,4,6,8,10 :",nama_lengkap[0:10:2])

# pengurutan string
print("\npaling kecil :",min(nama_lengkap))
print("paling besar :",max(nama_lengkap))

spasi = ord(" ")
print("spasi untuk abc adalah", str(spasi))

data = 119
print("char untuk abc 119 adalah", chr(data))

# method built in string
data = "imron"
jumlah = data.count("o")
print("jumlah o :",jumlah)