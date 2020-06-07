#!/usr/bin/python
# -*- coding: UTF-8 -*-
#ddt框架的使用
#装饰器：会在你的函数运行之前运行
from ddt import ddt,data,unpack
import unittest
test_data=[1,3]
@ddt#只能用来装饰测试类
class TestMath(unittest.TestCase):
    @data(*test_data)#装饰测试方法，拿到几个数据，就执行几条用例
    def test_print_data(self,itme):
        print(itme)