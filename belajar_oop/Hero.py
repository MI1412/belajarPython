class Hero:
    def __init__(self,name,tipe):
        # private
        self.__name = name
        self.__exp = 0
        self.__level = 0
        
        self.tipe = tipe
        # membuat darah berdasarkan level
        self.health_pool = [0,100,200,300,400,500]
        # membuat attk berdasarkan level
        self.attk_pool = [0,10,20,30,40,50]
        self.magic_pool = [0,10,20,30,40,50]
        self.armor_pool = [0,10,20,30,40,50]
        
    def info(self):
        print(f'\n{self.__name} \ntipe : {self.tipe} \nlevel: {self.__level} \ndarah : {self.__health} \nattack power : {self.__attckpower} \nmagic power : {self.__magicpower} \narmor : {self.__armor}')
    
    @property
    def health_pool(self):
        pass
    
    @property
    def attk_pool(self):
        pass
    
    @property
    def magic_pool(self):
        pass
    
    @property
    def armor_pool(self):
        pass
    
    @property
    def levelUp(self):
        pass
    
    @property
    def gainExp(self):
        pass
    
    @health_pool.setter
    def health_pool(self,input):
        self.__health_pool = input
        
    @attk_pool.setter
    def attk_pool(self,input):
        self.__attk_pool = input
        
    @armor_pool.setter
    def armor_pool(self,input):
        self.__armor_pool = input
        
    @magic_pool.setter
    def magic_pool(self,input):
        self.__magic_pool = input
    
    @gainExp.setter
    def gainExp(self,input):
        self.__exp = input
        if self.__exp >= 100:
            print(f'\n{self.__name} level up')
            self.levelUp = self.__exp//100
            self.__exp %= 100
    @levelUp.setter
    def levelUp(self,input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attckpower = self.__attk_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]
        self.__magicpower = self.__magic_pool[self.__level]

class Hero_mage(Hero):
    def __init__(self,name):
        super().__init__(name,tipe='Mage')
        self.health_pool = [0,50,150,250,350,450,550]
        self.magic_pool = [50,100,200,300,450,600]
        self.attk_pool = [10,15,20,25,30,35]
        self.armor_pool = [20,30,40,50,60,70]
        self.levelUp = 1
        
class Hero_assasin(Hero):
    def __init__(self,name):
        super().__init__(name,tipe='Assasin')
        self.health_pool = [0,60,70,80,150,300,400,500]
        self.magic_pool = [0,0,0,0,0]
        self.attk_pool = [25,50,100,100.5,100.6,100.7]
        self.armor_pool = [1.5,1.9,2.5,2.9,3.5,3.9]
        self.levelUp = 1