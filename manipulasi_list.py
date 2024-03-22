# method list

data = ["imron","ammar","musa"]

# mengambil data 

data_0 = data[0]
print("indeks =",data_0)

# mengambil jumlah list data

data_panjang = len(data)
print(f"panjang data adalah {data_panjang}")

# manipulasi data list
# menambahkan item pada list

print(f"data sebelum {data}")
data.insert(1,"mama") # (indeks,data)

print(f"data sudah ditambah {data}")

# menambah data pada akhir list
data.append("caca")
print(f"data ditambah {data}")

# menggabungkan list 
data_baru = ["rafi","rido","abyan"]
data.extend(data_baru)
print(f"data list digabung \n{data}")

# merubah data
data[2] = "tes"
print(f"data dirubah {data}")

# menghapus data

data.remove("caca")
print(f"data yang dihapus caca \n{data}")

# menghapus data paling belakang
data.pop()
print(f"menghapus data diakhir {data}")

