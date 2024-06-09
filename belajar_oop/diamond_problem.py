# diamond problem di class inheritance
# kenapa dipanggil diamond problem ? 
# karena bentuk problemnya seperti diamond


class A:
    pass
    # def info(self):
    #     print('ini adalah class A')

class B(A):
    pass
    # def info(self):
    #     print('ini adalah class B')

class C(A):
    # pas
    def info(self):
        print('ini adalah class C')


class D(B,C):
    pass


# class D akan mengambil class method dari B,C, jika class B tidak ada methodnya maka Class D akan mengambil method dari class C, jika tidak ada maka akan mengambil method induknya
# ini disebut solusi diamond dalam class

objek = D()
objek.info()

# help(objek)
