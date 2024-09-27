
import requests
from bs4 import BeautifulSoup


def baseRequest(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        print("Falha na requisição!", e)
        return None

def parserExample(url):
    html = baseRequest(url)

    if html:
        soup = BeautifulSoup(html, 'lxml')

        print(soup.prettify())

        promo_div = soup.find('div', class_='swiper-wrapper')

        if promo_div:
            produtos = promo_div.find_all('a', class_='productLink')
            for item in produtos:
                href = item.get('href')
                if href:
                    print(href)
        else:
            print("Não foi possível localizar a div com a classe swiper-wrapper.")
