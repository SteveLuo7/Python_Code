

def test01():
    print('*' * 8)
    print("luoshibin is millionaire")

print(id(test01()))
print(type(id(test01())))
print(test01())


print('================================')

for i in range(10):
    test01()
    print('This is {}'.format(i))

