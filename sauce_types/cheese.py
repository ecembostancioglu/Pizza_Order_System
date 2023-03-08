from decorator import Decorator


class Cheese(Decorator):
    
    def __init__(self):
        super().__init__()
        self.description='Peynir'
        self.price=5