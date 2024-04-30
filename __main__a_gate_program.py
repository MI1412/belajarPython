# __main__ adalah gerbang program di python
# __main__ adalah top level code environment

# __name__ == __main__
# __name__ pada file program utama
# __name__ ketika dipanggil oleh program utama maka akan menjadi tetapi ketika __name__ pada luar program utama maka akan dipanggil sesuai nama file
print(f"\nnilai __name__ pada file ini = '{__name__}'")

# contoh 1 :
# __name__ pada file program eksternal
import fungsi

# contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a:int,b:int)-> int:
    return a + b
    

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 5
    hasil = fungsi_tambah(angka1,angka2)
    print(f"\nhasil tambah = {hasil}")

# contoh 2  :
#  __name__ pada package
import package
# ketika di import tidak terjadi apa apa tetapi ketika dipanggil di cmd dengan python <nama package> maka akan keluar hasil program


