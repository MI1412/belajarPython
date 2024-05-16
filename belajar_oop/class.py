class hero:
    # class variabel adalah variabel didalam class
    jumlah = 0
    
    # magic keyword constructor
    def __init__(self,name,stat,umur): # argumen self memanggil diri sendiri / memanggil hero 
        # contoh instance variabel :
        self.name = name # variabel penampung nama
        self.stat = stat
        self.umur = umur
        
        hero.jumlah += 1 # akses class variabel.dengan titik
        print('tes '+ name)




hero1 = hero('hehehahha','pelajar',10)

# memanggil semua argumen
print(hero1.__dict__)
print(hero.jumlah)
# contoh memanggil hero name
print(hero1.name) # memanggil nama dari hero
# contoh mamanggil stat dan umur
print(hero1.umur)
print(hero1.stat) 
