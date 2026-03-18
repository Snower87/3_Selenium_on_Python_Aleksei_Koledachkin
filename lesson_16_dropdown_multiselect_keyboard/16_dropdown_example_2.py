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
time.sleep(2)

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
time.sleep(2)

# Перебираем все значения в выпадающем списке
all_options = DROPDOWN.options

# Способ №1 - перебор по значению
"""
for option in all_options:
    time.sleep(3)
    #if "Option 1" in option.text:
    #    print("Option 1 - присутствует")
    # Выбор элементов и подставление в select
    DROPDOWN.select_by_visible_text(option.text)
"""

# Способ №2 - перебор по индексу
"""
for option in all_options:
    time.sleep(3)
    DROPDOWN.select_by_index(all_options.index(option))
"""

# Способ №3 - перебор по значению
for option in all_options:
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value"))