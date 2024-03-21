# continue dan pass

# pass berfungsi untuk dummy, tidak akan dieksekusi

# angka = 0
# while angka < 5:
#     angka += 1
    
#     if angka == 3:
#         pass # ini tidak akan dieksekusi
#     print(angka) 

# continue 
# angka = 0
# print("\n")
# print(f"angka sekarang {angka}") # aksi 1
# while angka < 5:
#     angka += 1
#     print(f"angka diloop {angka}")
#     if angka == 3:
#         print("siip")
#         continue # ini akan membuat loop loncat ke aksi yang pertama
#     print("halo imron") # aksi 2
    
# print("end program")    

# break 
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang : {angka}") # aksi 1
    if angka == 3:
        print("halo imron")
        break # break digunakan untuk menghentikan alur loop
    print("tes") # aksi 2
print("end program")    