# tingkat lanjut dalam list

data0 = [1,2]
data1 = [3,4]

data_2d = [data0,data1,10]
data_2d_copy = data_2d.copy()

print(f"data 2d = {data_2d}")
print(f"data copy 2d = {data_2d_copy}")

# mengambil data dari nested list / list bersarang
data = data_2d[0][0] # [indeks list yaitu data0] [memilih data pada data0]
print(f"data = {data}")

# alamat data 2d dan data copy 2d
print(F"alamat data 2d \t    = {hex(id(data_2d))}")
print(F"alamat data 2d copy = {hex(id(data_2d_copy))}")


print("\nalamat dari member ke-1")
print(F"alamat data 2d \t    = {hex(id(data_2d[0]))}")
print(F"alamat data 2d copy = {hex(id(data_2d_copy[0]))}")

data_2d[1][0]= 5
data_2d[2]= 9
print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")

# menggunakan deep copy()
from copy import deepcopy # import dari library copy yaitu deepcopy
data_2d = [data0,data1,10]
data_2d_deepcopy = deepcopy(data_2d)
print(F"alamat data 2d \t        = {hex(id(data_2d[0]))}")
print(F"alamat data 2d deepcopy = {hex(id(data_2d_deepcopy[0]))}")

print("\nalamat dari member ke-1")
print(F"alamat data 2d \t         = {hex(id(data_2d[0]))}")
print(F"alamat data 2d deep copy = {hex(id(data_2d_deepcopy[0]))}")

# pembuktian
data_2d[1][0] = 30
print(f"data 2d = {data_2d}")
print(f"data copy 2d = {data_2d_copy}")
print(f"data deepcopy 2d = {data_2d_deepcopy}")
