#导入unittest框架
import unittest

#导入测试用例，并实例化
from Unittest框架.testcases.完整的测试框架案例 import Test01
from Unittest框架.testcases.test02 import Test02
from Unittest框架.testcases.test04 import Test04
if __name__ == '__main__':
    #实例化testsuite
    suite = unittest.TestSuite()
    #调用添加用例方法 Test02类 里的test001方法
    suite.addTest(unittest.makeSuite(Test02))

    runner = unittest.TextTestRunner()
    runner.run(suite)
