a = int(input("masukkan angka A : "))
b = int(input("masukkan angka B : "))
aritmatika = int(input("pilih operasi aritmatika 1(-) 2(+) 3(:) 4(x) 5(%) : "))
if aritmatika == 1:
	ar_kurang = a - b
	print(ar_kurang)
elif aritmatika == 2:
	ar_tambah = a + b
	print(ar_tambah)
elif aritmatika == 3:
	ar_bagi = a / b 
	print(ar_bagi)
elif aritmatika == 4:
	ar_kali = a * b
	print(ar_kali)
elif aritmatika == 5:
	ar_modulus = a % b
	print(ar_modulus)