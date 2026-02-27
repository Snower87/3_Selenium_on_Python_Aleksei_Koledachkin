from selenium.webdriver.common.by import By

HEADER = ""

BUTTON_SIGN_IN = "//span[contains(normalize-space(.), 'Sign')]"
BUTTON_START_FOR_FREE = "//button//span[contains(normalize-space(.), 'Start')]"
BUTTON_START_FOR_FREE2 = (By.XPATH, "//button//span[contains(normalize-space(.), 'Start')]")

LINK_PRICING_TEXT = (By.LINK_TEXT, "Pricing")
LINK_FOR_BUSINESS_TEXT = (By.LINK_TEXT, "For Business")