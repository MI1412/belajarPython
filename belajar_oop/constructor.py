class hero:
    # magic keyword constructor
    def __init__(self,name,stat,umur): # argumen self memanggil diri sendiri / memanggil hero 
	self.name = name # variabel penampung nama
	self.stat = stat
	self.umur = umur




hero1 = hero('hehehahha','pelajar'.10)

# memanggil semua argumen
print(hero1)
# contoh memanggil hero name
print(hero1.name) # memanggil nama dari hero
# contoh mamanggil stat dan umur
print(hero1.umur)
print(hero1.stat) 
