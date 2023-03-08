from decorator import Decorator


class Meat(Decorator):
    
    def __init__(self):
        super().__init__()
        self.description='Et'
        self.price=15