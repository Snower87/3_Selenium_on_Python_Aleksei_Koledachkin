import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открываем страницу
driver.get("https://northpole.com/")

# Поиск нужного элемента
#driver.find_element(By.ID, "top").click()
element = driver.find_element(By.LINK_TEXT, "Holiday Breads")

# Прокручиваем страницу до найденного элемента
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# Проверяем адрес открытой страницы
assert driver.current_url == "https://northpole.com/Kitchen/Cookbook/Breads"

time.sleep(2)