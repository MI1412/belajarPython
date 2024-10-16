from timeit import Timer
# NAME
#     timeit - Tool for measuring execution time of small code snippets.

tes = Timer('t = a; a = b; b = t','a = 1; b = 2').timeit()
print(tes)

tes2 = Timer('a,b = b,a', "a = 1; b = 2").timeit()
print(tes2)
