class Ogrenci:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
    
    # Property metodu: ad ve soyadı birleştirir
    @property
    def tam_ad(self):
        return f"{self.ad} {self.soyad}"

# Bir öğrenci nesnesi oluşturalım
ogrenci = Ogrenci("Ali", "Yılmaz")

# Ad ve soyadın birleşimi olan tam adı ekrana yazdıralım
print("Öğrencinin Tam Adı:", ogrenci.tam_ad)
