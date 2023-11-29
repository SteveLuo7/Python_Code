import re

s = 'hello python'
pattern = 'hello'
o=re.match(pattern,s)

print(o)

print(dir(o))

print(o.group())
print(o.span())
print(o.start())

o = re.match(pattern,s,flags=re.I)
print(o)
print(s)
print(pattern)
print(o.group())