import re
pattern = '[A-Z][a-z]*'
s = 'Hello'
o = re.match(pattern,s)
print(o)


print('---------------case2-------------')
pattern = '[a-zA-Z_][a-zA-Z0-9_]*'
# pattern = '[a-zA-Z_]\w*'
s = 'userName'
# s = 'a'
# s = '3er'
o = re.match(pattern,s)
print(o)

print('------------------case3----------------')
pattern = '[1-9]\d?'    #   ? ->  once or multiple
s = "56"
o = re.match(pattern,s)
print(o)

print('------------------case4-------------------')
pattern='\w{8,20}'
# s = '123456789'
s = '123543654#'
o = re.match(pattern,s)
print(o)