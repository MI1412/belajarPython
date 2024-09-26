# melakukan penghapusan secara rekursif
# pada saat del akan menghapus dari kiri ke kanan
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] #hapus data index 0
print(f"a: {a}")
del a[:] # del a[:] menghapus isi list atau del a akan menghapus variabel

print(f"a: {a}")