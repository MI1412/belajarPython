#casting merubah tipe data ke tipe lain
#contoh
# int > float
tipe_int = 0
print("data : ",tipe_int,"tipe data : ",type(tipe_int))
tipe_float = float(tipe_int)
print("data : ",tipe_float,"tipe data : ",type(tipe_float))

# int > string
tipe_string = str(tipe_int)
print("data : ",tipe_string,"tipe data : ",type(tipe_string))

# int > boolean 
boolean = bool(tipe_int)
print("data : ",boolean,"tipe data : ",type(boolean))

#float > int
cast_float =10.9
cast_int = int(cast_float)
print("data : ",cast_int,"tipe data : ",type(cast_int))