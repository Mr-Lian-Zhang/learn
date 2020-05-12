#接口自动化需要用到的第三方库：request
#导入第三方库
import requests
res=requests.get('接口地址')#get请求
res=requests.post('接口地址','data')
data={'username':'lian','pwd':'123'}
#打印返回的文本
print(res.text)
#打印信息头
print(res.headers)
#打印cookies
print(res.cookies)

