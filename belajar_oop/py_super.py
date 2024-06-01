# super() adalah mengambil method dari super class

class Hero:
    def __init__(self,name,darah,armor,magic,attack,attk_spped):
        self.name = name
        self.darah = darah
        self.armor = armor
        self.magic = magic
        self.attack = attack
        self.attk_spped = attk_spped
        self.darah = darah
    def info(self):
        print(f'\n{self.name} \ndarah : {self.darah} \narmor : {self.armor} \nmagic : {self.magic} \nattack : {self.attack} \nattack speed : {self.attk_spped}')
        
class Hero_Tank(Hero):
    
    def __init__(self,name):
        
        # mengambil method dari induk
        # self dan name disini mengambil dari class hero tank bukan hero
        # Hero.__init__(self,name,10000,500,0,40,90)
        # atau bisa menggunakan method super()
        # ini artinya kita mengambil init dari induk / super class
        super().__init__(name,10000,500,0,40,90)
        super().info()

class Hero_Mage(Hero):
    
    def __init__(self,name):
        # Hero.__init__(self,name,8000,50,500,50,20)
        super().__init__(name,7500,50,500,80,50)
        super().info()
        
class Hero_Assasin(Hero):
    
    def __init__(self,name):
        # Hero.__init__(self,name,7500,50,0,500,70)
        super().__init__(name,6000,50,0,500,70)
        super().info()
class Hero_Marskman(Hero):
    
    def __init__(self,name):
        # Hero.__init__(self,name,6000,60,0,200,500)       
        super().__init__(name,6000,70,0,200,500)
        super().info()
        
tigreal = Hero_Tank('Tigreal')
haya = Hero_Assasin('Hayabusa')
joy = Hero_Mage('Joy')
broto = Hero_Marskman('Broto')

# masalahnya adalah di sub class mengulang variabel darah dan name padahal di konsep pewarisan bukan seperti itu


# untuk menampilkan haya termasuk ke class hero apa
# print(type(haya))
# print('\n')
# print(haya.__dict__)
# print(type(tigreal))
# print(tigreal.__dict__)
# print(type(joy))
# print(joy.__dict__)
# print(type(broto))
# print(broto.__dict__)
