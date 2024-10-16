import bisect
# NAME
#     bisect - Bisection algorithms.
# digunakan untuk mengurutkan list secara rekursif

# bisect bisa digunakan untuk handling urutan list, dict, tuple, set

poin_list = [["amir",100],["amar",100]]
poin_set = {("amir",1000),("amar",9090)}
poin_dict = {"amir":100,"amar":1909}
bisect.insort(poin_list,["tes",90909])
# bisect.insort(poin_dict,{"tes":90909}) dict bukan tipe urutan
# bisect.insort(poin_set,("tes",90909)) set ga support indexing
print(type(poin_list))
print(poin_list)
print(poin_set)
print(type(poin_set))