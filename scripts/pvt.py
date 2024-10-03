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
driver.get("https://workspaces.pexa.com.au/pexa_web/login.html")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
print('Assert')
element = driver.find_element(By.ID, 'username')
assert element.is_displayed()

print(driver.title)

driver.quit()
print('Done')
