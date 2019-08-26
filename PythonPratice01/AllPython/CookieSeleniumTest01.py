from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://hidemyna.me/en/proxy-list')
time.sleep(5)
#driver.get('https://hidemyna.me/en/proxy-list')
#time.sleep(5)
#print(driver.get_cookies())

urlcookie=""
for i in driver.get_cookies():
    urlcookie+=i['name']+"="+i['value']+";"

print(urlcookie)

#time.sleep(10)
driver.quit()
