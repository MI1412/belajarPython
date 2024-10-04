# Komposisi adalah hubungan yang lebih kuat daripada agregasi. Dalam komposisi, satu kelas memiliki objek dari kelas lain sebagai bagian dari dirinya.

# contoh:
class Mesin:
    def __init__(self, tipe):
        self.tipe = tipe

class Mobil:
    def __init__(self, merek):
        self.merek = merek
        self.mesin = Mesin("Mesin V8")  # Mobil memiliki mesin

# Penggunaan
mobil1 = Mobil("Toyota")

# Menampilkan informasi mobil dan mesinnya
print(f"Merek Mobil: {mobil1.merek}, Tipe Mesin: {mobil1.mesin.tipe}")

