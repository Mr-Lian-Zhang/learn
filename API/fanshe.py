#coding:utf-8

#！！！反射！！！
class GetData:
    Cookie="小郭"
if __name__=='__main__':
    print(GetData.Cookie)
    setattr(GetData,'Cookie','小黄')#可以直接把类里面的属性值做修改
    print(hasattr(GetData,'Cookie'))#判断是否有这个属性值
    print(getattr(GetData,'Cookie'))#输出打印这个属性
    delattr(GetData,'Cookie')#删除这个属性
#面试题：在做单元测试时 如果第二条用例需要用到第一条用例的返回结果你要怎么做？ 例如 cookie
#方法1.可以把cookie作为全局变量
#方法2.使用反射setattr这种方法