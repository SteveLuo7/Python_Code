class Person:

    def __init__(self,name):
        self.name = name

    def __add__(self, other):
        if isinstance(other,Person):
            return "{} -- {}".format(self.name,other.name)
        else:
            return "NO THE SAME, NO ADD "

    def sayhi(self):
        print("My name is {}".format(self.name))


p1 = Person("Cristaino")
p2 = Person("Benzema")

x = p1 + p2
print(x)
p1.sayhi()

print(x * 5)