from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time



def parser_kabum(url):

    product = {}

    lista_produtos = []


    try:

        # Inicializa o ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get(url)
        time.sleep(10)

        # Localiza a div pai
        promo_div = driver.find_element(By.CLASS_NAME, 'swiper-wrapper')
        if promo_div:
            # Pega todos os produtos
            produtos = promo_div.find_elements(By.CLASS_NAME, 'productCard')

            for produto in produtos:

                product = {}

                # Pega o link
                link_element = produto.find_element(By.CLASS_NAME, 'productLink')
                if link_element:
                    href = link_element.get_attribute('href')
                    product['link'] = href

                # Pega a imagem
                img_element = produto.find_element(By.CLASS_NAME, 'imageCard')
                if img_element:
                    src = img_element.get_attribute('src')
                    product['image'] = src

                try:
                    name_element = produto.find_element(By.CLASS_NAME, 'bESAoj')
                    span_element = name_element.find_element(By.TAG_NAME, 'span')
                    product['name'] = span_element.text
                except:
                    product['name'] = 'Nome indisponível'

                try:
                    price_element = produto.find_element(By.CLASS_NAME, 'availablePricesCard')
                    span_element = price_element.find_element(By.CLASS_NAME, 'priceCard')
                    product['price'] = span_element.text
                except:
                    product['price'] = 'Preço indisponível'

                lista_produtos.append(product)

        print(lista_produtos)

        # Fecha o navegador após o scraping
        driver.quit()

    except Exception as e:
        print("Falha ao usar Selenium:", e)

