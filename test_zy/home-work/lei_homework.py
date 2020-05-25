# #1.创建一个名为user的类，其中包含属性first_name和last_name，还要用户简介通常储存的其他几个属性。
# #在类user中定义一个名为describe_user的方法，它打印用户信息的摘要，再定义一个名为greet_user（）方法，它
# #向用户发出个性化的问候，创建多个表示不同用户的实例，并对每个实例都调用上述两个方法
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
#
# #2.定义一个学生类
# #有下面的类属性：1.姓名，2.年龄，3.成绩（语数英）（每科成绩的类型为整数），均放在初始化函数里面
# #获取学生的姓名：get_name(),返回类型：str/获取学生的年龄：get_age(),返回类型int
# #返回三门科目中最高的分数：get_course(),返回类型int
# #1.成绩为列表
# class student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#     def get_name(self):
#         return str(self.name)
#     def get_age(self):
#         return int(self.age)
#     def get_course(self):
#         return int(max(self.grade))
# x=student("阿坤",18,[99,145,30])
# print(x.get_name())
# print(x.get_age())
# print(x.get_course())

# #2.成绩为字典
# #1）第一种方法
# class student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         a=grade
#         list=[a["语文"],a["数学"],a["英语"]]
#         self.grade=list
#     def get_name(self):
#         return str(self.name)
#     def get_age(self):
#         return int(self.age)
#     def get_course(self):
#         return int(max(self.grade))
# x=student("阿坤",18,{"语文":99,"数学":145,"英语":30})
# print(x.get_name())
# print(x.get_age())
# print(x.get_course())
# #3.按照以下要求定义一个游乐园门票类，并创建实例调用函数，
# #完成儿童和大人的总票价统计（人数不定，由你输入的人数个数来决定）
# #平日票价100元
# #周末票价为平日票价的120%
# #儿童半价
# class menpiao:
#     def __init__(self,jiage=100):
#         self.jiage=jiage
#     def goumai(self):
#         a=int(input("购买时间1-5代表周一到周五，6-7代表周六到周日："))
#         b=int(input("大人数："))
#         c=int(input("小孩数："))
#         if a in range(1,6):
#             total=b*self.jiage+c*self.jiage*0.5
#         elif a in range(6,8):
#             total=b*self.jiage*1.2+c*self.jiage*1.2*0.5
#         else:
#             print("操作错误！")
#         return total
# b=str(menpiao().goumai())
# print("您需要支付"+b)

#4.人和机器猜拳游戏写成一个类，有如下几个函数#视频26
#函数1：选择角色：1曹操2张飞3刘备
#函数2：角色猜拳1剪刀，2石头，3布，玩家输入一个1-3的数字
#函数3：电脑出拳，随机产生一个1-3的数字，提示电脑出拳结果
#函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果，...赢...输，然后提示用户是否继续？按y继续，按n退出
#最后结束的时候输出结果，角色赢几局，电脑赢几局，平局几次，游戏结束
import random
class Game:
    role_dict={1:"曹操",2:"张飞",3:"刘备"}
    fist_dict={1:"剪刀",2:"石头",3:"布"}
    def get_role_name(self):#选择角色
        role_num=input("请输入你要选择的角色1:曹操,2:张飞,3:刘备")
        return self.role_dict[int(role_num)]
    def get_role_fist(self):#角色出拳
        fist_num=input('请出拳：1:"剪刀",2:"石头",3:"布"')
        return int(fist_num)
    def get_computer_fist(self):
        fist_num=random.randint(1,3)
        #print("电脑出拳{0}".format(fist_num))
        return int(fist_num)
    def play_games(self):
        role_win=0#记录人赢了
        cp_win=0#记录电脑赢了
        draw=0#平局
        role_name=self.get_role_name()#变量存储角色名
        while True:
            role_fist=self.get_role_fist()#角色出拳
            computer_fist=self.get_computer_fist()#机器出拳
            print(role_name + "角色出拳为{0}，电脑出拳{1}".format(self.fist_dict[role_fist],self.fist_dict[computer_fist]))
            if role_fist-computer_fist==1or role_fist-computer_fist==-2:
                role_win+=1
                print("角色赢了！")
            elif role_fist-computer_fist==-1or role_fist-computer_fist==2:
                cp_win+=1
                print("电脑赢了！")
            elif role_fist-computer_fist==0:
                draw+=1
                print("平局！")
            choose=input("你是否要继续？（y:继续，n：退出）：")
            if choose=="n":
                break
        print("{0}赢了{1}局，电脑赢了{2}局，平局{3}局".format(role_name,role_win,cp_win,draw))
if __name__ == '__main__':#测试代码，检测运行/主程序的执行入口，只有在当前模块下执行的时候，才会执行下面的代码
   Game().play_games()







