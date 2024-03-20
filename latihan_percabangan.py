# membuat kalkulator sederhana
angka1 = float(input("masukkan angka ke 1 : "))
angka2 = float(input("masukkan angka ke 2 : "))
print("operasi aritmatika \n1. + \n2. - \n3. : \n4. x \n5. %")
aritmatik = int(input("pilih operasi aritmatika : "))

if aritmatik == 1:
    hasil = angka1 + angka2
    print("hasil :",hasil)    
elif aritmatik == 2:
    hasil = angka1 - angka2
    print("hasil :",hasil)    
elif aritmatik == 3:
    hasil = angka1 / angka2
    print("hasil :",hasil)    
elif aritmatik == 4:
    hasil = angka1 * angka2
    print("hasil :",hasil)    
elif aritmatik == 5:
    hasil = angka1 % angka2                
    print("hasil :",hasil)    
else:
    print("anda yang masukkan bukan operasi aritmatika ")