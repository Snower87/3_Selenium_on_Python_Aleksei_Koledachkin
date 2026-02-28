import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 0. Создаем объект options
chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager" # "eager", "normal"
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1100,1080") # если задаем размер через опции, то изначально окно открывается в том размере, который указываем
chrome_options.add_argument("--disable-cache")
# 1. Создаем объект сервис, который отвечает за открытие/закрытие браузера
service = Service(executable_path=ChromeDriverManager().install())
# 2. Прокидываем его в качестве init-аргумента в наш Хром
driver = webdriver.Chrome(service=service, options=chrome_options)

#driver.maximize_window()

#Cуществует три типа стратегии загрузки:
# normal - используется по дефолту и ожидает загрузки всех ресурсов (картинки, js-код, шрифты и т.д) на странице.
# eager - ожидает только готовности загрузки DOM (html-структуры), но при этом картинки и прочее может до сих пор грузиться.
# none - Вообще ничего не ждет, не знаю зачем это придумали ахха

time_start = time.time()

driver.get("https://whatismyipaddress.com/")
time_end = time.time()
print(time_end - time_start)

driver.quit()