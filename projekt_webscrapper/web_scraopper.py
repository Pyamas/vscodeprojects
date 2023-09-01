import requests
from bs4 import BeautifulSoup

url = 'https://toscrape.com/'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    article_titles = soup.find_all('h2')

    with open('tytuly_artykulow.txt', 'w', encoding='utf-8')as file: 
        for title in article_titles:
            file.write(title.text + '\n')

else:
    print(f"nieudane zapytranie http. Kod statusu: {response.status_code}")