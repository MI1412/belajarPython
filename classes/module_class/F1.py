def f1(self):
    return f"f1 :{self.function_f1}" # membuat nilai dengan sama seperti nilai properti
class F1:
    function_f1 = f1
    
    def p(self):
        return "halo F1"
    def hai(self):
        return f"hai: {self.p()}"