import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

types_of_money = [
    'Dólar americano',
    'Dólar australiano',
    'Dólar bahamense',
    'Dólar barbadense',
    'Dólar belizenho',
    'Dólar bermudense', 
    'Dólar bruneano',
    'Dólar canadense',
    'Dólar das Ilhas Cayman',
    'Dólar das Ilhas Salomão',
    'Dólar de Hong Kong',
    'Dólar de Trinidad e Tobago',
    'Dólar do Caribe Oriental',
    'Dólar fijiano',
    'Dólar guianense',
    'Dólar jamaicano',
    'Dólar namibiano',
    'Dólar neozelandês',
    'Dólar singapuriano',
    'Dólar surinamês'
]

prices = []

def dolar_web_scrapping():
    driver = webdriver.Chrome()
    driver.get('https://google.com')

    # Fazendo a primeira iteração no Google
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(types_of_money[0] + ' para real hoje')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

    dolar = get_value_of_dolar(driver)
    prices.append(dolar)

    for i in range(1, len(types_of_money)):
        select_types = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/select')
        types = Select(select_types)
        types.select_by_visible_text(types_of_money[i])
        dolar = get_value_of_dolar(driver)
        prices.append(dolar)
        time.sleep(1)

    for i in range(len(prices)):
        print(types_of_money[i] + ": R$ " + prices[i])

def get_value_of_dolar(driver):
    return driver.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').text

if __name__ == '__main__':
    dolar_web_scrapping() 