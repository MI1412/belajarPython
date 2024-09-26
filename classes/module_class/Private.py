class Private:
    def __init__(self):
        self.__private_var = "ini var private" # akan dimangling / diacak
    def __method_private(self):
        print("ini private method")