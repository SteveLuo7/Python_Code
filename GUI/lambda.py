from tkinter import *

root = Tk();root.geometry("270x50")

def mouseTest1():
    print("command function: NOT about event obj")

def mouseTest2(a,b):
    print("{},{}".format(a,b))

Button(root, text="test Command1",
        command=mouseTest1).pack(side="left")
Button(root, text="test Command2",
        command=lambda : mouseTest2("steve","luo")).pack(side="left")

root.mainloop()


