# Requests + BeautifulSoup

import json
import requests
from bs4 import BeautifulSoup

# tek bir kitabın bilgilerini çekmek için

book_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(book_url)
soup = BeautifulSoup(response.content, 'html.parser')
# html içeriği beautifulsoup ile okunabilr hale getilirir
title = soup.find('h1').text
price = soup.find('p', class_='price_color').text

rating_element = soup.find('p', class_='star-rating')
rating_classes = rating_element.get('class')
rating = rating_classes[1]

print(f"Title: {title}")
print(f"Price: {price}")
print(f"Rating: {rating}")



# anasayfadaki tüm kitapları çekmek için

home_url = "https://books.toscrape.com/"
response = requests.get(home_url)
soup = BeautifulSoup(response.content, 'html.parser')
books = soup.find_all('article', class_='product_pod')
books_data = []
# kitap bilgilerini saklamak için boş liste
for book in books:
# bulunan her kitap için döngü
    title_link = book.find('h3').find('a')
    title = title_link.get('title')
 
    price_element = book.find('p', class_='price_color')
    price = price_element.text if price_element else 'No price'
 
    rating_element = book.find('p', class_='star-rating')
    if rating_element:
        rating_classes = rating_element.get('class')
        rating = rating_classes[1]
    else:
        rating = 'No rating'
 
    book_data = {
        'title': title,
        'price': price,
        'rating': rating
    }
    books_data.append(book_data)


# sonuclar
print(f"Found {len(books_data)} books")
print("\nFirst 5 books:")
for i, book in enumerate(books_data[:5]):
    print(f"{i+1}. {book['title']} - {book['price']} - {book['rating']} stars")
print(f"\nTotal books scraped: {len(books_data)}")

# verileri json dosyasına kaydetmekicin
with open("data/books.json", "w", encoding="utf-8") as file:
    json.dump(books_data, file, ensure_ascii=False, indent=4)

print("\nVeriler data/books.json dosyasına kaydedildi.")