#python来完成http请求
#requests第三方库
import requests
# #get请求
# url="https://simple.looklookfactory.com/api/blade-custom/custInfo/leftContent"
# headers={"Authorization":"Basic c2FiZXI6c2FiZXJfc2VjcmV0",
#                               "Blade-Auth":"bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiI1NTk0NDQiLCJ1c2VyX25hbWUiOiJNTCIsImF2YXRhciI6Ii"
#                                            "IsImF1dGhvcml0aWVzIjpbImFkbWluIl0sImNsaWVudF9pZCI6InNhYmVyIiwicm9sZV9uYW1lIjoiYWRtaW4iLCJsaWNlbnNlIjoicG93ZXJl"
#                                            "ZCBieSBibGFkZXgiLCJ1c2VyX2lkIjoiMTIxMTYxNDgwOTI2ODQwNDIyNiIsInJvbGVfaWQiOiIxMjExNjE0MjUyMTQyOTQ0MjU3Iiwic2NvcG"
#                                            "UiOlsiYWxsIl0sIm5pY2tfbmFtZSI6Ik1MIiwiYXRpIjoiYTQwOTQ1YTktYTAyMi00YmZlLThkMzQtZTg4MmI0Mjc3NmNjIiwiZXhwIjoxNTk"
#                                            "wNDk5MzQyLCJkZXB0X2lkIjoiMTIxMTYxNDI1MjE1OTcyMTQ3NCIsImp0aSI6ImIxZDlhMzZlLThmMzYtNGFjOC1iYjE3LTI3NTlkYTJhM2MzY"
#                                            "SIsImFjY291bnQiOiJNTCIsImVtYWlsIjoiIn0.dfqpOhtaUBMMnUrwm82OkIXIq3X42m8YwgGLIDh8WiE"}
# res=requests.get(url,headers=headers)#返回的是个消息实体
# #消息实体拆分：响应头，响应状态码，响应正文
# print("响应头",res.headers)
# print("响应状态码",res.status_code)
# print("响应正文",res.text)#json格式

# #post请求
url="https://simple.looklookfactory.com/api/blade-auth/oauth/token"
h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
   "Authorization":"Basic c2FiZXI6c2FiZXJfc2VjcmV0","Tenant-Id":"559444"}#代理User-Agent伪装（反爬虫）
data={"tenantId":"559444","username":"ML","password":"123456","grant_type":"password","scope":"all","type":"account"}
run=requests.post(url,data,headers=h)
# print("响应头",run.headers)
# print("响应状态码",run.status_code)
# print("响应正文",run.json())#json格式
print("响应头",run.headers,"\n响应状态码",run.status_code,"\n响应正文",run.json())
print(run.request.headers)#获取请求头里面的headers
##如果说有cookies
# print("cookies",run.cookies)#类字典形式 可以根据key取值
# print("cookeies",run.cookies["JSESSIONID"])
#如果说登录接口返回的有cookies，并且其他接口要用到cookies，
# 在其他接口的请求中加入不定长参数cookie=run.cookies

#https不想认证，关键字参数直接传verify=False


