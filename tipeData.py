# tipe data dalam python

# 1. angka 
# integer 
print('\ntipe data angka')
tipeInteger = 9 
print ("tipe data integer : ", tipeInteger, "tipe data : ", type(tipeInteger))
#float
tipeFloat = 1.8
print ("tipe data float : ", tipeFloat, "tipe data : " , type(tipeFloat))
# tipe data khusus complex
dataKomplex = complex(5,6)
print("tipe data complex : ", dataKomplex, "tipe data : ", type(dataKomplex))
# tipe data dari bahasa C
from ctypes import c_double
dataCDouble = c_double(10.5)
print("data : ", dataCDouble, "tipe data : ", type(dataCDouble))

# 2. teks
# string 
tipeString = "imron"
print('\ntipe data string')
print("data : ", tipeString, "tipe data : ", type(tipeString))

# 3. tipe data berurutan
# list
print('\ntipe data ber urutan')
tipe_list = [1,2,3,4,5,6]
print(f'tipe data list : {tipe_list} tipe data : {type(tipe_list)}')
# tuple
tipe_tuple = (1,2,3,4,5,6,7)
print(f'tipe data tuple : {tipe_tuple} tipe data : {type(tipe_tuple)}')
# range
tipe_range = range(8)
print(f'tipe data range : {tipe_range} tipe data : {type(tipe_range)}')



# 4. tipe data boolean
tipeBoolean = True
print('\ntipe data boolean')
print("tipe data boolean : ", tipeBoolean, "tipe data : ", type(tipeBoolean))

# 5. tipe data mapping
# dict
tipe_mapping = {'apple':'buah','singa':'hewan','pulpen':'benda'}
print('\ntipe data mapping')
print("tipe data mapping : ", tipe_mapping, "tipe data : ", type(tipe_mapping))

# 6. tipe set
# set
tipe_set = set({'amir','rafi','rido'})
# frozenset
tipe_frozenSet = frozenset({1,2,4,5,6,7})
print('\ntipe data set')
print(f'tipe data set : {tipe_set} tipe data : {type(tipe_set)}')
print(f'tipe data frozenset : {tipe_frozenSet} tipe data : {type(tipe_frozenSet)}')

# 7. tipe binary
# bytes
print('\ntipe data binary')
tipe_bytes = bytes(1)
print(f'tipe data bytes : {tipe_bytes} tipe data : {type(tipe_bytes)}')
# bytearray
tipe_byteArray = bytearray(5)
print(f'tipe data tipe byteArray : {tipe_byteArray} tipe data : {type(tipe_byteArray)}')
# memoryView
tipe_memoryview = memoryview(bytes(5))
print(f'tipe data memoryView : {tipe_memoryview[1]} tipe data : {type(tipe_memoryview)}')

# 8. tipe data none / tidak ada
# nonetype
tipe_none = None
print(f'tipe data none : {tipe_none} tipe data : {type(tipe_none)}')
