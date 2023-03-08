from decorator import Decorator


class Mushroom(Decorator):
    
     def __init__(self):
        super().__init__()
        self.description='Mantar'
        self.price=4