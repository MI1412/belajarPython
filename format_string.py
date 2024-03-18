# format string
# contoh umum 
# string
a = "imron"
format_str = f"halo {a}"
print(format_str)

# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka 
angka = 2005.7
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 105
format_str = f"bilangan bulat = {angka:d}" # :d digunakan untuk mendeklair bahwa angka itu bilangan bulat
print(format_str)

# bilangan ribuan
angka = 2000
format_str = f"bilangan = {angka:,}"
print(format_str)

# bilangan decimal 
angka = 2005.7979
format_str = f"decimal = {angka:.4f}"
print(format_str)

# menampilkan leading zero
angka = 2005.7979
format_str = f"decimal = {angka:010.4f}"
print(format_str)

# menampilkan tanda + atau - 
angka_minus = -10
angka_positif = 10
# contoh decimal
decimal_minus =  -10.1200
decimal_positif = 10.1200
format_min = f"decimal min = {decimal_minus:-.2f}" # harus menambahkan f dikarenakan tipe datanya float
format_positif = f"decimal positif = {decimal_positif:+.2f}" # harus menambahkan f dikarenakan tipe datanya float
print(format_min)
print(format_positif)
format_min = f"minus = {angka_minus:-d}" # harus menambahkan d dikarenakan tipe datanya integer / angka bulat
format_positif = f"positif = {angka_positif:+d}"
print(format_min)
print(format_positif)

# format persen
persen = 1
format_persen = f"persen = {persen:.0%}"
print(format_persen)

# didalam kurung kurawal {} bisa melakukan operasi aritmatika 
harga = 10000
jumlah = 5
format_str = f"harga total = {harga * jumlah:,}"
print(format_str)

# format binary, heksadecimal,octal
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"oktal = {oct(angka)}"
format_heksa =  f"heksadecimal = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_heksa)