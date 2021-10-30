from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://www.price.com.hk/product.php?p=516473")

elem = driver.find_element(By.CSS_SELECTOR, ".SuggestionSearch-input")
#elem.clear()
#elem.send_keys("chair")
#elem.send_keys(Keys.RETURN)
#while True:

    quotations = driver.find_element(By.CSS_SELECTOR, ".page-product > ul > li(id)")

know_smallest_price = 99999
know_smallest_btn = None

    for quotation in quotations:
        price_elem = quotations.find_element(By.CSS_SELECTOR,".text-price-number")
        price = float(price_elem.text.replace(",","")) #1,249
        #price = float(price_elem.get_attribute('data-price')) #1249.0

        quotation_elem = quotations.find_element(By.CSS_SELECTOR,".new_referral_btn")
        #quotation_elem = quotations.find_element(By.CSS_SELECTOR,"[title="安心訂購]")

        if price < know_smallest_price:
            know_smallest_price = price
            know_smallest_btn = quotation_elem

    know_smallest_btn.click()







