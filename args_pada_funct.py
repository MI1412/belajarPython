# args
# memasukkan data / argument
def fungsi(nama,tinggi,berat):
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')

fungsi('imron',13,9)

# membuat funct dengan data list 
def funct(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
    
funct(['imr',9,18])

# membuat funct dengan args
def funct(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
    
funct('imron',18,19)    

# studi kasus
def tambah(*data): # *args adalah untuk bisa menambahkan input berapapun yang dimasukkan  
    # data tipenya tuple bisa di looping
    output = 0
    for angka in data:
        output += angka
        
    return output
    
hasil = tambah(1,2,3,4,5,6,7,8,9,)    
print(f'\nhasil = {hasil}')

hasil = tambah(10,5,60)    
print(f'\nhasil = {hasil}')