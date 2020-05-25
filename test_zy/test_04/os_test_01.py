#相对路径/绝对路径
#Python OS模块 文件/目录方法
# import os

# #创建目录/文件夹
# os.mkdir("dengkun")
#跨级新建目录，用/代表路径的不同层级,必须保证上面的层级是存在的
#os.mkdir("dengkun/test")#相对路径  斜杠正反都行)
# os.mkdir("C:\\dk_test")#绝对路径
# #对于可能会出现转义字符的问题，例如\n，加"\"或者r，R让转义符进行失效

#删除 删除文件也是一级一级的删除的，不推荐一次性删除
# os.rmdir("dengkun/test")
# os.rmdir("dengkun")
# os.rmdir("C:/dk_test")

#课外拓展：1.文件夹下有子文件夹，是否可以强制删除2）怎么新建文件【open】，删除文件

# #获取当前路径1 具体到当前目录，目录最后一级
# path=os.getcwd()
# print("当前获取到的目录是{0}".format(path))
#获取当前路径2 获取当前文件所在的绝对路径，具体到模块名
# path=os.path.realpath(__file__) #__file__ 当前文件
# print("当前获取到的文件目录是{0}".format(path))

# #拼接路径1)
# new_path=os.getcwd()+"\\python_01"
# print("当前获取到的文件目录是{0}".format(new_path))
# os.mkdir(new_path)
#拼接路径2）join
# new_path = os.path.join(os.getcwd(),"python_01","dk_01")#或者"python_01\dk_01"（但必须保证前一级目录已经存在）
# print("当前获取到的文件目录是{0}".format(new_path))
# os.mkdir(new_path)

#判断是目录还是文件
# print(os.path.isfile(__file__))#返回布尔值
# print(os.path.isdir(os.getcwd()))

# #判断文件是否存在
# print(os.path.exists("test_dk"))

# #列出当前路径的所有的目录和文件
# print(os.listdir(os.getcwd()))

#给定一个路径，打印出路径下所有的文件夹以及文件（思路：递归函数）
#当前路径
#提示：
import os
for path in os.listdir(os.getcwd()):
    if os.path.isdir(path):
        os.listdir(os.path.join(os.getcwd(),path))
    else:
        print(os.path.join(os.getcwd(),path))

file = os.getcwd()





