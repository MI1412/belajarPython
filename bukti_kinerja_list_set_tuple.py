import random
import timeit

# Buat dataset acak dengan 1 juta elemen
data = random.sample(range(10000000), 1000000)

# Set, List, dan Tuple yang akan digunakan untuk pengujian
my_list = list(data)
my_tuple = tuple(data)
my_set = set(data)

# Menguji kinerja pencarian
list_time = timeit.timeit("1000 in my_list", globals=globals(), number=100000)
tuple_time = timeit.timeit("1000 in my_tuple", globals=globals(), number=100000)
set_time = timeit.timeit("1000 in my_set", globals=globals(), number=100000)

print(f"Pencarian dalam List: {list_time} detik")
print(f"Pencarian dalam Tuple: {tuple_time} detik")
print(f"Pencarian dalam Set: {set_time} detik")


# Menguji kinerja penambahan elemen pada list dan set
list_append_time = timeit.timeit("my_list.append(10000000)", globals=globals(), number=100000)
set_add_time = timeit.timeit("my_set.add(10000000)", globals=globals(), number=100000)

print(f"Penambahan elemen dalam List: {list_append_time} detik")
print(f"Penambahan elemen dalam Set: {set_add_time} detik")

# Menguji kinerja iterasi melalui semua elemen
list_iter_time = timeit.timeit("for _ in my_list: pass", globals=globals(), number=100)
tuple_iter_time = timeit.timeit("for _ in my_tuple: pass", globals=globals(), number=100)
set_iter_time = timeit.timeit("for _ in my_set: pass", globals=globals(), number=100)

print(f"Iterasi dalam List: {list_iter_time} detik")
print(f"Iterasi dalam Tuple: {tuple_iter_time} detik")
print(f"Iterasi dalam Set: {set_iter_time} detik")

