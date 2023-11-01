class Person:

    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def say_age(self):
        print("我的年龄是多少{}".format(self.__age))

class Student(Person):

    def __init__(self,name,age,score):
        Person.__init__(self,name,age)
        self.score = score


# print(Student.mro())

s = Student("Cristiano",38,200)
s.say_age()
print(s._Person__age)