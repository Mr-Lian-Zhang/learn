#!/usr/bin/python
# -*- coding: UTF-8 -*-
#cookie处理的三种方法
1.设置全局变量
global cookie

COOKIE=None
if COOKIE=res.cookie:
    COOKIE=res.cookie
缺点：关联性比较强

2.使用反射
class GetData:
    cookie='志勇'
setattr(GetData,'cookie','秀娟')#可以直接把类里面的属性更改
print(hasattr(GetData,'cookie'))#判断是否有这个属性值
delattr(GetData,'cookie')#删除在各个属性值

3.setup 再次请求一次用例