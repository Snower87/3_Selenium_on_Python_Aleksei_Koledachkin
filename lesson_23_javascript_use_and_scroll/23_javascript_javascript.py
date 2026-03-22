import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://seiyria.com/bootstrap-slider/")
time.sleep(2)

# Выполнение javascript кода
driver.execute_script("alert('Hello World')") # Вызов js-кода на странице

time.sleep(3)
