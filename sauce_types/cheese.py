from decorator import Decorator


class Cheese(Decorator):
    
    def __init__(self,component):
        super().__init__(component,description='Peynir',price=20)