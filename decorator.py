from pizza_class import Pizza


class Decorator:

    def __init__(self,component):
        super().__init__()
        self.component=component
    

    def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self)


    def get_description(self):
       return self.component.get_description() + \
         ' ' + Pizza.get_description(self)
