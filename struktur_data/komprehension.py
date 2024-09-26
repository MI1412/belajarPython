# komprehension adalah cara ringkas untuk membuat ringkas struktur data seperti list, set, dictionary atau generator
# intinya untuk meringkas struktur data

# <--list komprehension
# rumus: [expression for item in iterable if condition]
pangkat = [x**2 for x in range(1,6)]
print(pangkat)

# <--set komprehension
# rumus: {expression for item in iterable if condition}
pangkat_unik = {x**2 for x in range(1,6)}
print(pangkat_unik)

# <-- dict komprehension
# rumus: {key: value for item in iterable if condition}
pangkat_dict = {x:x**2 for x in range(1,6)}
print(pangkat_dict)

# <--pangkat generator
pangkat_gen = (x**2 for x in range(1,6))
# print(pangkat_gen)
for p in pangkat_gen:
    print(p)