# lambda

f = lambda a,b,c,d:a*b*c*d



def f1(a,b,c,d):
    return a*b*c*d


print(f1(2,3,4,5))

print(f(2,3,4,5))

print('**************************')


g = [lambda a:a*2, lambda b:b*3]
print(g[0](5))

