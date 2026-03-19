
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

#Локаторы
FOR_BUSINESS_BUTTON_LOCATOR = ("xpath", "//a[text()=' For Business ']")
START_FREE_BUTTON_LOCATOR = ("xpath", "//a[text()='Start a free trial']")

time.sleep(3)

driver.get("https://hyperskill.org/tracks")

print()

# Получаем дескриптор текущего окна - того, где находимся в текущий момент
print("Дескриптор текущего окна:", driver.current_window_handle)

driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
time.sleep(3)
# Все открытые вкладки и окна
#print("Все открытые вкладки и окна:", driver.window_handles)

tabs = driver.window_handles
# Переключаемся в окне по индексу на 2 вкладку
driver.switch_to.window(tabs[1])

driver.find_element(*START_FREE_BUTTON_LOCATOR).click()
time.sleep(3)