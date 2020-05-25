#coding:utf-8
import  requests,json#'''导入requests模块'''
import urllib3
urllib3.disable_warnings()
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
class HttpRequest:#利用request模块封装get与post请求'''
    def http_request(self,url,data,method,cookie=None):
        if  method.lower()=="get":
            xuexi = requests.get(url, data, cookies=cookie, verify=False)  # 响应结果的消息实体
        else:
            xuexi=requests.post(url,data,cookies=cookie,verify=False)#响应结果的消息实体
        return xuexi
        #返回一个消息实体
if __name__=='__main__':
    login_url="https://www.ketangpai.com/UserApi/login"#登陆的url
    data={"email":"15839412586@163.com","password":"lzy12345","remember":0}#需要传的参数
    res=HttpRequest().http_request(login_url,data,"post")#调用
    print("登录结果是{0}".format(res.json()))
    print("课堂派登录的cookie是{0}".format(res.cookies))
