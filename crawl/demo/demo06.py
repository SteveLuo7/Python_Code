import ssl
from random import choice
from urllib.request import Request,urlopen


url = 'http://httpbin.org/get'

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)2",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)3",
]

header = {
        "User-Agent": choice(user_agents)
    }

req = Request(url,headers=header)
resp = urlopen(req)
print(resp.read().decode())