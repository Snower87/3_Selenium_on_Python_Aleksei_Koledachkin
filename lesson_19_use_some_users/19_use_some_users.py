import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=1920,1080")
driver_1 = webdriver.Chrome(options=options)
wait = WebDriverWait(driver_1, 25, poll_frequency=0.25)

#Локаторы
LOGIN_FIELD = ("xpath", "//input[@type='email']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

driver_1.get("https://hyperskill.org/login")

wait.until(EC.element_to_be_clickable(LOGIN_FIELD))
driver_1.find_element(*LOGIN_FIELD).send_keys("aleksey@ya.ru")

wait.until(EC.element_to_be_clickable(PASSWORD_FIELD))
driver_1.find_element(*PASSWORD_FIELD).send_keys("pass123123")

time.sleep(3)
wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON))
driver_1.find_element(*SUBMIT_BUTTON).click()

# Чтобы протестировать вторым/другим пользователем, никаких switch.to() создавать не надо
# А НАДО СОЗДАТЬ ВТОРОЙ экземпляр драйвера!!!

# Второй пользователь
driver_2 = webdriver.Chrome(options=options)
driver_2.get("https://hyperskill.org/login")
time.sleep(3)
