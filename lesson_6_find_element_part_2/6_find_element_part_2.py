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
elements = driver.find_elements("class name", "number")

# Кликаем по 3 элементу
elements[2].click()
print(elements)