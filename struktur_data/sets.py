# set adalah kumpulan data yang terurut {} dan tidak ada elemen duplikat
keranjang = {'buah','atk','dll'}
sets = {9,8,7,6,5,4,3,2,1}
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(keranjang)
print(basket)
print(f"set: {sets}")

isIn1 = 1 in sets
isIn20 = 20 in sets
print(f"is 1 in sets: {isIn1}")
print(f"is 20 in sets {isIn20}")

z = [1,2,3,4,5,12,3,4,5,6,2,1]
a = set(z)
b = set('alacazam')
c = set('abracadabra')
min_ = c -b
or_ = b | c
and_ = b & c
orTop_ = b ^ c
print(f"or_ {or_}") # huruf dalam a atau b atau keduanya
print(f"min_ {min_}") # huruf dalam b tapi tidak dalam c
print(f"and_ {and_}") # huruf b dan c
print(f"or ^: {orTop_}") # huruf dalam b atau c tetapi tidak keduanya
print(f"b: {b}")
print(f"a: {a}")

# set juga suport dengan list komprehension

set_komprehension = {data for data in [1,2,3,4,5,6,7,8,9] if data not in [1,2,3,4,5]}
print(f"set komprehension {set_komprehension}")