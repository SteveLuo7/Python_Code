from random import choice
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import quote

args = '皇家马德里'

url = 'http://www.baidu.com/s?wd={}'.format(quote(args))
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

request = Request(url,headers=header)
resp = urlopen(request)

print(resp.read().decode())