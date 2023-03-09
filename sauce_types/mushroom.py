from decorator import Decorator


class Mushroom(Decorator):
    
     def __init__(self,component):
        super().__init__(component,description='Mantar',price=30)
        