# ### Terjemahan

# Tentu saja, sebuah fitur bahasa tidak akan layak disebut "kelas" tanpa mendukung pewarisan. Sintaks untuk mendefinisikan kelas turunan terlihat seperti ini:

# ```python
# class DerivedClassName(BaseClassName):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# ```

# Nama `BaseClassName` harus didefinisikan dalam ruang nama yang dapat diakses dari lingkup yang berisi definisi kelas turunan. Sebagai pengganti nama kelas dasar, ekspresi arbitrarial lainnya juga diperbolehkan. Ini bisa berguna, misalnya, ketika kelas dasar didefinisikan di modul lain:

# ```python
# class DerivedClassName(modname.BaseClassName):
# ```

# Eksekusi definisi kelas turunan berlangsung sama seperti untuk kelas dasar. Ketika objek kelas dibuat, kelas dasar diingat. Ini digunakan untuk menyelesaikan referensi atribut: jika atribut yang diminta tidak ditemukan dalam kelas, pencarian dilanjutkan untuk mencari di kelas dasar. Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri diturunkan dari kelas lain.

# Tidak ada yang istimewa tentang instansiasi kelas turunan: `DerivedClassName()` membuat instance baru dari kelas tersebut. Referensi metode diselesaikan sebagai berikut: atribut kelas yang sesuai dicari, menurun ke bawah rantai kelas dasar jika perlu, dan referensi metode valid jika ini menghasilkan objek fungsi.

# Kelas turunan dapat menggantikan metode dari kelas dasar mereka. Karena metode tidak memiliki hak istimewa saat memanggil metode lain dari objek yang sama, metode dari kelas dasar yang memanggil metode lain yang didefinisikan dalam kelas dasar yang sama mungkin akhirnya memanggil metode dari kelas turunan yang menggantikannya. (Untuk programmer C++: semua metode di Python secara efektif adalah virtual.)

# Metode yang menggantikan di kelas turunan mungkin sebenarnya ingin memperluas daripada sekadar mengganti metode kelas dasar dengan nama yang sama. Ada cara sederhana untuk memanggil metode kelas dasar secara langsung: cukup panggil `BaseClassName.methodname(self, arguments)`. Ini kadang-kadang berguna bagi klien juga. (Perhatikan bahwa ini hanya berfungsi jika kelas dasar dapat diakses sebagai `BaseClassName` dalam ruang lingkup global.)

# Python memiliki dua fungsi bawaan yang bekerja dengan pewarisan:

# - Gunakan `isinstance()` untuk memeriksa tipe instance: `isinstance(obj, int)` akan True hanya jika `obj.__class__` adalah `int` atau beberapa kelas yang diturunkan dari `int`.
# - Gunakan `issubclass()` untuk memeriksa pewarisan kelas: `issubclass(bool, int)` adalah True karena `bool` adalah subclass dari `int`. Namun, `issubclass(float, int)` adalah False karena `float` bukan subclass dari `int`.

# #### Pewarisan Berganda

# Python juga mendukung bentuk pewarisan berganda. Definisi kelas dengan beberapa kelas dasar terlihat seperti ini:

# ```python
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# ```

# Untuk sebagian besar tujuan, dalam kasus yang paling sederhana, Anda dapat menganggap pencarian atribut yang diwarisi dari kelas induk sebagai pencarian kedalaman pertama, dari kiri ke kanan, tanpa mencari dua kali di kelas yang sama di mana ada tumpang tindih dalam hierarki. Jadi, jika atribut tidak ditemukan di `DerivedClassName`, itu dicari di `Base1`, kemudian (secara rekursif) di kelas dasar `Base1`, dan jika tidak ditemukan di sana, dicari di `Base2`, dan seterusnya.

# Faktanya, ini sedikit lebih kompleks dari itu; urutan resolusi metode berubah secara dinamis untuk mendukung panggilan kooperatif ke `super()`. Pendekatan ini dikenal di beberapa bahasa pewarisan berganda lainnya sebagai `call-next-method` dan lebih kuat daripada panggilan `super` yang ditemukan dalam bahasa pewarisan tunggal.

# Pengurutan dinamis diperlukan karena semua kasus pewarisan berganda menunjukkan satu atau lebih hubungan berlian (di mana setidaknya satu dari kelas induk dapat diakses melalui beberapa jalur dari kelas yang paling bawah). Misalnya, semua kelas mewarisi dari objek, jadi setiap kasus pewarisan berganda memberikan lebih dari satu jalur untuk mencapai objek. Untuk menjaga kelas dasar tidak diakses lebih dari sekali, algoritma dinamis menglineariskan urutan pencarian dengan cara yang mempertahankan urutan kiri ke kanan yang ditentukan dalam setiap kelas, memanggil setiap induk hanya sekali, dan bersifat monoton (artinya, sebuah kelas dapat diturunkan tanpa mempengaruhi urutan prioritas induknya). Secara keseluruhan, properti ini memungkinkan perancangan kelas yang andal dan dapat diperluas dengan pewarisan berganda.

# ### Kesimpulan

# Dokumentasi ini menjelaskan pentingnya pewarisan dalam pemrograman berorientasi objek menggunakan Python, menjelaskan bagaimana kelas turunan didefinisikan, serta cara kerja pewarisan berganda. Python memfasilitasi pencarian metode dan atribut melalui hierarki kelas, memungkinkan untuk menggunakan metode dari kelas dasar dalam kelas turunan dan memberikan cara untuk memeriksa tipe instance dan pewarisan kelas.

# ### Contoh Penggunaan

# Berikut adalah contoh penggunaan pewarisan dan pewarisan berganda dalam Python:

# ```python
# # Kelas dasar
# class Animal:
#     def speak(self):
#         return "Animal speaks"

# # Kelas dasar kedua
# class Pet:
#     def owner(self):
#         return "This pet has an owner."

# # Kelas turunan yang mewarisi dari dua kelas dasar
# class Dog(Animal, Pet):
#     def speak(self):
#         return "Dog barks"

# # Menggunakan kelas turunan
# dog_instance = Dog()
# print(dog_instance.speak())  # Output: Dog barks
# print(dog_instance.owner())   # Output: This pet has an owner.
# ```

# Dalam contoh di atas, `Dog` mewarisi dari kelas `Animal` dan `Pet`, dan bisa menggunakan metode dari kedua kelas dasar tersebut. Metode `speak` di kelas `Dog` menggantikan metode `speak` di kelas `Animal`.