from decorator import Decorator


class Meat(Decorator):
    
    def __init__(self, isim, fiyat):
        super().__init__(isim, fiyat)