import re
print('-----------sub and subn------------')
phone = "2004-959-559 # This is national telephone number"
pattern = r'#.*$'
result = re.sub(pattern,'',phone)
print('sub: ',result)

pattern = r'#\D*'
result = re.sub(pattern,'',phone)
print('sub-',result)


print('------------subn--------------')
result = re.subn(pattern,'',phone)
print(result)