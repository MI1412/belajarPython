print(f"\nnilai __name__ pada fungsi.py = '{__name__}'")

# deklarasi
def fungsi_tambah(a:int,b:int)-> int:
    return a + b
    

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 5
    hasil = fungsi_tambah(angka1,angka2)
    print(f"\nhasil tambah pada file fungsi.py = {hasil}")
else:
    print("\ntidak bisa ditambahkan karena file fungsi bukan main")    