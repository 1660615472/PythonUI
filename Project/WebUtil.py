from appium.webdriver import webdriver
from selenium.webdriver import *
from time import sleep
import os,traceback

#打开浏览器的方法
class Browser():
    def __init__(self):
        self.driver = None
        self.text = ''

    #打开浏览器方法
    def openBrower(self,b='gc',dr='../lib/chromedriver.exe'):
        if b=='gc':
            mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
            # 创建一个用来配置chrome属性的变量
            option = ChromeOptions()
            #让谷歌浏览器以手机模式打开
            option.add_experimental_option('mobileEmulation', mobileEmulation)
            # 关闭谷歌浏览器提示条
            option.add_argument('--disable-infobars')
            # 打开谷歌浏览器
            self.driver = Chrome(executable_path='../lib/chromedriver.exe', options=option)
            #设置隐式等待
            self.driver.implicitly_wait(30)
        elif b=='ie':
            if dr is None:
                dr ='../lib/chromedriver.exe'
                #打开IE
            self.driver = Ie(executable_path='../lib/IEDriverServer')
        elif b=='ff':
            if dr is None:
                dr = '../lib/chromedriver.exe'
                #打开火狐
            self.driver = Ie(executable_path='../lib/geckdriver.exe')

     #输入打开域名方法
    def get(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            #抛出异常
            print(str(traceback.format_exc()))

    #通过Xpath操作元素方法
    def inputByXpath(self,xpath,value):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(str(value))
        except Exception as e:
            # 抛出异常
            print(str(traceback.format_exc()))

    #通过Xpath单击某个元素
    def clickByXpath(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            # 抛出异常
            print(str(traceback.format_exc()))


    #强制等待方法
    def waitTime(self,time):
        sleep(time)

    #获取元素文本
    def getText(self,xpath):
        try:
            self.text = self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            # 抛出异常
            print(str(traceback.format_exc()))


    #关闭浏览器
    def quit(self):
        self.driver.quit()


