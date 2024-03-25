# looping dari list 
# for loop
kumpulan_angka = [4,6,1,3,2,5]
print(" ")

for angka in kumpulan_angka:
    print(f"angka = {angka}")
    
peserta = ["amir","lutfi","admin","ahmd"]
print(" ")
for nama in peserta:
    print(f"nama = {peserta}")    
    
# foor loop dan range

kumpulan_angka = [8,7,4,6,1,3,2,5]

panjang = len(kumpulan_angka)

print(" ")
for i in range (panjang):
    print(f"kumpulan angka {i}")

# while

panjang = len(kumpulan_angka)
print(" ")
i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
print(" ")
data = ["mamang",1,2,3,"amir"]
[print(f"data = {i}") for i in data]
angka = [8,7,4,6,1,3,2,5]
angka_kuadrat = [i**2 for i in angka]
print(f"angka kuadrat = {angka_kuadrat}")

# enumerate
print(" ")
data_list = ["mamang",1,2,3,"amir"]

for index,data in enumerate (data_list):
    print(f"index = {index} \ndata = {data}")