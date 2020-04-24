from selenium import webdriver
import unittest
class Test01(unittest.TestCase):

    @classmethod
    def setUpClass(cls) : #该方法在脚本中先执行一次
        global driver #global 标识该变量为全局变量
        driver = webdriver.chrome()

    @classmethod
    def tearDownClass(cls) : #该方法脚本中最后执行一次
        driver.quit()

    def test1(self):
        '''打开网站'''
        print("测试1")


if __name__ == '__main__':
    unittest.main(verbosity=2)
