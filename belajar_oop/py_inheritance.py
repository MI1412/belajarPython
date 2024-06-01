# inheritence / penurunan / pewarisan artinya suatu class yang diturunkan ke class lain 
# contoh class_1 ingin diturunkan ke class_2
# yang class_1 disebut super class / induk class, class_2 disebut sub class
# contoh nyata : saya punya class HERO tapi saya ingin buat sub class lagi yang bertipe assasin,tank,marskman,fighter
# kenapa konsep inheritance begitu ? 
# karena ingin menghindari perulangan / looping

class Hero:
    
    def __init__(self,name,darah):
        self.name = name
        self.darah = darah
        
    # untuk memberi pewarisan sub class cukup berikan pada nama class ()    
class Hero_Mage(Hero):
    pass
        
class Hero_Assasin(Hero):
    pass        

# print(Hero.__dict__)
mira = Hero('Mira',6070)
aurora = Hero_Mage('Aurora',5900)
saber = Hero_Assasin('Saber',5000)

print(mira.name)
print(aurora.name)
print(saber.name)

# untuk mengetahui aurora termasuk class hero apa
# print(help(aurora))

