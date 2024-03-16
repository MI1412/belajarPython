# membuat gabungan area rentang dari angka 
# contoh : ++++++3-------------10++++++
# penggabungan logika
input_user = float(input("masukkan angka yang bernilai kurang dari 3 atau lebih besar dari 10 : "))
# <3
# validasi angka < 3
kurang_dari_3 = (input_user < 3)
print("ini kurang dari 3 ",kurang_dari_3)
# >10
# validasi angka > 10
lebih_dari_10 = (input_user > 10)
print("lebih dari 10 ",lebih_dari_10)

correct = kurang_dari_3 or lebih_dari_10
print("angka yang anda masukkan ",correct)

print("\n",10*"====","\n")
# contoh lagi : ----3++++++10--------
# memotong logika
input_user = float(input("masukkan angka yang bernilai lebih dari 3 dan kurang dari 10 : "))

# -------3+++++++++
# > 3
lebihDari3 = input_user > 3
print("ini lebih dari 3 : ",lebihDari3)

# +++++++++10------------
kurangDari10 = input_user < 10
print("ini kurang dari 10 : ",kurangDari10)

tiga_kurang_dari_sepuluh = lebihDari3 and kurangDari10
print("angka yang anda masukka : ",tiga_kurang_dari_sepuluh)
