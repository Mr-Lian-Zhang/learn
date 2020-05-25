#coding:utf-8
import requests
class HttpRequest:
    def http_request(self,url,data,method,cookie=None):
        if method.lower()=='get':
            res=requests.get(url,data,cookies=cookie,verify=False)
        else:
            res=requests.post(url,data,cookies=cookie,verify=False)
        return res
if __name__ == '__main__':
    url="https://www.ketangpai.com/UserApi/login"
    data = {"email": "15839412586@163.com", "password": "lzy123456", "remember": 0}  # 需要传的参数
    res = HttpRequest().http_request(url, data, "post")  # 调用
    print("登录结果是{0}".format(res.json()))
    print("课堂派登录的cookie是{0}".format(res.cookies))
    print("状态是",res.json()["status"])