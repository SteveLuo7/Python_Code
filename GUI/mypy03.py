from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self,text="Luoshibin", width=10, height=3, bg="blue", fg="purple")
        self.label01.pack()
        self.label02 = Label(self,text="罗仕斌", width=20, height=5)
        self.label02.pack()
        self.label02 = Label(self, text="GuangDong\nGuangZhou\nLuoshibin", borderwidth=1,relief="solid",justify="right")
        self.label02.pack()

root = Tk()
root.geometry("800x600+300+200")
root.title("GUI Application")
app = Application(master=root)

root.mainloop()
