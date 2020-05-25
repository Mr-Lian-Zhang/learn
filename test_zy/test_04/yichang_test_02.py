#异常处理error    /调试（类与对象的时候讲）
import os
# #1）处理某个错误，例FileExistsError/ 2）处理某种类型的错误例：OSErroe/ 3）有错就抓except：
# try:#警察
#    os.mkdir("python_01")#FileExistsError:嫌疑人
# except FileExistsError:#警力出动 OSErroe(层级父类)/Exception所有异常的基类
#     print("等待进一步处理！")
#
##处理措施
##1.try ..except
# try:
#     os.mkdir("python_01")
# except Exception as e:
#     print("等待进一步处理")
#     print("出现的错误是{0}".format(e))
#     file=open("error.txt","a+",encoding="utf-8")
#     file.write(str(e))
#     file.close()#关闭文件
# print("hello,world!")
#
#2.try .. except ..finally
# try:
#     os.mkdir("python_01")
# except Exception as e:
#     print("等待进一步处理")
#     print("出现的错误是{0}".format(e))
#     file=open("error.txt","a+",encoding="utf-8")
#     file.write(str(e))
#     file.close()#关闭文件
# finally:#犯不犯错，下面的代码都是要执行的
#  print("hello,world!")
#
#3.try .. except ..else
# try:
#     os.mkdir("python_01")
# except Exception as e:
#     print("等待进一步处理")
#     print("出现的错误是{0}".format(e))
#     file=open("error.txt","a+",encoding="utf-8")
#     file.write(str(e))
#     file.close()#关闭文件
# else:#跟try下面的代码是一起是，如果有错误下面的代码就不会执行
#  print("hello,world!")
#

