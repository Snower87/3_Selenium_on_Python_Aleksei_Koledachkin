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
# Важно знать, что чек-бокс реализуется с помощью тега <input> , но с type=’checkbox’
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

driver.get("http://the-internet.herokuapp.com/checkboxes")
time.sleep(2)

CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
print("До клика:", driver.find_element(*CHECKBOX_1).get_attribute("checked")) # -> None
driver.find_element(*CHECKBOX_1).click()
print("После клика:", driver.find_element(*CHECKBOX_1).get_attribute("checked"))  # -> true (string)
print("После клика, is_selected():", driver.find_element(*CHECKBOX_1).is_selected())  # -> True (string)
time.sleep(2)

assert driver.find_element(*CHECKBOX_1).get_attribute("checked") == "true"

# Способы получения статуса checkbox'а:
# Вариант 1 - атрибут "checked"
# Тк значение атрибута "checked" - это тип стринг, то:
# 1. проверяется, что значение is not None
assert driver.find_element(*CHECKBOX_1).get_attribute("checked") is not None
# 2. Что значение строки = "true"
assert driver.find_element(*CHECKBOX_1).get_attribute("checked") == "true"

# Вариант 2 - метод is_selected() -> True
assert driver.find_element(*CHECKBOX_1).is_selected() == True
