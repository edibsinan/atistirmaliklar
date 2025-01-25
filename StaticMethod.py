class Geometri:
    @staticmethod
    def alan(en, boy):
        """
        Bu metot, bir dikdörtgenin en ve boyunu alarak alanını hesaplar.
        """
        return en * boy  # Alan formülü: en * boy

# Statik metodu doğrudan sınıf adıyla çağırabiliriz
dikdortgen_alan = Geometri.alan(5, 10)  # en=5, boy=10 olan dikdörtgenin alanını hesapla

print(f"Dikdörtgenin alanı: {dikdortgen_alan}")
