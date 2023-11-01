class Workers:

    __company = "realMadrid"

    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def __work(self):
        print('GOAL!!!')
        print('age,{}'.format(self.__age))
        print(Workers.__company)

    def play(self):
        print('playing football game')


e = Workers('crsitiano',38)

print(e._Workers__age)

e._Workers__work()

print("外部调用{}".format(Workers._Workers__company))

e.play()
