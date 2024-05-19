# latihan membuat membuat game sederhana
class hero:
    
    def __init__(self,name,health,attk_p,def_poin):
        self.name = name
        self.health = health
        self.attk_p = attk_p
        self.def_poin = def_poin
        
    def attk(self,lawan):
        print('\n'+self.name,'menyerang',lawan.name) # lawan.name akan mengambil variabel dalam instance variabel selama objek ada nama.name maka bisa membuat nama argumen sendiri
        lawan.attked(self,self.attk_p)
    
    def attked(self,lawan, attack_p_lawan):
        print(self.name,'terserang', lawan.name) 
        attk_acc = attack_p_lawan / self.def_poin
        print('damage :', str(attk_acc))
        self.health -= attk_acc
        print('health : ', self.name, 'tersisa', int(self.health))
        

saber = hero('saber',1500,2000,450)

# dipyhthon semua tipe data adalah objek
# untuk memanggil objek kedua maka ditulislah sebuah class 
tigreal = hero('tigreal',3000,500,1000)
hayabusa = hero('hayabusa',2000,250,50)

saber.attk(tigreal)
tigreal.attk(saber)

