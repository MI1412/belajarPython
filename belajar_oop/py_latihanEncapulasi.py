# contoh membuat program game yang ada sebuah hero dengan attck, health, armor seiring penaikan exp maka hero tersebut makin bertambah kuat

class Hero:
    # private class variabel
    __jumlah = 0 
    def __init__(self,name,attack,health,armor):
        self.__name = name
        self.__attackBase = attack
        self.__healthBase = health
        self.__armorBase = armor
        self.__level = 1
        self.__exp = 0
        
        self.__healthMax = self.__healthBase * self.__level
        self.__attackPower = self.__attackBase * self.__level
        self.__armor = self.__armorBase * self.__level
        self.__health = self.__healthMax
        
        Hero.__jumlah += 1
        
        
    @property
    def info(self):
        return 'Nama Hero : {} \nLevel : {}\nDarah : {}/{} \nAttack : {} \nArmor : {}'.format(self.__name,self.__level,self.__health,self.__healthMax,self.__attackPower,self.__armor)
    
    # membuat method mengambil exp
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(f'\n{self.__name} UP LEVEL !!')
            self.__level += 1
            self.__exp -= 100
            
            self.__healthMax = self.__healthBase * self.__level
            self.__attackPower = self.__attackBase * self.__level
            self.__armor = self.__armorBase * self.__level
    def attack(self,musuh):
        self.gainExp = 120

zero = Hero('Zero',400,6000,500)
slender = Hero('Slender',500,4000,450)

print(zero.info) # ini tidak bisa dirubah karena bukan variabel
print(zero.__dict__)

zero.attack(slender)

print(zero.info) # yang bisa dilihat oleh client ada hanya info saja jika kita coba gainexp maka akan none
print(zero.gainExp)
print('\n',zero.__dict__)


