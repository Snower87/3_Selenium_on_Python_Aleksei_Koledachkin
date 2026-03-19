import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXY_SERVER = "119.148.8.182:22122"
# Авторизация в прокси сервере через логин-пароль
PROXY = "username:password@37.19.220.129:8443"
options = Options()
options.add_argument (f"--proxy-server={PROXY_SERVER}")
driver = webdriver.Chrome()

time.sleep(1)
driver.get("http://2ip.ru")
time.sleep(5)