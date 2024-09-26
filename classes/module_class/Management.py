# class Management:
#     def __init__(self,waktu,tenaga):
#         self.waktu = waktu
#         self.tenaga = tenaga

# class Method(Management):
#     def __init__(self):
#         super().__init__(waktu=0,tenaga=0)
        
#     def tidur(self,lama:int):
#         self.tenaga += lama
#         return self.tenaga 
    

# class Human(Management,Method):
#     def __init__(self,nama):
#         self.nama = nama
#         super().__init__(waktu=10000,tenaga=0)

# kesalahan ada pada class bentrok

class Management:
    def __init__(self, waktu, tenaga):
        self.waktu = waktu
        self.tenaga = tenaga

class Method:
    def __init__(self):
        self.tenaga = 0  # Inisialisasi tenaga di sini
    
    def tidur(self, lama: int):
        self.tenaga += lama
        
        return self.tenaga

class Human(Management, Method):
    def __init__(self, nama):
        # Inisialisasi kelas Management dan mengoverride
        Management.__init__(self, waktu=10000, tenaga=0)
        # Inisialisasi kelas Method dan mengoverride
        Method.__init__(self)  # Memanggil konstruktor dari Method
        self.nama = nama