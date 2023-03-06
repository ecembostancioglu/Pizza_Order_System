from decorator import Decorator


class Mantar(Decorator):
    
    def __init__(self, isim, fiyat):
        super().__init__(isim, fiyat)