
# menggunakan class

class Symbol:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Symbol({self.name})'

# Contoh penggunaan
sym1 = Symbol('mySymbol')
sym2 = Symbol('mySymbol')
print(sym1)  # Output: Symbol(mySymbol)
print(f"compare sym class: {sym1 is sym2}")  # Output: False, karena objeknya berbeda

# menggunakan tuple
symbol1 = ("symbol", "mySymbol")
symbol2 = ("symbol", "mySymbol")
print(symbol1)
print(symbol2)
print(f"compare sym tuple: {symbol1 == symbol2}")


# menggunakan uuid
import uuid as uid

def create_symbol():
	return uid.uuid4()

sym1 = create_symbol()
sym2 = create_symbol()
print(sym1)
print(sym2)
print(f"compare sym uuid: {sym1 == sym1}")
