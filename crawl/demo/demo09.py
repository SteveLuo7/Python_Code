import ssl
from random import choice
from urllib.parse import urlencode
from urllib.request import Request, urlopen, build_opener, ProxyHandler
from fake_useragent import UserAgent

url = 'https://weibo.com/login.php'
form_data = {
    "user":"291581211",
    "password": "Luo010495"
}

headers = {
    "User-Agent": UserAgent().chrome,
    "Cookie": "SUB=_2AkMSH_h1f8NxqwFRmfoUzWvrb49yzgHEieKkQwmuJRMxHRl-yT9vqnQItRB6OZ_Wmq_-YK-JPU5Jan9QqoAJ7h6y8xxz; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WF9B40S5LaUGBCY8bAyFAU5; _ga_B61YQPGY9T=GS1.1.1700329724.1.0.1700329724.0.0.0; _ga_7WMZ8XEWGJ=GS1.1.1700329724.1.0.1700329724.0.0.0; _ga_QZXMWYY4QK=GS1.1.1700329724.1.0.1700329724.60.0.0; _ga_DL2CM4NHWS=GS1.1.1700329724.1.0.1700329724.0.0.0; __gads=ID=5954b5a8bc9c4736:T=1700329725:RT=1700329725:S=ALNI_Ma-wxchWQzINwoTwDH8FrCLXDjiMQ; __gpi=UID=00000c8d50d9cf95:T=1700329725:RT=1700329725:S=ALNI_Maycl_WL3yRVeGaPbzrBkifJvcZ2w; _ga=GA1.2.1374486924.1700329725; SINAGLOBAL=5905927805129.531.1700382028465; ULV=1701153470719:2:2:1:5219563811018.861.1701153470717:1700382028467"
}

req = Request(url,headers=headers,data=urlencode(form_data).encode())
# handler = ProxyHandler({'http':'name:password@ip:port'})

resp = urlopen(req)
print(resp.read().decode())