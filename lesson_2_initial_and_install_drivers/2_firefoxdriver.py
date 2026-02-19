from time import sleep

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.firefox.service import Service as FirefoxService # импортируем нужный класс сервиса


# 1. Создаем объект сервис, который отвечает за открытие/закрытие браузера
service = Service(executable_path=GeckoDriverManager().install())
# 2. Прокидываем его в качестве init-аргумента в наш Хром
driver = webdriver.Firefox(service=service).quit()

sleep(2)

driver.quit()

