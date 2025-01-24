class Araba:
    def __init__(self):
        self.__calisiyor_mu = False  # Motor durumu (private)
        self.__hiz = 0               # Hız (private)

    def motoru_baslat(self):
        if not self.__calisiyor_mu:  # Eğer motor kapalıysa çalıştır
            self.__calisiyor_mu = True
            print("Motor çalıştırıldı.")
        else:
            print("Motor zaten çalışıyor.")

    def motoru_durdur(self):
        if self.__calisiyor_mu:
            if self.__hiz == 0:  # Motoru durdurmak için hızın sıfır olması gerekir
                self.__calisiyor_mu = False
                print("Motor durduruldu.")
            else:
                print("Motoru durduramazsınız. Lütfen önce hızı sıfırlayın.")
        else:
            print("Motor zaten kapalı.")

    def hiz_artir(self, miktar):
        if self.__calisiyor_mu:  # Eğer motor çalışıyorsa hız değiştirilebilir
            self.__hiz += miktar
            if self.__hiz < 0:  # Hız sıfırın altına düşerse sıfırlıyoruz
                self.__hiz = 0
            print(f"Hız {miktar} km/h { 'artırıldı' if miktar > 0 else 'azaltıldı' }. Şu anki hız: {self.__hiz} km/h")
        else:
            print("Motor çalışmıyor. Önce motoru başlatmalısınız.")

    def hiz_goruntule(self):
        print(f"Şu anki hız: {self.__hiz} km/h")

araba = Araba()

araba.hiz_goruntule()
araba.hiz_artir(20)
araba.motoru_baslat()
araba.hiz_artir(-20)
araba.motoru_durdur()
araba.hiz_artir(-20)
araba.motoru_durdur()
