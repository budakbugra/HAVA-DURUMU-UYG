import requests

API_KEY  = "d859954a90b2083a19115cb616cd4810"

def hava_durumu_ogrenme():
    sehir = input("Hava Durumunu Ogrenmek Istediginiz Sehiri Girin: ")

    birim = input("Sıcaklı Birimini Seçin.\nCelcius için ""C""\nFahreinheit için ""F""\nKelvin için ""K"" tuşunu girin")
    
    if birim == "C":
        print("Sıcaklık Biriminiz Celcius Olarak Ayarlanmıştır.")

        units = "metric" #Celciusun openweatherdaki birimi

    elif birim == "K":
        print("Sıcaklık Biriminiz Kelvin Olarak Ayarlanmıştır")

        units = "standard" #Kelvinin openweatherdaki birimi

    elif birim == "F":
        print("Sıcaklık Biriminiz Fahreinheit Olarak Ayarlanmıştır.")

        units = "imperial" #Fahreinheitin openweatherdaki birimi

    else:
        print("Yanlış Bir Tuşlama Yaptınız. Lütfen Tekrar Deneyin.")

        return  

    url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={API_KEY}&lang=tr&units={units}"
    
    veri_cekme = requests.get(url)

    veri = veri_cekme.json() #json formatına çeviriyorum.

    if veri_cekme.status_code == 200:
        
        sehir_adi = veri["name"]
        sicaklık = veri["main"]["temp"]
        hava_durumu = veri["weather"][0]["description"] # sıfıra indeksledim çünkü hava durumunun birden fazla olması durumunda kafa karışıklığı olup hata vermesini istemedim.
        hissedilen = veri["main"]["feels_like"]
        nem_miktarı = veri["main"]["humidity"]

        print(f"Şehir Adı:{sehir_adi}\nSıcaklık Miktarı:{sicaklık}{birim}\nHava Durumu Bilgisi:{hava_durumu}\nHissedilen Sıcaklık:{hissedilen}\nNem Miktari:{nem_miktarı}")
        

    elif veri_cekme.status_code == 404:
        print(f"Şehir Adını Kontrol Edin. Hata Kodu:{veri_cekme.status_code}")

    elif veri_cekme.status_code == 401:
        print(f"Geçersiz veya Eksik API kullanımı. Hata Kodu:{veri_cekme.status_code}")
