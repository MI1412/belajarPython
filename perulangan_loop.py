# looping for
# ini dengan list
angka_list = [0,1,2,3,4,5]

for i in angka_list:
    print(f"i adalah {i}")
print("akhir program dengan list\n")    

# ini dengan range
angka_range = range(5)
for i in angka_range:
    print(f"i adalah {i}") 
print("akhir program dengan range\n")    

angka_range = range(-1,10) # ini , adalah untuk membatasi angka yang dimulai dan berakhir
for i in angka_range:
    print(f"i adalah {i}") 
print("akhir program dengan range pembatas\n")  

# menggunakan string 
data_string = "imron"
for i in data_string:
    print(i) 
print("akhir program string\n")    

# looping while

angka = 0
print(f"angka awal = {angka}\n")
while angka < 5:
    angka += 1 # kondisi boolean 
    print(f"angka adalah {angka}")
print("end program")    

# di python tidak ada do while