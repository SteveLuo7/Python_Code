class CarFactory:

    __obj = None
    __init_flag = True

    def create_car(self,brand):
        if brand == "Benz":
            return Benz()
        elif brand == "BMW":
            return BMW()
        elif brand == "BYD":
            return BYD()
        else:
            return "NONE"

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self):
        print("init....CarFactory")
        CarFactory.__init_flag = False


class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

factory = CarFactory()
c1 = factory.create_car("Benz")
c2 = factory.create_car("BYD")
print(c1)
print(c2)

print("========================================")
factory2 = CarFactory()
print(factory)
print(factory2)