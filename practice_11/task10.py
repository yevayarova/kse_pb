import requests
from bs4 import BeautifulSoup
import os

def download_gutenberg_book(book_id):
    # URL сторінки книги
    page_url = f"https://www.gutenberg.org/ebooks/{book_id}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(page_url, headers=headers)
    if response.status_code != 200:
        print("❌ Не вдалося отримати сторінку книги.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    link = soup.find('a', string='Plain Text UTF-8')
    if not link:
        print("❌ Не знайдено текстової версії книги.")
        return

    href = link['href']
    file_url = f"https://www.gutenberg.org{href}" if href.startswith('/') else href

    # Назва файлу
    file_name = f"book_{book_id}.txt"

    # 🔽 Шлях до твоєї папки
    save_folder = "D:/книги гумберта"
    os.makedirs(save_folder, exist_ok=True)
    full_path = os.path.join(save_folder, file_name)

    # БЕЗПЕЧНЕ СКАЧУВАННЯ ФАЙЛУ chunk за chunk
    try:
        with requests.get(file_url, headers=headers, stream=True, timeout=30) as r:
            r.raise_for_status()
            with open(full_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        print(f"✅ Книга збережена як: {full_path}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Помилка під час завантаження: {e}")

# ====== ГОЛОВНА ПРОГРАМА ======
book_id = input("Введи ID книги з Gutenberg: ").strip()
download_gutenberg_book(book_id)
