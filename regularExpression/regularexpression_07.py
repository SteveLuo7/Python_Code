print('d:\\a\\b\\c')
print('\nabc')
print('\\nabc')
print('\t123')
print('\\t123')

import re
s = '\\t123'
pattern = '\\\\t\d*'
o = re.match(pattern,s)
print(o)

