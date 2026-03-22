import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.options import Options

from scrolls import Scrolls

# 1. Создаем объект options
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
actions = ActionChains(driver)
scrolls = Scrolls(driver, actions)


driver.get("https://useragents.ru/stable.html?ysclid=mn188urmnb488638371")
time.sleep(2)

EXAMPLE2_LOCATOR = ("xpath", "//h2[text()='Opera']")
EX2 = driver.find_element(*EXAMPLE2_LOCATOR)

# Скролл до элемента + 700 пикселей вниз от него
scrolls.scroll_to_element(EX2)

time.sleep(3)
