from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("file:///E:/BaiduNetdiskDownload/2018%E9%BB%91%E9%A9%AC%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/%E8%AF%BE%E4%BB%B6-%E4%B8%80%E6%9C%9F/%E4%B8%8A%E6%B5%B7%E9%BB%91%E9%A9%AC%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E4%B8%80%E6%9C%9F/%E5%B0%B1%E4%B8%9A%E7%8F%AD/%E7%AC%AC%E5%9B%9B%E9%98%B6%E6%AE%B5%20web%E8%87%AA%E5%8A%A8%E5%8C%96+%E7%99%BD%E7%9B%92/web%E8%87%AA%E5%8A%A8%E5%8C%96Day01/02_%E5%85%B6%E4%BB%96%E8%B5%84%E6%96%99/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")

driver.implicitly_wait(10)

#设置cookie
str={"id":"userId","name":"testName"}
driver.add_cookie(str)

#查看cookie是否设置成功
cookies = driver.get_cookies()
print(cookies)

#获取指定cookie
cookie = driver.get_cookie("id")
print(cookie)

sleep(2)
driver.quit()