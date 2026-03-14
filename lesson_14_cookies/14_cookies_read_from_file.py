import os
import time
import pickle


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
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

cookies = pickle.load(open(os.getcwd() + "/cookies/cook.pkl", "rb"))
print("Считали куки из файл")

# Чтобы не было дубляжа куков - надо перед добавлением удалить вообще все!
driver.delete_all_cookies()

# перебираем все ранее сохраненые куки и добавляем по 1
for cookie in cookies:
    driver.add_cookie(cookie)

# driver.refresh() - чтобы куки применились
driver.refresh()
print("Куки применились!!!")