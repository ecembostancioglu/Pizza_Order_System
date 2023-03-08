from decorator import Decorator


class Corn(Decorator):
    
     def __init__(self):
        super().__init__()
        self.description='Mısır'
        self.price=7