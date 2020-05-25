#coding:utf-8
#什么是ddt？-它是依赖unittest来进行数据处理的第三方库
#什么是装饰器？-它会在你函数运行之前运行
from ddt import ddt,data,unpack
import unittest
test_data=(1,2,3)
@ddt#用来装饰测试类
class TestMath(unittest.TestCase):
    @data(test_data)#用来装饰测试方法 拿到几个数据 就执行几条用例
    @unpack#如果unpack后的参数少于五个  推荐用unpack但要注意用变量去接受
           #如果你要对字典进行unpack的话参数名要对字典key对应
    def test_print_data(self,haha):
        print(haha)
