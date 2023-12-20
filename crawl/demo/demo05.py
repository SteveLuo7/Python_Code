import ssl
from urllib.request import Request,urlopen


url = 'https://www.12306.cn/index/'

header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

req = Request(url,headers=header)
#   忽略ssl证书
context = ssl._create_unverified_context()
resp = urlopen(req,context=context)
print(resp.read().decode())