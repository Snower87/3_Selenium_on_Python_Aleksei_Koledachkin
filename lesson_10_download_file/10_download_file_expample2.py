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

driver.get("https://the-internet.herokuapp.com/upload")

chose_file = driver.find_element(By.ID, "file-upload")
file_path = f"{os.getcwd()}/!!!Антресоли 4.PNG"
chose_file.send_keys(file_path)
time.sleep(3)

upload_file = driver.find_element(By.ID,"file-submit")
upload_file.click()
time.sleep(3)