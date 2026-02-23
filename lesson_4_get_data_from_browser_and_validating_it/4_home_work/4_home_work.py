import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_home_work_4():
    # 1. Самостоятельная работа
    # 2. Инициализировать драйвер (любой, попробуйте Firefox) p.s: не забудьте его установить.
    # 2.1 Создаем объект сервис, который отвечает за открытие/закрытие браузера
    service = Service(executable_path=ChromeDriverManager().install())
    # 2.2 Прокидываем его в качестве init-аргумента в наш Хром
    driver = webdriver.Chrome(service=service)

    # 3. Открыть любую страницу, например: vk.com.
    driver.get("https://vk.com/")

    # 4. Получить и вывести title в консоль.
    PAGE_TITLE_VK = driver.title
    print('Title страницы:', PAGE_TITLE_VK)

    # 5. Открыть любую другую страницу, например: ya.ru.
    #driver.get("https://yandex.ru/")
    driver.get("https://ya.ru/")

    # 6. Получить и вывести title в консоль.
    PAGE_TITLE_YA = driver.title
    print('Title страницы:', PAGE_TITLE_YA)

    # 7. Вернуться назад и, используя assert, убедиться, что вы точно вернулись обратно.
    logo = (By.XPATH, "//div[contains(@class,'dzen-layout--desktop-base-header__logoContainer-pu')]")
    #driver.find_element(By.XPATH, "//div[contains(@class,'dzen-layout--desktop-base-header__logoContainer-pu')]").click()
    driver.back()

    assert driver.title == PAGE_TITLE_VK

    # 8. Сделать рефреш страницы.
    driver.refresh()

    # 9. Получить и вывести URL-адрес текущей страницы.
    print("9. URL-адрес текущей страницы:", driver.current_url)

    # 10. Вернуться "вперед" на страницу из пункта 5.
    driver.forward()
    time.sleep(10)

    # 11. Убедиться, что URL-адрес изменился.
    #assert driver.current_url == PAGE_TITLE_YA - жесткое равенство
    #assert PAGE_TITLE_YA in driver.title # мягкое сравнение
    assert "ya.ru" in driver.current_url  # мягкое сравнение

test_home_work_4()