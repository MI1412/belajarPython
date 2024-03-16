
# soal nomer 1. ------0++++5--------8++++++++11-------
# no 1
input_user = float(input("no 1. masukkan angka : "))
# -----0
lebih_dari0 = input_user >= 0 

# +++++5
kurang_dari5 = input_user <= 5

# correct 0 > 5
correct1 = lebih_dari0 and kurang_dari5

# -----8

lebih_dari8 = input_user >= 8

# +++++11
kurang_dari11 = input_user <= 11

correct2 = lebih_dari8 and kurang_dari11

hasil = correct1 or correct2
print("\nhasil : ",hasil)

print(5*"======")
# soal nomer 2. ++++++++++0-------5+++++8--------11+++++++
# no 2
input_user = float(input("no 2. masukkan angka : "))

# ++++0
kurang_dari0 = input_user <= 0 

# ----5
lebih_dari5 = input_user >= 5

correct1 = kurang_dari0 or lebih_dari5

# +++++8
kurang_dari8 = input_user <= 8

# ----11
lebih_dari11 = input_user >= 11

correct2 = kurang_dari8 or lebih_dari11

hasil = correct1 and correct2
print("\nhasil : ",hasil)

print("\n\t      DONE")