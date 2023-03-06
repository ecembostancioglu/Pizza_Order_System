class Pizza:

    def __init__(self,name,description,price):
        self.name=name
        self.description=description
        self.price=price
    

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.price
