# Sekarang, apa yang terjadi ketika pengguna menulis from sound.effects import *? Idealnya, kita berharap bahwa ini secara otomatis mencari sistem berkas, menemukan submodul yang ada dalam paket, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor submodul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika submodul diimpor secara eksplisit.

# Satu-satunya solusi adalah bagi penulis paket untuk menyediakan indeks eksplisit dari paket tersebut. Pernyataan impor menggunakan konvensi berikut: jika kode __init__.py dari sebuah paket mendefinisikan daftar bernama __all__, maka daftar tersebut dianggap sebagai daftar nama modul yang harus diimpor ketika from package import * digunakan. Penulis paket harus memastikan daftar ini selalu diperbarui ketika versi baru dari paket dirilis. Penulis paket juga dapat memutuskan untuk tidak mendukung fitur ini jika mereka tidak melihat kegunaan untuk mengimpor * dari paket mereka. Misalnya, file sound/effects/__init__.py bisa berisi kode berikut:
# __all__ = ["echo", "surround", "reverse"]
# Ini berarti bahwa from sound.effects import * akan mengimpor ketiga submodul yang disebutkan dalam paket sound.effects.

# Perlu diingat bahwa submodul mungkin menjadi tertutup oleh nama yang didefinisikan secara lokal. Misalnya, jika Anda menambahkan fungsi reverse ke dalam file sound/effects/__init__.py, from sound.effects import * hanya akan mengimpor dua submodul echo dan surround, tetapi bukan submodul reverse, karena nama tersebut ditutupi oleh fungsi reverse yang didefinisikan secara lokal:

# __all__ = [
#     "echo",      # merujuk ke file 'echo.py'
#     "surround",  # merujuk ke file 'surround.py'
#     "reverse",   # !!! merujuk ke fungsi 'reverse' sekarang !!!
# ]

# def reverse(msg: str):  # <-- nama ini menutupi submodul 'reverse.py'
#     return msg[::-1]    #     dalam kasus 'from sound.effects import *'
# Jika __all__ tidak didefinisikan, pernyataan from sound.effects import * tidak akan mengimpor semua submodul dari paket sound.effects ke dalam namespace saat ini; ia hanya memastikan bahwa paket sound.effects telah diimpor (mungkin menjalankan kode inisialisasi di __init__.py) dan kemudian mengimpor nama-nama yang didefinisikan dalam paket tersebut. Ini termasuk nama-nama yang didefinisikan (dan submodul yang dimuat secara eksplisit) oleh __init__.py. Ini juga mencakup submodul dari paket yang dimuat secara eksplisit oleh pernyataan impor sebelumnya. Pertimbangkan kode berikut:
# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *

# Dalam contoh ini, modul echo dan surround diimpor ke dalam namespace saat ini karena mereka didefinisikan dalam paket sound.effects saat pernyataan from...import dijalankan. (Ini juga berlaku ketika __all__ didefinisikan.)

# Meskipun beberapa modul dirancang untuk mengekspor hanya nama yang mengikuti pola tertentu ketika menggunakan import *, ini masih dianggap sebagai praktik buruk dalam kode produksi.

# Ingatlah, tidak ada yang salah dengan menggunakan from package import specific_submodule! Bahkan, ini adalah notasi yang disarankan kecuali modul yang mengimpor perlu menggunakan submodul dengan nama yang sama dari paket yang berbeda.


# kesimpulan: 
# from package import *: Ini mengimpor semua nama yang ada dalam daftar __all__ dari paket. Jika __all__ tidak didefinisikan, ini hanya mengimpor nama-nama yang sudah ada dalam paket dan modul-modul yang dimuat sebelumnya.
# Perlunya __all__: Jika didefinisikan, __all__ menentukan modul mana yang diimpor dengan from package import *. Tanpa __all__, hanya nama-nama yang ada di paket yang akan diimpor, bukan submodul.
# Masalah Potensial: Nama-nama dalam __all__ bisa ditutupi oleh nama-nama lokal dalam __init__.py. Ini bisa menyebabkan modul yang seharusnya diimpor tidak tersedia.
# Rekomendasi: Sebaiknya gunakan from package import specific_submodule untuk menghindari masalah dan praktik buruk dalam kode produksi.