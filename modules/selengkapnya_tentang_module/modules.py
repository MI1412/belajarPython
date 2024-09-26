# jika kamu keluar dari python interpreter dan membuka itu lagi, syntax yang kamu tulis akan hilang
# untuk itu jika kamu ingin menulis proram panjang lebih baik menyiapka text editor yang sudah ada python interpreter dan menjalankan file disana

# untuk membantu ini python punya sebuah definisi didalam sebuah file dan menggunakannya di python interpreter yang dipanggil module

# definisi module adalah bisa melakukan import ke beberapa module atau ke module utama (sebuah koleksi dari variabel yang kamu punya akses ke eksekusi ke level atas dan mode penghitungan)

# module berisi file dari beberapa definisi python dan beberapa statement. nama module adalah file yang berakhiran .py
# nama module alias sebuah string tersedia di value variabel global bernama __name__.
# contoh memanggil file ini

def calc(a:int,c:str,b:int):
    """operasi calc"""
    match c:
        case '+':
            return a +b
        case '-':
            return a - b
        case '/':
            return a / b
        case '*':
            return a * b
        case '%':
            return a % b
        case _:
            return 'ga valid'

def _hai(a:str)->str:
    print(f"hai {a}")

# <--selengkapnya tentang module
# ketika selesai import validasi dengan module.__name__ untuk mengetahui nama module
# sebuah module berisi eksekusi dan definisi fungsi yang dijalankan pada pertama kali modul diimport

# setiap module memiliki namespace / variabel global bagi fungsi dalam modul tersebut, sehingga penulis modul dapat menggunakan variabel global tanpa konflik dengan variabel global lainnya, namun variabel global modul dapat diakses dari luar modul menggunakan cara yang sama seperti mengakses fungsi
# format memanggil: namaModul.namaItem




 
