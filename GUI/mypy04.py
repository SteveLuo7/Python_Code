from tkinter import *
from tkinter import messagebox
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self,text="Username")
        self.label01.pack()

        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get());print(self, self.entry01.get())

        self.btn01 = Button(self,text="Login",command=self.login)
        self.btn01.pack()

    def login(self):
        print("Username: " + self.entry01.get())
        messagebox.showinfo("Login Sucess")

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300+100+200")
    app = Application(master=root)
    root.mainloop()