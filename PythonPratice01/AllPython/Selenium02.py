from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()


#driver.delete_all_cookies()
#driver.add_cookie({"test":"OAO"})

cookie={'name':'mytest','value':'myvalue'}
print(type(cookie))
#cookie={'domain': '.facebook.com', 'httpOnly': False, 'name': '_js_reg_fb_gate', 'path': '/', 'secure': True, 'value': 'https%3A%2F%2Fwww.facebook.com%2F'}, {'domain': '.facebook.com', 'expiry': 1552794815.960536, 'httpOnly': True, 'name': 'fr', 'path': '/', 'secure': True, 'value': '1DzftIVyh2zJ1xQw3..BcFx3X.zp.AAA.0.0.BcFx3X.AWUUYyAA'}, {'domain': '.facebook.com', 'expiry': 1608090815.960621, 'httpOnly': True, 'name': 'sb', 'path': '/', 'secure': True, 'value': '1x0XXF5Wj4dt-n5eYtr_q2zL'}, {'domain': '.facebook.com', 'expiry': 1608090816, 'httpOnly': False, 'name': '_js_datr', 'path': '/', 'secure': True, 'value': '1x0XXJJxXTKmWQ4DxIvU0EdY'}, {'domain': '.facebook.com', 'httpOnly': False, 'name': '_js_reg_fb_ref', 'path': '/', 'secure': True, 'value': 'https%3A%2F%2Fwww.facebook.com%2F'}, {'domain': '.facebook.com', 'expiry': 1545623617, 'httpOnly': False, 'name': 'wd', 'path': '/', 'secure': True, 'value': '1034x572'}
driver.delete_all_cookies()

driver.add_cookies({'name':'key-aaaaaaa', 'value':'value-bbbb'})
#driver.get('http://fb.me')
#print(driver.get_cookies())


#driver.find_element_by_name('q').send_keys("Yuhang")
#p1=driver.find_element_by_name('q').submit()

#driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a[1]/h3')



time.sleep(3)
#driver.quit()


#driver.execute_script("window.open('about:blank', 'tab2');")
#handles = driver.window_handles

