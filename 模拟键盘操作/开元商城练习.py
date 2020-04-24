from selenium import webdriver
from time import sleep
#鼠标API
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("http://112.74.191.10:8000/Home/user/login.html")

driver.maximize_window()
driver.implicitly_wait(10)
sleep(2)
driver.find_element_by_css_selector("#username").send_keys("13800138006")
sleep(2)
driver.find_element_by_css_selector("#password").send_keys("123456")
sleep(2)
driver.find_element_by_css_selector("#verify_code").send_keys("1234")
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/div/div[6]/a").click()
sleep(2)
driver.find_element_by_link_text("首页").click()
sleep(5)
driver.find_element_by_css_selector(".dt > a").click()
#鼠标悬停
#ActionChains(driver).move_to_element(driver.find_element_by_link_text("手机通讯")).perform()
