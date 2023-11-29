f = lambda a,b,c:a+b+c
print('2+3+4',f(2,3,4))

L = map(lambda x:x*x,[1,2,3,4,5,6,7])
print(list(L))

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


stu1 = Student('luoshibin',28)
stu2 = Student('cristiano',26)
stu3 = Student('leo',27)
result_list = sorted([stu1,stu2,stu3],key=lambda x:x.age)
for stu in result_list:
    print('name:',stu.name)
    print('age:',stu.age)

