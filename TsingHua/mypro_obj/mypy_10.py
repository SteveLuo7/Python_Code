class People:

    def eat(self):
        print("WOW,delicous")



class Chinese(People):

    def eat(self):
        super().eat()
        print("Eating with sticks")

class English(People):
    def eat(self):
        super().eat()
        print("Eating with forks")

class Indian(People):
    def eat(self):
        super().eat()
        print("Eating with hands")

def peopleEat(m):
    if isinstance(m,People):
        m.eat()
    else:
        print("NO EATING")

peopleEat(Indian())