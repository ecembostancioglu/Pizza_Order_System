from pizza_class import Pizza


class TurkPizza(Pizza):
    
    def __init__(self, isim, aciklama, fiyat):
        super().__init__(isim, aciklama, fiyat)