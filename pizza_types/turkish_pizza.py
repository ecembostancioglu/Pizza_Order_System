from pizza_class import Pizza


class TurkishPizza(Pizza):
    
    def __init__(self):
        super().__init__(description='Turkish Pizza',price= 400)