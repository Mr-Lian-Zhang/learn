#coding:utf-8
#接口测试本质是测试类里面的函数
class MathMethod:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def muliy(self):
        return self.a*self.b