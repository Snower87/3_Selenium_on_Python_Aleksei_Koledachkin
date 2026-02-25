import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открываем страницу
driver.get("https://www.freeconferencecall.com/ru")
driver.maximize_window()

# Ждем 5 сек до загрузки страницы
time.sleep(2)

# Поиск нужного элемента
login_btn = driver.find_element(By.XPATH, "//a[@id='login-desktop']")
# Кликаем по кнопке 'login'
login_btn.click()

email_field = driver.find_element(By.XPATH, "//input[@id='login_email']")
email_field.send_keys("akoledachkin@ya.ru")

# Получаем атрибуты у полей: введенное значение и макс.длину
print(email_field.get_attribute("value"))
print(email_field.get_attribute("maxlength"))

# Чистим поле и вводим новое значение
time.sleep(2)
email_field.clear()
email_field.send_keys("AasdasAAAA")

print(email_field.get_attribute("value"))
print(email_field.get_attribute("maxlength"))

driver.quit()