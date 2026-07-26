
# Web Scraping ve Veri Toplama Yöntemleri

Web üzerindeki farklı kaynaklardan veri çekmetekniklerini incelemek ve uygulamak amacıyla hazırlandı. 3 farklı temel veri toplama yöntemi denendi ve elde edilen tüm veriler düzenli bir şekilde data klasörü altına JSON formatında kaydedildi.


## Kullanılan Yöntemler Mantığı


### 1. Statik Web Scraping (books_scraper.py)
Hedef Kaynak: Books to Scrape (books.toscrape.com)
Kullanılan Kütüphaneler: requests, BeautifulSoup
Çalışma Mantığı: Statik HTML yapısına sahip bu sitede, sayfanın kaynak kodları çekilerek DOM ağacı üzerinden etiket ayrıştırması yapıldı. Kitapların başlık, fiyat ve puan bilgileri HTML etiketlerinden filtrelenerek toplandı.
Çıktı: data/books.json

### 2. Dinamik Web Scraping ve Tarayıcı Otomasyonu (unsplash_scraper.py)
Hedef Kaynak: Unsplash Nature (unsplash.com)
Kullanılan Kütüphaneler: selenium
Çalışma Mantığı: Unsplash gibi JavaScript ağırlıklı çalışan ve aşağı kaydırdıkça yeni içerik yükleyen (infinite scroll) sitelerde düz HTML istekleri yetersiz kalmaktadır. Bu nedenle Selenium WebDriver kullanılarak gerçek bir tarayıcı otomasyonu oluşturulmuş, sayfa kodla aşağı kaydırılmış ve yüklenen görsellerin adresleri ile açıklamaları çekilmiştir.
Çıktı: data/unsplash_photos.json

### 3. API Tabanlı Veri Çekme (wikipedia_scraper.py)
Hedef Kaynak: Wikipedia REST API & Action API (tr.wikipedia.org)
Kullanılan Kütüphaneler: requests, json, math
Çalışma Mantığı: HTML kodlarını kazımak yerine, Wikipedia'nın geliştiricilere sunduğu resmi API uç noktalarına (endpoints) istek atılmıştır. İlk adımda arama parametreleri ile makaleler listelenmiş, ikinci adımda REST API üzerinden makalelerin özetleri, kelime sayıları, son güncelleme tarihleri ve görsel bağlantıları temiz JSON verisi olarak alınmıştır.
Çıktı: data/wiki_veriler.json


## Kurulum ve Çalıştırma

kodları çalıştırmak için gerekli python kütüphanelerinin yüklenmesi gerekiyor:

pip install requests beautifulsoup4 selenium

chrome tarayıcısının ve uygun ChromeDriver sürücüsünün yüklü olduğundan eminsek scriptleri sırasıyla çalıştırabiliriz.

python books_scraper.py
python unsplash_scraper.py
python wikipedia_scraper.py
