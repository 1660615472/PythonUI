

#使用def定义函数
#a,b是必填参数，c选填参数
def test(a,b,c):
        """
        :param a:第一个必填
        :param b: 第二个必填
        :param c: 第三个必填
         :return:无
        """
        return (a+b)/c



d = test(1,2,3)
print(d)