from decorator import Decorator

class Corn(Decorator):
    
   def __init__(self,component):
     super().__init__(component,description='Mısır',price=7)