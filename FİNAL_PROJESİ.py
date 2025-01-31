import requests
from dotenv import load_dotenv
import os

# Favoriler listesi
favoriler = []

# Kullanıcı tercihlerinin alındığı sınıf
class KullanıcıTercihleri:
    def __init__(self):
        self.sehir = None
        self.birim = ""
        self.units = ""

    def veri_al(self):
        if self.sehir is None:
            self.sehir = input("Hava Durumunu Öğrenmek İstediğiniz Şehri Girin: ")

        while True:
            self.birim = input("Sıcaklık Birimini Seçin. Celsius için 'C', Fahrenheit için 'F', Kelvin için 'K': ")
            if self.birim.upper() == "C":
                print("Sıcaklık Biriminiz Celsius Olarak Ayarlanmıştır.")
                self.units = "metric"
                break
            elif self.birim.upper() == "K":
                print("Sıcaklık Biriminiz Kelvin Olarak Ayarlanmıştır.")
                self.units = "standard"
                break
            elif self.birim.upper() == "F":
                print("Sıcaklık Biriminiz Fahrenheit Olarak Ayarlanmıştır.")
                self.units = "imperial"
                break
            else:
                print("Yanlış Bir Tuşlama Yaptınız. Lütfen Tekrar Deneyin.")

# Hava durumu sınıfı
class HavaDurumu(KullanıcıTercihleri):

    def __init__(self):
        super().__init__()
        load_dotenv()
        self.api_key = os.getenv("API_KEY")  # .env dosyasından alınan API anahtarı
        self.veri_al()

    def anlık_hava_durumu(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.sehir}&appid={self.api_key}&lang=tr&units={self.units}"
        response = requests.get(url)
        veri = response.json()

        if response.status_code == 200:
            print(f"\n{veri['name']} Şehri İçin Anlık Hava Durumu:")
            print(f"Sıcaklık: {round(veri['main']['temp'])}{self.birim}")
            print(f"Hava Durumu: {veri['weather'][0]['description']}")
            print(f"Hissedilen Sıcaklık: {round(veri['main']['feels_like'])}{self.birim}")
            print(f"Nem: %{veri['main']['humidity']}")
        else:
            print(f"Hata oluştu! Kod: {response.status_code}")

    def tahmin_hava_durumu(self):
        while True:
            try:
                gün_sayısı = int(input("\nKaç Günlük Tahmin Almak İstiyorsunuz? (1-5): "))
                if 1 <= gün_sayısı <= 5:
                    break
                print("Lütfen 1 ile 5 arasında bir sayı girin.")
            except ValueError:
                print("Geçerli bir sayı giriniz.")

        url = f"https://api.openweathermap.org/data/2.5/forecast?q={self.sehir}&appid={self.api_key}&lang=tr&units={self.units}"
        response = requests.get(url)
        veri = response.json()

        if response.status_code == 200:
            print(f"\n{self.sehir} için {gün_sayısı} günlük hava durumu tahmini:")
            for i in range(0, gün_sayısı * 8, 8):
                print(f"Tarih: {veri['list'][i]['dt_txt']}")
                print(f"Sıcaklık: {round(veri['list'][i]['main']['temp'])}°{self.birim}")
                print(f"Hava Durumu: {veri['list'][i]['weather'][0]['description']}\n")
        else:
            print(f"Hata oluştu! Kod: {response.status_code}")

    def yeniden_sehir_sec(self):
        self.sehir = None
        self.veri_al()

    def favori_sehir(self):
        if self.sehir not in favoriler:
            favoriler.append(self.sehir)
            print(f"{self.sehir} favorilere eklendi.")
        else:
            print(f"{self.sehir} zaten favorilerinizde.")

    def favori_sehir_goster(self):
        if favoriler:
            print("\nFavori Şehirleriniz:")
            for i, sehir in enumerate(favoriler, 1):
                print(f"{i}. {sehir}")

            favori_secim = input("\nŞehir Seçmek İstiyor Musunuz? (İstiyorsanız '1' tuşuna, İstemiyorsanız '2' tuşuna basınız): ")

            if favori_secim == "1":
                while True:
                    try:
                        secim = int(input("Hangi Şehri Seçmek İstiyorsunuz? (Başındaki Sayıyı Girin): "))
                        if 1 <= secim <= len(favoriler):
                            self.sehir = favoriler[secim - 1] 
                            print(f"{self.sehir} artık ana şehir olarak seçildi.")
                            break
                        else:
                            print("Geçersiz seçim, lütfen tekrar deneyin.")
                    except ValueError:
                        print("Geçerli bir sayı giriniz.")

            else:
                print("Ana Ekrana Gönderiliyorsunuz")
                
        else:
            print("Henüz favorilere eklenmiş şehir yok.")

if __name__ == "__main__":
    hava_durumu = HavaDurumu()

    while True:
        secim = input("\n1. Anlık Hava Durumu\n2. Hava Durumu Tahmini\n3. Şehir Değiştir\n4. Favorilere Ekle\n5. Favori Şehirleri Göster\n6. Çıkış\nSeçiminiz: ")

        if secim == "1":
            hava_durumu.anlık_hava_durumu()
        elif secim == "2":
            hava_durumu.tahmin_hava_durumu()
        elif secim == "3":
            hava_durumu.yeniden_sehir_sec()
        elif secim == "4":
            hava_durumu.favori_sehir()
        elif secim == "5":
            hava_durumu.favori_sehir_goster()
        elif secim == "6":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")
