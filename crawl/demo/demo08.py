import ssl
from random import choice
from urllib.request import Request, urlopen, build_opener, ProxyHandler
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'

headers = {
    "User-Agent": UserAgent().chrome
}

req = Request(url,headers=headers)
# handler = ProxyHandler({'http':'name:password@ip:port'})
handler = ProxyHandler({'http':'27.184.145.168:21212'})
opener = build_opener(handler)
resp = opener.open(req)
print(resp.read().decode())