class Bio:
    def __init__(self,nama,status,ttl):
        self.nama = nama
        self.status = status
        self.ttl = ttl
    
    def printBio(self):
        print(f"\nnama: {self.nama}\nttl: {self.ttl}\nstatus: {self.status}")

class Karyawan (Bio):
    def __init__(self,nama,ttl,status):
        super().__init__(nama,ttl,"karyawan")

class Murid(Bio):
    def __init__(self,nama,ttl,status):
        super().__init__(nama,ttl,"murid")

