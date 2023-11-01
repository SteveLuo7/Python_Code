import copy

a = [10,20,[5,6]]
b = copy.copy(a)

print('a:',a)
print('b:',b)

b.append(30)
b[2].append(7)


print('copy...')

print('a:',a)
print('b:',b)


def testCopy():
    a = [10,20,[5,6]]
    b = copy.deepcopy(a)
    print('a:',a)
    print('b:',b)

    b.append(30)
    b[2].append(7)
    print("deepCOPY...")

    print('a:',a)
    print('b:',b)

    return

testCopy()

