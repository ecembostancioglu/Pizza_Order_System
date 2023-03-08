from decorator import Decorator


class Onion(Decorator):
     def __init__(self):
        super().__init__()
        self.description='Soğan'
        self.price=7