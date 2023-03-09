from decorator import Decorator


class Onion(Decorator):
    
     def __init__(self,component):
      super().__init__(component,description='Soğan',price=35)
      

