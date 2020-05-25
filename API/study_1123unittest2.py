#-*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
from API.study_1123unittest1 import TestMathMethod
suite=unittest.TestSuite()
#如何添加用例
#第一种方法 加方法名
# suite.addTest(TestMathMethod('test_add_two_positive'))
# runner=unittest.TextTestRunner()
# runner.run(suite)
#第二种方法：使用TestLoader()  创建一个加载器
# loader=unittest.TestLoader()#创建一个加载器
# suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))#类名以下的全执行
# runner=unittest.TextTestRunner()
# runner.run(suite)
#第三种方法：从模块里面来加载测试用例
loader=unittest.TestLoader()
from API import study_1123unittest1
suite.addTest(loader.loadTestsFromModule(study_1123unittest1))

# with open("test.txt","w+",encoding='UTF-8') as file:#上下文管理器可以关闭文件
# #     runner=unittest.TextTestRunner(stream=file,verbosity=2)
# #     runner.run(suite)
with open("test_report.html",'wb') as fail:
    runner=HTMLTestRunner.HTMLTestRunner(stream=fail,
                                         verbosity=2,
                                         title="第一模块测试报告",
                                         description="此报告可查看所暴露的问题")
    runner.run(suite)