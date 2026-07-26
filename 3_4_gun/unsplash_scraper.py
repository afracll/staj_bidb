
# selenium ile

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    print("Unsplash sayfasına gidiliyor...")
    driver.get("https://unsplash.com/t/nature")
    
    time.sleep(4)

    print("Sayfa aşağı kaydırılıyor...")
    for i in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    print("Sayfadaki görsel verileri toplanıyor...")
    images = driver.find_elements(By.TAG_NAME, "img")
    
    photos_data = []

    for img in images:
        src = img.get_attribute("src")
        alt = img.get_attribute("alt")

        if src and "images.unsplash.com/photo-" in src:
            description = alt if alt else "Açıklama yok"
            
            print(f"-> Çekilen Fotoğraf: {description}")

            photos_data.append({
                "description": description,
                "image_url": src
            })

# veri kaydet
    with open("data/unsplash_photos.json", "w", encoding="utf-8") as file:
        json.dump(photos_data, file, ensure_ascii=False, indent=4)

    print("\n--------------------------------------------------")
    print(f"İşlem Tamamlandı! Toplam {len(photos_data)} adet fotoğraf verisi kaydedildi.")
    print("--------------------------------------------------")

except Exception as e:
    print(f"Bir hata oluştu: {e}")

finally:
    driver.quit()