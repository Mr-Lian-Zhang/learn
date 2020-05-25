#operator运算符*五大类
#算数运算符+ — * / %
#模运算/取余运算 判断某个数是奇数还是偶数
# a = 4
# print(a%3)

#赋值运算符 = += -=
# a=3
# a+=1#a=a+1
# a-=5#a=a-5
# print(a)

#比较运算符 <, >, <=, >=, !=, ==,六种运算符,多用于判断*******
#结果返回布尔值true flase
# print("hi".upper()=="HI")
# print("hi"=="HI".lower())

#逻辑运算符 and or not
#结果返回布尔值 true flase
#and左右两边都为真才为真，真真为真，有一个为假则为假
#or左右两边都为假才为假，假假为假，有一个为真则为真
# a=10
# b=5
# print(a>=10 and b<=5)
# print(a>100 or b<-100)

#成员运算符 in，not in
a = (1,2,3)
b = {"o":"19","d":"100"}
print(1 in a)
print (3 not in a)
#列表亦是如此，字典判断key
print("o" in b)
