from pizza_class import Pizza


class Decorator(Pizza):

    def __init__(self,component,description,price):
        self.component=component
        self.description=description
        self.price=price
        Pizza.__init__(self,description,price)
    

    def get_cost(self):
       if self.price is not None:
          return self.component.get_cost() + (self.price) #str(Pizza.get_cost(self))
       else:
          return 0


    def get_description(self):
       return str(Pizza.get_description(self))
