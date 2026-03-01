import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 0. Создаем объект options
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}/download"
}
chrome_options.add_experimental_option("prefs", prefs)
# 1. Создаем объект сервис, который отвечает за открытие/закрытие браузера
service = Service(executable_path=ChromeDriverManager().install())
# 2. Прокидываем его в качестве init-аргумента в наш Хром
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.freeconferencecall.com/ru/ru/login")

login_field = driver.find_element(By.ID, "login_email")
login_field.send_keys("selenium2@ya.ru")
print("Шаг 1")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("yayayya2)")
#time.sleep(2)
print("Шаг 2")

checkbox_field = driver.find_element(By.XPATH, "//*[text()='Запомнить меня']")
checkbox_field.click()
#time.sleep(2)
print("Шаг 3")

#time.sleep(2)
# driver.get("https: login_field= driver.find_element("xpath", " login_field.send_keys("selenium@ya.ru")
# password_field= driver.find_element("xpath", " agree checkbox = driver.find_element("xpath", " submit button driver.find_element("xpath", " driver.get("https:

button_login = driver.find_element(By.ID, "loginformsubmit")
button_login.click()

driver.get("https://www.freeconferencecall.com/profile/settings")

# Часто при нажатии на кнопку 'button' высвечивается окно с выбором файла
# и не понятно что делать. а оно делается через добавление в теге <input>
# Надо найти input соответствующий этомой кнопке и передать в input файл

upload_field = driver.find_element("xpath", "//input[@type='file']")
file_path = f"{os.getcwd()}/!!!Антресоли 4.PNG"
upload_field.send_keys(file_path)

time.sleep(3)
driver.quit()