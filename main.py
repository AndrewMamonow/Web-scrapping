import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
SOURCE = requests.get('https://habr.com/ru/articles').text
soup = BeautifulSoup(SOURCE, 'html.parser')

for article in soup.find_all('article'):
    headline = article.h2.a.text
    post_link = article.find('a', class_='tm-title__link')['href']
    post_link = 'https://habr.com' + post_link
    public_date = article.find('a', class_='tm-article-datetime-published').time['title']
    
    for search_word in KEYWORDS:
        if (search_word.lower() in headline.lower()):
            print(f'Дата: {public_date} - Заголовок: {headline} - Ссылка: {post_link}')