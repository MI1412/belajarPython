print("konversi temperatur")
#celcius
data_celcius = float(input("masukkan suhu celcius : "))
print("celcius : ",data_celcius,"\b° C")

#fahrenheit
data_fahrenheit = float(input("masukkan suhu fahrenheit : "))
print("fahrenheit : ",data_fahrenheit,"\b° F")

#reamur 
data_reamur = float(input("masukkan suhu reamur : "))
print("reamur : ",data_reamur,"\b° R")

#kelvin
data_kelvin = float(input("masukkan suhu kelvin : "))
print("kelvin : ",data_kelvin,"K")

# konversi suhu
#c > k
value_konversi = float(input("masukkan pilihan konversi 1(C > R), 2(C > F), 3(R > C), \n4(F > C), 5(C > K), 6(K > C), 7(F > K) : "))

if value_konversi == 1 :
	hasil_1 = data_celcius * (4/5)
	print("hasil : ",hasil_1,"\b° R")
elif value_konversi == 2 :
	hasil_2 = data_celcius * (9/5) + 32
	print("hasil : ",hasil_2,"\b° F")
elif value_konversi == 3 :
	hasil_3 = data_reamur * (5/4)
	print("hasil : ",hasil_3,"\b° C")
elif value_konversi == 4 :
	hasil_4 = (data_fahrenheit - 32) * 5/9
	print("hasil : ",hasil_4,"\b° C")

# repeat konversion 
input_user = bool(int(input("apakah anda ingin mengulang konversi lagi ? ya (1) tidak(0) : ")))
if input_user == False:
	print(":-)")

elif input_user == True:
	 value_konversi = float(input("masukkan pilihan konversi 1(C > R), 2(C > F), 3(R > C), \n4(F > C), 5(C > K), 6(K > C), 7(F > K) : "))

if value_konversi == 1 :
	hasil_1 = data_celcius * (4/5)
	print("hasil : ",hasil_1,"\b° R");
elif value_konversi == 2 :
	hasil_2 = data_celcius * (9/5) + 32
	print("hasil : ",hasil_2,"\b° F");
elif value_konversi == 3 :
	hasil_3 = data_reamur * (5/4)
	print("hasil : ",hasil_3,"\b° C");
elif value_konversi == 4 :
	hasil_4 = (data_fahrenheit - 32) * 5/9
	print("hasil : ",hasil_4,"\b° C");