from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("My first GUI Application")
root.geometry("500x300+100+100")

btn01 = Button(root)
btn01['text'] = 'Give me flowers'

btn01.pack()


def songhua(e):
    messagebox.showinfo("Message", "Give you a flowers and kiss me ")
    print("Give you 99 flowers")


btn01.bind("<Button-1>", songhua)
root.mainloop()
