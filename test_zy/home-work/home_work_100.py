#1.题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# sum=""
# count=0
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b!=c:
#                 sum+=str(a*100+b*10+c)+str(",")
#                 count+=1
# print("能组成互不相同而且无重复的数字有{0}个，是{1}".format(count,sum))
#2.输出九九口诀

# for a in range(1,10):
#     for b in range(1,a+1):
#         print(str(a),"*",str(b),"=",str(a*b))

# for a in range(1,10):
#     for b in range(1,a+1):
#         print("{0} * {1} = {2}  ".format(a,b,a*b),end='')
#     print('')
# for a in range(6):
#     print(a)
#写函数，将姓名，性别，城市作为参数《并且性别默认为f（女），如果城市是在长沙并且性别为女，则输出姓名，性别
#城市，并返回true，否则返回flasec

# def dk(x,c,f="女"):
#     if f=="女" and  c== "长沙":
#         print(x,f,c)
#         print("女" in f)
#     else:
#         print("falase")
# dk(x = input("请输入你的姓名："),f = input("请输入您的性别"),c = input("请输入你所在的城市："))

# #写一个软件测试工程师类，要求有属性，有函数，并完成属性和函数的调用
# class Test:
#     a = "25"
#     b = "qa"
#     def aq(self):
#         print("安全测试工程师")
#     def zdh(self):
#         print("自动化测试工程师")
# qa = Test()
# print(qa.a)
# qa.aq()

################################################################################
import requests
class ErpHttp:
    def ligon(self):
        url = "https://simple.looklookfactory.com/api/blade-auth/oauth/token"
        h = {"Authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0", "Tenant-Id": "559444"}
        data = {"tenantId": "559444", "username": "ML", "password": "123456", "grant_type": "password", "scope": "all",
                "type": "account"}
        run = requests.post(url, data, headers=h)
        print("响应头", run.headers)
        print("响应状态码", run.status_code)
        print("响应正文", run.json())  # json格式
    def kehu(self):
        self.ligon()
        url = "https://simple.looklookfactory.com/api/blade-custom/custInfo/leftContent"
        headers = {"Authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0",
                   "Blade-Auth": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiI1NTk0NDQiLCJ1c2VyX25hbWUiOiJNTCIsImF2YXRhciI6Ii"
                                 "IsImF1dGhvcml0aWVzIjpbImFkbWluIl0sImNsaWVudF9pZCI6InNhYmVyIiwicm9sZV9uYW1lIjoiYWRtaW4iLCJsaWNlbnNlIjoicG93ZXJl"
                                 "ZCBieSBibGFkZXgiLCJ1c2VyX2lkIjoiMTIxMTYxNDgwOTI2ODQwNDIyNiIsInJvbGVfaWQiOiIxMjExNjE0MjUyMTQyOTQ0MjU3Iiwic2NvcG"
                                 "UiOlsiYWxsIl0sIm5pY2tfbmFtZSI6Ik1MIiwiYXRpIjoiYTQwOTQ1YTktYTAyMi00YmZlLThkMzQtZTg4MmI0Mjc3NmNjIiwiZXhwIjoxNTk"
                                 "wNDk5MzQyLCJkZXB0X2lkIjoiMTIxMTYxNDI1MjE1OTcyMTQ3NCIsImp0aSI6ImIxZDlhMzZlLThmMzYtNGFjOC1iYjE3LTI3NTlkYTJhM2MzY"
                                 "SIsImFjY291bnQiOiJNTCIsImVtYWlsIjoiIn0.dfqpOhtaUBMMnUrwm82OkIXIq3X42m8YwgGLIDh8WiE"}
        res = requests.get(url, headers=headers)  # 返回的是个消息实体
        # 消息实体拆分：响应头，响应状态码，响应正文
        print("响应头", res.headers)
        print("响应状态码", res.status_code)
        print("响应正文", res.json())  # json格式
a=ErpHttp()
# a.ligon()
a.kehu()
