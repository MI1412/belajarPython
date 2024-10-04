# Specialization adalah kebalikan dari generalization. Ini adalah proses di mana kita mengambil kelas umum dan membuat kelas-kelas yang lebih spesifik dengan menambahkan atribut atau perilaku tambahan.

# contoh
class HewanPeliharaan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        pass

class Kucing(HewanPeliharaan):
    def __init__(self, nama, ras):
        super().__init__(nama)
        self.ras = ras

    def bersuara(self):
        return "Meow"

class Anjing(HewanPeliharaan):
    def __init__(self, nama, ukuran):
        super().__init__(nama)
        self.ukuran = ukuran

    def bersuara(self):
        return "Bark"

# Penggunaan
kucing1 = Kucing("Kitty", "Persia")
anjing1 = Anjing("Buddy", "Sedang")

print(f"{kucing1.nama}: {kucing1.bersuara()}, Ras: {kucing1.ras}")  # Output: Kitty: Meow, Ras: Persia
print(f"{anjing1.nama}: {anjing1.bersuara()}, Ukuran: {anjing1.ukuran}")  # Output: Buddy: Bark, Ukuran: Sedang

