import requests
from bs4 import BeautifulSoup


url = "https://finance.yahoo.com/?guccounter=1"
html = requests.get(url).text

soup = BeautifulSoup(html,'lxml')
print(soup.title)
print(soup.div.get('class'))
print(soup.a['href'])