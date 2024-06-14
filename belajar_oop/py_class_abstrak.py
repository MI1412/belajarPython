# class abstrak adalah contoh dari class, class abstrak tidak bisa diimplementasikan menjadi objek
# contoh

# tambahkan module abs dari pyhon 
# abc = abstrak base class
from abc import ABC,abstractmethod


class Button(ABC): # ini akan menjadi class abstrak
    
    # decorator abstrak class
    # membuat wadah dengan properti abstrak method
    @abstractmethod
    def click(self):
        # print('button diclick')
        pass
        
class PushButton(Button):
    
    # jadi kita overload classnya
    # mengisi wadah method class abstrak tersebut
    def click(self):
        print('push button berjalan')


tombol1 = PushButton()
# tombol2 = Button() # jadi class abstrak class tidak bisa membuat objek dari class abstrak

# jika mencoba tombol 1 yang merupakan turunan class button ini tidak bisa diimplementasikan 
tombol1.click()
help(tombol1)
# tombol2.click()
# abstrak class tidak seperti ini walaupun strukturnya sama
# kegunaan abstrak class adalah sama persis ketika membuat nasi goreng, abstrak classnya adalah buku masak


# class biasa adalah contoh dari objek

