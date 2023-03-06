from pizza_class import Pizza


class MargheritaPizza(Pizza):
    
    def __init__(self, name, description, price):
        super().__init__(name, description, price)