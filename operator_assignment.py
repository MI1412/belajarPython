# operator assignment adalah operator penugasan / juga operator = 
# contoh 
a = 5 #ini adalah contoh assignment sederhana
print('\nnilai a =',a)

a += 1
print('nilai a += 1 adalah',a)


a -= 1
print('nilai a -= 1 adalah',a)


a *= 4
print('nilai a *= 4 adalah',a)


a /= 2
print('nilai a /= 2 adalah',a)

# digunakan untuk mendapatkan hasil bagi
a %= 3
print('nilai a %= 2 adalah',a)

# digunakan untuk pembulatan
a = 6
a //= 2
print('nilai a //= 2 adalah',a)

# digunakan untuk menghitung nilai pangkat
a = 2
a **= 3
print('nilai a **= 2 adalah',a)

# operator assignment bisa digunakan untuk operator bitwise 

# or |
c = True
print("\nc adalah",c)
c |= False
print("c = True","or =",c)

# and &
c = True
c &= False
print("c = True","& =",c)

#  xor ^
c = True
c ^= False
print("c = True","xor =",c)

# operator shifting
d = 0b0100
print("\nnilai d =\t    ",d,format(d,'04b'))

# shift right >>=
d >>= 2
print("nilai d >>= 2 adalah",d,format(d,'04b'))

# shift left <<=
d <<= 2
print("nilai d <<= 2 adalah",d,format(d,'04b'))