class Student:

    def __init__(self,name,score): #self must be first obj
        self.name = name
        self.score = score

    def say_score(self):
        print('{}的分数为:{}'.format(self.name,self.score))


s1 = Student("Cristiano", 720)
s1.say_score()

s1.age = 38
s1.salary = 3000000

print(s1.age)

s2 = Student('messi',200)
s2.say_score()
print('================')
Student.say_score(s2)

stu2 = Student
s3 = stu2('luoshibin',100)
s3.say_score()

