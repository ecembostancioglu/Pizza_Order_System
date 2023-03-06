from decorator import Decorator


class Et(Decorator):
    
    def __init__(self, isim, fiyat):
        super().__init__(isim, fiyat)