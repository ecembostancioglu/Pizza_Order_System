from pizza_class import Pizza


class BasePizza(Pizza):
    
    def __init__(self):
        super().__init__(description='Sade Pizza',price= 300)