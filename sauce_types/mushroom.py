from decorator import Decorator


class Mushroom(Decorator):
    
    def __init__(self, name, price):
        super().__init__(name, price)