#Superclass
class Pizza:

    def __init__(self,description='',price=0):
        self.description=description
        self.price=price
    

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.price if self.price is not None else 0
