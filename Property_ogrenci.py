"""Bir Ogrenci sınıfı oluşturun. Bu sınıfda bir ad ve soyad 
özellikleri bulunsun. Ayrıca, bu sınıfta bir de 
ad ve soyad özelliklerini birleştirecek bir property 
metodu tanımlansın. Bu metod getter olarak tanımlanmalı ve 
çağrıldığında öğrencinin adı ve soyadı beraber ekranda döndürülsün."""
class Ogrenci:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
    
    # Property metodu tanımlanıyor
    @property
    def tam_ad(self):
        return f"{self.ad} {self.soyad}"

# Örnek kullanım
ogrenci = Ogrenci("Ali", "Can")
print(ogrenci.tam_ad)  # Öğrencinin adı ve soyadı birlikte döndürülür
