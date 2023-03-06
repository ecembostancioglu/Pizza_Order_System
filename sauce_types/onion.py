from decorator import Decorator


class Sogan(Decorator):
    
    def __init__(self, isim, fiyat):
        super().__init__(isim, fiyat)