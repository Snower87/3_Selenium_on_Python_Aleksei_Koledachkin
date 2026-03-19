
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#---------------------------------
# webdriver не видит разницы между окном и вкладкой
#---------------------------------

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://hyperskill.org/tracks")
time.sleep(5)

windows = driver.window_handles
driver.switch_to.window(windows[1])

driver.get("https://ya.ru")
time.sleep(5)