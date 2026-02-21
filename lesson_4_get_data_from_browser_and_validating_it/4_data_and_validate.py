import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 1. Создаем объект сервис, который отвечает за открытие/закрытие браузера
service = Service(executable_path=ChromeDriverManager().install())
# 2. Прокидываем его в качестве init-аргумента в наш Хром
driver = webdriver.Chrome(service=service)
# 3. Открываем сайт Википедии
driver.get("https://www.wikipedia.org/")
# 4. Получаем адрес открытой url-страницы
url = driver.current_url
print("URL страницы:", url)
time.sleep(3)
# 5. Валидация/проверка url открытой страницы
assert url == "https://www.wikipedia.org/", "Ошибка в URL, открыта не та страница"
# 6. Получаем title (заголовок) страницы
current_title = driver.title
print("Заголовок страницы:", current_title)
# 7. Валидация/проверка title открытой страницы
assert current_title == "Wikipedia", "Некорректный заголовок страницы"