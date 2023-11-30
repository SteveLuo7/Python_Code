import re
qq = '291581211@qq.com'
pattern = '[1-9]\d{4,9}@qq.com$'
o = re.match(pattern,qq)
print(o)

print('----------^---------------')
# s = 'hello world'
s = 'hello python'
pattern = r'^hello.*'
o = re.match(pattern,s)
print(o)

print('----------\b left---------------')
pattern = r'.*\bab'
s = '123 ab'
o = re.match(pattern,s)
print(o)

print('----------\b right---------------')
pattern = r'.*ab\b'
s = '123 ab'
o = re.match(pattern,s)
print(o)

print('----------\B---------------')
pattern = r'.*ab\B'
s = '123 ab'
o = re.match(pattern,s)
print(o)
