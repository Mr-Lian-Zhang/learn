#控制语句 分流分支 循环语句 for while
#判断语句 if elif else 关键字
#if （比较 逻辑 成员）均可 2.字符串，列表，元组，字典，空数据==false 非空数据==true
# age = 20
# if age > 18:#当if后面的语句 满足条件，运行结果是true，那就会执行他的子语句
#     print("你已经成年了。")

#if 条件语句：
#   子语句
#elif 条件语句：（可存在多个elif）
    #子语句
#else： #后不能添加条件语句
#   子语句
#input（）函数，从控制台获取数据，获取的数据都为字符串类型
#对控制台输入类型做判断关键函数：isdigtal
# age = int (input("你的年龄是："))#input输入字符类型默认为str，要做int类型转换
# # age = -10
# if age>18:
#     print("你已经成年了")
# elif age<=18 and age>=0:
#     print("你还小")
# else:
#     print("你还没出生")
print(type(input("你的年龄是：")))#类型判断