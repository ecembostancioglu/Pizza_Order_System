class Pizza:

    def __init__(self,isim,aciklama,fiyat):
        self.isim=isim
        self.aciklama=aciklama
        self.fiyat=fiyat
    

    def get_description(self):
        return self.aciklama
    
    def get_cost(self):
        return self.fiyat
