import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from page_urls import *

# Урок 7. Самостоятельная работа

# 1. Создать файл locators.py
# 2. Записать все xpath-локаторы, для всех элементов на странице https://hyperskill.org/tracks в формате кортежей:
# Пример:
    # Header
    #LOGO = ("xpath", "//a[@class='xxx']")
    # Body
    #ALL_TRACKs_TAB = ("xpath", "//button[@id='xxx']")
# 3. Обязательно проверить, что все локаторы валидные, т.е элемент по ним находится.

def click_by_locator(locator):
    time.sleep(2)
    element = driver.find_element(*locator)
    element.click()

def back_page():
    time.sleep(2)
    driver.back()

def check_page_url(check_url):
    print(driver.current_url)
    print(check_url)
    if len_open_tabs():
        driver.switch_to.window(driver.window_handles[-1])
        assert driver.current_url == check_url
    else:
        assert driver.current_url == check_url

def len_open_tabs():
    tabs = driver.window_handles
    return len(tabs)


#==============================================================================
# 1. Создаем объект сервис, который отвечает за открытие/закрытие браузера
service = Service(executable_path=ChromeDriverManager().install())
# 2. Прокидываем его в качестве init-аргумента в наш Хром
driver = webdriver.Chrome(service=service)
# 3. Переходим на страницу Яндекса и ждем 10 сек
url = "https://hyperskill.org/courses"
driver.get(url)

# Ждем прогрузки страницы (ожидание, что document.readyState == 'complete')
WebDriverWait(driver, 10).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

driver.maximize_window()
time.sleep(5)

#driver.find_element("xpath", BUTTON_START_FOR_FREE).click()
# 1.1 Нажимаем на кнопку 'Sign in' и возвращаемся обратно
button_sign_in = driver.find_element(By.XPATH, BUTTON_SIGN_IN)
button_sign_in.click()
time.sleep(2)
assert sign_url == driver.current_url
driver.back()
# 1.2 Проверяем адрес возврата url-страницы: "https://hyperskill.org/courses"
assert url == driver.current_url

# 2.1 Нажимаем на кнопку 'Start for free' и возвращаемся обратно
# button_start_for_free = driver.find_element("xpath", BUTTON_START_FOR_FREE) - Вариант 1 (традиционный)
#button_start_for_free = driver.find_element(*BUTTON_START_FOR_FREE2) # Вариант 2 (через распаковку кортежа, падает - не успевает прогрузиться)

# Вариант 3
# Ждем видимости и доступности элемента (до 10 секунд)
button_start_for_free = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(BUTTON_START_FOR_FREE2)  # видим и доступен
)

button_start_for_free.click()
time.sleep(2)
assert start_for_free == driver.current_url
driver.back()
# 2.2 Проверяем адрес возврата url-страницы: "https://hyperskill.org/courses"
assert url == driver.current_url

# 3. Проверка пеехода 'pricing'
click_by_locator(LINK_PRICING_TEXT)
check_page_url(url_pricing_page)
back_page()

# 4. Проверка пеехода 'for business'
click_by_locator(LINK_FOR_BUSINESS_TEXT)
check_page_url(url_for_organization)
back_page()

time.sleep(2)

