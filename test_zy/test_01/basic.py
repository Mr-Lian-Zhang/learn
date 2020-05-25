# a = 1
# print (a)
# b = 'hello!'
# print (type(b))#type查看字符类型
# print(len(b))#打印字符长度

# 字符串索引取值str
# s = 'happy!'
# print(s[5])
# print(s[-1])
# print(s[1:5:2])#切片：取头不取尾
# #练习题：请利用切片，倒序输出s的值
# print(s[-1:-7:-1])
#print (s[::-1])

# s = 'happy!'
# #字符串的分割格式：字符串.split（指定的字符，切割次数）
# #返回一个列表类型的数据，列表内的子元素都是字符串类型
# print(s.split('p',1))
# 字符串的替换格式： 字符串.replace(指定替换值，新值，替换次数),替换字符要用新的变量赋值
# new = s.replace('p','P',2)
# print(new)
#字符串的去除指定字符格式：字符串.strip(指定字符)，去除字符要用新的变量赋值
#1默认去除空格，2只能去除头和尾的字符
# print(len(s))
# news = s.strip('!')
# print(len(news))

# # 字符串的拼接，打印时用+号拼接
s_1 = '哇，'
s_2 = '金色传说！'
s_3 = 666 #整型拼接字符串打印时，可用str(变量)进行强制转换，也可以用逗号隔开直接输出
print(s_1+s_2+str(s_3))
# print(s_1,s_2,s_3)
# #字符串的格式输出：% format
# age = 20
# name = '憨憨'
# score = 10.0
# print('来自梁山幼儿园的'+name+'同学今年'+str(age)+'岁了！')# 普通拼接打印
# #格式化输出1：format 特点 {}符来占位置进行输出
# print('来自梁山幼儿园的{1}同学今年{0}岁了！'.format(age,name))#{}内加索引赋值，不填按顺序取值
# #格式化输出2：% %s字符串，%d数字，%f浮点数
# print ('来自梁山幼儿园的%s同学今年%d岁了，数学考了%.2f分！'%(name,age,score))#按顺序取值
# #  %s 可以填任何数据类型
# #  %d 填数字，浮点数，整型
# #  %f 浮点数，%.2f可保留小数点后两位

#*********************************拓展****************************************************************************
#print("hi".upper())#upper最大
# print("HI".lower())#lower最小
# s = str(100)
#字符类型的转换
# print(type(s))
# a = int("100")
# print(type(a))
# b = float(100)
# print(type(b))
# #整数的拆分
# n = 12345
# f = list(str(n))#进行转换拆分，list&tuple
# for aa in f:
#     print(str(aa),end="")





