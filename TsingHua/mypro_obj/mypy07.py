class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age


    def say_age(self):
        print("我的年龄是： {}".format(self.__age))

    def say_introduce(self):
        print("我的名字是： {}".format(self.name))

class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)
        self.score = score

    def say_introduce(self):
        print("Hello Teacher, My name is {}".format(self.name))


a = Person('cristiano',38)
b = Student('messi',36,0)
a.say_introduce()
b.say_introduce()
print(b.score)
b.say_age()