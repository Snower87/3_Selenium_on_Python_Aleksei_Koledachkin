import time

from selenium import webdriver
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

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")

driver.get("http://the-internet.herokuapp.com/dropdown") # Страница для работы
time.sleep(5)

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
time.sleep(3)
# Вариант 1 - выбор по визуальному тексту
#DROPDOWN.select_by_visible_text("Option 1")
# Вариант 2 - выбор по значению
time.sleep(3)
DROPDOWN.select_by_value("1")
# Вариант 3 - выбор по индексу
time.sleep(3)
DROPDOWN.select_by_index(2)
time.sleep(3)
