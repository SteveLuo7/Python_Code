import copy

class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen


class CPU:
    def caculate(self):
        print("1234556")
        print("cpu",self)

class Screen:
    def show(self):
        print("Show aminuosi")
        print("screen: ", self)

c1 = CPU()
c2 = c1
print(c1)
print(c2)
s1 = Screen()
m1 = MobilePhone(c1,s1)
m2 = copy.copy(m1)

print("=====================")
print(m1,m1.cpu,m1.screen)
print(m2,m2.cpu,m2.screen)