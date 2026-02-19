from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 1. Создаем объект сервис, который отвечает за открытие/закрытие браузера
service = Service(executable_path=ChromeDriverManager().install())
# 2. Прокидываем его в качестве init-аргумента в наш Хром
driver = webdriver.Chrome(service=service)