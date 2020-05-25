#file文件的读写
#file：txt，xml，html

#mode 打开文件的模式
#r w a
#r+ w+ a+
#read write append
#rb rb+ wb wb+ ab ab+ /做单元测试的时候用到
# file=open("python11.txt","r+",encoding="utf-8")
# # a=file.read()#进行完一次读取操作后，光标就到文末
# file.write('阿坤 2020/4/13')
# # print(a)
# #1.file文件open之后默认是r 只读模式 如过你要写入内容，就会报错
#2.r+可读可写 1）先写的话，从头开始覆盖写；2）读光标之后的内容，读写跟着光标走
#3.如果要写入中文，指定编码格式encoding='utf-8'/读和写尽量分开

#####################################################
# #1.w 只写 硬要去读 就会报错
# #2.w+ 可读可写 不管是w 还是w+ 如果文件存在 就直接清空再重写/如果文件不存在，则新建一个文件，然后写
# file=open("python12.txt","w+",encoding="utf-8")
# file.write("哈哈哈，今天是充实的一天！")
#拓展：怎么移动光标？（自行学习）

#######################################################
#1.a 追加 a+（推荐）
#2.如果文件存在 就直接追加写在后面;如果文件不存在，则新建一个文件进行结果写入
# file=open("python13.txt","a+",encoding="utf-8")
# file.write("\n今天是愉快的一天")#加转义符\n 可进行换行写

###############***************##################
# #*重点掌握'r','a'
# file=open('python13.txt','r',encoding='utf-8')
# # print(file.read())#读取所有内容
# # print(file.readline())
# # print(file.readline())#按行读取，读取两行
# print(file.readlines())#读取多行，已列表的形式展示

file_01=open('python13.txt','a',encoding='utf-8')
file_01.write("hhhhhhhhh")#单行写入
file_01.writelines(["\n33333\n","4444444\n","555555"])#多行写入
#也可用绝对路径
