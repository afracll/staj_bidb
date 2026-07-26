
#api veri çekme

import json
import math
import requests


def wikipedia_veri_cek(arama_terimi, limit=5):

    search_url = "https://tr.wikipedia.org/w/api.php"

    # robot engeline takılmamak için user-agent tanımı
    headers = {"User-Agent": "OdevScraper/1.0 (contact@example.com)"}

    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": arama_terimi,
        "srlimit": limit,
        "format": "json",
    }

    print(f"'{arama_terimi}' konusu Wikipedia'da aranıyor...\n")
    response = requests.get(search_url, headers=headers, params=search_params)

    if response.status_code != 200:
        print(f"Arama hatası! Durum kodu: {response.status_code}")
        return

    search_results = response.json().get("query", {}).get("search", [])
    toplanan_veriler = []

    # api verileri çekme
    for item in search_results:
        baslik = item["title"]
        print(f"-> Veriler işleniyor: {baslik}")

        # rest api ile ozet alıyorum
        summary_url = f"https://tr.wikipedia.org/api/rest_v1/page/summary/{requests.utils.quote(baslik)}"
        detail_response = requests.get(summary_url, headers=headers)

        if detail_response.status_code == 200:
            data = detail_response.json()
            ozet_metni = data.get("extract", "")

            # kelime sayısı
            kelime_sayisi = len(ozet_metni.split())

            # verilerim
            toplanan_veriler.append(
                {
                    "baslik": data.get("title"),
                    "dil": data.get("lang"),
                    "ozet": ozet_metni,
                    "kelime_sayisi": kelime_sayisi,
                    "son_guncelleme": data.get("timestamp"),
                    "sayfa_url": data.get("content_urls", {})
                    .get("desktop", {})
                    .get("page"),
                    "gorsel_url": data.get("thumbnail", {}).get("source")
                    if data.get("thumbnail")
                    else "Görsel yok",
                }
            )

    # json yaz
    output_path = "data/wiki_veriler.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(toplanan_veriler, f, ensure_ascii=False, indent=4)

    print("\n")
    print(
        f"İşlem Tamamlandı! {len(toplanan_veriler)} adet makale verisi '{output_path}' dosyasına kaydedildi."
    )
    print("\n")


wikipedia_veri_cek("Yapay zeka", limit=5)