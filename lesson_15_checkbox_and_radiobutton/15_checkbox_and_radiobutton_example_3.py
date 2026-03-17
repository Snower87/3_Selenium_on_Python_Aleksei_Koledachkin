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

#-------------------------------------
# Правило:
# 1 элемент для взаимодействия и 1 элемент для получения статуса
#-------------------------------------

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

#-------------------------------------
# Правило:
# - 1 элемент для взаимодействия и
# - 1 элемент для получения статуса
#-------------------------------------

YES_RADIO_STATUS = ("xpath", "//input[@id='yesRadio']")
YES_RADIO_ACTION = ("xpath", "//label[@for='yesRadio']")

NO_RADIO_STATUS = ("xpath", "//input[@id='noRadio']")
NO_RADIO_ACTION = ("xpath", "//label[@for='noRadio']")

driver.get("https://demoqa.com/radio-button ")
time.sleep(2)

before = driver.find_element(*YES_RADIO_STATUS).is_selected()
print(before)
driver.find_element(*YES_RADIO_ACTION).click()
after = driver.find_element(*YES_RADIO_STATUS).is_selected()
print(after)

print("Доступность активной radio:", driver.find_element(*YES_RADIO_STATUS).is_enabled())
print("Доступность НЕактивной radio:", driver.find_element(*NO_RADIO_STATUS).is_enabled())