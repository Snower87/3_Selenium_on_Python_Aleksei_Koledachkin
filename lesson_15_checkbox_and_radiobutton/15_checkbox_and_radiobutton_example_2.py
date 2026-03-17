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

CHECKBOX_HOME_STATUS = ("xpath", "//input[@id='tree-node-home']")
CHECKBOX_HOME_ACTION = ("xpath", "//span[@class='rc-tree-checkbox rc-tree-checkbox-checked'][1]")

driver.get("https://demoqa.com/checkbox")
time.sleep(2)

#print("До клика:", driver.find_element(*CHECKBOX_HOME_STATUS).is_selected)
#driver.find_element(*CHECKBOX_HOME_ACTION).click()
#print("После клика:", driver.find_element(*CHECKBOX_HOME_STATUS).is_selected)

# Сам чек-бокс для проверки статуса
HOME_CHECKBOX = ("xpath", "//input[@aria-label='for screen reader']")

# Элемент для клика, чтобы выставить флажок
#HOME_BUTTON = ("xpath", "//span[text()='Home']/..")
HOME_BUTTON = ("xpath", '//span[@role="checkbox" and @aria-label="Select Home"]')


# Кликаем на элемент, который выставляет чек-бокс
driver.find_element(*HOME_BUTTON).click()
time.sleep(5)

# Выведем статус чек-бокса, так как он меняется при клике на элемент, отвечающий за выставление флажка
print(driver.find_element(*HOME_BUTTON).is_selected())
