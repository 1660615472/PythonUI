from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("file:///E:/BaiduNetdiskDownload/2018%E9%BB%91%E9%A9%AC%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/%E8%AF%BE%E4%BB%B6-%E4%B8%80%E6%9C%9F/%E4%B8%8A%E6%B5%B7%E9%BB%91%E9%A9%AC%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E4%B8%80%E6%9C%9F/%E5%B0%B1%E4%B8%9A%E7%8F%AD/%E7%AC%AC%E5%9B%9B%E9%98%B6%E6%AE%B5%20web%E8%87%AA%E5%8A%A8%E5%8C%96+%E7%99%BD%E7%9B%92/web%E8%87%AA%E5%8A%A8%E5%8C%96Day02/01_%E8%AF%BE%E4%BB%B6/_book/02img/%E6%B3%A8%E5%86%8CA.html")

driver.find_element_by_css_selector("#userA").send_keys("admin")

driver.find_element_by_css_selector("#passwordA").send_keys("zhang1234")

driver.find_element_by_css_selector("#telA").send_keys("166061564672")

sleep(2)
#修改文本框内容，先清除
driver.find_element_by_css_selector("#passwordA").clear()
driver.find_element_by_css_selector("#passwordA").send_keys("zhangjie70403009")

sleep(2)

driver.quit()
