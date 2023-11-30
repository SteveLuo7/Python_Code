import re
# pattern = '\d\d\d\d\d\d\d\d\d\d\d'
pattern = "1[35789]\d\d\d\d\d\d\d\d\d"
s = '18688206601'
o = re.match(pattern,s)

print(o)