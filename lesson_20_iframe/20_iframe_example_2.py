import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#------------------------------
# iframe - html-страница внутри другой страницы
#------------------------------

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 25, poll_frequency=0.25)

# 1. Локаторы
SWITCH_TO_WINDOW_TWO_IFRAMES = ("xpath", "//a[text()='Iframe with in an Iframe']")
MULTI_FRAME_LOCATOR = ("xpath", "//iframe[@src='MultipleFrames.html']")

# 2.Переход на страницу
driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(*SWITCH_TO_WINDOW_TWO_IFRAMES).click()
time.sleep(3)
driver.switch_to.frame(*MULTI_FRAME_LOCATOR)
print(driver.find_element("xpath", "//body").text) # Parent frame

# 3. Находясь в iframe переключимся на child-фрейм
driver.switch_to.frame(0)
print(driver.find_element("xpath", "//body").text) # Child frame

# 4. Возврат не в default, а на родитеслький (parent-фрейм)
driver.switch_to.parent_frame()
print(driver.find_element("xpath", "//body").text) # Parent frame

# 4. Переключение на default контент
driver.switch_to.default_content()
print(driver.find_element("xpath", "//body").text)
