# # class abstrak adalah contoh dari class, class abstrak tidak bisa diimplementasikan menjadi objek
# # contoh

# # tambahkan module abs dari pyhon 
# # abc = abstrak base class
# from abc import ABC,abstractmethod


# class Button(ABC): # ini akan menjadi class abstrak
    
#     # decorator abstrak class
#     # membuat wadah dengan properti abstrak method
#     @abstractmethod
#     def click(self):
#         # print('button diclick')
#         pass
        
# class PushButton(Button):
    
#     # jadi kita overload classnya
#     # mengisi wadah method class abstrak tersebut
#     def click(self):
#         print('push button berjalan')


# tombol1 = PushButton()
# # tombol2 = Button() # jadi class abstrak class tidak bisa membuat objek dari class abstrak

# # jika mencoba tombol 1 yang merupakan turunan class button ini tidak bisa diimplementasikan 
# tombol1.click()
# help(tombol1)
# # tombol2.click()
# # abstrak class tidak seperti ini walaupun strukturnya sama
# # kegunaan abstrak class adalah sama persis ketika membuat nasi goreng, abstrak classnya adalah buku masak


# # latihan abstrak class
# # mencoba menghubungkan staticmethod, classmethod,properti, getter, setter dengan abstrak class
# # contoh blue print sebuah class
from abc import ABC,abstractmethod

# create abstrak class
class Button(ABC):
    # diabstrak class ini bisa dicampur ada yang abstrak method dan ada ga abstrak method
    # contohnya adalah :
    def __init__(self,link): # bukan abstrak method
        self.link = link
    
    # properti dari ABC abstrak method
    @abstractmethod
    def click(self):
        pass
    
    # karena di module abc yang sekarang belum ada caranya atribut bukan abstrak method dari super class untuk bisa masuk di sub class. makanya kita pakai decorator properti getter dan setter
    @property # yang asalnya dari atribute menjadi method digunakan untuk menyambungkan link atribute dengan link method
    @abstractmethod # perlu dilihat juga urutannya dari property kemudian abstrak method, method
    def link(self):
        pass
    
    
class PushButton(Button):
    # problem nya adalah ketika click dibawah ini tidak tahu abstrak classnya seperti apa maka akan tidak jelass / implisit
    def click(self):
        print(f'go to : {self.link}')
        
        
    @Button.link.setter
    def link(self,input):
        self.__link = input    
        
    @link.getter
    def link(self):
        return self.__link   

tombol1 = PushButton('E:\\belajarPython\\belajar_oop\\')
tombol1.click()









