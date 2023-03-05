from decorator import Decorator


class Onion(Decorator):
    
    def __init__(self, isim, fiyat):
        super().__init__(isim, fiyat)