import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

KEYBOARD_INPUT = ("xpath", "//input[@id='target']")

driver.get("http://the-internet.herokuapp.com/key_presses") # Страница для работы
time.sleep(2)

driver.find_element(*KEYBOARD_INPUT).send_keys("Строка: АБРА_КАДАБРА-Дзинь!") # посылаем строку
time.sleep(2)

driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.CONTROL + "a") # Control + 'A'
time.sleep(2)

driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.BACKSPACE) # BACKSPACE - удаление
time.sleep(2)

driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.ENTER) # Enter
time.sleep(2)