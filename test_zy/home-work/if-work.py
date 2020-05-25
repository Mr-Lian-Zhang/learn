#1
price = int(input("此次消费为："))
if 50<= price <=100:
    print("折扣10%，"+"折扣后价格为："+str(int(price*(1-0.1))))
elif price>100:
    print("折扣20%，""折扣后价格为："+str(int(price*(1-0.2))))
else:
    print("您的消费为满足优惠条件，此次消费金额为："+str(price))

#2
# import random
# n = random.randint(1,9)#引用random，生成随机整数
# m = int(input("输入数字来比较："))
# print("随机数字为{0}".format(n))
# if m>n:
#     print("bigger")
# elif m<n:
#     print("less")
# else:
#     print("equal")

