import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

# Implicit waits - Неявные ожидания
# Неявные ожидания задаются сразу для всего проекта (при инициализации драйвера):
# - используется для обнаружения элемента на странице (появления)
# - используется для find_element(), find_elements()
# - рекомендует использовать явные ожидания
# Использовать - либо одно, либо другое!!! Не мешать явные + неявные

# Explicit waits - Явные ожидания:
# - исчезновение элемента, текста элемента, состояния и тд
# - указываем для элемента, с  которым работаем


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 25, poll_frequency=0.25)

url = "https://omayo.blogspot.com/"
driver.get(url)

# Создаем объект actions и перемещаем фокус к элементу
#ActionChains(driver).move_to_element(element).perform()

#1. Дождитесь исчезновения текста
falling_text1 = ("id", "deletesuccess")
wait.until(EC.invisibility_of_element_located(falling_text1))
print("1")

#2 Дождитесь появления текста в элементе
falling_text2 = (By.ID, "delayedText")
#element = driver.find_element()
#ActionChains(driver).move_to_element(falling_text2).perform()
wait.until(EC.text_to_be_present_in_element(falling_text2, r"This text is displayed after 10 seconds of wait."))
print("2")

#3 Дождитесь состояния enabled
timer_enabled_button = ("id", "timerButton")
wait.until(EC.element_to_be_clickable(timer_enabled_button))
print("3")

#4 После клика дождитесь состояния disabled
disable_enable_button = ("id", "myBtn")
wait.until(EC.visibility_of_element_located(disable_enable_button)).click()
driver.find_element(By.XPATH, "//button[text()='Try it']").click()
wait.until(EC.element_attribute_to_include(disable_enable_button, "disabled"), "")
print("4")