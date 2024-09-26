# Operator yang Dapat Digunakan dalam Kondisi: Python memungkinkan penggunaan operator apa pun dalam kondisi while dan if, bukan hanya operator perbandingan.

# Operator Perbandingan:

# in dan not in: Operator ini memeriksa apakah sebuah nilai ada atau tidak ada dalam sebuah container (misalnya list atau string).
# is dan is not: Operator ini membandingkan apakah dua objek adalah objek yang sama (bukan hanya memiliki nilai yang sama).
# Prioritas Operator: Operator perbandingan memiliki prioritas yang lebih rendah daripada operator numerik. Semua operator perbandingan memiliki prioritas yang sama.

# Chaining (Penghubungan) Perbandingan: Anda bisa menghubungkan beberapa perbandingan dalam satu ekspresi, seperti a < b == c, yang memeriksa apakah a kurang dari b dan apakah b sama dengan c.

# Operator Boolean:

# and, or, not: Operator boolean ini bisa digunakan untuk menggabungkan beberapa perbandingan. Prioritasnya adalah: not memiliki prioritas tertinggi, diikuti oleh and, dan or memiliki prioritas terendah.
# Short-circuiting: Evaluasi ekspresi berhenti begitu hasilnya sudah bisa ditentukan. Contohnya, jika A benar, tetapi B salah, maka ekspresi A and B and C tidak mengevaluasi C.
# Menggunakan Hasil Perbandingan sebagai Nilai: Hasil dari perbandingan atau ekspresi boolean bisa disimpan dalam variabel, seperti pada contoh non_null.

# Operator Walrus (:=): Python membutuhkan penggunaan eksplisit dari operator walrus untuk melakukan penugasan dalam ekspresi. Ini menghindari kesalahan yang sering terjadi di bahasa lain, seperti C, di mana = bisa tertukar dengan ==.

# 1.Penggunaan in dan not in:
numbers = [1, 2, 3, 4]
if 3 in numbers:
    print("3 ada dalam list")

# 2.Penggunaan is dan is not:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, krn variabel referensinya sama
print(a is c)

# 3.Chaining Perbandingan:
a = 5
b = 5
c = 10

if a < c == b:
    print("a kurang dari c dan b sama dengan c")

# 4.Short-Circuiting:
A = True
B = False
C = True

result = A and B and C  # B salah, jadi C tidak dievaluasi
print(result)  # Output: False

# 5.Menggunakan Hasil Perbandingan dalam Variabel:
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)  # Output: 'Trondheim'

# 6.Operator Walrus (:=):
while (num := int(input("Enter a number: "))) > 0:
    print(f"You entered {num}")
# Penugasan dilakukan di dalam ekspresi dengan := 
