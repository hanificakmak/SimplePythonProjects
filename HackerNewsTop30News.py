# without API

import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup

target_url = "https://news.ycombinator.com/newest"
response = requests.get(target_url)
soup = bs(response.text, features="html.parser")

news = soup.find_all('tr', class_ = 'athing')

for new in news:
    heading = new.find('span', class_ ='titleline').find('a').text
    link = new.find('span', class_='titleline').find('a')['href']

    rank = new.find('span', class_='rank').text.strip('.')

    print(f"{rank}. {heading}")
    print(f"   {link}\n")
