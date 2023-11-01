"""测试一个经典的GUI程序的写法，试用面向对象的方式"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的GUI程序"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.btn01 = Button(self)
        self.btn01["text"] = "Click to send flowers"
        self.btn01.pack()
        self.btn01["command"] = self.songhua

        self.btnQuit = Button(self, text="Quit", command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("Send Flowers", "Send you 99 flowers")


root = Tk()
root.geometry("800x600+300+200")
root.title("GUI Application")
app = Application(master=root)

root.mainloop()
