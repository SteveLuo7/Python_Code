import re
pattern = 'hello'
s = 'hello python'

m = re.match(pattern,s)
print(m)
print(m.group())

s = re.search(pattern,s)
print(s)

print('-----------match and search-----------')
