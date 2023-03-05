from pizza_class import Pizza


class Decorator:


    def __init__(self,isim,fiyat):
        self.isim=isim
        self.fiyat=fiyat
    

    def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self)


    def get_description(self):
       return self.component.get_description() + \
         ' ' + Pizza.get_description(self)
