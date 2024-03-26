# looping pada dictionary

orang = {
    "sepp":"asepp",
    "fii":"rafi",
    "dil":"fadil",
    "ce":"pace"
}

# looping first try
print("\nloop sederhana")
for teman in orang:
    print(teman) # menampilkan key nya ini tidak disarankan
    
# operator untuk mengambil item / iterables
print("\nmengambil keys ")
keys = orang.keys()
print(keys)

print("\nloop pada key")
for key in orang.keys():
    print(f"data dict : {orang.get(key)}") # mengambil value pada key 
    
print("\nvalue dictionary")    
value = orang.values()
print(value)

print("\nloop value dictionary")
for values in orang.values():
    print(f"data value : {values}")
    
items = orang.items()
print(" isi item ")
print(items) # menampilkan semua item pada dict

print("\nloop item")
for item in orang.items():
    print(item)
    
print("\nloop item lebih rapi")
for key,value in orang.items():
    print(f"key = {key} \nvalue = {value}")    