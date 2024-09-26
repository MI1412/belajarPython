class Complex:
    def __init__(self,realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    
    def f(self,format:str) -> str:
        return f"{format}r: {self.r}\ni: {self.i}"