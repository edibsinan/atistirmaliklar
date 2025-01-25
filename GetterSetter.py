class Araba:
    def __init__(self):
        self.__hiz = 0  # Private nitelik

    # Getter metodu
    def get_hiz(self):
        return self.__hiz

    # Setter metodu
    def set_hiz(self, yeni_hiz):
        if yeni_hiz >= 0:  # Negatif hız engelleniyor
            self.__hiz = yeni_hiz
        else:
            print("Hız negatif olamaz!")

araba = Araba()

# Private niteliğe erişim ve değiştirme
print(araba.get_hiz())  # Şu anki hız: 0
araba.set_hiz(50)       # Hız 50'ye ayarlandı
print(araba.get_hiz())  # Şu anki hız: 50
