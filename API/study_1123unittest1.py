#1.写用例 ：TestCase
#coding:utf-8
encoding='gb18030'
#2.执行用例：（1.TestSuite存储用例 （2.TestLoader找用例，加载用例存到TestSsuite
import unittest
from API.study_1123unittest import MathMethod  #要进行单元测试的目标类
class TestMathMethod(unittest.TestCase):#规定：一个用例就是一个函数不能传参
    def test_add_two_positive(self):
        res=MathMethod(1,1).add()
        print("1+1的结果是",res)
        try:
            self.assertEqual(2,res)#添加断言：第一个参数为期望值 第二个参数为实际值
        except AssertionError as w:
            print("出错了，断言错误是{0}".format(w))
            raise w

    def test_add_positive(self):
        res=MathMethod(-1,-2).add()
        print("-1+-2的结果是",res)
        try:
            self.assertEqual(-3,res)
        except AssertionError as w:
            print("出错了，断言错误是{0}".format(w))
            raise w
    def test_positive(self):
        qws=MathMethod(-1,-2).muliy()
        print("-1*-2的结果是",qws)
        try:
            self.assertEqual(-3,qws)
        except AssertionError as w:
            print("出错了，断言错误是{0}".format(w))
            raise w
    def test_wpositive(self):
        qws=MathMethod(9,9).muliy()
        print("9*9的结果是",qws,"数字错了 ")
        try:
            self.assertEqual(80,qws)
        except AssertionError as w:
            print("出错了，断言错误是{0}".format(w))
            raise w
if __name__=='__main__':
    unittest.main()