# file = open("workfile.txt","r",encoding="utf-8")

# praktek terbaik menggunakan with dengan open
# catatan untuk membuka dan membaca file gambar dan aplikasi membutuhkan mode binary
file = open("workfile.txt","r",encoding="utf-8") # input
def baca():
    with file as f:
        # print(f"dibaca semua : \t{f.read()}")
        # catatan file ini hanya bisa satu kali baca jika sudah terbaca maka tidak bisa menggunakan output lagi, krn sudah terbaca duluan
            # print(f"dibaca perbaris : {f.readline()}")
            
            # bisa membaca baris file dengan di loop
            # for lines in f:
            #     print(lines,end=" \n")
            
            # membaca isi file dalam bentuk list
        print(list(f))
    
baca()
# menutup file otomatis
file = open("workfile.txt","r",encoding="utf-8") 
def ditutup():
    with file as f:
        pass
    print(f"ditutup ?: {f.closed}")
ditutup()

# kenapa bisa ketutup sendiri padahal tidak memanggil f.close()

# Warning
# Calling f.write() without using the with keyword or calling f.close() might result in the arguments of f.write() not being completely written to the disk, even if the program exits successfully.

# looping dengan for in
with open("workfile.txt","r",encoding="utf-8") as f:
    for line in f:
        print("\nfor in:")
        print(line, end=" ")
        # untuk membaca semua isi file bisa pakai list() atau f.readlines()

# menghitung panjang huruf
with open("workfile.txt","w",encoding="utf-8") as f:
    tulis = f.write("hai dev")
    tell = f.tell()
    print(f"\ntulis: {tulis}huruf \ntell:{tell} huruf") # mengembalikan nilai huruf diketik


# mengatur posisi file yang akan dibaca atau ditulis
f = open("bin.txt","rb+")
print(f.write(b"0123456789abcdef"))
print(f.seek(0)) # pindah kursor ke baris 15
print(f.read(1)) # membaca kursor
# whence default = 0 hitung kursor saat ini, 1 setelah kursor, 2 akhir dari file
print(f.seek(5,1))
print(f.read(1)) # membaca kursor
print(f.seek(17))
print(f.write(b"hai"))
print(f"tell: {f.tell()}")
print(f.seek(19))
print(f.read(1))

print(f"truncate: {f.truncate()}")
print(f"isatty: {f.isatty()}")