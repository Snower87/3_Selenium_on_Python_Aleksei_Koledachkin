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

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# Как вы можете видеть, зона для перетаскивания появляется с задержкой, только после долгого нажатия на перетаскиваемый элемент, соответсвенно логика тут будет отличаться.
# Все по причине того, что для стандартный drag_and_drop() требует того, чтобы сразу были видны оба элемента, тот который будет перетаскиваться и место куда этот элемент будет перетянут.

# Но не беда, тут все решается через цепочку действий и уже знакомыми нам методами, но для начала опишу алгоритм словами:
# 1. Нажимаем и удерживаем кнопку на перетаскиваемом элементе с помощью метода click_and_hold().
# 2. Ждем появления зоны для перетаскивания.
# 3. Перетаскиваем на нее элемент.
# 4. Отпускаем кнопку мыши - это как раз и является нашей главной темой, так как selenium в цепочке действий работает точно как человек, ему нужно передать не только нажатие, но и отпускание кнопки в явном виде).

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)
action = ActionChains(driver)

driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")

source = driver.find_element("xpath", "//div[@class='grid__item'][7]") # Что перетаскиваем
target = driver.find_element("xpath", "//div[@class='drop-area__item'][2]") # Куда перетаскиваем

action.click_and_hold(source) \
    .pause(2) \
    .move_to_element(target) \
    .release() \
    .perform()