# LAN-Scanner-Odev

##Gerekli Kütüphaneler

scapy
configparser

##Gerekli Kütüphanelerin Kurulumu

"scapy" için:

```
pip install scapy
```

"configparser" için:

```
pip install configparser
```

##Programı Nasıl Çalıştırırım?

Programın olduğu dizinde root yetkilerine sahip olarak şu şekilde çalıştırabiliriz:

```
sudo python main.py
```

Programı ilk çalıştırdığımızda ağımızdaki ip ve bu iplere karşılık gelen mac adresleri main.py ile aynı dizinde bulunan config.conf dosyasının içindeki [IP-MAC] bölümüne kaydedilir. Bundan sonraki her çalıştırmamızda kullanıcının aksiyonlarına göre liste güncellenir.
