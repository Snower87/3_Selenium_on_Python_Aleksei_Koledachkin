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

driver.get("https://demoqa.com/upload-download")

# Записываем поле ввода в переменную
upload_file_button = driver.find_element(By.XPATH, "//input[@id='uploadFile']")
# Загружаем картинку
file_path = os.path.join(os.getcwd(), "!!!Антресоли 4.PNG")
upload_file_button.send_keys(file_path)
# Скачиваем картинку
download_button = driver.find_element(By.XPATH, "//a[@id='downloadButton']")
download_button.click()

time.sleep(5)