from selenium import webdriver

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get('https://www.baidu.com')
input = driver.find_element_by_id('kw')
input.send_keys('jtahstu')
button = driver.find_element_by_xpath('//*[@id="su"]')
print(button.get_attribute("value"))
button.click()