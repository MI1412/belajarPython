# beberapa definisi function

# funcdef                   ::=  [decorators] "def" funcname [type_params] "(" [parameter_list] ")"
#                                ["->" expression] ":" suite
# decorators                ::=  decorator+
# decorator                 ::=  "@" assignment_expression NEWLINE
# parameter_list            ::=  defparameter ("," defparameter)* "," "/" ["," [parameter_list_no_posonly]]
#                                  | parameter_list_no_posonly
# parameter_list_no_posonly ::=  defparameter ("," defparameter)* ["," [parameter_list_starargs]]
#                                | parameter_list_starargs
# parameter_list_starargs   ::=  "*" [parameter] ("," defparameter)* ["," ["**" parameter [","]]]
#                                | "**" parameter [","]
# parameter                 ::=  identifier [":" expression]
# defparameter              ::=  parameter ["=" expression]
# funcname                  ::=  identifier

# Ini adalah **grammar** atau aturan sintaksis yang mendefinisikan bagaimana fungsi dideklarasikan dalam Python menggunakan function annotations dan parameter, sesuai dengan PEP 3107. Mari kita jabarkan bagian-bagian penting dari grammar ini:

# 1. **`funcdef`**: Definisi fungsi dimulai dengan kata kunci `def` diikuti dengan nama fungsi (`funcname`), daftar parameter, dan blok kode (`suite`). Jika ada, tipe kembalian fungsi ditunjukkan setelah `->` dan sebelum titik dua `:`.

#    - **`[decorators]`**: Fungsi bisa menggunakan dekorator, yang dideklarasikan dengan simbol `@` diikuti oleh ekspresi.
#    - **`funcname`**: Nama fungsi yang berupa identifier.
#    - **`type_params`**: Menunjukkan parameter tipe (opsional) untuk generik.
#    - **`-> expression`**: Tanda bahwa fungsi mengembalikan tipe yang ditentukan oleh ekspresi (opsional).
#    - **`suite`**: Badan fungsi atau blok kode.

# 2. **`decorators` dan `decorator`**: Dekorator adalah simbol `@` yang ditempatkan di atas definisi fungsi, diikuti oleh ekspresi penugasan. Digunakan untuk memodifikasi atau menghias fungsi.

# 3. **`parameter_list`**: Daftar parameter yang diterima oleh fungsi, terdiri dari satu atau lebih parameter. Parameter bisa dibagi menjadi:
#    - **Positional-only parameters**: Dideklarasikan sebelum tanda `"/"`.
#    - **Non-positional parameters**: Semua parameter yang tidak dibatasi oleh posisionalitas.

# 4. **`parameter_list_starargs`**: Bagian dari daftar parameter yang menunjukkan parameter variabel dengan `*args` (untuk argumen posisi variabel) dan `**kwargs` (untuk argumen kata kunci variabel).

# 5. **`parameter`**: Setiap parameter dapat memiliki anotasi tipe dalam bentuk `identifier : expression`, di mana `expression` adalah anotasi tipe yang menjelaskan tipe parameter tersebut.

# 6. **`defparameter`**: Parameter dengan nilai default. Ini berarti parameter bisa memiliki anotasi tipe dan juga nilai default, dalam bentuk `parameter = expression`.

# 7. **`funcname`**: Nama fungsi yang merupakan identifier.

### Kesimpulan:
# Grammar ini mendefinisikan struktur sintaksis fungsi Python yang mencakup anotasi tipe, dekorator, parameter, dan nilai kembalian. Ini memberikan fleksibilitas dalam mendeklarasikan fungsi dengan berbagai jenis parameter dan anotasi, sambil tetap mengikuti aturan standar Python untuk definisi fungsi.