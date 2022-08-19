from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome('C:/Users/seda/Downloads/chromedriver_win32/chromedriver.exe')

browser.get('https://www.sahibinden.com/arazi-suv-pickup-citroen-c3-aircross-1.5-bluehdi-feel?sorting=km-nu_asc')

time.sleep(2)
cars = browser.find_elements(By.CSS_SELECTOR, value='.searchResultsItem')
for car in cars:
    if car.get_attribute('data-id') is None:
        continue

    else:
        price = car.find_elements(by= By.CSS_SELECTOR, value = '.searchResultsPriceValue')
        year = car.find_elements(by=By.CSS_SELECTOR, value='.searchResultsAttributeValue')
        km = car.find_elements(by=By.CSS_SELECTOR, value='.searchResultsAttributeValue')
        print(price[0].text)
        print(year[0].text)
        print(km[0].text)


time.sleep(2)

browser.close()




