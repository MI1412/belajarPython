# error adalah pada saat proses terjadi kesalahan syntax pada saat runtime
# exception adalah sebuah kesalahan pada saat menulis kode, yang dimana kesalahan itu bisa diubah

# syntax error
# >>> while True print('Hello world')
#   File "<stdin>", line 1
    # while True print('Hello world')
            #    ^^^^^
# SyntaxError: invalid syntax

# exception
# >>> 10 * (1/0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>> 4 + spam*3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'spam' is not defined
# >>> '2' + 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str

# <--except handling

# try:
#     a = 10 * (1/0)
# except (KeyboardInterrupt,InterruptedError,ZeroDivisionError) as e:
#     print("error exception: ",e)

# # <--except in class
# class a (Exception):
#     pass
# class b (a):
#     pass
# class c (b):
#     pass

# for cls in [a,b,c]:
#     try:
#         raise cls()
#     except c:
#         print(f"tipe {c}")
#         print("c")
#     except b:
#         print("b")
#     except a:
#         print("a")

# exception dgn argumen
# try:
#     raise Exception('tes','1')
# except Exception as e:
#     print(f"tipe: {type(e)}")
#     print(f"args: {e.args}")
#     print(f"e: {e}")
#     a,b = e.args # set var dari beberapa argumen menggunakan args
#     print(f"a,b= {a,b}")

# menggunakan log untuk menyimpan exception
# try:
#     f = open(' ')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print(f"\nos error: {err}")
# except ValueError:
#     print("\ntidak bisa convert")
# except Exception as err:
#     print(f"\nSIAPA SANGKA: {err=}, type{type(err)=}")
#     raise

# function handling error
# def fail()->None:
#     a = 1/0
#     print(a)

# try:
#     fail()
# except ZeroDivisionError as err:
#     print(f"menangani error saat berjalan: {err}")


# raise
# try:
#     raise NameError("SIAPA SANGKA ERROR")
# except NameError:
#     print("\nsatu exception ditemukan:")
#     raise # menaikkan raise exception yang dibuat


# <--exception berantai
# try:
#     open("data.sqlite")
# except OSError as e:
#     raise RuntimeError("error tidak bisa menghandle file") from e

# ini bisa digunakan saat mengubah exception, contoh
# def funct():
#     raise ConnectionError
# try:
#     funct()
# except ConnectionError as e:
#     raise RuntimeError("gagal membuka database") from e


# mengembalikan pesan kosong
# try:
#     open("data.txt")
# except OSError:
#     raise RuntimeError()

# membuat exception sendiri
# class kesalahan(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#         super().__init__(self.msg)
    
# def nilaiKosong(value):
#     if value <= 0:
#         raise kesalahan("tidak boleh kosong atau minus")
    
# try:
#     nilaiKosong(0)
# except kesalahan as err:
#     print(f"KESALAHAN: {err.msg}")

# <--finally
# def logika()->bool:
#     try:
#         return True
#     finally:
#         return False
# print(logika())

# jika dibanding denga ini
# def divide(x:int,y:int)->int:
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("\ntidak boleh dibagi dengan kosong !!") 
#     except TypeError:
#         print("\nformat harus int !!!")
#     else:
#         print(f"\nhasil: {result}")
#     finally:
#         print("eksekusi berhenti\n")

# divide("1","19")

# <--memicu exception dan menangani exception
# def f():
#     excs = [OSError('os error coy'), SystemError('system error')]
#     raise ExceptionGroup("sepertinya ada masalah",excs)
# try:
#     f()
# except Exception as e:
#     print(f"tipe: {type(e)}\n")
# print(f"Exception Grup: {f()}")

# <--memicu exception dan menangani exception dengan exception * dan mengakses exception
# def error():
#     raise ExceptionGroup("grup pertama",[OSError("os error1"),OSError("os error3"),SystemError("sys error1"),SystemError("sys error2"),OSError("os error2"),ExceptionGroup("grup kedua",[OSError("os error3"),SystemError("sys error3"),OSError("os error4"),RecursionError("ini error rekursif")])])
# try:
#     error()
# except * OSError as e:
#     print(f"ini os error : ada {len(e.exceptions)}\ntype: {type(e)}")
#     # mengambil semua isi except
#     for i in e.exceptions:
#         print(f"grup pertama: {i}")
#         if isinstance(i,ExceptionGroup):
#             for n in i.exceptions:
#                 print(f"grup kedua: {n}")
# except* SystemError as e:
#     print(f"ini sys error: ada {len(e.exceptions)}\ntype: {type(e)}")
#     for n in e.exceptions:
#         print(f"grup pertama: {n}")
#         if isinstance(n,ExceptionGroup):
#             for i in n.exceptions:
#                 print(f"grup kedua: {i}")


class Test:
    def __init__(self, name, should_fail=False):
        self.name = name
        self.should_fail = should_fail

    def run(self):
        if self.should_fail:
            raise ValueError(f"Test '{self.name}' gagal.")
        else:
            print(f"Test '{self.name}' dilewatkan.")

# Membuat daftar tes
tests = [
    Test("Test 1"),  # Tes ini berhasil
    Test("Test 2", should_fail=True),  # Tes ini gagal
    Test("Test 3"),  # Tes ini berhasil
    Test("Test 4", should_fail=True),  # Tes ini gagal
]

excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e) # menambahkan error ke list
for i in excs:
    print(f"error: {i}")

# <--mencatat exceptions menggunakan method add_note("pesan")
# try:
#     raise TypeError("type ga jelas")
# except Exception as e:
#     e.add_note("error bro")
#     e.add_note(f"error bro: {e}")
#     raise

# contoh mengoleksi exceptions
def funct():
    raise OSError("operasi dibatalkan")
excs = []
for i in range(3):
    try:
        funct()
    except Exception as e:
        e.add_note(f"exception ditambahkan {i+1}")
        excs.append(e)

print(excs)
for i in excs:
    print(i)
if excs:
    exc_group = ExceptionGroup("kita dapat error bro: ",excs)

for i in exc_group.exceptions:
    print(f"\nexceptions: {i}")
    print(f"\nnote: {i.__notes__}")