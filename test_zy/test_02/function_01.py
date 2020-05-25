#函数强化练习function-1 and function-2
#内置函数
#函数的特点：可以重复使用
#函数的语法：def  关键字
#函数名的规范：不能以数字开头，小写字母，不同的字母之间要用下划线隔开
#语法：
#def 函数名（）：
    #函数体      #具体实现的功能
#调用：函数名

# def d_k(age):#d_k(age)形参/位置参数   #age=20默认参数
#     print("{0}别留遗憾了。".format(age))
# d_k("昨天")#实参
# d_k("今天")
# d_k("明天")

# #请把1-100的数字相加，写成一个函数
# def sum():
#     a=0
#     for b in range(101):
#         a+=b
#     print("1-100数字相加和为{0}".format(a))
# sum()

#功能写成函数方法
#1.先用代码实现功能，还可以选取一组数据证明自己的diamante是否正确
#2.变成函数，加def
#3.想办法提高代码的复用性

#复用拓展：
#利用range函数求任意范围内所有整数的和
# def sum(m,n,k=2):#k=1为默认参数，不进行赋值默认就为1，mn为形参，默认参数必须放在位置参数的后面
#
#     a=0
#     for b in range(m,n,k):
#         a+=b
#     print("相加和为{0}".format(a))
# sum(1,10)#可进行指定参数赋值，比如m=1
# #不指定默认按顺序赋值

#return 当你调用这个函数的时候，就会返回一个值,return后面的表达式
#在函数里面，return相当与一个结束符合，表示到此位置，后面的代码不会被执行
# def sum(m,n,k=2):
#
#     a=0
#     for b in range(m,n,k):
#         a+=b
#     return a
# print(sum(1,10))
#
#联系题：写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
# k=[1,3,3,4]
# def list(l):
#      if len(l)>2:
#             new_list = l[0:2]
#      return new_list
#
# print(list(k))#实参为k
#
# #动态参数/不定长参数 *args （缩写arguments）其他的也行（*a，*b，*c，）
#在函数内部 作为元组来传递
def make_sandwich(*args):
    all=""
    for item in args:
        all+=item
        all+=','
    print("你的三明治里面包含了"+all)
make_sandwich('鸡蛋','牛排','培根','番茄酱')
# #求任意数字的和
# def add_sum(*l,a):#可以组合混用（*l,a,**k)
#     sum=0
#     for item in (l):
#         sum+=item
#     print("和为",sum)
#     print('常量值为',a)
# add_sum(1,2,3,4,a=3)

# #关键字函数 key-value **kwargs （key word） 必须加**/其他的也行（**a，**b，**c，）
# #在函数里面体现为字典
def kw_function(**kwargs):
    print(kwargs)
kw_function(x=1,y=2)

##############################################拓展######################################
# # 复用拓展：
# # 利用range函数求任意范围内所有整数的和
# def sum(m,n,k=1):
#     a=0
#     for b in range(m,n,k):
#         a+=b
#     print("相加和为{0}".format(a))
# def sub(a,b):
#     print(a-b)
# if __name__ == '__main__':
#     sub(7,4)
#
# #if __name__ == '__main__':测试代码，检测运行/主程序的执行入口，只有在当前模块下执行的时候，才会执行下面的代码
# if __name__ == '__main__':
#  sum(1,101)
#  print("hhhhhhhh")



