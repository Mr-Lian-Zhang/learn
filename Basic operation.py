#!/usr/bin/python
# -*- coding: UTF-8 -*-
#TODO 知识点1 加减乘除
print(1+1)#相加
print(1-1)#相减
print(1*1)#相乘
print(1/1)#相除 输出是浮点型
print(7//3)#整除
print(7%3)#取余数
print(2**3)#2的三次方
from decimal import Decimal #导入decimal在进行浮点型计算时可保持很精确的计算
#注意 decimal要接收字符串形式 不要数字
print(Decimal("0.00112")+Decimal("0.00113"))
#TODO 知识点2 赋值运算 += -=
surname="连"
surname+="志勇"# 原先的基础上加上 志勇
print(surname)
a=[1.2,3]
a.clear()
print(a.insert(8,1))
print(a.clear())
#TODO 知识点3 逻辑运算  and not or
#and 并且
print(1==1 and 3==3)
#or 或者
print(1==3 or 1==1)
#not 非  取反的
print(not (1==3 or 1==1))
#TODO 知识点4 成员运算 in not in
print("连" in "连志勇")
print("连" not in "连志勇")
#TODO 知识点5 if elif else
smail="给我笑一个"
if type(smail)==int:
    print("你吃饭了吗？")
elif type(smail)==float:
    print("我吃的很饱")
else:
    print("中午吃的烤鸭")
#TODO 知识点6 pass
#如果冒号后不想执行任何程序就用pass表示
if type(smail)==int:
    pass
else:
    print("我笑了啊")
#TODO 知识点7 for循环
cool=["连志勇","贺创鑫","王贺选","吴俊辉"]
for boy in cool:
    print("帅哥分别有{}".format(boy))
baby={"连晨汐":"beautifulgirl","贺韩":"beautifulgirltoo"}
for girl in baby:
    print("漂亮的女孩有{}".format(girl))#默认获取的是字典中的key
#TODO 知识点8 while循环
#while后加条件 若条件成立则一直执行
#跳出循环的两种方式 1.加break
a=2
b=4
while a+b==6:
    print("连晨汐快乐成长")
    break
#跳出循环的两种方式 2.加条件判断
c=0
while c<10:
    print("我确实长得很帅")
    c+=1
list1=[1,2,3]
list2=[7,8,9]
for v1 in list1:
    for v2 in list2:
        print("{}*{}={}".format(v1,v2,v1+v2))