import re

pattern = r'[xyz]'
s = 'y'
o = re.match(pattern,s)
print('Use list[] :',o)


pattern  = r'x|y|z'
s = 'y'
o = re.match(pattern,s)
print('Choose one|:',o)
print('')

pattern = r'[ab][cd]'
s = 'ac'
o = re.match(pattern,s)
print(o)

pattern = r'ab[cd]'
s = 'abd'
o = re.match(pattern,s)
print(o)