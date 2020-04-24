from appium.webdriver import webdriver
from selenium.webdriver import *
import time
from Project.WebUtil import Browser

driver = Browser()
driver.openBrower('gc')
driver.get('http://www.wsypshop.com/app/index.php?i=2&c=entry&m=ewei_shopv2&do=mobile&mid=2497')


#登录页面
def login(driver):
    driver.waitTime(2)
    driver.inputByXpath("//input[@class='logininput mobile']",'16606154672')
    driver.waitTime(2)
    driver.inputByXpath("//input[@class='logininput vcode']",'12345')
    driver.waitTime(2)
    driver.clickByXpath("//div[@class='loginbtn']")


def closeBrower(driver):
    driver.quite()
