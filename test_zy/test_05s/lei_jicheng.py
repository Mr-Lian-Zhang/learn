# #继承
# class Robotone:#第一代机器人
#     def __init__(self,name,year):
#         self.name=name
#         self.year=year
#     def walking_on_ground(self):
#         print(self.name+"只能在平地上行走，有障碍物就会摔倒")
#     def robot_info(self):
#         print("{0}机器人于{1}年生产，中国制造".format(self.name,self.year))
# #继承
# class Robottwo(Robotone):#第二代机器人
#     def walking_on_ground(self):#子类的函数名与父类的函数名重复时，就叫重写
#         print(self.name+"可以平稳的在平地上行走")
#     def walking_avoid_block(self):#父类没有的函数，称为拓展
#         self.robot_info()#子类函数调用直接调用父类函数
#         print(self.name+"可以避开障碍物")
# #第二代机器人
# #继承的类，是否要用到初始化函数，看是否从父类继承的有
# #1：父类有的，继承后，子类可以直接拿过来用
# #2.分类有的函数名，子类也有，那么子类的实例就优先调用子类的函数
# r2 = Robottwo("绿绿","1998")
# r2.robot_info()
# r2.walking_on_ground()
# r2.walking_avoid_block()
#############################################################################################################
#多继承
#具有两个父类的属性和方法，如果两个父类有同样的函数名，优先调用第一个（就近原则）
class Robotone:#第一代机器人
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def walking_on_ground(self):
        print(self.name+"只能在平地上行走，有障碍物就会摔倒")
    def robot_info(self):
        print("{0}机器人于{1}年生产，中国制造".format(self.name,self.year))
#继承
class Robottwo:#第二代机器人
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def walking_on_ground(self):
        print(self.name+"可以平稳的在平地上行走")
    def walking_avoid_block(self):#
        print(self.name+"可以避开障碍物")
    def robot_info(self):
        print("{0}机器人于{1}年生产，中国制造".format(self.name, self.year))
class Robotthree(Robotone,Robottwo):
    def jump(self):
        print(self.name+"可以单膝跳跃")
r3 = Robotthree("大王","2013")
r3.jump()
r3.walking_on_ground()#具有两个父类的属性和方法，如果两个父类有同样的函数名，优先继承第一个（就近原则）
r3.walking_avoid_block()
r3.robot_info()#如果父类1和父类2初始化函数不一致时，会报错（尽量保存一致），可以进行重写