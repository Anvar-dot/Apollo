import requests
from bs4 import BeautifulSoup

URL = "https://manascinema.com/schedule"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем все блоки с фильмами
film_blocks = soup.find_all("div", class_="schedule-item")

for block in film_blocks:
    # Извлекаем название фильма
    title = block.find("h4", class_="schedule-title")
    if title:
        title = title.get_text(strip=True)
    else:
        title = "Без названия"

    # Извлекаем время сеанса
    time = block.find("span", class_="schedule-time")
    if time:
        time = time.get_text(strip=True)
    else:
        time = "Время не указано"

    print(f"Фильм: {title}, Время: {time}")
