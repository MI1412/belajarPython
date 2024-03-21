# latihan looping
sisi = int(input("masukkan sisi segitiga : "))

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
# menggunakan segitiga ganjil 
print("\nsegitiga ganjil\n")
count = 1
spasi = int(sisi/2)
while True:
    if (count % 2):
        # print jika ganjil
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else:   
        # kembali keatas jika ganjil 
        count += 1
        continue
    # break jika count melebihi sisi
    if count > sisi:
        break
    
# segitiga sama kaki

# tugas buat belah ketupat