#库的安装以及模块的引用
#库的安装a or b
#a:在线安装
#1.pip install 模块名
#2.使用国内源去进行安装，pip install 国内源地址 模块名
#3，file-setting-project interpreter- +（manage repositories添加地址，可添加国内源地址）
#b.离线安装
#下载离线安装包，cmd键入安装安装包路径 python setup.py install
#文件安装到了lib，lib——stepackagei
#
#怎么引用
#1.自己写的 怎么导入（平级目录）
#1）import
# import test_02.function_01
# test_02.function_01.sum(1,101)
#2）from...import
# from test_02 import function_01
# function_01.sum(1,101)
# from test_02.function_01 import sum
# sum(1,101)
#同时引用多个方法
from test_02.function_01 import *
sum(1,101)
sub(100,1)

#2：python自带的，或者是后面安装的第三方库，怎么引用（比1简单）
#1）import  2）from...import
#1）调用寻找顺序：平级目录-lib-stepackagei
# import email.mime.python_math
# #一层一层的剥开
# #引用里面的方法
# email.mime.python_math.add(1,11)
#2）(推荐使用)import后必须要具体到模块，也可直接引用到模块中的方法
# from email.mime import python_math
# python_math.add(1,100)