from pizza_class import Pizza


class MargheritaPizza(Pizza):
    
    def __init__(self):
        super().__init__(description='Margarita Pizza',price= 250)