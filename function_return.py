# return di function 

# def nama_function(argumen):
#   badan fungsi
#   return output

# function kuadrat
def kuadrat(input_angka):
    output = input_angka**2
    return output

y = kuadrat(2)
print(y)

# funct tambah
def tambah(angka1,angka2):
    return angka1 + angka2

print(tambah(2,1))

# funct operasi mtk
def operasi_mtk(angka1,angka2):
    nambah = angka1 + angka2
    kurang = angka1 - angka2
    bagi = angka1 / angka2
    kali = angka1 * angka2
    return nambah,kurang,bagi,kali # mengembalikan nilai dari variabel didalam function

a,b,c,d = operasi_mtk(10,5) # mengambil return di function operasi mtk
print(f'hasil tambah \t= {a}')
print(f'hasil kurang \t= {b}')
print(f'hasil bagi \t= {c}')
print(f'hasil kali \t= {d}')
