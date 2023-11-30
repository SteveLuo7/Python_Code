'''
*
?
{m}
{m,n}

'''

import re
print('---------------------*re-------------------------')
pattern = '\d*'
s = '123qwe'
s = '123456qwe'
s = 'qwe'
o = re.match(pattern,s)
print(o)

print('-------------{}-------------------------')
pattern = '\d{m}'
s = '123qwe'
o = re.match(pattern,s)
print(o)

print('-------------{m,n}-------------------------')
pattern = '\d{2,5}'
s = '123qwe'
o = re.match(pattern,s)
print(o)
