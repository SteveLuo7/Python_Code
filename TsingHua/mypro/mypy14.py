# eval function

s = "print('abcde')"
eval(s)

a = 10
b = 20
c = eval("a+b")

print(c)

dict1 = dict(x=100,y=200)
d = eval("x+y",dict1)
print(d)