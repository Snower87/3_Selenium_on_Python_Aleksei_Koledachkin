#from time import sleep
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 1. Создаем объект сервис, который отвечает за открытие/закрытие браузера
service = Service(executable_path=ChromeDriverManager().install())
# 2. Прокидываем его в качестве init-аргумента в наш Хром
driver = webdriver.Chrome(service=service)
# 3. Переходим на страницу Яндекса и ждем 10 сек
driver.get("https://yandex.ru/")
time.sleep(10)
# 4. Нажимаем в браузере кнопку "Назад" с задержкой 5 сек
driver.back() # <-- кнопка "Назад"
time.sleep(5)
# 5. Нажимаем в браузере кнопку "Вперед" с задержкой 5 сек
driver.forward() # --> кнопка "Вперед"
time.sleep(5)
# 6. Нажимаем в браузере кнопку "Обновить" с задержкой 5 сек
driver.refresh() # --> кнопка "Обновить"
time.sleep(5)