# membaca file eksternal
print(3*"=","membaca file txt",3*"=")
file = open("data.txt",mode="r")

print(f"status read : {file.readable()}")

# method membaca semua file
print(f"file dibaca semua : {file.read()}") 

# baca file perbaris
# print(file.readline(),end ="") # enter diganti dengan string kosong
# print(file.readline(),end="") 

# baca semua baris sebagai list
# print(file.readlines())

# menutup file yang dibuka 
print(f"\napakah file sudah ditutup : {file.closed}") # mengecek file yang selesai ditutup
file.close()
print(f"apakah file sudah ditutup : {file.closed}") # mengecek file yang selesai ditutup

print("\n",3*"=","membaca file txt dengan with",3*"=")
# teknik membuka file di python dengan with
with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah ditutup : {file.closed}") # mengecek file yang selesai ditutup
    
print(f"apakah file sudah ditutup : {file.closed}") # auto menutup file yang dibuka