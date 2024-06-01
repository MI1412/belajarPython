# # method override digunakan untuk menyampingkan method pada super class 
# class Hero:
    
#     def __init__(self,nama,darah):
#         self.nama = nama
#         self.darah = darah
        
#     def info(self,tipe):
#         print(f'\n{self.nama} : {tipe} \ndarah : {self.darah}')

# class Hero_mage(Hero):
#     def __init__(self,nama):
#         super().__init__(nama,5000)
        
#     def info(self):
#         super().info('Mage')


# class Hero_assasin(Hero):
#     def __init__(self,nama):
#         super().__init__(nama,4500)

#     def info(self):
#         super().info('Assasin')
        
        
# mind = Hero_mage('Mind')
# rar = Hero_assasin('Rar')

# mind.info()
# rar.info()

# ini tidak bisa cepat kalau mendevelop aplikasi

# maka disini kita pakai override

# method override digunakan untuk menyampingkan method pada super class 
class Hero:
    
    def __init__(self,nama,darah):
        self.nama = nama
        self.darah = darah
        
    def info(self):
        print('info di hero')
        print(f'\n{self.nama} \ndarah : {self.darah}')

class Hero_mage(Hero):
    
    # bagian objek ini tidak akan menimpa di objek super class tetapi menyampingkan hal yang sama terus ditimpa dengan hal baru
    def __init__(self,nama):
        super().__init__(nama,5000)
        
        # info akan menimpa dibagian kelas utama atau super class
        
        # override
    def info(self):
        print('info di sub mage')
        print(f'{self.nama} \ndarah : {self.darah} \ntipe : mage')


class Hero_assasin(Hero):
    def __init__(self,nama):
        super().__init__(nama,4500)

    # def info(self):
    #     print('\ninfo di sub assasin')
    #     print(f'{self.nama} \ndarah : {self.darah} \ntipe : assasin')
        
        
mind = Hero_mage('Mind')
rar = Hero_assasin('Rar')

rar.info()
