import time

from selenium import webdriver

options = webdriver.ChromeOptions()
# Добавляем работу с расширениями
options.add_extension("extensions/AdBlock_Chrome.crx") # валится при добавлении

driver = webdriver.Chrome(options=options)
driver.get("https://ya.ru")

time.sleep(10)