#dict#字典#符号{}
# #字典的key必须是唯一的
# #字典的存储方式：key：values
# a = {"name":"AKUN",
#      "k_age":20,
#      "k_sex":"man",
#      "score":[88.8,99.9,100]}
#
# #字典的取值[key]
# # print(a["name"])
# print(a.values())#获取字典里的values
# print(a.keys())#获取字典里的keys
#
# # #删除 pop（key），指明删除的值(可将删除的值赋给新的变量)
# # res = a.pop("score")
# # print(a)
# # print(res)
#
# #新增 a[新key]=value
# # a["looks"] = "cool"
# # print(a)
#
# #修改 a[已存在的值]=news values
# a["k_age"] = 18
# print(a)
#高阶函数sorted，对字典进行排序
dict1={"a":4,"b":5,"c":6,"d":7}
dict2=sorted(dict1)
print(dict2)
