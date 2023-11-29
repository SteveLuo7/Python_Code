'''
    often use dic
'''
import re

print("===================================")
s = 'a'
s = 'A'
s = '8'
s = '_'
pattern = '.'
o = re.match(pattern, s)
print(o)
print("===============\d====================")
s = '0'
s = '5'
# s = 'a'
pattern = '\d'
o = re.match(pattern, s)
print(o)
