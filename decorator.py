# Superclass
class Decorator():

    def __init__(self):
        self.description='Sauce'
        self.price=0

    def get_cost(self):
       if self.price is not None:
          return self.get_cost
       else:
          return 0


    def get_description(self):
       return self.description
