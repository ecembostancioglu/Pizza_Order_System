from pizza_class import Pizza


class MargheritaPizza(Pizza):
    
    def __init__(self):
        super().__init__(description='Margherita Pizza',price= 250)