import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
action = ActionChains(driver)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/sortable")

# Ваши локаторы
SOURCE_LOCATOR = ("xpath", "(//div[@class='list-group-item list-group-item-action'])[1]")
TARGET_LOCATOR = ("xpath", "(//div[@class='list-group-item list-group-item-action'])[5]")

# Находим элементы
SOURCE = driver.find_element(*SOURCE_LOCATOR)  # Находим source-элемент
TARGET = driver.find_element(*TARGET_LOCATOR)  # Находим target-элемент

wait.until(EC.element_to_be_clickable(SOURCE))  # Ждем кликабельности source-элемента
time.sleep(2)
action.drag_and_drop(SOURCE, TARGET).perform()  # Перетаскиваем
time.sleep(2)





