"""Bir Ogrenci sınıfı oluşturun. Bu sınıf, tüm öğrenciler için 
geçerli olan okulun adını belirten bir sınıf özelliğine sahip olsun. 
Ayrıca, bu sınıf, okul adını değiştirecek bir sınıf metoduna da sahip olmalıdır. 
Bu metod classmetodu sayesinde okulun adını değiştirebilmelidir. Son olarak, 
sınıf metodunu kullanarak okul adını güncelleyin ve yeni okul adını ekrana yazdırın."""

class Ogrenci:
    # Sınıf düzeyinde ortak bir özellik
    okul_adi = "Evren ilkogretim"
    
    # Sınıf metodunu tanımlıyoruz
    @classmethod
    def okul_adini_degistir(cls, yeni_okul_adi):
        cls.okul_adi = yeni_okul_adi  # Sınıf özelliğini güncelliyoruz


print("Eski okul: ",Ogrenci.okul_adi)
# Okul adını değiştirmek için sınıf metodunu çağırıyoruz

Ogrenci.okul_adini_degistir("bilim ve Sanat")

# Yeni okul adını ekrana yazdırıyoruz
print("Güncellenmiş okul adı:", Ogrenci.okul_adi)
