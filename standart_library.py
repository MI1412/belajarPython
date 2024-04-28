import datetime
# mengambil data waktu

dt_time = datetime.datetime.now()
print(f"data waktu sekarang {dt_time}")

print(f"\ndata tahun sekarag {dt_time.year}")

print(f"\ndata waktu format hari {dt_time.strftime('%A')}")

from collections import Counter
# menghitung data

data = ['a','b','c','d','e','f','g','b','d']
data_count = Counter(data)

print(f"\ndata count = {data_count}")
print(f"\ndata jumlah a = {data_count['a']}\n")

import io

file = io.open("sayHello.txt","r")

print(file.read())

""" dan masih banyak lagi standart library di python"""
