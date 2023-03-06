from decorator import Decorator


class Corn(Decorator):
    
    def __init__(self, name, price):
        super().__init__(name, price)