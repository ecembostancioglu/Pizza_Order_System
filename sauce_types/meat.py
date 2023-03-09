from decorator import Decorator

class Meat(Decorator):

    def __init__(self, component):
        super().__init__(component,description='Et',price=50)