# #招10-12岁女足球员，性别：男x，女y。询问十次后，输出满足条件的总人数
# a = 1
# sum = 0
# while a<=10:
#     age = int(input("请问你的年龄是："))
#     sex = input("请问你的性别是：")
#     a=a+1
#     if 10<=age<=12 and sex=="x":
#         print("符合")
#         sum+=1
#     else:
#         print("不符合")
# print("本次共询问人数为{1}，符合条件人数为{0}".format(sum,a))

#例如：passwd={"andmin":"123456","user1":"111111"}
#1.设计一个登录程序，不同的用户名和对应的密码在同一个字典里面，输入正确的用户名和密码进行登录
#2.首先输入用户名，如果用户名不存在或者为空，则一直提示输入正确的用户名
#3.当用户名正确时，提示去输入密码，如果密码跟用户名不对应，则提示密码错误请重新输入
#4.如果密码错误超过三次，中断程序运行
#5.当输入密码错误时，提示还剩余几次机会
#6.用户名和密码都正确时，提示登录成功！
passwd = {"admin":"123456","user1":"111111"}
s = 3
while True:
        u = input("请输入用户名：")
        if u in passwd:
            print("用户名正确")
            while s > 0:
                  p = input("请输入密码：")
                  if passwd[u]==p:
                      print("登录成功！")
                      s-=100
                  else:
                      s-=1
                      print("密码错误，请重新输入,剩余{0}次机会".format(s))
            break
        else:
            print("用户名错误，请重新输入")





