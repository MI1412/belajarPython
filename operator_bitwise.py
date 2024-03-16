# operator bitwise
# operator bitwise adalah operaor binary
# contoh : 
a = 9 
b = 5 
print(5*"======")
# operator | (or) atau bisa sebagai operator logika or
print("\n\t      or")
c = a | b
print("nilai a :",a,"binary :",format(a,'08b'))
print("nilai b :",b,"binary :",format(b,'08b'))
print("nilai c :",c,"binary :",format(c,'08b'))
print(5*"======")

# operator & (and) atau bisa sebagai operator logika and
c = a & b 
print("\n\t      and")
print("nilai a :",a,"binary :",format(a,'08b'))
print("nilai b :",b,"binary :",format(b,'08b'))
print("nilai c :",c,"binary :",format(c,'08b'))
print(5*"======")
# operator ^ (xor) atau bisa sebagai operator logika xor
c = a ^ b 
print("\n\t      xor")
print("nilai a :",a,"binary :",format(a,'08b'))
print("nilai b :",b,"binary :",format(b,'08b'))
print("nilai c :",c,"binary :",format(c,'08b'))
print(5*"======")

# operator ~ (not) atau bisa sebagai operator logika not
c = ~ b 
d = ~ a
print("\n\t      not")
print("nilai a :",a,"binary :",format(a,'08b'))
print("nilai b :",b,"binary :",format(b,'08b'))
print("nilai c not b :",c,"\nbinary :",format(c,'08b'))
print("nilai d not a :",d,"\nbinary :",format(d,'08b'))
print(5*"======")

# operator shifting angka bit digeser 
# shifting right (>>)
c = a >> 1 # 1 adalah nilai yang digeser
print("\n\t  shift right")
print("nilai a :",a,"binary :",format(a,'08b'))
# dari 00001001
print("nilai c :",c,"binary :",format(c,'08b'))
# ke 00000100
print(5*"======")

# operator shifting angka bit digeser 
# shifting left (<<)
c = a << 1 # 1 adalah nilai yang digeser
print("\n\t  shift left")
print("nilai a :",a,"binary :",format(a,'08b'))
# dari 00001001
print("nilai c :",c,"binary :",format(c,'08b'))
# ke 00010010
print(5*"======")
