# Packages dalam Python adalah cara untuk mengorganisasi namespace modul dengan menggunakan nama modul yang terdotasi. Ini membantu dalam mengelompokkan modul-modul terkait dalam satu paket sehingga mereka tidak saling bertabrakan nama modulnya. Dengan menggunakan nama modul terdotasi, pengembang tidak perlu khawatir tentang konflik nama antara modul yang berbeda dalam paket multi-modul seperti NumPy atau Pillow.

# Contoh Kasus: Jika Anda ingin mendesain koleksi modul untuk menangani berkas suara dan data suara secara seragam, Anda mungkin harus menangani berbagai format berkas suara (seperti .wav, .aiff, .au) dan berbagai operasi pada data suara (seperti pencampuran, menambahkan echo, menerapkan fungsi equalizer). Menggunakan struktur paket memungkinkan Anda mengelompokkan modul-modul ini dengan cara yang terorganisasi, menghindari konflik nama, dan memudahkan pemeliharaan.

# Contoh Struktur Paket: Misalnya, jika Anda merancang paket untuk menangani berbagai format berkas suara dan operasi pada data suara, struktur paket Anda bisa terlihat seperti ini dalam sistem file hierarkis:

# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

# Saat Python mengimpor sebuah paket, Python mencari subdirektori paket di direktori yang ada dalam sys.path.

# File __init__.py:

# Fungsi Utama: File __init__.py diperlukan untuk membuat Python menganggap direktori yang berisi file tersebut sebagai paket. Ini memungkinkan Python untuk membedakan antara direktori yang berfungsi sebagai paket dan direktori biasa dengan nama yang sama.
# Kegunaan Lain: Dalam kasus sederhana, __init__.py bisa berupa file kosong. Namun, file ini juga bisa digunakan untuk mengeksekusi kode inisialisasi paket atau mengatur variabel __all__ yang mengontrol apa yang diimpor ketika from package import * digunakan.
# Tujuan dari __init__.py:

# Mencegah direktori dengan nama umum dari secara tidak sengaja menyembunyikan modul yang valid yang muncul lebih belakangan dalam jalur pencarian modul.
# Menyediakan kontrol tambahan atas apa yang termasuk dalam paket dan bagaimana paket diinisialisasi.
# Dengan adanya __init__.py, Python dapat mengelola struktur paket dengan lebih baik, mencegah konflik nama dan memberikan cara untuk mengatur atau menginisialisasi paket sesuai kebutuhan.

# contoh: import sound.effects.echo

# Ini memuat submodul sound.effects.echo. Submodul ini harus direferensikan dengan nama lengkapnya.
# contoh: sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# ada alternatif lain untuk import submodule, berikut contohnya:
# from sound.effects import echo
# ini juga memuat submodule echo dan membuatnya tersedia tanpa prefix package, jadi bisa melakukan ini sebagai berikut
# echo.echofilter(input, output, delay=0.7, atten=4)

# atau bisa import function secara langsung dari package / variabel
# from sound.effects.echo import echofilter
# sekali lagi ini memuat fungsi saja : echofilter(input, output, delay=0.7, atten=4)

# Perhatikan bahwa ketika menggunakan from package import item, item dapat berupa submodul (atau subpaket) dari paket tersebut, atau nama lain yang didefinisikan dalam paket, seperti fungsi, kelas, atau variabel. Pernyataan impor pertama-tama menguji apakah item didefinisikan dalam paket; jika tidak, maka dianggap sebagai modul dan mencoba memuatnya. Jika gagal menemukannya, akan muncul pengecualian ImportError.

# Sebaliknya, ketika menggunakan sintaks seperti import item.subitem.subsubitem, setiap item kecuali yang terakhir harus berupa paket; item terakhir dapat berupa modul atau paket tetapi tidak bisa berupa kelas, fungsi, atau variabel yang didefinisikan dalam item sebelumnya.
