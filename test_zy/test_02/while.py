#while 控制循环
#语法：
#while 条件表达式：#逻辑 成员 比较 空数据 布尔值
     #代码块
#执行规律：首先判断while后面的条件表达式是否成立
#如果为true，那就执行代码块，执行完毕后，继续判断
#如果为flase，不进入内部执行代码块
#防止代码进入死循环，加一个变量来控制循环次数
#利用break和continue进行控制循环

# #利用whlie循环，实现1-100的整数相加
# a = 1
# sum = 0
# while a <=100:
#     sum += a
#     a = a+1
# print("运行了{0}次，1-100的和为{1}".format(a,sum))

#break & continue
a = 1
sum = 0
while a>0:
    sum+=a
    a+=1
    if a > 100:
        break
    else:
        continue
print("运行了{0}次，1-100的和为{1}".format(a,sum))