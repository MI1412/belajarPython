# method resolution order digunakan untuk melihat urutan eksekusi class // multiple inheritance 

# class A:
#     def info_A(self):
#         print('ini adalah class A')
    
# class B:
#     def info_B(self):
#         print('ini adalah class B')

# # class c mengambil method dari induknya
# class C(A,B):
#     pass

# objek = C()
# objek.info_A()
# objek.info_B()

# tetapi bagaimana kalau methodn induknya sama ?

class A:
    def info(self):
        print('ini adalah class A')
    
class B:
    def info(self):
        print('ini adalah class B')

# class c mengambil method dari induknya
class C(A,B):
    pass

objek = C()
objek.info()

# untuk melihat urutan eksekusi MRO gunakan help(contoh_objek)
help(objek)
