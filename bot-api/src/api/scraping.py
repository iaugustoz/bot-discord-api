from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time



def parser_selenium(url):
    try:
        # Inicializa o ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get(url)
        time.sleep(5)

        # Localiza a div pai
        promo_div = driver.find_element(By.CLASS_NAME, 'swiper-wrapper')

        if promo_div:
            # Pega todos os links
            produtos = promo_div.find_elements(By.CLASS_NAME, 'productLink')

            for produto in produtos:
                href = produto.get_attribute('href')
                if href:
                    print(href)
        else:
            print("Não foi possível localizar a div com a classe swiper-wrapper.")

        # Fecha o navegador após o scraping
        driver.quit()

    except Exception as e:
        print("Falha ao usar Selenium:", e)
