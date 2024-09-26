# beberapa atribut khusus

# 1. none
# menunjukkan tidak ada nilai apapun yang dikembalikan
# nilai boolean adalah false
None

# 2. NotImplemented

# NotImplemented adalah objek khusus dalam Python yang digunakan untuk menunjukkan bahwa suatu operasi atau metode tidak diimplementasikan untuk jenis operand tertentu. Ini membantu Python untuk mengetahui bahwa operasi yang dimaksud tidak bisa dilakukan dengan cara yang sedang dicoba, dan memungkinkan Python untuk mencoba metode lain atau mekanisme fallback.

# Berikut adalah beberapa hal penting tentang NotImplemented:

# Singleton: NotImplemented adalah objek tunggal, artinya hanya ada satu instance dari objek ini.

# Penggunaan dalam Metode: Ketika Anda mengimplementasikan metode seperti __eq__, __add__, atau metode perbandingan kaya lainnya, dan jika metode tersebut tidak dapat menangani operand yang diberikan, Anda dapat mengembalikan NotImplemented. Ini memungkinkan Python untuk mencoba metode lain pada operand tersebut (misalnya, metode refleksi) untuk menyelesaikan operasi.

# Tidak Digunakan dalam Konteks Boolean: NotImplemented tidak boleh digunakan dalam konteks boolean. Ini berarti Anda tidak boleh menganggap NotImplemented sebagai True atau False. Jika Anda perlu memeriksa apakah suatu metode telah diimplementasikan, Anda harus membandingkan nilai tersebut dengan NotImplemented secara eksplisit.

# 3. ellipsis
# Ellipsis dalam pemrograman Python adalah objek khusus yang dilambangkan dengan tiga titik (...). Ini memiliki beberapa kegunaan, tergantung pada konteksnya:

# 3.1 Sebagai Placeholder: Dalam kode, ellipsis sering digunakan sebagai placeholder untuk menunjukkan bahwa bagian kode tersebut belum diimplementasikan atau sedang dalam pengembangan. Ini berguna saat Anda sedang merancang struktur kode dan ingin menandai tempat-tempat yang perlu diisi kemudian.
def my_function():
    ...
my_function()
# Dalam contoh di atas, ... menunjukkan bahwa fungsi my_function belum diimplementasikan.

# 3.2 Sebagai Indikator dalam Indeksing: Dalam konteks array multidimensi (misalnya, dengan menggunakan NumPy), ellipsis digunakan untuk menunjukkan bahwa ada beberapa dimensi yang tidak ditampilkan secara eksplisit. Ini sering digunakan untuk mempermudah akses ke elemen dalam array besar tanpa harus menuliskan semua indeks.
import numpy as np
array = np.random.rand(5, 5, 5)
subarray = array[..., 1]  # Mengakses semua elemen di dimensi terakhir dengan indeks 1
# Dalam contoh di atas, ... digunakan untuk mewakili semua elemen di dimensi pertama dan kedua dari array, hanya fokus pada dimensi ketiga.
# 3.3 Sebagai Objek Literal: Ellipsis juga dapat digunakan sebagai objek literal dalam Python. Anda dapat menggunakan Ellipsis dalam kode untuk mewakili objek atau nilai khusus dalam konteks tertentu. Ini jarang digunakan secara langsung tetapi mungkin ditemukan dalam kode yang lebih kompleks.
x = Ellipsis
# Dalam contoh ini, x diatur menjadi objek Ellipsis, dan Anda dapat menggunakan Ellipsis dalam konteks yang sesuai.
# Secara keseluruhan, ellipsis adalah fitur fleksibel dalam Python yang digunakan untuk berbagai tujuan, dari placeholder sederhana hingga manipulasi indeks dalam array multidimensi.

# 4 numbers.number
# Objek angka ini dibuat oleh literal numerik dan dikembalikan sebagai hasil oleh operator aritmatika dan fungsi built-in aritmatika. Objek numerik bersifat tidak dapat diubah (immutable); begitu dibuat, nilai mereka tidak pernah berubah. Angka dalam Python tentu saja terkait erat dengan angka matematika, tetapi tunduk pada keterbatasan representasi numerik dalam komputer.

# Representasi string dari kelas numerik, yang dihitung oleh `__repr__()` dan `__str__()`, memiliki properti sebagai berikut:

# - Mereka adalah literal numerik yang valid yang, ketika diteruskan ke konstruktor kelas mereka, menghasilkan objek dengan nilai dari angka aslinya.
# - Representasi berada dalam basis 10, jika memungkinkan.
# - Nol di depan, kecuali satu nol sebelum titik desimal, tidak ditampilkan.
# - Nol di belakang, kecuali satu nol setelah titik desimal, tidak ditampilkan.
# - Tanda hanya ditampilkan ketika angka tersebut negatif.

# Python membedakan antara integer, angka floating-point, dan angka kompleks:

# 4.1 bilangan bulat / integer
# Ini mewakili elemen dari himpunan matematika bilangan bulat (positif dan negatif).

# Catatan Aturan untuk representasi bilangan bulat bertujuan untuk memberikan interpretasi yang paling berarti dari operasi geser (shift) dan masker (mask) yang melibatkan bilangan bulat negatif.

# Ada dua jenis bilangan bulat:

# Bilangan Bulat (int) Ini mewakili angka dalam rentang tak terbatas, tergantung pada memori (virtual) yang tersedia. Untuk tujuan operasi geser dan masker, asumsi yang digunakan adalah representasi biner, dan bilangan negatif direpresentasikan dalam varian dari 2’s complement yang memberikan ilusi deretan bit tanda yang tak terbatas yang memanjang ke kiri.

# Boolean = 0 false, 1 true (bool) Ini mewakili nilai kebenaran False dan True. Dua objek yang mewakili nilai False dan True adalah satu-satunya objek Boolean. Tipe Boolean adalah subtype dari tipe integer, dan nilai Boolean berperilaku seperti nilai 0 dan 1, masing-masing, dalam hampir semua konteks, kecuali bahwa ketika dikonversi ke string, string "False" atau "True" akan dikembalikan, masing-masing.

# 4.2 bilangan floating-poin
# Ini mewakili angka floating-point presisi ganda pada tingkat mesin. Anda bergantung pada arsitektur mesin yang mendasari (dan implementasi C atau Java) untuk rentang yang diterima dan penanganan overflow. Python tidak mendukung angka floating-point presisi tunggal; penghematan dalam penggunaan prosesor dan memori yang biasanya menjadi alasan penggunaan presisi tunggal tidak sebanding dengan overhead penggunaan objek dalam Python, sehingga tidak ada alasan untuk memperumit bahasa dengan dua jenis angka floating-point.

# 4.3 bilangan complex
# Ini mewakili angka kompleks sebagai sepasang angka floating-point presisi ganda pada tingkat mesin. Peringatan yang sama berlaku seperti untuk angka floating-point. Bagian nyata dan imajiner dari angka kompleks z dapat diambil melalui atribut hanya-baca z.real dan z.imag.

# 5 berurutan
# Ini mewakili himpunan terurut yang terbatas yang diindeks oleh angka non-negatif. Fungsi bawaan len() mengembalikan jumlah item dalam sebuah urutan. Ketika panjang urutan adalah n, set indeks berisi angka 0, 1, …, n-1. Item ke-i dari urutan a dipilih dengan a[i]. Beberapa urutan, termasuk urutan bawaan, menginterpretasikan subskrip negatif dengan menambahkan panjang urutan. Sebagai contoh, a[-2] sama dengan a[n-2], yaitu item kedua dari akhir dalam urutan a dengan panjang n.

# Urutan juga mendukung pemotongan (slicing): a[i:j] memilih semua item dengan indeks k sehingga i <= k < j. Ketika digunakan sebagai ekspresi, sebuah pemotongan adalah urutan dengan tipe yang sama. Komentar di atas tentang indeks negatif juga berlaku untuk posisi pemotongan negatif.

# Beberapa urutan juga mendukung "pemotongan lanjutan" dengan parameter ketiga "langkah" (step): a[i:j:k] memilih semua item dari a dengan indeks x di mana x = i + n*k, n >= 0 dan i <= x < j.

# Urutan dibedakan menurut mutabilitasnya:

# 5.1 urutan tetap
# Sebuah objek dari tipe urutan yang tidak dapat diubah (immutable) tidak dapat berubah setelah dibuat. (Jika objek tersebut berisi referensi ke objek lain, objek-objek lain ini mungkin dapat diubah; namun, koleksi objek yang langsung direferensikan oleh objek yang tidak dapat diubah tidak dapat berubah.)

# Tipe-tipe berikut adalah urutan yang tidak dapat diubah:

# String Sebuah string adalah urutan nilai yang mewakili titik kode Unicode. Semua titik kode dalam rentang U+0000 - U+10FFFF dapat direpresentasikan dalam sebuah string. Python tidak memiliki tipe char; sebaliknya, setiap titik kode dalam string diwakili sebagai objek string dengan panjang 1. Fungsi bawaan ord() mengonversi titik kode dari bentuk string-nya ke sebuah integer dalam rentang 0 - 10FFFF; chr() mengonversi sebuah integer dalam rentang 0 - 10FFFF ke objek string dengan panjang 1 yang sesuai. str.encode() dapat digunakan untuk mengonversi sebuah str menjadi bytes menggunakan pengkodean teks yang diberikan, dan bytes.decode() dapat digunakan untuk mencapai sebaliknya.

# Tuple Item-item dari sebuah tuple adalah objek Python sembarang. Tuple dengan dua atau lebih item dibentuk oleh daftar ekspresi yang dipisahkan koma. Sebuah tuple dengan satu item (sebuah 'singleton') dapat dibentuk dengan menambahkan koma pada sebuah ekspresi (sebuah ekspresi itu sendiri tidak menciptakan sebuah tuple, karena tanda kurung harus dapat digunakan untuk pengelompokan ekspresi). Sebuah tuple kosong dapat dibentuk dengan sepasang tanda kurung kosong.

# Bytes Objek bytes adalah array yang tidak dapat diubah. Item-itemnya adalah byte 8-bit, yang diwakili oleh integer dalam rentang 0 <= x < 256. Literal bytes (seperti b'abc') dan konstruktor bawaan bytes() dapat digunakan untuk membuat objek bytes. Selain itu, objek bytes dapat didekode menjadi string melalui metode decode().

# 5.2 urutan berubah
# Urutan yang dapat diubah (mutable) dapat diubah setelah dibuat. Notasi langganan (subscription) dan pemotongan (slicing) dapat digunakan sebagai target dari pernyataan penugasan dan del (hapus).

# Saat ini ada dua tipe urutan yang dapat diubah (mutable) yang intrinsik:

# lists (Lists) Item-item dalam sebuah daftar adalah objek Python sembarang. Daftar dibentuk dengan menempatkan daftar ekspresi yang dipisahkan koma dalam tanda kurung siku. (Perlu dicatat bahwa tidak ada kasus khusus yang diperlukan untuk membentuk daftar dengan panjang 0 atau 1.)

# Array Byte (Byte Arrays) Objek bytearray adalah array yang dapat diubah. Mereka dibuat oleh konstruktor bawaan bytearray(). Selain dapat diubah (dan oleh karena itu tidak dapat di-hash), array byte memberikan antarmuka dan fungsionalitas yang sama seperti objek bytes yang tidak dapat diubah.

# catatan modul array dan collection menyediakan contoh tambahan tentang tipe sekuens yang dapat diubah.

# 6. tipe set
# Ini mewakili himpunan yang tidak terurut, terbatas, dan terdiri dari objek unik yang tidak dapat diubah (immutable). Karena itu, mereka tidak dapat diindeks oleh subskrip apa pun. Namun, mereka dapat diiterasi, dan fungsi bawaan len() mengembalikan jumlah item dalam sebuah himpunan. Penggunaan umum untuk himpunan adalah pengujian keanggotaan dengan cepat, menghapus duplikasi dari urutan, dan menghitung operasi matematika seperti irisan (intersection), gabungan (union), perbedaan (difference), dan perbedaan simetris (symmetric difference).

# Untuk elemen himpunan, aturan ketidakberubahan yang sama berlaku seperti untuk kunci dictionary (dictionary). Perlu diperhatikan bahwa tipe numerik mematuhi aturan perbandingan numerik normal: jika dua angka dibandingkan dan sama (misalnya, 1 dan 1.0), hanya salah satunya yang dapat dimasukkan ke dalam himpunan.

# Saat ini ada dua jenis himpunan yang intrinsik:

# sets (Sets) Ini mewakili himpunan yang dapat diubah (mutable). Mereka dibuat oleh konstruktor bawaan set() dan dapat dimodifikasi setelahnya dengan beberapa metode, seperti add().

# Frozen sets Ini mewakili himpunan yang tidak dapat diubah (immutable). Mereka dibuat oleh konstruktor bawaan frozenset(). Karena frozenset tidak dapat diubah dan dapat di-hash, ia dapat digunakan kembali sebagai elemen dari himpunan lain, atau sebagai kunci dalam kamus (dictionary).

# 7. Mappings / denah
# Ini mewakili himpunan terbatas dari objek yang diindeks oleh nilai-nilai yang hampir sewenang-wenang. Satu-satunya jenis nilai yang tidak dapat diterima sebagai kunci adalah nilai yang berisi daftar (lists) atau kamus (dictionaries) atau jenis yang dapat diubah (mutable) lainnya yang dibandingkan berdasarkan nilai daripada berdasarkan identitas objek, karena implementasi kamus yang efisien mengharuskan nilai hash dari kunci tetap konstan. Tipe numerik yang digunakan sebagai kunci mengikuti aturan perbandingan numerik normal: jika dua angka dibandingkan dan sama (misalnya, 1 dan 1.0), maka mereka dapat digunakan secara bergantian untuk mengindeks entri kamus yang sama.

# dictionary (dictionaries) mempertahankan urutan penyisipan, yang berarti kunci akan dihasilkan dalam urutan yang sama dengan saat mereka ditambahkan secara berurutan ke dalam dictionary. Mengganti kunci yang ada tidak mengubah urutannya, namun menghapus kunci dan menambahkannya kembali akan menambahkannya ke akhir alih-alih mempertahankan posisinya yang lama.

# dictionary bersifat mutable (dapat diubah); mereka dapat dibuat menggunakan notasi {...} (lihat bagian tampilan dictionary).

# Modul ekstensi dbm.ndbm dan dbm.gnu memberikan contoh tambahan dari tipe pemetaan, demikian juga dengan modul collections.

# 8. callable