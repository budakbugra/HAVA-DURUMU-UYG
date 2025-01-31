# 🌤 Hava Durumu Uygulaması
Bu proje, OpenWeather API kullanarak seçilen şehirlerin hava durumu bilgilerini gösteren bir Python uygulamasıdır. Kullanıcı, anlık hava durumu ve 5 günlük tahmin alabilir. Favorilere şehir ekleyip o şehirler üzerinden işlem yapabilir.
## 🚀 Özellikler
🌍 Anlık hava durumu bilgisi

🔮 1-5 günlük hava tahmini

📌 Favori şehirleri ekleyip yönetme

🌡️ Sıcaklık birimi seçimi (Celsius, Fahrenheit, Kelvin)

🔑 Çevresel değişkenler ile API anahtarı güvenliği

## 🛠 Kurulum
Projeyi klonlayın:  
```bash
git clone https://github.com/kullanıcı_adı/hava-durumu-uygulamasi.git
cd hava-durumu-uygulamasi

## GEREKLİ KÜTÜPHANELERİ EKLEYİN
pip install -r requirements.txt
```
## 🔑 API Anahtarı Ayarlama
OpenWeather sitesine kaydolun ve API anahtarınızı alın.


.env dosyasına aşağıdaki satırı ekleyin:

```
API_KEY=your_api_key_here
```

## 🎯 Kullanım
Uygulamayı başlatmak için aşağıdaki komutu çalıştırın:

```
python FİNAL_PROJESİ.py
```

## 🤝 Katkıda Bulunma
Katkıda bulunmak isterseniz, lütfen bir Pull Request oluşturun veya issue açın.

## 📸 Uygulama Ekran Görüntüleri

### 🌤 Anlık Hava Durumu
![Anlık Hava Durumu](anlik_hava_durumu.png)

### ⭐ Favori Şehirler Listesi
![Favori Şehirler](favori_sehirler.png)


## 🎯Kodun Amacı

### Kullanıcı Tercihlerini Alma:

Kullanıcıdan hava durumu bilgilerini alacağı şehri ve sıcaklık birimini seçmesi istenir.
Sıcaklık birimi, Celsius (C), Fahrenheit (F) veya Kelvin (K) olarak belirlenir ve buna göre uygun birim seçimi yapılır. Bu tercihler, hava durumu API'sine gönderilir.

### Anlık Hava Durumu Bilgisi Sağlamak:

Kullanıcı tarafından girilen şehir için OpenWeather API'si üzerinden anlık hava durumu bilgisi alınır.
Alınan verilerle, şehir adı, sıcaklık, hava durumu açıklaması, hissedilen sıcaklık ve nem gibi bilgiler ekrana yazdırılır.


### Hava Durumu Tahmini Sağlamak:

Kullanıcıya, kaç günlük hava durumu tahmini almak istediği sorulur (1-5 gün arası).
API'den alınan verilerle, her bir gün için hava durumu tahminleri (tarih, sıcaklık, hava durumu açıklamaları) gösterilir.


### Şehir Değiştirme:

Kullanıcı, hava durumu bilgilerini almak istediği şehri değiştirebilir. Bu, şehir bilgisini sıfırlayarak tekrar şehir seçilmesini sağlar.


### Favori Şehirler Listesi:

Kullanıcı, sıkça hava durumu bilgisi almak istediği şehirleri favorilerine ekleyebilir.
Favori şehirler listesi ekrana yazdırılır ve kullanıcı bu şehirlerden birini ana şehir olarak seçebilir.

### Ana Menü ve Seçimler:

Programın ana menüsünde, kullanıcının tercih ettiği işlemi seçmesine olanak tanınır:

Anlık hava durumu görmek

Hava durumu tahmini almak

Şehir değiştirmek

Favorilere şehir eklemek

Favori şehirleri göstermek

Çıkış yapmak

