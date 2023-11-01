a = [10,20]
print(id(a))
print(a)
print('=============================')

def test01(m):
    print(id(m))
    m.append(300)
    print(id(m))


test01(a)

print(a)

b = 100
def f1(n):
    print("n:",id(n))
    n = n+200
    print("n:",id(n))
    print(n)

f1(b)