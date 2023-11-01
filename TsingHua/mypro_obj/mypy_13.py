class A1:
    def sayA1(self):
        print("I am A1 ")


class B1(A1):
    pass


x = B1()

x.sayA1()

print("-----------------")

class A2:
    def sayA2(self):
        print("i am A2")

class B2:
    def __init__(self,a):
        self.a = a
a2 = A2()
y = B2(a2)
y.a.sayA2()