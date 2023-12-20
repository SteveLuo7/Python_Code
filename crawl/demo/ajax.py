from urllib.request import Request,urlopen
from time import sleep

# url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='

header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
i  = 0
base_url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=&start={}&limit=20'
while True:

    req = Request(base_url.format(i*20),headers=header)
    resp = urlopen(req)
    info = resp.read().decode()
    if info == '[]':
        break
    else:
        i +=1
    print(info)
    sleep(3)