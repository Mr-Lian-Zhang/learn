#python 类的语法
#class 类名： #类名的规范：数字字母下划线组成，不能以数字开头，首字母大写，驼峰命名
  #类属性            #类里面的变量值
  #类方法             #写在类里面的类方法
##############################调用  ##########################################
#调用的方法：实例方法self，类方法@classmethod，静态方法@staticmethod 属性只能用实例来调用
#区别：
# 1.实例方法可以调用类属性：self.属性名
# 2.类方法和静态方法不可以调用类里面的属性，如果需要参数，需要另外传递
#备注：一般调用使用的实例方法，当调用函数与其他函数或者类属性没有关系时，可以定义为类方法和静态方法
#
# class Fdk:
#     heigit = 175
#     weight = 125
#     money = "8000"
#     def cooking(self):#self相当于实例本身，固定的占坑符
#         print("男朋友要会做饭")
#     def earn(self):
#         print("月薪是8000")
# #实例/对象 ，具体的一个例子：类名（）
# dk = Fdk()#创建实例
# print(dk)
# print(dk.money)#调用类属性 实例.属性名
# dk.cooking()#调用类方法 实例.方法名()
#*************
# Fdk().cooking()#直接调用类方法
#
######################强化################################
class Fdk:
    heigit = 175
    weight = 125
    money = "8000"
    def cooking(self):#self实例本身，固定的占坑符
        print("男朋友要会做饭")
    def earn(self):
        print(self.money,"月薪是8000")
    @classmethod#类方法
    def aihao(cls):#cls类本身
        print("喜欢电子产品")
    @staticmethod#静态方法
    def zilu():
        print("卸载游戏")
    @staticmethod
    def sum(a,b):
        print(a+b)
#实例方法
x = Fdk()
x.earn()
#调用类方法@classmethod
Fdk.aihao()
#静态方法@staticmethod，可以传参数
Fdk.zilu()
Fdk.sum(1,2)

# #初始化函数__init__(self),常用
# class dk:
#     def __init__(self,name,sg,tz):
#         self.name=name
#         self.sg=sg
#         self.tz=tz
#     def cooking(self):#self实例本身，固定的占坑符
#         print(self.name,self.sg,self.tz,"男朋友要会做饭")
#     def earn(self):
#         self.cooking()#函数之间的相互调用
#         print("月薪是8000")
#     def aihao(self):
#         print(self.name,self.sg,self.tz,"喜欢电子产品")
# o = dk("kk","172","120")
# o1 = dk("ss","162","99")
# o.cooking()
# o1.aihao()
# o.earn()

###################work#######################
#创建一个名为user的类，其中包含属性first_name和last_name，还要用户简介通常储存的其他几个属性。
#在类user中定义一个名为describe_user的方法，它打印用户信息的摘要，再定义一个名为greet_user（）方法，它
#向用户发出个性化的问候，创建多个表示不同用户的实例，并对每个实例都调用上述两个方法
# class user:
#     def __init__(self,first_name,last_name,age,sex):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#         self.sex=sex
#     def describe_user(self):
#         print("姓名：{0}{1}，年龄：{2}，性别:{3}".format(self.first_name,self.last_name,self.age,self.sex))
#     def greet_user(self,count):
#         self.describe_user()
#         print("早上好呀，{0}{1}，".format(self.first_name,self.last_name),count)
# a1 = user("小","黄","20","男")
# a1.greet_user("今天是晴天！")
# a2 = user("小","绿","20","女")
# a2.greet_user("今天真是美好的一天！")

user("小","绿","20","女").describe_user()
#如果类里面有初始化函数，创建实例的时候，就必须在实例传递对应个数参数
###################################################################################################


