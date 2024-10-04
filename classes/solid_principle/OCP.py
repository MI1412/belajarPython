# Open / Closed Prinsiple (ocp) yaitu Prinsip Terbuka/Tertutup menyatakan bahwa kelas harus terbuka untuk ekstensi dan tertutup untuk dimodifikasi
# Penjelasan: Kita bisa menambahkan fungsionalitas baru tanpa mengubah kode yang sudah ada
# contoh
class Shape:
    def area(self):
        raise NotImplementedError("Metode ini harus diimplementasikan")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Fungsi untuk menghitung area
def total_area(shapes):
    return sum(shape.area() for shape in shapes)

# Penggunaan
shapes = [Rectangle(10, 5), Circle(7)]
print("Total area:", total_area(shapes))  # Output: Total area: 86.0

# Penjelasan: Kita dapat menambah bentuk baru (misalnya, Triangle) tanpa mengubah kelas yang ada, hanya dengan mengimplementasikan metode area().
