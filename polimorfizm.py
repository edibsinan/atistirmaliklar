# Üst sınıf
class Sekil:
    def alan(self):
        # Bu metot alt sınıflar tarafından geçersiz kılınacaktır
        raise NotImplementedError("Bu metot alt sınıflar tarafından tanımlanmalıdır.")

# Alt sınıf: Kare
class Kare(Sekil):
    def __init__(self, kenar):
        self.kenar = kenar
    
    def alan(self):
        return self.kenar * self.kenar

# Alt sınıf: Daire
class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap
    
    def alan(self):
        return 3.14 * self.yaricap * self.yaricap

# Polimorfik alan_hesapla fonksiyonu
def alan_hesapla(sekil):
    print(f"{sekil.__class__.__name__} alanı: {sekil.alan()}")

# Örnek kullanım
kare = Kare(5)  # Kenar uzunluğu 5 olan bir kare
daire = Daire(3)  # Yarıçapı 3 olan bir daire

alan_hesapla(kare)   # Kare alanını hesaplar
alan_hesapla(daire)  # Daire alanını hesaplar
