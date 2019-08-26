from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('https://www.google.com')
driver.find_element_by_name('q').send_keys("Yuhang")
#driver.find_element_by_name('q').send_keys(Keys.ENTER)
p1=driver.find_element_by_name('q').submit()

driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a[1]/h3')



time.sleep(3)


driver.execute_script("window.open('about:blank', 'tab2');")
handles = driver.window_handles



#driver.switch_to_frame("frameName")
#print(handles)
#print(handles[0])
#print(handles[1])




#for handle in handles:
#    print(handle)


#driver.switch_to.window("tab2")
#driver.get()

#driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a[1]/h3').click().switch_to.window("tab2")



time.sleep(8)
driver.quit()
#driver.close()
