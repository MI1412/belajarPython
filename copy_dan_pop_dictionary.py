# copy dictionary
orang = {
    "sepp":"asep",
    "satt":"satria",
    "ce":"pace"
}

friends = orang.copy()
print(f"\norang : {orang}")
print(f"\nteman : {friends}")

orang["sepp"] = "kasepp"
print(f"\norang : {orang}")
print(f"\nteman : {friends}")

# pop dictionary adalah mengambil data pada dictionary kemudian dijadikan variabel
# pop berdasarkan key
data_asep = friends.pop("sepp") # ketik key untuk mengambil data dictionary
print(f"\ndata asep = {data_asep}")
print(f"\nteman : {friends}")


# pop item dictionary adalah mengambil item yang ada pada dict terakhir
data = friends.popitem()
print(f"\ndata pop item = {data}")
print(f"\nteman : {friends}")


