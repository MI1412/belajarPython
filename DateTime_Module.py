# mengidentifikasi module
import datetime

# menampilkan isi date time
print(f"isi dalam module : {dir(datetime)}")

# bantuan di dalam module
# help(datetime)

date = datetime.date(2024,9,30)

print(date)

# akses yang digunakan di module datetime 
# 1. module : datetime
# 2. class : datetime
# 3. method : today()

now = datetime.datetime.today()
print(f"waktu sekarang : {now}")
print(f"micro second : {now.microsecond}")

# convert strings ke datetimes
# method : strptime()
besok = '8/30/2024'
besok_datetime = datetime.datetime.strptime(besok,'%m/%d/%Y')
print(f"selesai diconvert : {besok_datetime}")




