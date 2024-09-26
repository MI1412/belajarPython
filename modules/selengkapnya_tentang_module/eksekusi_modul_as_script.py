#saat menjalankan module python denngan:
#python fibo.py <arguments>
# kode didalam modul itu akan dieksekusi, jika hanya sebagai import tapi dengan __name__ diset menjadi __main__.
# ini contoh penambahan kode di akhir module
import modules as md

if __name__ == "__main__":
    import sys
    md.calc(int(sys.argv[1]))


