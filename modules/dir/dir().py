import sys
import modules as md

#tanpa beberapa argument dir
dir_list = [1,2,3,4,5,6]
calc = md.calc
print(dir())


dir_md = dir(md) # menampilkan isi module md
dir_sys = dir(sys)
print(dir_md)
print(dir_sys)

# catatan itu menampilkan isi semua list, variabel, modules dll

# import builtIns
import builtins as bltn
print(f'builtins: {dir(bltn)}')
