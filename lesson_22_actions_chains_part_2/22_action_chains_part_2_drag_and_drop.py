import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("https://the-internet.herokuapp.com/drag_and_drop")
time.sleep(3)

OBJECT_A = ("id", "column-a")
OBJECT_B = ("id", "column-b")

A = driver.find_element(*OBJECT_A)
B = driver.find_element(*OBJECT_B)

# drag_and_drop принимает в себя 2 элемента (объекта): A -> to B
action.drag_and_drop(A, B).perform()
time.sleep(5)