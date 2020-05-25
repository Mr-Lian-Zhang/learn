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
            print("响应报文",res.json())
        elif method.lower()=='post':
            res=requests.post(url,data=data,headers=headers)
            print("响应报文", res.json())
            print(res.request.headers)
        else:
            print("不支持此类型请求方式！")
        return res#返回接口的消息实体
if __name__ == '__main__':
    #登录
    http=HttpRequest()
    login_url="https://simple.looklookfactory.com/api/blade-auth/oauth/token"
    login_headers = {"Authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0", "Tenant-Id": "559444"}
    login_data = {"tenantId": "559444", "username": "TEST", "password": "123456", "grant_type": "password", "scope": "all",
            "type": "account"}
    print("登录")
    http.http_request('post', login_url, login_data, login_headers)
############################################################################
   #获取客户列表页
    headers={"Authorization":"Basic c2FiZXI6c2FiZXJfc2VjcmV0",
             "Content-Type":"application/json;charset=UTF-8",
              "Blade-Auth":""
                           "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiI1NTk0NDQiLCJ1c2VyX25hbWUiOiJURVNUIiwiYXZhdGFyIjoiIiwiYXV0aG9yaXRpZXMiOlsidGVzdCJdLCJjbGllbnRfaWQiOiJzYWJlciIsInJvbGVfbmFtZSI6InRlc3QiLCJsaWNlbnNlIjoicG93ZXJlZCBieSBibGFkZXgiLCJ1c2VyX2lkIjoiMTI0MzA1MjkxNjM3MDgxNzAyNSIsInJvbGVfaWQiOiIxMjQzMDQ2ODc0NDQyMjIzNjE3Iiwic2NvcGUiOlsiYWxsIl0sIm5pY2tfbmFtZSI6IlRFU1QiLCJhdGkiOiI1N2U0YzJkZS1kYWJmLTQ1YzAtYmRkYi1iZWE2ZTc0MGI1MzUiLCJleHAiOjE1OTA2NjUzMzMsImRlcHRfaWQiOiIxMjQzMDUzMTc5NzkzOTUyNzcwIiwianRpIjoiMWJkZWIyNGYtOWMxOC00Mzk1LTgxZTktOWQ0OWZkNDA2OWRkIiwiYWNjb3VudCI6IlRFU1QiLCJlbWFpbCI6IiJ9.tgoVIhz4qclLpAPnXyXmNwte5Wt8b7u76VwUCl5gB8I"}
    # kehu_url = "https://simple.looklookfactory.com/api/blade-custom/custInfo/leftContent"
    # print("客户列表")
    # http.http_request('get', kehu_url, headers=headers)
    email_url="https://simple.looklookfactory.com/api/blade-email/emailInfo"
    email_data={"addresseeEmail":["dengkun_02@163.com"],"emailCarbonCopy":[],"emailSecretDelivery":[],"emailHtmlpicList":[],"emailSubject":"这是主题",
                "emailContent":"正文正文","emailReceipt":0,"emaileDelivery":0,"monocular":0,"emailTrack":1,"emailSendTiming":"","senderEmail":"dengkun_01@163.com","senderNickName":"TEST","boxId":"","emailOriginalId":"","isCarbonCopy":false,"isSecretDelivery":false,"sendType":""}
    print("发送邮件")
    http.http_request('post',email_url,email_data,headers=headers)


