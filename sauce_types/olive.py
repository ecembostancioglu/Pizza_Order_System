from decorator import Decorator


class Olive(Decorator):
    
    def __init__(self, name, price):
        super().__init__(name, price)