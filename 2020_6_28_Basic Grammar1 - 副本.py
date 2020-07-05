#!/usr/bin/python
# -*- coding: UTF-8 -*-

#TODO:知识点1：input 输入：让用户输入信息
name=input("你叫什么名字")
print("我叫",name)

#TODO:知识点2：变量：用来存储数据
#命名规则：
# 1.只能由数字，_,字母组成 不能由数字开头
# 2.不能命名为python的内置关键字 例如：def Ture
# 3.命名建议使用下划线：name_age或者驼峰命名：nameAge

# TODO:知识点3：字符串的要注意的问题
# 1.如果字符串内部有双引号则最外层用单引号
# 2.如果字符串内部有单引号则最外层用双引号

#TODO:知识点4：字符串的各种操作
#1.字符串的拼接：+
name="连志勇"
cool="真帅"
print(name+cool)
# 2.获取字符串的长度：len（）
myname="连志勇好帅"
print(len(myname))
# 3.获取字符串中某一个字符从左边开始数则是0 1 2 3...(获取"连")
print(myname[0])
# 4.获取字符串中某一个字符从右边开始数则是-1 -2 -3...(获取”连“）
print(myname[-5])
# 5.获取字符串中多个字符：切片 myname[start: end : step]（获取”志勇“）
    #如果是切片从左往右的话 坐标就从1开始数 想取到几 就数到几 除0之外 start值不取
    #如果步长超出则获取剩余所有的字符串
print(myname[2:4])
    #如果是切片从右往左的话 坐标就从1开始数 想取到几 就数到几 除0之外 end值不取
    #如果步长超出则获取剩余所有的字符串
print(myname[-3:-5:-1])
# 6.字符串的格式化操作：format
school=input("请输入您的学校")
grade=input("请输入您的班级")
name1=input("请输入您的名字")
subject=input("请输入您的学科")
score=input("请输入您的成绩")
print("恭喜"+"{0}{1}{2}{3}考了{4}".format(school,grade,name1,subject,score))
# 7.数据类型的转换
a="3"
b="4"
c=5
d=6
#强转换成整数型
print(int(a)*int(b))
#强转换成字符串型
print(str(c)+str(d))
# 8.字符串的大小写转换： upper lower swapcase
my_str="cool boy"
my_str1="COOL BOY"
my_str2="COOL boy"
#强转换成大写
print(my_str.upper())
#强转换成小写
print(my_str1.lower())
#大写转换成小写/小写转换成大写
print(my_str2.swapcase())
# 9.字符串的查找：find  index
my_str3="连志勇长得贼帅"
print(my_str3.find("帅"))#若找得到则返回该字符的索引值
print(my_str3.find("丑"))#若找不到则返回-1
#print(my_str3.index("丑"))#index与find类似只不过找不到时会报错
# 10.字符串的替换：replace
my_str4="连志勇帅的掉渣"
new_my_str4=my_str4.replace("渣","油",1)#变量.replace(要替换的值,替换后的新值,替换的数量)
print(new_my_str4)
# 11.字符串的统计：count
my_str5="志勇，志勇，志勇长得真帅"
print(my_str5.count("志勇"))#统计出一共包含几个志勇
# 12.字符串的拼接join
xingming="连志勇"
nianling="25岁"
waimao="长得很帅"
yigong='名叫'.join([xingming,nianling,waimao])#插在每个变量之间不包括头尾
print(yigong)
# 13.字符串的切割split
print(yigong.split("岁"))#从"岁"开始切割 打印出列表
# 14.去除字符串头尾指定字符串strip
song="吗连志勇长得帅吗"
song1="连志勇长得真帅"
print(song.strip("吗"))#头尾一样所以全部去除
print(song.lstrip("吗连"))#去除头部字符串
print(song.rstrip("帅吗"))#去除尾部字符串
print(song1.lstrip("连").rstrip("吗"))#若头尾不一样则可这也去除
# 15.判断是否是一个正整数isdigit
junhui="沙雕"
print(junhui.isdigit())

#TODO:知识点5:列表
#1.获取列表中某个元素：取对应索引值从0开始
tem=["连志勇","吴军辉","王贺选","贺创新"]
print(tem[2])#取出王贺选
#2.获取列表中多个元素：切片
print(tem[1:3])#取出吴军辉和王贺选取左不取右边
#3.获取列表的长度len
print(len(tem))
#4.添加新的元素：append
tem.append("朱秀杰")#添加到最后面
print(tem)
#5.添加多个元素：extend
tem.extend(["马海玉","韩闯"])
print(tem)
#6.在列表中固定添加位置insert（索引值,要插入的值）
tem.insert(0,"自动化")
print(tem)
#7.删除指定的值：remove
tem.remove("自动化")
print(tem)
#8.删除索引坐在的值：pop
tem.pop(6)#有返回值可提取出来 不填写索引值则删除最后一个
print(tem)
#9.删除列表中所有的元素clear
# tem.clear()
# print(tem)
#10.修改
tem[0]="帅帅的连长"
print(tem)
#11.返回元素的索引值：index
print(tem.index("帅帅的连长"))
#12.列表倒序显示：reverse
tem.reverse()
print(tem)
#13.列表的倒序显示2
tem1=tem[::-1]#需要一个新的变量取接收
print(tem1)
#14.列表的排序：sort
source=[8,4,5,89,421,45,1]
ch=["p","w","s","d","f"]
source.sort()
ch.sort()
print(source)
print(ch)