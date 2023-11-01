class Workers:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if 18<age<50:
            self.__age = age
        else:
            print("OOPS Somthing Wrong")

emp1 = Workers('cristiano',38)
print(emp1.get_age())
emp1.set_age(15)
print(emp1.get_age())
