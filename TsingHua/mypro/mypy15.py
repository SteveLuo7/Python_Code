def test01(n):
    print('test01:',n)
    if n == 0:
        print('over')
    else:
        test01(n-1)
    print('test01*********',n)

def test02():
    print('test02')

test01(4)