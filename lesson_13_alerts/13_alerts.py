import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создание экземпляра веб-драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

def example1_alert_OK():
    # Переход на веб-страницу
    driver.get("https://demoqa.com/alerts")

    time.sleep(5)

    # Клик на кнопку, которая вызывает alert
    BUTTON_1 = ("xpath", "//button[@id='alertButton']")
    wait.until(EC.element_to_be_clickable(BUTTON_1)).click()

    # Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
    alert = wait.until(EC.alert_is_present())

    time.sleep(5)

    # Переключение на alert
    driver.switch_to.alert

    time.sleep(3)

    # Принимаем, кликаем ОК
    alert.accept()

    time.sleep(3)


def example2_alert_dismiss():
    # Переход на веб-страницу
    driver.get("https://demoqa.com/alerts")

    time.sleep(5)

    # Клик на кнопку, которая вызывает alert
    BUTTON_3 = ("xpath", "//button[@id='confirmButton']")
    wait.until(EC.element_to_be_clickable(BUTTON_3)).click()

    # Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
    alert = wait.until(EC.alert_is_present())

    time.sleep(5)

    # Переключение на alert
    driver.switch_to.alert

    time.sleep(3)

    print(alert.text) # Do you confirm action?
    # Отказываем, кликаем NO
    alert.dismiss()

    time.sleep(3)

def example3_send_keys():
    # Переход на веб-страницу
    driver.get("https://demoqa.com/alerts")

    time.sleep(5)

    # Клик на кнопку, которая вызывает alert
    BUTTON_4 = ("xpath", "//button[@id='promtButton']")
    wait.until(EC.element_to_be_clickable(BUTTON_4)).click()

    # Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
    alert = wait.until(EC.alert_is_present())

    time.sleep(5)

    # Переключение на alert
    driver.switch_to.alert

    time.sleep(3)

    alert.send_keys("Hello world")
    time.sleep(3)
    # Принимаем, кликаем OK
    alert.accept()

    time.sleep(3)

example3_send_keys()