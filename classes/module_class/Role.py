class Role:
    def __init__(self,nama,role,attk):
        self.role = role
        self.nama = nama
        self.attk = attk
        
    def status(self):
        print(f"status: {self.nama,self.role,self.attk}")

class Mage(Role):
    # override
    def __init__(self,nama):
        super().__init__(nama,"Mage",90999999)
        
class Tank(Role):
    # override
    def __init__(self,nama):
        # super mengoverride super class
        super().__init__(nama,"Tank",0)

class Assasin(Role):
    # override
    def __init__(self,nama):
        super().__init__(nama,"Assasin",10909090)
    