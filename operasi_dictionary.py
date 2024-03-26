# operator dictionary

data_dict = {
    "imron":"muhammad imron",
    "musa":"musa k",
    "caca":"salsabila"
    
}

# panjang dictionary 
len_dict = len(data_dict)
print(f"panjang / isi dari dictionary : {len_dict}")

# mengecek key ada atau tidak
key = "halo"
check_key = key in data_dict
print(f"apakah {key} ada di dalam dictionary : {check_key}")

# mengakses value (read) dengan get
print(data_dict["imron"]) # ini bisa
print(data_dict.get("imron")) # ini bisa
print(data_dict.get("p","data tidak ditemukan")) # ini error atau output none dengan mengecek message key tidak ditemukan string("nama key","pesan eror")

# update data dictionary
data_dict["imron"] = "imr" # mengubah value pada key
print(f"mengubah value key imron : {data_dict}")

data_dict.update({"imron":"muhammad imron"})
print(f"setelah dirubah imron : {data_dict}")
data_dict.update({"asep":"aseppp"})
print(f"data key asep ditambah  : {data_dict}") # kalau tidak ada key nya maka auto nambah sendiri

# menghapus data pada dictionary
del data_dict["asep"] # untuk menghapus ketikkan nama key nya
print(f"data asep sudah dihapus : {data_dict}")