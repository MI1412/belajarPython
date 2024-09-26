# # <--lingkup dan namespace
# # def scopes():
# #     def var_local():
# #         spam = "ini dilokal"
# #     def var_nonLocal():
# #         nonlocal spam
# #         spam = "ini nonlocal"
# #     def var_global():
# #         global spam
# #         spam = "ini global"
# #     spam = "test spam"
# #     var_local()
# #     print(f"var lokal {spam}")
# #     var_nonLocal()
# #     print(f"var nonlocal {spam}")
# #     var_global()
# #     print(f"var global {spam}")

# # scopes()
# # print(f"di dalam var global: {spam}")

# # <--definition class
# from module_class.name_class import name_class as nc
# rido = nc("rido","p","ppp","p")
# rido.halo("asep")
# data = rido.data
# rido.tampilkan_data()
# for k in data:
#     print(f"data rido: \n\tvalue: {k}")

# from module_class.init_class import init as init
     
# p = init("hehehaha",True,False, 10)
# # sama seperti ini
# # data = p.tambah_data(True, False, "str")
# ambil = p.get_data()
# print(f"data diambil dari init: {ambil}\n\ttipe: {type(ambil)}")

# from module_class.complex import Complex as cmplx
# x = cmplx(1.5,19.8)
# print(f"\nr: {x.r}\n\ti: {x.i}")

# # <--instance objek
# # membuat properti objek baru
# x.counter = 12
# while x.counter > 10:
#     x.counter = x.counter * 2
#     break
# print(x.counter)
# # method class
# xf = x.f("\n")
# print(xf)

# from module_class.Human import Human as hm
# abyan = hm("abyan")

# print(f"akses properti tanpa objek: {hm.properti}")
# print(f"nama: {abyan.name}\nakses properti dari {abyan.name}: {abyan.properti}")


# # <--perbedaan instance/objek dengan class
# # ketika menampilkan objek dengan dict, dir, module
# print(f"isi class dict: {abyan.__dict__}\ttipe: {type(abyan.__dict__)}")
# print(f"isi class dir: {abyan.__dir__} tipe: {type(abyan.__dir__)}")

# # menampilkan tanpa objek dengan dict, akan mengembalikan mappingproxy objek
# print(f"\nisi class dict: {hm.__dict__}")
# print(f"dari module {type(hm)} : {hm.__module__}")

# # <--perubahan yang terjadi pada properti
# from module_class.Warehouse import Warehouse as wh
# alamat = wh
# abyan = alamat("abyan","SDA")
# imron = alamat("imron","SBY")
# print(f"alamat abyan: {dict(abyan.__dict__)}")
# print(f"alamat imron: {dict(imron.__dict__)}")

# abyan = alamat("asep","ASIA")
# print(f"perubahan alamat abyan: {dict(abyan.__dict__)}\n")


# # <---membuat function diluar class
# from module_class.F1 import F1
# # contoh referensi class
# tes_f1 = F1
# print(tes_f1().p())
# print(tes_f1().hai())

# # contoh objek
# p_f1 = F1()
# print(p_f1.p)
# print(p_f1.hai())
# print(p_f1.function_f1())

# from module_class.Bag import Bag as bag
# tasku = bag()
# tasku.add('mie','bakso',True,False,"dan seterusnya")
# item = [item for item in tasku.data]
# print(f"\nisi tas gua (╯°□°）╯︵ ┻━┻): {item}")


# # <--inherit
# from module_class.Role import (Role as r,Mage as mg,Assasin as ass, Tank as tank)
# saber = ass("saber")
# steneb = mg("Steneb")
# ras = tank("ras")
# print(f"saber: {saber.__dict__}")
# saber.status()
# steneb.status()
# ras.status()
# print(f"steneb: {steneb.__dict__}")

# # <--multiple inherit
# from module_class.Management import (Human as hm,Management as mg,Method as mthd)

# human = hm
# imron = human("imron")
# print(f"imron: {imron.__dict__}")
# imron.tidur(10000)
# print(f"imron: {imron.__dict__}")

# # <--self parameter
# from module_class.self_parameter import Self as s
# objek = s
# imron = objek("imron")
# print(f"imron: {imron.hai()}")

# # menghapus objek properti
# del imron.nama

# from module_class.Bio import (Murid as murid, Karyawan as karyawan)
# imron = murid("imron","SDA",12)
# imron.printBio()
# musa = karyawan("musa",10,12)
# musa.printBio()

# # <--private variabel dan private method
# from module_class.Private import Private as private
# var_private = private()
# method_private = private()
# print(f"var privat: {var_private._Private__private_var}")
# method_private._Private__method_private()

# # <--data classes
# from module_class.Product import Product as product
# laptop = product("laptop",19000.00,19)
# print(f"\nproduct: {laptop.name}")
# print(f"harga: {laptop.price}")
# print(f"kuantitas: {laptop.quantity}")

# # <--iterators
# from module_class.Reversed import Reverse as reverse
# data = [10,9,8,7,6,5,4,3,2,1]
# terkecil = reverse(data)
# print(f"data di reverse{[data for data in terkecil]}")

# # <--generator
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for data in reverse("iah"):
    print(data,end=",")
