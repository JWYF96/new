from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://www.apple.com/hk-zh/shop/buy-iphone/iphone-13-pro")

elem = driver.find_element(By.CSS_SELECTOR, ".SuggestionSearch-input")
#elem.clear()
#elem.send_keys("chair")
#elem.send_keys(Keys.RETURN)
#while True:

driver.find_element(By.CSS_SELECTOR, 'input[value="6_1inch"]').click()
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR, 'input[value="sierrablue"]').click()
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR, 'input[value="128GB"]').click()
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR, 'input["noTradeIn"]').click()
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, 'input[value="add-to-cart"]').click()

