from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("file:///E:/BaiduNetdiskDownload/2018%E9%BB%91%E9%A9%AC%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/%E8%AF%BE%E4%BB%B6-%E4%B8%80%E6%9C%9F/%E4%B8%8A%E6%B5%B7%E9%BB%91%E9%A9%AC%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E4%B8%80%E6%9C%9F/%E5%B0%B1%E4%B8%9A%E7%8F%AD/%E7%AC%AC%E5%9B%9B%E9%98%B6%E6%AE%B5%20web%E8%87%AA%E5%8A%A8%E5%8C%96+%E7%99%BD%E7%9B%92/web%E8%87%AA%E5%8A%A8%E5%8C%96Day01/02_%E5%85%B6%E4%BB%96%E8%B5%84%E6%96%99/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")

#获取文本框大小
size = driver.find_element_by_css_selector("#user").size
print("获取用户输入文本框大小为：" ,size)

#获取文本值
text = driver.find_element_by_css_selector("#fw").text
print("获取文本框的值为:",text)

#获取元素属性值
attrable = driver.find_element_by_css_selector("#fw").get_attribute("href")
print("元素的属性为:",attrable)

#获取当前浏览器title
current_title = driver.title
print("当前页面title是：",current_title)

#获取当前页面url
current_url = driver.current_url
print("当前页面url为",current_url)

#判断span元素是否显示
boolean = driver.find_element_by_css_selector("span").is_displayed()
print("span元素是否显示？",boolean)

#判断取消按钮是否可用
boolean = driver.find_element_by_css_selector("#cancel").is_enabled()
print("取消按钮是否可用？",boolean)



sleep(3)

#关闭所有
driver.quit()