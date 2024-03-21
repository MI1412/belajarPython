# latihan looping
sisi = int(input("masukkan sisi segitiga : "))
if sisi % 2 != 1:
    print("Masukkan angka ganjil.")
    exit()

# menggunakan for
# variabel dummy
print("menggunakan for\n")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
    
print("\nmenggunakan while\n") 
# menggunakan while
count = 1
while True:
    print("*"*count) # count akan dikali dengan * dan akan ditambahkan
    count += 1
    if count > sisi:
        break
# menggunakan segitiga sama sisi 
print("\nsegitiga sama sisi\n")
count = 1
spasi = int(sisi/2)
while True:
    if (count % 2):
        # print jika ganjil
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else:   
        # kembali keatas jika genap 
        count += 1
        continue
    # break jika count melebihi sisi
    if count > sisi:
        break
    
# segitiga sama kaki

# tugas buat belah ketupat

print("\nbelah ketupat\n")
spasi = sisi // 2
for i in range(1, sisi + 1, 2):  # Melangkah 2 untuk membuat pola ganjil
    print(" " * spasi + "*" * i)
    spasi -= 1
spasi = 1  # Kembalikan spasi ke 1 untuk bagian bawah belah ketupat
for i in range(sisi - 2, 0, -2):  # Melangkah mundur 2 untuk membuat pola ganjil
    print(" " * spasi + "*" * i)
    spasi += 1