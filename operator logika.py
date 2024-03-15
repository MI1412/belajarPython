#digunakan untuk membuat hasil boolean
#operator logika 
#not, or, and, xor
print("operator not")
#not kebalikan dari boolean
a = bool(int(input("isi logika a berikut 1(True) 0(False) : ")))
b = not a 
print("a =",a, "not b =",b)

print("\noperator or")
#jika satu variabel benar maka benar 
a = bool(int(input("isi logika a berikut 1(True) 0(False) : ")))
b = bool(int(input("isi logika b berikut 1(True) 0(False) : ")))
c = a or b
print("a =",a,"or","b =",b ,"=",c)

print("\noperator and")
#jika dua variabel true maka true 
a = bool(int(input("isi logika a berikut  1(True) 0(False) : ")))
b = bool(int(input("isi logika b berikut  1(True) 0(False) : ")))
c = a and b 
print("a =",a,"and" ,"b =",b ,"=",c)

print("operator xor")
#xor adalah operator bitwise tetapi bisa dipakai untuk logika
#jika 1 variabel true maka true 
a = bool(int(input("isi logika a berikut 1(True) 0(False) : ")))
b = bool(int(input("isi logika b berikut 1(True) 0(False) : ")))
c = a ^ b 
print("a =", a,"XOR / ^", "b =", b,"=",c)