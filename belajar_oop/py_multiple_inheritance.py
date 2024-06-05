# # multiple inheritance adalah pengambilan method dari beberapa SuperClass atau induk class ke subClass

# # contoh penjelasan 
# class A:
#     def method_A(self):
#         print('ini adalah method A')

# class B:
#     def method_B(self):
#         print('ini adalah method B')
                

# # contoh penggunaan multiple inheritance di sub class ada superClass A dan superClass B                 
# class Someone(A,B):
#     pass

# objek = Someone()

# objek.method_A()
# objek.method_B()

# contoh :
class Job:
    def setJob(self,job):
        self.job = job
        
    def showJob(self):
        print(f'{self.job}')    
        

class Tipe:
    def setTipe(self,tipe):
        self.tipe = tipe
        
    def showTipe(self):
        print(f'{self.tipe}')    

class Hero(Job,Tipe):
    def __init__(self,name,darah):
        self.name = name
        self.darah = darah

xinn = Hero('Xinn',900)
xinn.setJob('thief')
xinn.setTipe('assasin')
xinn.showJob()
xinn.showTipe()

