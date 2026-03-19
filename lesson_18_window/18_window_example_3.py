
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# драйвер автоматически переключит наш драйвер на новую вкладку/таб
driver.switch_to.new_window("tab")
time.sleep(5)

# драйвер автоматически переключит наш драйвер на новую вкладку/таб
driver.switch_to.new_window("window")
time.sleep(5)

driver.get("https://ya.ru")
time.sleep(5)
