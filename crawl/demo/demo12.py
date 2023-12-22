import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pyquery import pyquery as pq

url = "https://www.qidian.com/rank/yuepiao/year2023-month12-page2/"
headers = {
    "User-Agent": UserAgent().chrome
}
resp = requests.get(url,headers=headers)

doc = pq(resp.text)
names = [a.text for a in doc('h4 a')]
authors_a = doc('.author a')
i = 0
for num in range(len(authors_a)):
    print(num)
