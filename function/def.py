
# definisikan ini function
def fib(n):
    """print a fibonacci contoh docstring"""
    a, b = 0,1
    while a < n :
        print(a, end=' ')
        a,b = b, a+b
    print()

# default value = none 
print(fib(0))

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result
f100 = fib2(100) # calling function
print(f"f100: {f100}")               


# <--default argument
def test(n=9 ):
    pass

# contoh lain
def ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('batas telah habis')
        print(reminder)

print(ok('masukkan y/n: ', 5, 'ulangi lagi'))


# definisi scopes

i = 7 # 
def p(arg=i):# i akan mengambil var diatas
    print(arg)
# i = 6 tidak akan ditampilkan
p()    

# hati hati pada saat membuat default argumen array, karena datanya dapat berubah ubah
# def addList(a, l=[]):
#     l.append(a)
#     return l
# print(addList(1))
# print(addList(2))
# print(addList(3))

# gunakan default argumen none kemudia kelola
def addList(a,l=None):
    if l is None:
        l=[]
    l.append(a)
    return l
print(addList(9))
# print(addList(9))

# keyword argumen lihat di keyword argumen
# keyword agumen
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

def function(a=0):
    pass
# function(0, a=0) ini salah karena argumen a ada banyak

# fungsi memiliki parameter **name, parameter tersebut akan menerima sebuah dictionary berisi semua keyword arguments yang tidak sesuai dengan parameter formal yang sudah didefinisikan.
# Selain itu, fungsi bisa memiliki parameter *name, yang menerima tuple berisi positional arguments tambahan. Penting bahwa *name harus muncul sebelum **name.
def contoh_fungsi(pos1, *args, kwarg1=None, **kwargs):
    print(f"Pos 1: {pos1}, Posisi tambahan: {args}, kata kunci ke-1: {kwarg1}, beberapa kata kunci tambahan: {kwargs}")

contoh_fungsi(1, 2, 3, kwarg1=4, kwarg2=5,kwarg3=6)
# Pos 1: 1, Posisi tambahan: (2, 3), kwarg1: 4, Kata kunci tambahan: {'kwarg2': 5}

# <--parameter spesial
# special parameters adalah parameter fungsi yang memiliki sintaks khusus untuk menangani argumen dengan cara tertentu. Mereka meliputi:

# standart
def standart(arg):
    print(arg)
    

# 1. *args
def fungsi(*a):
    # iterable dari beberapa argumen
    for arg in a:
        print(arg)

fungsi({9,0,8,21,112})

# 2. **kwargs
def fungsi(**kwargs):
    # iterable dari beberapa keyword
    for key, value in kwargs.items():
        print(f"{key} = {value}")

fungsi(a=1, b=2, c=3)

# 3. *(Positional-Only keyword):
# Menandai bahwa parameter sebelum * harus dipanggil sebagai argumen posisi saja dan tidak bisa dipanggil dengan nama, ini bisa memisahkan kwarg dengan arg
def fungsi(a, b, *, c, d):
    print(a, b, c, d)
    
def post_only_kw(*,arg):
    print(arg)

fungsi(a=4,b=1,c=1,d=6) # bisa pakai kwarg bisa tidak sebelum * setelahnya harus panggil dengan kwarg

# 4. /  (Positional-Only argumen):
# Menandai bahwa parameter sebelum / hanya bisa dipanggil dengan posisi dan tidak bisa dipanggil dengan nama, ini bisa memisahkan kwarg dengan arg

def fungsi(a, b, /, c, d):
    print(a, b, c, d)

def post_only_arg(arg,/):
    print(arg)

fungsi(1, 2, 3, d=4)

# contoh kombinasi
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standart(102)
post_only_arg(19)
post_only_kw(arg=19)
combined_example(19,2,kwd_only=10)

# hati hati pada saat menggunakan arg,/,**kwargs, karena bisa mengakses arggumen sebelumnya, ini akan menjadi kode ambigu
def foo(name, /,**kwds):
    return 'name' in kwds

print(foo('asep',name="asep"))

# <--kesimpulan
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

# Sebagai panduan:
# Gunakan positional-only jika Anda tidak ingin nama parameter tersedia untuk pengguna. Ini berguna ketika nama parameter tidak memiliki makna yang nyata, jika Anda ingin menegakkan urutan argumen saat fungsi dipanggil, atau jika Anda perlu menerima beberapa parameter posisi dan kata kunci yang sembarang.

# Gunakan keyword-only ketika nama parameter memiliki makna dan definisi fungsi menjadi lebih mudah dipahami dengan menyebutkan nama parameter secara eksplisit, atau jika Anda ingin mencegah pengguna bergantung pada posisi argumen yang diteruskan.

# Untuk API, gunakan positional-only untuk mencegah perubahan yang merusak API jika nama parameter dimodifikasi di masa depan.

# <--daftar list argumen sembarangan
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

# Membuka file untuk menulis
with open('output.txt', 'w') as file:
    # Memanggil fungsi dengan pemisah koma dan beberapa item
    write_multiple_items(file, ', ', 'apple', 'banana', 'cherry')


# daftar argumen yang sembarangan
# Biasanya, argumen variadic (parameter *args) akan menjadi yang terakhir dalam daftar parameter formal, karena mereka menangkap semua argumen yang tersisa yang diteruskan ke fungsi. Parameter formal yang muncul setelah parameter *args adalah argumen ‘hanya-kata-kunci’ (keyword-only arguments), yang berarti mereka hanya dapat digunakan sebagai argumen kata kunci, bukan sebagai argumen posisi.

def concat_arg(*args, sep="/"):
    print(sep.join(args))

concat_arg('a','b','c',sep=',')

def concat_kw(sep=None, **kwargs):
    print(sep.join(kwargs))
concat_kw(sep='/',kwargs='tes',namaa='imron',alamat='SBY')

# <--membongkar list argumen
def tes_bongkar_argumen(tes,a=9,nama='anonimous'):
    print(f"a: {a} tes: {tes} nama: {nama}")
pack = {'a':6,'tes':'p','nama':'asep'}
tes_bongkar_argumen(**pack)
print(list(range(1,10)))

v = [1,5] #iterable
print(list(range(*v))) # perlu *var krn iterable

# contoh lain 
def funct(key="value"):
    print(key)
funct_contoh = {'key':'ini diubah'}
funct(funct_contoh)

# lambda
# lihat di file lambda.py

# docstring
# digunakan untuk menampilkan deskripsi fungsi
# """"""

# function annotation
# digunakan untuk menambahkan informasi tambahan pada fungsi tanpa memengaruhi eksekusi kode
# help(__annotations__)
def say_hi(name:str)->str:
    print(f"annotations: {say_hi.__annotations__}")
    print(f'hai saya {name}')

say_hi(90)
# di hints: keluar name:str, ini berarti menunjukkan var name tipe data str 
# funct(arg)->bool, menujukkan funct ini return bool 
# perlu diingat function annotation digunakan untuk memberi petunjuk agar mudah mengembangkan kode
# untuk melihat annotasi apa yang dikeluarkan: dengan nama_funct.__annotations__


