'''closure'''
def sum(a,b):
    return a + b

def funOut(num1):
    def funIn(num2, num1=None):
        num1+=100
        return num2 + num1
    return funIn

funIn = funOut(100)
print(type(funIn))

