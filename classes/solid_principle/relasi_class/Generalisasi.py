# Generalization adalah proses di mana kita mengidentifikasi atribut dan perilaku umum dari beberapa kelas dan menggabungkannya ke dalam kelas yang lebih umum atau induk

# contoh

class HewanPeliharaan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        pass  # Ini akan diimplementasikan di kelas turunan

class Kucing(HewanPeliharaan):
    def bersuara(self):
        return "Meow"

class Anjing(HewanPeliharaan):
    def bersuara(self):
        return "Bark"

# Penggunaan
kucing1 = Kucing("Kitty")
anjing1 = Anjing("Buddy")

print(f"{kucing1.nama}: {kucing1.bersuara()}")  # Output: Kitty: Meow
print(f"{anjing1.nama}: {anjing1.bersuara()}")  # Output: Buddy: Bark

