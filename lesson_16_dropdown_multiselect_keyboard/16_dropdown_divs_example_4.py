import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

SELECT_LOCATOR = ("xpath", "//input[@id='react-select-3-input']")

SELECT_ONE = ("xpath", "//div[@id='selectOne']")
OPTION_PROF = ("xpath", "//div[text()='Prof.']")

driver.get("https://demoqa.com/select-menu") # Страница для работы
time.sleep(2)

# Если современный селектор реализован через <div>
# Способ 1 - Вводим строку "Ms." и нажимаем ENTER
"""
driver.find_element(*SELECT_LOCATOR).send_keys("Ms.")
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(2)
"""

# Способ 2 - получаем локаторы через setTimeout и кликаем на соотв. значение div
# !!! Для активации выполнения скриптов в DevTools надо ввести: allow pasting
# setTimeout(function() { debugger; }, 5000); - включит отложенный старт дебаг-режима в devtools.
driver.find_element(*SELECT_ONE).click()
time.sleep(3)
driver.find_element(*OPTION_PROF).click()
time.sleep(3)