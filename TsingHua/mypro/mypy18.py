# 测试nolocal global

def outer():
    b = 10

    def inner():
        nonlocal b
        print('outer:',b)
    inner()
outer()