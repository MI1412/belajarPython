class init:
    def __init__(self,*args):
        self.data = []
        self.data.append(args)
        
        
    def tambah_data(self,*args):
        return f"data: {self.data.append(args)}"
    
    def get_data(self):
        return self.data
