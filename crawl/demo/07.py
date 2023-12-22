from urllib.request import Request, urlopen, build_opener

from fake_useragent import UserAgent

url = 'http://httpbin.org/get'

header = {
        "User-Agent": UserAgent().chrome
    }

req = Request(url,headers=header)

# resp = urlopen(req)
opener = build_opener()
resp = opener.open(req)
print(resp.read().decode())

