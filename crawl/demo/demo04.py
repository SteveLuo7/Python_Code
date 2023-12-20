from random import choice
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import quote


def get_html(url):
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    request = Request(url,headers=header)

    resp = urlopen(request)
    return resp.read().decode()


def save_html(html,filename):
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)


def main():
    content = input('Do you want to search for what?')
    num = int(input('please input the number page you want'))
    for i in range(num):

        url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(quote(content),(i*50))
        print(url)
        html = get_html(url)
        filename = 'NO.'+str(i+1)+'Page.html'
        save_html(html,filename)



if __name__ == '__main__':
    main()
