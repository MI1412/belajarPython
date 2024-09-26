# ### Terjemahan

# Iterators  
# Saat ini, Anda mungkin telah memperhatikan bahwa sebagian besar objek kontainer dapat dilalui menggunakan pernyataan for:

# ```python
# for element in [1, 2, 3]:
#     print(element)
# for element in (1, 2, 3):
#     print(element)
# for key in {'one': 1, 'two': 2}:
#     print(key)
# for char in "123":
#     print(char)
# for line in open("myfile.txt"):
#     print(line, end='')
# ```

# Gaya akses ini jelas, ringkas, dan nyaman. Penggunaan iterators meresap dan menyatukan Python. Di balik layar, pernyataan for memanggil `iter()` pada objek kontainer. Fungsi ini mengembalikan objek iterator yang mendefinisikan metode `__next__()` yang mengakses elemen dalam kontainer satu per satu. Ketika tidak ada lagi elemen, `__next__()` akan mengangkat pengecualian `StopIteration` yang memberi tahu loop for untuk berhenti. Anda dapat memanggil metode `__next__()` menggunakan fungsi bawaan `next()`. Contoh berikut menunjukkan cara kerjanya:

# ```python
# s = 'abc'
# it = iter(s)
# print(next(it))  # Output: 'a'
# print(next(it))  # Output: 'b'
# print(next(it))  # Output: 'c'
# print(next(it))  # Raises StopIteration
# ```

# Setelah melihat mekanisme di balik protokol iterator, mudah untuk menambahkan perilaku iterator ke kelas Anda. Definisikan metode `__iter__()` yang mengembalikan objek dengan metode `__next__()`. Jika kelas mendefinisikan `__next__()`, maka `__iter__()` cukup mengembalikan `self`:

# ```python
# class Reverse:
#     """Iterator untuk melintasi urutan secara terbalik."""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]

# rev = Reverse('spam')
# for char in rev:
#     print(char)
# ```

# ### Kesimpulan

# Dokumentasi ini menjelaskan cara kerja **iterators** di Python, di mana objek kontainer dapat dilalui menggunakan pernyataan `for`. Protokol iterator memungkinkan Anda untuk mengakses elemen satu per satu, dan jika tidak ada lagi elemen yang tersisa, pengecualian `StopIteration` akan diangkat untuk menghentikan loop. Anda juga dapat membuat kelas kustom dengan perilaku iterator dengan mendefinisikan metode `__iter__()` dan `__next__()`.

# ### Contoh Penggunaan

# Berikut adalah contoh penggunaan iterator yang dibuat sendiri untuk membalik urutan sebuah string:

# ```python
# class Reverse:
#     """Iterator untuk melintasi urutan secara terbalik."""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]

# # Menggunakan iterator Reverse
# rev = Reverse('hello')
# for char in rev:
#     print(char)
# ```

# **Output:**
# ```
# o
# l
# l
# e
# h
# ```

# Dalam contoh ini, kelas `Reverse` memungkinkan Anda untuk melintasi string "hello" secara terbalik, mencetak setiap karakter dari belakang ke depan.