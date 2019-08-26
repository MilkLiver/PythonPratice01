from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('ftp://fileserver.fic.com.tw')
alert = driver.switch_to_alert()
time.sleep(2)
alert.accept()
print (alert.text)
