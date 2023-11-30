import re

print('匹配座机号码')
pattern = r'(\d{3,4})-([1-9]\d{4,7}$)'
s ='0379-3658518'
o = re.match(pattern,s)
print(o)
print(o.group())
print(o.group(1))
print(o.group(2))


print('匹配网页标签内数据')
pattern = r'<(.+)><(.+)>.+</\2></\1>'
s = '<html><head>TOP TOPIC</head></html>'
# s = '<html><head>TOP TOPIC</head></body>'
o = re.match(pattern,s)
print(o)


print('起别名')
pattern = r'<(?P<k_html>.+)><(?P<k_head>.+)>.+</(?P=k_head)></(?P=k_html)>'
s = '<html><head>TOP TOPIC</head></html>'
# s = '<html><head>TOP TOPIC</head></body>'
o = re.match(pattern,s)
print(o)

