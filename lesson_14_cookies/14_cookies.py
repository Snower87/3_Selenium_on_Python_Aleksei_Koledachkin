import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Создаем объект options
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_argument("--user-agent=Selenium")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36")
# Скрытие присутствия Selenium
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 2. Создание экземпляра веб-драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Переход на веб-страницу
driver.get("https://www.freeconferencecall.com/ru/ru/login")

# - Получение куки по имени
print(driver.get_cookie("country_code"))
# - Получение всех куков
print(driver.get_cookies())

# - Добавление куков
driver.add_cookie({
    "name": "Example",
    "value": "Kukushka"
})

# - Проверяем все куки
print(driver.get_cookies())

# - Замена куки: удаляем, потом добавляем
before = driver.get_cookie("split")
print(f"before: {before}")
driver.delete_cookie("split")
driver.add_cookie({
    "name": "split",
    "value": "split222"
})
after = driver.get_cookie("split")
print(f"before: {after}")

# - Удаление всех куков
driver.delete_all_cookies()
driver.add_cookie({
    "name": "split_new",
    "value": "new_Value!!!"
})
print(driver.get_cookies())
