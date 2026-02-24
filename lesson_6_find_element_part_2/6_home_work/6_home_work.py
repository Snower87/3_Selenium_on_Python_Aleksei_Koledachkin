import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#На странице https://testautomationpractice.blogspot.com/
url = "https://testautomationpractice.blogspot.com/"
driver.get(url)
time.sleep(5)
# 1. Найти иконку Wikipedia по имени класса
icon_wiki = driver.find_element("class name", "wikipedia-icon")
# 2. Найти поле ввода Wikipedia по id
input_wiki = driver.find_element("id", "name")
# 3. Найти кнопку поиска Wikipedia по классу
btn_find_wiki = driver.find_element("class name", "wikipedia-search-button")
# 4. Найти любой другой элемент на странице по тегу
find_tag = driver.find_element("tag name", "body")
print(find_tag)
