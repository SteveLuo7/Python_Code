
def funOut(func):
    print('decorator-1')
    def funIn():
        print('function-Foo')
        func()
    return funIn

def funOut2(func):
    print('decorator-2')
    def funIn():
        print('hello')
        func()
    return funIn


@funOut2
@funOut
def Foo():
    print('Foo function is running')

# foo = funOut(Foo)

Foo()
