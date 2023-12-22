import requests
from fake_useragent import UserAgent

url = 'http://www.baidu.com/s'
args = {
    "wd":"快代理"
}
headers = {
    "User-Agent": UserAgent().chrome
}
resp = requests.get(url,params=args,headers=headers)
resp.encodeint = 'utf-8'
print(resp.text)