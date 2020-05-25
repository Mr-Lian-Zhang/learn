# #招10-12岁女足球员，性别：男x，女y。询问十次后，输出满足条件的总人数
# sum = 0
# for item in (1,2,3,4,5,6,7,8,9.10):
#     age = int(input("请问你的年龄是："))
#     sex = input("请问你的性别是：")
#     if 10<=age<=12 and sex =='y':
#         print("符合条件")
#         sum += 1
#     else:
#         print("不符合条件")
# print(sum)

# #利用for循环和range函数，完成0-100相加的和（包括0，100）
# sum = 0
# for k in range(101):
#     sum += k
# print(sum)
#
# # #利用嵌套循环生成一个直角三角形
# #1）
# a=" "
# b="*"
# for i in range(10):
#     for item in b:
#         a=item+a
#         print(a)
#1.1）
# for i in range(6):
#     for j in range(1,i+1):
#         print("*",end='')
#     print("")#换行处理
# #2）
# for i in range(11):
#     print("*"*i)

# # 2、输入num为四位数，对其按照如下的规则进行加密:
# # 1)每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# # 2)将该数的第1位和第4为互换，第二位和第三位互换
# # 3)最后合起来作为加密后的整数输出=优酷笔试题
# a =input("请输入四位整数：")
# b=""
# for item in a:
#     # print(item)
#     # print("每一位加五除以十后的值为",(int(item)+5)%10)
#     b+=str((int(item)+5)%10)
# c=b[::-1]
# print(c)
#
# #写一个程序，分别求出0-100的奇数和，偶数和
# #1）利用运算
# j_sum=0
# o_sum=0
# for item in range(0,101):
#     if item%2==0:
#         o_sum+=item
#     else:
#         j_sum+=item
# print("0-100奇数和为{0}".format(j_sum))
# print("0-100偶数和为{0}".format(o_sum))
# #2）利用步长
# a=0
# b=0
# for x in range(0,101,2):
#     a+=x
# for y in range(1,101,2):
#     b+=y
# print("0-100奇数和为{0}".format(b))
# print("0-100偶数和为{0}".format(a))

# #打印出等腰三角形
# for x in range(1,6):
#     for y in range(1,6-x):
#         print(" ",end="")
#     for b in range(1,x+1):
#         print("* ",end="")
#     print("")



