from random import choice
from urllib.request import urlopen
from urllib.request import Request


url = 'http://www.baidu.com'
user_agents = [
    'ua1',
    'ua2',
    'ua3',
    'ua4',
]

print(choice(user_agents))

#   定义UA
header = {
    "User-Agent":choice(user_agents)
}


#   封装request对象
req = Request(url, headers=header)

# resp = urlopen(req)

# print(resp.read().decode())

print(req.get_header("User-agent"))