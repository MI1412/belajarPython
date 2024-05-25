# encapsulasi dibuat untuk variabel private 
# menggunakan getter dan setter
# getter untuk mengambil variabel dari private
# setter untuk mengsetting variabel dari private

# contoh
class Yo:

    def __init__(self,name,tipe):
        self.name = name
        self.tipe = tipe


satria = Yo('satria','murid')
print(satria.__dict__)