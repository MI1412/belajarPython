# Dalam Python, dimungkinkan untuk menulis program yang menangani **exceptions** tertentu. Contohnya, program berikut meminta pengguna memasukkan angka hingga angka yang valid dimasukkan, tetapi tetap memungkinkan pengguna menghentikan program (misalnya, menggunakan Control-C atau sesuai dukungan sistem operasi), yang akan menghasilkan **KeyboardInterrupt**.

# ```python
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
# ```

# **Penjelasan `try` statement**:
# 1. Pertama, blok `try` dieksekusi.
# 2. Jika tidak ada exception, blok `except` dilewati, dan eksekusi selesai.
# 3. Jika ada exception, eksekusi blok `try` dihentikan dan masuk ke blok `except`.
# 4. Jika exception tidak cocok dengan yang ada di `except`, diteruskan ke luar, dan jika tidak ada penanganan lain, program berhenti dengan pesan error.

# Anda dapat memiliki lebih dari satu blok `except` untuk menangani exceptions berbeda. Sebagai contoh:

# ```python
# except (RuntimeError, TypeError, NameError):
#     pass
# ```

# Kelas dalam `except` akan menangkap exceptions yang merupakan turunan dari kelas tersebut. Misalnya:

# ```python
# class B(Exception): pass
# class C(B): pass
# class D(C): pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")
# ```

# Jika urutan `except` diubah, hasil cetak akan berbeda karena urutan blok menentukan yang akan ditangkap pertama kali.

# Exceptions juga bisa memiliki nilai terkait (arguments). Misalnya:

# ```python
# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     print(inst)
#     x, y = inst.args
#     print('x =', x)
#     print('y =', y)
# ```

# **BaseException** adalah kelas dasar dari semua exceptions, dengan **Exception** sebagai kelas dasar untuk exceptions non-fatal. Exceptions yang tidak diturunkan dari **Exception** biasanya tidak ditangani karena mengindikasikan program harus dihentikan (seperti **SystemExit** dan **KeyboardInterrupt**).

# Saat menangani exceptions, lebih baik menangkap exceptions spesifik, dan biarkan exceptions tak terduga diteruskan ke penanganan lebih lanjut.

# Contoh umum penanganan exceptions:

# ```python
# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise
# ```

# Blok `else` opsional dapat digunakan setelah semua blok `except`, dan digunakan jika tidak ada exception yang terjadi di blok `try`.

# ```python
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()
# ```

# Blok `else` lebih baik daripada menambahkan kode ekstra di blok `try`, karena membantu menghindari menangkap exception yang tidak diinginkan.

# Penanganan exceptions juga berlaku untuk fungsi yang dipanggil di dalam blok `try`:

# ```python
# def this_fails():
#     x = 1/0

# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)
# ```

# #### Kesimpulan:

# 1. **`try-except` Statement**: Python menyediakan cara untuk menangani exceptions yang memungkinkan kode tetap berjalan meskipun terjadi kesalahan.
# 2. **Multiple Handlers**: Blok `try` dapat memiliki beberapa blok `except` untuk menangani jenis exceptions yang berbeda.
# 3. **Hierarki Exceptions**: Exceptions dapat diatur dalam hierarki kelas, dan blok `except` akan menangkap exceptions yang sesuai dengan urutan blok.
# 4. **Exception Arguments**: Exceptions dapat menyimpan nilai atau argumen terkait, yang dapat diakses dan digunakan dalam penanganan kesalahan.
# 5. **Best Practices**: Gunakan penanganan exceptions yang spesifik dan hindari penggunaan penanganan yang terlalu umum, kecuali memang diperlukan.

# Ini memungkinkan program tetap stabil dan lebih mudah di-debug jika terjadi kesalahan saat runtime.