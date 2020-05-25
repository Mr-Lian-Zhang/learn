import requests
#
class HttpRequest:
    def http_request(self,method,url,data=None,headers=None):
        '''method：请求的的方式，支持get post
        url：请求的地址
        data：传递的参数，非必填参数，字典的格式传递参数
        headers 请求头，字典格式'''
        if method.lower()=='get':
            res = requests.get(url, data=data, headers=headers)
        elif method.lower()=='post':
            res=requests.post(url,data=data,headers=headers)
        else:
            print("不支持此类型请求方式！")
        return res#返回接口的消息实体
if __name__ == '__main__':
    #登录
    http=HttpRequest()
    url="https://simple.looklookfactory.com/api/blade-auth/oauth/token"
    headers = {"Authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0", "Tenant-Id": "559444"}
    data = {"tenantId": "559444", "username": "TEST", "password": "123456", "grant_type": "password", "scope": "all",
            "type": "account"}
    res_1=http.http_request('post',url,data,headers)
    print("登录响应报文",res_1.json())
   #获取客户列表页
    url = "https://simple.looklookfactory.com/api/blade-custom/custInfo/leftContent"
    headers={"Authorization":"Basic c2FiZXI6c2FiZXJfc2VjcmV0",
                                  "Blade-Auth":"bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiI1NTk0NDQiLCJ1c2VyX25hbWUiOiJURVNUIiwiYXZhdGFyIjoiIiwiYXV0aG9yaXRpZXMiOlsidGVzdCJdLCJjbGllbnRfaWQiOiJzYWJlciIsInJvbGVfbmFtZSI6InRlc3QiLCJsaWNlbnNlIjoicG93ZXJlZCBieSBibGFkZXgiLCJ1c2VyX2lkIjoiMTI0MzA1MjkxNjM3MDgxNzAyNSIsInJvbGVfaWQiOiIxMjQzMDQ2ODc0NDQyMjIzNjE3Iiwic2NvcGUiOlsiYWxsIl0sIm5pY2tfbmFtZSI6IlRFU1QiLCJhdGkiOiI1N2U0YzJkZS1kYWJmLTQ1YzAtYmRkYi1iZWE2ZTc0MGI1MzUiLCJleHAiOjE1OTA2NjUzMzMsImRlcHRfaWQiOiIxMjQzMDUzMTc5NzkzOTUyNzcwIiwianRpIjoiMWJkZWIyNGYtOWMxOC00Mzk1LTgxZTktOWQ0OWZkNDA2OWRkIiwiYWNjb3VudCI6IlRFU1QiLCJlbWFpbCI6IiJ9.tgoVIhz4qclLpAPnXyXmNwte5Wt8b7u76VwUCl5gB8I"}
    res_1=http.http_request('get',url,headers=headers)
    print("客户列表返回的是",res_1.json())

