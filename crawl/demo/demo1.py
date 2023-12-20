from urllib.request import urlopen
#   url visited
url = 'http://www.baidu.com'
#   send request

response = urlopen(url)
#   read
info = response.read()

#   print

# print(info.decode())
print(response.getcode())

print('-----------------------')

print(response.geturl())

print('-----------------------')

print(response.info())
