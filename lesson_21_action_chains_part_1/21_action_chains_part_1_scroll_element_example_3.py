import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)  # создает обьект через который будут выполняться действия мыши

# Зачастую нам необходимо сначала сделать скролл к элементу, чтобы при попытке взаимодействия с ним не получать разного рода ошибки.
# Для этого у action есть метод scroll_to_element()
# В целом ничего сложного и одного примера будет более чем достаточно:

driver.get("https://clipboardjs.com/")

SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")

SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)

action.scroll_to_element(SOME_ELEMENT).perform() # Используем скролл до элемента