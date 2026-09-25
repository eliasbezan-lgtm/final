from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://www.dinatran.gov.py:8082/wsint3/servlet/com.wsint3.conplacanac")

time.sleep(3)

web_element = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
web_element.send_keys("AAFD154" + Keys.ENTER)

time.sleep(120)