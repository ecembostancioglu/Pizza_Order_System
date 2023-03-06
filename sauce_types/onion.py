from decorator import Decorator


class Onion(Decorator):
    
    def __init__(self, name, price):
        super().__init__(name, price)