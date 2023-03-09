from decorator import Decorator


class Olive(Decorator):
    
     def __init__(self,component):
        super().__init__(component,description='Zeytin',price=6)
        