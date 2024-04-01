# type hints untuk function
import string
# standart funct
# studi kasus
# def fungsi(param):
#     hasil = param**2
#     print(hasil)
# fungsi('imron')    
# fungsi(False)    

# penggunaan type hints

def funct_hints(param:int) -> int: # membuat : sebuah tipe data dan hints ->
    # fungsi dengan hints
    hasil = 10**param
    return hasil
hasil = funct_hints(2)
print(hasil)

def display(arg:string) -> string:
    print(arg)
    
display('imron')
import os
hasil = os.system('clear')
print(hasil)