import doctest
# NAME
#     doctest - Module doctest -- a framework for running examples in docstrings.
def genap(n):
    """"
    tes apakah genap ?
    >>> genap(4)
    >>> genap(2)
    >>> genap(1)
    """
    
    return n % 2 == 0
    

tes = doctest.testmod()
print(tes)