#单元测试
#接口测试的本质：就是测试类里面的函数，通过数据驱动
#单元测试的本质：测试函数 代码级别 通过代码级别
#单元测试的框架：unittest（标准库模块）+接口 / pytest+web可以利用到接口测试（后续）
#pytest+jenkins+allure

#功能测试
#1：写用例 TestCase(类)
#2.执行用例 1.TestSuite 存储用例 2.TestLoader 找用例，加载用例，存到1的TestSuite
#3.对比实际结果 期望结果，判断用例是否通过 #断言 Assert
#4.出具测试报告 TextTestRunner
#
import unittest
from test_07_unittest_01.math_method import MathMethod#测试的目标类
#写一个测试类，对我们自己写的math_method模块里面的类，进行单元测试
class TestMathMethod(unittest.TestCase):#继承了unittest里面的TestCase，专门用来写用例
    #编写测试用例（不成文规定）
    #1：一个用例对应一个函数 不能传参 只有self关键字
    #2.所有的用例（所有的函数，都是test开头 test_）
    def test_add_two_positive(self):#两个正数相加1+1
        res=MathMethod(1,1).add()
        print("1+1的结果是",res)
    def test_add_two_zero(self):#两个0相加 0+0
        res=MathMethod(0,0).add()
        print("0+0的结果是",res)
    def test_add_two_negative(self):#两个负数数相加-1+-2
        res=MathMethod(-1,-2).add()
        print("-1+-2的结果是",res)
if __name__ == '__main__':
    TestMathMethod().main()#执行所有的测试用例

#ASCII编码排序
#按照函数名的首字母abcdefghi......



