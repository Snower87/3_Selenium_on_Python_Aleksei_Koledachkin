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
INPUT_IFRAME = ("xpath","//input[@type='text']")
REGISTER_LINK = ("xpath","//a[text()='Register']")
IFRAME_LOCATOR = ("xpath","//iframe")

# 2.Переход на страницу
driver.get("https://demo.automationtesting.in/Frames.html")

# После работы и нажатия на странице iframe - контекст/управление передается на нее
# Чтобы переключиться на обычную/сандартную страницу - надо вызвать switch_to.default_content

# Вариант 1 - переход на фрейм по его названию:
# driver.switch_to.frame("SingleFrame")
# Вариант 2 - поиск фрейма через локатор
driver.switch_to.frame(*IFRAME_LOCATOR)

time.sleep(3)
driver.find_element(*INPUT_IFRAME).click()
driver.find_element(*INPUT_IFRAME).send_keys("Hello World")
time.sleep(3)

#  Чтобы переключиться на обычную/дефолтную страницу
driver.switch_to.default_content()
driver.find_element(*REGISTER_LINK).click()
time.sleep(3)