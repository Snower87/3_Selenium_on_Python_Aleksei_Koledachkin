import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)  # создает обьект через который будут выполняться действия мыши

driver.get("https://demoqa.com/buttons")
time.sleep(3)
DB_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")

BUTTON = driver.find_element(*DB_BUTTON_LOCATOR)

# 1. Двойной клик левой кнопкой мыши
action.double_click(BUTTON).perform()
time.sleep(3)

# 2. Для клика правой кнопкой мыши action использует метод context_click()
RС_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClickBtn']")
BUTTON = driver.find_element(*RС_BUTTON_LOCATOR)
action.context_click(BUTTON).perform()