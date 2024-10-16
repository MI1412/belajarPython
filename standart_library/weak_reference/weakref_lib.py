import weakref, gc
# NAME
#     weakref - Weak reference support for Python.

# NAME
#     gc - This module provides access to the garbage collector for reference cycles.

class A:
    def __init__(self,value):
        self.value = value
    def __repr__(self):
        return str(self.value)
# membuat referensi
a = A(10)

# # tidak dapat membuat reff
d = weakref.WeakValueDictionary()
d["primary"] = a
print(d["primary"])

del a
sampah = gc.collect()
print(sampah)
