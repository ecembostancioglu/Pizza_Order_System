from pizza_class import Pizza


class BasePizza(Pizza):
    
    def __init__(self):
        super().__init__(description='Base Pizza',price= 300)