class name_class:
    """ini docstring dari name_class"""
    
    # __init__ digunakan untuk membuat objek baru
    def __init__(self,nama,*data):
        # properti
        self.nama = nama
        self.data = data
        
    # function / behavior
    def tampilkan_data(self):
        print(f"data: {self.data} tipe: {type(self.data)}")
    def halo(self,nama):
        print(f"halo {self.nama} nama saya: {nama}")
# help(name_class)