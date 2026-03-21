import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)  # создает обьект через который будут выполняться действия мыши

# Для наведения на элемент, action использует метод move_to_element(), где в качестве аргумента принимает веб-элемент для наведения.

# В примере ниже, мы реализуем цепочку из 3 шагов:
# 1. Навестись на меню
# 2. Навестись на подменю
# 3. Кликнуть на нужный элемент меню

driver.get("https://demoqa.com/menu")

STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

STEP_1 = driver.find_element(*STEP_1_LOCATOR)
STEP_2 = driver.find_element(*STEP_2_LOCATOR)
STEP_3 = driver.find_element(*STEP_3_LOCATOR)

      # Наведение не пункт меню # Наведение на подпункт # Пауза 5 # Клик на подпункт
action.move_to_element(STEP_1) \
    .move_to_element(STEP_2) \
    .pause(5) \
    .click(STEP_3).perform() # Выполнить

time.sleep(5)