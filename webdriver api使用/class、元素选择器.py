from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("file:///E:/BaiduNetdiskDownload/2018%E9%BB%91%E9%A9%AC%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/%E8%AF%BE%E4%BB%B6-%E4%B8%80%E6%9C%9F/%E4%B8%8A%E6%B5%B7%E9%BB%91%E9%A9%AC%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E4%B8%80%E6%9C%9F/%E5%B0%B1%E4%B8%9A%E7%8F%AD/%E7%AC%AC%E5%9B%9B%E9%98%B6%E6%AE%B5%20web%E8%87%AA%E5%8A%A8%E5%8C%96+%E7%99%BD%E7%9B%92/web%E8%87%AA%E5%8A%A8%E5%8C%96Day02/01_%E8%AF%BE%E4%BB%B6/_book/02img/%E6%B3%A8%E5%86%8CA.html")
#元素选择器是用标签名定位
driver.find_elements_by_css_selector("input")[0].send_keys("admin")
driver.find_elements_by_css_selector("input")[1].send_keys("zhang1234")
driver.find_elements_by_css_selector("input")[2].send_keys("16606154672")

#属性选择器
driver.find_element_by_css_selector("[type='emailA']").send_keys("15062693133@163.com")

#层级选择器，根据元素父子关系确定
driver.find_element_by_css_selector("p>input[placeholder='文本1']").send_keys("hello word")
sleep(2)

driver.quit()


