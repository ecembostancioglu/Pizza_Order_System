from decorator import Decorator


class Cheese(Decorator):
    
    def __init__(self):
        self.description='Cheese'
        self.price=20