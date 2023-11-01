s = input("please input a number")

if int(s) < 10:
    print('s is the number below 10')
else:
    print('s is the number upper 10')

print('s是小于10的数字' if int(s)<10 else 's是大于10的数字')
