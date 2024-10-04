#Liskov Substitution Principle (LSP), Subkelas harus dapat digunakan sebagai pengganti superclass tanpa menyebabkan masalah pada program.

# contoh:
class Bird:
    def make_sound(self):
        pass

class Sparrow(Bird):
    def make_sound(self):
        return "Tweet!"

class Penguin(Bird):
    def make_sound(self):
        return "Squawk!"
    
    # Jangan menambahkan fly() karena penguin tidak bisa terbang
