#coding:utf-8
import unittest
from API import test_task
import HTMLTestRunner
suite=unittest.TestSuite()
#通过loader方式来加载用例
loder=unittest.TestLoader()
suite.addTest(loder.loadTestsFromModule(test_task))
#执行
with open("test_task.html",'wb') as file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                         verbosity=2,
                                         title="测试课堂派登录接口结果",
                                         description="应该全部为pass")
    runner.run(suite)