from pizza_class import Pizza


class ClassicPizza(Pizza):
    
    def __init__(self):
        super().__init__(description='Classic Pizza',price='200')
