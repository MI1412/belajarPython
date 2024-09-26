# ### Terjemahan dan Kesimpulan

# #### Terjemahan
# **Kelas**  
# Kelas menyediakan cara untuk menggabungkan data dan fungsionalitas bersama-sama. Membuat kelas baru menciptakan tipe objek baru, memungkinkan pembuatan instance baru dari tipe tersebut. Setiap instance kelas dapat memiliki atribut yang terlampir untuk mempertahankan statusnya. Instance kelas juga dapat memiliki metode (yang didefinisikan oleh kelasnya) untuk memodifikasi statusnya.

# Dibandingkan dengan bahasa pemrograman lain, mekanisme kelas Python menambahkan kelas dengan minimum sintaksis dan semantik baru. Ini merupakan campuran dari mekanisme kelas yang ditemukan di C++ dan Modula-3. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat mengubah metode dari kelas dasar atau kelas-kelasnya, dan suatu metode dapat memanggil metode dari kelas dasar dengan nama yang sama. Objek dapat berisi jumlah dan jenis data yang tidak terbatas. Seperti halnya modul, kelas berpartisipasi dalam sifat dinamis Python: mereka dibuat pada waktu berjalan, dan dapat dimodifikasi lebih lanjut setelah dibuat.

# Dalam terminologi C++, biasanya anggota kelas (termasuk anggota data) bersifat publik (kecuali jika variabel privat disebutkan di bawah). Seperti di Modula-3, tidak ada singkatan untuk merujuk pada anggota objek dari metodenya: fungsi metode dinyatakan dengan argumen pertama yang eksplisit yang mewakili objek, yang diberikan secara implisit oleh panggilan. Seperti di Smalltalk, kelas itu sendiri adalah objek. Ini memberikan semantik untuk mengimpor dan mengganti nama. Berbeda dengan C++ dan Modula-3, tipe bawaan dapat digunakan sebagai kelas dasar untuk ekstensi oleh pengguna. Selain itu, seperti di C++, sebagian besar operator bawaan dengan sintaksis khusus (operator aritmatika, penyusunan, dll.) dapat didefinisikan ulang untuk instance kelas.

# **Kata tentang Nama dan Objek**  
# Objek memiliki keindividualan, dan beberapa nama (dalam beberapa ruang lingkup) dapat terikat pada objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain. Ini biasanya tidak diperhatikan pada pandangan pertama di Python, dan dapat diabaikan ketika berurusan dengan tipe dasar yang tidak dapat diubah (angka, string, tuple). Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang dapat diubah seperti daftar, kamus, dan sebagian besar tipe lainnya. Ini biasanya digunakan untuk manfaat program, karena alias berperilaku seperti pointer dalam beberapa aspek. Misalnya, melewatkan objek itu murah karena hanya pointer yang diteruskan oleh implementasi; dan jika sebuah fungsi memodifikasi objek yang diteruskan sebagai argumen, pemanggil akan melihat perubahan tersebut — ini menghilangkan kebutuhan untuk dua mekanisme pengiriman argumen yang berbeda seperti dalam Pascal.

# **Lingkup dan Ruang Nama Python**  
# Sebelum memperkenalkan kelas, saya harus memberi tahu Anda sesuatu tentang aturan lingkup Python. Definisi kelas memainkan beberapa trik yang menarik dengan ruang nama, dan Anda perlu mengetahui cara kerja ruang lingkup dan ruang nama untuk sepenuhnya memahami apa yang terjadi. Secara kebetulan, pengetahuan tentang subjek ini berguna bagi setiap pemrogram Python tingkat lanjut.

# Ruang nama adalah pemetaan dari nama ke objek. Sebagian besar ruang nama saat ini diimplementasikan sebagai kamus Python, tetapi biasanya itu tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin berubah di masa depan. Contoh ruang nama adalah: kumpulan nama bawaan (yang berisi fungsi seperti abs(), dan nama-nama pengecualian bawaan); nama global dalam modul; dan nama lokal dalam pemanggilan fungsi. Dalam arti tertentu, kumpulan atribut dari sebuah objek juga membentuk ruang nama. Hal penting yang perlu diketahui tentang ruang nama adalah bahwa tidak ada hubungan antara nama-nama di ruang nama yang berbeda; misalnya, dua modul yang berbeda dapat mendefinisikan fungsi yang sama tanpa kebingungan — pengguna modul harus memberikan awalan dengan nama modul.

# Atribut dapat bersifat hanya baca atau dapat ditulis. Dalam kasus terakhir, penugasan pada atribut dimungkinkan. Atribut modul dapat ditulis: Anda dapat menulis `modname.the_answer = 42`. Atribut yang dapat ditulis juga dapat dihapus dengan pernyataan `del`. Misalnya, `del modname.the_answer` akan menghapus atribut `the_answer` dari objek yang dinamakan oleh `modname`.

# Ruang nama dibuat pada momen yang berbeda dan memiliki masa hidup yang berbeda. Ruang nama yang berisi nama bawaan dibuat saat interpreter Python mulai, dan tidak pernah dihapus. Ruang nama global untuk modul dibuat ketika definisi modul dibaca; biasanya, ruang nama modul juga bertahan sampai interpreter keluar. Pernyataan yang dieksekusi oleh pemanggilan tingkat atas interpreter, baik dibaca dari file skrip atau secara interaktif, dianggap sebagai bagian dari modul yang disebut `__main__`, sehingga mereka memiliki ruang nama global mereka sendiri. (Nama bawaan sebenarnya juga hidup dalam modul; ini disebut builtins.)

# Ruang nama lokal untuk fungsi dibuat ketika fungsi dipanggil, dan dihapus ketika fungsi mengembalikan nilai atau melempar pengecualian yang tidak ditangani di dalam fungsi. (Sebenarnya, melupakan adalah cara yang lebih baik untuk menggambarkan apa yang terjadi.) Tentu saja, pemanggilan rekursif masing-masing memiliki ruang nama lokal mereka sendiri.

# Lingkup adalah wilayah tekstual dari program Python di mana ruang nama dapat diakses langsung. "Dapat diakses langsung" di sini berarti bahwa referensi tanpa kualifikasi untuk nama mencoba mencari nama di ruang nama.

# Meskipun lingkup ditentukan secara statis, mereka digunakan secara dinamis. Pada setiap saat selama eksekusi, terdapat 3 atau 4 lingkup bersarang yang ruang namanya dapat diakses secara langsung:

# - Lingkup terdekat, yang dicari pertama, berisi nama lokal.
# - Lingkup fungsi yang membungkus, yang dicari mulai dari lingkup yang paling dekat, berisi nama non-lokal, tetapi juga non-global.
# - Lingkup kedua terakhir berisi nama global modul saat ini.
# - Lingkup terluar (yang dicari terakhir) adalah ruang nama yang berisi nama bawaan.

# Jika sebuah nama dinyatakan sebagai global, maka semua referensi dan penugasan langsung menuju lingkup kedua terakhir yang berisi nama global modul. Untuk mengikat kembali variabel yang ditemukan di luar lingkup terdekat, pernyataan `nonlocal` dapat digunakan; jika tidak dinyatakan sebagai `nonlocal`, variabel tersebut bersifat hanya baca (upaya untuk menulis variabel tersebut akan membuat variabel lokal baru di lingkup terdekat, meninggalkan variabel luar dengan nama yang sama tidak berubah).

# Biasanya, lingkup lokal merujuk pada nama lokal dari fungsi (secara tekstual) saat ini. Di luar fungsi, lingkup lokal merujuk pada ruang nama yang sama dengan lingkup global: ruang nama modul. Definisi kelas menempatkan ruang nama lain di lingkup lokal.

# Penting untuk menyadari bahwa lingkup ditentukan secara tekstual: lingkup global dari fungsi yang didefinisikan dalam modul adalah ruang nama modul tersebut, tidak peduli dari mana atau oleh alias apa fungsi tersebut dipanggil. Di sisi lain, pencarian sebenarnya untuk nama dilakukan secara dinamis, pada waktu berjalan — namun, definisi bahasa sedang berkembang menuju resolusi nama statis, pada waktu "kompilasi", jadi jangan bergantung pada resolusi nama dinamis! (Sebenarnya, variabel lokal sudah ditentukan secara statis.)

# Keanehan khusus dari Python adalah bahwa — jika tidak ada pernyataan global atau nonlocal yang berlaku — penugasan nama selalu pergi ke lingkup terdekat. Penugasan tidak menyalin data — mereka hanya mengikat nama ke objek. Hal yang sama berlaku untuk penghapusan: pernyataan `del x` menghapus ikatan `x` dari ruang nama yang dirujuk oleh lingkup lokal. Faktanya, semua operasi yang memperkenalkan nama baru menggunakan lingkup lokal: khususnya, pernyataan impor dan definisi fungsi mengikat nama modul atau fungsi di ruang lingkup lokal.

# Pernyataan global dapat digunakan untuk menunjukkan bahwa variabel tertentu berada di ruang lingkup global dan harus diikat ulang di sana; pernyataan nonlocal menunjukkan bahwa variabel tertentu berada di ruang lingkup yang membungkus dan harus diikat ulang di sana.

# ---

# ### Kesimpulan
# Kelas dalam Python menggabungkan data dan fungsionalitas, memungkinkan pembuatan objek dengan berbagai atribut dan metode. Kelas mendukung fitur Pemrograman Berorientasi Objek seperti pewarisan, memungkinkan pengguna untuk memperluas kelas dasar dan mengoverride metode. Python memiliki mekanisme ruang nama yang canggih, di mana objek dapat memiliki nama yang berbeda dalam ruang lingkup yang berbeda, dan ruang nama ini memiliki masa hidup yang berbeda. Lingkup merujuk pada area di mana nama-nama tersebut dapat diakses, dengan hierarki pencarian yang diatur secara statis namun digunakan secara dinamis. Pengetahuan tentang ruang nama dan lingkup penting bagi pemrogram Python untuk memahami cara kerja objek dan kelas dalam kode mereka.