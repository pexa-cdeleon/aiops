#!/usr/bin/env python3

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"/usr/bin/chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless=new")

driver = webdriver.Chrome(service=service,options=options)
driver.get("https:/www.pexa.com.au")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div[4]/a'))).click()
print(driver.title)

driver.quit()
print('Done')
