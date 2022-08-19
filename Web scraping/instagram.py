from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import os
import wget

driver = webdriver.Chrome('C:/Users/seda/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://www.instagram.com/')
# chorome open instagram by the agency of wedriver library

time.sleep(1)

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input [name= 'username']")))
# web sayfasındaki input isimli elementi cekiyoruz

password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input [name= 'password']")))

time.sleep(1)
# validate username is empty should empty
username.clear()
password.clear()

#login otomatic full
username.send_keys("KoreanSeriesOne")
password.send_keys("Ak510716@")

#insta sayfasındaki şeyleri çekme ve what do you want you put the same area
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button [type= 'submit']"))).click()

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH," //button[contain(text(),'Not Now]"))).click()

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH," //input [@placeholder = 'Search']"))).click()

searchbox.clear()
keyword = "#cat"
searchbox.send_keys(keyword)


#cat is working when you put enter

driver.execute_script("window.scrollTo(0,400);")

#images in insta we are take of them
images = driver.find_element_by_id('img')
images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path,keyword[1:] + "s")
os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path,keyword[1:] + str(counter) + '.jpg')
    wget.dawnload(image,save_as)
    counter += 1
