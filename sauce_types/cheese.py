from decorator import Decorator


class Cheese(Decorator):
    
    def __init__(self, name, price):
        super().__init__(name, price)