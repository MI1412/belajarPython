# ### Terjemahan

# **9.6. Variabel Pribadi**

# Variabel instance “pribadi” yang tidak dapat diakses kecuali dari dalam suatu objek tidak ada dalam Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: sebuah nama yang diawali dengan garis bawah (misalnya, `_spam`) harus dianggap sebagai bagian non-publik dari API (baik itu fungsi, metode, atau anggota data). Itu harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.

# Karena ada kasus penggunaan yang valid untuk anggota kelas privat (yaitu untuk menghindari bentrok nama dengan nama yang didefinisikan oleh subclass), ada dukungan terbatas untuk mekanisme semacam itu, yang disebut **name mangling**. Setiap pengidentifikasi dengan bentuk `__spam` (setidaknya dua garis bawah di depan, maksimal satu garis bawah di belakang) secara tekstual digantikan dengan `_classname__spam`, di mana `classname` adalah nama kelas saat ini dengan garis bawah di depan dihapus. Pengacakan ini dilakukan tanpa mempertimbangkan posisi sintaks dari pengidentifikasi, selama itu terjadi dalam definisi kelas.

# Lihat juga spesifikasi pengacakan nama untuk rincian dan kasus khusus.

# Pengacakan nama berguna untuk memungkinkan subclass mengganti metode tanpa merusak panggilan metode dalam kelas. Sebagai contoh:

# ```python
# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)

#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)

#     __update = update   # salinan privat dari metode update() asli

# class MappingSubclass(Mapping):

#     def update(self, keys, values):
#         # menyediakan tanda tangan baru untuk update()
#         # tetapi tidak merusak __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)
# ```

# Contoh di atas akan berfungsi bahkan jika `MappingSubclass` memperkenalkan pengidentifikasi `__update` karena ia digantikan dengan `_Mapping__update` di kelas `Mapping` dan `_MappingSubclass__update` di kelas `MappingSubclass`, masing-masing.

# Perhatikan bahwa aturan pengacakan dirancang terutama untuk menghindari kecelakaan; masih mungkin untuk mengakses atau memodifikasi variabel yang dianggap pribadi. Ini bahkan bisa berguna dalam keadaan khusus, seperti dalam debugger.

# Perhatikan bahwa kode yang diteruskan ke `exec()` atau `eval()` tidak menganggap nama kelas dari kelas yang memanggil sebagai kelas saat ini; ini mirip dengan efek dari pernyataan `global`, yang efeknya juga dibatasi pada kode yang dikompilasi byte bersama. Pembatasan yang sama berlaku untuk `getattr()`, `setattr()`, dan `delattr()`, serta saat merujuk langsung ke `__dict__`.

# ### Kesimpulan

# Dokumentasi ini menjelaskan tentang konsep variabel pribadi dalam Python. Meskipun Python tidak memiliki variabel pribadi yang sebenarnya, ia menggunakan konvensi penamaan dengan garis bawah untuk menandakan bahwa suatu variabel bersifat non-publik. Selain itu, terdapat mekanisme **name mangling** yang mengubah nama variabel untuk membantu menghindari bentrok antara kelas dasar dan kelas turunan. Ini memungkinkan metode dalam kelas dasar dipanggil dengan aman meskipun ada metode dengan nama yang sama di subclass.

# ### Contoh Penggunaan

# Berikut adalah contoh penggunaan variabel pribadi dan name mangling dalam Python:

# ```python
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # variabel pribadi

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Deposited: {amount}, New Balance: {self.__balance}")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawn: {amount}, New Balance: {self.__balance}")
#         else:
#             print("Insufficient funds")

# # Penggunaan
# account = BankAccount(100)
# account.deposit(50)      # Output: Deposited: 50, New Balance: 150
# account.withdraw(30)     # Output: Withdrawn: 30, New Balance: 120

# # Mencoba mengakses __balance secara langsung akan menyebabkan kesalahan
# # print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# # Namun, Anda masih dapat mengaksesnya menggunakan name mangling
# print(account._BankAccount__balance)  # Output: 120
# ```

# Dalam contoh ini, `__balance` adalah variabel pribadi yang tidak dapat diakses langsung dari luar kelas. Meskipun demikian, Anda dapat mengaksesnya menggunakan nama yang telah di-mangle, yaitu `_BankAccount__balance`.