from decimal  import *
# NAME
#     decimal - C decimal arithmetic module
# round(Decimal('0.80') * Decimal('.8'), 2)
# Decimal('0.76') 
# print(round(.80,1.8))
desimal = Decimal(.90)
print(desimal)
print(type(desimal))
total = sum([desimal]* 8)
cek = desimal == .90
print(cek)
print(total)
print(type(total))