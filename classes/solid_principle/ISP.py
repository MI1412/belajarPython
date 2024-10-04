# Interface Segregation Principle (ISP), artinya Sebaiknya kita memecah antarmuka besar menjadi antarmuka yang lebih kecil dan spesifik agar klien hanya menggunakan metode yang relevan.


class Flyable:
    def fly(self):
        pass

class Swimmable:
    def swim(self):
        pass

class Duck(Flyable, Swimmable):
    def fly(self):
        print("Duck flying")
    
    def swim(self):
        print("Duck swimming")
