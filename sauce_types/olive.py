from decorator import Decorator


class Olive(Decorator):
    
     def __init__(self,component):
        super().__init__(component)
        self.description='Zeytin'
        self.price=6