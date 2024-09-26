# <--lambda
# lambda adalah cara untuk mendefinisikan fungsi tanpa nama / anonymous funct
# contoh : lambda_expr ::=  "lambda" [parameter_list] ":" expression
# lihat juga definisi function / functiondefinition.py

def increment(b):
    """digunakan untuk pertambahan"""
    return lambda a:a +b
p = increment(1) # p adalah anonymous funct

print(p(6))

packs =  [(1,'satu'),(2,'dua'),(3,'tiga'),(4,'empat')]
packs.sort(key=lambda pack:pack[1] )
print(f"packs: {packs}")
