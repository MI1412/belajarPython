# latihan library date and time
import datetime as dt #import datetime sebagai dt

hari_ini = dt.date.today()
# print(hari_ini)
# print(f"hari ini adalah hari {hari_ini:%A}")
# tanggal = dt.date(2006,9,13)

# print(tanggal)
# print(f"hari ini adalah hari {tanggal:%A}")

print(5*"=","masukkan tanggal lahir",5*"=")

tanggal = int(input("tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("tahun \t\t: "))

print(10*"=","output","="*10)
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print("tanggal lahir\t\t:",tanggal_lahir)
print(f"hari lahir\t\t: {tanggal_lahir:%A}")
print(f"bulan lahir\t\t: {tanggal_lahir:%m}")
print(f"tahun lahir\t\t: {tanggal_lahir:%Y}")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"umur sekarang\t\t: {umur_tahun:} tahun \nhari yang \ndipakai untuk hidup \t: \n{umur_hari}")