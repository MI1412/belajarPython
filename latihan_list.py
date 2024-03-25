# program list buku

list_buku = [] # tempat menyimpan buku

while True:
    print("masukkan data buku")
    judul = input("masukkan judul buku \t: ")
    penulis = input("masukkan nama penulis \t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru) # tambah buku baru
    
    print(10*"=","data buku",10*"=")
    for index,buku in enumerate (list_buku):
        print(f"| buku ke -{index+1} \n| judul buku : {buku[0]} \n| nama penulis : {buku[1]}")
    
    is_lanjut = input("\napakah ingin lanjut ? (y/n)")
    if is_lanjut == "n":
        break
print("end program")    