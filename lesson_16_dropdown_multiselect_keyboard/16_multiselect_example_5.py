import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
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

MULTISELECT_LOCATOR = ("xpath", "//input[@id='react-select-4-input']")

driver.get("https://demoqa.com/select-menu") # Страница для работы
time.sleep(2)

"""
driver.find_element(*MULTISELECT_LOCATOR).send_keys("Green")
# Варианты подтверждения выбора:
# 1 Способ - нажать 'Tab'
# 2 Способ - нажать 'Enter'
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.TAB)
time.sleep(2)
"""

driver.find_element(*MULTISELECT_LOCATOR).send_keys("Red")
time.sleep(2)
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(2)

# Выбор элемента по неполному названию селекта:
driver.find_element(*MULTISELECT_LOCATOR).send_keys("Gre")
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.TAB)
time.sleep(2)
