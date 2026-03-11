import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Implicit waits - Неявные ожидания
# Неявные ожидания задаются сразу для всего проекта (при инициализации драйвера):
# - используется для обнаружения элемента на странице (появления)
# - используется для find_element(), find_elements()
# - рекомендует использовать явные ожидания
# Использовать - либо одно, либо другое!!! Не мешать явные + неявные

# Explicit waits - Явные ожидания:
# - исчезновение элемента, текста элемента, состояния и тд
# - указываем для элемента, с  которым работаем


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=0.25)

def example1():
    # неявное ожидание. Драйвер пытается достучаться до элемента (в DOM) в течении времени
    # driver.implicitly_wait(10)

    url = "https://demoqa.com/dynamic-properties"
    driver.get(url)
    time.sleep(5)

    BTN_VISIBLE_AFTER = (By.ID, "visibleAfter")
    ENABLE_IN_SECONDS = ("id", "enableAfter")
    # driver.find_element(*BTN_VISIBLE_AFTER).click()

    # возвращает WebElement
    BUTTON = wait.until(EC.visibility_of_element_located(BTN_VISIBLE_AFTER)) # - распаковывает
    BUTTON.click()

    wait.until(EC.element_to_be_clickable(ENABLE_IN_SECONDS))
    time.sleep(5)

def example2():
    url = "https://the-internet.herokuapp.com/dynamic_controls"
    driver.get(url)

    REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
    driver.find_element(*REMOVE_BUTTON) # - НЕ распаковывает, нужно распаковать самому

    wait.until(EC.visibility_of_element_located(REMOVE_BUTTON))
    print("ВСЕ ОК")

def example3():
    url = "https://the-internet.herokuapp.com/dynamic_controls"
    driver.get(url)

    ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
    TEXT_FIELD = ("xpath", "//input[@type='text']")

    # ДО
    #driver.find_element(*ENABLE_BUTTON).click()
    # ПОСЛЕ
    wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("Hello")
    time.sleep(2)
    wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, "Hello"))
    time.sleep(2)
    print("ВСЕ ОК 3")

example3()